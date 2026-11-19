# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 3 (englanti)

## Viikon 3 teema
**Prosessin kuvaaminen**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O7**: Prosessin kuvaaminen: lista, vaiheittainen rakenne ja yksinkertainen vuokaavio
- **O8**: Abstraktio
- **O9**: Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia

## Viikon keskeinen viesti
Kun osaat pilkkoa ongelman, seuraava taito on *kuvata* prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa.

## Bloom-katto
Muistaminen + Ymmärtäminen hallitsevia; Soveltaminen sallittu (opiskelijat piirtävät yksinkertaisia vuokaavioita ja tunnistavat uudelleenkäytettäviä lohkoja).

## Ammatillinen näkökulma
Esimerkit, joita Rasmus käyttää: help desk -triage-vuo, tiedostonimeämiskäytäntö, "rekisteröi uusi laite" -menettely, joka toistuu jokaisen uuden läppärin kohdalla.

## Arvioinnin kosketuspiste
Tällä viikolla ei AT-palautusta. Viikko 3 rakentaa sanastoa AT2:ta (prosessikuvaus) varten viikoilla 5–6.

## Tuotoskieli
**Englanti.** Börje (suomen kielenhuolto) ohitetaan tällä ajolla.

## Tuotoksen laajuus (tämä ajo)
- Sune tuottaa viikon 3 suunnitelman lukittujen hyväksymiskriteerien, Rasmus-briefin ja eteenpäin katsovien luonnosten kanssa.
- Rasmus rakentaa **vain viikon 3**.
- Linnea + Wilhelm auditoivat viikon 3.
- Alfred paketoi viikon 3 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** putkessa tällä kierroksella. Markdown-julkaisu on toimitettava.

## Kanoninen lohkorakenne per viikko (lukittu)
```
student/week-03/
├── overview.md         # viikon teema + must-do-minimi vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria, kattaa kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---' erottimet
teacher/week-03/
├── teacher-materials.md  # 3 × 90 min ohjaus, oppituntikohtaisilla kalvovihjeillä
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajavetoinen tuntiharjoitus
```

Lisäksi vain silloin, kun luento-osio aidosti tarvitsee syvemmän materiaalin, lisätiedosto `student/week-03/slides-l<n>-<aihe>.md` (4–8 kalvoa). Rasmus päättää luento-osiokohtaisesti.

## Kovat säännöt kaikille viikoille
- **Englanti läpi**, kaikki 7 tiedostoa.
- **"AI-resilient"-leima on sisäinen** — se ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuutta, ei leimaa.
- **"If you are doing this alone"** -alaosio (`### If you are doing this alone`) vaaditaan jokaiseen tehtävään, joka olettaa parin / seuraajan / testaajan, ja sen mukana konkreettinen vaihtoehto (24h tauko, videoitu oma itsesi, eri laite, luokan chat).
- **"Must-do minimum"** on PAKOLLISTEN tehtävien sanamuoto overview.md:ssä ja student-tasks.md:ssä (ei "mandatory minimum").
- **Kalvovihjeet** vaaditaan jokaiselle 90 minuutin oppituntisuunnitelmalle `teacher-materials.md`:ssä.
- **30–50 % itsenäistä työtä** -lohko vaaditaan jokaiseen 90 minuutin oppituntisuunnitelmaan.
- **Ei kalvotiedostoja `slides.md`:n (+ valinnainen `slides-l<n>-*.md`) lisäksi.** Ei PowerPointia, ei jest/mocha/vitest/pytest-viittauksia missään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi jos viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitaan kyseinen AT).
- **Tiedostojen välinen johdonmukaisuus**: tehtävänumerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; `teacher-materials.md`:ssä viitatut tuntiaktiviteetit löytyvät `in-class-tasks.md`:stä.

## Kurssitason konteksti
Yllä oleva toimeksianto on siivu **viikolta 3** 8-viikkoisesta kurssista. Täysi kurssitoimeksianto ja lukittu 24 oppitunnin tiekartta on:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssitoimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon tiekartta)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyylireferenssinä)

## Kultainen näyte (suomeksi, tyyli/syvyys/laajuus-referenssi)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason laajuus on noin 3 × yhden kultaisen näyteoppitunnin laajuus. Yllä mainitun polun viikon 1 julkaisu on myös referenssi kokonaiselle englanninkieliselle viikolle.
