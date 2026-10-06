"""Builds every Zenday exhibition piece as its own separate, print-ready HTML page.

    python3 build.py            # writes the NN-*.html sources next to this file
    node render.mjs . NN-*.html # renders each to export/ (print PDF with bleed + PNG previews)

The A5 leaflet layout (front/back styles, fonts, colours) lives in _leaflet-base.html;
every other piece is self-contained here.
"""
import pathlib

D = pathlib.Path(__file__).parent
base = (D / '_leaflet-base.html').read_text()

# ───────────────────────────── shared copy ─────────────────────────────
FREELANCERS = 'freelancers ομορφιάς &amp; ευεξίας'
SUB = ('<p class="sub"><b>Εσείς φέρνετε την τέχνη. Εμείς, τους πελάτες.</b><br>'
       'Η πρώτη πλατφόρμα στην Ελλάδα για online κρατήσεις κατ’&nbsp;οίκον — αποκλειστικά για ' + FREELANCERS + '.</p>')
SLOGANS = {  # English only in the slogans; the wordmark draws ZENDΛY
    'make-every-day': 'Make every day<br><em>a</em> <span class="wm">Zenday</span>.',
    'every-day-is':   'Every day<br><em>is</em> <span class="wm">Zenday</span>.',
    'make-your-day':  'Make your day<br><em>a</em> <span class="wm">Zenday</span>.',
}

