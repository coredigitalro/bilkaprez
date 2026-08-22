#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator static — montaj-acoperis-top.ro
Rulează:  python3 build.py
Scrie toate paginile HTML în rădăcina proiectului.
"""
import os, json, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ date firmă
B = {
    "name":     "BilkaRoofMontaj",
    "legal":    "BilkaRoofMontaj",
    "tagline":  "Acoperișuri · Mansardări",
    "domain":   "https://montaj-acoperis-top.ro",
    "tel_disp": "0758 680 276",
    "tel_raw":  "+40758680276",
    "wa":       "40758680276",
    "street":   "Strada Martir Ion Miron 29",
    "city":     "Timișoara",
    "zip":      "300254",
    "region":   "Timiș",
    "maps":     "https://maps.app.goo.gl/5yu8v53zWMhieLG68",
    "rating":   "5,0",
    "reviews":  48,
    "years":    10,
    "projects": 180,
    "founded":  "2016",
    "email":    "bilkaroofmasters@gmail.com",
}
WA_TXT = "Bun%C4%83%20ziua%21%20A%C8%99%20dori%20o%20ofert%C4%83%20pentru%20lucr%C4%83ri%20la%20acoperi%C8%99."
WA_LINK = f"https://wa.me/{B['wa']}?text={WA_TXT}"
TEL = f"tel:{B['tel_raw']}"

CITIES = ["Timișoara", "Arad", "Lugoj", "Reșița", "Caransebeș", "Deva", "Hunedoara", "Cluj-Napoca"]

# ------------------------------------------------------------------ navigație
NAV = [
    ("servicii",            "/servicii/",            "Servicii"),
    ("lucrari",             "/lucrari/",             "Lucrări"),
    ("recenzii",            "/recenzii/",            "Recenzii"),
    ("calculator-pret",     "/calculator-pret/",     "Calculator preț"),
    ("intrebari-frecvente", "/intrebari-frecvente/", "Întrebări"),
    ("despre",              "/despre/",              "Despre noi"),
    ("contact",             "/contact/",             "Contact"),
]

# ------------------------------------------------------------------ conținut
SERVICES = [
    dict(k="inlocuire", tag="Cel mai cerut", img="svc-metalica.jpg",
         t="Înlocuire acoperiș",
         s="Demontăm învelitoarea veche și montăm un acoperiș nou, complet.",
         d="Demontăm învelitoarea veche, verificăm starea șarpantei și refacem acoperișul strat cu strat: astereală, folie anticondens, contrașipci, șipci, învelitoare și tinichigerie. Vă spunem înainte de start ce s-ar putea găsi sub țiglă și cum se tarifează, ca să nu apară surprize la mijlocul lucrării."),
    dict(k="montaj-nou", tag="Case noi", img="svc-ceramica.jpg",
         t="Montaj acoperiș nou",
         s="Executăm acoperișul unei case noi, de la șarpantă la ultimul accesoriu.",
         d="Preluăm acoperișul unei case în construcție de la structura de lemn până la jgheaburi. Dimensionăm șarpanta corect pentru deschidere și pentru încărcarea din zăpadă, montăm straturile în ordinea corectă și închidem toate racordurile: coame, dolii, coșuri, lucarne."),
    dict(k="reparatii", tag="Urgențe", img="svc-reparatii.jpg",
         t="Reparații și infiltrații",
         s="Găsim sursa reală a infiltrației și reparăm punctual.",
         d="O pată pe tavan apare rareori exact sub gaură. Urmărim traseul apei și reparăm cauza: țigle sparte sau deplasate, coame desfăcute, dolii ruginite, șorțuri lipsă la coș, folie ruptă. Pentru infiltrații active ne organizăm cât putem de repede."),
    dict(k="dulgherie", tag="Structură", img="svc-dulgherie.jpg",
         t="Dulgherie și șarpantă",
         s="Executăm și consolidăm structura de lemn a acoperișului.",
         d="Construim șarpante noi și consolidăm sau înlocuim elemente atacate de umezeală și carii. Lemnul se tratează ignifug și antifungic înainte de montaj, iar îmbinările se execută astfel încât structura să lucreze ca un tot, nu ca o sumă de grinzi."),
    dict(k="mansardari", tag="Spațiu în plus", img="svc-sandwich.jpg",
         t="Mansardări",
         s="Transformăm podul într-o cameră locuibilă, izolată corect.",
         d="Închidem podul cu structură, izolație de grosime corectă, barieră de vapori montată continuu și finisaje. Cele mai multe mansarde reci sau cu condens provin dintr-o barieră de vapori pusă neetanș, nu din prea puțină vată, așa că acolo insistăm."),
    dict(k="hidroizolatii", tag="Terase", img="svc-hidroizolatii.jpg",
         t="Hidroizolații și terase",
         s="Hidroizolăm terase și acoperișuri de tip terasă.",
         d="Curățăm suportul, refacem panta acolo unde apa băltește și montăm membrana cu suprapuneri sudate corect. Tratăm separat punctele unde cedează în practică o terasă: gurile de scurgere, atice și racordurile la pereți."),
    dict(k="jgheaburi", tag="Pluvial", img="svc-jgheaburi.jpg",
         t="Jgheaburi și burlane",
         s="Montăm și reparăm sisteme pluviale, cu pantă corectă.",
         d="Dimensionăm jgheabul după suprafața acoperișului și îl montăm cu panta necesară către burlan. Un sistem subdimensionat sau montat orizontal se revarsă la ploi puternice și udă fațada și fundația, chiar dacă arată bine."),
    dict(k="lindab", tag="Tablă fălțuită", img="svc-lindab.jpg",
         t="Tablă fălțuită și Lindab",
         s="Învelitori din tablă prefaltată, montate cu fălț dublu.",
         d="Montăm tablă fălțuită pe astereală continuă, cu agrafe care permit dilatarea. Este soluția potrivită pentru pante mici, forme complicate și pentru case unde se dorește o linie curată, fără profil de țiglă."),
    dict(k="sindrila", tag="Bituminoasă", img="svc-sindrila.jpg",
         t="Șindrilă bituminoasă",
         s="Soluție ușoară pentru forme complicate și anexe.",
         d="Șindrila urmează forme pe care țigla nu le poate acoperi curat și încarcă foarte puțin structura. Se montează pe astereală continuă, cu folie de sub-acoperiș și cu bandă de start lipită corect la streașină."),
]

WORKS = [
    ("pf-01.jpg", "Înlocuire", "Acoperiș nou din țiglă metalică antracit", "Casă individuală, Timișoara"),
    ("pf-02.jpg", "Renovare",  "De la tablă veche la țiglă metalică nouă", "Casă la curte, jud. Timiș"),
    ("pf-03.jpg", "Montaj",    "Acoperiș executat la casă nouă",           "Construcție nouă, Arad"),
    ("pf-04.jpg", "Dulgherie", "Șarpantă refăcută integral",               "Casă veche, Lugoj"),
    ("pf-05.jpg", "Pluvial",   "Jgheaburi și burlane înlocuite complet",   "Casă cu etaj, Timișoara"),
    ("pf-06.jpg", "Mansardare","Pod transformat în spațiu locuibil",       "Locuință, jud. Timiș"),
]

REVIEWS = [
    ("Vasile P.", "Timișoara",  "Ne-au făcut acoperișul la casă și la magazie. Prețul a rămas cel spus de la început, fără să apară costuri pe parcurs."),
    ("Ionel M.",  "Arad",       "Au înlocuit tabla veche cu țiglă metalică în trei zile. De atunci e uscat în pod, chiar și după ploile de vară."),
    ("Gheorghe D.","Lugoj",     "Am pus țiglă nouă pe casa părintească. Oameni de cuvânt, au strâns tot molozul la final."),
    ("Adriana S.","Timișoara",  "Aveam infiltrație de doi ani și nimeni nu găsea de unde vine. Au urmărit traseul apei și au reparat racordul la coș."),
    ("Mircea T.", "Caransebeș", "Mansardarea a ieșit exact cum am discutat. Iarna trecută nu am mai avut condens în pod."),
    ("Florin C.", "Reșița",     "Deviz clar, pe etape. Am putut compara cu alte două oferte și am văzut exact ce lipsea la ele."),
]

FAQ = [
    ("Ce fel de lucrări executați?",
     ["Tot ce ține de acoperiș: înlocuire, renovare, montaj la case noi, reparații și infiltrații, dulgherie și șarpante, mansardări, jgheaburi și burlane, hidroizolații și terase. Montăm și tablă fălțuită, șindrilă bituminoasă, ferestre de mansardă și luminatoare."]),
    ("Lucrați cu materialele dumneavoastră sau cu ale mele?",
     ["Executăm manopera. Vă calculăm necesarul exact de materiale, vă recomandăm furnizori de încredere și cumpărați direct de la ei, la prețul lor.",
      "Așa vedeți separat cât plătiți pe materiale și cât pe manoperă, fără adaos ascuns între cele două."]),
    ("Îmi puteți da un preț la telefon?",
     ["Vă putem spune la telefon cum stau lucrurile în general și la ce să vă așteptați, dar un preț real vine după măsurătoare.",
      "Suprafața reală a unui acoperiș este mai mare decât amprenta casei, uneori cu 30 până la 50 la sută, în funcție de pantă și de formă. Un preț dat fără măsurători aproape întotdeauna crește pe parcurs. Deplasarea și măsurătoarea sunt gratuite."]),
    ("În ce zone lucrați?",
     [f"Baza noastră este în {B['city']}. Lucrăm curent în Timiș, Arad, Caraș-Severin, Hunedoara și Cluj, iar pentru lucrări mai mari ne deplasăm în toată țara.",
      "Deplasarea pentru evaluare și măsurători este gratuită."]),
    ("Cine execută efectiv lucrarea?",
     ["Echipa noastră. Nu subcontractăm lucrările către echipe găsite pentru un singur proiect, tocmai ca să existe un singur responsabil pentru toate etapele și cineva la care puteți reveni după finalizare."]),
    ("Ce garanție oferiți?",
     ["Oferim garanție scrisă la manoperă pentru toate lucrările executate de echipa noastră. Garanția materialelor vine de la producătorul pe care îl alegeți, iar un montaj corect este chiar condiția ca acea garanție să rămână valabilă."]),
    ("Cât durează o lucrare?",
     ["O înlocuire de acoperiș la o casă obișnuită durează în general între trei și șapte zile lucrătoare, în funcție de suprafață, de formă și de starea șarpantei. O reparație punctuală se rezolvă de obicei într-o zi.",
      "Vă dăm un termen în ofertă și vă anunțăm din timp dacă vremea ne obligă să îl decalăm."]),
    ("Se poate lucra iarna?",
     ["Da, pentru reparații și pentru intervenții de urgență. Înlocuirile mari le programăm în sezon, pentru că acoperișul stă desfăcut o parte din timp și nu vrem să lăsăm casa descoperită pe ninsoare."]),
    ("Se poate plăti în rate?",
     ["Pentru lucrările mai mari putem eșalona plata pe etapele lucrării. Ne spuneți la telefon ce variantă v-ar conveni și vedem ce se poate face."]),
    ("Ce se întâmplă dacă apar surprize după ce se demontează?",
     ["La acoperișurile vechi, starea reală a lemnului se vede abia după ce se scoate învelitoarea. Vă spunem de la început ce ar putea apărea și cât costă fiecare situație, apoi vă sunăm și vă arătăm înainte să lucrăm ceva ce nu era în deviz."]),
]

# ------------------------------------------------------------------ blocuri
LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true">'
        '<rect width="32" height="32" rx="8" fill="#161E27"/>'
        '<path d="M4.5 17.5 L16 7 L27.5 17.5" stroke="#F0A500" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
        '<path d="M8.5 16.5 V25 H23.5 V16.5" stroke="#FFFFFF" stroke-width="2.6" '
        'stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')


def head(title, desc, path, og_img="hero-1.jpg", extra_ld=None):
    url = B["domain"] + path
    ld = {
        "@context": "https://schema.org",
        "@type": "RoofingContractor",
        "@id": B["domain"] + "/#business",
        "name": B["name"],
        "description": "Înlocuire, montaj și reparații acoperișuri, dulgherie, mansardări, hidroizolații și jgheaburi.",
        "telephone": B["tel_raw"],
        "url": B["domain"] + "/",
        "image": f"{B['domain']}/images/{og_img}",
        "hasMap": B["maps"],
        "address": {"@type": "PostalAddress", "streetAddress": B["street"],
                    "addressLocality": B["city"], "postalCode": B["zip"],
                    "addressRegion": B["region"], "addressCountry": "RO"},
        "areaServed": [{"@type": "City", "name": c} for c in CITIES],
        "priceRange": "$$",
        "foundingDate": B["founded"] + "-01-01",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "07:00", "closes": "21:00"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5.0",
                            "reviewCount": str(B["reviews"]), "bestRating": "5"},
        "review": [{"@type": "Review",
                    "author": {"@type": "Person", "name": n},
                    "reviewRating": {"@type": "Rating", "ratingValue": "5"},
                    "reviewBody": t} for n, _, t in REVIEWS[:3]],
    }
    blocks = ('<script type="application/ld+json">'
              + json.dumps(ld, ensure_ascii=False, separators=(",", ":")) + "</script>")
    if extra_ld:
        blocks += ('<script type="application/ld+json">'
                   + json.dumps(extra_ld, ensure_ascii=False, separators=(",", ":")) + "</script>")
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#161E27">
<meta property="og:type" content="website">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="{B['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{B['domain']}/images/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{blocks}
</head>
<body>"""


