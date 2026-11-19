# Ohjelmallinen ajattelu — Viikon 5 suunnitelma (Sune, Portti #1)

Kurssi: Ohjelmallinen ajattelu (englanninkielinen)
Kohderyhmä: 1. vuoden ammatillisen koulutuksen ICT-opiskelijat, ~15–17 v., ei aiempaa ohjelmointikokemusta
Kesto: 8 viikkoa × 3 oppituntia/viikko × 90 min = 24 oppituntia
Viikon 5 sisältö: O13 (Sekvenssi), O14 (Ehdot), O15 (Toisto) — kolme klassista logiikkarakennetta.
Pipelinen tämänkertainen laajuus: Sune tuottaa tämän viikon 5 suunnitelman; Rasmus rakentaa täyden viikon 5 paketin kanonisessa viikkorakenteessa; Linnea/Wilhelm auditoivat viikon 5; Alfred paketoi pelkkä-Markdown-julkaisun viikolle 5 (ei PDF:ää, ei PPTX-renderöintiä tällä kierroksella).

Viikko 5 perii muodon viikon 1 julkaisusta polussa `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` ja syvyyden/volyymin kultaisesta näytteestä polussa `/Users/agent/ai-perusteet-md/student/lesson-01/`. *Tämän suunnitelmatiedoston* H2-otsikot pysyvät suomeksi Sune-mallin mukaisesti; **kaikkien 7:n Rasmuksen viikon 5 tiedoston on oltava täysin englanniksi**.

---

## Suunnitelma

### Viikon 5 sijoittuminen kurssilla

Viikot 1–4 rakensivat käsitteellisen rungon: tietokone on sananmukainen tulkitsija (V1), isot ongelmat pilkotaan pienemmiksi (V2), prosesseja voidaan kuvata ja uudelleenkäyttää (V3), ja "oikea" ei ole ainutkertainen (V4). **Viikko 5 nimeää ne kolme rakenteellista liikettä, joista jokainen kuvattu prosessi koostuu** — sekvenssi, ehto, toisto — ja harjoittaa opiskelijaa tunnistamaan ne arkipuheessa *ennen* niiden kohtaamista koodina viikoilla 6–8. Viikko 5 on myös **välitön perustusviikko AT2:lle**, joka pyytää prosessikuvausta, jossa käytetään selvästi kaikkia kolmea rakennetta ja joka palautetaan viikon 5 lopussa / viikon 6 aikana. Suunnitelma käsittelee viikkoa 5 siis tuotoksen rakennustelineenä, ei itsenäisenä aiheena.

### Viikon 5 teemalauselma

Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: **sekvenssi** (tee A, sitten B, sitten C), **ehto** (jos X, tee A; muuten tee B) ja **toisto** (tee A kunnes/niin kauan kuin/jokaiselle). Kun opiskelija osaa nimetä nämä kolme arkisissa tilanteissa — reseptissä, salasanasäännössä, sähköpostien läpikäynnissä — hänellä on jokaisen ohjelman luuranko. Viikko 5 pysyy *nimeämisen* ja *luonnollisella kielellä ilmaisemisen* tasolla. **Ei koodia, ei testauskehyksiä, ei muodollista vuokaaviosyntaksia sen yli, mitä viikko 3 jo kattoi.** Löyhä, pseudokoodimainen merkintä (`if … then …`, `repeat until …`, `for each …`) on sallittu, mutta sitä käsitellään englanninkielisenä lyhennemerkintänä, ei muodollisena kielenä parser-tason säännöillä.

### O13–O15 erittely viikolle 5

#### Oppitunti 13 — Sekvenssi: ohjelma etenee vaihe vaiheelta

- **Oppimistavoitteet** (Muistaminen + Ymmärtäminen, kevyt Soveltaminen):
  - (a) **Määrittele** *sekvenssi* omin sanoin "yhden vaiheen tekemiseksi toisensa perään, kiinteässä järjestyksessä". *(Muistaminen)*
  - (b) **Tunnista** sekvenssi arkisessa prosessissa (resepti, käyttöönottolista, aamurutiini). *(Ymmärtäminen)*
  - (c) **Selitä**, miksi vaiheiden järjestys yleensä merkitsee, ja anna yksi esimerkki, jossa kahden vaiheen vaihtaminen rikkoo prosessin. *(Ymmärtäminen)*
  - (d) **Kirjoita** 6–10 vaiheen sekvenssi tutusta prosessista niin, että järjestys on tehty näkyväksi numeroinnilla. *(kevyt Soveltaminen)*
- **Avainsanaston esikatsaus:** sekvenssi, vaihe, järjestys, riippuvuus (esikatsaustermi: *ehto*).
- **Keskeinen viesti (yhdellä lauseella):** Sekvenssi on oletusarvo — kun mitään muuta ei sanota, "tee A, sitten B, sitten C" on se, mitä sananmukainen tulkitsija tekee, joten kirjoittamasi järjestys on se järjestys, jonka saat.

#### Oppitunti 14 — Ehdot: if-then-else -ajattelu ja päätöspuut

- **Oppimistavoitteet** (Muistaminen + Ymmärtäminen, kevyt Soveltaminen):
  - (a) **Määrittele** *ehto* omin sanoin "testiksi, joka päättää, mikä vaihe tapahtuu seuraavaksi". *(Muistaminen)*
  - (b) **Tunnista** if/then/else-muoto arkisissa säännöissä (salasanasäännöt, tikettien reititys, "jos sataa, mene bussilla"). *(Ymmärtäminen)*
  - (c) **Selitä** ero *if … then …* (ei vaihtoehtoa) ja *if … then … else …* (vaihtoehto) välillä. *(Ymmärtäminen)*
  - (d) **Piirrä** yksinkertainen kaksi- tai kolmehaarainen päätöspuu tutusta arkisesta säännöstä. *(kevyt Soveltaminen)*
  - (e) **Ilmaise** tositilanteen sääntö luonnollisella `if … then … else …` -muodossa. *(kevyt Soveltaminen)*
- **Avainsanaston esikatsaus:** ehto, testi, haara, päätöspuu, if-then, if-then-else, AND, OR (epämuodollinen). Esikatsaustermi: *toisto*.
- **Keskeinen viesti (yhdellä lauseella):** Ehto on testi, joka jakaa prosessin polun kahtia (tai useampaan), ja testin nimeäminen selkokielellä riittää tekemään jaon näkyväksi sananmukaiselle tulkitsijalle.

#### Oppitunti 15 — Toisto: saman asian tekeminen monta kertaa

- **Oppimistavoitteet** (Muistaminen + Ymmärtäminen, kevyt Soveltaminen):
  - (a) **Määrittele** *toisto* omin sanoin "saman vaiheen tai vaihejoukon tekemiseksi useammin kuin kerran". *(Muistaminen)*
  - (b) **Erottele** *for each* (tunnettu lista), *repeat until* (lopetusehto) ja *while* (jatkamisehto) arkisissa tilanteissa. *(Ymmärtäminen)*
  - (c) **Tunnista** toisto tutuissa prosesseissa (sähköpostien läpikäynti, läsnäolon merkitseminen, puhelimen lataaminen). *(Ymmärtäminen)*
  - (d) **Ilmaise** tositilanteen toistuva toiminta luonnollisella kielellä selkeällä lopetus- tai jatkamisehdolla. *(kevyt Soveltaminen)*
  - (e) **Tunnista** ero kerralleen tehtävän vaiheen ja toistuvan vaiheen välillä prosessikuvauksessa. *(Ymmärtäminen)*
- **Avainsanaston esikatsaus:** toisto, silmukka (epämuodollinen), for-each, repeat-until, while, lopetusehto, laskuri (kevyt, epämuodollinen). Esikatsaustermi: *pseudokoodi* (viikko 6).
- **Keskeinen viesti (yhdellä lauseella):** Toisto on tapa sanoa "sama asia, uudelleen, selkeällä lopetuksella" — ja lopetuksen nimeäminen selkokielellä on se, mikä erottaa hyödyllisen toiston karanneesta.

### Viikko 5 — must-do minimum vs. syventävä

**Must-do minimum (jokaisen opiskelijan on viikon 5 päätteeksi osattava):**
- Nimetä kolme rakennuspalikkaa — sekvenssi, ehto, toisto — ja tunnistaa kukin niistä lyhyessä arkiprosessissa.
- Ilmaista yksi ehto luonnollisella `if … then … else …` -muodolla, ankkuroituna tositilanteen sääntöön.
- Ilmaista yksi toisto luonnollisella muodolla selkeällä lopetuksella (`repeat until …`, `for each item in …`, `while … keep going`).
- Yhdistää kaikki kolme rakennuspalikkaa yhdeksi prosessikuvaukseksi (3–6 sekvenssivaihetta + vähintään yksi ehto + vähintään yksi toisto) tutusta tehtävästä. Tämä on AT2-syöttötuotos.

**Syventävä (valinnainen laajennus, ei pakollinen AT2:n perustasolla):**
- Tunnistaa sisäkkäisiä tai yhdistettyjä ehtoja (`if A AND B` / `if A OR B`) säännöissä, joita he ovat nähneet.
- Huomata ja kuvata yksi rajatapaus, jossa `repeat until` voisi pyöriä ikuisesti, ja lisätä turvalopetus selkokielellä.
- Soveltaa kolmea rakennuspalikkaa ammatilliseen IT-tilanteeseen (salasanan tarkistussääntö, sähköpostien läpikäynti, käyttöönottolista).
- Käyttää LLM:ää harjoitusvastustajana omaa päätöspuutaan vastaan strukturoidulla kehotteella ja selkeällä "älä hyväksy LLM:n tulostetta sananmukaisesti" -ohjeella.

### Miten viikko 5 syöttää AT2:ta

AT2 (palautetaan viikon 5 lopussa / viikon 6 aikana) pyytää opiskelijaa kuvaamaan valitsemansa prosessin luonnollisella kielellä, **vähintään yhdellä sekvenssirungolla, vähintään yhdellä ehdolla ja vähintään yhdellä toistolla**. Viikon 5 must-do minimum on juuri tämä tuotos pienemmässä mittakaavassa, joten AT2-palautus on viikon 5 pakollisen tehtävän hallittu laajennus, ei harppaus. Jokaisen tehtävän `### Säilytä muistiinpanot` -lohkon tiedostossa `student-tasks.md` on muistutettava opiskelijaa, että **tuotos, jonka tällä viikolla tuotat, on AT2:n raaka-ainetta** (ei AT1, joka on jo palautettu viikon 2 loppuun mennessä).

