import { connect } from "cloudflare:sockets";

const SMTP_HOST = "smtp.openxchange.eu";
const SMTP_PORT = 587;
const SMTP_USER = "contact@simetrika.lu";
const RECIPIENT = "contact@simetrika.lu";

function response(status, data) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

function base64Utf8(value) {
  const bytes = new TextEncoder().encode(value);
  let binary = "";
  for (let index = 0; index < bytes.length; index += 0x8000) {
    binary += String.fromCharCode(...bytes.subarray(index, index + 0x8000));
  }
  return btoa(binary);
}

function makeSmtpStream(socket) {
  const reader = socket.readable.getReader();
  const writer = socket.writable.getWriter();
  const decoder = new TextDecoder();
  let buffer = "";

  async function readLine() {
    while (!buffer.includes("\n")) {
      const { value, done } = await reader.read();
      if (done) throw new Error("SMTP connection closed unexpectedly");
      buffer += decoder.decode(value, { stream: true });
    }

    const newline = buffer.indexOf("\n");
    const line = buffer.slice(0, newline).replace(/\r$/, "");
    buffer = buffer.slice(newline + 1);
    return line;
  }

  async function readResponse() {
    const lines = [];
    let code;

    while (true) {
      const line = await readLine();
      lines.push(line);
      const match = /^(\d{3})([ -])/.exec(line);
      if (!match) throw new Error("Invalid SMTP response");

      code = Number(match[1]);
      if (match[2] === " ") break;
    }

    return { code, lines };
  }

  async function sendLine(line) {
    await writer.write(new TextEncoder().encode(line + "\r\n"));
    return readResponse();
  }

  function release() {
    reader.releaseLock();
    writer.releaseLock();
  }

  return { readResponse, sendLine, release };
}

function expectCode(result, accepted) {
  if (!accepted.includes(result.code)) {
    throw new Error(`SMTP rejected command with code ${result.code}`);
  }
  return result;
}

function dotStuff(message) {
  return message.replace(/(^|\r\n)\./g, "$1..");
}