def header(active=""):
    nav = "".join('<a href="%s"%s>%s</a>' % (u, ' class="on"' if k == active else "", t)
                  for k, u, t in NAV)
    mnav = "".join(f'<a href="{u}">{t}</a>' for k, u, t in NAV)
    return f"""
<div class="topbar"><div class="wrap">
  <span>{B['city']} · Timiș · Arad · Caraș-Severin · <b>Deplasare și deviz gratuit</b></span>
  <span class="tb-r"><span>Program 07:00 – 21:00, urgențe non-stop</span>
  <span><span class="tb-star">★★★★★</span> {B['reviews']} de recenzii pe Google</span></span>
</div></div>

<header class="hdr">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{B['name']} — pagina principală">{LOGO}
      <span class="brand-t"><b>{B['name']}</b><span>{B['tagline']}</span></span></a>
    <nav class="nav" aria-label="Navigare principală">{nav}</nav>
    <div class="hdr-cta">
      <a class="hdr-tel" href="{TEL}"><span>Sunați-ne</span><b>{B['tel_disp']}</b></a>
      <a class="btn btn-p btn-sm" href="/calculator-pret/">Cereți oferta</a>
      <button class="burger" aria-label="Deschideți meniul" aria-expanded="false"><i></i><i></i><i></i></button>
    </div>
  </div>
  <div class="mnav"><div class="wrap">{mnav}
    <div class="mnav-cta">
      <a class="btn btn-d" href="{TEL}">Sunați: {B['tel_disp']}</a>
      <a class="btn btn-p" href="/calculator-pret/">Cereți oferta</a>
    </div></div></div>
</header>"""