### Miten viikko 5 luovuttaa viikolle 6

Viikko 6 (pseudokoodi ja käsiajo) ottaa viikon 5 luonnollisen kielen sekvenssi/ehto/toisto-kuvaukset ja muodollistaa ne pseudokoodiksi muuttujineen ja jäljitystaulukkoineen. Viikon 5 lopun sanastonkatsaus nimeää **pseudokoodin** selvästi, jotta opiskelijat tietävät, mistä ensi viikolla on kyse. Viikko 5 ei saa ennakoida viikkoa 6 esittelemällä pseudokoodisyntaksia tiukoilla säännöillä; löyhä `if … then …` ja `repeat until …` ovat hyväksyttäviä, mutta muodollinen sisennys, muuttujien sijoitus `:=`- tai `=`-merkillä ja jäljitystaulukot jäävät viikolle 6.

---

## Rajaukset

**Viikon 5 ulkopuolella:**
- **Ei lainkaan koodia.** Ei JavaScriptiä, ei Pythonia, ei syntaksin korostavia koodilohkoja millekään, joka näyttää ohjelmointikieleltä. Sallittu pseudokoodimainen merkintä (`if … then …`, `repeat until …`, `for each …`) menee *tavalliseen Markdown-tekstiin tai lainauslohkoihin*, ei kielelle merkityille koodilohkoille. (Rasmus saa käyttää merkkimättömiä koodilohkoja visuaaliseen kontrastiin lyhyissä esimerkeissä.)
- **Ei muodollista pseudokoodia** tiukalla sisennyksellä, muuttujien sijoituksilla tai operaattorisemantiikalla — se kuuluu viikolle 6.
- **Ei testauskehyksiä** (jest, mocha, vitest, pytest jne.) missään niistä 7 tiedostosta. Tämä on kova kurssin laajuinen sääntö; Wilhelm grep-tarkistaa.
- **Ei totuustauluja, ei Boolen algebran merkintää** (`∧`, `∨`, `¬`). AND ja OR esiintyvät vain selkokielisinä sanoina syventävässä materiaalissa.
- **Ei IDE:itä, ei terminaaleja, ei asennusvaiheita**, ei kehittäjätyökaluja. Viikko 5 on paperia ja ajattelua.
- **Ei alustakohtaisia itsenäisiä harjoituksia** (niitä tuottaa eri tiimi).
- **Ei syvää tietojenkäsittelyteoriaa.** Ei automaatteja, ei pysähtymisongelmaa (edes epämuodollisesti — *karannut silmukka* on OK, *pysähtymisongelma* ei ole), ei Big-O:ta.
- **Ei PDF:ää, ei PPTX-renderöintiä** pipelinessa tällä kierroksella. Alfred paketoi pelkkä-Markdown-julkaisun viikolle 5.
- **Ei "(AI-resilient)"-merkintää** tehtävissä. Ominaisuus auditoidaan Linnean toimesta; merkintä on sisäinen eikä saa esiintyä missään oppijalle näkyvässä tiedostossa.

**Tyyliopas:**
- **Arkinen ennen ICT:tä, aina.** Toimeksiannon nimetyt esimerkit ovat pakollisia: **salasanan tarkistussääntö (ehto), sähköpostien läpikäynti (toisto), käyttöönottolista (sekvenssi).** Jokaisen näistä on esiinnyttävä vähintään kerran tiedostossa `self-study.md` ja oltava uudelleenkäytössä tiedostoissa `student-tasks.md` ja `slides.md`, jotta arki→ICT-yhteys on näkyvissä kaikissa tiedostoissa.
- **"Tietokone on sananmukainen, ei tyhmä."** Peritty viikolta 1. Uudelleenkehystäminen ei ole enää otsikossa, mutta ilmausta "tietokone on tyhmä" ei saa esiintyä missään viikolla 5.
- **Ei "ohjelmallinen ajattelu on vain ohjelmointia"** -virhekäsitystä; ennakoi tarpeen mukaan, jos ehtojen aihe houkuttelee opiskelijaa kytkemään ne `if`-avainsanoihin. Viikko 5 käsittelee silti kolmea rakennetta *ajatteluliikkeinä ensin, syntaksina myöhemmin*.

**Kieli:** Englanti läpi tiedostojen. Börje (suomenkielinen viimeistely) ohitetaan. Tämän suunnitelmatiedoston H2-otsikot (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) saavat pysyä suomeksi, koska ne ovat osa Sune-mallia; **kaikkien 7:n Rasmuksen viikon 5 tiedoston on oltava täysin englanniksi**, mukaan lukien niiden osio-otsikot.

**Pipelinen tämänkertainen laajuus:**
- Sune tuottaa tämän viikon 5 suunnitelman (jota luet).
- Rasmus rakentaa **vain viikon 5** kanonisessa 7 tiedoston viikkorakenteessa (plus halutessaan yhden lisämateriaalin `slides-l14-decision-trees.md`, jos oppitunti 14 tarvitsee syvempää tukea).
- Linnea ja Wilhelm auditoivat vain viikon 5.
- Alfred paketoi pelkkä-Markdown-julkaisun viikolle 5.

---

## Hyväksymiskriteerit

Wilhelm tarkistaa viikon 5 paketin seuraavia konkreettisia, tarkistettavia kriteereitä vasten.

### Rakenteellinen — tiedostot ja kansiot

1. **Kaikki 7 kanonista tiedostoa läsnä**, täsmälleen näillä tiedostonimillä (isot/pienet kirjaimet, pieni alkukirjain, kebab-case):
   - `student/week-05/overview.md`
   - `student/week-05/self-study.md`
   - `student/week-05/student-tasks.md`
   - `student/week-05/vocabulary.md`
   - `student/week-05/slides.md`
   - `teacher/week-05/teacher-materials.md`
   - `teacher/week-05/in-class-tasks.md`
