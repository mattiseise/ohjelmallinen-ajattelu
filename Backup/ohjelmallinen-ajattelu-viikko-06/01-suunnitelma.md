# Ohjelmallinen ajattelu — viikon 6 suunnitelma (Sune, portti #1)

Kurssi: Ohjelmallinen ajattelu (englanninkielinen)
Kohderyhmä: Ammatillisen toisen asteen ICT-opiskelijat, ensimmäinen vuosi, ~15–17 v., ei aiempaa ohjelmointikieltä
Kesto: 8 viikkoa × 3 oppituntia/viikko × 90 min = 24 oppituntia
Tämän ajon putkilaajuus: Sune tuottaa tämän viikon 6 suunnitelman; Rasmus rakentaa täyden viikon 6 paketin kanonisessa viikkorakenteessa; Linnea/Wilhelm auditoivat viikon 6; Alfred paketoi pelkkänä Markdownina tehdyn viikon 6 julkaisun (ei PDF:ää, ei PPTX-renderöintiä tällä kierroksella).

24 oppitunnin aihetaulukko, Bloom-kartoitus ja AT-sijoittelu peritään sanatarkasti lukitusta kurssisuunnitelmasta osoitteessa `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md`. Tämä tiedosto määrittelee vain viikon 6.

---

## Suunnitelma

### Viikon 6 teemalauseke

Viikko 6 on **kurssin ohjelmallisen ajattelun puoliskon synteesiviikko**. Kaikki, mitä opiskelija on harjoitellut arkikielellä — selkeää sekvenssiä (viikot 1–2), abstraktiota ja prosessikuvausta (viikot 3–4), ehtoja ja toistoa (viikko 5) — yhdistyy yhdeksi täsmällisemmäksi notaatioksi: **pseudokoodiksi**. Viikon ydinviesti on, että pseudokoodi on silta arkikielen ja oikean koodin välillä: tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida. Mitään oikeaa ohjelmointikieltä ei esiinny tällä viikolla. Viikko 6 päättyy harjoittelemalla aloittelevien ohjelmoijien kaikkein vähiten harjoiteltua taitoa: **koodin lukemista paperilla ja sen ennustamista, mitä se tekee**, rivi riviltä, jäljityskaaviolla. **AT2 palautetaan oppitunnin 18 tienoilla**, ja se rakentuu suoraan oppituntien 16–18 pseudokoodi- ja käsiajotyölle. Oikea koodi (JavaScript) saapuu viikolla 7.

### Viikon 6 ydinviesti (yksi lause)

Pseudokoodi on silta arkikielen ja oikean koodin välillä: tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida.

### O16–O18 jaottelu viikolle 6

