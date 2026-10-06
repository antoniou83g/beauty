# Zenday — exhibition kit · designer handoff

Nine separate pieces for the beauty-professionals exhibition (Treatwell & Fresha on the same floor).
Every piece has its own source (`NN-*.html`, open in Chrome), its own print PDF and PNG previews in `export/`.
Rebuild after a copy change: `python3 build.py` then `node render.mjs . NN-*.html` (needs Playwright).

## The idea — «Ομορφιά & ευεξία στο σπίτι»
Treatwell and Fresha were built for shops (hair salons, beauty centres). Zenday is for the **freelancer who brings beauty & wellness into the client's home**.
- **Brand line:** «Ομορφιά & ευεξία στο σπίτι.»
- **Promise:** «Εσείς φέρνετε την τέχνη. Εμείς, τους πελάτες.»
- **Claim (gold seal):** «Η πρώτη στην Ελλάδα · κατ’ οίκον · για freelancers».
- **Demand:** «Zen πελάτες αναζητούν τις υπηρεσίες σας.» + three already-paid bookings (same-day, Saturday wedding at home, Sunday massage).
- **For whoever you are:** already employed (a second income), a sparkling new start, or working alone — the platform was made for all three.
- **English, only in the slogans:** "Make every day a Zenday." · "Every day is Zenday." · "Make your day a Zenday." · "Shhh… it's a Zenday."
- The **Λ** of the wordmark is also the roof of the client's home. No numbers, percentages or fees anywhere; competitors never named.