def shared(html):
    """Copy changes that apply to every leaflet: freelancers, zen clients, personas, new back rhythm."""
    rep = [
        ('Η ΠΡΩΤΗ ΣΤΗΝ ΕΛΛΑΔΑ ◆ ΚΑΤ’ ΟΙΚΟΝ ◆ ΓΙΑ ΕΠΑΓΓΕΛΜΑΤΙΕΣ ◆', 'Η ΠΡΩΤΗ ΣΤΗΝ ΕΛΛΑΔΑ ◆ ΚΑΤ’ ΟΙΚΟΝ ◆ ΓΙΑ FREELANCERS ◆'),
        ('<h2>Σας ψάχνουν <em>ήδη.</em></h2>', '<h2>Zen πελάτες <em>αναζητούν τις υπηρεσίες σας.</em></h2>'),
        ('<p>Στον δικό τους χώρο, στη δική τους ώρα — και πληρωμένοι πριν φτάσετε.</p>',
         '<p>Στο σπίτι τους, στην ώρα τους — και πληρώνουν πριν φτάσετε.</p>'),
        ('<p>Πελάτες που θέλουν την περιποίηση στον δικό τους χώρο, στη δική τους ώρα — και πληρώνουν πριν φτάσετε.</p>',
         '<p>Στο σπίτι τους, στην ώρα τους — και πληρώνουν πριν φτάσετε.</p>'),
        ('alt="QR κωδικός εγγραφής επαγγελματία"', 'alt="QR κωδικός εγγραφής"'),
        # back: the personas band replaces the manifesto
        ('<p class="manifesto">Οι μεγάλες πλατφόρμες φτιάχτηκαν για κομμωτήρια και κέντρα. <b>Το Zenday φτιάχτηκε αποκλειστικά για εσάς</b> — που φέρνετε ομορφιά &amp; ευεξία στο σπίτι του πελάτη.</p>\n  </div>',
         '''</div>

  <div class="who">
    <p class="kicker">Όπου κι αν βρίσκεστε, το Zenday φτιάχτηκε για εσάς</p>
    <div class="cols">
      <div><span class="tag">Ήδη εργαζόμενοι</span><h3>Έχετε ήδη δουλειά;</h3><p>Ραντεβού όποτε είστε ελεύθεροι. Ένα δεύτερο εισόδημα.</p></div>
      <div><span class="tag">Νέο ξεκίνημα</span><h3>Ξεκινάτε τώρα;</h3><p>Ένα λαμπερό ξεκίνημα, με πελάτες από την πρώτη μέρα.</p></div>
      <div><span class="tag">Ανεξάρτητοι</span><h3>Δουλεύετε μόνοι;</h3><p>Κρατήσεις, πληρωμές και φορολογικά, σε ένα μέρος.</p></div>
    </div>
  </div>'''),
        ('<h3>Πληρωμένο, πριν φτάσετε.</h3></div>\n      <p>Κλείνουν και πληρώνουν online. Χωρίς τηλέφωνα, χωρίς μετρητά.</p>',
         '<h3>Πληρωμένα ραντεβού.</h3></div>\n      <p>Κλείνουν και πληρώνουν online. Χωρίς τηλέφωνα, χωρίς μετρητά.</p>'),
        ('<p>Ξεκάθαροι όροι, καμία δέσμευση. Όταν κερδίζετε εσείς, κερδίζουμε κι εμείς.</p>', '<p>Ξεκάθαροι όροι, καμία δέσμευση. Κερδίζουμε μαζί.</p>'),
        ('<p>Δικές σας τιμές, ώρες και περιοχές — ακόμα και μόνο μια Κυριακή.</p>', '<p>Τιμές, ώρες, περιοχές: τα ορίζετε εσείς.</p>'),
        ('<h3>Ξέρετε πού πηγαίνετε.</h3></div>\n      <p>Επιβεβαιωμένοι πελάτες, με ιστορικό από συναδέλφους σας.</p>',
         '<h3>Ξέρετε πού πάτε.</h3></div>\n      <p>Επιβεβαιωμένοι πελάτες, με ιστορικό από συναδέλφους.</p>'),
        ('<h3>Τέλος οι χαμένες ώρες.</h3></div>\n      <p>Ορίζετε τη δική σας χρέωση για ακυρώσεις της τελευταίας στιγμής.</p>',
         '<h3>Τέλος οι ακυρώσεις.</h3></div>\n      <p>Δική σας χρέωση για ακυρώσεις της τελευταίας στιγμής.</p>'),
        ('<p>Νόμιμα. Τα φορολογικά και τα ασφαλιστικά τα υπολογίζουμε εμείς.</p>', '<p>Νόμιμα. Τα φορολογικά τα υπολογίζουμε εμείς.</p>'),
        ('<p>Δωρεάν, από το κινητό σας. Δεν τα πάτε καλά με την τεχνολογία; Το στήνουμε εμείς για εσάς.</p>',
         '<p>Δωρεάν, από το κινητό σας — ή το στήνουμε εμείς για εσάς.</p>'),
        ('<p>Ήδη πληρωμένα. Εσείς πηγαίνετε — η αμοιβή σας έρχεται στον λογαριασμό σας.</p>',
         '<p>Ήδη πληρωμένα. Η αμοιβή σας, στον λογαριασμό σας.</p>'),
    ]
    for a, b in rep:
        if a in html:
            html = html.replace(a, b)
    css = '''
  /* ── back, round 4: personas band + tighter rhythm ── */
  .back .head{top:11mm}
  .back h2{font-size:21pt}
  .back .manifesto{margin-top:2.4mm;font-size:7.8pt}
  .who{position:absolute;left:13mm;right:13mm;top:33mm;padding:3mm 0 3.2mm;border-top:.3mm solid rgba(198,166,100,.8);border-bottom:.3mm solid rgba(198,166,100,.8)}
  .who > .kicker{color:var(--brick);font-size:5.8pt}
  .who .cols{display:grid;grid-template-columns:repeat(3,1fr);column-gap:4mm;margin-top:2.2mm}
  .who .cols > div + div{border-left:.25mm solid rgba(73,16,9,.15);padding-left:4mm}
  .who .tag{display:inline-block;padding:.9mm 2mm;border-radius:99px;background:var(--blush);font:800 4.8pt/1 Manrope,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--brick)}
  .who h3{margin-top:1.8mm;font:500 10pt/1.1 'Noto Serif Display',serif}
  .who p{margin-top:1.2mm;font:500 6.8pt/1.42 Manrope,sans-serif;color:rgba(73,16,9,.75)}
  .grid{top:70mm;row-gap:4mm}
  .b .ic{width:6.4mm;height:6.4mm}
  .b .ic svg{width:3.6mm;height:3.6mm}
  .b h3{font-size:8.6pt;white-space:nowrap}
  .b p{margin-top:1.1mm;font-size:6.6pt;line-height:1.38}
  .steps{top:104mm;height:49mm;padding-top:5.4mm}
  .steps h3{margin-top:1.4mm;font-size:14pt}
  .steps ol{margin-top:4.6mm}
  .steps ol::before{top:3.5mm}
  .steps .n{width:8mm;height:8mm;font-size:12pt}
  .steps ol::before{top:4mm}
  .steps li h4{margin-top:2.4mm;font-size:9.4pt}
  .steps li p{margin-top:1mm;font-size:6.8pt}
  .cta{height:63mm;padding-top:7mm}
  .cta h4{font-size:21pt}
  .cta h4 .wm{font-size:17pt}
'''
    return html.replace('</style>', css + '</style>', 1)

base = shared(base)
fs = base.index('<!-- ════════════════════════ FRONT')
fe = base.index('<!-- ════════════════════════ BACK')
front = base[fs:fe]
seal = front[front.index('  <!-- Seal'):front.index('</svg>', front.index('  <!-- Seal')) + 6]
lower = front[front.index('  <div class="demand">'):front.rindex('</section>')]

