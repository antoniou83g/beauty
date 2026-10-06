# Zenday — Pro leaflet · designer handoff

**Use:** exhibition handout for beauty professionals (Treatwell & Fresha on the same floor).
**Format:** A5 portrait, 148 × 210 mm, double-sided, full colour. Files include **3 mm bleed** (154 × 216 mm).
**Files:** `export/zenday-leaflet-A5-print-bleed3mm.pdf` (print proof), `export/*.png` (trimmed previews), `zenday-leaflet.html` (editable source — open in Chrome).

## The idea — «Ομορφιά & ευεξία στο σπίτι»
Treatwell and Fresha were built for **shops** (hair salons, beauty centres). Zenday is for the **independent professional who brings beauty & wellness into the client's home**.
- **Brand line:** «Ομορφιά & ευεξία στο σπίτι.»
- **Promise to the pro:** «Εσείς φέρνετε την τέχνη. Εμείς, τους πελάτες.»
- **Claim:** gold seal «Η πρώτη στην Ελλάδα · κατ’ οίκον · για επαγγελματίες», repeated in plain words under the headline.
- **Demand:** «Σας ψάχνουν ήδη.» + three already-paid booking notifications (urgent same-day, Saturday wedding at home, Sunday massage for someone who'd rather stay zen at home).
- **Back:** why Zenday (6 benefits) → how to start in 1-2-3 → CTA «Σήμερα είναι Zenday».
- The **Λ** of the wordmark doubles as the roof of the client's home.
- Copy rules: no numbers, percentages or fees (those live in the contract); competitors never named.

## Cover options (the back is the same for all) — side by side in `export/cover-options-1-2-3-4.jpg`
- **1 · Door** (`zenday-leaflet-1-door.html` = current `zenday-leaflet.html`): «Ομορφιά & ευεξία στο σπίτι.» over a smiling woman at a front door (photo mirrored, warm-toned).
- **2 · Sofa:** «Σας κλείνουν από τον καναπέ. *Εσείς χτυπάτε το κουδούνι.*» over a client booking from her sofa.
- **3 · Ding-dong:** «Ντιν-ντον. *Ομορφιά & ευεξία στο σπίτι.*» doorbell duotoned oxblood/rose, gold rings.
- **4 · Λ window:** «Η τέχνη σας, *στο σπίτι τους.*» the hairdresser at work inside the Λ.

## The door, as a concept (`zenday-concepts-board.html` → `export/zenday-concepts-board.png`)
1. **Door hanger** (`zenday-door-hanger.html`, print PDF in `export/`): 90 × 230 mm + 3 mm bleed, hole Ø34 mm + slit, r4 corners — the magenta dashed line is the **die-cut**, put it on its own spot layer, never print it.
   Side A, for the client's door: «Μην ενοχλείτε. *Ομορφιά & ευεξία σε εξέλιξη.*» · Side B, for the pro: «Κρεμάστε το *στην επόμενη πόρτα.*» + QR (`qr-hanger.svg`, tagged `utm_medium=door_hanger`).
   Suggested stock: 350–400 g uncoated or soft-touch, so it survives door handles.
2. **Key tag:** «Το κλειδί *για νέους πελάτες.*» — 46 × 96 mm fob with hole, QR on the back. Lives on the pro's keyring.
3. **Thank-you card** (85 × 55): «Ευχαριστώ που μου *ανοίξατε την πόρτα.*» / back «Την επόμενη φορά, *κλείστε με στο Zenday.*» + client QR (`qr-client.svg`). The pro signs it and leaves it — repeat bookings for them, new users for Zenday.
4. **The stand is a door:** «Ντιν-ντον. *Περάστε.*» — a front-door entrance with the gold Λ roof, a «Καλώς ήρθατε» doormat and a real doorbell.

## Image sources & rights
- `img/welcome.jpg` — StockSnap "Woman Portrait", CC0 (public domain, no credit needed). Original 3456 × 2304: https://stocksnap.io/photo/HV6O4C5CZA — 960 px preview here, **download the original for print**.
- `img/sofa.jpg` — StockSnap "Woman Mobile", CC0. Original 7680 × 5120: https://stocksnap.io/photo/Q93BUD2Z3Z — preview here; keep the shopping bag (bottom left) cropped out.
- `img/doorbell.jpg` — StockSnap "Wood Door", CC0. Original 5616 × 3744: https://stocksnap.io/photo/F2CDF3B476 — preview here, download the original.
- `img/hairdresser.jpg` — Unsplash `photo-1562322140-8baeececf3df` (already on zenday.gr), Unsplash License: free commercial use incl. print. 3000 px.
- `img/hair|massage|facial|nails|makeup.jpg` — frames from the zenday.gr homepage film (1440 × 1080).
- The ideal hero — a smiling Zenday pro greeted by a client at the door — doesn't exist as free stock. One half-day shoot with a real pro (door greeting, hand on the work case, the door hanger on a real door) would give the campaign its own images.

## Colour (from zenday.gr)
| Role | HEX | Suggested CMYK (check against your printer's profile) |
|---|---|---|
| Oxblood — primary dark | `#491009` | 30 / 95 / 95 / 65 |
| Brick — accent | `#972010` | 15 / 95 / 100 / 15 |
| Cream — paper | `#F7ECE4` | 2 / 7 / 9 / 0 |
| Blush — ticker / icon discs | `#FEDADB` | 0 / 18 / 9 / 0 |
| Rose — italic highlights | `#F3B7B3` | 0 / 35 / 20 / 0 |
| Gold — roof line, kickers | `#C6A664` | 22 / 32 / 70 / 5 (or a gold foil / Pantone 7502 as an upgrade) |

Large oxblood areas: ask the printer for a rich build so it doesn't print muddy.

## Type (all served by zenday.gr, in `fonts/`)
- **Zenday Wordmark** — logotype only. Type "Zenday" in it, no tracking; it draws ZENDΛY.
- **Noto Serif Display** — headlines; *italic light* for the coloured second line.
- **Manrope** — body (500), kickers in ExtraBold 800, caps, tracking ~ +200.
- Licences: SIL OFL 1.1 (`fonts/LICENSE.txt`).

## Layout notes
- Margins: 13 mm from the bleed edge (10 mm from trim). Keep everything ≥ 5 mm inside the trim.
- Front: wordmark top-left · seal at the roof apex · headline left-aligned at ~⅓ height · «Σας ψάχνουν ήδη» + three notification cards cascading left→right, alternating ±1–2° rotation, soft shadows · blush benefit ticker on the bottom edge.
- Back: headline + manifesto → 6 benefits (3 × 2, icon discs) → 1-2-3 steps on a full-bleed blush band → oxblood CTA band with QR.
- QR (`qr.svg`, vector) → `https://zenday.gr/mgo-artist/?utm_source=expo&utm_medium=leaflet` (the UTM tags let you count leaflet sign-ups in analytics). Keep it ≥ 25 mm; test-scan the printed proof.
- The PDF is a high-quality proof produced from HTML; for press, rebuild in InDesign/Illustrator with these specs, or export CMYK from the source.

## Upgrades worth the money
- Gold foil on the Λ roof line and the wordmark.
- Soft-touch matte laminate on 350 g silk — it feels like a beauty brand in the hand.
- Optional: one real photo of a pro at work (hands + tools, warm light) behind the front card, toned into the oxblood.

## Still open (fill before print)
- A stand-only offer, if any (e.g. free setup) — the CTA band has room for one line.
- Instagram / phone, if you want them next to zenday.gr.
