// Renders each piece to a print PDF (page size from its CSS @page, bleed included) and PNG previews.
// Usage: node render.mjs <dir> NN-piece.html [...]   (needs the playwright package resolvable from this script)
// Leaflets (two A5 pages) → export/<name>-print-bleed3mm.pdf + <name>-front.png / -back.png (trimmed to A5).
// Other pieces → export/<name>.pdf + <name>[-side-a|-side-b].png (with bleed and die-line, as the printer sees it).
import { chromium } from 'playwright';
import path from 'node:path';

const dir = path.resolve(process.argv[2] || '.');
const files = process.argv.slice(3);
const out = path.join(dir, 'export');
const MM = 96 / 25.4;

const browser = await chromium.launch();
for (const file of files) {
  const name = path.basename(file, '.html');
  const page = await browser.newPage({ deviceScaleFactor: 4, viewport: { width: 1400, height: 1000 } });
  await page.goto('file://' + path.join(dir, file), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const sides = await page.$$('.page');
  const first = await sides[0].boundingBox();
  await page.setViewportSize({ width: Math.ceil(first.width + 2 * first.x), height: 1000 });
  const leaflet = name.includes('leaflet');

  const { w, h } = { w: first.width / MM, h: first.height / MM };
  await page.pdf({ path: path.join(out, leaflet ? `${name}-print-bleed3mm.pdf` : `${name}.pdf`),
                   width: `${w.toFixed(2)}mm`, height: `${h.toFixed(2)}mm`, printBackground: true, preferCSSPageSize: true });

  for (const [i, el] of sides.entries()) {
    const box = await el.boundingBox();
    const b = leaflet ? 3 * MM : 0;
    const label = leaflet ? (i ? '-back' : '-front') : sides.length > 1 ? `-side-${'ab'[i]}` : '';
    await page.screenshot({ fullPage: true, path: path.join(out, `${name}${label}.png`),
                            clip: { x: box.x + b, y: box.y + b, width: box.width - 2 * b, height: box.height - 2 * b } });
  }
  await page.close();
  console.log('rendered', name);
}
await browser.close();