def form(idsuf, title, sub, compact=False, dark=False):
    lucrare = "" if compact else f"""
      <div class="field"><label for="lu{idsuf}">Ce lucrare vă interesează</label>
        <select id="lu{idsuf}" name="lucrare">
          <option value="">Alegeți din listă</option>
          {"".join(f'<option>{s["t"]}</option>' for s in SERVICES)}
          <option>Altă lucrare</option>
        </select></div>
      <div class="field"><label for="de{idsuf}">Detalii (opțional)</label>
        <textarea id="de{idsuf}" name="detalii" placeholder="Suprafață aproximativă, tip de învelitoare, ce problemă aveți."></textarea></div>"""
    return f"""<div class="cta-f">
  <h3>{title}</h3><p>{sub}</p>
  <form data-mail novalidate>
    <div class="field-2">
      <div class="field"><label for="nu{idsuf}">Nume *</label>
        <input id="nu{idsuf}" name="nume" type="text" autocomplete="name" required></div>
      <div class="field"><label for="te{idsuf}">Telefon *</label>
        <input id="te{idsuf}" name="telefon" type="tel" autocomplete="tel" required></div>
    </div>
    <div class="field"><label for="or{idsuf}">Localitate</label>
      <input id="or{idsuf}" name="oras" type="text" autocomplete="address-level2"></div>
    {lucrare}
    <p class="f-msg" role="status"></p>
    <button class="btn btn-p btn-w" type="submit">Trimiteți solicitarea</button>
    <p class="f-hint">Solicitarea ajunge pe e-mail la <b>{B['email']}</b>. Preferați direct? <a href="{TEL}" style="border-bottom:2px solid var(--signal)">Sunați</a> sau <a href="{WA_LINK}" target="_blank" rel="noopener" style="border-bottom:2px solid var(--signal)">scrieți pe WhatsApp</a>.</p>
  </form>
</div>"""


def footer():
    svc = "".join(f'<li><a href="/servicii/#{s["k"]}">{s["t"]}</a></li>' for s in SERVICES[:6])
    return f"""
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-g">
      <div class="ftr-brand">
        <a class="brand" href="/">{LOGO}<span class="brand-t"><b>{B['name']}</b><span>{B['tagline']}</span></span></a>
        <p>Echipă proprie de acoperișuri cu baza în {B['city']}. Executăm manopera, nu vindem materiale.</p>
        <a class="ftr-tel" href="{TEL}">{B['tel_disp']}</a>
      </div>
      <div><h4>Servicii</h4><ul>{svc}</ul></div>
      <div><h4>Firma</h4><ul>
        <li><a href="/despre/">Despre noi</a></li>
        <li><a href="/lucrari/">Lucrări executate</a></li>
        <li><a href="/recenzii/">Recenzii</a></li>
        <li><a href="/calculator-pret/">Calculator preț</a></li>
        <li><a href="/intrebari-frecvente/">Întrebări frecvente</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="{TEL}">{B['tel_disp']}</a></li>
        <li><a href="{WA_LINK}" target="_blank" rel="noopener">Scrieți pe WhatsApp</a></li>
        <li><a href="mailto:{B['email']}">{B['email']}</a></li>
        <li><a href="{B['maps']}" target="_blank" rel="noopener">{B['street']}<br>{B['city']} {B['zip']}</a></li>
        <li>Luni – duminică, 07:00 – 21:00</li>
        <li><a href="https://anpc.ro/" target="_blank" rel="noopener nofollow">ANPC</a> · <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener nofollow">SOL</a></li>
      </ul></div>
    </div>
    <div class="ftr-bot">
      <span>© <span data-year></span> {B['legal']}. Toate drepturile rezervate.</span>
      <span><span style="color:var(--signal)">★★★★★</span> {B['reviews']} de recenzii pe Google</span>
    </div>
  </div>
</footer>

<div class="mbar">
  <a class="m-call" href="{TEL}">Sunați acum</a>
  <a class="m-wa" href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp</a>
</div>
<a class="wa-f" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Scrieți-ne pe WhatsApp">
<svg viewBox="0 0 448 512" aria-hidden="true"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg></a>

<script src="/assets/script.js" defer></script>
</body>
</html>"""


def phero(crumb, h1, lead):
    return f"""<section class="phero"><div class="wrap">
  <div class="crumb"><a href="/">Acasă</a> / {crumb}</div>
  <h1>{h1}</h1><p>{lead}</p>
</div></section>"""


def stars(n=5):
    return f'<span class="stars" aria-label="{n} din 5 stele">{"★" * n}</span>'


def rev_card(name, city, text):
    return f"""<article class="rev-c">{stars()}
  <p>{text}</p>
  <div class="rev-who"><span class="rev-av" aria-hidden="true">{name[0]}</span>
    <span><b>{name}</b><span>{city}</span></span></div></article>"""


def faq_block(items):
    out = []
    for i, (q, aa) in enumerate(items):
        ans = "".join(f"<p>{p}</p>" for p in aa)
        cls = " on" if i == 0 else ""
        exp = "true" if i == 0 else "false"
        out.append(f'<div class="faq-i{cls}"><button class="faq-q" type="button" aria-expanded="{exp}">{q}</button>'
                   f'<div class="faq-a">{ans}</div></div>')
    return f'<div class="faq">{"".join(out)}</div>'


FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage",
          "mainEntity": [{"@type": "Question", "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": " ".join(a)}}
                         for q, a in FAQ]}


