# Ohjelmallinen ajattelu — viikon 8 suunnitelma (Sune, Portti #1)

Kurssi: Ohjelmallinen ajattelu (englanniksi)
Kohderyhmä: 1. vuoden ammatillisen ICT:n opiskelijat, ~15–17 v., ei aiempaa ohjelmointitaustaa
Kesto: 8 viikkoa × 3 oppituntia/viikko × 90 min = 24 oppituntia
Putkikierroksen laajuus tällä ajolla: Sune tuottaa tämän viikon 8 suunnitelman; Rasmus rakentaa koko viikon 8 paketin kaksikielisessä viikkorakenteessa; Linnea/Wilhelm auditoivat viikon 8; Alfred paketoi viikon 8 Markdown-julkaisun. Ei PDF:ää, ei PPTX-renderöintiä.

Viikko 8 sulkee kurssin. AT3 (pieni JavaScript- tai C#-ohjelma, joka on rakennettu opiskelijan omasta viikon 6 pseudokoodista) palautetaan ja esitetään tällä viikolla.

---

## Suunnitelma

### Mihin viikko 8 sijoittuu

Viikko 8 sulkee kaaren, jonka viikko 1 avasi. Oppitunti 1 kysyi *"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"* Viikko 8 vastaa tähän konkreettisesti: opiskelija kirjoittaa pienen ohjelman, ajaa sen, näkee oikean virheilmoituksen, korjaa bugin ja selittää ohjelman ääneen toiselle ihmiselle kahdessa minuutissa. Ohjelmointi ei enää ole mysteeri — se on 15 rivin tiedosto, jonka opiskelija osaa lukea ylhäältä alas ja puolustaa.

Viikolla 7 esiteltiin JavaScript ja C# rinnakkain (tuloste, muuttujat, vertailut, if/else). Opiskelijat valitsivat kielensä viikon 7 lopussa ja pitäytyivät siinä AT3:a varten. Viikko 8 lisää kerroksen silmukoita ja kokoaa sitten kaikki kurssin käsitteet (sekvenssi, ehto, toisto, muuttujat, syöte/tuloste) yhdeksi pieneksi toimivaksi ohjelmaksi opiskelijaa kohden.

### Viikon 8 teemalause

Viikko 8 on **synteesiviikko**: käsitteellisesti mitään aidosti uutta, mutta ensimmäinen kerta, kun kaikki, mitä kurssi on harjoitellut — ositus, täsmälliset ohjeet, vuokaaviot, vaihtoehdot, logiikkarakenteet, pseudokoodi — kootaan oikealla ohjelmointikielellä ja ajetaan oikealla koneella. Kolme oppituntia käsittelevät (O22) silmukoita, (O23) yhtä kokonaista rakennuspäivää, jolloin opiskelijat kääntävät palan omaa viikon 6 pseudokoodiaan JavaScriptiksi tai C#:ksi, ja (O24) testaamista, yhden bugin korjaamista ja tuloksen esittämistä 2 minuutin suullisena. Viikon lopussa jokainen opiskelija on palauttanut **AT3:n**: pienen ohjelman ja 2 minuutin esityksen valitsemallaan kielellä.

### O22–O24 -jako viikolle 8

#### Oppitunti 22 — Silmukat koodissa: yksinkertainen for- tai while-rakenne

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Tunnista** silmukka koodissa ja **nimeä** osat: ehto, runko, päivitys. *(Ymmärtäminen)*
  - (b) **Lue** pieni for-/while-silmukka ja **ennusta**, mitä se tulostaa. *(Ymmärtäminen)*
  - (c) **Kirjoita** 3–6 rivin silmukka, joka pyörii tunnetun määrän kertoja (laske 1–5, tulosta "Hello" kolme kertaa). *(Soveltaminen)*
  - (d) **Yhdistä** viikon 5/6 toista-kunnes-kuvio toimivaan for-/while-silmukkaan. *(Soveltaminen)*
- **Avainsanaston ennakointi:** loop, for, while, laskuri, ehto (palautetaan mieleen), runko, iteraatio, ikuinen silmukka.
- **Keskeinen viesti (yhdellä lauseella):** Silmukka on muodollinen nimi sille *toista-kunnes*-idealle, jonka kurssi on jo opettanut — vain nyt toistaja on tietokone, ei ihminen.

#### Oppitunti 23 — Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:iin

- **Oppimistavoitteet** (Soveltaminen):
  - (a) **Valitse** yksi omasta viikon 6 pseudokoodipätkästäsi käännettäväksi. *(Soveltaminen)*
  - (b) **Käännä** kyseinen pseudokoodi toimivaksi JavaScript- tai C#-ohjelmaksi, jossa on ~10–25 riviä. *(Soveltaminen)*
  - (c) **Aja** ohjelma selaimen konsolissa (JS) tai online-.NET-ajurissa (C#) ja varmista vähintään yksi odotettu tuloste. *(Soveltaminen)*
  - (d) **Tallenna** lähdekoodi `.js`- tai `.cs`-tiedostona (tai selvästi merkittynä pätkänä AT3-palautukseen liitettynä). *(Soveltaminen)*
- **Avainsanaston ennakointi:** kääntäminen (pseudokoodi → koodi), lähdekooditiedosto, ajaminen, odotettu tuloste, todellinen tuloste.
- **Keskeinen viesti (yhdellä lauseella):** Pseudokoodin kääntäminen ohjelmointikieleen on enimmäkseen englanninkielisten sanojen korvaamista kielen syntaksilla — rakenne oli jo paikoillaan.

#### Oppitunti 24 — Testaaminen, aloittelijatason virheenkorjaus, esittäminen ja oman ratkaisun selittäminen

- **Oppimistavoitteet** (Soveltaminen + kevyt Arvioiminen):
  - (a) **Testaa** ohjelmaa ajamalla sitä ainakin kahdella eri syötteellä/arvolla. *(Soveltaminen)*
  - (b) **Lue** oikea virheilmoitus (tai odottamaton tuloste) ja **paikanna** vastuussa oleva rivi. *(Soveltaminen)*
  - (c) **Sovella** yhtä pientä korjausta ja aja uudelleen. *(Soveltaminen)*
  - (d) **Selitä** ohjelma vertaiselle tai luokalle **kahdessa minuutissa**: mitä se tekee, miten se tekee sen, mikä meni vikaan, miten se korjattiin. *(kevyt Arvioiminen — oma työ)*
  - (e) **Vertaile** omaa ratkaisuasi vertaisen ratkaisuun selkeällä englannilla (eri valintoja, sama tavoite). *(kevyt Arvioiminen)*
- **Avainsanaston ennakointi:** testi, virheilmoitus, bugi, korjaus, esitys, vertaispalaute.
- **Keskeinen viesti (yhdellä lauseella):** Virheenkorjaus tällä tasolla tarkoittaa sen lukemista, mitä tietokone kertoi, sen yhden rivin löytämistä, josta se puhui, ja yhden pienen muutoksen tekemistä — erikoistyökaluja ei tarvita.

### Viikko 8 — must-do minimum vs. syventävä

**Must-do minimum (jokaisen opiskelijan on osattava viikon 8 jälkeen):**
- Lukea pieni for- tai while-silmukka valitsemallaan kielellä ja ennustaa sen tuloste.
- Kääntää yksi pala omaa viikon 6 pseudokoodiaan pieneksi, toimivaksi JavaScript- tai C#-ohjelmaksi.
- Ajaa ohjelman, nähdä todellisen tulosteen ja palauttaa lähdekoodi sekä kuvakaappaus AT3:na.
- Laukaista vähintään yhden virheilmoituksen tarkoituksella tai vahingossa, lukea sen ja soveltaa yhtä pientä korjausta.
- Pitää 2 minuutin suullinen esitys ohjelmasta (mitä se tekee, miten, bugi, korjaus).

**Syventävä (valinnainen lisäosa, ei vaadittu AT3:n läpäisyyn):**
- Yhdistää silmukan if/elseen (esim. laske, kuinka moni salasanoista on tarpeeksi pitkä).
- Vertailla omaa JS-versiotaan luokkakaverin saman ohjelman C#-versioon (tai päinvastoin) ja kirjoittaa 3–5 lausetta eroista.
- Lisätä syöte funktioista `prompt()` (JS) tai `Console.ReadLine()` (C#) ja validoida se.
- Laajentaa ohjelmaa toisella ominaisuudella, joka kirjoitetaan ensin pseudokoodirivinä ja sitten käännetään.

### Kaksikielinen rakenne (jatkuu viikolta 7)

Molemmat kielet ovat tasapuolisesti tuettuja. Opiskelija valitsi JS:n tai C#:n viikon 7 lopussa ja pysyy valinnassaan AT3:n osalta. Rasmus toimittaa **molemmat** tehtävätiedostot täysimittaisina, molemmat sisältäen saman määrän ja muotoiset tehtävät, molemmat rinnakkaiset AT3-briiffaukset. Mikään kieli ei ole "oletus" eikä mikään kieli ole "vaihtoehto".

```
student/week-08/
├── overview.md
├── self-study.md            # kattaa molemmat kielet rinnakkain
├── student-tasks-js.md      # 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ, kaikki JavaScriptillä
├── student-tasks-csharp.md  # 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ, kaikki C#:lla
├── vocabulary.md            # termit kielineutraaleja, missä mahdollista
└── slides.md
teacher/week-08/
├── teacher-materials.md
└── in-class-tasks.md
```

AT3-briiffaus on itsessään yksi PAKOLLISISTA tehtävistä **molemmissa** tiedostoissa `student-tasks-js.md` ja `student-tasks-csharp.md`. Kaksi AT3-briiffausta ovat rinnakkaisia: sama laajuus, samat tuotokset, sama sanamäärä, sama palautusmuoto — vain kieli eroaa.

### Kurssin sulkeminen: viikko 8 takaisin viikkoon 1

Oppitunti 24 palaa eksplisiittisesti kurssin keskeiseen kysymykseen. O24:n suunnitelmassa ja yhdellä `slides.md`:n loppupään kalvolla kysymys esiintyy sanatarkasti vielä kerran — *Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?* — rinnalla rehellinen tunnustus, että opiskelijalla on nyt toimiva vastaus.

---

## Rajaukset

**Viikon 8 ulkopuolella:**
- **Ei automaattisia testaus- tai virheenkorjauskehyksiä.** Ei jest, mocha, vitest, pytest, xUnit, NUnit, MSTest, FsCheck. Sanottu eksplisiittisesti. "Testaaminen" O24:ssä tarkoittaa ohjelman ajamista käsin eri arvoilla. "Virheenkorjaus" tarkoittaa konsolin virheen lukemista ja yhden pienen korjauksen soveltamista.
- **Ei varsinaista debuggeria.** Ei `debugger;`-lausetta, ei Chrome DevToolsin keskeytyspisteitä, ei Visual Studion keskeytyspisteitä, ei askel-askeleelta-ajoa. O24:n virheenkorjausharjoitus on tekstin lukemista ja yhden rivin muuttamista.
- **Ei uusia ohjelmointikielen ominaisuuksia silmukoiden lisäksi.** Ei funktioita, ei taulukoita JS:ssä (lista-tyylinen silmukka voi käyttää sellaista vain C#:ssa, jos yksinkertaisin esimerkki aidosti tarvitsee sitä; muutoin pitäydy laskurisilmukoissa), ei olioita, ei luokkia, ei moduuleja, ei async, ei LINQ.
- **Ei npm:ää, ei Node.js-asennusta, ei Visual Studio -asennusta.** JS pyörii selaimen konsolissa; C# pyörii online-.NET-ajurissa (dotnetfiddle.net tai vastaava), joka ei vaadi rekisteröitymistä valinnaisen sähköpostin lisäksi.
- **Ei arviointimatriisia yksinkertaisen tarkistuslistan lisäksi.** AT3 on hyväksytty / ei-vielä-hyväksytty pienen havaittavien kriteerien joukon perusteella (ohjelma pyörii; opiskelija osaa nimetä, mitä se tekee; vähintään yksi bugi on korjattu).
- **Ei pitkää kirjallista raporttia.** AT3 sisältää lähdekoodin, kuvakaappauksen ja 2 minuutin suullisen. Ei esseetä.
- **Ei PowerPointia, ei PPTX:ää, ei Reveal.js:ää, ei Google Slidesia.** Rasmus tuottaa vain `slides.md`:n.
- **Bloom-katto: Soveltaminen + kevyt Arvioiminen.** Kiellettyjä verbejä viikon 8 tavoitteissa: *suunnittele, kehitä, rakenna, luo (Bloom-verbinä), analysoi, suunnittele arkkitehtuuri, optimoi, refaktoroi*. "Luo" arkipäiväisessä merkityksessä ("luo tiedosto") on hyväksyttävää — kielletty on Bloom-tason *Luomis*-verbi.

**Kieli:** Englanti kauttaaltaan. Sune-pohjan H2-otsikot (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) pysyvät suomeksi tässä suunnitelmatiedostossa; kaikki 7 Rasmus-tiedostoa ovat täysin englanniksi.

**Putkikierroksen laajuus tällä ajolla:**
- Sune tuottaa tämän viikon 8 suunnitelman (jota luet).
- Rasmus rakentaa **vain viikon 8** kaksikielisessä viikkorakenteessa (7 pakollista tiedostoa; valinnainen täydentävä `slides-l<n>-*.md` vain, jos luento-osuus sitä aidosti tarvitsee).
- Linnea ja Wilhelm auditoivat vain viikon 8.
- Alfred paketoi viikon 8 Markdown-julkaisun.

---

## Hyväksymiskriteerit

Wilhelm tarkistaa viikon 8 paketin seuraavien konkreettisten, tarkastettavien kriteerien mukaan.

### Rakenteelliset — tiedostot ja kansiot

1. **Kaikki 7 kanonista tiedostoa läsnä**, täsmälleen näillä tiedostonimillä (kirjainkokoherkkä, pienaakkoset, kebab-case):
   - `student/week-08/overview.md`
   - `student/week-08/self-study.md`
   - `student/week-08/student-tasks-js.md`
   - `student/week-08/student-tasks-csharp.md`
   - `student/week-08/vocabulary.md`
   - `student/week-08/slides.md`
   - `teacher/week-08/teacher-materials.md`
   - `teacher/week-08/in-class-tasks.md`
2. **Ei `student-tasks.md`-tiedostoa** kansion `student/week-08/` ylätasolla. Kaksi kielikohtaista tiedostoa korvaavat sen. (Valinnainen 5-rivinen `student-tasks.md` *hakemisto* sallitaan, jos Rasmus haluaa sellaisen, mutta se ei ole pakollinen eikä se saa sisältää tehtäväsisältöä.)
3. **Ei `.pptx`, `.key`, Reveal.js HTML- tai muita kalvomuotoja** missään. Kova hylkäys, jos löytyy.
4. **Valinnainen täydentävä kalvopaketti** sallittu: `student/week-08/slides-l24-presentation-rubric.md` (4–8 kalvoa). Rasmus päättää, sisällyttääkö sen.

### Volyymi (järkevyystarkistusrajat, ei kovia rajoja)

5. `overview.md`: **200–400 sanaa**.
6. `self-study.md`: **2400–4000 sanaa** (kattaa O22, O23, O24, molemmat kielet rinnakkain).
7. `student-tasks-js.md`: **800–1800 sanaa**. **1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ** tehtävää, kaikki JavaScriptillä.
8. `student-tasks-csharp.md`: **800–1800 sanaa**. **1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ** tehtävää, kaikki C#:lla. **Rinnakkainen lukumäärältään ja muodoltaan** tiedoston `student-tasks-js.md` kanssa.
9. `vocabulary.md`: **10–18 termiä**, sanamuoto kielineutraali, missä mahdollista; missä termi tarvitsee molemmat syntaksit (esim. "silmukan avainsana"), anna JS- ja C#-muoto rinnakkain.
10. `slides.md`: **~12–20 kalvoa** (hieman korkeampi kuin 10–20 perustaso, koska viikko kattaa silmukat + AT3 + esityksen).
11. `teacher-materials.md`: **2400–4400 sanaa**. Sisältää **3 × 90 minuutin oppituntisuunnitelmaa** (O22, O23, O24), joiden kesto on yhteensä 90 ja joissa on oppituntikohtaiset **kalvovihjeet**.
12. `in-class-tasks.md`: **400–1200 sanaa**. **Vähintään 1 PAKOLLINEN** opettajavetoinen tuntiharjoitus.

### Pakolliset H2-osiot tiedostoittain

13. `overview.md`:n on sisällettävä (tässä järjestyksessä):
    - `## Week 8 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening`
    - `## How the three lessons fit together`
    - `## Choosing your language (reminder from Week 7)`
14. `self-study.md`:n on sisällettävä:
    - `# <Viikon otsikko>` (houkutteleva H1).
    - `## Introduction` — toistaa kurssin keskeisen kysymyksen sanatarkasti ja esittelee AT3:n.
    - `## Lesson 22 — Loops in code` (tai lähivariaatio), **JS- ja C#-alaosiot rinnakkain**.
    - `## Lesson 23 — From pseudocode to a small program`.
    - `## Lesson 24 — Test, fix one bug, present`.
    - `## How AT3 is assessed` — tarkistuslistaversio AT3:n kriteereistä.
    - `## Summary — closing the loop on the central question`.
    - **Vähintään 4 `> **Pause for a moment:**` -pohdintakehotetta** kolmen oppitunnin yli (vähintään 1 per oppitunti).
15. `student-tasks-js.md` ja `student-tasks-csharp.md` -tiedostojen on kummankin sisällettävä:
    - `## Overview of the week's tasks`
    - Yksi H2 per tehtävä, alkutunnisteena `🟢 MANDATORY —` tai `🟣 DEEPENING —`.
    - **Yksi PAKOLLINEN tehtävä tiedostoa kohden on itse AT3-briiffaus.**
    - Jokainen tehtävä päättyy `### Keep your notes` -lohkoon, joka mainitsee **AT3:n eksplisiittisesti** (tämän viikon palautus), ei AT1:tä.
    - Jokainen tehtävä, joka olettaa parin (vertaislukija, tuntiesitys, luokkakaveri-testaajana), sisältää `### If you are doing this alone` -aliotsikon konkreettisella vaihtoehdolla (24 h tauko, video itsestä, luokan chat, eri laite).
    - Sanonta **"must-do minimum"** esiintyy vähintään kerran yleiskatsauksessa tai PAKOLLISTEN tehtävien kuvauksissa.
16. `vocabulary.md`:n on sisällettävä yksi H2 `## Week 8 vocabulary`. Vähintään yksi termi merkitty **"kurssin loppukoonti — palautettu mieleen aiemmilta viikoilta"** (ehdota *algorithm*, *pseudocode* tai *condition*).
17. `slides.md`:n on:
    - Aloitettava otsikkokalvolla.
    - Sisällettävä vähintään yksi kalvo, joka näyttää kurssin keskeisen kysymyksen sanatarkasti (kurssin päätöskalvo lähellä loppua).
    - Käytettävä `---`-merkintää omalla rivillään kalvojen välissä.
    - Esitettävä **sekä JS- että C#-syntaksia rinnakkain** vähintään silmukan esittelykalvolla ja if/else-silmukkakalvolla (jos sellainen on).
    - Viitattava tehtävänumeroihin johdonmukaisesti molempien tehtävätiedostojen kanssa (esim. *Tehtävä 8.1 (PAKOLLINEN) — katso oman kielesi tehtävätiedostosta*).
18. `teacher-materials.md`:n on sisällettävä (tässä järjestyksessä):
    - `## Week 8 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 8` (≥6 viikossa, ≥2 per oppitunti, jokaisella *Correction:* -rivi)
    - `## Lesson 22 — 90-minute plan` — **Slide cues** -aliotsikko.
    - `## Lesson 23 — 90-minute plan` — **Slide cues**.
    - `## Lesson 24 — 90-minute plan` — **Slide cues**, **on sisällettävä 2 minuutin opiskelijan esitysosuus**.
    - `## Facilitation tips`
    - `## Answers to common student questions` (≥5 viikossa)
    - `## Formative assessment tips`
19. `in-class-tasks.md`:n on sisällettävä:
    - `## Overview`
    - Vähintään 1 H2-tehtävä merkitty **MANDATORY**, joka vaatii aitoa luokkahuonevuorovaikutusta (parityö, näytä-ja-kerro, koko luokan loppukeskustelu). Ristiviitattu tiedostosta `teacher-materials.md`.

### Pedagogiset säännöt

20. **30–50 % -sääntö**: `teacher-materials.md`:ssä kunkin kolmen 90 minuutin oppituntisuunnitelman aikajanoilla näkyvästi *opiskelijan itsenäiseksi työksi* merkityt lohkot ovat yhteensä **27–45 minuuttia**. Wilhelm tarkistaa aritmeettisesti.
21. **Bloom-katto**: Viikon 8 oppimistavoitteet käyttävät vain Soveltamis-verbejä (*käännä, kirjoita, aja, testaa, sovella, ennusta, lue, paikanna, korjaa, vertaile, selitä*) sekä kevyttä Arvioimista O24:ssä (*vertaile omaa ratkaisua vertaisen ratkaisuun*, *selitä oma valinta omin sanoin*). Kiellettyjä verbejä viikon 8 tavoitteissa: *suunnittele, kehitä, rakenna, suunnittele arkkitehtuuri, optimoi, refaktoroi, arvioi, kritisoi, analysoi* (Bloom-verbeinä).
22. **Keskeinen kysymys** — *Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?* — esiintyy **sanatarkasti** tiedostossa `self-study.md` (Introduction ja Summary tai ainakin kerran yhteensä) **ja** vähintään yhdellä kalvolla tiedostossa `slides.md` (kurssin päätöskalvo).
23. **Kaksikielinen pariteetti**: jokaisella konkreettisella syntaksiesimerkillä `self-study.md`:ssä ja `slides.md`:ssä, joka on olemassa JS:lle, on myös C#-vastine ja päinvastoin. Wilhelm tarkistaa pistokokein 5 esimerkkiä.
24. **O24:n virheenkorjauksen kehystys**: "debugging" missä tahansa tiedostossa viittaa **konsolin virheilmoituksen lukemiseen ja yhden pienen korjauksen soveltamiseen**. Ei viittauksia debuggeriin, keskeytyspisteisiin, askel-askeleelta-ajoon tai mihinkään automatisoituun testaustyökaluun.
25. **Ei testaus-/virheenkorjauskehyksiä**: merkkijonot `jest`, `mocha`, `vitest`, `pytest`, `xunit`, `nunit`, `mstest`, `chai`, `assert` (kehyksen nimenä), `debugger;` (JS-lause), `Debug.WriteLine`, *breakpoint*, *step over*, *step into* eivät esiinny yhdessäkään 7 tiedostosta. Wilhelm hakee.
26. **Kurssin päätöksen kehystys**: vähintään yksi kappale `self-study.md`:ssä ja yksi kalvo `slides.md`:ssä yhdistää viikon 8 takaisin oppituntiin 1 eksplisiittisesti (mainitsee "Week 1" tai "Lesson 1" tai "the central question we started with").

### Tehtävät (AI-resilienssi ja kaksikielinen pariteetti)

27. Kumpikin tiedosto `student-tasks-js.md` ja `student-tasks-csharp.md` sisältää **1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ** tehtävää. **AT3-briiffaus on yksi PAKOLLISISTA tehtävistä molemmissa tiedostoissa.** Kaksi AT3-briiffausta ovat rinnakkaisia laajuudeltaan, tuotoksiltaan ja sanamäärältään.
28. **AT3-briiffaus-PAKOLLINEN tehtävä** on AI-resilientti rakenteeltaan: se vaatii opiskelijan omaa viikon 6 pseudokoodia (heidän oma artefaktinsa aikaisemmalta kurssilta), aidon ajon-ja-kuvakaappauksen sekä 2 minuutin suullisen esityksen. LLM ei voi väärentää mitään näistä ilman, että opettaja huomaa.
29. Jos SYVENTÄVÄ tehtävä käyttää LLM:ää sparrauskumppanina (esim. "pyydä LLM:ää ehdottamaan yhtä laajennusta ja hylkää tai muokkaa sitten"), se sisältää aidoatun esimerkkikehotteen ja eksplisiittisen ohjeen olla liittämättä LLM:n tulostetta sanatarkasti.
30. 2 minuutin suullisen esityksen vaatimus mainitaan **AT3-briiffaus-PAKOLLISEN tehtävän sisällä** molemmissa kielitiedostoissa (ei vain `teacher-materials.md`:ssä).

### Tuntitehtävät

31. `in-class-tasks.md` sisältää **vähintään 1 PAKOLLISEN** opettajavetoisen tuntiharjoituksen, joka aidosti vaatii luokkahuonevuorovaikutusta. Suositeltu oletus on **"Show-and-tell loops"** (ks. Briefing). Se on ristiviitattu tiedostosta `teacher-materials.md` täsmälleen oikealla 90 min aikalohkolla oppitunnilta O22 tai O23.

### Kieli ja viimeistely

32. **Englanti kauttaaltaan**, ei suomea yhdessäkään 7 tiedostosta paitsi selvästi välttämättömissä erisnimissä.
33. **Rekisteri**: `self-study.md`, `student-tasks-js.md`, `student-tasks-csharp.md`, `overview.md`, `vocabulary.md`, `slides.md` CEFR-tasolla ~B1; `teacher-materials.md` ja `in-class-tasks.md` CEFR-tasolla ~B2.
34. **Validi Markdown**: jokainen koodiaita sulkeutuu (ja on aidattu `js`- tai `csharp`-tunnuksella tarpeen mukaan), jokainen taulukko renderöityy, ei rikkinäisiä sisäisiä linkkejä, `---`-erotin `slides.md`:ssä yksinään omalla rivillään.

### AT3:n hyväksymiskriteerit (lukittu, esillä `self-study.md`:ssä ja molemmissa tehtävätiedostoissa)

35. Opiskelija palauttaa valitsemallaan kielellä:
    - lähdekoodin (tiedosto tai selvästi aidattu pätkä, kielitunnisteen vastatessa valittua kieltä);
    - kuvakaappauksen ohjelman ajosta vähintään yhdellä odotetulla tulosteella;
    - 3–5 lauseen kirjallisen reflektion, jossa nimetään **yksi bugi**, jonka löysi, ja **yksi korjaus**, jonka teki;
    - 2 minuutin suullisen esityksen luokassa O24:llä.
36. Opettajan hyväksytty / ei-vielä-hyväksytty -tarkistus kattaa:
    - ohjelma pyörii (tai dokumentoitu yritys korjauksesta, joka ei onnistunut, ja virheilmoitus kirjattu);
    - opiskelija osaa nimetä selkeällä englannilla, mitä ohjelma tekee;
    - vähintään yksi bugi-ja-korjaus-pari on dokumentoitu;
    - 2 minuutin esitys on pidetty.

---

## Briefing Rasmukselle

### Ristikkäiset muistutukset (koskevat kaikkia 8 tiedostoa, joita Rasmus saattaa tuottaa — 7 pakollista + valinnainen rubriikkikalvopaketti)

- **Silmukan sulkeminen.** Tämä on viimeinen viikko. Nojaa jatkuvuuteen: viittaa jokaisessa tiedostossa vähintään yhden aiemman viikon artefaktiin (viikon 6 pseudokoodi, viikon 5 ehdot, viikon 1 keskeinen kysymys).
- **Molemmat kielet ovat ensiluokkaisia.** Älä koskaan kirjoita "the JavaScript version" ennen "the C# version" -ilmausta kaikkialla; vaihtele, kumpi kieli näytetään ensin esimerkkien välillä. Molemmat kielet saavat yhtä paljon tilaa jokaisella jaetulla kalvolla ja jokaisessa jaetussa itseopiskelu-osiossa.
- **"Virheenkorjaus" on lukemista ja korjaamista, ei työkaluja.** Aina kun sana *debugging* esiintyy missään tiedostossa, ympäröivän tekstin on tehtävä selväksi, että tämä tarkoittaa konsolin virheilmoituksen lukemista ja yhden rivin muuttamista. Ei viittauksia debuggeriin. Ei viittauksia keskeytyspisteisiin.
- **AT3 O24:llä sisältää 2 minuutin suullisen esityksen.** Mainitse aikaraja eksplisiittisesti (sanat "2 minutes" tai "two minutes").
- **"Must-do minimum"** on sanamuoto PAKOLLISILLE tehtäville overview.md:ssä ja kahdessa student-tasks-tiedostossa (ei "mandatory minimum").
- **"If you are doing this alone"** -aliotsikko vaaditaan jokaisessa tehtävässä, joka olettaa parin (vertaislukija, esityksen yleisö, luokkakaveri-testaajana). Vaihtoehtoja ovat: jätä 24 h tauko ja lue oma ohjelmasi tuoreilla silmillä, nauhoita itsesi pitämässä esitystä videona, julkaise luokan chatissa vertaiskommenttia varten, aja ohjelma eri laitteella.
- **Ei viittauksia `.pptx`-muotoon.** Rasmus toimittaa `slides.md`:n; orkesterointi (ei tämän kierroksen laajuudessa) tekisi muunnoksen. Tällä kierroksella ei tuoteta PDF:ää eikä PPTX:ää.
- **Ei testaus-/virheenkorjauskehyksiä missään.**
- **Keskeisen kysymyksen on esiinnyttävä sanatarkasti** `self-study.md`:ssä ja yhdellä `slides.md`:n kalvolla: *Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?*

---

### Ohjelmat, joita opiskelijat oikeasti rakentavat — molemmat kielet, valmiit luonnokset

Rasmus poimii 4–6 näistä esimerkkiohjelmiksi tiedostoon `self-study.md` ja aloitusesimerkkeinä tehtävätiedostoihin. Kaikki ovat pieniä, kaikki ovat käännettävissä viikon 6 pseudokoodikuvioista, joita opiskelijat ovat jo harjoitelleet, kaikki pyörivät selaimen konsolissa (JS) tai online-.NET-ajurissa (C#).

**Ohjelma A — Ikätarkistus**
- *Pseudokoodikuvio (viikko 6):* lue ikä, jos ikä ≥ 18 tulosta "allowed", muuten tulosta "not allowed".
- *JavaScript:*
  ```js
  let age = 17;
  if (age >= 18) {
    console.log("allowed");
  } else {
    console.log("not allowed");
  }
  ```
- *C#:*
  ```csharp
  int age = 17;
  if (age >= 18) {
      Console.WriteLine("allowed");
  } else {
      Console.WriteLine("not allowed");
  }
  ```

**Ohjelma B — Salasanan pituuden tarkistus**
- *Pseudokoodikuvio:* lue salasana, jos pituus ≥ 8 tulosta "strong enough", muuten tulosta "too short".
- *JS:*
  ```js
  let password = "hi";
  if (password.length >= 8) {
    console.log("strong enough");
  } else {
    console.log("too short");
  }
  ```
- *C#:*
  ```csharp
  string password = "hi";
  if (password.Length >= 8) {
      Console.WriteLine("strong enough");
  } else {
      Console.WriteLine("too short");
  }
  ```

**Ohjelma C — Pisteet palautteeksi**
- *Pseudokoodikuvio:* annettuna pisteet, tulosta yksi kolmesta viestistä.
- *JS:*
  ```js
  let score = 72;
  if (score >= 80) {
    console.log("great work");
  } else if (score >= 50) {
    console.log("you passed");
  } else {
    console.log("try again");
  }
  ```
- *C#:*
  ```csharp
  int score = 72;
  if (score >= 80) {
      Console.WriteLine("great work");
  } else if (score >= 50) {
      Console.WriteLine("you passed");
  } else {
      Console.WriteLine("try again");
  }
  ```

**Ohjelma D — Yksinkertainen laskuri (O22:n silmukkaesimerkki)**
- *Pseudokoodikuvio:* toista 5 kertaa: tulosta nykyinen luku.
- *JS:*
  ```js
  for (let i = 1; i <= 5; i++) {
    console.log(i);
  }
  ```
- *C#:*
  ```csharp
  for (int i = 1; i <= 5; i++) {
      Console.WriteLine(i);
  }
  ```

**Ohjelma E — Tervehdys nimellä (silmukkavariantti)**
- *Pseudokoodikuvio:* toista 3 kertaa: tulosta "Hello, NAME".
- *JS:*
  ```js
  let name = "Aino";
  for (let i = 0; i < 3; i++) {
    console.log("Hello, " + name);
  }
  ```
- *C#:*
  ```csharp
  string name = "Aino";
  for (int i = 0; i < 3; i++) {
      Console.WriteLine("Hello, " + name);
  }
  ```

**Ohjelma F — Oikean vastauksen tarkistaja (silmukka + if)**
- *Pseudokoodikuvio:* kysy enintään 3 kertaa; jos vastaus täsmää, lopeta; muuten sano "try again".
- *JS (laskurisilmukkaversio — pidä yksinkertaisena, ei prompt():*
  ```js
  let answers = ["red", "green", "blue"];
  let correct = "blue";
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === correct) {
      console.log("got it on try " + (i + 1));
      break;
    } else {
      console.log("try again");
    }
  }
  ```
- *C#:*
  ```csharp
  string[] answers = { "red", "green", "blue" };
  string correct = "blue";
  for (int i = 0; i < answers.Length; i++) {
      if (answers[i] == correct) {
          Console.WriteLine("got it on try " + (i + 1));
          break;
      } else {
          Console.WriteLine("try again");
      }
  }
  ```
  *(Ohjelma F on monimutkaisuuden ylärajalla — Rasmus käyttää sitä SYVENTÄVÄNÄ esimerkkinä, ei pakollisena esimerkkinä.)*

Rasmus käyttää ohjelmia A–E tiedostossa `self-study.md` ja kalvoilla; ohjelmia A–D aloitusesimerkkeinä PAKOLLISISSA tehtävissä; ohjelmia E ja F SYVENTÄVIEN tehtävien siemeninä. AT3-briiffaus-PAKOLLINEN tehtävä **ei** ole määräävä siitä, mikä ohjelma — se kertoo opiskelijalle, että käännä **omaa** viikon 6 pseudokoodiaan ja tarjoaa A–F:n varamalleina, jos pseudokoodi puuttuu tai on liian iso.

---

### Tiedosto 1 — `student/week-08/overview.md` (200–400 sanaa)

**Pakollinen H2-rakenne (järjestyksessä):**
1. `## Week 8 theme` — yksi lyhyt kappale: tämä on päätösviikko; AT3 laskeutuu tähän; kurssin keskeinen kysymys saa oikean vastauksen.
2. `## What you will be able to do by the end of the week` — luettelo 5–7 selkeällä englannilla kirjoitetusta "osaan tehdä" -lauseesta, jotka on yhdistetty O22–O24-tavoitteisiin mutta kirjoitettu opiskelijalle suunnatulla kielellä. Vähintään yksi kohta viittaa 2 minuutin esitykseen.
3. `## Must-do minimum vs. deepening` — kahden luettelon kontrasti. Käytä täsmälleen sanamuotoa **"must-do minimum"**.
4. `## How the three lessons fit together` — yksi lyhyt kappale: O22 silmukat → O23 rakennus → O24 testi, korjaus, esitys.
5. `## Choosing your language (reminder from Week 7)` — yksi lyhyt kappale: valitsit JS:n tai C#:n viikolla 7; pysyt siinä AT3:n osalta. Molemmat tehtävätiedostot ovat olemassa; käytät sitä, joka vastaa kieltäsi.

---

### Tiedosto 2 — `student/week-08/self-study.md` (2400–4000 sanaa)

**Pakollinen rakenne (järjestyksessä):**
- `# <Viikon otsikko>` — ehdotus: *"Closing the loop — your first real program"*. Rasmus voi parantaa.
- `## Introduction` — palauta keskeinen kysymys mieleen **sanatarkasti**. Kerro opiskelijalle, että AT3 (heidän ensimmäinen oikea ohjelmansa) laskeutuu tällä viikolla, että he valitsevat ohjelman omasta viikon 6 pseudokoodistaan ja että he esittävät sen 2 minuuttia O24:llä.
- `## Lesson 22 — Loops in code`
  - `### Why loops exist` — yhdistä viikon 5 *toista-kunnes*-kuvioon ja viikon 6 pseudokoodisilmukoihin.
  - `### The shape of a for loop` — JS ja C# **rinnakkain** kahden sarakkeen koodilohkossa tai pareittain aidatuissa lohkoissa. Käytä ohjelmaa D (yksinkertainen laskuri).
  - `### The shape of a while loop` — JS ja C# rinnakkain. Lyhyt esimerkki: tulosta "Hello", kun laskuri on alle 3.
  - `### Counter, condition, body, update` — nimeä for-silmukan neljä osaa molemmissa kielissä.
  - `### When a loop runs forever` — lempeä johdanto *ikuiseen silmukkaan*, miten sen huomaa (selaimen konsoli jumiutuu, .NET-ajuri katkaisee aikakatkaisulla), mitä muuttaa, jotta se pysähtyy.
  - 1 `> **Pause for a moment:**` -pohdintakehote.
- `## Lesson 23 — From pseudocode to a small program`
  - `### Pick one piece of your Week 6 pseudocode` — konkreettiset ohjeet: 6–20 riviä on optimi; isompi tarkoittaa, että lohkaisee vain yhden osan.
  - `### The translation table` — 6–10 rivin taulukko, joka kuvaa yleisiä viikon 6 pseudokoodikuvioita JS- ja C#-syntaksiin: *tulosta X*, *jos X niin Y muuten Z*, *toista N kertaa*, *aseta X arvoon Y*, *lue X*, *kasvata X yhdellä*, *tarkista, jos X on yhtä kuin Y*, jne.
  - `### Save, run, see output` — JS selaimen konsolissa; C# online-.NET-ajurissa. Nimeä **yksi** online-.NET-ajuri (dotnetfiddle.net on oletusehdotus — jos Rasmus suosii eri ilmaista, jolla ei ole pakollista rekisteröitymistä, se on hyväksyttävää).
  - `### When the screen is empty / silent` — mitä tarkistaa ensin: ajoitko oikeasti tiedoston? Onko tulostekutsussa kirjoitusvirhe?
  - 1–2 `> **Pause for a moment:**` -pohdintakehotetta.
- `## Lesson 24 — Test, fix one bug, present`
  - `### Testing by hand` — ohjelman ajaminen kahdesti kahdella eri arvolla. Näytä molemmat kielet.
  - `### Reading a real error message` — näytä yksi JS-virhe (esim. `Uncaught ReferenceError: scre is not defined`) ja yksi C#-virhe (esim. `CS0103: The name 'scre' does not exist in the current context`). Näytä kummallekin väärin kirjoitettu rivi ja korjaus.
  - `### One small fix, one re-run` — siinä kaikki, mitä "virheenkorjaus" tarkoittaa tässä. Eksplisiittisesti: ei debuggeria, ei keskeytyspisteitä, ei testauskehystä. Lue viesti, etsi rivi, korjaa kirjoitusvirhe, aja uudelleen.
  - `### Your 2-minute presentation` — 4-kohdan luonnos siitä, mitä sanoa: mitä ohjelma tekee, miten se toimii (silmukka + if?), mikä meni vikaan, miten se korjattiin. Mainitse aikaraja eksplisiittisesti: **2 minuuttia**.
  - 1 `> **Pause for a moment:**` -pohdintakehote.
- `## How AT3 is assessed` — tarkistuslistaversio kriteereistä 35–36. Hyväksytty / ei-vielä-hyväksytty.
- `## Summary — closing the loop on the central question` — toista keskeinen kysymys **sanatarkasti**. Yksi kappale yhdistäen takaisin viikkoon 1.

---

### Tiedosto 3 — `student/week-08/student-tasks-js.md` (800–1800 sanaa)

**Pakollinen rakenne:**
- `## Overview of the week's tasks` — 2–4 lausetta. Totea, että 🟢 PAKOLLISET tehtävät ovat **must-do minimum** ja että 🟣 SYVENTÄVÄT tehtävät ovat valinnaisia lisäosia. Mainitse, että AT3 palautetaan tällä viikolla.

**Neljä ehdokastehtävää, joista Rasmus poimii (hän pitää 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ):**

**Tehtävä 8.1-JS — 🟢 PAKOLLINEN — "AT3-briiffaus: käännä viikon 6 pseudokoodisi JavaScriptiin"**
- Opiskelija valitsee yhden palan viikon 6 pseudokoodistaan (6–20 riviä). Jos hän ei löydä yhtä tai se on liian iso, hän voi käyttää ohjelmaa A, B, C, D tai E varamallina — mutta hänen on mukautettava arvot omaan kontekstiinsa.
- Opiskelija kirjoittaa JavaScript-ohjelman selaimen konsoliin (tai `.js`-tiedostoon, joka liitetään palautukseen).
- Opiskelija ajaa ohjelman vähintään **kahdella eri syötteellä** (tai kahdella eri lähtömuuttujan arvolla) ja kaappaa tulosteen (konsolin kuvakaappaus).
- Opiskelija tarkoituksellisesti tai vahingossa syöttää yhden virheen, lukee virheilmoituksen, korjaa sen, ajaa uudelleen.
- Opiskelija kirjoittaa 3–5 lauseen reflektion, jossa nimeää bugin ja korjauksen.
- Opiskelija valmistelee **2 minuutin suullisen esityksen** O24:lle: mitä ohjelma tekee, miten se toimii (silmukka? if/else?), mikä meni vikaan, miten se korjattiin.
- `### If you are doing this alone` — jos O24:llä ei ole yleisöä, nauhoita 2 minuutin video itsestäsi esittäen ohjelmaa kameralle, tai julkaise ohjelma + 3 lauseen tiivistelmä luokan chatissa.
- `### Keep your notes` — tämä **on** AT3. Tallenna lähdekooditiedosto, kuvakaappaus ja reflektio. Tuo ne O24:lle.

**Tehtävä 8.2-JS — 🟢 PAKOLLINEN (vaihtoehto tai lisäksi) — "Silmukan lämmittely: laske 1:stä 5:een JS:llä"**
- Opiskelija kirjoittaa 4–6 rivin `for`-silmukan, joka tulostaa 1–5 konsoliin. Sitten muokkaa sen tulostamaan 5:stä 1:een (käänteinen). Sitten muokkaa sen vielä tulostamaan "Hello, NAME" kolme kertaa.
- Palautus: 3 lyhyttä pätkää yhteen tiedostoon.
- `### Keep your notes` — nämä kuviot esiintyvät AT3-ohjelmassasi.

**Tehtävä 8.3-JS — 🟣 SYVENTÄVÄ — "Yhdistä silmukka + if/else JS:ssä"**
- Opiskelija kirjoittaa pienen JS-ohjelman, joka käy läpi 5 salasanayritystä (taulukko, jossa on 5 merkkijonoa opiskelijan valitsemana) ja tulostaa jokaiselle joko "long enough" tai "too short".
- Reflektio: 3 lausetta siitä, mitä ohjelma tekee ja yksi asia, jonka lisäisi seuraavaksi.
- `### Keep your notes` — hyödyllinen AT3-ohjelman laajennuksena, jos aikaa on.

**Tehtävä 8.4-JS — 🟣 SYVENTÄVÄ — "Lue oikea virheilmoitus ja korjaa se (JS)"**
- Opiskelijalle annetaan 3 lyhyttä JS-pätkää, joista jokaisessa on täsmälleen yksi virhe (kirjoitusvirhe muuttujan nimessä, väärä vertailuoperaattori `=` `===:n` sijaan, puuttuva sulkeva aaltosulje). Jokaiselle: liitä konsoliin, lue virhe, nimeä rivi ja korjaus selkeällä englannilla, sitten sovella se.
- LLM-sparraus-vaihe (valinnainen): liitä virheilmoitus ja pätkä LLM:ään mukana toimitetulla kehotteella, jossa pyydetään LLM:ää selittämään viesti **kertomatta korjausta**, sitten hylkää LLM:n selitys, jos se antaa korjauksen joka tapauksessa. Esimerkkikehote aidatussa lohkossa.

**Tehtävä 8.5-JS — 🟣 SYVENTÄVÄ — "Vertaile C#-luokkakaveriin"**
- Etsi luokkakaveri, joka käytti C#:ia AT3:lle. Lukekaa toistenne ohjelmat. Kirjoita 3–5 lausetta selkeällä englannilla eroista (puolipisteet, `Console.WriteLine` vs `console.log`, `int` vs `let`, jne.) ja yhdestä asiasta, joka on sama (silmukkarakenne, if/else, tavoite).
- `### If you are doing this alone` — lue C#-versio yhdestä ohjelmista A–E `self-study.md`:stä ja kirjoita samat 3–5 lausetta.

**Oletusvalinta, jonka Rasmus toimittaa tiedostossa `student-tasks-js.md`:**
- 🟢 PAKOLLINEN: Tehtävä 8.1-JS (*AT3-briiffaus*) — **pakollinen**. Valinnaisesti myös Tehtävä 8.2-JS (*Silmukan lämmittely*) toisena PAKOLLISENA.
- 🟣 SYVENTÄVÄT: Tehtävät 8.3-JS, 8.4-JS ja 8.5-JS.

---

### Tiedosto 4 — `student/week-08/student-tasks-csharp.md` (800–1800 sanaa)

**Pakollinen rakenne:** peilaa tiedostoa `student-tasks-js.md` täsmälleen. Sama tehtävämäärä, sama tehtävän muoto, rinnakkainen AT3-briiffaus.

**Neljä ehdokastehtävää, joista Rasmus poimii:**

**Tehtävä 8.1-CS — 🟢 PAKOLLINEN — "AT3-briiffaus: käännä viikon 6 pseudokoodisi C#:iin"**
- Sama laajuus ja samat tuotokset kuin tehtävällä 8.1-JS. Opiskelija kirjoittaa C#-ohjelman online-.NET-ajurissa (dotnetfiddle.net tai vastaava), ottaa kuvakaappauksen ajosta, korjaa yhden bugin, valmistelee 2 minuutin suullisen esityksen.
- `### If you are doing this alone` — samat vaihtoehdot kuin 8.1-JS:ssä (nauhoitettu video, luokan chat -julkaisu).
- `### Keep your notes` — tämä **on** AT3.

**Tehtävä 8.2-CS — 🟢 PAKOLLINEN (vaihtoehto tai lisäksi) — "Silmukan lämmittely: laske 1:stä 5:een C#:lla"**
- Sama muoto kuin 8.2-JS, mutta C#:lla. Kolme lyhyttä pätkää yhteen tiedostoon.

**Tehtävä 8.3-CS — 🟣 SYVENTÄVÄ — "Yhdistä silmukka + if/else C#:ssa"**
- Sama muoto kuin 8.3-JS. C#-taulukko 5 merkkijonosta, silmukka, tulosta "long enough" / "too short".

**Tehtävä 8.4-CS — 🟣 SYVENTÄVÄ — "Lue oikea virheilmoitus ja korjaa se (C#)"**
- Sama muoto kuin 8.4-JS. Kolme lyhyttä C#-pätkää, joista jokaisessa on täsmälleen yksi virhe (kirjoitusvirhe muuttujan nimessä, `=` `==:n` sijaan, puuttuva sulkeva aaltosulje). Lue virhe, nimeä korjaus, sovella se. Valinnainen LLM-sparraus-vaihe samalla esimerkkikehotteella.

**Tehtävä 8.5-CS — 🟣 SYVENTÄVÄ — "Vertaile JS-luokkakaveriin"**
- Tehtävän 8.5-JS peilikuva. Etsi JS-luokkakaveri, lukekaa toistenne ohjelmat, kirjoita 3–5 lausetta eroista ja yhdestä asiasta, joka on sama.
- `### If you are doing this alone` — lue JS-versio yhdestä ohjelmista A–E `self-study.md`:ssä.

**Oletusvalinta, jonka Rasmus toimittaa tiedostossa `student-tasks-csharp.md`:**
- 🟢 PAKOLLINEN: Tehtävä 8.1-CS (*AT3-briiffaus*) — **pakollinen**. Valinnaisesti myös Tehtävä 8.2-CS (*Silmukan lämmittely*) toisena PAKOLLISENA.
- 🟣 SYVENTÄVÄT: Tehtävät 8.3-CS, 8.4-CS ja 8.5-CS.

**Pariteettitarkistus:** Rasmuksen on varmistettava, että PAKOLLISTEN tehtävien lukumäärä JS-tiedostossa vastaa C#-tiedostoa ja että SYVENTÄVIEN tehtävien lukumäärä vastaa. Jos 8.1-JS ja 8.2-JS ovat molemmat PAKOLLISIA, niin 8.1-CS ja 8.2-CS ovat molemmat PAKOLLISIA.

---

### Tiedosto 5 — `student/week-08/vocabulary.md` (10–18 termiä)

**Pakolliset termit (Rasmus voi lisätä 1–4 omaa):**
1. Loop
2. for (silmukan avainsana sekä JS:ssä että C#:ssa)
3. while (silmukan avainsana molemmissa)
4. Counter
5. Iteration
6. Body (silmukan)
7. Infinite loop
8. Error message
9. Bug
10. Fix
11. Test (palautettu mieleen viikolta 1)
12. Source code
13. Run (a program)
14. Presentation
15. **Algorithm** — merkitty **"kurssin loppukoonti — palautettu mieleen viikolta 1"**.

Valinnaiset lisäykset: *console* (palautettu mieleen viikolta 7), *console.log / Console.WriteLine* (palautettu mieleen), *condition* (palautettu mieleen viikolta 5).

Jokainen määritelmä on 1–3 lausetta, selkeällä englannilla, lyhyellä esimerkillä. Missä termillä on eri muodot JS:ssä ja C#:ssa, näytä molemmat (esim. *"merkkijonon pituus: `password.length` JS:ssä, `password.Length` C#:ssa"*).

---

### Tiedosto 6 — `student/week-08/slides.md` (~12–20 kalvoa)

**Suositeltu kalvorunko (Rasmus voi mukauttaa rakenteen hengessä):**

1. `# Week 8 — Closing the loop`
2. `## What lands this week` — luettelo: silmukat, AT3-rakennus, AT3-esitys.
3. `## Loops — the shape (JS and C# side by side)` — Ohjelma D molemmilla kielillä yhdellä kalvolla.
4. `## Counter, condition, body, update` — nimeä neljä osaa.
5. `## A while loop (JS and C# side by side)` — lyhyt esimerkki.
6. `## When a loop runs forever` — miltä ikuinen silmukka näyttää ja miten se pysäytetään.
7. `## From your pseudocode to your program` — yksi lause + 3 rivin käännöstaulukon pätkä.
8. `## The translation table` — 4–6 riviä: *tulosta*, *if/else*, *toista N kertaa*, *aseta X arvoon Y*.
9. `## Save, run, see output` — yksi kalvo per kielityökalu (selaimen konsoli / online-.NET-ajuri).
10. `## Reading a real error message (JS)` — yksi virhe ja yksi korjaus.
11. `## Reading a real error message (C#)` — yksi virhe ja yksi korjaus.
12. `## One small fix, one re-run` — sitä on virheenkorjaus tällä tasolla. (Eksplisiittisesti: ei debuggeria, ei keskeytyspisteitä.)
13. `## Your 2-minute presentation` — luettelo siitä, mitä sanoa.
14. `## Must-do minimum vs. deepening` — kahden sarakkeen kontrasti.
15. `## Tasks this week (see your language's task file)` — 1 rivi per tehtävä viitaten molempiin tiedostoihin.
16. `## How AT3 is assessed` — tarkistuslista.
17. `## Closing the loop — the central question, one more time` — keskeinen kysymys **sanatarkasti**.
18. `## Thank you and what comes next`

Tavoitelukumäärä 14–18 kalvoa. Käytä `---`-erotinta omalla rivillään jokaisen kalvon välissä.

---

### Tiedosto 7 — `teacher/week-08/teacher-materials.md` (2400–4400 sanaa)

**Pakolliset H2-osiot (järjestyksessä):**

1. `## Week 8 learning objectives (mapped to Bloom)` — toista O22–O24-tavoitteet, ryhmiteltyinä Bloom-vaiheittain. Soveltaminen vallitsevana; kevyt Arvioiminen O24:llä (vertaile omaa vertaisen ratkaisuun, selitä omin sanoin, korjaa yksi bugi).

2. `## Common misconceptions for Week 8` — vähintään 6 viikossa (≥2 per oppitunti). Ehdotettu joukko:
   - **O22**: *"A loop is a complicated thing only programmers understand."* → Correction: it is the formal name for the "repeat 3 times" pattern from Week 6 pseudocode. // *"You need `while`; `for` is more advanced."* → Correction: a `for` loop with a counter is usually simpler than a `while` loop for beginners.
   - **O23**: *"Pseudocode and code are completely different."* → Correction: most of the work is replacing English words with the language's syntax — the structure is already there. // *"If my program does not print anything, something is broken."* → Correction: more often, you simply did not run it, or there is a typo in the print line.
   - **O24**: *"Debugging needs a special tool."* → Correction: at this level, debugging is reading the console error and changing one line. // *"If the program runs, it is correct."* → Correction: running and being correct are not the same — test with at least two different values.

3. `## Lesson 22 — 90-minute plan` — **Slide cues** -aliotsikko lopussa. Aikalohkot yhteensä 90, itsenäisen työn lohko 27–45 min. Ehdotettu runko:
   - 0–10 min: lämmittely — näytä kaksi viikon 6 pseudokoodin "toista 3 kertaa" -riviä ja pyydä opiskelijoita ennustamaan, miltä silmukka näyttää.
   - 10–25 min: opettajan luento — Ohjelma D molemmilla kielillä, nimeä neljä osaa.
   - 25–55 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat tekevät tehtävän 8.2 valitsemallaan kielellä (laske 1–5; käänteinen; tervehdi nimellä).
   - 55–75 min: **PAKOLLINEN tuntiaktiviteetti** — "Show-and-tell loops" (ks. in-class-tasks.md): kukin pari ajaa silmukkansa live luokalle.
   - 75–85 min: koko luokan loppukeskustelu — mikä oli helppoa, mikä näytti oudolta.
   - 85–90 min: päätösreflektio + O23:n ennakko.
   - **Slide cues:** kalvot 1–6.

4. `## Lesson 23 — 90-minute plan` — **Slide cues**. Ehdotus:
   - 0–10 min: lämmittely — jokainen opiskelija nimeää viikon 6 pseudokoodin, jonka aikoo kääntää.
   - 10–25 min: opettajan luento — käännöstaulukko; näytä yksi täysi käännös (Ohjelma A tai B).
   - 25–65 min: **ITSENÄINEN TYÖ** (40 min) — opiskelijat kääntävät pseudokoodinsa valitsemallaan kielellä. Opettaja kiertää.
   - 65–80 min: paritarkistus — näytä parillesi ohjelmasi ja tuloste.
   - 80–88 min: koko luokan loppukeskustelu — tyypilliset kipupisteet.
   - 88–90 min: O24:n ennakko (esitys huomenna).
   - **Slide cues:** kalvot 7–9.

5. `## Lesson 24 — 90-minute plan` — **Slide cues**. **Sisältää 2 minuutin opiskelijan esitysosuuden.** Ehdotus:
   - 0–10 min: lämmittely — näytä yksi JS-virhe ja yksi C#-virhe taululla; luokka selittää.
   - 10–25 min: opettajan luento — virheilmoituksen lukeminen, yhden pienen korjauksen soveltaminen, 2 minuutin esityksen runko.
   - 25–55 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat testaavat ohjelmaansa kahdella eri arvolla, laukaisevat tarkoituksella tai vahingossa yhden virheen, korjaavat sen, valmistautuvat 2 minuutin esitykseen. Opettaja kiertää ja vahvistaa valmiuden.
   - 55–85 min: **AT3-esitykset** — kukin opiskelija pitää **2 minuutin** esityksen. 12 hengen luokassa 30 min riittää kaikille; isommassa luokassa jaa kahteen yhtäaikaiseen ~6 hengen ryhmään apuopettajan kanssa tai kierrätä kahden istunnon yli. (Rasmus huomauttaa suuremman luokan mukautuksesta.)
   - 85–90 min: kurssin sulkeminen — lue keskeinen kysymys uudelleen; kiitä luokkaa.
   - **Slide cues:** kalvot 10–18.

6. `## Facilitation tips` — käytännön vinkkejä: miten pitää 2 minuutin esitykset aikataulussa (käytä kaikille näkyvää puhelimen ajastinta), miten käsitellä opiskelijaa, jonka ohjelma ei koskaan toiminut (kohdista esitys bugiin, jota hän ei pystynyt korjaamaan ja siihen, mitä hän kokeili), miten käsitellä kaksikielistä luokkahuonetta (ryhmitä JS- ja C#-opiskelijat vierekkäisiin pöytiin paritarkistuksen helpottamiseksi), miten käsitellä online-.NET-ajurin hitautta (varaa varalinkki, salli kuvakaappauksen myöhäinen palautus).

7. `## Answers to common student questions` — vähintään 5. Ehdotus: *Voinko käyttää `console.log`:ia vahingossa C#-ohjelmassani? / Miksi C#-ohjelmani sanoo "CS0103"? / Mitä jos viikon 6 pseudokoodini on liian iso? / Pitääkö minun pitää esitys, jos olen ujo? / Voinko käyttää ChatGPT:tä ohjelman kirjoittamiseen?*

8. `## Formative assessment tips` — 3–5 nopeaa tarkistusta (poistumislippu: nimeä `for`-silmukan neljä osaa; parin raportointi: mikä oli se yksi bugi?; yhden minuutin paperi O24:n jälkeen: vastasiko kurssi keskeiseen kysymykseensä sinun osaltasi?).

Ristiviitta `in-class-tasks.md`:ään O22:lta (show-and-tell loops) ja valinnaisesti O23:lta (paritarkistus).

---

### Tiedosto 8 — `teacher/week-08/in-class-tasks.md` (400–1200 sanaa)

**Pakollinen rakenne:**
- `## Overview` — 2–3 lausetta, joissa nimetään aktiviteetit ja se, mihin viikolla ne sopivat.
- Vähintään 1 H2-tehtävä merkitty **MANDATORY**.

**Kaksi konkreettista aktiviteetti-ideaa, jotka Rasmus toimittaa (oletus: molemmat):**

**Aktiviteetti A — PAKOLLINEN — "Show-and-tell loops"** *(pari / koko luokka, ~20 min, sijoitettu O22:lle välille 55–75 min)*
- Kukin pari (tai sooloopiskelija) on juuri kirjoittanut silmukkapätkänsä (Tehtävä 8.2 heidän kielellään).
- Yksi kerrallaan kukin pari kävelee eteen (tai heijastaa paikaltaan), ajaa silmukkansa **live** luokan edessä ja lukee tulosteen ääneen.
- Luokka nimeää silmukan neljä osaa (laskuri, ehto, runko, päivitys) vähintään yhdelle näytetyistä silmukoista.
- Sekoittakaa JS- ja C#-silmukat — pointti on, että *muoto* on sama molemmissa kielissä.
- **Miksi se vaatii luokkahuoneen:** live-ajo + julkinen nimeäminen on koko juju. Ei voi tehdä kotitehtävänä.
- Ristiviite: `teacher-materials.md` O22-aikalohko 55–75 min.

**Aktiviteetti B — PAKOLLINEN — "AT3-esitykset"** *(koko luokka, ~30 min, sijoitettu O24:lle välille 55–85 min)*
- Kukin opiskelija pitää **2 minuutin** esityksen AT3-ohjelmastaan (käsitelty yksityiskohtaisesti tiedostossa `teacher-materials.md` O24:llä). Tämä on virallinen AT3:n suullinen osuus.
- Opettaja käyttää näkyvää puhelimen ajastinta.
- Lyhyt vertaispalautekysymys kunkin jälkeen: *"Nimeä yksi asia, jonka huomasit."*
- Ristiviite: `teacher-materials.md` O24-aikalohko 55–85 min.

Valinnainen Aktiviteetti C — VALINNAINEN — "Käännöskilpailu" *(pari, ~15 min, voi sijoittaa O23:lle välille 65–80 min)* — yksi pari kääntää saman viikon 6 pseudokoodin JS:ksi, toinen C#:ksi. 10 minuutin jälkeen verratkaa rivi riviltä. Hyödyllinen luokille, jotka valmistuvat aikaisin.

---

### Valinnainen täydentävä kalvopaketti — `student/week-08/slides-l24-presentation-rubric.md` (4–8 kalvoa)

Rasmus voi sisällyttää tämän lyhyen paketin, jonka opettaja heijastaa O24:llä esitysten välillä muistuttamaan 2 minuutin rakenteesta.

Ehdotettu runko:
1. `# 2-minute presentation rubric` (otsikkokalvo)
2. `## What to say (4 beats)` — mitä ohjelma tekee / miten se toimii / mikä meni vikaan / miten se korjattiin.
3. `## Timing — 2 minutes` — noin 30 sekuntia per kohta.
4. `## Pass criteria` — tarkistuslista opettajalle: ohjelma pyörii (tai yritys dokumentoitu) / opiskelija nimeää, mitä se tekee / yksi bugi-ja-korjaus kuvattu / 2 minuuttia pidetty.
5. `## What is *not* required` — täydellinen koodi, hienot kalvot, ulkoa opeteltu käsikirjoitus.
6. `## After each presentation` — yksi lyhyt vertaisnoteeraus: "nimeä yksi asia, jonka huomasit".

Tämä paketti on **valinnainen**. Jos Rasmus sisällyttää sen, Wilhelm tarkistaa 4–8 kalvon lukumäärän ja ajastinmuistutuksen läsnäolon.

---

## Avoimet kysymykset

1. **Online-C#-ajurin valinta.** Tämä suunnitelma ehdottaa **dotnetfiddle.net**:iä oletuksena, ilman pakollista rekisteröitymistä. Jos koulussa on suosittu ympäristö (esim. itse hostattu ajuri), Rasmus voi korvata sen. **Oletusoletus:** dotnetfiddle.net, nimeää sen `self-study.md`:n O23-osiossa.

2. **Pidetäänkö molemmat PAKOLLISET tehtävät vai vain AT3-briiffaus.** Kova sääntö sanoo 1–2 PAKOLLISTA per kielitiedosto, ja AT3-briiffaus on yksi niistä. Rasmus voi sisällyttää myös Silmukan lämmittelyn (Tehtävä 8.2) toisena PAKOLLISENA opiskelijoille, jotka saapuvat ilman valmista viikon 6 pseudokoodia. **Oletusoletus:** Rasmus toimittaa **molemmat** PAKOLLISINA (8.1 + 8.2 kummassakin kielitiedostossa) antaen opiskelijoille lyhyemmän lämmittelyn ennen isompaa AT3-tehtävää. Wilhelm hyväksyy 1 tai 2 PAKOLLISTA tehtävää tiedostoa kohden, kunhan AT3-briiffaus on yksi niistä.

3. **AT3:n suullisen esityksen pituus.** Toimeksianto lukitsee **2 minuuttia**. **Oletusoletus:** Rasmus kirjoittaa "2 minutes" täsmälleen (ei "1–3 minutes" tai "around 2 minutes"). Wilhelm grep-hakee merkkijonon.

4. **Luokkakoko ja O24:n esitysslotti.** 12 hengen luokka sopii 30 minuuttiin; isompi luokka tarvitsee mukautusta. **Oletusoletus:** Rasmus kirjoittaa 90 minuutin O24-suunnitelman ~12 hengen luokalle, plus yksi lause *Facilitation tips* -osiossa siitä, miten skaalata (jaa kahteen yhtäaikaiseen ryhmään; tai jatka toiseen istuntoon).

5. **Sijaitseeko AT3-briiffaus molemmissa tehtävätiedostoissa vai myös `self-study.md`:ssä.** Kova sääntö sijoittaa sen sekä `student-tasks-js.md`:hen että `student-tasks-csharp.md`:hen PAKOLLISENA tehtävänä. `self-study.md` sisältää myös `## How AT3 is assessed`. **Oletusoletus:** toiminnallinen briiffaus on kahdessa tehtävätiedostossa; `self-study.md` vain tiivistää arviointikriteerit.

6. **Mainitaanko ikuiset silmukat lainkaan.** Ne ovat yleinen bugilähde. **Oletusoletus:** Rasmus mainitsee ikuiset silmukat O22:n itseopiskelussa (yksi lyhyt aliosio, ei pelottavaa jargonia) ja yhdellä kalvolla. Ei tehtävissä.

7. **C#:n taulukkosyntaksi SYVENTÄVÄSSÄ tehtävässä 8.3-CS / Ohjelma F.** Taulukot ovat teknisesti uusi ominaisuus viikon 7 esitellyn lisäksi. **Oletusoletus:** Rasmus käyttää taulukoita vain SYVENTÄVISSÄ tehtävissä, ei koskaan PAKOLLISISSA tehtävissä, ja selittää taulukon literaalin yhdellä rivillä siellä, missä se ensimmäisen kerran esiintyy.

8. **Kalvojen lukumäärä.** Tämä suunnitelma suosittelee 14–18 kalvoa; kanoninen toimeksianto sanoo ~10–20. **Oletusoletus:** Rasmus tavoittelee 14–18; Wilhelm hyväksyy missä tahansa välillä 12–20.

9. **Täydentävä kalvopaketti `slides-l24-presentation-rubric.md`.** **Oletusoletus:** Rasmus **sisällyttää** sen (4–6 kalvoa) — viikko 8 on ainoa viikko, jossa on arvosteltu suullinen, joten rubriikkikalvopaketti on aidosti hyödyllinen.

10. **Ammatillinen kulma.** Toimeksianto luettelee kuusi esimerkkiohjelmaa (A–F). **Oletusoletus:** Rasmus käyttää ohjelmia A–E `self-study.md`:ssä ja aloitusesimerkkeinä; Ohjelma F esiintyy vain SYVENTÄVISSÄ tehtävissä, koska se yhdistää silmukan + if:n + taulukon indeksoinnin.

11. **Sallitaanko `prompt()` / `Console.ReadLine()` PAKOLLISISSA tehtävissä.** Nämä lisäävät monimutkaisuutta (käyttäjän syöte), mutta tekevät ohjelmista oikealta tuntuvia. **Oletusoletus:** sallittu vain SYVENTÄVISSÄ tehtävissä; PAKOLLISET tehtävät käyttävät kovakoodattuja muuttuja-arvoja kynnyksen pitämiseksi alhaalla. Rasmus mainitsee tämän eksplisiittisesti AT3-briiffauksessa.

12. **Näyttääkö `slides.md` molemmat kielet jokaisella koodikalvolla.** **Oletusoletus:** jokaisella kalvolla, joka näyttää koodia, näytetään JS ja C# **rinnakkain** (paritetut aidatut lohkot tai kahden sarakkeen taulukko). Tämä on pariteettisääntö kriteeristä #23.