COVER_CSS = '''
  /* ── covers ── */
  .cv{background:radial-gradient(110mm 80mm at 12% 100%, rgba(151,32,16,.4), transparent 70%),#491009}
  .cv .photo{position:absolute;left:0;top:0;width:154mm;overflow:hidden}
  .cv .photo img{display:block;width:100%;height:100%;object-fit:cover}
  .cv .photo .tone{position:absolute;inset:0;background:#972010;mix-blend-mode:soft-light;opacity:.5}
  .cv .photo .fade{position:absolute;inset:0}
  .cv .demand p{max-width:none}
  .cv h1 small{display:block;margin-top:2.4mm;font:300 italic 17pt/1.1 'Noto Serif Display',serif;color:#F3B7B3}
  .cv .sub{max-width:118mm;margin-top:4mm;font-size:8.8pt}
  .cv .demand{top:124mm}
  .cv .demand h2{font-size:15pt}
  .cv .notif.n1{top:139mm}.cv .notif.n2{top:157mm}.cv .notif.n3{top:175mm}
'''

def leaflet(cls, label, inner, hero, css, slogan):
    body = f'''<!-- ════════════════════════ FRONT · {label} ════════════════════════ -->
<section class="page front cv {cls}" aria-label="Μπροστινή όψη">
{inner}
  {seal}
  <div class="logo wm">Zenday</div>
  <div class="hero">
{hero}
  </div>
{lower}</section>

'''
    html = base[:fs] + body + base[fe:]
    html = html.replace('<h4>Σήμερα<br><em>είναι</em> <span class="wm">Zenday</span>.</h4>', f'<h4>{SLOGANS[slogan]}</h4>')
    return html.replace('</style>', COVER_CSS + css + '</style>', 1)

pieces = {}

# 01 · Zen at home — the massage photo from zenday.gr, warmed, towel faded into oxblood
pieces['01-leaflet-zen-at-home'] = leaflet('c1', '01 · ZEN AT HOME',
    '  <div class="photo"><img src="img/zen-massage.jpg" alt=""><div class="tone"></div><div class="fade"></div></div>',
    '    <h1>Ομορφιά &amp; ευεξία<br><em>στο σπίτι.</em></h1>\n    ' + SUB, '''
  .c1 .photo{height:106mm}
  .c1 .photo img{object-position:30% 50%;filter:sepia(.3) saturate(.85) contrast(1.04)}
  .c1 .photo .fade{background:linear-gradient(180deg,rgba(73,16,9,.75) 0,rgba(73,16,9,.15) 18mm,rgba(73,16,9,0) 30mm,rgba(73,16,9,0) 52mm,rgba(73,16,9,.88) 78mm,#491009 100mm)}
  .c1 .seal{left:114mm;top:12mm;width:26mm;height:26mm;filter:drop-shadow(0 1mm 3mm rgba(20,4,2,.5))}
  .c1 .hero{top:73mm}
  .c1 h1{font-size:32pt;line-height:.98}
''', 'make-every-day')

# 02 · Ding-dong — the doorbell, duotoned
pieces['02-leaflet-ding-dong'] = leaflet('c2', '02 · DING-DONG',
    '  <div class="duo"><img src="img/doorbell.jpg" alt=""><div class="tint"></div><div class="gold"></div><div class="fade"></div></div>\n'
    '  <div class="ring" aria-hidden="true"><i></i><i></i><i></i></div>',
    '    <h1>Ντιν-ντον.<small>Ομορφιά &amp; ευεξία στο σπίτι.</small></h1>\n    ' + SUB.replace('<br>', ' '), '''
  .c2 .duo{position:absolute;left:0;top:0;width:154mm;height:104mm;overflow:hidden;background:#491009}
  .c2 .duo img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.6) brightness(1.3);mix-blend-mode:screen}
  .c2 .duo .tint{position:absolute;inset:0;background:#F3B7B3;mix-blend-mode:multiply}
  .c2 .duo .gold{position:absolute;inset:0;background:radial-gradient(22mm 22mm at 45.5% 47%,rgba(198,166,100,.55),transparent 70%);mix-blend-mode:screen}
  .c2 .duo .fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(73,16,9,.5) 0,rgba(73,16,9,0) 22mm,rgba(73,16,9,0) 50mm,#491009 102mm)}
  .c2 .ring{position:absolute;left:70mm;top:49mm;width:0;height:0}
  .c2 .ring i{position:absolute;left:0;top:0;border:.3mm solid #C6A664;border-radius:50%;transform:translate(-50%,-50%)}
  .c2 .ring i:nth-child(1){width:30mm;height:30mm;opacity:.8}
  .c2 .ring i:nth-child(2){width:44mm;height:44mm;opacity:.45}
  .c2 .ring i:nth-child(3){width:60mm;height:60mm;opacity:.2}
  .c2 .seal{left:115mm;top:11mm;width:26mm;height:26mm}
  .c2 .hero{top:70mm}
  .c2 h1{font-size:40pt;line-height:.95}
''', 'every-day-is')

