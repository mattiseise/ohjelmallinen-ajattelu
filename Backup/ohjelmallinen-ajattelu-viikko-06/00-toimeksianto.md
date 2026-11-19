# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 6 (englanninkielinen)

## Viikon 6 teema
**Ajattelusta koodiin**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O16**: Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon
- **O17**: Syöte, käsittely, tuloste ja muuttujan idea
- **O18**: Pseudokoodin testaaminen: käsiajo ja virheiden etsiminen (AT2 palautetaan tämän oppitunnin tienoilla)

## Viikon ydinviesti
Pseudokoodi on silta arkikielen ja oikean koodin välillä. Se on tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida.

## Bloom-katto
Ymmärtäminen + Soveltaminen (kirjoita pseudokoodia, käsiaja jäljityskaavion avulla, korjaa pseudokoodissa oleva bugi).

## Ammatillinen kulma
Esimerkkejä, joihin Rasmuksen pitäisi nojata: pseudokoodi help-deskin vastauksen priorisointiin, salasanan vahvuuden tarkistamiseen, päivittäiseen varmuuskopiointirutiiniin.

## Arvioinnin kosketuspiste
AT2 palautetaan O18:n tienoilla. Tämän viikon tehtävät syöttävät suoraan AT2:een. Vielä ei koodia — vain pseudokoodia.

## Lisäsäännöt tälle viikolle

- Ehdottomasti ei JavaScriptiä eikä mitään oikeaa ohjelmointikieltä tällä viikolla. Vain pseudokoodia.
- Ei testauskehyksiä (jest, mocha, vitest, pytest). Testaaminen tarkoittaa täällä paperilla tehtävää käsiajoa jäljityskaavion avulla.

## Tuotoskieli
**Englanti.** Börje (suomenkielinen kielenhuolto) ohitetaan tällä ajolla.

## Tuotoksen laajuus (tällä ajolla)
- Sune tuottaa viikon 6 suunnitelman lukittuine hyväksymiskriteereineen, Rasmukselle suunnatun briefin ja eteenpäin katsovat tyngät.
- Rasmus rakentaa **vain viikon 6**.
- Linnea + Wilhelm auditoivat viikon 6.
- Alfred paketoi viikon 6 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** putkessa tällä kierroksella. Markdown-julkaisu on toimitettava tuotos.

## Kanoninen lohkorakenne per viikko (lukittu)
```
student/week-06/
├── overview.md         # viikon teema + must-do-minimi vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria, kattaa kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLINEN + 2–3 🟣 SYVENTÄVÄ -tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---'-erottimet
teacher/week-06/
├── teacher-materials.md  # 3 × 90 min fasilitointi, oppituntikohtaiset Slide cues -vihjeet
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajan vetämä tuntitehtävä
```

Lisäksi vain silloin, kun jokin luento-osio aidosti kaipaa syvällisempää materiaalia, lisätiedosto `student/week-06/slides-l<n>-<aihe>.md` (4–8 kalvoa). Rasmus päättää luento-osiokohtaisesti.

## Kovat säännöt kaikille viikoille
- **Englantia läpi koko viikon**, kaikki 7 tiedostoa.
- **"AI-resilient"-leima on sisäinen** — se ei saa esiintyä missään opiskelijalle näkyvässä tiedostossa. Linnea auditoi ominaisuuden, ei leimaa.
- **"If you are doing this alone"** -alaotsikko (`### If you are doing this alone`) vaaditaan jokaiseen tehtävään, joka olettaa parin / seuraajan / testaajan, ja siihen on liitettävä konkreettinen vaihtoehto (24 h tauko, video itsestä, eri laite, luokan chat).
- **"Must-do minimum"** on PAKOLLISTEN tehtävien sanamuoto overview.md:ssä ja student-tasks.md:ssä (ei "mandatory minimum").
- **Slide cues** vaaditaan jokaiselle 90 minuutin oppituntisuunnitelmalle `teacher-materials.md`:n sisällä.
- **30–50 % itsenäisen työn** lohko vaaditaan jokaiselle 90 min oppituntisuunnitelmalle.
- **Ei muita kalvotiedostoja kuin `slides.md` (+ valinnainen `slides-l<n>-*.md`).** Ei PowerPointia, ei jest/mocha/vitest/pytest-viittauksia missään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi kun viikon tehtävät syöttävät AT2:een tai AT3:een — silloin mainitaan vastaava AT).
- **Tiedostojen välinen yhdenmukaisuus**: tehtävien numerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; `teacher-materials.md`:ssä viitatut tuntiaktiviteetit ovat olemassa tiedostossa `in-class-tasks.md`.

## Kurssin tason konteksti
Yllä oleva toimeksianto on **viikon 6** siivu 8 viikon kurssista. Koko kurssin toimeksianto ja lukittu 24 oppitunnin tiekartta sijaitsevat:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssin toimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon tiekartta)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyylireferenssinä)

## Kultaiset näytteet (suomenkielinen, tyyli-/syvyys-/määräreferenssi)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason määrä on noin 3× yksittäinen kultaisen näytteen oppitunti. Viikon 1 julkaisu yllä olevassa polussa on myös referenssi päästä päähän rakennetulle englanninkieliselle viikolle.