def cta_section():
    return f"""<section class="sec sec-paper"><div class="wrap"><div class="cta">
  <div>
    <span class="eyebrow">Următorul pas</span>
    <h2>Cereți oferta pentru acoperișul dumneavoastră</h2>
    <p style="font-size:1.05rem;margin-top:16px">Vă sunăm, venim și măsurăm gratuit, apoi primiți un deviz pe etape, cu preț final și garanție scrisă la manoperă. Fără obligații.</p>
    <div class="hero-act" style="margin-top:26px">
      <a class="btn btn-d" href="{TEL}">Sunați: {B['tel_disp']}</a>
      <a class="btn btn-o" href="{WA_LINK}" target="_blank" rel="noopener">Scrieți pe WhatsApp</a>
    </div>
  </div>
  {form("c", "Solicitare rapidă", "Lăsați numele și telefonul. Vă contactăm noi.", compact=True)}
</div></div></section>"""


# ------------------------------------------------------------------ pagini
def page_home():
    svc_cards = "".join(f"""<article class="svc-c rv">
      <div class="svc-ph"><img src="/images/{s['img']}" alt="{s['t']} — lucrare executată de echipa {B['name']}" loading="lazy" width="640" height="400">
        <span class="svc-tag">{s['tag']}</span></div>
      <div class="svc-b"><h3>{s['t']}</h3><p>{s['s']}</p>
        <a class="svc-more" href="/servicii/#{s['k']}">Detalii</a></div></article>""" for s in SERVICES[:6])

    work_cards = "".join(f"""<a class="work-c rv" href="/lucrari/">
      <img src="/images/{im}" alt="{t} — {loc}" loading="lazy" width="600" height="450">
      <div class="work-o"><span>{tag}</span><h3>{t}</h3></div></a>""" for im, tag, t, loc in WORKS[:6])

    steps = [
        ("Ne contactați", "Ne spuneți ce aveți de făcut. Dacă nu sunteți sigur, vă lămurim la telefon în câteva minute."),
        ("Venim și măsurăm", "Ne deplasăm la fața locului, luăm măsurătorile reale și verificăm starea șarpantei."),
        ("Primiți devizul", "Pe etape, cu necesarul de materiale și manopera separat, la preț final."),
        ("Executăm lucrarea", "Începem la data stabilită, lucrăm curat și lăsăm locul strâns la final."),
    ]
    proc = "".join(f"""<div class="proc-i"><span class="proc-n">Pasul {i+1:02d}</span>
      <h3>{t}</h3><p>{d}</p></div>""" for i, (t, d) in enumerate(steps))

    why = [
        ("Fără intermediar", "Echipă proprie", "Lucrarea o execută oamenii noștri, de la șarpantă până la tinichigerie. Un singur responsabil pentru tot."),
        ("Fără adaos ascuns", "Nu vindem materiale", "Vă calculăm necesarul exact și cumpărați direct de la furnizor, la prețul lui. Noi facem manopera."),
        ("Fără surprize", "Deviz pe etape", "Vedeți separat structura, folia, învelitoarea și tinichigeria, nu o singură cifră pentru tot."),
        ("Fără cost", "Deplasare și măsurătoare", "Venim, măsurăm și vă dăm un preț real înainte să începem ceva."),
        ("Scrisă", "Garanție la manoperă", "Dacă apare o problemă la lucrarea noastră, ne întoarcem și o remediem."),
        (f"{B['years']} ani", "Experiență verificabilă", f"Peste {B['projects']} de acoperișuri și mansarde executate și {B['reviews']} de recenzii pe Google."),
    ]
    why_html = "".join(f'<div class="why-i"><span class="why-k">{k}</span><h3>{t}</h3><p>{d}</p></div>'
                       for k, t, d in why)

    revs = "".join(rev_card(*r) for r in REVIEWS[:3])
    chips = "".join(f"<span>{c}</span>" for c in CITIES)

    return head(
        f"Acoperișuri {B['city']} — înlocuire, montaj și reparații | {B['name']}",
        f"Echipă proprie cu {B['years']} ani de experiență în {B['city']} și vestul țării. Deplasare și deviz gratuit, preț final, garanție la manoperă. {B['rating']} ★ din {B['reviews']} de recenzii Google.",
        "/", extra_ld=FAQ_LD) + header("") + f"""

<section class="hero"><div class="wrap"><div class="hero-g">
  <div>
    <span class="eyebrow">{B['city']} · Timiș · Arad · Caraș-Severin</span>
    <h1>Înlocuim, renovăm și reparăm acoperișuri, la cheie</h1>
    <p class="hero-lead">Echipă proprie, cu {B['years']} ani de experiență și peste {B['projects']} de acoperișuri executate. Ne deplasăm și măsurăm gratuit, apoi primiți un deviz pe etape, cu preț final și garanție scrisă la manoperă.</p>
    <div class="hero-act">
      <a class="btn btn-p" href="/calculator-pret/">Calculați prețul</a>
      <a class="btn btn-o" href="{TEL}">Sunați acum</a>
    </div>
    <p class="hero-tel">Preferați telefonic? <a href="{TEL}">{B['tel_disp']}</a></p>
  </div>
  <div class="hero-ph">
    <img src="/images/hero-1.jpg" alt="Acoperiș din țiglă metalică montat de echipa {B['name']}" width="900" height="600" fetchpriority="high">
    <div class="hero-badge">
      <span class="hb-t">{stars()}<b>{B['reviews']} de recenzii pe Google</b></span>
    </div>
  </div>
</div></div>

<div class="spec"><div class="wrap"><div class="spec-g">
  <div class="spec-i"><div class="spec-n">{B['years']}<em> ani</em></div><div class="spec-l">De experiență</div></div>
  <div class="spec-i"><div class="spec-n">{B['projects']}<em>+</em></div><div class="spec-l">Acoperișuri executate</div></div>
  <div class="spec-i"><div class="spec-n">{B['reviews']}</div><div class="spec-l">Recenzii pe Google</div></div>
  <div class="spec-i"><div class="spec-n">0<em> lei</em></div><div class="spec-l">Deplasare și deviz</div></div>
</div></div></div>
</section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">Servicii</span>
    <h2>Tot ce ține de acoperișul dumneavoastră</h2>
    <p>De la o reparație punctuală până la un acoperiș refăcut de la structură. Aceeași echipă pentru toate etapele, deci un singur responsabil pentru rezultat.</p></div>
  <div class="svc">{svc_cards}</div>
  <div style="margin-top:32px"><a class="btn btn-o" href="/servicii/">Vedeți toate cele {len(SERVICES)} servicii</a></div>
</div></section>

<section class="sec sec-dark sec-pitch"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow eyebrow-l">Cum lucrăm</span>
    <h2>De la o întrebare la un acoperiș gata</h2>
    <p>Patru pași, fără niciun cost până în momentul în care acceptați oferta.</p></div>
  <div class="proc rv">{proc}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">De ce noi</span>
    <h2>Șase lucruri pe care le puteți verifica</h2>
    <p>Un acoperiș se vede greu după ce e montat, iar problemele apar abia la a doua sau a treia iarnă. Astea sunt lucrurile pe care merită să le întrebați orice firmă, inclusiv pe noi.</p></div>
  <div class="why rv">{why_html}</div>
</div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">Lucrări</span>
    <h2>Acoperișuri executate de echipa noastră</h2>
    <p>Câteva dintre casele la care am lucrat în ultimii ani, în {B['city']} și în împrejurimi.</p></div>
  <div class="work">{work_cards}</div>
  <div style="margin-top:32px"><a class="btn btn-o" href="/lucrari/">Vedeți toate lucrările</a></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h sec-h-c rv"><span class="eyebrow">Recenzii</span>
    <h2>Ce spun clienții noștri</h2></div>
  <div class="rev-line rv">{stars()}<b>{B['reviews']} de recenzii pe Google</b></div>
  <div class="rev-g">{revs}</div>
  <div style="margin-top:32px;text-align:center"><a class="btn btn-o" href="/recenzii/">Citiți toate recenziile</a></div>
</div></section>

<section class="sec sec-dark"><div class="wrap"><div class="zone">
  <div>
    <span class="eyebrow eyebrow-l">Zona de lucru</span>
    <h2>Ne găsiți în {B['city']}, dar venim la dumneavoastră</h2>
    <p>Lucrăm curent în Timiș, Arad, Caraș-Severin, Hunedoara și Cluj. Pentru lucrări mai mari ne deplasăm în toată țara. Spuneți-ne unde este casa și organizăm o vizită pentru evaluare și măsurători gratuite.</p>
    <div class="zone-chips">{chips}</div>
    <a class="btn btn-p" href="{TEL}">Sunați: {B['tel_disp']}</a>
  </div>
  <div class="zone-facts">
    <div class="zone-f"><span>Adresă</span><b>{B['street']}<br>{B['city']} {B['zip']}</b></div>
    <div class="zone-f"><span>Telefon</span><b>{B['tel_disp']}</b></div>
    <div class="zone-f"><span>Program</span><b>Luni – duminică<br>07:00 – 21:00</b></div>
    <div class="zone-f"><span>Urgențe</span><b>Non-stop, pentru infiltrații active</b></div>
  </div>
</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h sec-h-c rv"><span class="eyebrow">Întrebări frecvente</span>
    <h2>Ce ne întreabă oamenii cel mai des</h2></div>
  {faq_block(FAQ[:5])}
  <div style="margin-top:32px;text-align:center"><a class="btn btn-o" href="/intrebari-frecvente/">Toate întrebările</a></div>
</div></section>

{cta_section()}
""" + footer()