# 03 · Λ window — «Η τέχνη σας, στο σπίτι τους.»
pieces['03-leaflet-lambda-window'] = leaflet('c3', '03 · Λ WINDOW', '''  <svg class="win" viewBox="0 0 154 216" aria-hidden="true">
    <defs><clipPath id="lam"><path d="M114 27 L68 112 L160 112 Z"/></clipPath>
      <linearGradient id="lamfade" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#491009" stop-opacity="0"/><stop offset="1" stop-color="#491009" stop-opacity=".55"/></linearGradient></defs>
    <g clip-path="url(#lam)">
      <image href="img/hairdresser.jpg" x="36" y="34" width="146" height="97.5" preserveAspectRatio="xMidYMid slice"/>
      <rect x="60" y="27" width="100" height="86" fill="url(#lamfade)"/>
    </g>
    <path d="M68 112 L114 27 L160 112" fill="none" stroke="#C6A664" stroke-width=".45" stroke-linecap="round"/>
  </svg>''',
    '    <p class="kicker eyebrow">Ομορφιά &amp; ευεξία στο σπίτι</p>\n    <h1>Η τέχνη σας,<br><em>στο σπίτι</em><br><em>τους.</em></h1>\n    ' + SUB, '''
  .c3 .win{position:absolute;inset:0;width:100%;height:100%}
  .c3 .seal{left:100mm;top:13mm;width:28mm;height:28mm}
  .c3 .hero{top:48mm}
  .c3 h1{font-size:29pt;line-height:1.04}
  .c3 .sub{position:absolute;top:64mm;left:0;max-width:118mm;margin:0}
  .c3 .demand{top:131mm}
  .c3 .notif.n1{top:145mm}.c3 .notif.n2{top:163mm}.c3 .notif.n3{top:181mm}
''', 'make-your-day')

# ───────────────────────────── small pieces ─────────────────────────────
HEAD = base[:base.index('<style>') + len('<style>')]
FONTS = '\n'.join(l for l in base.splitlines() if '@font-face' in l)
ROOT = '''
  :root{--oxblood:#491009;--brick:#972010;--cream:#F7ECE4;--sand:#F3EBE5;--blush:#FEDADB;--rose:#F3B7B3;--gold:#C6A664}
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{background:#2a2a2a}
  body{font-family:Manrope,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;text-rendering:geometricPrecision}
  .wm{font-family:'Zenday Wordmark',serif;font-weight:400;letter-spacing:0;white-space:nowrap}
  .k{font:800 5.6pt/1.3 Manrope,sans-serif;letter-spacing:.24em;text-transform:uppercase}
  em{font-style:italic;font-weight:300}
  .page{position:relative;overflow:hidden;margin:0 auto 10mm;break-after:page}
  .page:last-child{margin-bottom:0}
  .die{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
  @media print{html,body{background:none}.page{margin:0}}
'''
DIECOL = '#e5007e'  # die-cut line colour: put on its own spot layer, never printed

def doc(title, w, h, note, css, pages):
    return f'''<!doctype html>
<html lang="el"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<!-- {note} -->
<style>
{FONTS}
{ROOT}
  @page{{size:{w}mm {h}mm;margin:0}}
  .page{{width:{w}mm;height:{h}mm}}
{css}
</style></head><body>
{pages}
</body></html>
'''

def die_hanger():
    return (f'<svg class="die" viewBox="0 0 96 236" aria-hidden="true"><g fill="none" stroke="{DIECOL}" stroke-width=".3" stroke-dasharray="1.4 1">'
            '<circle cx="48" cy="33" r="17"/><path d="M48 16 V3"/><rect x="3" y="3" width="90" height="230" rx="4"/></g></svg>')