2. **Korkeintaan yksi lisäkalvosarja** kansiossa `student/week-05/`, nimeltään `slides-l14-decision-trees.md` (jos Rasmus päättää, että oppitunti 14 tarvitsee sen — katso #16). Ei muita ylimääräisiä tiedostoja. Ei `.pptx`-tiedostoja, ei muita kalvomuotoja. `media/`-alikansio on sallittu vain, jos jokin kalvo viittaa nimenomaan siellä olevaan kuvaan (ei oleteta viikolla 5).
3. **Ei `slides.pptx`-tiedostoa, ei `deck.md`-tiedostoa, ei Reveal.js HTML:ää, ei PDF:ää** missään. Kova fail, jos löytyy.

### Volyymi (järkevyystarkistuksen rajat, ei kovat rajat)

4. `overview.md`: **200–400 sanaa**.
5. `self-study.md`: **2400–4000 sanaa** (kattaa O13:n, O14:n, O15:n yhdessä asiakirjassa, peilaten viikon 1 rakennetta).
6. `student-tasks.md`: **1000–2200 sanaa**. **1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ** tehtävää (katso #18).
7. `vocabulary.md`: **10–18 termiä**, kukin 1–3 lauseen englanninkielisellä määritelmällä.
8. `slides.md`: **10–20 kalvoa**, eroteltuna `---`-merkillä omalla rivillään, kukin kalvo alkaa H1-otsikolla (`#`) tai H2-otsikolla (`##`) ja 3–5 lyhyellä luettelokohdalla tai 1–2 lyhyellä lauseella.
9. `teacher-materials.md`: **2800–4500 sanaa**. Sisältää **3 × 90 minuutin oppituntisuunnitelmaa** (yksi per oppitunti), kunkin aikalohkot summautuvat 90:een.
10. `in-class-tasks.md`: **500–1400 sanaa**. Sisältää **vähintään 1 PAKOLLISEN opettajavetoisen tuntiharjoituksen**.
11. (Valinnainen) `slides-l14-decision-trees.md`: **4–8 kalvoa**, vain jos Rasmus toimittaa.

### Vaadittavat H2-osiot per tiedosto

12. `overview.md` tulee sisältää (tässä järjestyksessä):
    - `## Week 5 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (käyttäen täsmälleen ilmausta **must-do minimum**, ei "core minimum" eikä "mandatory minimum")
    - `## How the three lessons fit together`
    - `## How this week feeds AT2`
13. `self-study.md` tulee sisältää:
    - `# <Viikon otsikko>` (kutsuva H1, ehdotus: *"Three moves: sequence, condition, repetition"* — Rasmus saa parantaa).
    - `## Introduction` — nimeää viikon keskeisen viestin (sananmukaisesti alla olevassa muodossa).
    - `## Lesson 13 — Sequence: a program proceeds step by step` (tai läheinen variantti).
    - `## Lesson 14 — Conditions: if-then-else thinking and decision trees`.
    - `## Lesson 15 — Repetition: doing the same thing multiple times`.
    - `## Summary and what comes next` — esikatsaus viikolle 6 (pseudokoodi + käsiajo).
    - **Vähintään 5 `> **Pause for a moment:**` -pohdintatehtävää** kolmen oppitunnin yli (≥1 per oppitunti, vähintään 2 siinä oppitunnissa, jonka Rasmus arvioi pisimmäksi).
14. `student-tasks.md` tulee sisältää:
    - `## Overview of the week's tasks` — nimeää must-do minimumin ja muistuttaa opiskelijaa, että **AT2 laskeutuu viikon 5 lopussa / viikon 6 aikana**, ja sitä syötetään tämän viikon pakollisella tehtävällä.
    - Yksi H2 per tehtävä, etuliitteenä `🟢 MANDATORY —` tai `🟣 DEEPENING —`. **Ilmaus "must-do minimum" tulee esiintyä Overview-osiossa** (ei "mandatory minimum"). **Merkintä "(AI-resilient)" ei saa esiintyä** missään.
    - Jokaisella tehtävällä, joka olettaa kumppanin / seuraajan / testaajan, on `### If you are doing this alone` -aliosio konkreettisella vaihtoehdolla (24 tunnin tauko, video itsestäsi, eri laite, luokkachat).
    - Jokainen tehtävä päättyy `### Keep your notes` -lohkoon, joka viittaa **AT2:een** selvästi (ei AT1:een).
15. `vocabulary.md` tulee sisältää yhden H2:n `## Week 5 vocabulary`, sitten jokainen termi H3:na tai lihavoituna määritelmälistana. **Vähintään yksi termi merkittynä "looking ahead"** (ehdotus: *pseudocode* viikolle 6).
16. `slides.md` tulee:
    - Alkaa otsikkokalvolla.
    - Sisältää vähintään yksi kalvo, jonka runko näyttää **keskeisen viestin sananmukaisesti** (katso #21).
    - Käyttää `---`-merkkiä omalla rivillään kalvojen välissä.
    - Ei `.pptx`-viittauksia eikä esittäjän muistiinpanosyntaksia, joka olettaa tietyn renderöijän.
    - **Lisäkalvosarja `slides-l14-decision-trees.md`** on valinnainen; jos toimitettu, sen on oltava 4–8 kalvoa, jotka käyvät YHDEN arki-sitten-ICT-päätöspuun (ehdotettu pari: "pitäisikö ottaa sateenvarjo?" → "pitäisikö tämä kirjautumisyritys estää?"). Jos Rasmus ei toimita sitä, ei sakkoa — päälisen kalvojen on katettava päätöspuut vähintään yhdellä kalvolla joka tapauksessa.
17. `teacher-materials.md` tulee sisältää, **täsmälleen näillä H2-otsikoilla** (Wilhelm grep-tarkistaa):
    - `## Week 5 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 5`
    - `## Lesson 13 — 90-minute plan`
    - `## Lesson 14 — 90-minute plan`
    - `## Lesson 15 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions`
    - `## Formative assessment tips`
    - Jokaisen 90 minuutin suunnitelman on sisällettävä **Slide cues** -aliosio (viittaa päälinen kalvosarjaan ja, jos sovellettavissa, lisäkalvosarjaan).
    - **Common misconceptions for Week 5**: vähintään 6 viikon yli (≥2 per oppitunti), kukin `Correction:`-rivillä.
    - **Answers to common student questions**: vähintään 5 viikon yli.
17b. `in-class-tasks.md` tulee sisältää:
    - `## Overview`
    - Vähintään 1 H2-tehtävä merkittynä **MANDATORY**, joka vaatii opettajavetoista luokkavuorovaikutusta, ristiviitattuna tiedostosta `teacher-materials.md`.

### Pedagogiset säännöt

18. **30–50 %:n sääntö**: tiedostossa `teacher-materials.md` jokaisen 90 minuutin suunnitelman itsenäisen työskentelyn lohkojen on summauduttava **27–45 minuuttiin**. Wilhelm tarkistaa aritmeettisesti.
19. **Bloom-katto**: viikon 5 tavoitteet pysyvät Muistamisessa + Ymmärtämisessä, ja **kevyt Soveltaminen** sallittu (ilmaise ehtoja ja silmukoita luonnollisella kielellä; piirrä yksinkertainen päätöspuu; yhdistä kolme rakennetta yhdessä prosessikuvauksessa). **Kielletyt verbit** viikon 5 tavoitteissa: *luo, rakenna, suunnittele, kehitä, arvioi, tuomitse, debuggaa, optimoi, hajota* (hajota kuuluu viikolle 2; abstraktiopainoiset verbit kuuluvat viikolle 3). *Analyze* saa esiintyä kevyesti vain syventävissä tehtävissä, ei tavoitteissa.
20. **Kolme rakennuspalikkaa on nimettävä samalla tavalla kaikkialla**: *sequence*, *condition*, *repetition*. Synonyymit (selection, iteration, loop, branch) saavat esiintyä ohimennen, mutta yllä olevat kolme substantiivia ovat kanoniset nimet, joita käytetään joka tiedostossa. Wilhelm grep-tarkistaa `sequence`, `condition`, `repetition` tiedostoissa `overview.md`, `self-study.md`, `slides.md` ja `teacher-materials.md`.
21. **Keskeinen viesti sananmukaisesti** — *"Almost any process can be described with three building blocks: sequence, condition, and repetition."* — esiintyy sananmukaisesti **vähintään yhdellä kalvolla** tiedostossa `slides.md` ja **vähintään kerran** tiedostossa `self-study.md` (Introduction tai Summary). Rasmus saa laajentaa lausetta toimeksiannon jatkolla "Once you can name them in everyday tasks, you have the skeleton of every program."
22. **Arkinen ennen ICT:tä -periaate**: tiedostossa `self-study.md` jokainen osio, joka käyttää molempia esimerkkityyppejä, asettaa arkisen esimerkin ensin. Toimeksiannon kolme esimerkkiä on kunnioitettava: **käyttöönottolista (sekvenssi), salasanan tarkistussääntö (ehto), sähköpostien läpikäynti (toisto)** — kukin käytettynä vähintään kerran viikon aikana, ja kukin parittettuna arkisen vastineen kanssa, joka tulee ensin (esim. resepti → käyttöönottolista; "jos sataa, mene bussilla" → salasanan tarkistussääntö; astianpesukoneen tyhjennys → sähköpostien läpikäynti).
23. **Ei koodia missään** missään 7:stä tiedostosta. Pseudokoodimainen merkintä luonnollisen kielen fragmenteissa on hyväksyttävää; kielimerkityt koodilohkot eivät ole. Wilhelm grep-tarkistaa ` ```js`, ` ```javascript`, ` ```python`, ` ```ts` jne.
24. **Ei testauskehyksiä** mainittu missään.
25. **"Tietokone on sananmukainen, ei tyhmä."** Ilmaus "tietokone on tyhmä" / "tietokone on hidas" ei saa esiintyä.
26. **AT2, ei AT1.** Jokaisen `### Keep your notes` -lohkon tiedostossa `student-tasks.md` on viitattava **AT2:een (viikon 5 loppu / viikon 6 aikana)**, ei AT1:een.

### Tehtävät (valintasäännöt)

27. `student-tasks.md` sisältää **1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ** tehtävää. Vähintään **yksi PAKOLLINEN tehtävä** on AT2-syöttö — se pyytää opiskelijaa tuottamaan prosessikuvauksen, jossa yhdistyvät sekvenssi + ehto + toisto.
28. Jokaisella tehtävällä, joka olettaa kumppanin / seuraajan / testaajan, on `### If you are doing this alone` -aliosio. Wilhelm grep-tarkistaa täsmällisen otsikon.
29. Jos SYVENTÄVÄ tehtävä käyttää LLM:ää harjoitusvastustajana, sen on sisällettävä koodilohko esimerkkikehotteella ja selkeällä "älä hyväksy LLM:n tulostetta sananmukaisesti" -ohjeella.

### Tuntitehtävät

30. `in-class-tasks.md` sisältää **vähintään 1 PAKOLLISEN opettajavetoisen tuntiharjoituksen**, joka oikeasti vaatii luokkavuorovaikutusta. Oletuspakollinen: "etsi silmukka / etsi if" -luokitteluleikki tositilanteen esimerkeillä (katso Briefing Rasmukselle alta). Oletusvalinnainen: elävä päätöspuuharjoitus valitusta arkisäännöstä. Molempiin on viitattava asianmukaisesta 90 minuutin suunnitelmasta tiedostossa `teacher-materials.md`.

### Kieli ja viimeistely

31. **Englanti läpi tiedostojen**, kaikki 7 tiedostoa (ja valinnainen lisäkalvosarja, jos toimitettu).
32. **Rekisteri**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` ja `slides.md` CEFR ~B1; `teacher-materials.md` ja `in-class-tasks.md` CEFR ~B2.
33. **Pätevä Markdown**: jokainen koodilohko sulkeutuu, jokainen taulukko renderöityy, ei rikkinäisiä sisäisiä linkkejä, `---`-erottimet omalla rivillään tiedostossa `slides.md`.

---

## Briefing Rasmukselle

### Läpileikkaavat muistutukset (koskevat kaikkia 7 tiedostoa)

- **Arkinen ennen ICT:tä, aina.** Toimeksianto lukitsee kolme esimerkkiä: **käyttöönottolista (sekvenssi), salasanan tarkistussääntö (ehto), sähköpostien läpikäynti (toisto).** Kunkin on esiinnyttävä, ja kukin on edeltettävä arkisella vastineella ensimmäisessä esittelyssä. Ehdotetut arkiset paritukset: teeresepti / aamurutiini → käyttöönottolista; "jos sataa, mene bussilla" / "jos maito haisee, heitä se pois" → salasanan tarkistussääntö; astianpesukoneen tyhjennys / läsnäolon merkitseminen → sähköpostien läpikäynti.
- **Kolme rakennuspalikkaa, kolme nimeä.** Käytä *sequence*, *condition*, *repetition* kanonisina niminä joka tiedostossa. Synonyymit (selection, branch, loop, iteration) saavat esiintyä kerran self-studyssa kanonisen nimen kanssa suluissa, mutta älä vaihda nimiä asiakirjan keskellä.
- **Ei koodia, ei testauskehyksiä, ei muodollista pseudokoodia.** Luonnollisen kielen pseudokoodimaiset fragmentit (`if it rains, then take the bus, else walk`, `for each message in the inbox, …`, `repeat until the inbox is empty`) ovat hyväksyttäviä — ne menevät tavalliseen Markdown-tekstiin tai `>`-lainauslohkoihin, ei ohjelmointikielelle merkityille koodilohkoille. Lyhyet merkkimättömät koodilohkot visuaaliseen kontrastiin ovat hyväksyttäviä.
- **"Tietokone on sananmukainen, ei tyhmä."** Peritty viikolta 1. Älä kirjoita "tietokone on tyhmä/hidas" missään.
- **AT2, ei AT1.** Jokainen `### Keep your notes` viittaa AT2:een.
- **Ei "(AI-resilient)"-merkintää.** Linnea auditoi ominaisuuden, ei merkintää.
- **Keskeinen viesti sananmukaisesti** on esiinnyttävä kalvolla JA tiedostossa `self-study.md`: *"Almost any process can be described with three building blocks: sequence, condition, and repetition."*
- **Bloom-katto.** Vain kevyt Soveltaminen. Opiskelija *ilmaisee* ehdon ja silmukan luonnollisella kielellä; hän ei *toteuta*, *debuggaa* tai *optimoi* mitään.
- **Käytä viikon 1 julkaisun muotoa uudelleen.** Peilaa tiedostomuotoja polusta `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/`. Samat otsikot, sama syvyys, sama "Pause for a moment" -kehotekonvention.

---

### Tiedosto 1 — `student/week-05/overview.md` (200–400 sanaa)

**Vaadittu H2-rakenne (järjestyksessä):**
1. `## Week 5 theme` — yksi lyhyt kappale, joka nimeää kolme rakennuspalikkaa ja keskeisen viestin. Lausu keskeinen viesti *sananmukaisesti* (Rasmuksen valinta, lihavointi vai kursivointi — sen on oltava siellä sana sanalta).
2. `## What you will be able to do by the end of the week` — luettelo 5–7 selkokielisestä "voin tehdä" -lauseesta, kytkettynä O13–O15-tavoitteisiin mutta lausuttuna opiskelijan kielellä. Ehdotettu joukko:
   - Nimeä ja tunnista sekvenssi, ehto ja toisto arkisessa prosessissa.
   - Kirjoita 6–10 vaiheen sekvenssi niin, että järjestys on tehty näkyväksi numeroinnilla.
   - Ilmaise arkinen sääntö muodossa `if … then … else …` selkokielellä.
   - Piirrä pieni päätöspuu (kaksi tai kolme haaraa) tutusta säännöstä.
   - Ilmaise toistuva toiminta selkokielellä selkeällä lopetuksella (`repeat until …`, `for each item in …`).
   - Yhdistä kaikki kolme rakennetta yhdeksi lyhyeksi prosessikuvaukseksi tutusta tehtävästä.
3. `## Must-do minimum vs. deepening` — kahden sarakkeen tai kahden luettelokohdan kontrasti. Pakollisen sarakkeen on sisällettävä AT2-syöttötehtävä. Syventävän sarakkeen on sisällettävä AND/OR-yhdistetyn ehdon idea, karannut silmukka -rajatapaus, ammatillinen näkökulma ja LLM-sparrailuvaihtoehto.
4. `## How the three lessons fit together` — yksi lyhyt kappale, joka näyttää O13 → O14 → O15 -kaaren (*oletusarvo*, sitten *testi, joka jakaa sen*, sitten *testi, joka kierrättää sitä*).
5. `## How this week feeds AT2` — kaksi tai kolme lausetta. Nimeä AT2 selvästi. Sano, että tämän viikon pakollinen tehtävä *on AT2-tuotos pienemmässä mittakaavassa*, ja että muistiinpanojen säilyttäminen ei ole neuvoteltavissa.

**Esimerkit, joihin tukeutua:** teeresepti ja käyttöönottolista (sekvenssi); "jos sataa, mene bussilla" ja salasanan tarkistussääntö (ehto); läsnäolon merkitseminen ja sähköpostien läpikäynti (toisto).

**Pituustavoite:** ~300 sanaa.

---

### Tiedosto 2 — `student/week-05/self-study.md` (2400–4000 sanaa)

**Vaadittu rakenne (järjestyksessä):**

- `# <Viikon otsikko>` — ehdotus: *"Three moves: sequence, condition, repetition"*. Rasmus saa parantaa.
- `## Introduction` (~250–400 sanaa)
  - Aloita tutulla 15-vuotiaan kohtauksella, joka sekoittaa kaikki kolme liikettä nimeämättä niitä — esim. *"You wake up. You check your phone. If it is past 7:30, you skip breakfast; otherwise you eat. Then you walk to school. On the way you check every traffic light: if it is red, you stop; if it is green, you keep going. You repeat this for every crossing until you are at the gate."*
  - Tuo sitten nimet pintaan: **siinä kohtauksessa on kaikki kolme rakennuspalikkaa työssä.**
  - Lausu keskeinen viesti **sananmukaisesti**: *"Almost any process can be described with three building blocks: sequence, condition, and repetition."* Jatka toimeksiannon: *"Once you can name them in everyday tasks, you have the skeleton of every program."*
  - Nimeä AT2 (viikon 5 loppu / viikon 6 aikana) ja sano, että viikko on syöttö.

- `## Lesson 13 — Sequence: a program proceeds step by step` (~600–900 sanaa)
  - `### What sequence means` — lyhyt määritelmä: "yhden vaiheen tekemistä toisensa perään, kiinteässä järjestyksessä, ellei ohje toisin sano." Huomautus: sekvenssi on **oletusarvo** — kun mitään ehtoa tai toistoa ei ole kirjoitettu, sananmukainen tulkitsija kävelee vaiheet ylhäältä alas.
  - `### Sequence in everyday processes` — **arkinen ensin.** Käy yksi tuttu prosessi vaihe vaiheelta (ehdotus: teen tai aamurutiinin valmistus) numeroiden jokaisen vaiheen. **Vaihda sitten kaksi vaihetta** (esim. "kaada kiehuva vesi" ennen "laita teepussi mukiin") ja kysy lukijalta, mitä tapahtuu. Pointti: järjestys merkitsee, koska vaiheet **riippuvat** aiemmista vaiheista.
  - `### Sequence in an IT context` — toimeksiannon esimerkki: **käyttöönottolista** selkokielellä (esim. *"merge the branch → run the build → run the smoke tests → deploy to staging → notify the team → wait for sign-off → deploy to production"*). Huomauta, että useita näistä vaiheista ei voi järjestää uudelleen rikkomatta prosessia.
  - `### Independence vs. dependency` — pehmeä johdatus: jotkin vaiheet voidaan järjestää uudelleen (esim. hampaiden harjaus ennen pukeutumista tai sen jälkeen); jotkin eivät (esim. keitä vesi ennen kuin kaadat sen). Älä muodollista riippuvuuskaaviota — tämä on viikon 3 alue uudelleen vierailtuna. Pidä se intuitiivisena.
  - **≥1 `> **Pause for a moment:**` -kehote.** Ehdotus: *"Write down a 3-step everyday process where the order can be swapped, and another 3-step process where it cannot. What word would you use to describe the difference?"*

- `## Lesson 14 — Conditions: if-then-else thinking and decision trees` (~700–1000 sanaa)
  - `### What a condition is` — lyhyt määritelmä: "testi, joka päättää, mikä vaihe tapahtuu seuraavaksi." Ehto on prosessin hetki, jolloin polku jakautuu.
  - `### Everyday conditions you already use` — **arkinen ensin.** Kolme lyhyttä esimerkkiä:
    - *"If it rains, take the bus; otherwise walk."* — `if … then … else …`.
    - *"If you finish your homework before dinner, you can play games."* — `if … then …` (ei else).
    - *"If the milk smells off, throw it out."* — `if … then …` (yksihaarainen).
  - `### Writing a condition in natural language` — esittele rento merkintä `if … then …` / `if … then … else …` (ei merkitty koodina; tavallisessa tekstissä). Näytä kaksi tai kolme sääntöä ilmaistuna sekä luonnollisena lauseena että rentona muotona. **Ei kielimerkittyjä koodilohkoja.**
  - `### Decision trees — drawing the split` — selitä päätöspuu ehdon kuvana. Näytä 2-haarainen puu säännölle "jos sataa, bussi; muuten kävele" ja 3-haarainen puu säännölle "jos sataa, bussi; muuten jos olet myöhässä, juokse; muuten kävele." Pidä kaaviot ASCII- tai Mermaid-vapaina; kuvaile, miten ne piirretään paperille.
  - `### Conditions in an IT context — password validation` — toimeksiannon esimerkki. Käy tositilanteinen salasanasääntö selkokielellä: *"If the password is shorter than 8 characters, reject it. If it has no number, reject it. If it has no capital letter, reject it. Otherwise accept it."* Näytä sama pienenä päätöspuuna.
  - `### Compound conditions — AND, OR (informal, optional reading)` — lyhyt kappale. Käytä selkokielisiä sanoja *ja* ja *tai*. **Ei Boolen symboleja.** Esimerkki: *"If you have your bus card AND there is money on it, take the bus."* Merkitse tämä aliosio *syventäväksi lukemistoksi*, jos lukija on rohkea.
  - **≥2 `> **Pause for a moment:**` -kehotetta.** Ehdotuksia: (i) *"Write down a rule someone in your family uses with you that has the shape if … then … else … . What is the test?"* (ii) *"Look at a website's sign-up form. Can you name three different conditions the form is checking before it lets you submit?"*

- `## Lesson 15 — Repetition: doing the same thing multiple times` (~700–1000 sanaa)
  - `### What repetition means` — lyhyt määritelmä: "saman vaiheen tai vaihejoukon tekemistä useammin kuin kerran, lopetusehdon kanssa, joka kertoo tulkitsijalle, milloin pysähtyä."
  - `### Everyday repetitions you already use` — **arkinen ensin.** Kolme lyhyttä esimerkkiä:
    - *"Mark each name in the register present or absent."* (`for each name in the register, …`).
    - *"Keep adding sugar and stirring until it tastes right."* (`repeat until …`).
    - *"While the kettle is still hot, you don't need to boil it again."* (`while …`).
  - `### Three shapes of repetition` — anna kolme rentoa muotoa rinnakkain:
    - **For each** — "for each item in a list, do …". Käytä, kun lista on tiedossa etukäteen.
    - **Repeat until** — "do … until a stopping condition is true". Käytä, kun lopetus riippuu siitä, mitä tapahtuu.
    - **While** — "while a condition is true, keep doing …". Käytä, kun testi tarkistetaan ennen jokaista toistoa.
    - Pidä tämä epämuodollisena; älä piirrä vuokaaviota jokaiselle.
  - `### Repetition in an IT context — the inbox sweep` — toimeksiannon esimerkki. Käy luonnollisen kielen prosessi: *"For each unread message in the inbox, decide: if it is from a person, mark it for reply; if it is a newsletter, archive it; if it is spam, delete it. Repeat until the inbox is empty."* Osoita: tämä on yksi prosessi, joka käyttää **kaikkia kolmea rakennuspalikkaa** — sekvenssi viestiä kohti, ehto päätöstä kohti, toisto sähköpostin yli.
  - `### The stopping condition is the safety belt` — pehmeä varoitus karanneista toistoista. Käytä läksyesimerkkiä: *"Keep working on it until you understand"* — mitä jos et koskaan ymmärrä? Näytä, että *jokainen* toisto tarvitsee rehellisen, havaittavan lopetuksen. **Älä käytä sanaa "infinite loop"** kauhutermina; käytä "runaway repetition" tai "no honest stop" selkokielellä.
  - `### Counters (light, informal)` — *jos tarvitaan*, yksi lyhyt kappale: joskus lopetus on luku ("do this five times"). Käsittele luku eräänlaisena `for each`:nä numeroiden 1–5 yli. Ei muuttujasyntaksia. Tämä aliosio voidaan ohittaa, jos se ahtaa oppituntia.
  - **≥2 `> **Pause for a moment:**` -kehotetta.** Ehdotuksia: (i) *"Name one thing you did today that was a repetition. What was the stopping condition?"* (ii) *"Imagine a 'repeat until …' with no stop you can actually observe. What goes wrong?"*

- `## Summary and what comes next` (~200–350 sanaa)
  - Sulje silmukka: lausu keskeinen viesti sananmukaisesti uudelleen, jos sitä ei ollut Introductionissa.
  - Tee AT2-yhteys selväksi: tuotos, jonka tuotat tämän viikon pakollisessa tehtävässä, on samaa muotoa kuin AT2, vain pienempi.
  - Esikatso viikko 6 (pseudokoodi + käsiajo). Sano: *"Next week we tighten these natural-language descriptions into something a little closer to code — but still on paper. It is called pseudocode."*

**Esimerkkivalikko, josta Rasmuksen tulisi valita (arkinen ensin, ICT toisena):**
- Sekvenssi (arkinen): teeresepti, aamurutiini, voileipä, koulumatka, nukkumaanmenovalmistelu.
- Sekvenssi (ICT): käyttöönottolista; help-deskin ensilinjan tiketin triage; "mitä tehdä, kun tulostin ei toimi" -runbook.
- Ehto (arkinen): "jos sataa, mene bussilla", "jos maito haisee, heitä se pois", "jos saat läksyt valmiiksi ennen päivällistä, voit pelata", "jos sinulla on bussikortti JA siinä on rahaa, …".
- Ehto (ICT): salasanan tarkistus, kirjautumisyritys (lukitse tili 3 epäonnistuneen yrityksen jälkeen), roskapostisuodatussääntö, tikettien reititys ("jos opettajalta, prioriteetti 1; muuten prioriteetti 3").
- Toisto (arkinen): läsnäolon merkitseminen, toistojen tekeminen kuntosalisarjassa, perunasäkin kuorinta, jokaisen hampaan harjaaminen.
- Toisto (ICT): sähköpostien läpikäynti, taulukon jokaisen rivin käsittely käsin, jokaisen tuotteen tarkistus paketointilistasta vasten.

**Pituustavoite:** ~3000 sanaa.

---

### Tiedosto 3 — `student/week-05/student-tasks.md` (1000–2200 sanaa)

**Vaadittu rakenne:**

- `## Overview of the week's tasks` — 3–4 lausetta. Lausu, että 🟢 PAKOLLINEN tehtävä on **must-do minimum** ja 🟣 SYVENTÄVÄT tehtävät ovat valinnaisia laajennuksia. Muistuta, että **AT2 laskeutuu viikon 5 lopussa / viikon 6 aikana** ja että tämän viikon pakollinen tehtävä on AT2-tuotos pienemmässä mittakaavassa.

**Viisi tehtäväehdokasta (Rasmus pitää 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ). Oletusvalinta alla.**

**Tehtävä 5.1 — 🟢 PAKOLLINEN — "Kolme liikettä yhdessä prosessissa"** *(AT2-syöttö)*
- Opiskelija valitsee tutun prosessin, jota oikeasti tekee (pyykinpesu; aamupalan valmistus; perhechatin tarkistus; selainvälilehtien sulkeminen koulupäivän päätteeksi; puhelimella kaikkien viikonloppuvalokuvien läpikäynti ja säilytyspäätös).
- He kuvaavat prosessin selkokielellä **kaikilla kolmella rakennuspalikalla**:
  - 3–6 vaiheen sekvenssi runkona.
  - Vähintään yksi `if … then … else …` -ehto testillä, joka on nimetty selkokielellä.
  - Vähintään yksi toisto selkeällä lopetuksella (`for each …`, `repeat until …` tai `while …`).
- He piirtävät ehdon pieneksi päätöspuuksi paperille tai muistiinpanosovellukseen (karkea luonnos riittää).
- He kirjoittavat 3–5 lauseen pohdinnan: *mikä rakennuspalikka oli vaikein nimetä? missä sekvenssin ja toiston raja sumeni?*
- **Miksi PAKOLLINEN:** tämä on AT2-tuotos miniatyyrissä. Linnea auditoi, onko tehtävä AI-kestävä rakenteeltaan (se on — ankkuroitu opiskelijan omaan prosessiin, vaatii havaittavan tuotoksen käsinpiirretyllä puulla ja vaatii pohdintaa opiskelijan tekemästä oikeasta päätöksestä).
- **`### If you are doing this alone`** — ei ehdottoman tarpeellinen tässä (ei kumppania oleteta). Rasmus saa jättää pois TAI sisällyttää 1 lauseen "voit valita prosessin, jota teet täysin yksin, kuten hampaiden harjaus tai puhelimen lataaminen yön yli — ei seuraajaa tarvita."

**Tehtävä 5.2 — 🟢 PAKOLLINEN (vaihtoehto 5.1:lle) — "Etsi nuo kolme jonkun muun prosessista"**
- Opiskelija löytää todellisen prosessikuvauksen luonnosta — reseptin vanhemmalta, koulun protokolla-PDF:n, YouTube-videon transkriptin ohjeen, help deskin vastauksen, jonka he ovat saaneet.
- He merkitsevät asiakirjan alleviivamalla (tai kopioimalla) jokaisen sekvenssirungon, ympyröimällä jokaisen ehdon ja laatikoimalla jokaisen toiston. He kirjoittavat lyhyen lauseen jokaisen merkin viereen selittäen muodon.
- He **kirjoittavat sitten yhden kappaleen uudelleen** prosessista selkeämmässä luonnollisen kielen `if … then … else …` ja `for each / repeat until` -muodossa, säilyttäen merkityksen identtisenä.
- **Miksi PAKOLLINEN-ehdokas:** AT2-kohdistettu, mutta tuotos on annotaatio + uudelleenkirjoitus alkuperäisen kirjoittamisen sijaan. Rasmus valitsee 5.1:n *tai* 5.2:n pakolliseksi rungoksi (oletus: 5.1). Toinen voidaan toimittaa 🟣 SYVENTÄVÄNÄ.

**Tehtävä 5.3 — 🟣 SYVENTÄVÄ — "Päätöspuu todellisesta säännöstä"**
- Opiskelija valitsee todellisen säännön omasta elämästään, jossa on vähintään kaksi haaraa (koulun myöhästymispolitiikka; perheen sääntö ruutujen käytöstä päivällisen jälkeen; verkkosivun tilinpalautusprosessi; työhakemuksen kelpoisuusvaatimukset).
- He piirtävät päätöspuun 2–4 haaralla, nimeävät testin jokaisesta haarasta selkokielellä ja kirjoittavat 3–5 lausetta siitä, mikä haara on vaikein testata rehellisesti.
- Valinnainen: he tunnistavat **yhden yhdistetyn ehdon** (AND tai OR) säännöstä ja kirjoittavat sen uudelleen kahdeksi yksinkertaisemmaksi testiksi.
- **`### If you are doing this alone`** — ei ehdottoman tarpeellinen (ei kumppania oleteta). Rasmus saa sisällyttää 24 tunnin tauon itsetarkistuksena ("palaa huomenna ja piirrä puu muistista uudelleen; muistitko jokaisen haaran?").

**Tehtävä 5.4 — 🟣 SYVENTÄVÄ — "Lopetusehto on turvavyö"** *(rajatapaustyö)*
- Opiskelija kirjoittaa kolme lyhyttä toistoa selkokielellä (esim. *"Keep refreshing the page until the seat is available"* / *"For each photo, decide if it should be deleted"* / *"While the train hasn't arrived, keep checking the platform sign"*).
- Jokaiselle he kysyvät: **mitä jos lopetus ei koskaan tapahdu?** He kuvaavat karanneen tapauksen yhdellä lauseella ja lisäävät turvalopetuksen selkokielellä (esim. *"…or stop after 10 tries"*, *"…or after 30 minutes"*).
- **Miksi syventävä:** rajatapausajattelu; vaikeampaa kuin yhden silmukan ilmaiseminen.
- Ei kumppania tarvita; `### If you are doing this alone` -lohkoa ei vaadita.

**Tehtävä 5.5 — 🟣 SYVENTÄVÄ — "Ammatillinen näkökulma: salasanasääntö, tikettien reititys tai sähköpostien läpikäynti"** *(LLM-sparrailu valinnainen)*
- Opiskelija valitsee **yhden** kolmesta klassisesta ammatillisesta kohtauksesta:
  - Salasanan tarkistussääntö (ilmaise ehdot muodossa `if … then … else …`).
  - Help-deskin tikettien reititys (ilmaise pieneksi päätöspuuksi).
  - Sähköpostien läpikäynti (ilmaise muodossa `for each … if … then … else …` toisto ehtoineen sisällä).
- He kirjoittavat säännön selkokielellä ja piirtävät päätöspuun, jos relevantti.
- **Valinnainen LLM-sparrailuvaihe** — vain tässä viikolla 5. Tarjoa alla oleva strukturoitu kehote **koodilohkossa** ja ohjeista: *"älä hyväksy LLM:n tulostetta sananmukaisesti — jokaisen ehdotuksen kohdalla päätä, säilytätkö, muokkaatko vai hylkäätkö sen, ja kirjoita yksi lause sen viereen sanoen miksi."*

  Sananmukainen näyteohje, joka tulee sisällyttää:
  ```
  You are my sparring partner, not my teacher. I am a vocational ICT
  student practising sequence, condition and repetition in plain English.

  Below is my description of a [password rule / ticket routing rule /
  inbox sweep] using "if … then … else …" and "for each …" / "repeat
  until …" in natural language:

  [paste your description here]

  Please challenge me:
  - Is any condition I wrote ambiguous? Name the ambiguous word.
  - Is any repetition missing an honest stopping condition?
  - Did I confuse a one-off step (sequence) with a repeated step?
  Do not give me the "right" answer outright. Ask me a question that
  helps me see the gap myself.
  ```
- **`### If you are doing this alone`** — ei ehdottoman tarpeellinen (LLM-versiossa ei ihmiskumppania oleteta). Jos Rasmus tarjoaa "testaa luokkatoverilla, joka pelaa validaattoria" -variantin, sen variantin on kannettava otsikko.

**Oletusvalinta, jonka Rasmuksen tulisi toimittaa:**
- 🟢 PAKOLLINEN: **Tehtävä 5.1** (*Kolme liikettä yhdessä prosessissa* — AT2-syöttö).
- 🟣 SYVENTÄVÄ: **Tehtävä 5.3** (*Päätöspuu todellisesta säännöstä*), **Tehtävä 5.4** (*Lopetusehto on turvavyö*), **Tehtävä 5.5** (*Ammatillinen näkökulma*).
- Tehtävä 5.2 pidetään varastossa: Rasmus saa vaihtaa sen toiseksi PAKOLLISEKSI tai neljänneksi SYVENTÄVÄKSI, jos Linnea/Wilhelm pyytävät enemmän annotaatioharjoitusta.

Jokainen tehtävä päättyy `### Keep your notes` -lohkoon, joka viittaa **AT2:een (viikon 5 loppu / viikon 6 aikana)** — ei AT1:een. Ehdotettu sanamuoto: *"Keep your process description, your decision tree, and your reflection in the same notebook. AT2 lands at the end of this week / during Week 6 and will ask you to scale exactly this artefact up."*

**Pituustavoite:** ~1500 sanaa.

---

### Tiedosto 4 — `student/week-05/vocabulary.md` (10–18 termiä)

**Vaaditut termit** (Rasmus saa lisätä 1–4 omaa, mutta ei jättää pois mitään vaadittua):
1. Sequence
2. Step (palautettu viikolta 1; päivitä määritelmä)
3. Order
4. Dependency *(kevyt — "step B needs the result of step A")*
5. Condition
6. Test (palautettu viikolta 1; uusi merkitys: "the question a condition asks")
7. Branch
8. Decision tree
9. If-then
10. If-then-else
11. Repetition
12. For-each
13. Repeat-until
14. While
15. Stopping condition
16. **Pseudocode** — merkittynä **"looking ahead — central topic of Week 6"**.

Valinnaiset lisäykset, joita Rasmus saa sisällyttää, jos hyödyllistä: *counter* (kevyt, epämuodollinen), *runaway repetition*, *AND / OR (informal compound condition)*, *loop* (synonyymi toistolle, merkitse sellaiseksi).

Jokainen määritelmä on 1–3 lausetta, selkokielistä englantia, lyhyellä arkisella esimerkillä, jos luonnollista.

**Pituustavoite:** ~14 termiä.

---

### Tiedosto 5 — `student/week-05/slides.md` (10–20 kalvoa; tavoite 14–17)

**Suositeltu kalvorunko (Rasmus saa säätää järjestystä ja otsikoita rakenteen hengessä):**

1. `# Week 5 — Three moves: sequence, condition, repetition` *(otsikkokalvo)*
2. `## The central message` — runko: keskeinen viesti **sananmukaisesti**. *"Almost any process can be described with three building blocks: sequence, condition, and repetition."*
3. `## What this week trains` — 3 luettelokohdan esikatsaus O13:sta (sekvenssi), O14:stä (ehdot), O15:stä (toisto).
4. `## Sequence — the default move` — lyhyt määritelmä + 2 rivin esimerkki (teeresepti 4 numeroidulla vaiheella).
5. `## When order matters` — vierekkäin: kaksi saman reseptin järjestystä, yksi toimii, toinen ei.
6. `## Sequence at work — deployment checklist` — lyhyt lista (merge → build → smoke test → deploy to staging → sign-off → deploy to production).
7. `## Condition — a test that splits the path` — lyhyt määritelmä + `if it rains, take the bus, else walk` -esimerkki.
8. `## if … then … else …` — rento merkintä yhdellä kalvolla, yksi arkinen ja yksi ICT-esimerkki rinnakkain. **Ei merkitty koodina.**
9. `## Decision tree — drawing the split` — pieni kaksihaarainen puu näytettynä ASCII:na tai haarojen kuvauksena.
10. `## Condition at work — password validation` — salasanasääntö selkokielellä; 3–5 lyhyttä luettelokohtaa.
11. `## Repetition — doing it again, with a stop` — lyhyt määritelmä + arkinen esimerkki "merkitse jokainen nimi luettelosta".
12. `## Three shapes of repetition` — for each / repeat until / while, yksi rivi kullekin.
13. `## Repetition at work — the inbox sweep` — sähköpostien läpikäynti selkokielellä; merkitse, että se käyttää kaikkia kolmea rakennuspalikkaa.
14. `## The stopping condition is the safety belt` — lyhyt kalvo karanneista toistoista ja rehellisistä lopetuksista.
15. `## Three moves in one process` — visualisointi yhdestä lyhyestä prosessista, jossa sekvenssirunko, yksi ehto ja yksi toisto merkittynä.
16. `## Must-do minimum vs. deepening` — kahden sarakkeen kontrasti.
17. `## Tasks this week` — 1 rivi per tehtävä (5.1 pakollinen; 5.3, 5.4, 5.5 syventävä).
18. `## What comes next: Week 6 — pseudocode` — esikatsaus.
19. `## Recap — the central message, one more time` — keskeinen viesti **sananmukaisesti** uudelleen (täyttää sananmukaisuusvaatimuksen kalvon #2 rinnalla).

Tavoite ~15–17 kalvoa. Käytä `---`-merkkiä omalla rivillään jokaisen kalvon välissä. Sisältö: 3–5 lyhyttä luettelokohtaa tai 1–2 lyhyttä lausetta. Ei `.pptx`-viittauksia.

---

### Lisäkalvosarja — `student/week-05/slides-l14-decision-trees.md` (4–8 kalvoa; VALINNAINEN)

**Tarvearviointi.** Oppitunti 14 (ehdot + päätöspuut) on viikon tihein 90 minuutin osio: opiskelijat kohtaavat *ehdon*, *if-then-else:n*, *päätöspuun* ja (valinnaisesti) *AND / OR yhdistetyt ehdot* kaikki yhdessä oppitunnissa. Rasmuksen tulisi toimittaa lisäkalvosarja **jos** päälisen kalvosarjan kalvot 7–10 tuntuvat ahtailta tai jos hän haluaa antaa opettajalle "käy yksi päätöspuu hitaasti, päästä päähän" -vaihtoehdon oppitunnin 14 luento-osuuteen.

**Jos toimitetaan, 4–8 kalvon luonnos:**

1. `# Decision trees — one tree end to end` *(otsikkokalvo)*
2. `## The everyday rule` — *"Should I take an umbrella today?"* — näytä suullinen sääntö: *"If it is raining now, yes. If it is not raining but the forecast says rain, yes. Otherwise no."*
3. `## Draw the tree — branches and tests` — renderöi kolmehaarainen puu ASCII:lla tai kuvattuna muodossa: juurikysymys, "sataako nyt?", sitten "lupaako ennuste sadetta?", kolme lehteä.
4. `## Express the rule in natural-language if … then …` — kirjoita sama sääntö rentona merkintänä yhdellä kalvolla. **Ei merkitty koodina.**
5. `## The IT mirror — should this login attempt be blocked?` — *"If the password is wrong AND it is the 4th try in 5 minutes, block. If the password is wrong but fewer than 4 tries, retry. If the password is right, log in."* Näytä puu.
6. `## Same shape, different scene` — rinnakkain: sateenvarjopuu ja login-puu. Identtinen muoto, eri testit.
7. `## Naming the test honestly` — päätöskalvo: päätöspuun laatu on sen haarojen testien laatu. *"Onko nyt sade?"* on rehellinen. *"Tuleeko jossain vaiheessa sade?"* ei ole.

**Jos Rasmus ei toimita lisäkalvosarjaa**, päälisen kalvojen on silti katettava päätöspuut vähintään yhdellä kalvolla (kalvo #9 yllä olevassa rungossa). Ei sakkoa ohittamisesta; oletusarvo on **KYLLÄ — toimita se**, koska oppitunti 14 on tihein.

---

### Tiedosto 6 — `teacher/week-05/teacher-materials.md` (2800–4500 sanaa)

**Vaaditut H2-osiot (täsmälleen tällä sanamuodolla — Wilhelm grep-tarkistaa):**

1. `## Week 5 learning objectives (mapped to Bloom)` — lausu uudelleen O13–O15-tavoitteet tästä suunnitelmasta, ryhmiteltynä Bloom-vaiheen mukaan. Muistaminen + Ymmärtäminen hallitseva; kevyt Soveltaminen hyväksyttävää.

2. `## Common misconceptions for Week 5` — vähintään 6 viikon yli (≥2 per oppitunti). Ehdotettu joukko:
   - **O13:** *"Sekvenssi on liian itsestäänselvä laskettavaksi rakennuspalikaksi."* → Korjaus: suurin osa todellisista bugeista tulee yhdestä vaihdetusta vaiheesta. Sekvenssi on oletusarvo, ja oletusarvossa hajoamiset tapahtuvat. // *"Jos en kirjoita ehtoa, prosessissa ei ole päätöksiä."* → Korjaus: se tarkoittaa vain, että jokainen vaihe on ehdoton — sekvenssi on *haarautumisen puute*, ei tärkeyden puute.
   - **O14:** *"`if … then …` on sama kuin `if … then … else …`."* → Korjaus: `if … then …` ilman else-haaraa tarkoittaa "ei mitään ylimääräistä muuten"; `else` sanoo mitä tehdä sen sijaan. Tulkitsija käyttäytyy eri tavalla. // *"Yhdistetyt ehdot ovat edistyneitä ja minun pitäisi välttää niitä."* → Korjaus: käytät AND-sanaa ja OR-sanaa joka päivä ("jos minulla on kortti JA siinä on rahaa"). Niiden nimeäminen on hyväksyttävää. Vain symbolit ovat edistyneitä; ajattelu ei ole.
   - **O15:** *"Silmukka on vain sekvenssi, joka on kirjoitettu monta kertaa."* → Korjaus: silmukka on yksi lause ja lopetusehto. Jos joudut kirjoittamaan sen 100 kertaa, et ole ymmärtänyt toistoa. // *"`repeat until` pysähtyy aina."* → Korjaus: se pysähtyy jos ja vain jos lopetusehto pystytään oikeasti havaitsemaan ja saavuttamaan. *"Toista, kunnes ymmärrät"* ei ole lopetus.

3. `## Lesson 13 — 90-minute plan` — konkreettiset aikalohkot, jotka summautuvat 90:een, itsenäisen työn lohko **27–45 min**. Ehdotettu luuranko:
   - 0–10 min: lämmittely — luokka nimeää kolme arkista sekvenssiä taululle; opettaja vaihtaa kaksi vaihetta yhdessä niistä ja kysyy, mitä tapahtuu.
   - 10–25 min: opettajan input — määrittele sekvenssi; näytä yksi arkinen sekvenssi ja yksi ICT-sekvenssi (käyttöönottolista) rinnakkain.
   - 25–55 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat kirjoittavat 6–10 vaiheen sekvenssin oikeasti tekemästään prosessista, numeroiden jokaisen vaiheen, selvällä syötteellä ja tulosteella (tämä aloittaa AT2-syöttötehtävän; ehdot ja toisto lisätään O14:ssä/O15:ssä).
   - 55–75 min: pariaktiviteetti — opiskelijat vaihtavat sekvenssejä, vaihtavat kaksi vaihetta, joiden pari ajattelee voivansa silti toimia, ja antavat takaisin; kirjoittaja yrittää rikkoa sen.
   - 75–85 min: koko luokan purku — kerää 2–3 tapausta, joissa järjestys oikeasti merkitsi; rakenna "järjestys merkitsee / järjestys ei merkitse" -kaksisarakkeinen taulu.
   - 85–90 min: esikatsaus oppitunnille 14 (ehdot).
   - **Slide cues** -aliosio: lämmittely ei kalvoja; luennon kalvot 4 → 6 (Sequence + When order matters + Deployment checklist); itsenäinen työ ei kalvoja (tai jätä kalvo 5 hiljaiseksi muistutukseksi); pariaktiviteetti ei kalvoja; purku ei kalvoja (käytä taulua); päätös ei kalvoja.

4. `## Lesson 14 — 90-minute plan` — sama aritmetiikkarajoitus. Ehdotus:
   - 0–10 min: lämmittely — opettaja kirjoittaa suullisen arkisäännön taululle (*"if it rains, take the bus, else walk"*) ja pyytää luokkaa piirtämään puun paperille 2 minuutissa.
   - 10–30 min: opettajan input — määrittele ehto; käy `if … then …`, `if … then … else …` ja `if … then … else if … then … else …`. Käy yksi päätöspuu päästä päähän (sateenvarjosääntö). **Tässä lisäkalvosarja — jos toimitettu — käytetään täysimittaisesti.**
   - 30–55 min: **ITSENÄINEN TYÖ** (25 min) — opiskelijat laajentavat O13-sekvenssiään lisäämällä vähintään yhden ehdon `if … then … else …` -testillä, joka on nimetty selkokielellä. He piirtävät myös ehdon pieneksi puuksi.
   - 55–80 min: **PAKOLLINEN opettajavetoinen tuntiaktiviteetti** — *"Etsi if"* -luokitteluleikki (katso `in-class-tasks.md`). Opettaja lukee lyhyitä arki-/ICT-lauseita; luokka luokittelee jokaisen joko sisältäväksi ehdon (ja mikä testi) tai ei.
   - 80–88 min: koko luokan purku — mitkä lauseet olivat vaikeimpia luokitella? missä testi oli piilossa?
   - 88–90 min: esikatsaus oppitunnille 15 (toisto).
   - **Slide cues** -aliosio: lämmittely käyttää kalvoa 7 (Condition — a test that splits the path); luennon kalvot 7 → 10 (Condition + if/then/else + Decision tree + Password validation); **jos lisäkalvosarja toimitettu**, aja se päälisen kalvojen 9 ja 10 välissä; itsenäinen työ jätä kalvo 8 esille; tuntiaktiviteetti ei kalvoja; purku ei kalvoja; päätös ei kalvoja.

5. `## Lesson 15 — 90-minute plan` — sama aritmetiikkarajoitus. Ehdotus:
   - 0–10 min: lämmittely — luokka huutaa kolme toistoa, joita he ovat tehneet tähän mennessä tänään (hampaiden harjaus, 10 liikennevalon ohittaminen, chatin päivittäminen uusien viestien vuoksi); kerää taululle.
   - 10–28 min: opettajan input — määrittele toisto; näytä kolme muotoa (for each / repeat until / while) yhdellä esimerkillä per muoto; esittele "lopetusehto on turvavyö".
   - 28–58 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat lisäävät toiston O13+O14-prosessiinsa ja kirjoittavat selkeän lopetusehdon. He myös kirjoittavat yhden lauseen kuvaten miltä karannut tapaus näyttäisi.
   - 58–80 min: **VALINNAINEN mutta suositeltava opettajavetoinen aktiviteetti** — *"Etsi silmukka"* -luokitteluleikki (O14:n "Etsi if":n kumppani). Opettaja lukee lyhyitä arki-/ICT-lauseita; luokka luokittelee jokaisen joko sisältäväksi toiston (ja mikä lopetus) tai ei. Tämä on luokitteluleikin toinen puolikas tiedostossa `in-class-tasks.md`; opettajat voivat ajaa vain "Etsi if":n O14:ssä ja vain "Etsi silmukan" O15:ssä, tai ajaa yhdistetyn version molempien yli.
   - 80–88 min: koko luokan purku — kerää kolme karannutta tapausta ("toista, kunnes ymmärrät", "niin kauan kuin sivu vielä latautuu", "jokaiselle asialle listalla"); pohdi, miltä rehellinen lopetus näyttäisi.
   - 88–90 min: esikatsaus viikolle 6 (pseudokoodi + käsiajo). Mainitse, että AT2 palautetaan tämän viikon lopussa / viikon 6 aikana.
   - **Slide cues** -aliosio: lämmittely ei kalvoja; luennon kalvot 11 → 14 (Repetition + Three shapes + Inbox sweep + Stopping condition); itsenäinen työ jätä kalvo 12 esille; tuntiaktiviteetti ei kalvoja; purku ei kalvoja; päätös kalvo 18 (What comes next: Week 6) sitten kalvo 19 (Recap — central message verbatim).

6. `## Facilitation tips` — vähintään 5 lyhyttä vinkkiä. Ehdotuksia:
   - **Vaadi kanonisia nimiä.** *Sekvenssi, ehto, toisto.* Synonyymit (selection, branch, loop, iteration) ovat hyväksyttäviä, mutta pari ne aina kanonisen nimen kanssa ensimmäisellä kerralla.
   - **Johda arkisella esimerkillä. Aina.** Sama sääntö kuin viikolla 1. Salasanan tarkistussääntö, sähköpostien läpikäynti ja käyttöönottolista saapuvat teereseptin, "jos sataa, mene bussilla" ja "merkitse jokainen nimi luettelosta" *jälkeen*.
   - **Suojaa itsenäisen työn lohkoa.** Viikko 5 rakentaa AT2-tuotosta kolmen oppitunnin yli. Jos 90 minuutin suunnitelma liukuu, leikkaus tulee koko luokan purusta, ei itsenäisen työn lohkosta.
   - **Älä lipsahda koodiin.** Kun opiskelija luonnostaan kirjoittaa `if (x > 0) {` tai vastaavaa, kirjoita uudelleen taululle pehmeästi muotoon *"if x is greater than 0, then …"* selkokielellä. Koodi saapuu viikolla 7, ei viikolla 5.
   - **Nimeä testi, älä vastaus.** Kun opiskelija piirtää päätöspuun epämääräisellä haaralla kuten *"jos menee pieleen"*, paina: *"mikä täsmällinen testi sananmukainen tulkitsija tekisi tietääkseen, että meni pieleen?"*
   - **Rehelliset lopetukset.** Kun opiskelija kirjoittaa *"toista, kunnes valmis"*, kysy: *"miten tulkitsija tietää, että on valmis? Mitä he katsoisivat?"* Jos vastaus on *"he vain tietävät"*, lopetus ei ole vielä rehellinen.

7. `## Answers to common student questions` — vähintään 5 viikon yli. Ehdotuksia:
   - *"Onko `if … then …` sama kuin `if … then … else …`?"* — Ei. Ilman `else`-haaraa tulkitsija ei tee mitään ylimääräistä muutoin. `else`-haaran kanssa tulkitsija tekee jotain muuta.
   - *"Voiko ehdolla olla enemmän kuin kaksi haaraa?"* — Kyllä, `else if`-haaralla. Kolme tai neljä haaraa on normaalia; yli viisi tarkoittaa yleensä, että sääntö piilottaa syvemmän rakenteen.
   - *"Onko `for each` silmukka vai sekvenssi?"* — Silmukka (toisto). Se tekee saman asian kerran jokaiselle kohteelle, ja kohteiden lista on lopetusehto.
   - *"Mitä jos `repeat until` voisi pyöriä ikuisesti?"* — Lisää turvalopetus: `tai pysähdy N yrityksen jälkeen`, `tai pysähdy 30 minuutin jälkeen`. Jokaisella rehellisellä toistolla on vähintään yksi havaittavissa oleva lopetus.
   - *"Onko tämä AT2:ssa?"* — Kyllä. Tuotos, jonka rakennat O13:n, O14:n ja O15:n yli, on AT2-tuotos pienemmässä mittakaavassa. Säilytä muistiinpanosi.
   - *"Voinko käyttää koodia AT2:ssa?"* — Et vielä. AT2 on luonnollista kieltä, jossa `if … then … else …` ja `for each / repeat until / while` ovat löyhää, englanninkielistä merkintää. Pseudokoodi (hieman muodollisempi) esitellään ensi viikolla, viikolla 6.

8. `## Formative assessment tips` — 3–5 nopeaa tarkistusta. Ehdotuksia:
   - **Exit ticket O13:n jälkeen:** *"Nimeä yhden tänään ajamasi prosessin sekvenssirunko."* Yksi lause per opiskelija.
   - **Tauluäänestys O14:n jälkeen:** näytä kolme lyhyttä sääntöä ja kysy luokalta, kummalla on eniten haaroja päätöspuussaan.
   - **Tarralappujen keräys O15:n jälkeen:** jokainen opiskelija kirjoittaa yhden "karanneen toiston, jonka on kuullut tai sanonut" tarralapulle. Lue 3 satunnaisesti; luokka ehdottaa turvalopetusta kullekin.
   - **Minuuttipaperi viikon lopussa:** *"Yhdellä lauseella, nimeä rakennuspalikka, jonka tunnistat helpoimmin, ja se, jonka tunnistat vaikeimmin."*

Ristiviittaus `in-class-tasks.md`:hen O14:stä ja O15:stä. Luokitteluleikki on viikon pakollinen ankkuri.

**Pituustavoite:** ~3500 sanaa.

---

### Tiedosto 7 — `teacher/week-05/in-class-tasks.md` (500–1400 sanaa)

**Vaadittu rakenne:**
- `## Overview` — 2–3 lausetta nimeten tehtävät ja milloin viikon aikana ne sopivat.
- Vähintään 1 H2-tehtävä merkittynä **MANDATORY**.

**Kaksi konkreettista aktiviteetti-ideaa, jotka Rasmuksen tulisi toimittaa (oletus: molemmat):**

**Aktiviteetti A — PAKOLLINEN — "Etsi if / Etsi silmukka" (luokitteluleikki)** *(koko luokka + opettajavetoinen, 25 min per puolikas, sijoitettuna O14:een ja O15:een)*
- Opettaja valmistaa **kaksi pinoa lappuja** (tai kalvolista):
  - Pino 1 — **Ehdot:** ~10 lyhyttä lausetta, joistain sisältää ehdon ja joistain ei. Sekoita arkista ja ICT:tä. Ehdotettuja siemeniä: *"If the password is shorter than 8 characters, reject it."* / *"Boil the water."* / *"If it rains, take the bus, else walk."* / *"Pour 30 ml of milk into the mug."* / *"If the user has not logged in for 90 days, deactivate the account."* / *"Add a teaspoon of sugar."* / *"If you finish your homework before dinner, you can play games."* / *"Switch the kettle on."*
  - Pino 2 — **Toistot:** ~10 lyhyttä lausetta. Ehdotettuja siemeniä: *"For each name in the register, mark present or absent."* / *"Make a cup of tea."* / *"While the kettle is still hot, do not boil it again."* / *"Repeat until the inbox is empty."* / *"Press the button once."* / *"For each photo on the phone, decide if it should be deleted."* / *"Keep refreshing the page until the seat is available."* / *"Open the front door."*
- Ajojärjestys:
  1. **Oppitunnilla 14 (60–80 min slot, 25 min):** opettaja lukee pinon 1 lappu kerrallaan. Luokka äänestää: *ehto* tai *ei ehtoa*. Jos ehto, luokka nimeää testin. Opettaja kirjoittaa tuloksen taululle kanonisella `if … then … else …` -muodolla, jos relevantti.
  2. **Oppitunnilla 15 (58–80 min slot, ~22 min):** opettaja lukee pinon 2 lappu kerrallaan. Luokka äänestää: *toisto* tai *ei toistoa*. Jos toisto, luokka nimeää **lopetusehdon**. Opettaja kirjoittaa tuloksen taululle kanonisella `for each / repeat until / while` -muodolla.
- **Päätös kunkin puolikkaalle:** yksi lyhyt koko luokan kysymys — *"Mikä lappu oli vaikein luokitella, ja miksi?"*
- **Miksi PAKOLLINEN.** Tämä aktiviteetti on viikon kalibrointihetki. Opiskelijat eivät voi suorittaa AT2-syöttötehtävää itsevarmasti, ellei heillä ole kykyä tunnistaa kolmea rakennuspalikkaa kielestä, jota he eivät ole itse kirjoittaneet. Luokassa pidetty versio on nopeampi ja diagnostisempi kuin pyytää jokaista opiskelijaa tekemään se yksin vihossaan.

**Aktiviteetti B — VALINNAINEN mutta suositeltava — "Live-päätöspuu taululle"** *(koko luokka + opettajavetoinen, 20 min, sijoitettuna O14:een, 30–55 min slot tai vaihtoehtona osalle luentoa)*
- Opettaja valitsee yhden arkisäännön, jonka koko luokka tuntee (ehdotus: koulun myöhästymispolitiikka; tai perheen sääntö ruutujen käytöstä ennen nukkumaanmenoa; tai "pitäisikö ottaa sateenvarjo?"). Kirjoittaa säännön yhdellä lauseella taululle.
- Vaihe 1: **Tunnista juurikysymys.** Luokka ehdottaa yhden lauseen testin. Opettaja kirjoittaa sen puun huipulle.
- Vaihe 2: **Haarauta.** Luokka ehdottaa kaksi tai kolme haaraa (kyllä / ei tai kolme kauhaa). Opettaja piirtää viivat.
- Vaihe 3: **Testi jokaisessa haarassa.** Jokaiselle haaralle luokka ehdottaa, mitä tapahtuu lehdessä — ja odottaako siellä *toinen* testi.
- Vaihe 4: **Tunnista huono testi.** Opettaja kutsuu luokkaa nimeämään *yhden* haaran, jossa testi ei ole rehellinen — *"olenko myöhässä?"* ei ole rehellinen ennen kuin siitä tulee *"onko aika yli 8:15?"*. Kirjoita testi uudelleen taululle.
- Vaihe 5: **Yhdistä AT2:een.** Opettaja muistuttaa: *"Omassa AT2-tuotoksessanne jokaisen ehdon takana on tällainen puu piilossa. Testin rehellisyys merkitsee enemmän kuin puun muoto."*
- **Miksi VALINNAINEN.** Päällekkäinen Aktiviteetti A:n luokitteluleikin kanssa. Jos opettajalla on aikaa vain yhdelle, aja Aktiviteetti A — luokitteluleikki on diagnostisempi ja kattaa sekä ehdot että toistot. Aktiviteetti B on syvempi vaihtoehto luokille, jotka jo tuntevat olonsa varmaksi.

Ristiviittaa molemmat aktiviteetit takaisin tiedostoon `teacher-materials.md`, jotta opettaja tietää täsmällisen 90 minuutin slotin kullekin.

**Pituustavoite:** ~900 sanaa.

---

## Avoimet kysymykset

1. **Lisäkalvosarja — toimita vai pidätä?** Tämä suunnitelma suosittelee `slides-l14-decision-trees.md`:n (4–8 kalvoa) toimittamista, koska O14 on tihein oppitunti. **Oletusarvo:** Rasmus toimittaa sen. Jos hän pidättää, päälisen kalvojen on silti katettava päätöspuut vähintään yhdellä kalvolla.
2. **PAKOLLISEN tehtävän valinta — 5.1 vai 5.2?** Toimeksianto sallii 1–2 pakollista tehtävää. AT2-kohdistus on selkeämpi 5.1:llä (*Kolme liikettä yhdessä prosessissa*) kuin 5.2:lla (*Etsi nuo kolme jonkun muun prosessista*), koska AT2 odottaa alkuperäistä kirjoitusta. **Oletusarvo:** Rasmus toimittaa 5.1:n yksittäisenä PAKOLLISENA tehtävänä; 5.2 pidetään varastossa.
3. **AND / OR — pidä arkilohkossa vai työnnä syventävään?** Yhdistetyt ehdot ovat hyödyllisiä mutta riskeeraavat O14:n ahdistamisen. **Oletusarvo:** pidä AND / OR -aliosio `self-study.md`:n oppitunti 14:ssä merkittynä *syventäväksi lukemistoksi* (3–6 lausetta enintään) ja ÄLÄ sisällytä yhdistettyjä ehtoja must-do minimumiin.
4. **Laskurit toistossa — sisällytä vai ohita?** Laskurit ovat houkuttelevia, koska *"do this 5 times"* on intuitiivinen, mutta niiden esittely flirttaa muuttujien sijoittamisen kanssa ja on lähempänä viikkoa 6. **Oletusarvo:** Rasmus saa sisällyttää yhden lyhyen kappaleen `self-study.md`:n oppitunti 15:een kehystettynä *"sometimes the stop is a count — this is a kind of for-each over the numbers 1 to N"*. Ei muuttujasyntaksia.
5. **`### If you are doing this alone` — vaadittu tehtävässä 5.1?** Tehtävä 5.1 ei oleta paria. Toimeksianto sanoo otsikon olevan vaadittu *siellä, missä kumppani oletetaan*. **Oletusarvo:** Rasmus saa jättää `### If you are doing this alone` pois tehtävästä 5.1, TAI sisällyttää 1 lauseen "voit valita prosessin, jota teet täysin yksin" -huomautuksen. Tehtävät 5.2, 5.3, 5.5 eivät myöskään vaadi sitä; tehtävä 5.4 ei myöskään. Jos Rasmus toimittaa parin pohjaisen variantin jostakin tehtävästä, otsikko tulee pakolliseksi siellä.
6. **Mermaid vs. ASCII päätöspuuksi kalvoille.** Kalvojen pitää renderöityä tavallisessa Markdownissa. **Oletusarvo:** Rasmus käyttää **ASCII-puita** tai **kuvattuja haaroja** (vain tekstinä), ei Mermaid-syntaksia. Käsinpiirretyt puut pysyvät opiskelijan vihossa, eivät kalvoilla.
7. **Pohdintakehotteiden määrä `self-study.md`:ssä.** Tämä suunnitelma vaatii ≥5 kolmen oppitunnin yli (≥1 per oppitunti). **Oletusarvo:** Rasmus toimittaa 5–6 kehotetta, vähintään 2 O14:ssä (tihein oppitunti).
8. **Sana "silmukka".** *Silmukka* on hyödyllinen lyhenne *toistolle*, mutta toimeksianto lukitsee *toiston* kanoniseksi substantiiviksi. **Oletusarvo:** Rasmus käyttää *toistoa* ensisijaisena nimenä ja saa käyttää *silmukkaa* kerran `vocabulary.md`:ssä merkittynä synonyymiksi, plus inline `self-study.md`:n oppitunti 15:ssä ensimmäisellä kerralla muodossa *"repetition (also called a loop in everyday tech speak)"*. Sen jälkeen *toisto* läpi.
9. **Keskeisen viestin pituus.** Toimeksiannon täysi keskeinen viesti on kaksi lausetta (*"Almost any process can be described with three building blocks: sequence, condition, and repetition. Once you can name them in everyday tasks, you have the skeleton of every program."*). **Oletusarvo:** ensimmäinen lause on *sananmukainen* kalvo-/self-study-vaatimus; toinen lause on suositeltu mutta ei pakollinen.
10. **AT2-kehystys `### Keep your notes`:ssa.** Jotkin viikon 1 julkaisun tehtävät viittaavat AT1:een ilmauksella *"viikon 2 loppu"*. Viikolla 5 vastine on *"viikon 5 loppu / viikon 6 aikana"*. **Oletusarvo:** Rasmus käyttää täsmällistä ilmausta *"AT2 lands at the end of Week 5 / during Week 6"* jokaisessa `### Keep your notes` -lohkossa.
11. **Pinojen sisältö luokitteluleikille.** Tämä suunnitelma tarjoaa siemenlauseet molemmille pinoille tiedostossa `in-class-tasks.md`. **Oletusarvo:** Rasmus toimittaa täsmälleen siemenlistat Aktiviteetti A:ssa tai laajentaa niitä 2–4:llä kumpaakin, mutta ei lyhennä alle 10:n per pino.
12. **30–50 %:n sääntö per oppitunti.** Tämä suunnitelma budjetoi 30 / 25 / 30 minuuttia itsenäistä työtä O13:ssa, O14:ssä, O15:ssä (33 % / 28 % / 33 % 90 minuutista). O14 on alarajalla, koska luokassa pidettävä luokitteluleikki syö 25 minuuttia; Wilhelm hyväksyy 25 minuuttia 27–45 min alueeseen *vain jos* itsenäisen työn lohko on oikeasti itsenäistä. **Oletusarvo:** Rasmus tiivistää O14:n itsenäisen työn lohkon **27–30 min:iin** pysyäkseen turvallisesti säännön sisällä, lyhentäen luentoa tai purkua tarvittaessa.