#### Oppitunti 16 — Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Määrittele** pseudokoodi omin sanoin ja **vertaa** sitä arkikieleen ja oikeaan ohjelmointikieleen. *(Ymmärtäminen)*
  - (b) **Tunnista** kolme rakennuspalikkaa, jotka kohdattiin aiemmilla viikoilla — sekvenssi, ehto, toisto — lyhyestä pseudokoodista. *(Ymmärtäminen)*
  - (c) **Kirjoita** lyhyt pseudokoodi (10–20 riviä) tutusta prosessista käyttäen pientä kiinteää avainsanajoukkoa (`SET`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`, `READ`, `WRITE`). *(Soveltaminen)*
  - (d) **Selitä**, miksi pseudokoodi on luotettavampaa jaettavaa kuin englanninkielinen proosa, kun on kyse ohjeesta, jota tietokone lopulta suorittaa. *(Ymmärtäminen)*
- **Avainsanaston ennakkokatsaus:** pseudocode, keyword, indentation (epämuodollinen), block, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`; esikatsele termi *variable*.
- **Ydinviesti:** Pseudokoodi ei ole uusi kieli ulkoa opettelua varten — se on ne asiat, joita kirjoitat jo nyt, muutamilla yhteisillä sanoilla ja kiinteällä muodolla, jotta tuntematon voi lukea sen samalla tavalla kuin sinä.

#### Oppitunti 17 — Syöte, käsittely, tuloste ja muuttujan idea

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Kuvaa** pseudokoodin syöte → käsittely → tuloste -malli. *(Ymmärtäminen)*
  - (b) **Määrittele** *muuttuja* omin sanoin: nimetty säilö yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen aikana. *(Ymmärtäminen)*
  - (c) **Käytä** `SET variableName TO value`-, `READ variableName`- ja `WRITE variableName`-rakenteita oikein pseudokoodissa. *(Soveltaminen)*
  - (d) **Tunnista**, että muuttujan *nimen* tulisi kuvata, mitä se pitää sisällään, ja että huonot nimet tekevät pseudokoodista vaikeaa luettavaa. *(Ymmärtäminen)*
- **Avainsanaston ennakkokatsaus:** variable, value, name (muuttujan), assignment, input, processing, output; kerrataan *sequence*, *condition*, *repetition* viikolta 5.
- **Ydinviesti:** Pseudokoodiohjelma on lähes aina pieni kone, joka ottaa syötettä, tekee sille jotain ja tuottaa tulostetta — ja muuttuja on paikka, jossa se pitää asioita, jotka sen täytyy muistaa suoritusaikana.

#### Oppitunti 18 — Pseudokoodin testaaminen: käsiajo ja virheiden etsiminen (AT2 palautetaan tämän oppitunnin tienoilla)

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Selitä**, mikä jäljityskaavio on ja miksi käsiajo paperilla löytää bugeja, joita uudelleenlukeminen ei. *(Ymmärtäminen)*
  - (b) **Käsiaja** lyhyt pseudokoodi rivi riviltä jäljityskaavion avulla, päivittäen jokaisen muuttujan arvon jokaisella askeleella. *(Soveltaminen)*
  - (c) **Löydä** vähintään yksi bugi tarkoituksellisesti rikotusta pseudokoodista käsiajamalla se. *(Soveltaminen)*
  - (d) **Korjaa** bugi ja käsiaja korjattu pseudokoodi vahvistaaksesi odotetun tulosteen. *(Soveltaminen)*
- **Avainsanaston ennakkokatsaus:** dry run, trace table, bug, off-by-one (epämuodollinen), expected output, actual output; esikatsele termi *console* viikkoa 7 varten.
- **Ydinviesti:** Pseudokoodi ei ole valmis, kun se näyttää oikealta; se on valmis, kun jäljityskaavio todistaa, että se tuottaa odotetun tulosteen, mukaan lukien vähintään yhdellä hankalalla syötteellä.

### Viikko 6 — must-do-minimi vs. syventävä

**Must-do-minimi (jokaisen opiskelijan on viikon 6 päätteeksi osattava):**
- Määritellä pseudokoodi, muuttuja, käsiajo, jäljityskaavio, bugi arkikielellä.
- Lukea lyhyt pseudokoodipätkä (noin 10–15 riviä, vähintään yksi ehto ja yksi toisto) ja kertoa, mitä se tekee.
- Kirjoittaa pseudokoodi (10–20 riviä) tutusta prosessista käyttäen `SET`-, `IF/ELSE/ENDIF`- ja joko `WHILE/ENDWHILE`- tai `FOR/ENDFOR`-rakennetta vähintään kerran kutakin.
- Käsiajaa pseudokoodi jäljityskaaviolla, päivittäen jokaisen muuttujan rivi riviltä.
- Löytää bugi annetusta pseudokoodista käsiajamalla se, ja korjata bugi.

**Syventävä (valinnainen laajennus, mutta suositeltava, koska AT2 osuu tälle viikolle):**
- Ota luokkakaverin (tai oman vanhemman) kirjoittama pseudokoodi ja jäljitä se kysymättä ensin, mitä se tekee, ja vertaa sitten.
- Kirjoita pseudokoodi pienestä ammatillisesta skenaariosta: help-deskin vastauksen priorisointi, salasanan vahvuuden tarkistus, päivittäinen varmuuskopiointirutiini. Jäljitä yhdellä normaalilla ja yhdellä hankalalla syötteellä.
- Tunnista käsiajamalla löytämäsi bugin **tyyppi** — off-by-one, väärä vertailu, puuttuva alustus, väärä haara — arkikielellä.
- Lisää annettuun pseudokoodiin yksi *rajatapaus* (tyhjä syöte, negatiivinen luku, nolla) ja jäljitä mitä tapahtuu.

### Miten O16, O17 ja O18 sopivat yhteen

Kolme oppituntia on järjestetty tarkoituksella yhdeksi kaareksi. O16 esittelee pseudokoodin notaationa, joka kokoaa yhteen kaiken, mitä viikoilla 1–5 jo harjoiteltiin. O17 tarkentaa kameraa hyödyllisimpään uuteen ideaan tämän notaation sisällä — muuttujaan, ja syöte/käsittely/tuloste-runkoon, jota useimmat pseudokoodit noudattavat. O18 zoomaa taas ulos ja harjoittelee taitoa, joka tekee pseudokoodista todella hyödyllistä: käsiajamista paperilla bugien löytämiseksi ja korjaamiseksi. **AT2 palautetaan O18:n tienoilla**, ja se pyytää opiskelijaa kirjoittamaan lyhyen pseudokoodin pienestä ammatillisesta tehtävästä, käsiajamaan sen ja selittämään arkikielellä, mitä kukin osa tekee ja missä mahdolliset bugit löytyivät.

### Eteenpäin katsova huomio viikolle 7

Viikko 7 on ensimmäinen viikko oikealla koodilla. O16:n avainsanat (`SET`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`, `READ`, `WRITE`) kartoittuvat puhtaasti JavaScriptin primitiiveihin (`let x = ...`, `if/else`, `while`, `for`, prompt/console.log) viikolla 7. Rasmuksen tulee valita sellaiset pseudokoodin avainsanat, jotka *tekevät tästä hypystä helpon* nimeämättä JavaScriptiä koskaan viikolla 6.

---

## Rajaukset

**Viikon 6 ulkopuolelle jäävät:**
- **Ehdottomasti ei JavaScriptiä, ei Pythonia, ei C#:aa, ei Javaa, ei mitään oikeaa ohjelmointikieltä missään.** Vain pseudokoodia. Tämä on viikon kovin kova sääntö. Wilhelm hakee greppaamalla `console.log`, `let `, `function `, `def `, `var `, `print(`, `js`, `javascript` ja kaataa auditin osumalla.
- **Ei automaattisia testaus- tai debuggauskehyksiä** (jest, mocha, vitest, pytest jne.). "Testaaminen" tarkoittaa viikolla 6 **käsiajoa paperilla jäljityskaavion avulla**, piste.
- **Ei vuokaavioita uutena aiheena.** Vuokaaviot olivat viikolla 3. Ne saavat näkyä yhden rivin viittauksena viikkoon 3, jos Rasmus haluaa, mutta uutta vuokaavionotaatiota ei opeteta tällä viikolla.
- **Ei olio-ohjelmointiajattelua, ei funktioita parametreineen muodollisena aiheena, ei tietorakenteita yhden muuttujan ulkopuolella, jossa on luku, merkkijono tai kyllä/ei.** Listat/taulukot saavat näkyä korkeintaan kerran, ohimennen, `FOR each x in list` -esimerkissä — mutta ne eivät ole oppimistavoite.
- **Ei big-O:ta, ei Turingin koneita, ei kääntäjä-/tulkkiteoriaa.**
- **Ei IDE-asennusta, ei Node.js-asennusta, ei selainkonsolia.** Viikko 6 tarvitsee paperia ja kynän.
- **Ei arvosteltavia esseitä.** AT2 on tuotos + lyhyt reflektio; tuotos on pseudokoodi plus jäljityskaavio.
- **Ei suoraa PowerPoint-luontia.** Rasmus kirjoittaa `slides.md` (vain Markdown). Ei PDF:ää, ei PPTX:ää tällä kierroksella — Alfred paketoi vain Markdownia.
- **Ei kalvotiedostoja `slides.md`-tiedoston ja korkeintaan yhden valinnaisen `slides-l<n>-*.md`-tiedoston ulkopuolella per oppitunti**, jos sellainen on aidosti tarpeen. Oletus viikolle 6: **yksi valinnainen täydentävä kalvosarja O16:lle** (työstetty pseudokoodin läpikäynti) on vahvasti suositeltava; O17 ja O18 eivät tarvitse täydentäviä kalvoja.
- **Ei `media/`-kansiota**, ellei jokin kalvo nimenomaisesti viittaa kuvaan. Viikko 6 ei pitäisi tarvita kuvia; ASCII tai Markdown-taulukot riittävät jäljityskaavioille.
- **Ei sisäisen "AI-resilient"-leiman käyttöä** missään seitsemässä opiskelijalle näkyvässä tiedostossa. Rasmus suunnittelee tehtävät AI-resilienteiksi rakenteellisesti; Linnea auditoi ominaisuuden, ei leimaa.

**Kieli ja putki:**
- Englanti läpi koko viikon. Börje (suomenkielinen kielenhuolto) ohitetaan tällä ajolla.
- *Tämän suunnitelmatiedoston* H2-otsikot saavat pysyä suomeksi (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`), koska ne kuuluvat Sune-pohjaan; **kaikkien Rasmuksen seitsemän viikon 6 tiedoston on oltava täysin englanninkielisiä**, mukaan lukien niiden osio-otsikot.

---

## Hyväksymiskriteerit

Wilhelm tarkistaa viikon 6 paketin seuraavia konkreettisia, tarkistettavia kriteereitä vasten.

### Rakenteelliset — tiedostot ja kansiot

1. **Kaikki 7 kanonista tiedostoa läsnä** täsmälleen näillä tiedostonimillä (kirjainkoosta riippuva, pienaakkoset, kebab-case):
   - `student/week-06/overview.md`
   - `student/week-06/self-study.md`
   - `student/week-06/student-tasks.md`
   - `student/week-06/vocabulary.md`
   - `student/week-06/slides.md`
   - `teacher/week-06/teacher-materials.md`
   - `teacher/week-06/in-class-tasks.md`
2. **Täydentävä kalvosarja sallittu:** yksi valinnainen `student/week-06/slides-l16-pseudocode-walkthrough.md` (4–8 kalvoa). Muita täydentäviä kalvosarjoja ei odoteta. Jos Rasmus toimittaa O17- tai O18-täydentävän kalvosarjan, Wilhelm hyväksyy sen kunhan se on 4–8 lyhyttä kalvoa ja siihen viitataan tiedostosta `teacher-materials.md`.
3. **Ei ylimääräisiä tiedostoja** kansioissa `student/week-06/` tai `teacher/week-06/`. Ei `.pptx`-, ei `.key`-, ei Reveal.js-HTML-, ei PDF-tiedostoja. Kova hylkäys jos löytyy. `media/`-alikansio sallitaan vain, jos jokin kalvo tai itseopiskelu nimenomaisesti viittaa siellä olevaan kuvaan.

### Määrä (järkevyystarkistuksen haarukat, ei kovia rajoja)

4. `overview.md`: **200–400 sanaa**. Yksi osio per alue kohdassa #11 alla.
5. `self-study.md`: **2400–4000 sanaa** (≈3× yhden kultaisen näytteen oppitunti; tämä tiedosto kattaa O16, O17, O18).
6. `student-tasks.md`: **900–2000 sanaa** yhteensä. **1–2 🟢 PAKOLLINEN + 2–3 🟣 SYVENTÄVÄ** -tehtävää (katso #14, #24).
7. `vocabulary.md`: **10–18 termiä**, jokainen 1–3 lauseen englanninkielisellä määritelmällä. Vähintään yksi termi merkittynä "katse eteenpäin viikkoon 7" (ehdotus: *console*).
8. `slides.md` (pääsarja): **~12–20 kalvoa**, erotettu omilla riveillään olevilla `---`-merkeillä, jokainen kalvo alkaa H1:llä (`#`) tai H2:lla (`##`) ja sisältää vähäisen tukisisällön (3–5 lyhyttä luettelopistettä tai 1–2 lyhyttä virkettä). Tähtää ~15–18.
9. `slides-l16-pseudocode-walkthrough.md` (täydentävä sarja, jos toimitetaan): **4–8 kalvoa**, jotka käyvät läpi yhden konkreettisen pseudokoodiesimerkin alusta loppuun.
10. `teacher-materials.md`: **2600–4400 sanaa**. Sisältää **3 × 90 minuutin oppituntisuunnitelmaa** (yksi per oppitunti), jokaisessa aikalohkot summautuen 90:een. Lisäksi vaaditut H2:t kohdassa #16.
11. `in-class-tasks.md`: **500–1400 sanaa**. Sisältää **vähintään 1 PAKOLLINEN opettajan vetämä tuntiharjoitus**, joka aidosti vaatii luokkahuonevuorovaikutusta.

### Vaaditut H2-osiot tiedostoittain

12. `overview.md`:n on sisällettävä (tässä järjestyksessä):
    - `## Week 6 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (sanat **must-do minimum** vaaditaan; "mandatory minimum" on väärin)
    - `## How the three lessons fit together`
13. `self-study.md`:n on sisällettävä:
    - `# <Viikon otsikko>` (ehdotus: *"From thinking to code — meet pseudocode"*; Rasmus voi parantaa).
    - `## Introduction` — toistaa kurssin keskeisen kysymyksen ja nimeää tämän viikon ydinviestin sanatarkasti.
    - `## Lesson 16 — Pseudocode: from natural language to a more precise format` (tai lähinen variantti).
    - `## Lesson 17 — Input, processing, output, and the idea of a variable`
    - `## Lesson 18 — Testing pseudocode: dry running and finding errors`
    - `## Summary and what comes next` (esikatselee viikkoa 7 — ensimmäistä JavaScriptiä — nimeämättä JavaScript-syntaksia yksityiskohtaisesti).
    - **Vähintään 4 `> **Pause for a moment:**` -reflektiokehotetta** kolmen oppitunnin yli (≥1 per oppitunti; tähtää 5–6).
14. `student-tasks.md`:n on sisällettävä:
    - `## Overview of the week's tasks` — nimeää, että **AT2 palautetaan O18:n tienoilla** ja että tämän viikon tehtävät syöttävät suoraan AT2:een.
    - Yksi H2 per tehtävä, etuliitteenä `🟢 MANDATORY —` tai `🟣 DEEPENING —`. Sanamuodon **on käytettävä "must-do minimum"**, ei "mandatory minimum".
    - Jokainen tehtävä päättyy `### Keep your notes` -lohkoon, joka muistuttaa opiskelijaa, että **AT2 osuu tämän viikon O18:n tienoille** (ei AT1).
    - Jokaiselle tehtävälle, joka olettaa parin / seuraajan / testaajan / luokkakaverin, **`### If you are doing this alone`** -alaosio, jossa on konkreettinen vaihtoehto (24 tunnin tauko, video itsestä, eri laite, luokan chat).
15. `vocabulary.md`:n on sisällettävä yksi H2 `## Week 6 vocabulary`, sitten jokainen termi H3:na tai lihavoituna termiä määritelmälistassa. Vähintään yksi termi merkittynä **"katse eteenpäin"** -esikatseluna (ehdotus: *console*, *expression* tai *return value* — mikä tahansa viikolla 7 käytettävä).
16. `slides.md`:n on:
    - Aloitettava otsikkokalvolla.
    - Sisällettävä vähintään yksi kalvo, jonka rungossa näkyy **kurssin keskeinen kysymys sanatarkasti**: *How do I speak to a computer so that it understands what I want it to do?*
    - Käytettävä `---` omalla rivillään kalvojen välillä.
    - Ei saa sisältää upotettuja `.pptx`-viittauksia eikä puhujamuistiinpanosyntaksia, joka olettaa tiettyä renderöijää.
    - Viittaa viikon 6 ydinviestiin ("Pseudocode is the bridge between everyday English and real code…") vähintään yhdellä kalvolla.
17. `teacher-materials.md`:n on sisällettävä (sanatarkka H2-sanamuoto):
    - `## Week 6 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 6` — **vähintään 6 yli koko viikon** (≥2 per oppitunti), jokainen "**Correction:**"-rivillä.
    - `## Lesson 16 — 90-minute plan`
    - `## Lesson 17 — 90-minute plan`
    - `## Lesson 18 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions` — vähintään 5 yli koko viikon.
    - `## Formative assessment tips`
    - Jokaisessa 90 min suunnitelmassa on **konkreettiset aikalohkot, jotka summautuvat 90:een**, varaa **30–50 % itsenäiselle opiskelijatyölle** (katso #19) ja sisältää **Slide cues** -lohkon, joka viittaa `slides.md`:n kalvonumeroihin (ja täydentävään kalvosarjaan, jos Rasmus toimittaa sellaisen).
18. `in-class-tasks.md`:n on sisällettävä:
    - `## Overview`
    - Vähintään 1 H2-tehtävä merkittynä **MANDATORY**, vaatien opettajan vetämää luokkahuonevuorovaikutusta.
    - PAKOLLISEEN aktiviteettiin on viitattava ristiin tiedostosta `teacher-materials.md`, jotta opettaja tietää tarkan 90 min lohkon.

### Pedagogiset säännöt

19. **30–50 %:n sääntö**: tiedostossa `teacher-materials.md`, jokaiselle kolmesta 90 minuutin oppituntisuunnitelmasta, aikalohkot, jotka on näkyvästi merkitty *itsenäiseksi opiskelijatyöksi*, summautuvat **27–45 minuuttiin** 90:stä. Wilhelm tarkistaa aikalohkot aritmeettisesti.
20. **Bloom-katto**: viikon 6 oppimistavoitteet käyttävät vain **Ymmärtäminen + Soveltaminen** -verbejä (define, describe, explain, identify, recognise, use, write, dry-run, find, fix). **Kielletyt verbit** viikon 6 tavoitteissa: *evaluate, judge, design, create, build, develop, abstract, decompose* (ne kuuluvat viikoille 4 ja 8). Kevyt Analysointi saa esiintyä vain SYVENTÄVISSÄ tehtävissä (tunnista bugin tyyppi), ei koskaan ensisijaisena tavoitteena.
21. **Kurssin keskeinen kysymys** — *How do I speak to a computer so that it understands what I want it to do?* — esiintyy sanatarkasti **vähintään yhdellä kalvolla** tiedostossa `slides.md`. (Itseopiskelu mainitsee sen, mutta sen ei tarvitse olla sanatarkka toisen kerran; sanatarkka kalvo on auditankkuri.)
22. **Viikon 6 ydinviesti** — *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."* — esiintyy sanatarkasti tai lähes sanatarkasti `self-study.md`:n johdannossa ja vähintään yhdellä kalvolla.
23. **Esimerkit-ensin-periaate**: tiedostossa `self-study.md`, jokainen käsitteellinen osio, joka käyttää molempia esimerkkityyppejä, sijoittaa **arkiesimerkin ennen IT-esimerkkiä**. Wilhelm tarkistaa pistokokein kolme oppituntiosiota. (Ammatillisen kulman esimerkit — help-deskin priorisointi, salasanan tarkistus, varmuuskopiointirutiini — lasketaan IT:ksi.)
24. **Ei oikeaa ohjelmointikieltä missään.** Wilhelm hakee greppaamalla `console.log`, `let `, `var `, `const `, `function `, `def `, `print(`, `system.out`, `int main`, `<script`, `.js`, `JavaScript`, `Python`, `Java`, `C#`. **Kova hylkäys mistä tahansa osumasta** missä tahansa viikon 6 seitsemästä tiedostosta (ja täydentävässä kalvosarjassa, jos toimitettu). Pseudokoodin avainsanat (`SET`, `IF`, `ELSE`, `ENDIF`, `WHILE`, `ENDWHILE`, `FOR`, `ENDFOR`, `READ`, `WRITE`) ovat tietysti sallittuja.
25. **Ei automaattisia testauskehyksiä mainittu missään** (jest, mocha, vitest, pytest, junit).
26. **"Must-do minimum" -sanamuoto**: ilmausta **must-do minimum** käytetään (ei "mandatory minimum", ei "core minimum") tiedostoissa `overview.md` ja `student-tasks.md`. Wilhelm greppaa.
27. **"AI-resilient"-leima** ei saa esiintyä missään seitsemästä opiskelijalle näkyvästä tiedostosta. Ominaisuus pakotetaan; sisäistä leimaa ei paljasteta.
28. **AT-kehys tehtävissä**: jokaisen tehtävän `### Keep your notes` -lohko nimeää **AT2 tämän viikon O18:n tienoilla** (ei AT1, ei AT3). Wilhelm greppaa.

### Tehtävät (AI-resilienssi rakenteellisesti)

29. `student-tasks.md` sisältää **1–2 🟢 PAKOLLINEN + 2–3 🟣 SYVENTÄVÄ** -tehtävää. **Vähintään yhden PAKOLLISEN tehtävän on oltava AI-resilientti rakenteellisesti** — eli sen on vaadittava opiskelijan omaa konkreettista kontekstia (oikea tuttu prosessi, jota hän todella tekee), havaittavaa tuotosta (oma pseudokoodi paperilla, oma jäljityskaavio, oma lista löydetyistä bugeista) tai LLM:n kritisointimekanismia.
30. **Yhden PAKOLLISEN tehtävän on oltava:** "Kirjoita pseudokoodi tutusta prosessista, jota teet itse, vähintään yhdellä ehdolla ja yhdellä toistolla, ja käsiaja se sitten paperilla jäljityskaavion avulla." Tämä on AT2-valmiuden selkäranka. Rasmus valitsee tarkan sanamuodon.
31. Jos SYVENTÄVÄ tehtävä käyttää LLM:ää harjoituskumppanina, sen on sisällettävä koodikehys, jossa on esimerkkikehote ja eksplisiittinen ohje olla hyväksymättä LLM:n tuotosta sellaisenaan. (Sama sääntö kuin viikolla 1.)
32. Jokainen tehtävä, joka olettaa parin / seuraajan / testaajan, sisältää **`### If you are doing this alone`** -alaosion.

### Tuntitehtävät

33. `in-class-tasks.md` sisältää **vähintään 1 PAKOLLINEN opettajan vetämä tuntiharjoitus**, joka aidosti vaatii luokkahuonevuorovaikutusta. Vahva oletus: **"käsiajo luokkana"** -harjoitus, jossa opettaja kirjoittaa lyhyen pseudokoodin taululle ja luokka toimii kollektiivisesti jäljityskaaviona (yksi opiskelija per muuttuja, huutavat päivitykset rivi riviltä).
34. PAKOLLISEEN aktiviteettiin viitataan ristiin tiedostosta `teacher-materials.md` tietyllä aikalohkolla.

### Kieli ja viimeistely

35. **Englanti läpi koko viikon.** Ei suomenkielisiä sanoja missään 7 (tai 8 täydentävän kalvosarjan kanssa) tiedostossa, paitsi selvästi välttämättömät erisnimet.
36. **Rekisteri**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md`, `slides.md` ja mahdollinen täydentävä kalvosarja CEFR-tasolla ~B1; `teacher-materials.md` ja `in-class-tasks.md` CEFR-tasolla ~B2.
37. **Validi Markdown**: jokainen koodikehys sulkeutuu, jokainen taulukko renderöityy, ei rikkinäisiä sisäisiä linkkejä, `---`-erottimet kalvotiedostoissa yksin omilla riveillään.

---

## Briefing Rasmukselle

### Läpileikkaavia muistutuksia (koskevat kaikkia 7 tiedostoa)

- **Arki ennen IT:tä, aina.** Kun esität jonkin uuden idean, johdata tutulla 15-vuotiaalle tutulla kohtauksella (pyykinpesu, puhelimen lataaminen, teen keittäminen, bussisovelluksen tarkistaminen, Discord-vastauksen lähettäminen) ja vasta sitten siirry ammatilliseen IT-esimerkkiin (help-deskin priorisointi, salasanan vahvuuden tarkistus, päivittäinen varmuuskopiointirutiini).
- **Ei oikeaa ohjelmointikieltä missään.** Vain pseudokoodia. Ei `console.log`-, ei `let`-, ei `function`-, ei `var`-, ei Pythonia, ei JavaScriptiä nimeltä. Edes lause "tämä on aivan kuin JavaScript" on kielletty — viikko 7 on viikon päässä ja ansaitsee vertailun itse.
- **Ei testauskehyksiä.** "Testaaminen" = käsiajoa paperilla jäljityskaavion avulla.
- **Käytä yhtä yhtenäistä pseudokoodimurretta kaikkien seitsemän tiedoston yli.** Suositeltu kiinteä avainsanajoukko: `SET name TO value` · `READ name` · `WRITE expression` · `IF condition THEN … ELSE … ENDIF` · `WHILE condition DO … ENDWHILE` · `FOR each x IN list DO … ENDFOR` (listat valinnaisia). Sisennä lohkojen rungot 2 välilyönnillä koodikehysten sisällä, jotka on merkitty ` ```text `:llä. **Älä** käytä ` ```js `:tä tai mitään kielitunnistetta, joka viittaa oikeaan kieleen.
- **AT-kehys.** Jokainen `### Keep your notes` -lohko nimeää **AT2 tämän viikon O18:n tienoilla**. Ei AT1, ei AT3.
- **"Must-do minimum"** (ei "mandatory minimum", ei "core minimum"). Käytä täsmälleen tätä ilmaisua tiedostoissa `overview.md` ja `student-tasks.md`.
- **"AI-resilient"-leima** ei esiinny opiskelijalle näkyvissä tiedostoissa; Linnea auditoi ominaisuuden.
- **Kurssin keskeinen kysymys** esiintyy sanatarkasti vähintään yhdellä kalvolla.
- **Viikon 6 ydinviesti** esiintyy sanatarkasti tai lähes sanatarkasti `self-study.md`:n johdannossa ja vähintään yhdellä kalvolla: *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."*

---

### Tiedosto 1 — `student/week-06/overview.md` (200–400 sanaa)

**Vaadittu H2-rakenne (järjestyksessä):**
1. `## Week 6 theme` — yksi lyhyt kappale, joka nimeää viikon ydinviestin ja kolme oppituntiaihetta (O16 pseudokoodi, O17 muuttuja + syöte/käsittely/tuloste, O18 käsiajo + jäljityskaavio). Nimeää myös, että **AT2 palautetaan O18:n tienoilla**.
2. `## What you will be able to do by the end of the week` — luettelo 6–8 selkokielisestä "osaa tehdä" -lauseesta O16–O18 tavoitteisiin kartoitettuna.
3. `## Must-do minimum vs. deepening` — kahden luettelon vastakkainasettelu. Ilmaus **must-do minimum** vaaditaan.
4. `## How the three lessons fit together` — yksi lyhyt kappale, joka näyttää kaaren O16 (notaatio) → O17 (muuttujat + S/K/T-runko) → O18 (käsiajo + bugin korjaus) → AT2.

**Esimerkkejä, joihin nojautua:** teen keittäminen `IF`:llä (sokeri vai ei) ja `WHILE`:llä (kunnes vedenkeitin naksahtaa); salasanan vahvuuden tarkistus; help-deskin priorisointi, joka haarautuu tiketin tyypin mukaan. Arki ensin.

**Pituustavoite:** 250–320 sanaa on makea piste.

---

### Tiedosto 2 — `student/week-06/self-study.md` (2400–4000 sanaa)

**Vaadittu rakenne (järjestyksessä):**

- `# <Viikon otsikko>` — ehdotus: *"From thinking to code — meet pseudocode"*. Rasmus voi parantaa.
- `## Introduction` — avautuu tutulla kohtauksella (pyykit: *"jos korissa on tummia, tee tummien pesu; muutoin tarkista valkoiset"*). Toistaa kurssin keskeisen kysymyksen. Esittää **viikon 6 ydinviestin sanatarkasti**. Kertoo opiskelijalle, että AT2 osuu tälle viikolle (O18:n tienoilla).
- `## Lesson 16 — Pseudocode: from natural language to a more precise format`
  - `### From English to pseudocode` — näytä yksi arkiprosessi englanniksi (4–5 lausetta). Sitten sama prosessi pseudokoodina (10–14 riviä). Rinnakkaiskommentit: mikä tuli täsmällisemmäksi, mikä lyheni, mikä pysyi samana.
  - `### The small set of keywords` — esittele `SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`. Yksi lyhyt pseudokoodikatkelma per avainsana, yhdellä englanninkielisellä rivillä vieressä. Pidä tämä osio visuaalisesti siistinä — opiskelijoiden pitäisi voida käyttää sitä referenssikortina.
  - `### Sequence, condition, repetition — meet again` — yksi lyhyt kappale, joka muistuttaa opiskelijaa siitä, että viikon 5 sekvenssi/ehto/toisto ovat täsmälleen ne kolme asiaa, jotka pseudokoodi koodaa.
  - `### Why pseudocode is more reliable to share than English prose` — käsitteellinen kääntöpiste. Lyhyt.
  - 1–2 `> **Pause for a moment:**` -reflektiokehotetta.
- `## Lesson 17 — Input, processing, output, and the idea of a variable`
  - `### Input → processing → output` — nimeä kolmiosainen runko. Näytä yksi lyhyt pseudokoodiesimerkki (esim. pyydä numero, laske sen tuplaus, kirjoita tulos).
  - `### What is a variable?` — lyhyt määritelmä: nimetty säilö yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen aikana. Arkimetafora ensin (etiketöity laatikko hyllyllä, post-it-lappu purkissa), sitten pseudokoodiesimerkki `SET`:llä.
  - `### A variable name should describe what it holds` — vertaa `SET x TO 7` `SET passwordLength TO 7`:ään. Miksi jälkimmäinen on helpompi lukea.
  - `### A vocational example` — salasanan vahvuuden tarkistus pseudokoodina (lue salasana, laske sen pituus, aseta `isStrong` arvoon YES jos pituus ≥ 8 JA se sisältää numeron, muutoin NO; kirjoita tulos). Käytä samaa esimerkkiä uudelleen tiedostossa `slides.md`.
  - 1–2 `> **Pause for a moment:**` -reflektiokehotetta.
- `## Lesson 18 — Testing pseudocode: dry running and finding errors`
  - `### What is a dry run?` — lyhyt määritelmä. Vertaa viikon 1 "sananmukaiseen robottiin": käsiajo on opiskelija itse näyttelemässä sananmukaista robottia omalle pseudokoodilleen, paperilla.
  - `### The trace table` — näytä työstetty esimerkki. Käytä Markdown-taulukkosyntaksia: sarakkeet = rivinumero, jokainen muuttuja, tuloste. Kävele 6–8-rivinen pseudokoodikatkelma läpi 5–7 rivin avulla. Korosta hetki, kun muuttuja muuttuu.
  - `### Finding a bug` — anna tarkoituksellisesti rikottu lyhyt pseudokoodi (ehdotus: off-by-one `WHILE`-ehdossa, tai `<`, jonka pitäisi olla `<=`). Jäljitä se; jäljitys näyttää, että todellinen tuloste eroaa odotetusta tulosteesta; tunnista rivi ja korjaa.
  - `### Edge cases on paper` — yksi kappale: tyhjä syöte, nolla, negatiivinen luku. Jäljitys löytää sen, minkä silmä ei.
  - `### About AT2` — lyhyt, rauhallinen kappale: AT2 palautetaan tämän oppitunnin tienoilla; se pyytää opiskelijaa kirjoittamaan lyhyen pseudokoodin pienestä ammatillisesta tehtävästä ja käsiajamaan sen jäljityskaaviolla. O16–O18:n työ ON AT2:n raaka-aine. Ei uusia työkaluja, ei uutta notaatiota.
  - 1 `> **Pause for a moment:**` -reflektiokehote.
- `## Summary and what comes next` — sulkee silmukan: pseudokoodi on silta oikeaan koodiin, joka saapuu viikolla 7. Esikatsele viikkoa 7 yhdellä lauseella ("Next week the same pseudocode shape becomes a tiny program in a real language you run in a browser"), nimeämättä JavaScript-syntaksia yksityiskohtaisesti.

**Esimerkkivalikko, josta Rasmus valitsee (arki ensin, sitten ammatillinen):**

- Arki: teen keittäminen (`IF` sokeri, `WHILE` vedenkeitin ei naksahtanut), hampaiden harjaaminen `FOR each hammasalue`, aamuherätyksen torkkusilmukka, lukematta jääneiden viestien tarkistaminen chatista.
- Ammatillinen: help-deskin tikettien priorisointi (`IF` tiketissä sana "salasana" THEN ohjaa tasolle 1, ELSE IF "katkos" THEN tasolle 2, ELSE tasolle 3); salasanan vahvuuden tarkistus; päivittäinen varmuuskopiointirutiini (`FOR each folder in backupList`); päällekkäisten tiedostojen tunnistus (`FOR each file`, laske nimittäin).

**Pituustavoite:** 2800–3400 sanaa.

---

### Tiedosto 3 — `student/week-06/student-tasks.md` (900–2000 sanaa)

**Vaadittu rakenne:**
- `## Overview of the week's tasks` — 3–5 lausetta. Totea, että 🟢 PAKOLLINEN -tehtävät ovat **must-do-minimi** ja 🟣 SYVENTÄVÄ -tehtävät ovat valinnaisia laajennuksia. **Nimeä, että AT2 palautetaan tämän viikon O18:n tienoilla** ja että alla olevat tehtävät syöttävät suoraan AT2:een.

**Viisi ehdokastehtävää, joista Rasmus valitsee (Rasmus pitää 1–2 PAKOLLINEN + 2–3 SYVENTÄVÄ). Oletusvalinta lopussa.**

**Tehtävä 6.1 — 🟢 PAKOLLINEN — "Pseudokoodaa tuttu prosessi"** *(AI-resilientti rakenteellisesti)*
- Opiskelija valitsee yhden prosessin, jota hän tekee itse lähes joka päivä (teen keittäminen, aamuilmoitusten tarkistus, repun pakkaaminen kouluun, puhelimen lataaminen yön yli, rutiinisanoman lähettäminen Discordissa). Sen on oltava prosessi, jonka opiskelija todella tekee — ei oppikirjaesimerkki.
- Opiskelija kirjoittaa prosessin **pseudokoodina** (10–20 riviä) käyttäen `SET`-, `IF/ELSE/ENDIF`-rakennetta ja vähintään yhtä rakenteista `WHILE/ENDWHILE` tai `FOR/ENDFOR`. **Vähintään yksi ehto JA vähintään yksi toisto vaaditaan.**
- Opiskelija käsiaja pseudokoodin paperilla jäljityskaaviolla **yhdellä normaalilla syötteellä** (tyypillinen päivä) ja **yhdellä hankalalla syötteellä** (jotain puuttuu, jotain ylimääräistä).
- Reflektio (3–5 lausetta): mikä oli vaikeampaa ilmaista pseudokoodina kuin englanniksi? Mikä oli helpompaa?
- **Miksi AI-resilientti:** ankkuroitu opiskelijan omaan oikeaan rutiiniin. LLM ei voi väärentää hankalan syötteen tapausta *sinun* aamullesi paljastamatta itseään. Jäljityskaavio on myös havaittava tuotos, jonka opettaja voi verrata pseudokoodiin.
- **`### If you are doing this alone` -osiota ei tarvita** — tämä tehtävä ei oleta paria.

**Tehtävä 6.2 — 🟢 PAKOLLINEN (vaihtoehtoinen ehdokas 6.1:lle) — "Ammatillinen pseudokoodi + käsiajo"** *(AI-resilientti ammatillisen ankkurin kautta)*
- Opiskelija valitsee yhden pienen ammatillisen skenaarion kiinteältä listalta: **help-deskin tikettien priorisointi**, **salasanan vahvuuden tarkistus** tai **päivittäinen varmuuskopiointirutiini**. He kirjoittavat 12–20 riviä pseudokoodia ja käsiajavat sen jäljityskaaviolla kahdelle syötteelle.
- Suositeltu oletus: pidä **tehtävä 6.1** PAKOLLISENA tehtävänä (arkinen ankkuri on saavutettavampi O16/O17:lle) ja käytä 6.2:ta SYVENTÄVÄNÄ.

**Tehtävä 6.3 — 🟣 SYVENTÄVÄ — "Etsi bugi"** *(AI-resilientti; havaittava tuotos)*
- Rasmus kirjoittaa lyhyen rikotun pseudokoodikatkelman (8–14 riviä), jossa on täsmälleen yksi bugi. Ehdotettu bugi: `WHILE counter < 5`, jonka pitäisi olla `<= 5`, tai väärän haaran `IF` (`ELSE`-lohko saavutettavissa, vaikka ei pitäisi), tai puuttuva `SET total TO 0` ennen silmukkaa.
- Opiskelija käsiaja sen jäljityskaaviolla, tunnistaa bugin, korjaa sen ja jäljittää korjatun version uudelleen.
- Opiskelija kirjoittaa yhden lyhyen kappaleen arkikielellä: minkä tyyppinen bugi oli (off-by-one, väärä vertailu, puuttuva alustus, väärä haara). Tämä on ainoa paikka viikossa, jossa "bugin tyypin" nimeäminen vaaditaan.

**Tehtävä 6.4 — 🟣 SYVENTÄVÄ — "Jäljitä luokkakaverin pseudokoodi"** *(pari oletettuna → tarvitsee `### If you are doing this alone`)*
- Opiskelija vaihtaa pseudokoodia luokkakaverin kanssa (10–15 rivin katkelma, mielellään tehtävästä 6.1). **Kysymättä ensin, mitä se tekee**, he käsiajavat sen jäljityskaaviolla ja kirjoittavat yhden lauseen arvauksen tavoitteesta.
- He vertaavat sitten kirjoittajan kanssa: tuottiko jäljitys odotetun tulosteen? Oliko tavoite arvattavissa askeleista?
- `### If you are doing this alone` — vaihtoehto on: jäljitä **oma** pseudokoodi aiemmalta viikolta (viikon 5 logiikkarakenneharjoitukset voidaan koodata uudelleen) 24 tunnin tauolla, TAI vaihda luokan chatissa, TAI jäljitä puhelimella kirjoitettu pala ja jäljitä paperilla päivää myöhemmin.

**Tehtävä 6.5 — 🟣 SYVENTÄVÄ — "LLM harjoituskumppanina omaa käsiajoasi vastaan"** *(LLM:n kritisointimekanismi)*
- Opiskelija on käsiajanut oman pseudokoodinsa tehtävästä 6.1. Nyt hän liittää pseudokoodin (ei jäljitystä) LLM:ään annetulla kehotteella ja pyytää LLM:ää ennustamaan jäljityksen samalle hankalalle syötteelle.
- Opiskelija vertaa LLM:n ennustamaa jäljitystä omaansa. Hän kirjoittaa lyhyen kappaleen: missä LLM oli eri mieltä, kuka oli oikeassa (perusteltuna uudella jäljityksellä) ja mitä erimielisyys paljastaa joko opiskelijan pseudokoodista tai LLM:n lukutavasta.
- Koodikehyksessä annettu esimerkkikehote, jossa eksplisiittinen "älä hyväksy LLM:n jäljitystä totena" -rivi.

**Oletusvalinta, jonka Rasmuksen tulisi toimittaa:**
- 🟢 PAKOLLINEN: **Tehtävä 6.1** (*Pseudokoodaa tuttu prosessi*). "Kirjoita pseudokoodi tutusta prosessista ehdolla ja toistolla, sitten käsiaja paperilla" -tehtävä on viikon lukittu selkäranka.
- 🟣 SYVENTÄVÄ: **Tehtävä 6.3** (*Etsi bugi*), **tehtävä 6.4** (*Jäljitä luokkakaverin pseudokoodi*), **tehtävä 6.5** (*LLM-sparraus*).

Jokainen tehtävä päättyy `### Keep your notes` -lohkoon: "Säilytä pseudokoodisi ja jäljityskaavio — **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla** ja nämä ovat täsmälleen sitä raaka-ainetta, jota AT2 pyytää."

**Sanasto, jota jokaisen tehtävän on käytettävä selkokielessä:** pseudokoodi, muuttuja, jäljityskaavio, käsiajo, bugi, odotettu tuloste, todellinen tuloste.

---

### Tiedosto 4 — `student/week-06/vocabulary.md` (10–18 termiä)

**Vaaditut termit (Rasmus voi lisätä omia 1–4, mutta ei saa ohittaa yhtäkään vaadittua):**

1. **Pseudokoodi**
2. **Avainsana** (pseudokoodimerkityksessä — `SET`, `IF`, `WHILE` jne.)
3. **Muuttuja**
4. **Arvo**
5. **Sijoitus** (`SET … TO …` -toiminto)
6. **Syöte**
7. **Käsittely**
8. **Tuloste**
9. **Ehto** (kerrataan viikolta 5)
10. **Toisto** (kerrataan viikolta 5)
11. **Lohko** (`IF`:n, `WHILE`:n tai `FOR`:n runko)
12. **Käsiajo**
13. **Jäljityskaavio**
14. **Bugi**
15. **Odotettu tuloste**
16. **Todellinen tuloste**
17. **Rajatapaus** (kerrataan viikolta 1)
18. **Console** — merkittynä **"katse eteenpäin — viikko 7, jossa pseudokoodi kohtaa oikean kielen"**. (Jos Rasmus haluaa, *expression* tai *return value* voivat korvata tämän katse-eteenpäin-terminä, mutta täsmälleen yksi katse-eteenpäin-termi vaaditaan.)

Jokainen määritelmä on 1–3 lausetta, selkokielellä, lyhyellä arkiesimerkillä missä luonnollista. Tähtää ~14–16 termiä yhteensä.

---

### Tiedosto 5 — `student/week-06/slides.md` (~12–20 kalvoa; tavoite 15–18)

**Suositeltu kalvosisältö (Rasmus voi säätää järjestystä ja otsikoita rakenteen hengessä):**

1. `# Week 6 — From thinking to code` *(otsikkokalvo)*
2. `## The central question` — runko: kurssin keskeinen kysymys **sanatarkasti**.
3. `## This week — pseudocode, variables, dry run` — kolmen luettelopisteen esikatselu O16:sta, O17:sta, O18:sta. Mainitse, että AT2 osuu tälle viikolle.
4. `## What is pseudocode?` — lyhyt lainattava määritelmä. Sisällytä **viikon 6 ydinviesti** sanatarkasti tai lähes sanatarkasti: *"Pseudocode is the bridge between everyday English and real code."*
5. `## The small set of keywords` — `SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`. Yksi sarake.
6. `## English vs. pseudocode — making tea` — rinnakkain, 4 riviä kumpaakin.
7. `## Sequence · condition · repetition` — yhden rivin muistutus, että pseudokoodi koodaa viikon 5 kolme rakennuspalikkaa.
8. `## Input → processing → output` — kolme laatikkoa, yksi esimerkkilause kumpaankin.
9. `## What is a variable?` — määritelmä + etiketöidyn laatikon arkimetafora.
10. `## A good variable name` — `SET x TO 7` vs. `SET passwordLength TO 7`. Kaksi riviä.
11. `## A vocational example — password strength` — 8–10 riviä pseudokoodia yhdellä kalvolla. (Tämä kalvo sitoutuu O17:n itseopiskeluesimerkkiin.)
12. `## What is a dry run?` — määritelmä + linkki takaisin viikon 1 "sananmukaiseen robottiin".
13. `## The trace table` — pieni työstetty esimerkki: 4 riviä, 3 saraketta (rivi, muuttuja, tuloste).
14. `## Finding a bug — actual vs. expected output` — lyhyt ennen/jälkeen.
15. `## AT2 — submitted around Lesson 18` — 3 luettelopistettä: mitä AT2 pyytää, mitä tuoda, mitä EI tuoda.
16. `## Week 6 vocabulary at a glance` — 8–10 avaintermiä.
17. `## Must-do minimum vs. deepening` — kahden luettelon vastakkainasettelu.
18. `## Tasks this week` — 1 rivi per tehtävä.
19. `## What comes next — Week 7: first real code` — esikatselu, ei syntaksin yksityiskohtia.
20. `## Recap — the central question, one more time` — kurssin keskeinen kysymys **sanatarkasti uudestaan** loppukalvona.

Käytä `---` omalla rivillään jokaisen kalvon välillä. Runkosisältö: 3–5 lyhyttä luettelopistettä tai 1–2 lyhyttä virkettä. Ei puhujamuistiinpanosyntaksia, joka olettaa tiettyä renderöijää. **Ei `.pptx`-viittauksia.**

---

### Tiedosto 6 — `teacher/week-06/teacher-materials.md` (2600–4400 sanaa)

**Vaaditut H2-osiot (järjestyksessä, sanatarkalla sanamuodolla, joka on lueteltu toimeksiannossa):**

1. `## Week 6 learning objectives (mapped to Bloom)` — toista O16–O18:n tavoitteet tästä suunnitelmasta, ryhmiteltynä Bloom-vaiheen mukaan. Vain Ymmärtäminen + Soveltaminen.
2. `## Common misconceptions for Week 6` — vähintään 6 yli koko viikon (≥2 per oppitunti). Ehdotettu joukko:
   - **O16:** *"Pseudokoodi on ohjelmointikieli."* → Korjaus: pseudokoodi on jaettu konventio, ei kieli, jota tietokone voi ajaa. // *"On olemassa yksi oikea pseudokoodi."* → Korjaus: eri opettajat käyttävät eri avainsanajoukkoja; tämä kurssi käyttää yhtä kiinteää joukkoa, jotta kaikki lukevat pseudokoodia samalla tavalla.
   - **O17:** *"Muuttuja on sama kuin numero."* → Korjaus: muuttuja on nimetty säilö; tänään se pitää numeroa, huomenna se voi pitää eri numeroa (tai kyllä/ei-arvoa tai lyhyttä merkkijonoa). // *"Muuttujan nimellä ei ole väliä."* → Korjaus: `x` ja `passwordLength` tekevät saman asian tietokoneelle, mutta hyvin eri asioita seuraavalle pseudokoodin lukijalle.
   - **O18:** *"Jos pseudokoodi lukee oikein, se on oikein."* → Korjaus: lukeminen ei löydä off-by-onea, vääriä vertailuja tai puuttuvia alustuksia. Vain jäljityskaavio. // *"Jäljityskaavio on tyhjäntoimitusta — voin käsiajaa sen päässä."* → Korjaus: pään käsiajo on täsmälleen se paikka, jossa bugit selviävät. Taulukon idea on, että se pakottaa kirjoittamaan jokaisen askeleen alas.
3. `## Lesson 16 — 90-minute plan` — konkreettiset aikalohkot, jotka summautuvat 90:een. Ehdotettu runko (peilaa viikon 1 julkaisutyyliä):
   - 0–10 min: lämmittely — lue yksi lyhyt englanninkielinen ohje ääneen, sitten pyydä luokkaa tiivistämään se pseudokoodimaiseen muotoon taululle.
   - 10–30 min: opettajan syöte — pseudokoodin määritelmä + pieni avainsanajoukko. Käytä täydentävää kalvosarjaa `slides-l16-pseudocode-walkthrough.md` tässä (4–8 kalvoa) yhden tutun esimerkin viemiseen läpi alusta loppuun.
   - 30–60 min: **ITSENÄINEN TYÖ** (30 min) — jokainen opiskelija aloittaa tehtävän 6.1 (kirjoita pseudokoodi tutusta prosessista). Vain kirjoittaminen; käsiajo odottaa O18:aa.
   - 60–80 min: pariaktiviteetti — opiskelijat vaihtavat luonnoksia ja lukevat toistensa pseudokoodia hiljaa, alleviivaten yhden epäselvän rivin.
   - 80–88 min: koko luokan purku — kerää 3 esimerkkiriviä vaihdosta, kirjoita yhdessä uudelleen taululle.
   - 88–90 min: esikatsele O17.
   - **Slide cues — pääsarja `slides.md` + täydentävä sarja `slides-l16-pseudocode-walkthrough.md`.** Yhdistä kalvonumerot aikalohkoihin eksplisiittisesti.
4. `## Lesson 17 — 90-minute plan` — konkreettiset aikalohkot, jotka summautuvat 90:een. Ehdotettu:
   - 0–10 min: lämmittely — nimeä kolme oikean maailman "muuttujaa" huoneesta (taulun päivämäärä, nykyinen puhuja, lounasruoka). Pohjusta metafora.
   - 10–30 min: opettajan syöte — syöte/käsittely/tuloste-runko + muuttuja. Kävele salasanan vahvuuden esimerkki taululla elävänä.
   - 30–60 min: **ITSENÄINEN TYÖ** (30 min) — jokainen opiskelija ottaa O16:n pseudokoodinsa ja (a) merkitsee syöte-, käsittely- ja tuloste-osiot; (b) korvaa nimeämättömät arvot nimetyillä muuttujilla.
   - 60–80 min: pariaktiviteetti — parit jäljittävät toistensa syöte/käsittely/tuloste-rungon: löydätkö, missä käsittely tapahtuu?
   - 80–88 min: koko luokan purku — yksi esimerkki taululla.
   - 88–90 min: esikatsele O18 ja AT2.
   - **Slide cues — pääsarja `slides.md`.** (Täydentävää sarjaa ei suositella O17:lle.)
5. `## Lesson 18 — 90-minute plan` — konkreettiset aikalohkot, jotka summautuvat 90:een. AT2 palautetaan tämän oppitunnin tienoilla. Ehdotettu:
   - 0–10 min: lämmittely — taulu-demo jäljityskaaviosta 4 rivin pseudokoodille (esim. kahden arvon vaihto).
   - 10–25 min: opettajan syöte — mikä käsiajo on, miten piirretään jäljityskaavio, mikä lasketaan "bugiksi".
   - 25–55 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat käsiajavat omaa tehtävän 6.1 pseudokoodiaan **yhdellä normaalilla ja yhdellä hankalalla syötteellä**, piirtäen jäljityskaavion käsin.
   - 55–80 min: opettajan vetämä PAKOLLINEN tuntiaktiviteetti — **"Käsiajo luokkana"** (katso `in-class-tasks.md`). Opettaja kirjoittaa tarkoituksellisesti rikotun lyhyen pseudokoodin taululle; opiskelijat ovat jäljityskaavio.
   - 80–88 min: AT2-luovutus — 5 minuuttia siitä, mitä AT2 odottaa, 3 minuuttia selventäville kysymyksille. Rauhallinen tahti.
   - 88–90 min: esikatsele viikkoa 7.
   - **Slide cues — pääsarja `slides.md`.** (Täydentävää sarjaa ei suositella O18:lle.)
6. `## Facilitation tips` — 4–8 lyhyttä vinkkiä. Ehdotettu:
   - Vaadi, että opiskelijat lukevat pseudokoodia ääneen käsiajon aikana. Ääni löytää sen, mitä silmä ei.
   - Älä anna opiskelijoiden kirjoittaa pseudokoodia uudelleen samalla kun he jäljittävät. Jäljitä ensin, korjaa erilliselle sivulle.
   - Suojele 30 minuutin itsenäistä lohkoa; se on osa, jonka paineen alla olevat opettajat leikkaavat ensimmäisenä.
   - Käytä taulua jäljityskaavioille, ei kalvoja. Kalvot pohjustavat kysymyksen; jäljityksen on tapahduttava elävänä.
   - Yhdistä jokainen uusi termi takaisin viikkoon 5 (sekvenssi, ehto, toisto) ja viikkoon 1 (sananmukainen tulkinta, monitulkintaisuus). Viikko 6 on synteesi, ei tuore alku.
   - Kun opiskelijat väittelevät jäljityskaavion kanssa, kysy: *"Mitä rivi 4 sanoi? Lue ääneen. Mitä muuttuja nyt yhtä rivin 4 jälkeen?"*
7. `## Answers to common student questions` — vähintään 5. Ehdotettu:
   - *"Onko pseudokoodi oikea kieli?"* — Ei. Se on jaettu konventio. Eri opettajat käyttävät eri avainsanajoukkoja.
   - *"Voiko tietokone ajaa pseudokoodia?"* — Ei suoraan. Ihmisen (tai kääntäjän) on käännettävä se ensin oikeaksi kieleksi. Viikko 7 on se, jossa käännös alkaa.
   - *"Pitääkö käyttää näitä täsmällisiä avainsanoja?"* — Kyllä, tällä kurssilla, jotta luemme toistemme pseudokoodia samalla tavalla. Oikeissa työpaikoissa jokainen tiimi valitsee yhden joukon ja pysyy siinä.
   - *"Mitä AT2 oikeasti haluaa minulta?"* — Lyhyt pseudokoodi pienestä ammatillisesta tehtävästä (tai tutusta prosessista), jäljityskaavio yhdelle normaalille ja yhdelle hankalalle syötteelle, ja 5 lauseen reflektio siitä, mitä jäljityksesi löysi.
   - *"Mitä jos jäljityskaavioni on eri mieltä pseudokoodini kanssa?"* — Luota jäljityskaavioon yli pään. Sitten joko pseudokoodissa on bugi tai jäljityksessä on bugi; tee jäljitys toisen kerran tuoreelle sivulle ja katso, kumpi siirtyy.
8. `## Formative assessment tips` — 3–5 pikatarkistusta. Poistumislippu ("nimeä yksi muuttuja O16:n pseudokoodistasi ja yksi arvo, jonka se voisi pitää"), tauluäänestys ("kirjoittaako tämä 5 rivin katkelma oikean tulosteen?"), pariraportointi, yhden minuutin paperi.

Viittaa ristiin `in-class-tasks.md`:hen O18-suunnitelmasta ("Käsiajo luokkana" -harjoitus kuuluu O18:n 55–80 min lohkoon). Viittaa ristiin `slides-l16-pseudocode-walkthrough.md`:hen O16-suunnitelmasta.

---

### Tiedosto 7 — `teacher/week-06/in-class-tasks.md` (500–1400 sanaa)

**Vaadittu rakenne:**
- `## Overview` — 2–3 lausetta, jotka nimeävät tehtävät ja milloin viikon aikana ne sopivat.
- Vähintään 1 H2-tehtävä merkittynä **MANDATORY**, joka aidosti vaatii opettajan vetämää luokkahuonevuorovaikutusta.

**Kaksi konkreettista aktiviteetti-ideaa, jotka Rasmuksen tulisi toimittaa (oletus: molemmat):**

**Aktiviteetti A — PAKOLLINEN — "Käsiajo luokkana"** *(koko luokka + opettajan vetämä, ~25 min, sijoitettu O18:aan 55–80 min välille)*
- Opettaja valmistelee **lyhyen, tarkoituksellisesti rikotun pseudokoodikatkelman taululle** (8–14 riviä, täsmälleen yksi bugi). Ehdotettu bugin tyyppi: off-by-one `WHILE`-ehdossa (esim. `WHILE counter < 5` pitäisi olla `WHILE counter <= 5`).
- Luokasta tulee jäljityskaavio. Opettaja antaa yhden opiskelijan per muuttuja (tai yhden per "sarake"). Opettaja lukee pseudokoodin rivi riviltä, hitaasti. Jokaisen rivin jälkeen jokainen "muuttujaopiskelija" huutaa nykyisen arvonsa, ja yksi "tuloste-opiskelija" huutaa kaiken, mikä on kirjoitettu tulosteeseen.
- Koko luokan jäljitys ajetaan loppuun. Odotettu tuloste julkistetaan *vasta kun jäljitys on valmis*. Todellinen tuloste eroaa (bugin takia). Luokka diagnosoi, mikä rivi aiheutti eron.
- Opettaja korjaa bugin taululle (opiskelijoiden ehdotuksilla siitä, mikä rivi ja mikä muutos). Luokka ajaa jäljityksen uudelleen korjauksen yläpuolisesta rivistä. Odotettu tuloste täsmää nyt.
- **Päätös (3 min):** opettaja nimeää bugin tyypin arkikielellä ("tämä oli off-by-one"). Luokka lisää bugin tyypin juokseviin "bugit, jotka olemme löytäneet käsiajamalla" -listaan — pidetään tätä listaa läpi O18:n ja viikkoon 7 asti.
- **Miksi vaatii luokkahuoneen:** jokainen opiskelija saa tehtävän (oman muuttujansa). Ruumiillistettu jäljitys tekee "jäljityskaavio löytää sen, minkä silmä ei" fyysisesti näkyväksi. Sitä ei voi tehdä kotitehtävänä.

**Aktiviteetti B — VALINNAINEN — "Pseudokoodin vaihto ja jäljitys"** *(parityö, ~20 min, sopii O16:n 60–80 min lohkoon tai O17-lämmittelynä)*
- Pari A kirjoittaa lyhyen pseudokoodin (6–10 riviä, yhdellä `IF`:llä ja yhdellä `WHILE`:llä tai `FOR`:lla) mille tahansa tutulle prosessille. He **eivät** nimeä tavoitetta.
- Pari B lukee sen ja jäljittää sen paperilla yhdelle kirjoittajan valitsemalle syötteelle. He kirjoittavat yhden lauseen arvauksen siitä, mitä pseudokoodi tekee.
- Paljastus. Keskustele: tuottiko jäljitys odotetun tulosteen? Voisiko tavoitteen päätellä jäljityksestä?
- Roolit vaihtuvat. Päätöskeskustelu: mikä avainsana (`IF`, `WHILE`, `FOR`) teki tavoitteesta arvattavimman?

Viittaa ristiin takaisin `teacher-materials.md`:hen, jotta opettaja tietää tarkan 90 min lohkon kullekin.

---

### Täydentävä kalvosarja — `student/week-06/slides-l16-pseudocode-walkthrough.md` (SUOSITELTU, 4–8 kalvoa)

O16 on viikon luentopainotteisin osio — opiskelijat kohtaavat uuden notaation, pienen avainsanajoukon ja S/K/T-rungon 20 minuutissa. Pääsarjassa on yksi yhteenvetokalvo per käsite, mikä on hyvä kertaukseen mutta ohut ensikohtaamiseen. **Rasmuksen tulisi toimittaa O16:lle täydentävä kalvosarja, joka käy yhden konkreettisen pseudokoodiesimerkin englannista valmiiseen, jäljitettyyn osaan**, jotta opettaja voi ajaa sitä kalvo kerrallaan O16:n luento-osion aikana menettämättä huonetta.

**Ehdotettu 6 kalvon sisältö `slides-l16-pseudocode-walkthrough.md`:lle:**

1. `# Worked example — making tea` *(otsikkokalvo; lyhyt esittely: sama pohja, jota viikko 1 käytti pikanuudeleille)*
2. `## In English` — 4–5 lyhyttä englanninkielistä lausetta, jotka kuvaavat, miten opiskelija tekee teetä.
3. `## In pseudocode — the skeleton` — sama prosessi pseudokoodina (10–14 riviä), `IF` (sokeri kyllä/ei) ja `WHILE` (kunnes vedenkeitin naksahtaa) näkyvinä.
4. `## Naming the parts` — annotoi, mitkä rivit ovat syötettä, mitkä käsittelyä, mitkä tulostetta. (Sillaksi O17:lle.)
5. `## What got more precise` — yksi lyhyt kalvo, joka nimeää 3 asiaa, jotka pseudokoodi täsmensi, vaikka englanti jätti epämääräisiksi (mikä vedenkeitin, kuinka täynnä, kuinka kauan).
6. `## The template scales` — yksi lyhyt kalvo, joka nimeää kolme muuta paikkaa, joissa tämä runko toimii: help-deskin vastauksen priorisointi, salasanan vahvuuden tarkistus, päivittäinen varmuuskopiointirutiini.

**Miksi O17:n täydentävää kalvosarjaa EI suositella:** O17:n salasanan vahvuuden esimerkki on jo tarpeeksi lyhyt kävellä elävänä taululla, ja pääsarjan kalvo 11 kantaa sen.

**Miksi O18:n täydentävää kalvosarjaa EI suositella:** O18:n jäljityskaavio on parasta tehdä elävänä taululla (ruumiillistettu jäljitys on oppitunti). Kalvo kilpailisi taulun kanssa.

Jos Rasmus on eri mieltä O17:sta tai O18:sta, hän voi toimittaa täydentävän kalvosarjan kummalle tahansa; Wilhelm hyväksyy minkä tahansa 4–8 kalvon täydentävän sarjan, johon viitataan ristiin tiedostosta `teacher-materials.md`.

---

## Avoimet kysymykset

1. **Pseudokoodin murre.** Tämä suunnitelma suosittelee kiinteää avainsanajoukkoa (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). Jotkut opettajat suosivat pienaakkosia (`if`, `while`) tai `:=`:tä sijoitukseen. **Oletusoletus:** Rasmus käyttää ISOJEN KIRJAINTEN avainsanoja + `SET … TO …` -sijoitusta, sovellettuna johdonmukaisesti kaikkien 7 (tai 8) tiedoston yli. Wilhelm tarkistaa johdonmukaisuuden, ei tiettyä valintaa.
2. **Koodikehyksen kielitunniste.** Pseudokoodi menee kehystettyihin lohkoihin. **Oletusoletus:** Rasmus käyttää ` ```text ` (tai ei kielitunnistetta) — **ei koskaan** ` ```js `:tä, ` ```python `:ia tai mitään muuta oikean kielen tunnistetta. Wilhelm greppaa kielitunnisteita.
3. **Listat/taulukot.** Toimeksianto sallii `FOR each x IN list` -esimerkin. **Oletusoletus:** Rasmus käyttää listoja korkeintaan kerran viikon yli, ohimennen, ei koskaan oppimistavoitteena.
4. **AT2:n yksityiskohtainen toimeksianto.** AT2 on "palautetaan O18:n tienoilla" — varsinainen AT2:n toimeksianto elää viikon 6 ulkopuolella (viikon 5 suunnitelma päättyy Bloomin Soveltaminen-pohjaan; AT2:n toimeksianto on erillinen dokumentti). **Oletusoletus:** Rasmus ei kirjoita AT2:n toimeksiantoa; hän nimeää AT2:n tavalla, jota viikon 6 tiedostot vaativat (`### Keep your notes` -lohkot, O18-suunnitelman luovutus, AT2-kalvo) ja olettaa, että AT2:n toimeksianto toimitetaan orkestroijalta.
5. **Katse-eteenpäin-termi sanastossa.** Tämä suunnitelma ehdottaa termiä *console* viikon 7 esikatselutermiksi. **Oletusoletus:** Rasmus käyttää termiä *console*; jos hän suosii termiä *expression* tai *return value*, se on myös hyväksyttävä, kunhan täsmälleen yksi katse-eteenpäin-termi on merkitty.
6. **Reflektiokehotteiden määrä.** Vaadittu: ≥4 kolmen oppitunnin yli itseopiskelussa (≥1 per oppitunti). **Oletusoletus:** Rasmus tähtää 5–6 antaakseen Wilhelmille pelivaraa.
7. **30–50 %:n sääntö — yksi lohko vai jaettu.** Kuten viikolla 1, Wilhelm hyväksyy joko yhden yhtenäisen itsenäisen työn lohkon tai jopa kaksi selvästi merkittyä "ITSENÄINEN TYÖ" -lohkoa per oppitunti, jotka summautuvat 27–45 minuuttiin. **Oletusoletus:** yksi yhtenäinen 30 minuutin lohko per oppitunti (vastaa yllä olevia ehdotettuja runkoja).
8. **Tuntiaktiviteetin laajuus.** "Käsiajo luokkana" on viikon 6 vahva oletus PAKOLLISEKSI harjoitukseksi. **Oletusoletus:** Rasmus toimittaa sen aktiviteettina A O18:aan, plus aktiviteetti B (pseudokoodin vaihto ja jäljitys) VALINNAISENA O16/O17:aan.
9. **Ei-oikea-kieli-grep-lista.** Tämä suunnitelma listaa `console.log`, `let `, `var `, `const `, `function `, `def `, `print(`, `system.out`, `int main`, `<script`, `.js`, `JavaScript`, `Python`, `Java`, `C#` audit-grep-joukoksi. **Oletusoletus:** Wilhelm käyttää täsmälleen tätä listaa; muu ilmeinen oikean kielen tunnus, jonka Rasmus vahingossa kirjoittaa, kaataa myös auditin.
10. **AT2-sanamuoto `### Keep your notes`:ssä.** Tämä suunnitelma vaatii ilmauksen "AT2 lands around L18 of this week" (tai lähinen variantti). **Oletusoletus:** Rasmus käyttää *"AT2 palautetaan tämän viikon oppitunnin 18 tienoilla"* johdonmukaisesti kaikissa tehtävissä.