# 04 · Door hanger — 90 × 230 mm + 3 mm bleed
pieces['04-door-hanger'] = doc('Zenday Door Hanger', 96, 236,
    'Door hanger · 90 × 230 mm trim + 3 mm bleed. Magenta dashed = die-cut (hole Ø34 mm + slit, r4 corners): own spot layer, do not print. Side A hangs on the client\'s door; side B speaks to freelancers.', '''
  .a{background:radial-gradient(70mm 90mm at 70% 70%,rgba(151,32,16,.55),transparent 70%),var(--oxblood);color:var(--cream)}
  .a .roof{position:absolute;inset:0;width:100%;height:100%}
  .a .txt{position:absolute;left:11mm;right:11mm;top:78mm}
  .a .k{color:var(--gold)}
  .a h1{margin-top:5mm;font:400 38pt/.95 'Noto Serif Display',serif}
  .a h2{margin-top:6mm;font:300 italic 19pt/1.12 'Noto Serif Display',serif;color:var(--rose)}
  .a .shh{margin-top:8mm;font:500 8pt/1.5 Manrope,sans-serif;color:rgba(247,236,228,.75)}
  .a .eng{margin-top:10mm;font:400 italic 11pt/1.2 'Noto Serif Display',serif;color:var(--gold)}
  .a .eng .wm{font-style:normal;font-size:9pt}
  .a .foot{position:absolute;left:11mm;right:11mm;bottom:13mm;display:flex;justify-content:space-between;align-items:flex-end;border-top:.25mm solid rgba(198,166,100,.5);padding-top:4mm}
  .a .foot .wm{font-size:12pt}
  .a .foot span:not(.wm){font:600 6pt/1.3 Manrope,sans-serif;letter-spacing:.1em;color:rgba(247,236,228,.7);text-align:right}
  .b{background:var(--cream);color:var(--oxblood)}
  .b .txt{position:absolute;left:11mm;right:11mm;top:60mm}
  .b .k{color:var(--brick)}
  .b h1{margin-top:3mm;font:400 22pt/1.02 'Noto Serif Display',serif}
  .b h1 em{color:var(--brick)}
  .b .lead{margin-top:3.5mm;font:500 7.6pt/1.45 Manrope,sans-serif;color:rgba(73,16,9,.8)}
  .b ul{list-style:none;margin-top:5mm;display:grid;gap:2.2mm}
  .b li{display:flex;gap:2.4mm;align-items:center;font:600 7.8pt/1.2 Manrope,sans-serif}
  .b li i{flex:none;width:4.6mm;height:4.6mm;border-radius:50%;background:var(--blush);display:grid;place-items:center;font-style:normal;color:var(--brick);font-size:6pt}
  .b .cta{position:absolute;left:0;right:0;bottom:0;height:70mm;padding:8mm 11mm 11mm;background:var(--oxblood);color:var(--cream);display:grid;grid-template-columns:1fr 27mm;gap:4mm;align-items:center}
  .b .cta h3{font:400 14pt/1.08 'Noto Serif Display',serif;white-space:nowrap}
  .b .cta h3 em{color:var(--rose)}
  .b .cta h3 .wm{font-size:10.5pt;color:var(--rose)}
  .b .cta p{margin-top:2.4mm;font:800 5.4pt/1.5 Manrope,sans-serif;letter-spacing:.16em;color:var(--rose)}
  .b .cta .sig{display:block;margin-top:4mm;font-size:10pt}
  .b .qr{background:var(--cream);border-radius:2.6mm;padding:2.4mm}
  .b .qr img{display:block;width:100%}
''', f'''<section class="page a" aria-label="Πλευρά Α — για την πόρτα του πελάτη">
  <svg class="roof" viewBox="0 0 96 236" aria-hidden="true"><path d="M16 72 L48 58 L80 72" fill="none" stroke="#C6A664" stroke-width=".35" opacity=".9"/><path d="M48 55.6 l1.4 2.4 -1.4 2.4 -1.4 -2.4z" fill="#C6A664"/></svg>
  <div class="txt">
    <p class="k">Σσσ… ραντεβού σε εξέλιξη</p>
    <h1>Μην<br>ενοχλείτε.</h1>
    <h2>Ομορφιά &amp; ευεξία<br>σε εξέλιξη.</h2>
    <p class="shh">Μέσα, κάποιος κάνει χρόνο για τον εαυτό του.<br>Θα τα πούμε σε λίγο.</p>
    <p class="eng">Shhh… it’s a <span class="wm">Zenday</span>.</p>
  </div>
  <div class="foot"><span class="wm">Zenday</span><span>ΟΜΟΡΦΙΑ &amp; ΕΥΕΞΙΑ<br>ΣΤΟ ΣΠΙΤΙ · ZENDAY.GR</span></div>
  {die_hanger()}
</section>
<section class="page b" aria-label="Πλευρά Β — για freelancers">
  <div class="txt">
    <p class="k">Για freelancers ομορφιάς &amp; ευεξίας</p>
    <h1>Κρεμάστε το<br><em>στην επόμενη πόρτα.</em></h1>
    <p class="lead">Η πρώτη πλατφόρμα στην Ελλάδα για online κρατήσεις κατ’&nbsp;οίκον — για όσους έχουν ήδη δουλειά, κάνουν το πρώτο τους βήμα ή δουλεύουν μόνοι.</p>
    <ul>
      <li><i>✓</i>Ραντεβού ήδη πληρωμένα</li>
      <li><i>✓</i>Δικές σας τιμές, ώρες &amp; περιοχές</li>
      <li><i>✓</i>Με ή χωρίς επαγγελματικό ΑΦΜ</li>
      <li><i>✓</i>Δίκαιες συμφωνίες, καμία δέσμευση</li>
    </ul>
  </div>
  <div class="cta">
    <div><h3>Make every day<br><em>a</em> <span class="wm">Zenday</span>.</h3><p>ΣΚΑΝΑΡΕΤΕ · ΔΩΡΕΑΝ ΕΓΓΡΑΦΗ</p><span class="wm sig">Zenday</span></div>
    <div class="qr"><img src="qr-hanger.svg" alt="QR εγγραφής"></div>
  </div>
  {die_hanger()}
</section>''')