def page_servicii():
    cards = "".join(f"""<article class="svc-c rv" id="{s['k']}">
      <div class="svc-ph"><img src="/images/{s['img']}" alt="{s['t']} — {B['name']}" loading="lazy" width="640" height="400">
        <span class="svc-tag">{s['tag']}</span></div>
      <div class="svc-b"><h3>{s['t']}</h3><p>{s['d']}</p></div></article>""" for s in SERVICES)
    extra = ["Ferestre de mansardă și luminatoare", "Parazăpezi și accesorii de siguranță",
             "Foișoare, terase și pergole din lemn", "Tratamente ignifuge și antifungice pentru lemn",
             "Curățare și revizie anuală de acoperiș", "Șorțuri, dolii și racorduri la coșuri de fum"]
    return head(f"Servicii acoperișuri {B['city']} — montaj, reparații, mansardări | {B['name']}",
                f"Înlocuire și montaj acoperiș, reparații și infiltrații, dulgherie, mansardări, hidroizolații, jgheaburi. Echipă proprie în {B['city']} și vestul țării.",
                "/servicii/", "svc-metalica.jpg") + header("servicii") + f"""
{phero("Servicii", "Servicii de acoperișuri", f"Executăm manoperă și montaj, de la o reparație punctuală până la un acoperiș refăcut de la structură. Toate lucrările sunt executate de echipa noastră, cu garanție scrisă la manoperă.")}

<section class="sec"><div class="wrap">
  <div class="svc">{cards}</div>
</div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">Și în plus</span>
    <h2>Lucrări conexe pe care le executăm</h2>
    <p>Le facem în cadrul unei lucrări mai mari sau separat, dacă asta aveți nevoie.</p></div>
  <ul class="slist">{"".join(f"<li>{x}</li>" for x in extra)}</ul>
</div></section>

{cta_section()}
""" + footer()


def page_lucrari():
    cards = "".join(f"""<a class="work-c rv" href="{WA_LINK}" target="_blank" rel="noopener">
      <img src="/images/{im}" alt="{t} — {loc}" loading="lazy" width="600" height="450">
      <div class="work-o"><span>{tag} · {loc}</span><h3>{t}</h3></div></a>""" for im, tag, t, loc in WORKS)
    return head(f"Lucrări executate — acoperișuri în {B['city']} și Timiș | {B['name']}",
                f"Acoperișuri, șarpante și mansardări executate de echipa noastră în {B['city']}, Arad, Lugoj și împrejurimi. Peste {B['projects']} de lucrări în {B['years']} ani.",
                "/lucrari/", "pf-01.jpg") + header("lucrari") + f"""
{phero("Lucrări", "Lucrări executate", f"Peste {B['projects']} de acoperișuri și mansarde în {B['years']} ani. Mai jos sunt câteva dintre ele, cu tipul lucrării și zona în care s-a executat.")}

<section class="sec"><div class="wrap">
  <div class="work">{cards}</div>
  <div style="margin-top:44px;text-align:center">
    <p style="margin-bottom:20px">Vreți să vedeți o lucrare asemănătoare cu ce aveți dumneavoastră de făcut? Spuneți-ne ce casă aveți și vă trimitem poze de la o lucrare similară.</p>
    <a class="btn btn-p" href="{WA_LINK}" target="_blank" rel="noopener">Cereți poze pe WhatsApp</a>
  </div>
</div></section>

{cta_section()}
""" + footer()


def page_recenzii():
    revs = "".join(rev_card(*r) for r in REVIEWS)
    return head(f"Recenzii — {B['rating']} ★ din {B['reviews']} de recenzii Google | {B['name']}",
                f"Media de {B['rating']} stele din {B['reviews']} de recenzii pe Google. Ce spun clienții din {B['city']}, Arad, Lugoj, Reșița și Caransebeș despre lucrările noastre.",
                "/recenzii/", "rec-1.jpg") + header("recenzii") + f"""
{phero("Recenzii", "Ce spun clienții noștri", f"Avem {B['rating']} stele din {B['reviews']} de recenzii pe Google, strânse în ultimii ani de la oameni cărora le-am făcut acoperișul. Le puteți citi pe toate direct pe profilul nostru.")}

<section class="sec"><div class="wrap">
  <div class="rev-line rv">{stars()}<b>{B['reviews']} de recenzii pe Google</b></div>
  <div class="rev-g">{revs}</div>
  <div style="margin-top:32px;text-align:center"><a class="btn btn-o" href="{B['maps']}" target="_blank" rel="noopener">Vedeți-le pe Google</a></div>
</div></section>

<section class="sec sec-dark"><div class="wrap">
  <div class="sec-h sec-h-c rv"><span class="eyebrow eyebrow-l">Ați lucrat cu noi?</span>
    <h2>O recenzie ne ajută mai mult decât orice reclamă</h2>
    <p>Dacă v-am făcut acoperișul și sunteți mulțumit, lăsați-ne câteva rânduri pe Google. Durează un minut și ajută pe altcineva să aleagă în cunoștință de cauză.</p>
    <div style="margin-top:26px"><a class="btn btn-p" href="{B['maps']}" target="_blank" rel="noopener">Lăsați o recenzie</a></div>
  </div>
</div></section>

{cta_section()}
""" + footer()


