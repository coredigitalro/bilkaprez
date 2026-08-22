# BilkaRoofMontaj — montaj-acoperis-top.ro

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

Redirecturi 301-like (meta refresh + JS): `/oferta/`, `/calculator/`, `/pret/`, `/preturi/`, `/proiecte/`, `/portofoliu/`, `/galerie/`, `/despre-noi/`, `/faq/`, `/intrebari/`, `/review/`, `/reviews/`, `/testimoniale/`, `/acoperisuri/`, `/servicii-acoperisuri/`

## Date firmă

Toate datele sunt în dicționarul `B` din `build.py`: telefon, adresă, număr de recenzii,
ani de experiență, număr de lucrări. Schimbați acolo, rulați scriptul, gata.

- Telefon: 0758 680 276
- Adresă: Strada Martir Ion Miron 29, Timișoara 300254
- Google: 5,0 ★ din 48 de recenzii
- Experiență: 10 ani, peste 180 de lucrări

## Formulare

Toate formularele (inclusiv calculatorul de preț) trimit pe e-mail la **bilkaroofmasters@gmail.com**
prin FormSubmit, un serviciu gratuit care nu cere backend și merge pe GitHub Pages.

Adresa se schimbă din `B["email"]` în `build.py`. WhatsApp și telefonul rămân ca alternative,
nu mai sunt canalul principal.

**Important la prima rulare:** FormSubmit trimite un e-mail de confirmare la bilkaroofmasters@gmail.com
prima dată când cineva completează un formular. Până când cineva dă click pe linkul din acel
e-mail, mesajele nu ajung. Completați un formular de test și confirmați o singură dată.

## Design

- Paletă: ardezie `#161E27`, zinc `#5C6874`, galben de șantier `#F0A500`
- Typography: Archivo (titluri), IBM Plex Sans (text), IBM Plex Mono (cifre, etichete)
- Motiv recurent: linia înclinată de 13° = panta acoperișului (eyebrow-uri, separatoare, hero)
