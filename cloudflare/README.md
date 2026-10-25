# Simetrika Cloudflare Pages staging

This directory is an **unpublished staging placeholder**, not the final website.

Cloudflare Pages configuration:
- Framework preset: None
- Production branch: main (only after merging this branch)
- Build command: leave empty
- Build output directory: cloudflare
- Root directory: repository root

The placeholder explicitly disallows search indexing via HTML meta, robots.txt and X-Robots-Tag. These signals **do not provide privacy or access control**. Before sharing the preview or uploading real company content, protect the pages.dev hostname using Cloudflare Access (Zero Trust).

The existing Streamlit application remains at the repository root. No domain or DNS settings need changing.

Next: migrate website markup, language routes, estimator, legal pages, and a Cloudflare-compatible contact form. Do not use SMTP credentials in client-side code or Cloudflare Pages static files.
