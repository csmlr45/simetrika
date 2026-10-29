export async function onRequestPost({ request, env }) {
  const headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store",
  };
  const reply = (status, data) =>
    new Response(JSON.stringify(data), { status, headers });

  const origin = request.headers.get("Origin");
  if (origin) {
    let host;
    try {
      host = new URL(origin).hostname;
    } catch {
      return reply(403, { error: "origin" });
    }

    const allowedHosts = [
      "simetrika-7wr.pages.dev",
      "simetrika.lu",
      "www.simetrika.lu",
    ];
    if (!allowedHosts.includes(host) && !host.endsWith(".simetrika.pages.dev")) {
      return reply(403, { error: "origin" });
    }
  }

  const rawBody = await request.text();
  if (new TextEncoder().encode(rawBody).byteLength > 12_000) {
    return reply(413, { error: "size" });
  }

  let data;
  try {
    data = JSON.parse(rawBody);
  } catch {
    return reply(400, { error: "invalid_json" });
  }
  if (!data || typeof data !== "object" || Array.isArray(data)) {
    return reply(400, { error: "invalid_data" });
  }

  const value = (key, max) =>
    typeof data[key] === "string" ? data[key].trim().slice(0, max + 1) : "";
  const name = value("name", 150);
  const email = value("email", 254);
  const phone = value("phone", 80);
  const project = value("project", 5000);
  const website = value("website", 100);
  const requestedLang = value("lang", 8).toLowerCase();
  const lang = ["fr", "de", "en", "lb"].includes(requestedLang)
    ? requestedLang
    : "fr";

  // Honeypot: silently accept bot submissions without sending email.
  if (website) return reply(200, { ok: true });

  if (
    !name ||
    name.length > 150 ||
    !project ||
    project.length > 5000 ||
    (!email && !phone) ||
    email.length > 254 ||
    phone.length > 80
  ) {
    return reply(400, { error: "validation" });
  }

  if (email && !/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {
    return reply(400, { error: "email" });
  }

  if (!env.RESEND_API_KEY) {
    return reply(503, { error: "not_configured" });
  }

  const subjects = {
    fr: "Nouvelle demande de contact — Simetrika",
    de: "Neue Kontaktanfrage — Simetrika",
    en: "New contact request — Simetrika",
    lb: "Nei Kontaktufro — Simetrika",
  };
  const message = [
    "Nouvelle demande reçue via le formulaire du site Simetrika.",
    "",
    `Langue du formulaire : ${lang.toUpperCase()}`,
    `Nom : ${name}`,
    `E-mail : ${email || "Non indiqué"}`,
    `Téléphone : ${phone || "Non indiqué"}`,
    "",
    "Projet :",
    project,
  ].join("\\n");

  const payload = {
    from: "Simetrika <contact@simetrika.lu>",
    to: ["contact@simetrika.lu"],
    subject: subjects[lang],
    text: message,
  };
  if (email) payload.reply_to = email;

  try {
    const response = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      console.error("Resend contact email failed:", response.status);
      return reply(502, { error: "delivery_failed" });
    }

    return reply(200, { ok: true });
  } catch {
    return reply(502, { error: "delivery_failed" });
  }
}
