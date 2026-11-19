# Toimeksianto — Ohjelmallinen ajattelu -kurssi, Viikko 4 (englanninkielinen)

## Viikon 4 teema
**Ratkaisujen vertailu**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O10**: Sama ongelma, useita ratkaisuja
- **O11**: Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virhealttius
- **O12**: Oman ratkaisun parantaminen ja vertaispalaute

## Viikon ydinviesti
Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.

## Bloom-katto
Ymmärtäminen + kevyt Analysointi (vertaa kahta ratkaisua nimettyjen kriteerien kautta).

## Ammatillinen näkökulma
Esimerkkejä, joihin Rasmuksen kannattaa nojata: kaksi tapaa varmuuskopioida projektikansio; kaksi tapaa perehdyttää uusi käyttäjä; kaksi tapaa kirjoittaa help desk -makro.

## Arviointikosketuspiste
Kurssin puolivälin reflektioviikko. Rakentaa vertaispalaute- ja revisiointitottumuksia, joita käytetään uudelleen AT2:ssa ja AT3:ssa.

## Tuotoksen kieli
**Englanti.** Börje (suomenkielinen viimeistely) ohitetaan tällä ajolla.

## Tuotoksen laajuus (tällä ajolla)
- Sune tuottaa viikon 4 suunnitelman lukituilla hyväksymiskriteereillä, Rasmuksen briiffauksen ja eteenpäin katsovat aihiot.
- Rasmus rakentaa **vain viikon 4**.
- Linnea + Wilhelm auditoivat viikon 4.
- Alfred paketoi viikon 4 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** putkessa tällä kierroksella. Markdown-julkaisu on toimitettava.

## Kanoninen lohkorakenne viikkoa kohden (lukittu)
```
student/week-04/
├── overview.md         # viikon teema + must-do minimum vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria kaikista 3 oppitunnista (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---' erottimet
teacher/week-04/
├── teacher-materials.md  # 3 × 90 min fasilitointi, oppituntikohtaisilla kalvovinkeillä
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajavetoinen tuntiharjoitus
```

Lisäksi vain silloin, kun luentosegmentti aidosti tarvitsee syvempää materiaalia, lisätiedosto `student/week-04/slides-l<n>-<topic>.md` (4–8 kalvoa). Rasmus päättää luentosegmenttikohtaisesti.

## Tiukat säännöt kaikille viikoille
- **Englanti läpi kaiken**, kaikki 7 tiedostoa.
- **"AI-resilient" -leima on sisäinen** — ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuutta, ei leimaa.
- **"If you are doing this alone"** -aliotsikko (`### If you are doing this alone`) vaaditaan jokaisessa tehtävässä, joka olettaa parin / seuraajan / testaajan, ja siihen liittyy konkreettinen vaihtoehto (24 h väli, video itsestään, eri laite, luokan chat).
- **"Must-do minimum"** on PAKOLLISTEN tehtävien sanoitus overview.md:ssä ja student-tasks.md:ssä (ei "mandatory minimum").
- **Kalvovinkit** vaaditaan jokaiselle 90 minuutin oppituntisuunnitelmalle `teacher-materials.md`:n sisällä.
- **30–50 % itsenäisen työn** lohko vaaditaan jokaiseen 90 minuutin oppituntisuunnitelmaan.
- **Ei kalvotiedostoja `slides.md`:n (+ valinnaisen `slides-l<n>-*.md`) lisäksi.** Ei PowerPointia, ei jest/mocha/vitest/pytest-viittauksia missään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi kun viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitaan relevantti AT).
- **Tiedostojen välinen yhtenäisyys**: tehtävien numerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; `teacher-materials.md`:ssä viitatut tuntiaktiviteetit löytyvät `in-class-tasks.md`:stä.

## Kurssitason konteksti
Yllä oleva toimeksianto on viipale **viikolta 4** 8-viikkoisesta kurssista. Koko kurssin toimeksianto ja lukittu 24 oppitunnin roadmap löytyy:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssin toimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon roadmap)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssinsisäisenä tyylireferenssinä)

## Kultainen esimerkki (suomeksi, tyyli/syvyys/laajuus-referenssi)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason laajuus on ~3× yksittäisen kultaisen esimerkin oppituntiin. Viikon 1 julkaisu yllä olevassa polussa on myös referenssi päästä-päähän englanninkieliselle viikolle.
