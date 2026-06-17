# Abc Ore Pro — realtor marketing-kit storefront

A fast, static, single-page storefront that sells three low-ticket digital products to
real estate agents, presented as **property-style "listings"** plus a discounted bundle.
Plain HTML + CSS + a little vanilla JS — **no framework, no build step, no backend, no
browser storage.** Serves directly from GitHub Pages.

> Built from scratch to the project spec (there was no preview file to productionize).
> Palette: **portal-blue + navy + gold.** Type: **Plus Jakarta Sans / DM Sans.**

## Products

| Listing | Price | What it is |
|---|---|---|
| Database Reactivation Pack | $37 | 5-touch text + email sequence to re-engage cold past clients |
| Google Review Booster Kit | $37 | QR review cards, a 3-text request script, a local-ranking setup guide |
| 90-Day Content Calendar | $19 | 90 days of captions + a posting schedule |
| **The Agent Starter Kit** (bundle) | **$67** | All three together ($93 value, save $26) |

## Repo structure

```
index.html                  # the whole page
favicon.svg / favicon.ico   # site icons
assets/
  css/styles.css            # externalized design system (token-driven)
  js/main.js                # nav toggle, header shadow, footer year (no storage)
  img/
    reactivation.svg        # product "listing photos" (hand-authored, crisp, cacheable)
    reviews.svg
    calendar.svg
    bundle.svg
    og-image.png            # 1200x630 social/link-preview image
    favicon-32x32.png
    apple-touch-icon.png
tools/gen_meta_images.py     # regenerates og-image + favicon rasters (Pillow)
README.md
```

## Local preview

```bash
python3 -m http.server 8099   # then open http://localhost:8099/
```

## Quality floor (all met)

- Responsive to ~360px; visible `:focus-visible` states; `prefers-reduced-motion` respected.
- Semantic landmarks, heading order, skip link, `alt` on every image.
- `<title>`, meta description, canonical, Open Graph + Twitter tags, favicons (SVG + ICO + PNG + apple-touch).
- Page is ~20 KB of HTML; images are external/cacheable SVG + one PNG.

## Guardrails applied (deliberate — do not "fix" these back)

- **No unprovable claims.** "1000x ROI Success Promise" and "Top Local Rankings Guarantee"
  appear nowhere. Replaced with outcome framing ("One reactivated past client can pay for
  the whole kit many times over", "Built to help you climb your local map rankings").
- **No fake social proof.** No "3,200+ agents", no "★ 4.9", no invented testimonials.
  Honest framing only: "New — be one of the first."
- **No live checkout without a deliverable.** No checkout links and no confirmed product
  files exist yet, so **all four buy buttons are disabled "Coming soon"** (which also fits
  the listing metaphor). They are `<button disabled>`, not payment links.
- **Trademark safety.** Footer carries a Google non-affiliation + "results vary" disclaimer.
- **Images authored correctly** — no "Gooogle" typo, the calendar reads "90-Day Content
  Calendar." (The broken assets the spec warned about came from the missing preview; building
  fresh avoids them entirely.)

## Open TODOs before/at launch

1. **Brand name** — set to **Abc Ore Pro** (from the domain abcorepro.com). ✓ Resolved.
2. **`TODO_CHECKOUT_LINK` ×4** (one per HTML comment, by product). When a real deliverable
   exists for a product, swap its disabled button for a live link:
   ```html
   <a class="btn btn--block" href="PASTE_CHECKOUT_URL" target="_blank" rel="noopener">Get it — $37</a>
   ```
   Use Stripe Payment Links or Gumroad. **Do not enable a button until its file is real.**
3. **`TODO_CONTACT`** — footer "Contact (coming soon)" → real `mailto:` or contact URL.
4. **OG image font** — rendered with Liberation Sans (Plus Jakarta isn't installed as a TTF
   here). Cosmetic; only affects the social-share image, not the live page.

## Deploy (GitHub Pages)

Deploys from the `main` branch root to the custom domain **https://abcorepro.com/**
(the `CNAME` file holds `abcorepro.com`). DNS records to set at the registrar:

- Apex `A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- Apex `AAAA` (optional, IPv6) → `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
- `www` `CNAME` → `600589mbm-beep.github.io`

Until DNS propagates, the site also serves at `https://600589mbm-beep.github.io/realtor-storefront/`.
After the domain verifies, enable **Enforce HTTPS** in repo Settings → Pages.
