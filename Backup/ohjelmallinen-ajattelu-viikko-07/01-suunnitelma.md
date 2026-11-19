# Ohjelmallinen ajattelu — Viikon 7 suunnitelma (Sune, Portti #1)

Kurssi: Ohjelmallinen ajattelu (englanti)
Kohderyhmä: 1. vuoden ammatillisen ICT:n opiskelijat, ~15–17 v., joilla on jo kuuden viikon ohjelmallisen ajattelun pohja (viikot 1–6).
Viikko 7 8-viikkoisen kurssin kaaressa: **silta koodiin.** Kuuden viikon pseudokoodi, sekvenssi, ehto, toisto, käsiajo ja pilkkominen kohtaavat nyt oikean syntaksin — kahdella kielellä, JavaScriptillä ja C#:lla, rinta rinnan.
Putken laajuus tällä ajolla: Sune tuottaa tämän viikon 7 suunnitelman; Rasmus rakentaa viikon 7 kanonisessa week-XX-rakenteessa (kaksikielisellä tehtävätiedostojaolla); Linnea ja Wilhelm auditoivat viikon 7; Alfred paketoi **pelkkä-Markdown**-julkaisun viikolle 7 (ei PDF:ää, ei PPTX:ää).

---

## Suunnitelma

### Mihin viikko 7 sijoittuu kurssin kaaressa

Kurssin keskeinen kysymys — *"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"* — on saanut käsitteellisen vastauksen jo viikolta 1. Opiskelijat tietävät jo, että tietokone noudattaa ohjeita sananmukaisesti, että monitulkintaisuus on ohjeen ominaisuus, että algoritmi on arkinen nimi selkeälle sananmukaisten vaiheiden sarjalle ja että vuokaaviot, abstraktio, vaihtoehtoiset ratkaisut, logiikkarakenteet (sekvenssi, ehto, toisto) ja pseudokoodi käsiajolla ovat työkaluja.

Viikko 7 vie tämän käsitteellisen koneiston vihdoin oikean tulkin eteen. Viikko vastaa: *"Jos tietokone ei sananmukaisesti voi arvata, miltä näyttää ohje, jonka se osaa oikeasti suorittaa?"* Vastaus on **syntaksi** — pieni, tiukka, täsmällinen tapa kirjoittaa ohjeita. Viikko esittelee kaksi konkreettista kieltä, JavaScriptin ja C#:n, rinnakkain, jotta opiskelijat näkevät, että *ajattelu on siirrettävissä*, mutta *syntaksi on se sopimus, jonka teet yhden tietyn tulkin kanssa*. Oppitunti 19 pysyy kieliriippumattomana (mikä on ohjelmointikieli, miksi kaksi kieltä, mitä syntaksi edes tarkoittaa). Oppitunnit 20 ja 21 esittelevät konkreettisen syntaksin molemmilla kielillä rinta rinnan: ensin tulosteen ja muuttujat (O20), sitten ehdot (O21).

Ohjelmointi käsitellään viimeisenä kerroksena; ohjelmallinen ajattelu pysyy kerroksena, jota kurssi harjoittaa. AT3, joka julkaistaan ensi viikolla, pyytää opiskelijoita kääntämään palan omaa viikon 6 pseudokoodiaan pieneksi ohjelmaksi sillä kielellä, jonka he valitsevat tällä viikolla. Viikko 7 on silta.

### Viikon 7 teemalauseke

Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone osaa noudattaa niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain se syntaksi, jolla se kirjoitetaan. JavaScript ja C# ovat kaksi tällaista kieltä — eri pinta, sama taustalla oleva ajattelu. Viikon 7 lopussa opiskelija osaa suorittaa ensimmäisen käskyn **valitsemallaan kielellä** (joko JavaScriptin selainkonsolissa tai C#:n online-.NET-ympäristössä), esitellä muuttujan, tehdä yksinkertaisen vertailun ja kirjoittaa ensimmäisen `if/else`-rakenteen. Ei IDE-asennusta, ei debuggeria, ei testiframeworkkia.

### O19–O21 erittely viikolle 7

#### Oppitunti 19 — Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt ja ohjelmointikielten rooli

