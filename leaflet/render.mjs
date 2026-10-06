// Renders the leaflet to a print PDF (with 3 mm bleed) and PNG previews (trimmed to A5).
// Usage: node render.mjs <leaflet-dir> [page.html ...]   (needs the playwright package resolvable from this script)
// With no page names it renders zenday-leaflet.html; each page.html → export/<page>-print-bleed3mm.pdf, -front.png, -back.png.
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = process.argv[2] ? path.resolve(process.argv[2]) : path.dirname(fileURLToPath(import.meta.url));
const files = process.argv.slice(3).length ? process.argv.slice(3) : ['zenday-leaflet.html'];
const out = path.join(dir, 'export');
const MM = 96 / 25.4; // CSS px per mm

const browser = await chromium.launch();
for (const file of files) {
  const name = path.basename(file, '.html');
  const page = await browser.newPage({ deviceScaleFactor: 4, viewport: { width: Math.ceil(154 * MM), height: Math.ceil(216 * MM) } });
  await page.goto('file://' + path.join(dir, file), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);

  await page.pdf({ path: path.join(out, `${name}-A5-print-bleed3mm.pdf`), width: '154mm', height: '216mm', printBackground: true, preferCSSPageSize: true });

  const sides = await page.$$('.page');
  for (const [i, el] of sides.entries()) {
    const box = await el.boundingBox();
    const b = 3 * MM; // trim off the bleed for the preview
    await page.screenshot({
      fullPage: true,
      path: path.join(out, `${name}-${i ? 'back' : 'front'}.png`),
      clip: { x: box.x + b, y: box.y + b, width: box.width - 2 * b, height: box.height - 2 * b },
    });
  }
  await page.close();
  console.log('rendered', name);
}
await browser.close();