# 05 · Key tag — 46 × 96 mm + 3 mm bleed
KT_DIE = (f'<svg class="die" viewBox="0 0 52 102" aria-hidden="true"><g fill="none" stroke="{DIECOL}" stroke-width=".3" stroke-dasharray="1.2 .9">'
          '<path d="M3 26 A23 23 0 0 1 49 26 V93 A6 6 0 0 1 43 99 H9 A6 6 0 0 1 3 93 Z"/><circle cx="26" cy="15" r="5"/></g></svg>')
pieces['05-key-tag'] = doc('Zenday Key Tag', 52, 102,
    'Key tag · 46 × 96 mm trim + 3 mm bleed, arched top r23, hole Ø10 mm. Magenta dashed = die-cut. Suggest 600 µm laminated card or PVC.', '''
  .a{background:var(--oxblood);color:var(--cream);text-align:center}
  .a .k{position:absolute;left:0;right:0;top:28mm;color:var(--gold);font-size:4.6pt}
  .a h3{position:absolute;left:7mm;right:7mm;top:35mm;font:400 16pt/1.02 'Noto Serif Display',serif}
  .a h3 em{color:var(--rose)}
  .a .wm{position:absolute;left:0;right:0;bottom:10mm;font-size:8pt}
  .b{background:var(--cream);color:var(--oxblood);text-align:center}
  .b img{position:absolute;left:11mm;top:29mm;width:30mm}
  .b h3{position:absolute;left:5mm;right:5mm;top:64mm;font:400 11pt/1.05 'Noto Serif Display',serif}
  .b h3 em{color:var(--brick)}
  .b h3 .wm{font-size:8.5pt;color:var(--brick)}
  .b .k{position:absolute;left:0;right:0;bottom:11mm;font-size:4.4pt;color:var(--brick)}
''', f'''<section class="page a" aria-label="Μπροστά"><p class="k">Για freelancers</p><h3>Το κλειδί<br>για νέους<br><em>πελάτες.</em></h3><span class="wm">Zenday</span>{KT_DIE}</section>
<section class="page b" aria-label="Πίσω"><img src="qr.svg" alt="QR εγγραφής"><h3>Every day<br><em>is</em> <span class="wm">Zenday</span>.</h3><p class="k">Σκανάρετε · δωρεάν εγγραφή</p>{KT_DIE}</section>''')

# 06 · Thank-you card — 85 × 55 mm + 3 mm bleed
pieces['06-thank-you-card'] = doc('Zenday Thank-you Card', 91, 61,
    'Thank-you card · 85 × 55 mm trim + 3 mm bleed. The freelancer signs it and leaves it for the client. Back QR → zenday.gr (client side).', '''
  .a{background:var(--cream);color:var(--oxblood);padding:9mm 10mm}
  .a h3{font:400 14pt/1.08 'Noto Serif Display',serif}
  .a h3 em{color:var(--brick)}
  .a .sig{position:absolute;left:10mm;right:10mm;bottom:11mm;display:flex;justify-content:space-between;align-items:flex-end;font:500 6.6pt/1 Manrope,sans-serif;color:rgba(73,16,9,.6)}
  .a .sig b{display:inline-block;width:36mm;border-bottom:.25mm solid rgba(73,16,9,.4);margin-left:1.5mm}
  .a .sig .wm{font-size:7.5pt;color:var(--oxblood)}
  .b{background:var(--oxblood);color:var(--cream);padding:9mm 10mm;display:grid;grid-template-columns:1fr 22mm;gap:5mm;align-items:center}
  .b h3{font:400 12.5pt/1.1 'Noto Serif Display',serif}
  .b h3 em{color:var(--rose)}
  .b p{margin-top:2mm;font:800 4.8pt/1.5 Manrope,sans-serif;letter-spacing:.16em;color:var(--gold)}
  .b .eng{margin-top:1.6mm;font:400 italic 8pt/1.2 'Noto Serif Display',serif;letter-spacing:0;color:var(--rose)}
  .b .eng .wm{font-style:normal;font-size:6.6pt}
  .b .q{background:var(--cream);border-radius:1.6mm;padding:1.6mm}
  .b .q img{display:block;width:100%}
''', '''<section class="page a" aria-label="Μπροστά"><h3>Ευχαριστώ που μου<br><em>ανοίξατε την πόρτα.</em></h3><div class="sig"><span>Με αγάπη,<b></b></span><span class="wm">Zenday</span></div></section>
<section class="page b" aria-label="Πίσω"><div><h3>Την επόμενη φορά,<br><em>κλείστε με στο Zenday.</em></h3><p>ΟΜΟΡΦΙΑ &amp; ΕΥΕΞΙΑ ΣΤΟ ΣΠΙΤΙ</p><p class="eng">Make your day a <span class="wm">Zenday</span>.</p></div><div class="q"><img src="qr-client.svg" alt="QR zenday.gr"></div></section>''')

