// Renders the leaflet to a print PDF (with 3 mm bleed) and PNG previews (trimmed to A5).
// Usage: node render.mjs <leaflet-dir>   (needs the playwright package resolvable from this script)
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const dir = process.argv[2] ? path.resolve(process.argv[2]) : path.dirname(fileURLToPath(import.meta.url));
const src = 'file://' + path.join(dir, 'zenday-leaflet.html');
const out = path.join(dir, 'export');
const MM = 96 / 25.4; // CSS px per mm

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 4, viewport: { width: Math.ceil(154 * MM), height: Math.ceil(216 * MM) } });
await page.goto(src, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

await page.pdf({ path: path.join(out, 'zenday-leaflet-A5-print-bleed3mm.pdf'), width: '154mm', height: '216mm', printBackground: true, preferCSSPageSize: true });

const sides = await page.$$('.page');
for (const [i, el] of sides.entries()) {
  const box = await el.boundingBox();
  const b = 3 * MM; // trim off the bleed for the preview
  await page.screenshot({
    fullPage: true,
    path: path.join(out, `zenday-leaflet-${i ? 'back' : 'front'}.png`),
    clip: { x: box.x + b, y: box.y + b, width: box.width - 2 * b, height: box.height - 2 * b },
  });
}
await browser.close();
console.log('done');