def page_calculator():
    return head(f"Calculator preț acoperiș — estimare în 1 minut | {B['name']}",
                "Calculați suprafața reală a acoperișului și un interval orientativ de preț pentru manoperă și materiale. Prețul exact vine după măsurătoarea gratuită la fața locului.",
                "/calculator-pret/", "svc-ceramica.jpg") + header("calculator-pret") + f"""
{phero("Calculator preț", "Cât costă acoperișul dumneavoastră", "Estimați în mai puțin de un minut suprafața reală a acoperișului și intervalul de preț. Este o orientare, nu o ofertă: prețul final îl stabilim după ce venim și măsurăm.")}

<section class="sec"><div class="wrap"><div class="calc" id="calc">
  <div class="calc-f">
    <div class="field">
      <div class="range-row"><label for="c-amprenta" style="margin:0">Amprenta casei la sol</label>
        <b id="c-amprenta-v">120 mp</b></div>
      <input id="c-amprenta" type="range" min="40" max="400" step="5" value="120">
      <p class="f-hint">Lungimea înmulțită cu lățimea casei, la nivelul solului. Nu suprafața acoperișului.</p>
    </div>

    <div class="field"><label>Panta acoperișului</label>
      <div class="seg" data-key="panta">
        <button type="button" data-v="mica">Mică</button>
        <button type="button" data-v="medie" class="on">Medie</button>
        <button type="button" data-v="mare">Mare</button>
      </div>
      <p class="f-hint">Mică: acoperiș aproape plat. Medie: casă obișnuită. Mare: pod înalt sau mansardă.</p>
    </div>

    <div class="field"><label>Învelitoarea dorită</label>
      <div class="seg" data-key="material">
        <button type="button" data-v="metalica" class="on">Țiglă metalică</button>
        <button type="button" data-v="ceramica">Țiglă ceramică</button>
        <button type="button" data-v="bituminoasa">Șindrilă</button>
      </div>
    </div>

    <div class="field"><label>Tipul lucrării</label>
      <div class="seg" data-key="tip">
        <button type="button" data-v="inlocuire" class="on">Înlocuire</button>
        <button type="button" data-v="nou">Acoperiș nou</button>
        <button type="button" data-v="renovare">Renovare</button>
      </div>
    </div>
  </div>

  <div class="calc-out">
    <h3>Estimare orientativă</h3>
    <p class="calc-note">Pentru datele introduse, un acoperiș de acest tip se încadrează în general în:</p>
    <div class="calc-res" id="c-tot">—</div>
    <div class="calc-brk">
      <div><span>Suprafață acoperiș</span><b id="c-mp">—</b></div>
      <div><span>Manoperă</span><b id="c-man">—</b></div>
      <div><span>Materiale</span><b id="c-mat">—</b></div>
    </div>
    <p class="calc-note">Materialele le cumpărați direct de la furnizor, la prețul lui. Noi facturăm doar manopera. Intervalul de mai sus include TVA și nu acoperă situații speciale: șarpantă putredă, lucarne multiple, acces dificil.</p>
    <form class="calc-form" data-mail data-calc novalidate>
      <div class="field-2">
        <div class="field"><label for="c-nume">Nume *</label>
          <input id="c-nume" name="nume" type="text" autocomplete="name" required></div>
        <div class="field"><label for="c-tel">Telefon *</label>
          <input id="c-tel" name="telefon" type="tel" autocomplete="tel" required></div>
      </div>
      <div class="field"><label for="c-oras">Localitate</label>
        <input id="c-oras" name="oras" type="text" autocomplete="address-level2"></div>
      <p class="f-msg" role="status"></p>
      <button class="btn btn-p btn-w" type="submit">Trimiteți estimarea și cereți prețul exact</button>
    </form>
    <p class="calc-note" style="margin-top:14px">Estimarea de mai sus pleacă pe e-mail la <b style="color:#fff">{B['email']}</b> împreună cu datele dumneavoastră. Preferați altfel? <a href="{TEL}" style="color:#fff;border-bottom:2px solid var(--signal)">{B['tel_disp']}</a> sau <a id="c-wa" href="{WA_LINK}" target="_blank" rel="noopener" style="color:#fff;border-bottom:2px solid var(--signal)">WhatsApp</a>.</p>
  </div>
</div></div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">De citit</span>
    <h2>De ce suprafața acoperișului nu e suprafața casei</h2></div>
  <div class="arg rv">
    <div class="arg-i"><h3>Panta adaugă între 18 și 50 la sută</h3>
      <p>Un acoperiș este o suprafață înclinată, deci mai mare decât amprenta pe care o acoperă. La o casă obișnuită diferența este de aproximativ o treime. La un pod înalt poate ajunge la jumătate. De aceea o estimare dată la telefon, pe suprafața casei, iese aproape întotdeauna prea mică.</p></div>
    <div class="arg-i"><h3>Streșinile nu sunt incluse în amprentă</h3>
      <p>Acoperișul depășește pereții cu 40 – 80 cm de jur împrejur. La o casă de 10 pe 12 metri, streașina singură adaugă câțiva metri pătrați buni de învelitoare, de folie, de șipcă și de manoperă.</p></div>
    <div class="arg-i"><h3>Forma contează mai mult decât mărimea</h3>
      <p>Două acoperișuri de aceeași suprafață pot diferi semnificativ ca preț. Doliile, lucarnele, coșurile și racordurile cer timp, tinichigerie și tăieturi, iar acolo se duce manopera, nu pe suprafețele drepte.</p></div>
    <div class="arg-i"><h3>De aceea venim și măsurăm</h3>
      <p>Măsurătoarea la fața locului durează sub o oră și este gratuită, indiferent dacă lucrați cu noi sau nu. După ea primiți un deviz pe etape, cu preț final, pe care îl puteți compara cu orice altă ofertă.</p></div>
  </div>
</div></section>

{cta_section()}
""" + footer()


def page_faq():
    return head(f"Întrebări frecvente despre acoperișuri | {B['name']}",
                "Prețuri, garanție, materiale, durata lucrărilor, zone de lucru. Răspunsuri clare la întrebările pe care ni le pun cel mai des clienții.",
                "/intrebari-frecvente/", "svc-dulgherie.jpg", extra_ld=FAQ_LD) + header("intrebari-frecvente") + f"""
{phero("Întrebări frecvente", "Întrebări frecvente", "Dacă nu găsiți răspunsul aici, sunați-ne. Vă spunem cum stau lucrurile chiar dacă răspunsul nu este cel pe care sperați să îl auziți.")}

<section class="sec"><div class="wrap">{faq_block(FAQ)}</div></section>

{cta_section()}
""" + footer()