# 07 · Sticker — Ø60 mm round + 2 mm bleed
pieces['07-sticker'] = doc('Zenday Sticker', 64, 64,
    'Round sticker · Ø60 mm + 2 mm bleed. Magenta dashed = kiss-cut. For laptops, mirrors, kit cases — and for the leaflet bag at the stand.', '''
  .s{background:radial-gradient(40mm 40mm at 50% 30%,#6a1a10,var(--oxblood) 70%);color:var(--cream)}
  .s svg.t{position:absolute;inset:0;width:100%;height:100%}
''', f'''<section class="page s" aria-label="Sticker">
  <svg class="t" viewBox="0 0 64 64" aria-hidden="true">
    <defs><path id="r" d="M32 32 m-24.2 0 a24.2 24.2 0 1 1 48.4 0 a24.2 24.2 0 1 1 -48.4 0"/></defs>
    <circle cx="32" cy="32" r="27.4" fill="none" stroke="#C6A664" stroke-width=".35"/>
    <circle cx="32" cy="32" r="20.6" fill="none" stroke="#C6A664" stroke-width=".18"/>
    <text font-family="Manrope" font-weight="800" font-size="2.7" letter-spacing=".5" fill="#C6A664"><textPath href="#r" textLength="150" lengthAdjust="spacing">ΟΜΟΡΦΙΑ &amp; ΕΥΕΞΙΑ ΣΤΟ ΣΠΙΤΙ ◆ ZENDAY.GR ◆</textPath></text>
    <text x="32" y="28.6" text-anchor="middle" font-family="Noto Serif Display" font-style="italic" font-weight="300" font-size="5.6" fill="#F3B7B3">Every day is</text>
    <text x="32" y="37.6" text-anchor="middle" font-family="Zenday Wordmark" font-size="7.4" fill="#F7ECE4">Zenday</text>
    <path d="M32 41.4 l1 1.7 -1 1.7 -1 -1.7z" fill="#C6A664"/>
    <circle cx="32" cy="32" r="30" fill="none" stroke="{DIECOL}" stroke-width=".3" stroke-dasharray="1.2 .9"/>
  </svg>
</section>''')

# 08 · Tote bag — print area 300 × 360 mm
pieces['08-tote-bag'] = doc('Zenday Tote Bag', 300, 360,
    'Tote bag print · artwork 300 × 360 mm, natural or oxblood cotton bag. Screen-print in 2 spot colours: cream + gold (or foil gold).', '''
  .t{background:var(--oxblood);color:var(--cream)}
  .t svg{position:absolute;inset:0;width:100%;height:100%}
''', '''<section class="page t" aria-label="Tote bag">
  <svg viewBox="0 0 300 360" aria-hidden="true">
    <g fill="none" stroke="#C6A664" stroke-linecap="round"><path d="M40 150 L150 60 L260 150" stroke-width="1.6"/><path d="M150 52 l5 8 -5 8 -5 -8z" fill="#C6A664" stroke="none"/></g>
    <text x="150" y="200" text-anchor="middle" font-family="Noto Serif Display" font-weight="400" font-size="34" fill="#F7ECE4">Make every day</text>
    <text x="150" y="246" text-anchor="middle" font-family="Noto Serif Display" font-style="italic" font-weight="300" font-size="34" fill="#F3B7B3">a <tspan font-family="Zenday Wordmark" font-style="normal" font-size="30" fill="#F7ECE4">Zenday</tspan>.</text>
    <line x1="120" y1="282" x2="180" y2="282" stroke="#C6A664" stroke-width=".8"/>
    <text x="150" y="304" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="8" letter-spacing="2.4" fill="#C6A664">ΟΜΟΡΦΙΑ &amp; ΕΥΕΞΙΑ ΣΤΟ ΣΠΙΤΙ</text>
  </svg>
</section>''')