export async function onRequestPost({ request, env }) {
  const origin = request.headers.get("Origin");
  if (origin) {
    let host;
    try {
      host = new URL(origin).hostname;
    } catch {
      return response(403, { error: "origin" });
    }

    const allowedHosts = [
      "simetrika-7wr.pages.dev",
      "simetrika.lu",
      "www.simetrika.lu",
    ];
    if (!allowedHosts.includes(host) && !host.endsWith(".simetrika.pages.dev") && !host.endsWith(".simetrika-7wr.pages.dev")) {
      return response(403, { error: "origin" });
    }
  }

  const contentType = request.headers.get("Content-Type") || "";
  const contentLength = Number(request.headers.get("Content-Length") || 0);
  const maxRequestBytes = 12 * 1024 * 1024;
  if (contentLength > maxRequestBytes) {
    return response(413, { error: "size" });
  }

  let data;
  let photos = [];
  if (contentType.toLowerCase().includes("multipart/form-data")) {
    let formData;
    try {
      formData = await request.formData();
    } catch {
      return response(400, { error: "invalid_form_data" });
    }
    data = {};
    for (const [key, value] of formData.entries()) {
      if (typeof value === "string" && key !== "photos") data[key] = value;
    }
    photos = formData.getAll("photos").filter((value) => value instanceof File && value.size > 0);
  } else {
    const rawBody = await request.text();
    if (new TextEncoder().encode(rawBody).byteLength > 12_000) {
      return response(413, { error: "size" });
    }
    try {
      data = JSON.parse(rawBody);
    } catch {
      return response(400, { error: "invalid_json" });
    }
    if (!data || typeof data !== "object" || Array.isArray(data)) {
      return response(400, { error: "invalid_data" });
    }
  }

  const value = (key, max) =>
    typeof data[key] === "string" ? data[key].trim().slice(0, max + 1) : "";
  const name = value("name", 150);
  const email = value("email", 254);
  const phone = value("phone", 80);
  const project = value("project", 5000);
  const city = value("city", 120);
  const website = value("website", 100);
  const requestedLang = value("lang", 8).toLowerCase();
  const lang = ["fr", "de", "en", "lb"].includes(requestedLang)
    ? requestedLang
    : "fr";

  // Honeypot: silently accept bot submissions without sending email.
  if (website) return response(200, { ok: true });

  if (
    !name ||
    name.length > 150 ||
    !project ||
    project.length > 5000 ||
    city.length > 120 ||
    (!email && !phone) ||
    email.length > 254 ||
    phone.length > 80
  ) {
    return response(400, { error: "validation" });
  }

  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return response(400, { error: "email" });
  }

  if (photos.length > 5) {
    return response(400, { error: "photos_count" });
  }
  const allowedPhotoTypes = new Set([
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/gif",
    "image/avif",
    "image/heic",
    "image/heif",
  ]);
  if (photos.some((file) => !allowedPhotoTypes.has(file.type.toLowerCase()))) {
    return response(400, { error: "photos_type" });
  }
  if (photos.reduce((total, file) => total + file.size, 0) > 10 * 1024 * 1024) {
    return response(413, { error: "photos_size" });
  }

  if (!env.OX_SMTP_PASSWORD) {
    return response(503, { error: "not_configured" });
  }

  const message = [
    "New contact request from the Simetrika website.",
    `Form language: ${lang.toUpperCase()}`,
    `Name: ${name}`,
    `Email: ${email || "Not provided"}`,
    `Phone: ${phone || "Not provided"}`,
    `Project location: ${city || "Not provided"}`,
    "",
    "Project:",
    project,
  ].join("\r\n");

  const headers = [
    `From: Simetrika <${SMTP_USER}>`,
    `To: ${RECIPIENT}`,
    ...(email ? [`Reply-To: ${email}`] : []),
    "Subject: New contact request - Simetrika",
    "MIME-Version: 1.0",
  ];
  let emailBody;
  if (photos.length) {
    const boundary = `simetrika-${crypto.randomUUID()}`;
    headers.push(`Content-Type: multipart/mixed; boundary="${boundary}"`);
    const parts = [
      `--${boundary}`,
      "Content-Type: text/plain; charset=UTF-8",
      "Content-Transfer-Encoding: base64",
      "",
      base64Utf8(message).match(/.{1,76}/g)?.join("\r\n") || "",
    ];
    for (const file of photos) {
      const bytes = new Uint8Array(await file.arrayBuffer());
      const binary = [];
      for (let index = 0; index < bytes.length; index += 0x8000) {
        binary.push(String.fromCharCode(...bytes.subarray(index, index + 0x8000)));
      }
      const encodedPhoto = btoa(binary.join("")).match(/.{1,76}/g)?.join("\r\n") || "";
      const safeName = file.name.replace(/[^A-Za-z0-9._-]/g, "_").slice(0, 100) || "photo";
      parts.push(
        `--${boundary}`,
        `Content-Type: ${file.type.toLowerCase()}`,
        "Content-Transfer-Encoding: base64",
        `Content-Disposition: attachment; filename="${safeName}"`,
        "",
        encodedPhoto,
      );
    }
    parts.push(`--${boundary}--`);
    emailBody = parts.join("\r\n");
  } else {
    headers.push(
      "Content-Type: text/plain; charset=UTF-8",
      "Content-Transfer-Encoding: base64",
    );
    emailBody = base64Utf8(message).match(/.{1,76}/g)?.join("\r\n") || "";
  }
  const smtpMessage = dotStuff(headers.join("\r\n") + "\r\n\r\n" + emailBody);

  let socket;
  let smtpStage = "connect";
  try {
    smtpStage = "connect";
    socket = connect(
      { hostname: SMTP_HOST, port: SMTP_PORT },
      { secureTransport: "starttls" },
    );
    let stream = makeSmtpStream(socket);

    smtpStage = "server greeting";
    expectCode(await stream.readResponse(), [220]);
    smtpStage = "EHLO before TLS";
    expectCode(await stream.sendLine("EHLO simetrika.lu"), [250]);
    smtpStage = "STARTTLS command";
    expectCode(await stream.sendLine("STARTTLS"), [220]);
    stream.release();

    smtpStage = "TLS handshake";
    socket = socket.startTls();
    stream = makeSmtpStream(socket);

    smtpStage = "EHLO after TLS";
    expectCode(await stream.sendLine("EHLO simetrika.lu"), [250]);
    smtpStage = "AUTH LOGIN";
    expectCode(await stream.sendLine("AUTH LOGIN"), [334]);
    smtpStage = "SMTP username authentication";
    expectCode(await stream.sendLine(base64Utf8(SMTP_USER)), [334]);
    smtpStage = "SMTP password authentication";
    expectCode(await stream.sendLine(base64Utf8(env.OX_SMTP_PASSWORD)), [235]);
    smtpStage = "MAIL FROM";
    expectCode(await stream.sendLine(`MAIL FROM:<${SMTP_USER}>`), [250]);
    smtpStage = "RCPT TO";
    expectCode(await stream.sendLine(`RCPT TO:<${RECIPIENT}>`), [250, 251]);
    smtpStage = "DATA command";
    expectCode(await stream.sendLine("DATA"), [354]);
    smtpStage = "message body";
    expectCode(await stream.sendLine(smtpMessage + "\r\n."), [250]);
    smtpStage = "QUIT";
    expectCode(await stream.sendLine("QUIT"), [221]);
    stream.release();

    smtpStage = "socket close";
    await socket.close();
    return response(200, { ok: true });
  } catch (error) {
    const errorDetails = error instanceof Error
      ? `${error.name}: ${error.message}`.slice(0, 180)
      : "Unknown SMTP error";
    console.error("OX SMTP contact delivery failed", JSON.stringify({ stage: smtpStage, error: errorDetails }));
    try {
      await socket?.close();
    } catch {
      // Ignore cleanup errors after a failed SMTP exchange.
    }
    const diagnosticMode = new URL(request.url).searchParams.get("smtp-diagnostic") === "1" && name.startsWith("TEST Simetrika");
    return response(502, diagnosticMode
      ? { error: "delivery_failed", diagnostic: { stage: smtpStage, detail: errorDetails } }
      : { error: "delivery_failed" });
  }
}