def page_contact():
    return head(f"Contact — {B['name']} {B['city']} | {B['tel_disp']}",
                f"Sunați la {B['tel_disp']} sau scrieți pe WhatsApp. {B['street']}, {B['city']}. Deplasare și deviz gratuit în Timiș, Arad și Caraș-Severin.",
                "/contact/", "hero-2.jpg") + header("contact") + f"""
{phero("Contact", "Hai să vorbim despre acoperișul dumneavoastră", "Cel mai rapid este la telefon sau pe WhatsApp. Ne spuneți ce aveți de făcut, stabilim o vizită și veniți cu măsurătoarea la preț final.")}

<section class="sec"><div class="wrap">
  <div class="cont">
    <div class="cont-c"><span class="why-k">Telefon</span>
      <b><a href="{TEL}">{B['tel_disp']}</a></b>
      <p>Luni – duminică, 07:00 – 21:00. Pentru infiltrații active răspundem și în afara programului.</p></div>
    <div class="cont-c"><span class="why-k">WhatsApp</span>
      <b><a href="{WA_LINK}" target="_blank" rel="noopener">Trimiteți un mesaj</a></b>
      <p>Trimiteți-ne poze cu acoperișul și vă spunem din prima ce credem că are.</p></div>
    <div class="cont-c"><span class="why-k">E-mail</span>
      <b><a href="mailto:{B['email']}">{B['email']}</a></b>
      <p>Pentru oferte, devize și documente. Răspundem în aceeași zi lucrătoare.</p></div>
    <div class="cont-c"><span class="why-k">Adresă</span>
      <b><a href="{B['maps']}" target="_blank" rel="noopener">{B['street']}</a></b>
      <p>{B['city']} {B['zip']}, jud. {B['region']}. Lucrările le executăm la dumneavoastră, nu la sediu.</p></div>
  </div>

  <div class="cta">
    <div>
      <span class="eyebrow">Zona de lucru</span>
      <h2>Unde ne deplasăm</h2>
      <p style="margin-top:16px">Lucrăm curent în {", ".join(CITIES[:-1])} și {CITIES[-1]}, plus localitățile din jur. Pentru lucrări mai mari ne deplasăm în toată țara.</p>
      <p style="margin-top:14px">Deplasarea pentru evaluare și măsurători este gratuită și nu vă obligă la nimic.</p>
      <div class="hero-act" style="margin-top:26px">
        <a class="btn btn-d" href="{TEL}">Sunați acum</a>
        <a class="btn btn-o" href="{B['maps']}" target="_blank" rel="noopener">Deschideți în Google Maps</a>
      </div>
    </div>
    {form("k", "Scrieți-ne", "Completați și vă contactăm în cel mai scurt timp.")}
  </div>
</div></section>
""" + footer()


def page_despre():
    return head(f"Despre noi — echipă de acoperișuri în {B['city']} | {B['name']}",
                f"{B['years']} ani, peste {B['projects']} de acoperișuri și {B['reviews']} de recenzii pe Google. Echipă proprie, fără subcontractare, cu baza în {B['city']}.",
                "/despre/", "hero-3.jpg") + header("despre") + f"""
{phero("Despre noi", "O echipă, nu un intermediar", f"Suntem o echipă de acoperișuri cu baza în {B['city']}. Lucrăm de {B['years']} ani, avem peste {B['projects']} de lucrări în spate și {B['reviews']} de recenzii pe Google.")}

<section class="sec"><div class="wrap"><div class="about rv">
  <div>
    <span class="eyebrow">Cine suntem</span>
    <h2>Am început în {B['founded']}, cu o echipă și o dubă</h2>
    <p>Am pornit ca doi meseriași care făceau șarpante și învelitori în jurul {B['city']}. În {B['years']} ani am ajuns la o echipă stabilă care execută acoperișuri complete, de la structura de lemn până la ultimul jgheab, fără să dăm nimic mai departe la alții.</p>
    <p>Nu ne-am propus să fim cea mai mare firmă din zonă. Facem între cincisprezece și douăzeci de acoperișuri pe an, ca să apucăm să fim pe fiecare șantier și să răspundem când sună cineva la doi ani după lucrare.</p>
    <p>Nu vindem materiale. Vă calculăm necesarul exact, vă recomandăm furnizori și cumpărați direct de la ei. Noi facturăm manopera, iar dumneavoastră vedeți clar unde se duce fiecare leu.</p>
  </div>
  <img src="/images/hero-3.jpg" alt="Echipa {B['name']} la lucru pe un acoperiș" loading="lazy" width="800" height="600">
</div></div></section>

<section class="sec sec-paper"><div class="wrap">
  <div class="spec-g" style="background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden">
    <div class="spec-i"><div class="spec-n">{B['founded']}</div><div class="spec-l">Anul înființării</div></div>
    <div class="spec-i"><div class="spec-n">{B['projects']}<em>+</em></div><div class="spec-l">Acoperișuri executate</div></div>
    <div class="spec-i"><div class="spec-n">{B['reviews']}</div><div class="spec-l">Recenzii pe Google</div></div>
    <div class="spec-i"><div class="spec-n">5<em> jud.</em></div><div class="spec-l">În care lucrăm curent</div></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-h rv"><span class="eyebrow">Cum lucrăm</span>
    <h2>Cinci lucruri la care nu facem rabat</h2>
    <p>Nu sunt slogane. Sunt regulile după care am ajuns să avem {B['reviews']} de recenzii fără nicio reclamație.</p></div>
  <div class="arg rv">
    <div class="arg-i"><h3>Prețul din deviz e prețul final</h3>
      <p>Dacă apare ceva neprevăzut sub învelitoare, oprim, vă sunăm, vă arătăm și abia apoi continuăm. Nu vă anunțăm la jumătatea lucrării că mai sunt de plătit lucruri despre care nu s-a discutat.</p></div>
    <div class="arg-i"><h3>Nu punem folie sub țiglă doar ca să fie</h3>
      <p>Folia anticondens funcționează doar cu contrașipci care lasă aerul să circule pe sub învelitoare. Fără ele condensează și udă izolația. Este exact genul de etapă pe care o ofertă ieftină o sare, pentru că nu se vede.</p></div>
    <div class="arg-i"><h3>Lucrăm cu ancoraj</h3>
      <p>Oamenii noștri lucrează legați, cu ham și linie de viață. Costă timp la montaj, dar nu vrem să explicăm nimănui de ce a căzut cineva de pe casa lui.</p></div>
    <div class="arg-i"><h3>Strângem după noi</h3>
      <p>Molozul, țigla veche și cuiele pleacă de la dumneavoastră odată cu noi. Curtea rămâne cum a fost, nu ca după un șantier.</p></div>
    <div class="arg-i"><h3>Răspundem și după lucrare</h3>
      <p>Garanția la manoperă e scrisă, nu spusă la telefon. Dacă apare o problemă la ce am făcut noi, ne întoarcem și o rezolvăm.</p></div>
    <div class="arg-i"><h3>Spunem și când nu merită</h3>
      <p>Uneori un acoperiș nu are nevoie de înlocuire, ci de o reparație de câteva sute de lei. Vă spunem asta, chiar dacă înseamnă o lucrare mai mică pentru noi.</p></div>
  </div>
</div></section>

{cta_section()}
""" + footer()


