# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 8 (englanniksi)

## Viikon 8 teema
**Ohjelmointikielet käytännössä (JavaScript & C#, osa 2)**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O22**: Silmukat koodissa: yksinkertainen for- tai while-rakenne
- **O23**: Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:iin
- **O24**: Testaaminen, aloittelijatason virheenkorjaus, esittäminen ja oman ratkaisun selittäminen

## Viikon keskeinen viesti
Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen JavaScriptiksi tai C#:ksi, ajat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi on lakannut olemasta mystinen asia.

## Bloom-katto
Soveltaminen + kevyt Arvioiminen (vertaile omaa ratkaisua vertaisen ratkaisuun, selitä omin sanoin, korjaa yksi bugi).

## Ammatillinen kulma
Esimerkkejä, joihin Rasmuksen kannattaa nojata: ikätarkistus, salasanan pituuden tarkistus, pisteet-palautteeksi-ohjelma, yksinkertainen laskuri, tervehdys nimellä, oikean vastauksen tarkistaja.

## Arvioinnin kosketuspiste
AT3 (pieni JavaScript- tai C#-ratkaisu omasta pseudokoodista) palautetaan ja esitetään tällä viikolla. O23 on rakennuspäivä; O24 on testaus- ja esityspäivä.

## Lisäsäännöt tälle viikolle

- **Kaksikielisyysvaatimus jatkuu.** Ohjelmointiesimerkit ja tehtävät sekä JavaScriptillä että C#:lla, erillisissä tehtävätiedostoissa (`student-tasks-js.md` ja `student-tasks-csharp.md`). Opiskelijat valitsevat yhden kielen ja tekevät AT3:n sillä. Molemmat kielet on tuettava tasapuolisesti — Sunen suunnitelma ei saa suosia toista toisen kustannuksella.
- O24:n 'virheenkorjaus' **ei** tarkoita debuggerin käyttöä tai mitään automatisoitua testauskehystä. Se tarkoittaa konsolin virhetekstin lukemista, sen syyn paikantamista ja yhden pienen korjauksen tekemistä.
- O24 sisältää 2 minuutin suullisen esityksen — tämä on AT3:n reflektio- / suullinen osuus.

## Tulostuskieli
**Englanti.** Börje (suomenkielinen viimeistely) ohitetaan tällä ajolla.

## Tuotoslaajuus (tällä ajolla)
- Sune tuottaa viikon 8 suunnitelman lukittuine hyväksymiskriteereineen, Rasmus-briiffauksineen ja tulevaisuuteen katsovine tynkineen.
- Rasmus rakentaa **vain viikon 8**.
- Linnea + Wilhelm auditoivat viikon 8.
- Alfred paketoi viikon 8 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** tässä putkikierroksessa. Markdown-julkaisu on toimitettava.

## Kanoninen viikkokohtainen lohkorakenne (lukittu)
```
student/week-08/
├── overview.md         # viikon teema + must-do minimum vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria, joka kattaa kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---' erottimina
teacher/week-08/
├── teacher-materials.md  # 3 × 90 min fasilitointia, oppituntikohtaisin kalvovihjein
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajavetoinen tuntiharjoitus
```

Lisäksi vain silloin, kun jokin luento-osuus aidosti tarvitsee syvempää aineistoa, lisätiedosto `student/week-08/slides-l<n>-<topic>.md` (4–8 kalvoa). Rasmus päättää luento-osuuskohtaisesti.

## Kovat säännöt kaikille viikoille
- **Englanniksi kauttaaltaan**, kaikki 7 tiedostoa.
- **"AI-resilient" -merkintä on sisäinen** — ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuutta, ei merkintää.
- **"If you are doing this alone"** -aliotsikko (`### If you are doing this alone`) on pakollinen jokaisessa tehtävässä, joka olettaa parin / seuraajan / testaajan, ja siihen kuuluu konkreettinen vaihtoehto (24 h tauko, video itsestä, eri laite, luokan chat).
- **"Must-do minimum"** on sanamuoto PAKOLLISILLE tehtäville overview.md:ssä ja student-tasks.md:ssä (ei "mandatory minimum").
- **Kalvovihjeet** vaaditaan jokaiselle 90 minuutin oppituntisuunnitelmalle `teacher-materials.md`:ssä.
- **30–50 % itsenäisen työn** lohko vaaditaan jokaiseen 90 minuutin oppituntisuunnitelmaan.
- **Ei kalvotiedostoja `slides.md`:n (+ valinnaisen `slides-l<n>-*.md`:n) lisäksi.** Ei PowerPointia, ei viittauksia jest/mocha/vitest/pytest-kehyksiin missään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi jos tämän viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitaan relevantti AT).
- **Tiedostojen välinen johdonmukaisuus**: tehtävänumerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; `teacher-materials.md`:ssä viitatut tuntiaktiviteetit löytyvät `in-class-tasks.md`:stä.

## Kurssitason konteksti
Yllä oleva toimeksianto on **viikon 8** siivu 8 viikon kurssista. Koko kurssin toimeksianto ja lukittu 24 oppitunnin tiekartta on osoitteessa:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssitoimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon tiekartta)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyyliesimerkkinä)

## Kultainen malli (suomeksi, tyyli/syvyys/volyymi-referenssi)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason volyymi on ~3× yhden kultaisen mallioppitunnin volyymi. Viikon 1 julkaisu yllä olevassa polussa on myös referenssi kokonaiseen englanninkieliseen viikkoon.