# 09 · Stand entrance — concept visual (landscape, not for print)
pieces['09-stand-entrance'] = doc('Zenday Stand Entrance', 297, 210,
    'Stand concept · the entrance is a front door: gold Λ roof, real doorbell, «Καλώς ήρθατε» doormat. Visual for the stand builder, not a print file.', '''
  .st{background:linear-gradient(#f6eee8 0,#efe4dc 68%,#d9cbbf 68%,#cdbdb0 100%)}
  .st svg{position:absolute;inset:0;width:100%;height:100%}
  .st .cap{position:absolute;left:26mm;bottom:9mm;width:150mm;color:var(--oxblood)}
  .st .cap .k{color:var(--brick)}
  .st .cap h2{margin-top:1.6mm;font:400 18pt/1.05 'Noto Serif Display',serif}
  .st .cap h2 em{color:var(--brick)}
  .st .cap p{margin-top:1.6mm;font:500 8pt/1.45 Manrope,sans-serif;color:rgba(73,16,9,.8)}
''', '''<section class="page st" aria-label="Περίπτερο">
  <svg viewBox="0 0 297 210" aria-hidden="true">
    <!-- side walls -->
    <rect x="26" y="40" width="76" height="103" fill="#491009"/><rect x="198" y="40" width="76" height="103" fill="#491009"/>
    <text x="64" y="78" text-anchor="middle" font-family="Noto Serif Display" font-size="7.6" fill="#F7ECE4">Ομορφιά &amp; ευεξία</text>
    <text x="64" y="89" text-anchor="middle" font-family="Noto Serif Display" font-style="italic" font-weight="300" font-size="7.6" fill="#F3B7B3">στο σπίτι.</text>
    <text x="236" y="78" text-anchor="middle" font-family="Noto Serif Display" font-size="7.6" fill="#F7ECE4">Every day</text>
    <text x="236" y="89" text-anchor="middle" font-family="Noto Serif Display" font-style="italic" font-weight="300" font-size="7.6" fill="#F3B7B3">is <tspan font-family="Zenday Wordmark" font-style="normal" font-size="6.6" fill="#F7ECE4">Zenday</tspan>.</text>
    <!-- the door -->
    <path d="M108 52 L150 18 L192 52" fill="none" stroke="#C6A664" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M150 11 l3 5 -3 5 -3 -5z" fill="#C6A664"/>
    <rect x="118" y="52" width="64" height="91" fill="#5e1a10"/>
    <rect x="122" y="56" width="56" height="87" fill="#6d2214" stroke="#C6A664" stroke-width=".6"/>
    <rect x="127" y="62" width="46" height="34" fill="none" stroke="#C6A664" stroke-width=".35" opacity=".7"/>
    <rect x="127" y="101" width="46" height="36" fill="none" stroke="#C6A664" stroke-width=".35" opacity=".7"/>
    <text x="150" y="83" text-anchor="middle" font-family="Zenday Wordmark" font-size="8.5" fill="#F7ECE4">Zenday</text>
    <text x="150" y="122" text-anchor="middle" font-family="Noto Serif Display" font-style="italic" font-weight="300" font-size="7" fill="#F3B7B3">Περάστε.</text>
    <circle cx="173" cy="100" r="1.8" fill="#C6A664"/>
    <!-- the doorbell -->
    <g transform="translate(188 98)"><circle r="3" fill="#C6A664"/><circle r="6" fill="none" stroke="#C6A664" stroke-width=".4"/><circle r="9.5" fill="none" stroke="#C6A664" stroke-width=".3" opacity=".6"/><circle r="13.5" fill="none" stroke="#C6A664" stroke-width=".2" opacity=".35"/></g>
    <text x="188" y="117" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="1.9" letter-spacing=".5" fill="#491009">ΝΤΙΝ-ΝΤΟΝ</text>
    <!-- doormat -->
    <path d="M118 150 h64 l8 14 h-80z" fill="#972010"/>
    <text x="150" y="159.4" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="4.2" letter-spacing="1" fill="#F7ECE4">ΚΑΛΩΣ ΗΡΘΑΤΕ</text>
  </svg>
  <div class="cap">
    <p class="k">Το περίπτερο είναι μια πόρτα</p>
    <h2>Ντιν-ντον. <em>Περάστε.</em></h2>
    <p>Οι άλλοι έχουν πάγκους — εμείς έχουμε εξώπορτα. Στέγη-Λ σε χρυσό, χαλάκι «Καλώς ήρθατε» και αληθινό κουδούνι: ο επισκέπτης χτυπάει, του ανοίγουμε, και ο ήχος ακούγεται σε όλη την έκθεση.</p>
  </div>
</section>''')

for name, html in pieces.items():
    (D / f'{name}.html').write_text(html)
    print('wrote', name)