def page_404():
    return head("Pagina nu a fost găsită | " + B["name"],
                "Pagina căutată nu există. Reveniți la pagina principală sau sunați-ne.",
                "/404.html").replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                                     '<meta name="robots" content="noindex, follow">') + header("") + f"""
<section class="e404"><div class="wrap">
  <div class="e404-big">404</div>
  <h1>Pagina asta nu există</h1>
  <p>Poate a fost mutată sau linkul e greșit. Puteți să vă întoarceți la pagina principală sau să ne sunați direct.</p>
  <div class="hero-act" style="justify-content:center">
    <a class="btn btn-p" href="/">Înapoi la pagina principală</a>
    <a class="btn btn-o" href="{TEL}">Sunați: {B['tel_disp']}</a>
  </div>
</div></section>
""" + footer()


def redirect(target):
    return f"""<!DOCTYPE html><html lang="ro"><head><meta charset="UTF-8">
<title>Redirecționare…</title><link rel="canonical" href="{B['domain']}{target}">
<meta name="robots" content="noindex, follow">
<meta http-equiv="refresh" content="0; url={target}">
<script>location.replace("{target}");</script></head>
<body><p>Redirecționare către <a href="{target}">{B['domain']}{target}</a>…</p></body></html>"""


# ------------------------------------------------------------------ scriere
PAGES = {
    "index.html":                     page_home(),
    "servicii/index.html":            page_servicii(),
    "lucrari/index.html":             page_lucrari(),
    "recenzii/index.html":            page_recenzii(),
    "calculator-pret/index.html":     page_calculator(),
    "intrebari-frecvente/index.html": page_faq(),
    "contact/index.html":             page_contact(),
    "despre/index.html":              page_despre(),
    "404.html":                       page_404(),
}

REDIRECTS = {
    "oferta": "/calculator-pret/", "calculator": "/calculator-pret/", "pret": "/calculator-pret/",
    "preturi": "/calculator-pret/", "proiecte": "/lucrari/", "portofoliu": "/lucrari/",
    "galerie": "/lucrari/", "despre-noi": "/despre/", "faq": "/intrebari-frecvente/",
    "intrebari": "/intrebari-frecvente/", "review": "/recenzii/", "reviews": "/recenzii/",
    "testimoniale": "/recenzii/", "acoperisuri": "/servicii/", "servicii-acoperisuri": "/servicii/",
}

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
<rect width="32" height="32" rx="7" fill="#161E27"/>
<path d="M4.5 17.5 L16 7 L27.5 17.5" stroke="#F0A500" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
<path d="M8.5 16.5 V25 H23.5 V16.5" stroke="#FFFFFF" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

MANIFEST = {
    "name": B["name"] + " — " + B["tagline"],
    "short_name": B["name"],
    "start_url": "/",
    "display": "standalone",
    "background_color": "#FFFFFF",
    "theme_color": "#161E27",
    "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
}

SITEMAP_URLS = [("/", "1.0"), ("/servicii/", "0.9"), ("/calculator-pret/", "0.9"),
                ("/lucrari/", "0.8"), ("/recenzii/", "0.8"), ("/despre/", "0.8"),
                ("/intrebari-frecvente/", "0.7"), ("/contact/", "0.8")]

README = f"""# {B['name']} — montaj-acoperis-top.ro

Site static generat cu `build.py`. GitHub Pages, fără build tools.

## Regenerare

```bash
python3 build.py
```

Toate paginile HTML sunt generate din `build.py`. **Nu editați fișierele HTML direct** —
modificările se pierd la următoarea rulare. Editați `build.py`, apoi rulați scriptul.

## Structură

| Pagină | URL |
|---|---|
| Acasă | `/` |
| Servicii | `/servicii/` |
| Lucrări | `/lucrari/` |
| Recenzii | `/recenzii/` |
| Calculator preț | `/calculator-pret/` |
| Întrebări frecvente | `/intrebari-frecvente/` |
| Despre noi | `/despre/` |
| Contact | `/contact/` |

Redirecturi 301-like (meta refresh + JS): {", ".join("`/" + k + "/`" for k in REDIRECTS)}

## Date firmă

Toate datele sunt în dicționarul `B` din `build.py`: telefon, adresă, număr de recenzii,
ani de experiență, număr de lucrări. Schimbați acolo, rulați scriptul, gata.

- Telefon: {B['tel_disp']}
- Adresă: {B['street']}, {B['city']} {B['zip']}
- Google: {B['rating']} ★ din {B['reviews']} de recenzii
- Experiență: {B['years']} ani, peste {B['projects']} de lucrări

## Formulare

Toate formularele (inclusiv calculatorul de preț) trimit pe e-mail la **{B['email']}**
prin FormSubmit, un serviciu gratuit care nu cere backend și merge pe GitHub Pages.

Adresa se schimbă din `B["email"]` în `build.py`. WhatsApp și telefonul rămân ca alternative,
nu mai sunt canalul principal.

**Important la prima rulare:** FormSubmit trimite un e-mail de confirmare la {B['email']}
prima dată când cineva completează un formular. Până când cineva dă click pe linkul din acel
e-mail, mesajele nu ajung. Completați un formular de test și confirmați o singură dată.

## Design

- Paletă: ardezie `#161E27`, zinc `#5C6874`, galben de șantier `#F0A500`
- Typography: Archivo (titluri), IBM Plex Sans (text), IBM Plex Mono (cifre, etichete)
- Motiv recurent: linia înclinată de 13° = panta acoperișului (eyebrow-uri, separatoare, hero)
"""


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    n = 0
    for rel, html in PAGES.items():
        write(rel, html); n += 1
    for slug, target in REDIRECTS.items():
        write(f"{slug}/index.html", redirect(target)); n += 1
    write("favicon.svg", FAVICON)
    write("site.webmanifest", json.dumps(MANIFEST, ensure_ascii=False, indent=2))
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {B['domain']}/sitemap.xml\n")
    urls = "\n".join(f'  <url><loc>{B["domain"]}{u}</loc><changefreq>monthly</changefreq>'
                     f'<priority>{p}</priority></url>' for u, p in SITEMAP_URLS)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
                         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                         + urls + "\n</urlset>\n")
    write("README.md", README)
    write(".nojekyll", "")
    print(f"OK — {n} pagini HTML + assets scrise în {ROOT}")


if __name__ == "__main__":
    main()
