# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 5 (englanti)

## Viikon 5 teema
**Loogiset rakenteet**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O13**: Sekvenssi: ohjelma etenee vaihe vaiheelta
- **O14**: Ehdot: if-then-else -ajattelu ja päätöspuut
- **O15**: Toisto: saman asian tekeminen monta kertaa

## Viikon keskeinen viesti
Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto. Kun osaat nimetä nämä arkisissa tehtävissä, sinulla on jokaisen ohjelman luuranko.

## Bloom-katto
Muistaminen + Ymmärtäminen + kevyt Soveltaminen (ilmaise ehdot ja silmukat luonnollisella kielellä).

## Ammatillinen kulma
Esimerkkejä, joihin Rasmuksen kannattaa nojata: salasanan vahvuussääntö (ehto), sähköpostin saapuneet-kansion läpikäynti (toisto), vaiheittainen käyttöönottotarkistuslista (sekvenssi).

## Arvioinnin kosketuskohta
Pohjustusviikko AT2:lle (prosessin kuvaus sekvenssin + ehdon + toiston kanssa). AT2 osuu viikon 5 loppuun / viikolle 6.

## Tulosteen kieli
**Englanti.** Börje (suomenkielinen viimeistely) ohitetaan tällä kierroksella.

## Tulosteen laajuus (tämä kierros)
- Sune tuottaa viikon 5 suunnitelman lukittuine hyväksyntäkriteereineen, Rasmus-briefin ja eteenpäin katsovat luonnokset.
- Rasmus rakentaa **vain viikon 5**.
- Linnea + Wilhelm auditoivat viikon 5.
- Alfred paketoi viikon 5 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää eikä PPTX-renderöintiä** tässä putkikierroksessa. Markdown-julkaisu on toimitettava.

## Viikon vakiomuotoinen lohkorakenne (lukittu)
```
student/week-05/
├── overview.md         # viikon teema + must-do minimum vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria, kattaa kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---' erottimina
teacher/week-05/
├── teacher-materials.md  # 3 × 90 min fasilitointi, oppituntikohtaisilla kalvovihjeillä
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajavetoinen tuntitehtävä
```

Lisäksi, vain kun luento-osio aidosti tarvitsee syvempää aineistoa, ylimääräinen `student/week-05/slides-l<n>-<aihe>.md` -tiedosto (4–8 kalvoa). Rasmus päättää luento-osiokohtaisesti.

## Kaikkia viikkoja koskevat tiukat säännöt
- **Englanti läpi koko paketin**, kaikki 7 tiedostoa.
- **"AI-resilient" -merkintä on sisäinen** — se ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuutta, ei merkintää.
- **"If you are doing this alone"** -aliotsikko (`### If you are doing this alone`) on pakollinen jokaisessa tehtävässä, joka olettaa parin / seuraajan / testaajan, ja siihen kuuluu konkreettinen vaihtoehto (24h tauko, oma video, eri laite, luokan chat).
- **"Must-do minimum"** on overview.md:n ja student-tasks.md:n PAKOLLISTEN tehtävien sanamuoto (ei "mandatory minimum").
- **Kalvovihjeet (slide cues)** vaaditaan jokaiseen 90 min oppituntisuunnitelmaan `teacher-materials.md`:ssä.
- **30–50 % itsenäisen työn** lohko vaaditaan jokaisessa 90 min oppituntisuunnitelmassa.
- **Ei kalvotiedostoja muuta kuin `slides.md` (+ valinnainen `slides-l<n>-*.md`).** Ei PowerPointia, ei jest/mocha/vitest/pytest -viittauksia missään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi jos tämän viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitaan relevantti AT).
- **Tiedostojen välinen johdonmukaisuus**: tehtävänumerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; `teacher-materials.md`:ssä mainitut tuntiaktiviteetit löytyvät `in-class-tasks.md`:stä.

## Kurssitason konteksti
Yllä oleva toimeksianto on **viikon 5** siivu 8-viikkoisesta kurssista. Koko kurssin toimeksianto ja lukittu 24 oppitunnin runko on:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssin toimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon runko)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyyliviitteenä)

## Kultainen näyte (suomi, tyyli/syvyys/laajuus-viite)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason laajuus on ~3× yksittäinen kultaisen näytteen oppitunti. Yllä mainittu viikon 1 julkaisu on myös viite päästä päähän rakennetulle englanninkieliselle viikolle.

