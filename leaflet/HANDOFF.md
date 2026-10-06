# Zenday — Pro leaflet · designer handoff

**Use:** exhibition handout for beauty professionals (Treatwell & Fresha on the same floor).
**Format:** A5 portrait, 148 × 210 mm, double-sided, full colour. Files include **3 mm bleed** (154 × 216 mm).
**Files:** `export/zenday-leaflet-A5-print-bleed3mm.pdf` (print proof), `export/*.png` (trimmed previews), `zenday-leaflet.html` (editable source — open in Chrome).

## The idea
Treatwell and Fresha sell to **salons**. Zenday is for the **independent professional who goes to the client**.
So the line is: **«Εσείς είστε το σαλόνι.»** — *you* are the salon.
The **Λ** of the Zenday wordmark is redrawn as a gold **roof** on the front: the pro walks into the client's home.
**Campaign line — Zenday as a day of the week:** the front ends on «Η εβδομάδα σας μόλις απέκτησε όγδοη μέρα» ("your week just gained an eighth day") over a calendar strip ΔΕΥ … ΚΥΡ + a ZENDΛY pill; the back closes with «Σήμερα είναι Zenday» ("Today is Zenday") — the reason to register at the stand, today.
**Claim:** the gold seal at the roof's apex — «Η πρώτη στην Ελλάδα · κατ’ οίκον · για επαγγελματίες» — is repeated in plain words under the headline.
The floating "new booking — already paid" card is the single moment every pro wants; it sells the product without a single number.

Copy rules kept on purpose: no numbers, percentages or fees (those live in the contract). Competitors are never named — "the big platforms were made for salons".

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
- Front: wordmark top-left · seal at the roof apex · headline left-aligned at ~⅓ height · notification card rotated −2.2° bottom-right with a soft shadow · slogan + blush week strip on the bottom edge.
- Back: headline + manifesto → 6 benefits (2 × 3, icon discs) → "not good with tech?" box → specialty chips → oxblood CTA band with QR.
- QR (`qr.svg`, vector) → `https://zenday.gr/mgo-artist/?utm_source=expo&utm_medium=leaflet` (the UTM tags let you count leaflet sign-ups in analytics). Keep it ≥ 25 mm; test-scan the printed proof.
- The PDF is a high-quality proof produced from HTML; for press, rebuild in InDesign/Illustrator with these specs, or export CMYK from the source.

## Upgrades worth the money
- Gold foil on the Λ roof line and the wordmark.
- Soft-touch matte laminate on 350 g silk — it feels like a beauty brand in the hand.
- Optional: one real photo of a pro at work (hands + tools, warm light) behind the front card, toned into the oxblood.

## Still open (fill before print)
- A stand-only offer, if any (e.g. free setup) — the CTA band has room for one line.
- Instagram / phone, if you want them next to zenday.gr.