## The pieces
| # | Piece | Size (trim) | Files | Slogan |
|---|---|---|---|---|
| 01 | **Leaflet — Zen at home** | A5 148 × 210, +3 mm bleed | `export/01-…-print-bleed3mm.pdf`, `-front.png`, `-back.png` | Front «Ομορφιά & ευεξία στο σπίτι.» · back CTA "Make every day a Zenday." |
| 02 | **Leaflet — Ding-dong** | A5 | `export/02-…` | Front «Ντιν-ντον. Ομορφιά & ευεξία στο σπίτι.» · back "Every day is Zenday." |
| 03 | **Leaflet — Λ window** | A5 | `export/03-…` | Front «Η τέχνη σας, στο σπίτι τους.» · back "Make your day a Zenday." |
| 04 | **Door hanger** | 90 × 230, +3 mm bleed, hole Ø34 + slit, r4 | `export/04-door-hanger.pdf`, `-side-a/b.png` | A (client's door): «Μην ενοχλείτε. Ομορφιά & ευεξία σε εξέλιξη.» + "Shhh… it's a Zenday." · B (freelancers): «Κρεμάστε το στην επόμενη πόρτα.» + "Make every day a Zenday." |
| 05 | **Key tag** | 46 × 96, arched top, hole Ø10 | `export/05-key-tag.pdf`, `-side-a/b.png` | «Το κλειδί για νέους πελάτες.» · back "Every day is Zenday." + QR |
| 06 | **Thank-you card** (left by the freelancer for the client) | 85 × 55, +3 mm bleed | `export/06-thank-you-card.pdf`, `-side-a/b.png` | «Ευχαριστώ που μου ανοίξατε την πόρτα.» · back «Την επόμενη φορά, κλείστε με στο Zenday.» + "Make your day a Zenday." |
| 07 | **Sticker** | Ø60 round, +2 mm bleed, kiss-cut | `export/07-sticker.pdf/.png` | "Every day is Zenday." |
| 08 | **Tote bag** | print area 300 × 360 | `export/08-tote-bag.pdf/.png` | "Make every day a Zenday." — screen-print cream + gold on oxblood cotton |
| 09 | **Stand entrance** (visual for the stand builder) | — | `export/09-stand-entrance.pdf/.png` | «Ντιν-ντον. Περάστε.» — front door with gold Λ roof, real doorbell, «Καλώς ήρθατε» doormat |

The three leaflets share the same back: why Zenday → «Όπου κι αν βρίσκεστε, το Zenday φτιάχτηκε για εσάς» (three personas) → 6 benefits → 1-2-3 → CTA (the English slogan changes per leaflet).

**Die-cut / kiss-cut lines** are magenta dashed (`#e5007e`): put them on their own spot layer and never print them.

## Slogan bank
Greek: «Ομορφιά & ευεξία στο σπίτι.» · «Εσείς φέρνετε την τέχνη. Εμείς, τους πελάτες.» · «Η τέχνη σας, στο σπίτι τους.» · «Ντιν-ντον. Περάστε.» · «Zen πελάτες αναζητούν τις υπηρεσίες σας.» · «Μην ενοχλείτε. Ομορφιά & ευεξία σε εξέλιξη.» · «Το κλειδί για νέους πελάτες.» · «Ευχαριστώ που μου ανοίξατε την πόρτα.»
English: "Make every day a Zenday." · "Every day is Zenday." · "Make your day a Zenday." · "Shhh… it's a Zenday." · "Have a Zenday." · "Bring the zen home." · "Knock knock. It's Zenday."

## QR codes (vector, edit colour freely)
- `qr.svg` → `zenday.gr/mgo-artist/?utm_source=expo&utm_medium=leaflet` (leaflets, key tag)
- `qr-hanger.svg` → same page, `utm_medium=door_hanger`
- `qr-client.svg` → `zenday.gr/?utm_source=thankyou_card` (client side, thank-you card)
Keep each ≥ 20 mm (≥ 25 mm on the leaflets) and test-scan the printed proof.

## Images & rights
- `img/zen-massage.jpg` (leaflet 01) — Unsplash `photo-1649751295468-953038600bef`, already on zenday.gr; Unsplash License, free commercial use incl. print. 3000 px. The blue towel is warmed and faded into oxblood.
- `img/doorbell.jpg` (leaflet 02) — StockSnap "Wood Door", CC0. 960 px preview here; **download the 5616 px original** at https://stocksnap.io/photo/F2CDF3B476.
- `img/hairdresser.jpg` (leaflet 03) — Unsplash `photo-1562322140-8baeececf3df`, already on zenday.gr; Unsplash License. 3000 px.
- Worth one half-day shoot with a real Zenday freelancer: a client greeting her at the door, her hand on the work case, the door hanger on a real door.

## Colour (from zenday.gr)
| Role | HEX | Suggested CMYK (check against your printer's profile) |
|---|---|---|
| Oxblood — primary dark | `#491009` | 30 / 95 / 95 / 65 |
| Brick — accent | `#972010` | 15 / 95 / 100 / 15 |
| Cream — paper | `#F7ECE4` | 2 / 7 / 9 / 0 |
| Blush — bands, icon discs | `#FEDADB` | 0 / 18 / 9 / 0 |
| Rose — italic highlights | `#F3B7B3` | 0 / 35 / 20 / 0 |
| Gold — roof line, kickers | `#C6A664` | 22 / 32 / 70 / 5 (or gold foil / Pantone 7502) |

Large oxblood areas: ask the printer for a rich build so it doesn't print muddy.

## Type (all served by zenday.gr, in `fonts/`)
- **Zenday Wordmark** — logotype only. Type "Zenday" in it, no tracking; it draws ZENDΛY.
- **Noto Serif Display** — headlines; *italic light* for the coloured second line.
- **Manrope** — body (500), kickers in ExtraBold 800, caps, tracking ~ +200.
- Licences: SIL OFL 1.1 (`fonts/LICENSE.txt`).

## Print suggestions
- Leaflets: 350 g silk + soft-touch matte laminate; gold foil on the Λ roof, the seal and the wordmark.
- Door hanger: 400 g uncoated or soft-touch, so it survives door handles. Key tag: 600 µm laminated card or PVC.
- The PDFs are high-quality proofs produced from HTML; for press, rebuild in InDesign/Illustrator with these specs, or export CMYK from the sources.

## Still open
- A stand-only offer, if any (e.g. free setup) — the leaflet CTA band has room for one line.
- Instagram / phone, if you want them next to zenday.gr.