- **Oppimistavoitteet** (vain Ymmärtäminen tässä vaiheessa):
  - (a) **Määrittele** *ohjelmointikieli*, *syntaksi*, *käsky*, *tulkki* / *kääntäjä* omin sanoin (yhden lauseen epämuodollinen määritelmä riittää; *kääntäjä/tulkki*-jako nimetään, ei syväluodata).
  - (b) **Selitä** miksi ohjelmointikieli tarvitaan kun pseudokoodi on jo täsmällistä — eli että *oikea* tietokone ei osaa lukea englanninkielistä pseudokoodia.
  - (c) **Tunnista** että sama algoritmi voidaan kirjoittaa eri kielillä ja silti se tarkoittaa samaa.
  - (d) **Nimeä** kaksi todellista ohjelmointikieltä (JavaScript, C#) ja yksi paikka, jossa kumpaakin tyypillisesti käytetään (JS = selain; C# = .NET / työpöytä / pelit / Unity).
- **Kielistatus:** **kieliriippumaton.** Opiskelijalta ei vaadita toimivaa koodia. Side-by-side-esimerkkejä voidaan *näyttää* kalvoilla, mutta oppitunti puhuu syntaksista käsitteenä, ei JS- tai C#-kohtaisista säännöistä.
- **Keskeinen sanasto ennakkona:** ohjelmointikieli, syntaksi, käsky, tulkki (epämuodollinen), kääntäjä (epämuodollinen), virheilmoitus (ennakko), muuttuja (ennakko).
- **Keskeinen viesti (yksi lause):** Pseudokoodi on tarpeeksi täsmällistä ihmiselle noudatettavaksi; ohjelmointikieli on tarpeeksi täsmällistä *sananmukaiselle* tietokoneelle noudatettavaksi.

#### Oppitunti 20 — Ensimmäiset käskyt: tuloste, arvot, muuttujat, yksinkertaiset laskut (JS:llä ja C#:lla)

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Suorita** ensimmäinen ohjelma, joka tulostaa tekstiä konsoliin — `console.log("...")` JavaScriptissä, `Console.WriteLine("...")` C#:ssa.
  - (b) **Esittele** muuttuja ja **anna** sille arvo — `let name = "..."` / `let age = 16` JavaScriptissä, `string name = "..."` / `int age = 16` C#:ssa (nimeämme *tyypin* C#:ssa, mutta emme rämmi tyyppijärjestelmässä).
  - (c) **Tulosta** muuttujan arvo, mukaan lukien yhdistämällä (JS: `+` tai template literal -merkkijonot; C#: `+` tai string interpolation `$"..."` — Rasmus valitsee **yhden** tyylin per kieli ja pitäytyy siinä).
  - (d) **Suorita** yksinkertainen laskutoimitus (esim. vuosia täysi-ikäisyyteen, kokonaishinta) ja tulosta tulos.
  - (e) **Tunnista** että *ajattelu* (sekvenssi: lue, laske, tulosta) on sama molemmilla kielillä.
- **Kielistatus:** **kaksikielinen.** Jokainen käsite esitetään kahdesti, rinta rinnan.
- **Keskeinen sanasto lisätty:** konsoli, tuloste, muuttuja, arvo, sijoitus, merkkijono, numero/int, yhdistäminen, template literal / string interpolation (epämuodollinen).
- **Keskeinen viesti (yksi lause):** Ohjelma on sananmukaisten käskyjen sarja — ja "tulosta arvo konsoliin" on yksinkertaisin tällainen käsky kummallakin kielellä.

#### Oppitunti 21 — Ehdot koodissa: if, else, vertailut (JS:llä ja C#:lla)

- **Oppimistavoitteet** (Ymmärtäminen + Soveltaminen):
  - (a) **Kirjoita** vertailulauseke (`age >= 18`, `password.length >= 8`) molemmilla kielillä ja tunnista, että vertailuoperaattorit ovat olennaisesti identtiset JS:ssä ja C#:ssa.
  - (b) **Kirjoita** ensimmäinen `if/else`-lohko, joka tulostaa toisen kahdesta viestistä riippuen muuttujasta.
  - (c) **Kuvaa** pala viikon 6 pseudokoodia (`IF age >= 18 THEN ... ELSE ...`) koodiksi valitsemallaan kielellä.
  - (d) **Ennusta** pienen `if/else`-ohjelman tuloste **ennen sen ajamista**, sitten aja ja tarkista (yhteys viikon 6 käsiajoon).
- **Kielistatus:** **kaksikielinen.** Ehdot esitetään molemmilla kielillä side-by-side-katkelmilla.
- **Keskeinen sanasto lisätty:** ehto, vertailuoperaattori (`==`, `>=`, `<=`, `>`, `<`, `!=`), boolean (epämuodollinen), lohko `{ ... }`, `if`, `else`.
- **Keskeinen viesti (yksi lause):** `if/else` on sama päätös, jota olet kirjoittanut pseudokoodissa kaksi viikkoa — vain välimerkit ovat erilaiset.

### Viikko 7 — must-do-minimi vs. syventävä

**Must-do-minimi (jokaisen opiskelijan on osattava viikon 7 jälkeen):**
- Selittää selkokielisesti, miksi ohjelmointikieltä ylipäätään tarvitaan (eikä pelkkä pseudokoodi riitä).
- Nimetä JavaScript ja C# kahdeksi todelliseksi ohjelmointikieleksi ja yksi tyypillinen käyttötarkoitus kummallekin.
- Avata **selainkonsoli** (JS-polku) **TAI** online-C#-ympäristö kuten .NET Fiddle, sharplab.io tai C#-yhteensopiva Replit (C#-polku) — opiskelija valitsee yhden.
- Valitsemallaan kielellä suorittaa ohjelma, joka:
  - tulostaa tervehdyksen,
  - esittelee muuttujan ja tulostaa sen arvon,
  - käyttää `if/else`-rakennetta tulostaakseen toisen kahdesta viestistä muuttujan arvon mukaan.
- Tallentaa koodi (liimaa viikon muistiinpanoihin) — koodia käytetään uudelleen AT3:ssa ensi viikolla.

**Syventävä (valinnainen, ei vaadita AT3:lle):**
- Tee **sama** tehtävä *toisella* kielellä (sillä, jota et valinnut) — tunne syntaksiero, kun ajattelu on jo tehty.
- Käännä yksi pala omaa viikon 6 pseudokoodia pieneksi ohjelmaksi valitsemallasi kielellä (käsiajosta suoritukseen — tämä on myös AT3:n siemen).
- Yhdistä kaksi vertailua operaattoreilla `&&` / `||` (nimetään epämuodollisesti; syvemmät logiikkaoperaattorit tulivat jo viikolla 5, joten tämä on vain koodimuoto sille, minkä jo osaat).
- Lue oikea virheilmoitus: riko ohjelma tarkoituksella (unohda puolipiste C#:ssa, unohda lainausmerkki JS:ssä) ja kirjoita ylös, mitä tulkki / kääntäjä sanoi.

### Miksi kaksikielinen?

Kolme syytä, tärkeysjärjestyksessä:

1. **Ammatillinen realismi.** 1. vuoden ICT-opiskelijat Suomessa jakautuvat web-painotteisiin (JS/TS) ja .NET-painotteisiin (C#) polkuihin toisena vuotenaan. Ohjelmallisen ajattelun ankkurointi *molempiin* kieliin ensikontaktista vapauttaa viikon 7 ennakkoasettamasta yhtä polkua.
2. **Siirrettävyysviesti.** *Saman algoritmin* näyttäminen kahdella kielellä on vahvin mahdollinen perustelu sille, että *ajattelu on se asia* ja syntaksi on sopimus. Yksikielinen viikko 7 hiljaa ehdottaisi, että ohjelmointi = JS (tai = C#).
3. **AT3-reiluus.** AT3 viikolla 8 pyytää opiskelijaa kääntämään oman pseudokoodinsa pieneksi ohjelmaksi. Opiskelijan tulee valita kieli, jota hän mieluiten käyttää — ei sitä, jota me hänelle opetimme.

### Kalvostrategia (Sunen päätös)

`slides.md` on **yksi setti**. Setti sekoittaa kolme kalvotyyppiä:

- **Riippumattomat kalvot** (O19:lle ja O20/O21:n läpileikkaaville yhteenvetokalvoille) — ei JS- tai C#-spesifejä.
- **Side-by-side-syntaksikalvot** (O20:n ja O21:n päämuoto) — yksi kalvo, kaksi saraketta tai kaksi koodilohkoa: JS vasemmalla/yllä, C# oikealla/alla, **sama ajattelu** merkittynä niiden yläpuolelle.
- **Yksikieliset demokalvot** (säästeliäästi) — kun yhden kielen joku pieni mekaniikka tarvitsee näyttämistä (esim. selainkonsolin avaaminen, .NET Fiddlen avaaminen). Yksi tällainen kalvo per kieli per mekaniikka, selvästi merkittynä.

Rasmus voi lisätä **enintään kaksi täydentävää settiä** (`slides-l<n>-<aihe>.md`, 4–8 kalvoa kukin), jos luentosegmentti aidosti tarvitsee syvempää materiaalia. Vahvat ehdokkaat alla briefingissä.

### Miten nämä kolme oppituntia sopivat yhteen

O19 (syntaksin käsite, riippumaton) → O20 (ensimmäinen konkreettinen syntaksi, molemmat kielet, tuloste + muuttujat) → O21 (ensimmäinen konkreettinen syntaksi tärkeimmälle ohjausrakenteelle, molemmat kielet, `if/else`). O21 päättyy kuvaamalla viikon 6 pseudokoodikatkelma todelliseksi koodiksi molemmilla kielillä — tämä on eksplisiittinen luovutus AT3:lle viikolle 8.

---

## Rajaukset

**Viikon 7 ulkopuolella:**

- **Ei IDE-asennusta.** Ei VS Code -asennusta, ei Visual Studio -asennusta, ei Node.js-asennusta, ei .NET SDK -asennusta, ei `dotnet new`:tä. Suoritusalustat ovat:
  - **JavaScript:** selaimen DevTools-konsoli (Chrome, Firefox, Edge, Safari — mikä tahansa).
  - **C#:** online-C#-ympäristö — **.NET Fiddle** (oletussuositus), **sharplab.io** tai C#-yhteensopiva Replit. Ei tilin luomista .NET Fiddlessä eikä sharplab.io:ssa.
- **Ei debuggeria.** Ei breakpointteja, ei step-throughta. "Tulosta konsoliin ja lue tuloste" on viikon ainoa debugger-työkalu.
- **Ei testiframeworkkeja.** Ei jest, mocha, vitest, pytest, xUnit, NUnit, MSTest. Ei mainita missään tiedostossa. Kova fail.
- **Ei tyyppien syväsukellusta C#:ssa.** Sana *tyyppi* nimetään (`int`, `string`) ja sitä käytetään; tyyppijärjestelmää ei selitetä. Emme käsittele `var` vs `int`:iä, arvotyyppejä vs referenssityyppejä, nullable-referenssejä, geneeristä, mitään tällaista. C# esitetään muodossa "C# sattuu haluamaan, että nimeät tyypin — se on pieni ylimääräinen sana, ei eri ajattelutapa."
- **Ei puolipiste-kurinpidon poraamista.** JS:n (useimmissa tapauksissa valinnainen, käytössä konvention vuoksi) ja C#:n (pakollinen) ero puolipisteen suhteen *mainitaan kerran* eikä porata.
- **Ei async, ei luokkia, ei metodeja (paitsi `Console.WriteLine`), ei LINQ, ei DOM, ei fetch, ei Node-moduuleja, ei NuGet-paketteja.** Vain top-level-koodi.
- **Ei selainframeworkkeja** (React, Vue, Svelte). JavaScript tarkoittaa DevTools-konsolia.
- **Ei kolmannen osapuolen C#-työkaluja** isäntähostatun online-sandboxin lisäksi.
- **Ei PDF:ää, ei PPTX-renderöintiä** tällä putkiajolla. Vain Markdown-julkaisu.
- **Ei PowerPoint-viittauksia** missään tiedostossa. Rasmus kirjoittaa vain `slides.md`:n (ja valinnaisen `slides-l<n>-*.md`:n).
- **Ei Bloomin tasoja yli Soveltamisen.** Ei Analysointia, Arvioimista tai Luomista viikon 7 tavoitteissa. AT3 (Luomisen sävyinen) tulee ensi viikolla.
- **Ei `(AI-resilient)`-merkkiä** missään oppijalle näkyvässä tiedostossa. AI-kestävyys on ominaisuus, jonka Linnea auditoi; ei merkki, jonka opiskelijat näkevät.

**Putken laajuus tällä ajolla:**

- Sune tuottaa tämän viikon 7 suunnitelman (jota juuri luet).
- Rasmus rakentaa **vain viikon 7** kanonisessa week-XX-rakenteessa mutta **kaksikielisellä tehtävätiedostojaolla** (`student-tasks-js.md` + `student-tasks-csharp.md` yhden `student-tasks.md`:n sijaan; valinnainen ohut indeksi `student-tasks.md` on sallittu mutta ei vaadittu).
- Linnea ja Wilhelm auditoivat vain viikon 7.
- Alfred paketoi viikon 7 julkaisun Markdownina.

---

## Hyväksymiskriteerit

Wilhelm tarkistaa viikon 7 paketin seuraavia konkreettisia, tarkistettavissa olevia kriteereitä vasten.

### Rakenteellinen — tiedostot ja kansiot

1. **Kaikki kanoniset tiedostot mukana**, täsmälleen näillä tiedostonimillä (case-sensitive, lowercase, kebab-case):
   - `student/week-07/overview.md`
   - `student/week-07/self-study.md`
   - `student/week-07/student-tasks-js.md`
   - `student/week-07/student-tasks-csharp.md`
   - `student/week-07/vocabulary.md`
   - `student/week-07/slides.md`
   - `teacher/week-07/teacher-materials.md`
   - `teacher/week-07/in-class-tasks.md`
2. **Valinnainen kahdeksas opiskelijatiedosto**: ohut `student/week-07/student-tasks.md`, joka toimii indeksinä kahteen kielitiedostoon. Sallittu mutta ei vaadittu. Jos mukana, sen on oltava **≤200 sanaa** eikä se saa tuoda omaa tehtävänumerointia.
3. **Ei `student-tasks.md`:tä, joka sisältää tehtäväsisältöä.** Kaikki tehtävät asuvat kahdessa kielikohtaisessa tiedostossa.
4. **Ei ylimääräisiä tiedostoja kanonisen setin lisäksi paitsi enintään kaksi valinnaista täydennyssettiä** nimellä `slides-l<n>-<aihe>.md` kansiossa `student/week-07/`. `media/`-alikansio sallitaan vain, jos kalvo tai itseopiskelu eksplisiittisesti viittaa sen sisältämään kuvaan.
5. **Ei `slides.pptx`:ää, ei `deck.md`:tä, ei `slides.key`:tä, ei Reveal.js-HTML:ää** missään. Kova fail jos löytyy.

### Määrä (järkevyystarkistuksen haarukat, ei kovia rajoja)

6. `overview.md`: **200–400 sanaa**.
7. `self-study.md`: **2400–4000 sanaa** yhteensä, kattaen kaikki kolme oppituntia.
8. `student-tasks-js.md`: **600–1400 sanaa** yhteensä. **1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää.**
9. `student-tasks-csharp.md`: **600–1400 sanaa** yhteensä. **1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää.**
10. Kahdessa kielikohtaisessa tehtävätiedostossa on **sama määrä PAKOLLISIA tehtäviä ja sama määrä SYVENTÄVIÄ tehtäviä** kuin toisessa.
11. Valinnainen `student-tasks.md`: **≤200 sanaa** jos mukana.
12. `vocabulary.md`: **10–18 termiä.**
13. `slides.md`: **12–18 kalvoa**, erotettu `---`:llä omalla rivillä, jokainen kalvo alkaa H1- (`#`) tai H2- (`##`) otsikolla ja sisältää minimaalisen tukisisällön (3–5 lyhyttä bullet-pointtia tai 1–2 lyhyttä lausetta). Koodikatkelmat kalvoilla ovat ≤6 riviä ja fenced-koodilohkojen sisällä.
14. `teacher-materials.md`: **2400–4200 sanaa.** Sisältää **3 × 90 minuutin oppituntisuunnitelmaa** (O19, O20, O21), kunkin aikajaot summana 90.
15. `in-class-tasks.md`: **400–1200 sanaa.** Sisältää **≥1 PAKOLLISEN opettajavetoisen tuntiharjoituksen.**

### Vaaditut H2-osiot per tiedosto

16. `overview.md`:n on sisällettävä (tässä järjestyksessä):
    - `## Viikon 7 teema`
    - `## Mitä osaat viikon lopussa`
    - `## Must-do-minimi vs. syventävä`
    - `## Miten nämä kolme oppituntia sopivat yhteen`
    - `## Valitse kieli`
17. `self-study.md`:n on sisällettävä:
    - `# <Viikon otsikko>` (Rasmuksen kutsu).
    - `## Johdanto` — asettaa viikon, nimeää kurssin keskeisen kysymyksen uudelleen (sananmukaisesti kerran) ja nimeää kaksikielisen idean.
    - `## Oppitunti 19 — Miksi ohjelmointikieliä on olemassa` *(kieliriippumaton; merkitty niin eksplisiittisesti).*
    - `## Oppitunti 20 — Ensimmäiset käskyt: tuloste, arvot, muuttujat` *(kaksikielinen; side-by-side-katkelmat JS:llä ja C#:lla).*
    - `## Oppitunti 21 — Ehdot koodissa: if, else, vertailut` *(kaksikielinen; side-by-side-katkelmat JS:llä ja C#:lla).*
    - `## Kielen valinta AT3:lle` — lyhyt päätösosio, joka ennakoi AT3:a viikolla 8 ja kertoo opiskelijalle eksplisiittisesti, että tällä viikolla valittu kieli on AT3:ssa käytettävä kieli.
    - `## Yhteenveto ja mitä tulee seuraavaksi`.
    - **Vähintään 4 `> **Pysähdy hetkeksi:**`-reflektiokehotetta** läpi kolmen oppituntiosion (≥1 per oppitunti).
18. `student-tasks-js.md`:n on sisällettävä:
    - `## Yleiskatsaus tämän viikon JavaScript-tehtäviin`
    - 1–2 H2-tehtäväotsikkoa etuliitteellä `🟢 PAKOLLINEN —` ja 2–3 etuliitteellä `🟣 SYVENTÄVÄ —`. Jokaisen PAKOLLISEN tehtävän otsikkoon liitetään `(JS)` jälkiliite, jotta se on yksiselitteinen luettaessa erillään.
    - `### Miten avaat JavaScript-konsolin` -lohko jossain lähellä alkua (yksi pieni kappale per yleinen selain tai yksi universaali resepti — Rasmuksen valinta).
    - Jokainen tehtävä päättyy `### Pidä muistiinpanot` -lohkoon, joka mainitsee **AT3 saapuu viikon 8 lopussa** ja että näiden tehtävien koodia käytetään uudelleen.
    - Jokainen tehtävä, joka olettaa parin / seuraajan / testaajan, sisältää `### Jos teet tämän yksin` -alaluvun konkreettisella vaihtoehdolla (24 h tauko, video itsestä, eri selain, luokan chat).
19. `student-tasks-csharp.md`:n on sisällettävä rinnakkainen rakenne `student-tasks-js.md`:lle:
    - `## Yleiskatsaus tämän viikon C#-tehtäviin`
    - 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ H2-tehtäväotsikkoa. PAKOLLISTEN tehtävien otsikoissa `(C#)`-jälkiliite.
    - `### Miten avaat online-C#-ympäristön` -lohko lähellä alkua (suosittele oletuksena .NET Fiddleä; mainitse sharplab.io vaihtoehtona; mainitse Replit kolmantena).
    - `### Pidä muistiinpanot` -lohkot, jotka osoittavat AT3:een.
    - `### Jos teet tämän yksin` -alaluvut siellä, missä paria oletetaan.
20. **Rinnakkaisuus**: jokaista 🟢 PAKOLLISTA tehtävää kohden `student-tasks-js.md`:ssä on vastaava 🟢 PAKOLLINEN tehtävä `student-tasks-csharp.md`:ssä, joka opettaa **saman käsitteen**. Sama SYVENTÄVÄLLE. Kaksi tehtävätiedostoa muodostavat pareja.
21. `vocabulary.md`:n on sisällettävä yksi H2 `## Viikon 7 sanasto`, sitten jokainen termi H3:na tai lihavoituna määritelmälistassa. Vähintään **yksi termi merkitty "eteenpäin katsovaksi"** (esim. *silmukka* tai *virheilmoitus* viikolle 8). Määritelmät seuraaville vaaditaan: `console`, `command`, `syntax`, `variable`, `condition`, `if/else`, `comparison operator`, `string`, `int / number`, ja yksi kummallekin `console.log` ja `Console.WriteLine`.
22. `slides.md`:n on:
    - Aloitettava otsikkokalvolla.
    - Sisällettävä vähintään yksi kalvo, joka näyttää kurssin keskeisen kysymyksen sananmukaisesti (viikolta 1 uudelleenvierailtuna).
    - Sisällettävä vähintään yksi **riippumaton** kalvo O19:lle ("ohjelmointikielet ovat olemassa, koska…").
    - Sisällettävä vähintään **kolme side-by-side JS/C#-kalvoa** O20:n ja O21:n yhdistettynä, molemmat kielet samalla kalvolla.
    - Sisällettävä vähintään yksi kalvo, joka näyttää **miten selainkonsoli avataan** ja vähintään yksi kalvo, joka näyttää **miten online-C#-ympäristö avataan** (.NET Fiddle oletuksena).
    - Käyttää `---`:tä omalla rivillä kalvojen välissä.
    - Ei sisällettävä upotettuja `.pptx`-viittauksia eikä luennoitsijamuistiinpanosyntaksia, joka olettaa tiettyä renderöijää.
23. `teacher-materials.md`:n on sisällettävä (tässä järjestyksessä):
    - `## Viikon 7 oppimistavoitteet (kuvattuna Bloomiin)`
    - `## Yleisiä virhekäsityksiä viikolla 7` — **vähintään 6 läpi viikon** (≥2 per oppitunti), jokainen `Korjaus:`-rivillä. Vähintään kahden virhekäsityksen on koskettava **JS-vs-C#-valintaa** (esim. "C# on JS:ää vaikeampi", "JS ei ole oikea kieli, koska se ajetaan selaimessa").
    - `## Oppitunti 19 — 90 min suunnitelma`, `## Oppitunti 20 — 90 min suunnitelma`, `## Oppitunti 21 — 90 min suunnitelma` — kukin konkreettisilla aikajaoilla summana 90, kukin allokoiden **30–50 % itsenäiseen opiskelijatyöhön** (kriteeri #25) ja kukin sisältäen `### Kalvovinkit`-alaluvun, joka nimeää kalvot käytettäväksi järjestyksessä oppitunnin aikana.
    - `## Fasilitointivinkit` — lyhyt läpileikkaava lohko. On eksplisiittisesti kerrottava opettajalle: "IDE-asennusta ei vaadita; .NET Fiddle / sharplab.io ja selaimen DevTools-konsoli ovat ainoat suoritusalustat."
    - `## Vastauksia yleisiin opiskelijan kysymyksiin` — vähintään 5 läpi viikon, mukaan lukien: *"Minkä kielen valitsisin?"*, *"Onko toinen kielistä toista vaikeampi?"*, *"Riippuuko AT3:n arvosana kielestäni?"*
    - `## Formatiivisen arvioinnin vinkit`.
24. `in-class-tasks.md`:n on sisällettävä:
    - `## Yleiskatsaus`
    - Vähintään 1 H2-tehtävä merkittynä **PAKOLLINEN**, joka vaatii opettajavetoisen luokkavuorovaikutuksen. PAKOLLISEN tehtävän on toimittava sekä JS- että C#-opiskelijoille samassa huoneessa (eli se ei saa olettaa, että koko luokka valitsi yhden kielen).
    - Ristiviittaus takaisin `teacher-materials.md`:hen, jotta opettaja tietää slotin.

### Pedagogiset säännöt

25. **30–50 % sääntö**: `teacher-materials.md`:ssä, jokaisessa kolmessa 90 min oppituntisuunnitelmassa, näkyvästi *itsenäiseksi opiskelijatyöksi* merkityt aikalohkot (ei luento, ei pari, ei ryhmä, ei debrief) summautuvat **27–45 minuuttiin** 90:stä. Wilhelm tarkistaa aritmeettisesti.
26. **Bloom-katto**: viikon 7 tavoitteet käyttävät vain Ymmärtämisen ja Soveltamisen verbejä (*selitä, tunnista, nimeä, määrittele, suorita, esittele, anna, tulosta, kirjoita, ennusta, kuvaa*). **Kielletyt verbit** viikon 7 tavoitteissa: *analysoi, arvioi, suunnittele, luo, rakenna, debuggaa, refaktoroi, optimoi*.
27. **Keskeinen kysymys (kurssitaso)**: *"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"* esiintyy **sananmukaisesti** vähintään kerran `self-study.md`:ssä (Johdannossa tai Yhteenvedossa) ja vähintään yhdellä kalvolla `slides.md`:ssä.
28. **Kieliriippumaton O19**: `self-study.md`:ssä ja `slides.md`:ssä oppitunnin 19 osio / kalvot eivät saa sisältää JS-spesifejä eikä C#-spesifejä toimivaa koodia. Kahden kielen nimeäminen on ok; sanominen "JavaScriptissä kirjoittaisit `console.log(...)`" on ok *eteenpäin osoittavana viittauksena*, mutta O19:n *harjoitukset ja selitykset* eivät saa riippua JS- tai C#-syntaksin osaamisesta. Wilhelm spot-tarkistaa.
29. **Kaksikielinen tasapuolisuus** O20:ssa ja O21:ssä: jokainen käsite, joka esitetään yhdelle kielelle, näytetään myös toiselle, samassa osiossa, vertailukelpoisella syvyydellä. Wilhelm spot-tarkistaa `self-study.md`:n O20- ja O21-osiot tämän rinnakkaisuuden vuoksi.
30. **Ei IDE-asennusta mainittuna missään.** Ei `node`, ei `npm`, ei `nvm`, ei `dotnet`, ei `dotnet new`, ei `dotnet run`, ei Visual Studio, ei VS Code, ei JetBrains Rider. Vain "selaimen DevTools-konsoli" ja "online-C#-ympäristö (.NET Fiddle / sharplab.io / Replit)". Wilhelm grep-tarkistaa.
31. **Ei testiframeworkkeja** missään tiedostossa (`jest`, `mocha`, `vitest`, `pytest`, `xunit`, `nunit`, `mstest`). Wilhelm grep-tarkistaa.
32. **Ei `(AI-resilient)`-merkkiä** missään oppijalle näkyvässä tiedostossa. Wilhelm grep-tarkistaa.
33. **"must-do-minimi"** on sanamuoto `overview.md`:ssä ja kahdessa kielitehtävätiedostossa (ei "pakollinen minimi"). Wilhelm grep-tarkistaa.
34. **AT3-viittaus** jokaisen tehtävän `### Pidä muistiinpanot` -lohkossa sekä `student-tasks-js.md`:ssä että `student-tasks-csharp.md`:ssä — nimetään AT3 (ei AT1) eksplisiittisesti, koska viikko 7 on silta AT3:een.
35. **Tiedostojen välinen yhtenäisyys**:
    - Tehtävätunnisteet `slides.md`:n "Tehtävät tällä viikolla" -kalvon listassa, jossa molemmat kielitiedostot selkeästi.
    - Tuntiaktiviteetit, joihin viitataan `teacher-materials.md`:n oppituntisuunnitelmista, ovat olemassa `in-class-tasks.md`:ssä.
    - Sanaston termit, joita käytetään `self-study.md`:ssä, `slides.md`:ssä ja tehtävätiedostoissa, kaikki esiintyvät `vocabulary.md`:ssä.

### Tehtävät — AI-kestävyys

36. Vähintään **yksi PAKOLLINEN tehtävä jokaisessa kielitiedostossa on AI-kestävä rakenteeltaan**, mikä tarkoittaa, että se vaatii opiskelijan oman konkreettisen kontekstin (oman nimensä, oman ikänsä, oman valitsemansa viikon 6 pseudokoodikatkelman, kuvakaappauksen *omasta* konsolitulosteestaan, tarran tulkkinsa täsmällisestä virheilmoituksesta) ja tuottaa havaittavan artefaktin, jonka opettaja voi spot-tarkistaa LLM-transkriptiä vasten. AI-kestävyys on ominaisuus; `(AI-resilient)`-merkki on kielletty tiedostossa.
37. Jos SYVENTÄVÄ tehtävä käyttää LLM:ää sparrauskumppanina (esim. "pyydä LLM:ää kääntämään JS-koodisi C#:lle ja tarkista se"), sen on sisällettävä fenced-koodilohko esimerkkikehotteella ja eksplisiittinen ohje, ettei LLM:n tulostetta saa hyväksyä sellaisenaan — opiskelijan on ajettava koodi itse ja raportoitava mitä todella tapahtui.

### Tuntitehtävät

38. `in-class-tasks.md` sisältää **≥1 PAKOLLISEN opettajavetoisen tuntiharjoituksen**. Oletussuosittelu on **"konsolirelay"** (katso briefing alla). Sen on toimittava luokassa, jossa osa opiskelijoista on JS:llä ja osa C#:lla samanaikaisesti. Sen on oltava ristiviitattuna `teacher-materials.md`:stä.

### Kieli ja viimeistely

39. **Englanti läpi.** Ei suomenkielisiä sanoja missään 7+ tiedostossa paitsi selvästi välttämättömät erisnimet.
40. **Rekisteri**: `self-study.md`, kaksi tehtävätiedostoa, `overview.md`, `vocabulary.md`, `slides.md` CEFR ~B1-tasolla; `teacher-materials.md` ja `in-class-tasks.md` CEFR ~B2-tasolla.
41. **Pätevä Markdown**: jokainen fenced-koodilohko sulkeutuu, jokainen koodifence käyttää sopivaa kielitagia (` ```javascript `, ` ```csharp `, ` ```text ` tulosteelle, ` ```pseudo ` pseudokoodikaiuille), jokainen `---`-erotin `slides.md`:ssä on yksin omalla rivillään.

---

## Briefing Rasmukselle

### Läpileikkaavat muistutukset (koskevat kaikkia 7+ tiedostoa)

- **Tuo viikon 6 pseudokoodi mukaan.** Oppitunti 21 on vahvimmillaan, kun `if/else`-esimerkki on sellainen, jonka luokka on *jo kirjoittanut pseudokoodina*. Rasmus poimii yhden punaisen langan esimerkin (ehdotus: iän tarkistus — "Oletko tarpeeksi vanha pääsemään?") ja kantaa sitä pseudokoodista → JS-koodiksi → C#-koodiksi läpi viikon.
- **Side-by-side, ei "JS ensin sitten C#".** Kun näytetään molemmat kielet, laita ne samalle kalvolle, samaan osioon, samaan esimerkkiin. Älä opeta JS:ää kahden viikon edestä kalvoja ja pulttaa C#:n perään. Side-by-side-asettelu on viesti.
- **Ei IDE:tä.** Selaimen DevTools-konsoli JS:lle. .NET Fiddle (oletus), sharplab.io tai C#-yhteensopiva Replit C#:lle. Sano tämä kerran `self-study.md`:n Johdannossa, kerran `teacher-materials.md`:n Fasilitointivinkeissä ja kerran kunkin kielitehtävätiedoston alussa. Ei `npm install`:ia, ei `dotnet new`:tä.
- **Viittaa ja kunnioita viikkoa 6.** Pseudokoodi ja käsiajo ovat *jo luokan työkalu*. Käytä niitä. O21-tehtävien `### Ennusta ennen ajamista` -vaihe on käsiajo koodimuodossa.
- **"must-do-minimi"**, ei "pakollinen minimi". Sananmukainen sanamuoto `overview.md`:ssä ja tehtävätiedostoissa.
- **Ei `(AI-resilient)`-merkkiä.** Rakenna vain tehtävät niin, ettei LLM-transkripti voi korvata artefaktia.
- **Ei lauseketta "C# on JS:ää vaikeampi"** (tai päinvastoin) missään. Ne ovat eri pintoja samalle ajattelulle.
- **Ei testiframeworkkeja missään.**
- **Ei PowerPoint-viittauksia.** Rasmus toimittaa `slides.md`:n (+ valinnaisen `slides-l<n>-*.md`:n).
- **Keskeinen kurssikysymys** on esiinnyttävä sananmukaisesti vähintään kerran `self-study.md`:ssä ja vähintään kerran kalvolla: *"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"*

---

### Tiedosto 1 — `student/week-07/overview.md` (200–400 sanaa)

**Vaadittu H2-rakenne (järjestyksessä):**
1. `## Viikon 7 teema` — lyhyt kappale: keskeisen kysymyksen uudelleenvierailu, silta koodiin, kaksikielinen kehystys.
2. `## Mitä osaat viikon lopussa` — 5–7 selkokielistä "osaan"-lausetta (avaa konsoli, tulosta arvo, esittele muuttuja, kirjoita vertailu, kirjoita if/else).
3. `## Must-do-minimi vs. syventävä` — kahden bullet-listan vastakkainasettelu. Käytä täsmällistä sanamuotoa **"must-do-minimi"**.
4. `## Miten nämä kolme oppituntia sopivat yhteen` — lyhyt kappale, joka näyttää O19 (miksi kieli) → O20 (tuloste + muuttujat molemmilla) → O21 (if/else molemmilla).
5. `## Valitse kieli` — 3–6 lausetta, jotka kertovat opiskelijalle: valitse yksi tälle viikolle; voit vaihtaa missä vain; AT3 ensi viikolla käyttää valitsemaasi kieltä.

---

### Tiedosto 2 — `student/week-07/self-study.md` (2400–4000 sanaa)

**Vaadittu rakenne (järjestyksessä):**

- `# <Viikon otsikko>` — ehdotus: *"Pseudokoodista koodiin — kaksi kieltä, yksi ajattelutapa."*
- `## Johdanto`
  - Aloita lyhyellä kohtauksella: opiskelija viikolla 6 kirjoitti selkeän, käsiajetun pseudokoodin palan. Pseudokoodin lukija (ystävä, opettaja) osaa noudattaa sitä. **Oikea tietokone ei osaa.** Miksi? Koska tietokone on sananmukainen tulkitsija, eikä englanti ole sen kieli.
  - Ilmoita kurssin keskeinen kysymys sananmukaisesti kerran.
  - Nimeä viikon suunnitelma: O19 = miksi; O20 = ensimmäiset käskyt; O21 = ensimmäiset päätökset. Kaksi kieltä, rinta rinnan.
  - Yksi lause työkaluista: selainkonsoli JavaScriptille, online-ympäristö (esim. .NET Fiddle) C#:lle. **Ei asennusta tarvita.**
- `## Oppitunti 19 — Miksi ohjelmointikieliä on olemassa` *(kieliriippumaton)*
  - `### Pseudokoodista koodiin` — käsitteellinen pivot. Ajattelu on jo olemassa; puuttuu syntaksi, jonka *tietokone* hyväksyy.
  - `### Mitä syntaksi on?` — määritelmä + 2 arkielämän esimerkkiä (englannin vs. suomen sanajärjestys; kuinka automaatti hyväksyy vain oikean muotoiset kolikot) ennen 1 IT-esimerkkiä.
  - `### Tulkki ja kääntäjä (yksi kappale kustakin, epämuodollinen)` — epämuodolliset määritelmät. Nimeä JS tulkattavaksi (selain) ja C# käännettäväksi (sitten ajettavaksi). Älä rämmi JIT:n / tavukoodin kanssa.
  - `### Kaksi kieltä, yksi ajattelutapa` — nimeä JS ja C#. Yksi tyypillinen käyttö kummallekin (JS = verkkosivut, selain; C# = .NET-sovellukset, pelit, Unity, työkalut). Näytä **pieni** side-by-side-teaser, jos se auttaa, mutta varsinainen koodaus alkaa O20:ssa.
  - `### Miksi tämä on tärkeää IT-ammattilaiselle` — lyhyt ammatillinen kappale (luet enemmän koodia kuin kirjoitat; saatat vaihtaa kieliä useita kertoja urallasi; ajattelu on se siirrettävä taito).
  - 1 `> **Pysähdy hetkeksi:**` -reflektiokehote.
- `## Oppitunti 20 — Ensimmäiset käskyt: tuloste, arvot, muuttujat` *(kaksikielinen; kaikki rinta rinnan)*
  - `### Tuloste: konsolille puhuminen` — näytä miten tervehdys tulostetaan. Kaksi fenced-koodilohkoa, JS sitten C#, samalla tekstillä.
  - `### Muuttujat: arvon nimeäminen` — esittele `name`-muuttuja, esittele `age`-muuttuja, tulosta molemmat. Kaksi koodilohkoa per käsite.
  - `### Ensimmäinen laskutoimitus` — laske vuosia täysi-ikäisyyteen (`18 - age`) ja tulosta tulos. Kaksi koodilohkoa.
  - `### Tulosteen lukeminen` — viikon ainoa debugger-työkalu: lue mitä konsoli sanoo. Jos mitään ei ilmestynyt, ohjelma ei päässyt tulostukseen.
  - `### Ajattelu on sama` — sano ääneen: algoritmi on identtinen (lue arvo, laske, tulosta); sanat ja välimerkit eroavat.
  - 1–2 `> **Pysähdy hetkeksi:**` -reflektiokehotetta.
- `## Oppitunti 21 — Ehdot koodissa: if, else, vertailut` *(kaksikielinen; kaikki rinta rinnan)*
  - `### Pseudokoodin IF/ELSE:stä koodin if/else:ksi` — näytä yksi pseudokoodin pala, jonka luokka on nähnyt viikolla 6 (iän rajoitus -esimerkki), sitten sen JS-muoto, sitten sen C#-muoto.
  - `### Vertailuoperaattorit` — `==`, `!=`, `>=`, `<=`, `>`, `<`. Huomaa, että ne ovat olennaisesti identtiset JS:ssä ja C#:ssa. (Huomaa: JS:ssä on myös `===`; mainitse yhdessä lauseessa, älä rämmi.)
  - `### Yhteen koottuna — iän rajoitus -tarkistus` — työstetty side-by-side-esimerkki.
  - `### Ennusta ennen ajamista` — linkitä eksplisiittisesti viikon 6 käsiajoon. Ennusta tuloste; sitten aja; sitten vertaa.
  - 1 `> **Pysähdy hetkeksi:**` -reflektiokehote.
- `## Kielen valinta AT3:lle` — lyhyt päätösosio. Kerro opiskelijalle: AT3 saapuu ensi viikolla, käännät palan viikon 6 pseudokoodiasi koodiksi, valitset kielen. Sekä JS että C# käy; arvosana ei riipu kielestä.
- `## Yhteenveto ja mitä tulee seuraavaksi` — viikon 8 ennakko: silmukat koodissa, AT3, oikeiden virheilmoitusten lukeminen, AT3-ohjelmasi esittäminen.

**Esimerkkivalikko, johon Rasmuksen kannattaa nojata:**
- Tuloste: tulosta tervehdys; tulosta nimesi; tulosta "Hei, konsoli".
- Muuttuja: nimesi, ikäsi, lempinumerosi.
- Laskutoimitus: vuosia 18-vuotiaaksi; kokonaishinta = yksikköhinta × määrä; salasanan pituus.
- Ehto: age ≥ 18 (punainen lanka); salasanan pituus ≥ 8; pistemäärä ≥ läpäisyraja.

---

### Tiedosto 3 — `student/week-07/student-tasks-js.md` (600–1400 sanaa)

**Vaadittu rakenne:**

- `## Yleiskatsaus tämän viikon JavaScript-tehtäviin`
  - 2–3 lausetta, jotka nimeävät must-do-minimin (🟢 PAKOLLINEN) vs syventävän (🟣 SYVENTÄVÄ), **täsmällisellä sanamuodolla "must-do-minimi"**.
  - 1 lause: **AT3 viikon 8 lopussa käyttää uudelleen sitä, mitä kirjoitat tässä. Tallenna koodisi.**
- `### Miten avaat JavaScript-konsolin` — lyhyt universaali resepti (oikea klikkaus → Tarkasta → Konsoli-välilehti; tai `Ctrl+Shift+J` / `Cmd+Opt+J`). Yksi lyhyt kappale.
- Sitten tehtävät.

**Viisi ehdokastehtävää (Rasmus pitää 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ). Oletustoimitus: 1 PAKOLLINEN + 3 SYVENTÄVÄÄ.**

**Tehtävä JS-7.1 — 🟢 PAKOLLINEN — "Ensimmäinen konsoliohjelmasi (JS)"**
- Avaa selainkonsoli. Aja `console.log("Hello, <oma nimesi>")` oikealla nimelläsi. Ota kuvakaappaus tai liimaa tuloste muistiinpanoihin.
- Sitten: esittele `let age = <oma ikäsi>;` ja `console.log(age);`.
- Sitten: esittele `let yearsToAdulthood = 18 - age;` ja `console.log(yearsToAdulthood);`.
- Reflektio (2–3 lausetta): yksi asia, joka yllätti sinut, yksi asia, joka toimi täsmälleen kuten ennustit.
- *AI-kestävä rakenteeltaan:* käyttää opiskelijan oikeaa nimeä, oikeaa ikää, oikeaa kuvakaappausta konsolistaan.
- `### Pidä muistiinpanot` viittaa **AT3:een**.

**Tehtävä JS-7.2 — 🟢 PAKOLLINEN (vaihtoehto 7.1:lle) — "Konsolirelay: ennusta, sitten aja (JS)"**
- Annetaan 3 pientä JS-katkelmaa. Ennusta jokaisen tuloste *ennen* ajamista. Sitten aja ne konsolissa. Vertaa ennustustasi todellisuuteen ja kirjoita yksi lause per katkelma mahdollisesta yllätyksestä.
- *AI-kestävä kontekstin kautta:* opiskelijan omat ennusteet käsin (muistivihko) ovat artefakti.
- Linnea: tämä tehtävä on myös vahva lämmittelypuoliskoksi tunnin "konsolirelaylle".

**Tehtävä JS-7.3 — 🟣 SYVENTÄVÄ — "Ensimmäinen if/else (JS)"**
- Kirjoita 6-rivinen JS-ohjelma, jossa on muuttuja `age`, `if (age >= 18) { ... } else { ... }` ja tulostus kummassakin haarassa.
- Aja se kahdesti: kerran `age = 17`:lla, kerran `age = 19`:lla. Ota kuvakaappaus molemmista tulosteista.
- `### Jos teet tämän yksin`: tässä tehtävässä ei ole pariosuutta.

**Tehtävä JS-7.4 — 🟣 SYVENTÄVÄ — "Käännä viikon 6 pseudokoodisi (JS)"**
- Valitse yksi pala viikon 6 pseudokoodiasi, jossa on IF/ELSE. Käännä se JavaScriptiksi. Sen ei tarvitse olla elegantti; sen pitää ajaa.
- Tallenna alkuperäinen pseudokoodi ja JS-koodi rinnakkain muistiinpanoihisi — **tämä on täsmälleen se artefakti, jota AT3 pyytää.**

**Tehtävä JS-7.5 — 🟣 SYVENTÄVÄ — "Riko se tarkoituksella (JS)"**
- Tuo tarkoituksella yksi virhe kerrallaan toimivaan ohjelmaasi tehtävästä JS-7.3 (unohda lainausmerkki; unohda sulkeva kaarisulku; kirjoita `console.log` väärin). Kirjoita kullekin **täsmällinen virheilmoitus**, jonka konsoli tulostaa.
- Reflektio (2–3 lausetta): mikä virheilmoitus oli selkein? Mikä oli sekava?

---

### Tiedosto 4 — `student/week-07/student-tasks-csharp.md` (600–1400 sanaa)

**Rinnakkainen rakenne tiedostolle 3.** Tehtävät on käsitepareja JS-tiedoston kanssa.

- `## Yleiskatsaus tämän viikon C#-tehtäviin` — sama muoto kuin JS-tiedostossa. Sama "must-do-minimi"-sanamuoto. Sama AT3-muistutus.
- `### Miten avaat online-C#-ympäristön` — lyhyt kappale: oletussuositus on **.NET Fiddle** (`dotnetfiddle.net`, ei tilin luomista tarvita). Mainitse `sharplab.io` ja C#-yhteensopiva Replit vaihtoehtoina. Lyhyt kappale kustakin tai yksi lyhyt kappale kaikille kolmelle.

**Viisi ehdokastehtävää. Oletustoimitus: 1 PAKOLLINEN + 3 SYVENTÄVÄÄ, parina JS-tiedoston kanssa.**

**Tehtävä CS-7.1 — 🟢 PAKOLLINEN — "Ensimmäinen konsoliohjelmasi (C#)"** *(JS-7.1:n pari)*
- Avaa .NET Fiddle. Aja `Console.WriteLine("Hello, <oma nimesi>")` oikealla nimelläsi. Ota kuvakaappaus tulosteesta.
- Sitten: esittele `int age = <oma ikäsi>;` ja `Console.WriteLine(age);`.
- Sitten: esittele `int yearsToAdulthood = 18 - age;` ja `Console.WriteLine(yearsToAdulthood);`.
- Reflektio (2–3 lausetta) — sama kehote kuin JS-7.1:ssä.
- *AI-kestävä rakenteeltaan:* sama logiikka kuin JS-7.1:ssä.

**Tehtävä CS-7.2 — 🟢 PAKOLLINEN (vaihtoehto 7.1:lle) — "Konsolirelay: ennusta, sitten aja (C#)"** *(JS-7.2:n pari)*
- Annetaan 3 pientä C#-katkelmaa. Sama ennusta-sitten-aja-protokolla.

**Tehtävä CS-7.3 — 🟣 SYVENTÄVÄ — "Ensimmäinen if/else (C#)"** *(JS-7.3:n pari)*
- Sama rakenne, C#:ssa. Huomaa, että aaltosulkeet ovat samat kuin JS:ssä; eron, jonka opiskelija *tuntee*, on tyyppimerkintä `int age = ...` ja pakolliset puolipisteet.

**Tehtävä CS-7.4 — 🟣 SYVENTÄVÄ — "Käännä viikon 6 pseudokoodisi (C#)"** *(JS-7.4:n pari)*
- Sama protokolla kuin JS-7.4:ssa, C#:ssa. Sama AT3-luovutusmuistio.

**Tehtävä CS-7.5 — 🟣 SYVENTÄVÄ — "Riko se tarkoituksella (C#)"** *(JS-7.5:n pari)*
- Riko ohjelma tarkoituksella (unohda puolipiste — tämä on kova virhe C#:ssa toisin kuin JS:ssä; kirjoita `Console.WriteLine` väärin; mismatchaa aaltosulje). Merkitse muistiin tarkka kääntäjän virhe.

**Rinnakkaisuussääntö:** PAKOLLINEN tehtävä CS-7.1:ssä opettaa samat kolme asiaa kuin JS-7.1 (tuloste, muuttuja, laskutoimitus). SYVENTÄVÄT tehtävät pariutuvat 1-to-1.

---

### Valinnainen tiedosto 4b — `student/week-07/student-tasks.md` (≤200 sanaa, valinnainen)

Jos Rasmus päättää toimittaa tämän, se on ohut indeksi:

- 1 lyhyt kappale: "Tämän viikon tehtävät tulevat kahdessa makuvariantissa — valitse kielesi."
- 2 bullet-pointtia, jotka linkittävät `student-tasks-js.md`:hen ja `student-tasks-csharp.md`:hen.
- 1 lause: "Voit tehdä syventävät tehtävät *toisella* kielellä, jos haluat nähdä side-by-siden suoraan."
- Ei tehtäväsisältöä, ei omaa numerointia.

Sunen oletussuositus: **ohita tämä tiedosto.** Kaksi kielitiedostoa on selkeästi nimetty, ja yleiskatsaus osoittaa molempiin.

---

### Tiedosto 5 — `student/week-07/vocabulary.md` (10–18 termiä)

**Vaaditut termit** (Rasmus voi lisätä 1–4 omiaan, mutta ei saa ohittaa vaadittuja):

1. Ohjelmointikieli
2. Syntaksi
3. Käsky
4. Tulkki (epämuodollinen)
5. Kääntäjä (epämuodollinen)
6. Konsoli
7. Tuloste
8. Muuttuja
9. Arvo
10. Sijoitus
11. Merkkijono (string)
12. Int / numero
13. Ehto
14. If / else
15. Vertailuoperaattori
16. `console.log` *(JavaScript-spesifinen merkintä)*
17. `Console.WriteLine` *(C#-spesifinen merkintä)*
18. **Silmukka** — merkitty **"eteenpäin katsovaksi — viikon 8 keskeinen aihe"**.

Valinnaiset lisäykset: *boolean*, *lohko (aaltosulkeet)*, *puolipiste*, *template literal / string interpolation*, *virheilmoitus*.

Jokainen määritelmä on 1–3 lausetta, selkokielistä, lyhyellä esimerkillä siellä missä luonnollista.

---

### Tiedosto 6 — `student/week-07/slides.md` (~12–18 kalvoa)

**Suositeltu kalvojen runko (Rasmus voi säätää järjestystä ja otsikoita rakenteen hengen sisällä). Kalvon kielitagi: AGN = riippumaton, JS = vain JS, CS = vain C#, BOTH = side-by-side.**

1. `# Viikko 7 — Pseudokoodista koodiin` *(otsikkokalvo)* — AGN.
2. `## Keskeinen kysymys vielä kerran` — runko: kurssin keskeinen kysymys **sananmukaisesti** — AGN.
3. `## Mitä tämä viikko harjoittaa` — 3 bullet-pointtia O19:lle, O20:lle, O21:lle — AGN.
4. `## Miksi ohjelmointikieli?` — pseudokoodi on ihmisille; koodi on sananmukaiselle tietokoneelle — AGN.
5. `## Mitä syntaksi on?` — lyhyt määritelmä + 1 arkielämä + 1 IT-esimerkki — AGN.
6. `## Kaksi kieltä, jotka kohtaamme` — JS (selain) ja C# (.NET, Unity) — AGN.
7. `## Hello, console — rinta rinnan` — JS `console.log("Hello")` vs C# `Console.WriteLine("Hello");` — BOTH.
8. `## Selainkonsolin avaaminen` — pikahowto — JS.
9. `## .NET Fiddlen avaaminen` — pikahowto — CS.
10. `## Muuttujat — rinta rinnan` — `let age = 16;` vs `int age = 16;` — BOTH.
11. `## Ensimmäinen laskutoimitus — rinta rinnan` — vuosia täysi-ikäisyyteen — BOTH.
12. `## Ennusta ennen ajamista` — linkitä takaisin viikon 6 käsiajoon — AGN.
13. `## Vertailuoperaattorit` — taulukko `==`, `!=`, `>=`, `<=`, `>`, `<`. Huomaa "olennaisesti identtiset JS:ssä ja C#:ssa" — BOTH.
14. `## Ensimmäinen if/else — rinta rinnan` — iän rajoitus -tarkistus, molemmat kielet samalla kalvolla — BOTH.
15. `## Tunti: konsolirelay` — 1-kalvon kuvaus tuntiaktiviteetista — AGN.
16. `## Tehtävät tällä viikolla` — osoita `student-tasks-js.md`:hen ja `student-tasks-csharp.md`:hen; mainitse must-do-minimi vs. syventävä — AGN.
17. `## Kielen valinta AT3:lle` — ennakoi AT3:a viikolla 8 — AGN.
18. `## Yhteenveto — keskeinen kysymys` — sananmukaisesti uudelleen — AGN.

Tavoittele 15–18 kalvoa. **Vähintään 3 BOTH-kalvoa vaaditaan** (kriteeri #22). Käytä `---`:tä omalla rivillä kalvojen välissä. Koodi kalvoilla ≤6 riviä per fenced-lohko.

**Täydennyssetin ehdokkaat (valinnaisia, ≤2 yhteensä, 4–8 kalvoa kukin):**

- `slides-l20-walkthrough.md` — askel askeleelta läpikäynti "ensimmäisen ohjelman" demosta, JS-sarake ja C#-sarake, kuvakaappaus kuvakaappaukselta. Vahva ehdokas, jos opettaja haluaa kalvo kalvolta demon O20:lle.
- `slides-l21-age-check.md` — punainen lanka iän rajoitus -esimerkki kuljetettuna pseudokoodista → JS:ksi → C#:ksi, yksi muunnos per kalvo. Vahva ehdokas.

Rasmus päättää oman arvionsa mukaan.

---

### Tiedosto 7 — `teacher/week-07/teacher-materials.md` (2400–4200 sanaa)

**Vaaditut H2-osiot (järjestyksessä):**

1. `## Viikon 7 oppimistavoitteet (kuvattuna Bloomiin)` — esitä O19–O21 tavoitteet uudelleen, ryhmitettyinä Bloomin mukaan. Vain Ymmärtäminen + Soveltaminen.
2. `## Yleisiä virhekäsityksiä viikolla 7` — ≥6 läpi viikon (≥2 per oppitunti). Ehdotettu joukko:
   - **O19**: *"Pseudokoodi riittää — miksi tarvitsemme koodia?"* → Korjaus: pseudokoodi on ihmisille; tietokone lukee vain sitä, mitä se osaa jäsentää sananmukaisesti. // *"On olemassa yksi 'oikea' ohjelmointikieli."* → Korjaus: tuhansia kieliä on olemassa; JS ja C# ovat kaksi monista; ajattelu siirtyy.
   - **O20**: *"C# on JS:ää vaikeampi"* (tai päinvastoin) → Korjaus: ajattelu on sama; pinta eroaa hieman. // *"`console.log` ja `Console.WriteLine` tekevät eri asioita"* → Korjaus: ne tekevät saman asian — tulostavat konsoliin — eri syntaksilla.
   - **O21**: *"`=` tarkoittaa 'on yhtä suuri kuin'"* → Korjaus: `=` sijoittaa, `==` vertaa (ja JS:ssä on myös `===`). // *"`if` ilman `else`:tä on väärin"* → Korjaus: `else` on valinnainen; `if` yksin on pätevä.
3. `## Oppitunti 19 — 90 min suunnitelma` — kieliriippumaton. Aikajaot summana 90, itsenäisellä lohkolla 27–45 min. Ehdotettu luuranko:
   - 0–10 min: lämmittely — näytä yksi viime viikon pseudokoodikappale; kysy luokalta "voisiko tietokone ajaa tämän täsmälleen niin kuin kirjoitettu?"
   - 10–30 min: opettajan syöte — mikä on ohjelmointikieli, mikä on syntaksi, miksi JS ja C#.
   - 30–60 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat lukevat `self-study.md`:n O19-osion ja kirjoittavat 4–6 lausetta muistiinpanoihinsa: *"Miksi ohjelmointikielen täytyy olla olemassa, kun pseudokoodi on jo täsmällistä?"*
   - 60–80 min: pariaktiviteetti — parit jakavat vastauksensa; parit löytävät yhden paikan, jossa ovat eri mieltä; koko luokan debrief poimii 2 eri mielisyyttä.
   - 80–88 min: O20:n ennakko — näytä yksi side-by-side JS/C# `Hello`-kalvo.
   - 88–90 min: lopetus.
   - `### Kalvovinkit`: kalvot 1–6 järjestyksessä; näytä kalvo 7 vain teaserina.
4. `## Oppitunti 20 — 90 min suunnitelma` — kaksikielinen. Ehdotettu:
   - 0–10 min: lämmittely — avaa selainkonsoli livenä; avaa .NET Fiddle livenä; tulosta `"Hello, class"` kummassakin, rinta rinnan.
   - 10–25 min: opettajan syöte — muuttujat, sijoitus, tuloste. Opettaja kirjoittaa yhden esimerkin JS:ssä, sitten saman esimerkin C#:ssa, taululle tai näytölle.
   - 25–55 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat tekevät PAKOLLISEN tehtävän valitsemallaan kielellä (`JS-7.1` tai `CS-7.1`).
   - 55–75 min: tunnin opettajavetoinen aktiviteetti — **"Konsolirelay"** (katso `in-class-tasks.md`), kielisekoittunut.
   - 75–85 min: koko luokan debrief — kerää yksi yllätys per kieli; rakenna "näimme"-taulu.
   - 85–90 min: lopetus + O21:n ennakko.
   - `### Kalvovinkit`: kalvot 7–11 järjestyksessä; kalvo 12 siirtymänä O21:een.
5. `## Oppitunti 21 — 90 min suunnitelma` — kaksikielinen. Ehdotettu:
   - 0–10 min: lämmittely — laita viikon 6 iän rajoitus -pseudokoodi taululle; kysy luokalta "miltä tämä näyttäisi koodina?"
   - 10–30 min: opettajan syöte — vertailuoperaattorit (taulu) ja `if/else`-lohkorakenne. Demoa iän rajoitus -esimerkki molemmilla kielillä rinta rinnan.
   - 30–60 min: **ITSENÄINEN TYÖ** (30 min) — opiskelijat tekevät `if/else`-syventävän tehtävän valitsemallaan kielellä (`JS-7.3` tai `CS-7.3`).
   - 60–80 min: pariaktiviteetti — pariuta JS-opiskelijat C#-opiskelijoiden kanssa 1-to-1. Jokainen pari vertaa koodinsa rivi riviltä. Koko luokka kerää 2 eroa.
   - 80–88 min: lopetus — eksplisiittinen luovutus AT3:lle viikolla 8.
   - 88–90 min: huoltotyöt.
   - `### Kalvovinkit`: kalvot 12–18 järjestyksessä, mukaan lukien "Kielen valinta AT3:lle" -kalvo lähellä loppua.
6. `## Fasilitointivinkit` — lyhyt läpileikkaava lohko. On sisällettävä: "**IDE-asennusta ei vaadita.** Opiskelijat käyttävät **selaimen DevTools-konsolia** JavaScriptille ja **online-C#-ympäristöä** (.NET Fiddle, sharplab.io tai C#-yhteensopiva Replit) C#:lle. Älä asenna Node.js:ää, .NET SDK:ta, Visual Studiota tai VS Codea tälle viikolle." Plus 3–4 lyhyttä vinkkiä kielisekoittuneen luokkahuoneen hallintaan (anna opiskelijoiden valita; älä työnnä yhtä kieltä; pariuta JS+C#-opiskelijat O21:n pariaktiviteettiin).
7. `## Vastauksia yleisiin opiskelijan kysymyksiin` — vähintään 5 läpi viikon. Vaaditut kysymykset:
   - *"Minkä kielen valitsisin?"* — valitse se, joka näyttää sinusta vähemmän pelottavalta; voit vaihtaa milloin vain.
   - *"Onko toinen kielistä toista vaikeampi?"* — ei; ne ovat eri pintoja.
   - *"Riippuuko AT3:n arvosanani kielestäni?"* — ei; arvosana riippuu ajattelusta.
   - *"Tarvitsenko asentaa mitään?"* — ei. Selainkonsoli JS:lle, .NET Fiddle C#:lle.
   - *"Voinko käyttää ChatGPT:tä kirjoittamaan koodini?"* — voit käyttää sitä tarkistamiseen; et voi palauttaa AT3-koodia, jota et ymmärrä rivi riviltä.
8. `## Formatiivisen arvioinnin vinkit` — 3–5 nopeaa tarkistusta. Ehdotettu: exit-tiketti ("tulosta yksi rivi koodia, kummalla tahansa kielellä, joka tulostaa nimesi"); pariraportit; yhden minuutin paperi; live-näyttöjen näyttäminen.

Ristiviittaa `in-class-tasks.md`:hen O20-suunnitelmasta (jossa konsolirelay sijaitsee).

---

### Tiedosto 8 — `teacher/week-07/in-class-tasks.md` (400–1200 sanaa)

**Vaadittu rakenne:**

- `## Yleiskatsaus` — 2–3 lausetta, jotka nimeävät tehtävät ja milloin viikolla ne sopivat. Huomaa eksplisiittisesti, että aktiviteetit on suunniteltu toimimaan **kielisekoittuneessa huoneessa** (osa opiskelijoista JS:llä, osa C#:lla).

**Kaksi konkreettista aktiviteetti-ideaa (oletus: molemmat):**

**Aktiviteetti A — PAKOLLINEN — "Konsolirelay"** *(koko luokka + opettajavetoinen, ~20 min, sloti oppitunnille 20 välille 55–75 min)*

- Opettaja valmistelee **6 pientä katkelmaa**: 3 JavaScriptiä, 3 C#:a. Kukin on ≤4 riviä. Esimerkkejä:
  - JS: `let x = 5; let y = 3; console.log(x + y);`
  - JS: `let name = "Lyra"; console.log("Hei, " + name);`
  - JS: `let age = 17; if (age >= 18) console.log("aikuinen"); else console.log("alaikäinen");`
  - C#: `int x = 5; int y = 3; Console.WriteLine(x + y);`
  - C#: `string name = "Lyra"; Console.WriteLine("Hei, " + name);`
  - C#: `int age = 17; if (age >= 18) Console.WriteLine("aikuinen"); else Console.WriteLine("alaikäinen");`
- Yksi katkelma näytetään kerrallaan projektorilla. **Ennen ajamista** jokainen opiskelija kirjoittaa ylös (paperille tai chattiin), mitä konsolin uskoo tulostavan. **Sitten** opettaja ajaa sen livenä. Luokka vertailee ennusteita todellisuuteen.
- Sekoita kieliä tarkoituksella: jopa JS:n valinnut opiskelija näkee C#-katkelmat, ja päinvastoin, rinta rinnan JS-vastineen kanssa. Vertailu on oppitunti.
- 6 katkelmaa × ~3 min = ~18 min. Sopii 55–75 min slottiin.
- **Miksi tämä vaatii luokkahuoneen:** live-ennusta-sitten-aja-rytmi välittömällä vertaisvertailulla on koko pointti. Ei voida tehdä kotitehtävänä.
- **Ristiviittaus:** `teacher-materials.md` oppitunnin 20 90-min suunnitelma, 55–75 min lohko.

**Aktiviteetti B — VALINNAINEN — "Käännä naapurisi" (pari, ~20 min, sloti oppitunnille 21 välille 60–80 min)**

- Pariuta JS-opiskelija C#-opiskelijan kanssa.
- Jokainen näyttää toiselle oman `if/else`-koodinsa tehtävästä `JS-7.3` / `CS-7.3`.
- Jokainen yrittää **kääntää** toisen koodin omalle kielelleen — käsin, paperille, ei LLM:ää.
- Vertaa tulosta alkuperäiseen. Keskustele, mikä pysyi samana, mikä oli erilaista.
- Päätösdebrief: jokainen pari antaa yhden havainnon taululle.

Ristiviittaa takaisin `teacher-materials.md`:hen, jotta opettaja tietää tarkan 90-min slotin.

---

## Avoimet kysymykset

1. **Valinnainen `student-tasks.md`-indeksitiedosto.** Tämä suunnitelma suosittelee **sen ohittamista** — kaksi kielitiedostoa nimeltä on selkeitä yksinään. Wilhelm hyväksyy kumman tahansa valinnan; jos tiedosto on mukana, sen on oltava ≤200 sanaa ja sisällötön. **Oletusoletus:** Rasmus ei toimita `student-tasks.md`:tä.
2. **Oletusvalinta siitä, mikä PAKOLLINEN tehtävä toimitetaan kummassakin kielitiedostossa.** Kaksi ehdokasta tarjotaan (`X-7.1 "Ensimmäinen konsoliohjelmasi"` vs `X-7.2 "Konsolirelay ennusta-sitten-aja"`). **Oletusoletus:** Rasmus toimittaa **`X-7.1`:n PAKOLLISENA** (konkreettinen artefakti: kuvakaappaukset *heidän* konsolitulosteestaan *heidän* nimellään ja *heidän* iällään — vahvasti AI-kestävä) ja pitää `X-7.2`:n tuntikäyttöön konsolirelay-aktiviteettina kotitehtävän sijaan.
3. **PAKOLLISTEN tehtävien määrä per kielitiedosto.** Toimeksianto sanoo 1–2. **Oletusoletus:** Rasmus toimittaa **1** PAKOLLISEN per kielitiedosto plus **3** SYVENTÄVÄÄ tehtävää. Jos luokka on vahva, opettaja voi paikallisesti ylentää yhden SYVENTÄVÄN PAKOLLISEKSI; tämä ei ole Rasmuksen päätös.
4. **Täydennyssetit.** Kaksi vahvaa ehdokasta (`slides-l20-walkthrough.md` ja `slides-l21-age-check.md`). **Oletusoletus:** Rasmus toimittaa **yhden** näistä — `slides-l21-age-check.md` (kuljetus pseudokoodista JS:ksi C#:ksi on korkeimmän arvon täydennysoppitunti). Läpikäyntisetti on hyvä olla, mutta ei välttämätön. Rasmus voi päättää toisin.
5. **`===` JavaScriptissä.** Pitäisikö nimetä tiukka yhtäsuuruus vai piilottaa se nyt? **Oletusoletus:** nimetään **yhdellä lauseella** `self-study.md`:n oppitunti-21:ssä ("JS:ssä on myös `===` tiukalle yhtäsuuruudelle; molemmat toimivat siihen, mitä tässä teemme"); ei kalvoille; ei tehtäviin. Välttää löyhän yhtäsuuruuden kompastuskiven ensi vuonna ilman, että rämmitään tyyppipakotuksen aiheessa.
6. **C#-merkkijonon interpolointi vs. yhdistäminen.** Kaksi yhtä pätevää vaihtoehtoa (`"Hello, " + name` vs `$"Hello, {name}"`). **Oletusoletus:** Rasmus valitsee **yhdistämisen `+`:lla** molemmilla kielillä — syntaksin päällekkäisyys on viesti. Mainitse `$"..."` kerran sanastossa "eteenpäin katsovana" valinnaisena terminä.
7. **Puolipisteet.** JS on lempeä, C# on tiukka. **Oletusoletus:** Rasmus näyttää jokaisen JS-esimerkin **päättyvällä puolipisteellä** rinnakkaisuuden vuoksi, mainitsee yhdessä lauseessa, ettei JS sitä tiukasti tarvitse, ja jatkaa. Muuten side-by-side-vertailu saa visuaalisen änkytyksen ilman oppimishyötyä.
8. **Kalvojen määrä.** 12–18 kriteerin mukaan. **Oletusoletus:** Rasmus tähtää **15–17 kalvoon** `slides.md`:ssä.
9. **Reflektiokehotteiden määrä `self-study.md`:ssä.** ≥4 läpi kolmen oppitunnin (≥1 per oppitunti) vaaditaan. **Oletusoletus:** Rasmus toimittaa 5–6, joista 2 O20:ssa (tihein oppitunti).
10. **PAKOLLINEN-merkki rivissä.** `in-class-tasks.md` käyttää **PAKOLLINEN**:ta inline-tagina H2:ssa. Wilhelm grep-tarkistaa. **Oletusoletus:** yhdenmukainen viikon 1 kanssa.
11. **30–50 % lohkon yhtenäisyys.** Wilhelm hyväksyy yhden yhtenäisen itsenäisen lohkon per 90-min oppitunti tai enintään kaksi lohkoa summana 27–45 min. **Oletusoletus:** Rasmus toimittaa **yhden yhtenäisen 30 min lohkon** kullakin oppitunnilla — yksinkertaisin, vaikein väärin auditoida.
12. **Saako O19 *näyttää* side-by-side-teaserkatkelman.** Kriteeri #28 sanoo, että O19 ei saa riippua JS- tai C#-syntaksin osaamisesta. Teaser sallitaan eteenpäin osoittavana viittauksena. **Oletusoletus:** Rasmus sisällyttää **yhden** pienen teaserkalvon (kalvo 7 yllä olevassa rungossa) O19/O20-rajalle — se on teknisesti ensimmäinen O20-kalvo, mutta toiminnallisesti elää sauman kohdalla.
