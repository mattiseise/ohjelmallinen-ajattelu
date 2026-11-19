# Ohjelmallinen ajattelu — arvioitavat tehtävät AT1–AT3 (Sune, portti #1)

Kurssi: Ohjelmallinen ajattelu (fi), 8 viikkoa × 3 oppituntia × 90 min = 24 oppituntia
Kohderyhmä: ammatillisen ICT-alan 1. vuoden opiskelijat, 15–18 v, ei aiempaa ohjelmointiosaamista
Tämän ajon laajuus: **vain** kolme assessment-oppituntia (lesson-06, lesson-18, lesson-24) → `assessment.md` + `rubric.md` kullekin. Ei muuta materiaalia.
Manifestiluonnos: `/home/claude/oa-at/tuotanto/course.draft.json`

---

## Suunnitelma

### Lähtötilanne lähteiden perusteella

- Kurssi on jo tuotettu viikkotasolla (legacy `viikko-XX/opiskelija/opiskelijatehtavat.md`). Viikkotehtävät 2.1–2.5, 6.1–6.4 ja 8.1–8.5 (JS ja CS) ovat olemassa ja viittaavat AT-tehtäviin toistuvasti ("Säilytä muistiinpanosi — AT1 tulee oppitunnin 6 lopussa").
- AT1 ja AT2 ovat olemassa vain yhtenä diana kumpikin (`paadiat.md`, viikko 2 dia "AT1 — ensimmäinen arvioitava tehtävä"; viikko 6 dia "AT2 — palautus noin oppitunnilla 18"). Niistä ei ole opiskelijalle tehtävänantoa eikä rubriikkia.
- AT3 on kirjoitettu tehtävänä 8.1-JS / 8.1-CS. Siltä puuttuu kieliagnostinen koontiohje ja ES/S-/S/S+-rubriikki. Olemassa oleva 8.1 kuvaa hyväksynnän muodossa "Hyväksytty / ei vielä hyväksytty neljällä tarkistuksella" — tämä sovitetaan rubriikkiin (ks. Arvioitavat oppitunnit ja Avoimet kysymykset).
- Opettajan materiaalit lukitsevat AT:iden paikan 90 min tuntisuunnitelmissa: L6 itsenäinen työ 0:25–0:55 on AT1-luonnostelua, parikatselmointi 0:55–1:15, palautus 1:15–1:25. L18 itsenäinen työ 0:25–0:55 on oman 6.1-pseudokoodin jäljitystä, AT2:n luovutus 1:20–1:28. L23 itsenäinen työ 0:25–1:05 on AT3:n rakentamista (palautus tunnin lopussa), L24 itsenäinen työ 0:25–0:55 testausta ja korjausta, esitykset 0:55–1:25.

### Kolme assessment-oppituntia

| AT | Oppitunti (manifest-id) | Moduuli | Palautus | Mitä arvioidaan (lukittu toimeksiannossa) | Osatehtävät, joihin AT nojaa |
|----|----|----|----|----|----|
| AT1 | lesson-06 "IT-tehtävän pilkkominen" | module-2 (viikko 2) | L6:n lopussa (75 min kohdalla) tai viimeistään L7:n alussa | Arkisen tai IT-tehtävän pilkkominen: päätehtävä + tavoite, 4–8 osatehtävää osatavoitteineen, järjestys jossa ≥1 riippuvuus nimetty, 3–5 virkkeen reflektio. Artefakti: taulukko, kaavio tai tekstirakenne. | 2.1 (🟢 harjoitusversio), 2.2 (🟢 paritestaus), 2.3 (🟣 riippuvuudet), 2.4 (🟣 koulun IT-tehtävä — "vahvin AT1-ehdokas"), 2.5 (🟣 LLM-sparraus) |
| AT2 | lesson-18 "Pseudokoodin testaaminen: kuivaharjoittelu ja virheiden löytäminen" | module-6 (viikko 6) | noin L18 (luovutus 1:20–1:28) | Pseudokoodi (10–20 riviä) pienestä itse valitusta prosessista, ≥1 ehto ja ≥1 toisto, kurssin avainsanat; jäljitystaulukko normaalilla ja yhdellä hankalalla syötteellä; 5 virkkeen reflektio. Ei oikeaa ohjelmointikieltä. | 6.1 (🟢 "täysimittainen AT2-harjoitus"), 6.2 (🟣 etsi bugi), 6.3 (🟣 luokkakaverin pseudokoodi), 6.4 (🟣 LLM jäljitystä vastaan) |
| AT3 | lesson-24 "Testaa, korjaa yksi bugi, esitä" | module-8 (viikko 8) | kirjallinen osa L23:n lopussa, 2 min suullinen esitys L24:ssä | Oman viikon 6 pseudokoodin kääntäminen toimivaksi JS- tai C#-ohjelmaksi (10–25 riviä), ajo kahdella lähtöarvolla, yhden bugin korjaus; lähdekoodi + kuvakaappaus + 3–5 virkkeen pohdinta + esitys. | 8.1-JS / 8.1-CS (🟢 AT3-ohje — kielikohtaiset vaiheet), 8.2 (🟢 silmukkalämmittely), 8.3 (🟣), 8.4 (🟣 virheilmoitukset), 8.5 (🟣 kielivertailu); esitys: `lisamateriaali-l24-esitysrubriikki.md` |

AT3 sijoitetaan manifestissa oppituntiin **lesson-24**, koska suoritus täydentyy vasta esityksessä ja L24 on viikon 8 arviointipiste. `assessment.md` kertoo selvästi, että kirjallinen osa palautetaan jo L23:n lopussa.

### Oppimistavoitteet per assessment-oppitunti (manifestin `objectives`, opiskelijalle näkyvä muoto)

Nämä on johdettu legacy-opettajamateriaalien oppituntikohtaisista Bloom-tavoitteista ja toimeksiannon lukituista AT-sisällöistä. Rubriikin kriteerit mittaavat täsmälleen näitä.

**lesson-06 (AT1)** — Bloom: ymmärtää, soveltaa
- O6.1 Osaat tunnistaa todellisesta arkisesta tai IT-tilanteesta päätehtävän ja sanoa sen tavoitteen yhdellä virkkeellä: mikä on totta, kun tehtävä on valmis.
- O6.2 Osaat pilkkoa päätehtävän 4–8 osatehtäväksi, joilla jokaisella on oma, päätavoitteesta erottuva osatavoite.
- O6.3 Osaat järjestää osatehtävät ja nimetä vähintään yhden riippuvuuden sekä tunnistaa, mitkä osatehtävät ovat järjestyksen suhteen vapaita.
- O6.4 Osaat kertoa 3–5 virkkeellä, mikä pilkkomisessa oli vaikeinta ja mitä muutit, kun joku toinen (pari, 24 tunnin tauko tai LLM-sparraus) luki pilkkomisesi.

**lesson-18 (AT2)** — Bloom: ymmärtää, soveltaa
- O18.1 Osaat kirjoittaa 10–20 rivin pseudokoodin itse valitsemastasi pienestä prosessista kurssin avainsanoilla (SET, READ, WRITE, IF/ELSE/ENDIF, WHILE/ENDWHILE, FOR/ENDFOR) niin, että mukana on vähintään yksi ehto ja yksi toisto.
- O18.2 Osaat nimetä muuttujat niin, että nimi kertoo seuraavalle lukijalle, mitä arvoa muuttuja sisältää.
- O18.3 Osaat kuivaharjoitella pseudokoodin jäljitystaulukolla rivi riviltä yhdellä normaalilla ja yhdellä hankalalla syötteellä.
- O18.4 Osaat osoittaa jäljityksestä rivin, jolla toteutunut tuloste eroaa odotetusta ensimmäisen kerran, nimetä bugin yleiskielellä ja kuvata korjauksen — tai perustella jäljityksellä, että hankala syöte toimi.
- O18.5 Osaat selittää viidellä virkkeellä yleiskielellä, mitä pseudokoodisi tekee ja mitä jäljitys paljasti.

**lesson-24 (AT3)** — Bloom: soveltaa, arvioida (kevyt)
- O24.1 Osaat valita omasta viikon 6 pseudokoodistasi sopivan kokoisen palan ja kääntää sen 10–25 rivin toimivaksi JavaScript- tai C#-ohjelmaksi.
- O24.2 Osaat ajaa ohjelman kahdella eri lähtöarvolla, verrata tulostetta ennusteeseesi ja dokumentoida molemmat ajot kuvakaappauksella.
- O24.3 Osaat lukea konsolin tai kääntäjän virheilmoituksen, nimetä yhden bugin yleiskielellä ja kuvata sen yhden rivin korjauksen.
- O24.4 Osaat esittää ohjelmasi 2 minuutissa neljällä iskulla: mitä se tekee, miten se toimii, mikä meni pieleen, miten korjasit sen.

### Punainen lanka (concepts / builds_on)

Assessment-oppitunnit eivät opeta uusia käsitteitä (`concepts: []`), ne kokoavat. `builds_on` osoittaa legacy-viikkojen oppitunteihin:
- lesson-06 ← lesson-01 (kirjaimellinen suorittaja), lesson-04 (pilkkominen, päätehtävä, osatehtävä, osatavoite, tavoite), lesson-05 (järjestys, riippuvuus, vapaa osatehtävä).
- lesson-18 ← lesson-13/14/15 (järjestys, ehto, toisto), lesson-16 (pseudokoodi, avainsanat, sisennys), lesson-17 (muuttuja, syöte–käsittely–tuloste), lesson-01 (kirjaimellinen robotti = jäljittäjä).
- lesson-24 ← lesson-18 (jäljitys, bugi, odotettu vs. toteutunut tuloste), lesson-20/21/22 (console.log / Console.WriteLine, let / int / string, if–else, for/while), lesson-23 (käännöstaulukko, kuvakaappaus, lähdekooditiedosto), lesson-12 (palautteen vastaanottaminen, iteraatio).

### Kesto

AT:t eivät lisää uusia tunteja. Ne sijoittuvat jo suunniteltuihin itsenäisen työn jaksoihin (L6: 30 min, L18: 30 min, L23: 40 min, L24: 30 min) ja L24:n 30 min esitysjaksoon. `assessment.md` ei saa kuvata uutta tuntisuunnitelmaa.

---

## Rajaukset

- **Ei uutta oppimateriaalia.** Ei `self-study.md`, `vocabulary.md`, `student-tasks.md`, `teacher-materials.md`, `teacher-led-tasks.md` eikä dioja. Vain `student/lesson-XX/assessment.md` ja `teacher/lesson-XX/rubric.md` kolmelle oppitunnille.
- **Teacher-materials-otsikkokontraktia ei lukita**, koska opettajamateriaalia ei tuoteta. Wilhelm ei tee sitä tarkistusta tässä ajossa. 90 min -aikataulut ja 30–50 % -sääntö ovat legacy-materiaalin asia, eivät tämän ajon.
- **Olemassa olevia viikkotehtäviä ei muuteta eikä kirjoiteta uudelleen.** AT viittaa niihin id:llä ("tehtävä 2.4", "tehtävä 6.1", "tehtävä 8.1-JS / 8.1-CS"). Jos AT:n ja viikkotehtävän välillä on ristiriita, AT:n teksti kertoo sen lyhyesti ja noudattaa tehtävätiedostoa.
- **Numerointipoikkeama viikko 6:** diat numeroivat tehtävät 6.1, 6.3, 6.4, 6.5; tehtävätiedosto 6.1–6.4. AT2 käyttää tehtävätiedoston numerointia (6.1 pseudokoodi, 6.2 etsi bugi, 6.3 luokkakaverin pseudokoodi, 6.4 LLM-sparraus). Poikkeama kirjataan avoimiin kysymyksiin, ei opiskelijatekstiin.
- **AT2:n palautus on "noin oppitunnilla 18"** (diat + viikkotehtävät), ei toimeksiannon alkuperäinen "viikon 5 lopussa".
- **AT3 on kieliagnostinen.** `assessment.md` ei toista 8.1-JS:n tai 8.1-CS:n kielikohtaisia vaiheita (käännöstaulukko, konsoli vs. .NET Fiddle) vaan ohjaa: "JS-polku: tehtävä 8.1-JS; C#-polku: tehtävä 8.1-CS". Ei koodiesimerkkejä assessment.md:ssä.
- **L24-esitysrubriikki on olemassa** (`lisamateriaali-l24-esitysrubriikki.md`): neljä iskua, 2 min, neljä tarkistusta. AT3-rubriikin esityskriteeri viittaa siihen eikä kirjoita sitä uudelleen.
- **Ei automaattisia testausframeworkkeja**, ei IDE-asennuksia. Testaus = ajo kahdella arvolla; debuggaus = virheilmoituksen lukeminen + yksi korjaus (legacy-määritelmä).
- **Kurssialusta (itslearning-vienti) on out-of-scope** tälle putkelle.
- **Ei YAML-front-matteria.** Metadata on manifestissa.
- **Ei Mermaid-diagrammeja**: Mermaid kuuluu `self-study.md`:hen, jota ei tuoteta. Lesson-06, lesson-18 ja lesson-24 eivät tässä ajossa vaadi diagrammia — teksti riittää.
- **Ei 🟢/🟣-merkkiä AT-otsikoihin.** Opiskelijalle näkyvä luokka on "arvioitava tehtävä".

---

## Hyväksymiskriteerit

Wilhelm tarkistaa nämä. Linnea tarkistaa kohdat H10–H14.

### H1 Tiedostot ja polut

Täsmälleen nämä kuusi tiedostoa, ei muita:
- `student/lesson-06/assessment.md` + `teacher/lesson-06/rubric.md`
- `student/lesson-18/assessment.md` + `teacher/lesson-18/rubric.md`
- `student/lesson-24/assessment.md` + `teacher/lesson-24/rubric.md`

Manifestin `rubric`-polku resolvoituu jokaisella kolmella oppitunnilla. Ei YAML-front-matteria.

### H2 assessment.md:n H1 ja täsmälliset H2-otsikot (suomeksi, merkki merkiltä)

H1 muodossa `# AT1 — arvioitava tehtävä: <lyhyt otsikko>` (vastaavasti AT2, AT3). Ajatusviiva on pitkä viiva (—), ei tavuviiva. Otsikossa ei 🟢/🟣-merkkiä.

H2-otsikot täsmälleen tässä järjestyksessä, kaikissa kolmessa tiedostossa:

1. `## Tavoite`
2. `## Mitä palautat ja milloin`
3. `## Vaiheet`
4. `## Mihin viikon tehtäviin tämä nojaa`
5. `## Jos teet tämän yksin`
6. `## Arviointikohteet`

Ei muita H2-otsikoita. H3-alaotsikot ovat sallittuja vain `## Vaiheet`-osiossa (esim. AT3:ssa `### JavaScript-polku` / `### C#-polku`) ja `## Mitä palautat ja milloin` -osiossa (esim. AT3:ssa `### Kirjallinen osa (L23)` / `### Suullinen osa (L24)`).

### H3 rubric.md:n rakenne (templates/rubric-template.md)

- H1: `# Arviointirubriikki — <oppitunnin otsikko>`
- Rivit `**Arvioitava tehtävä:** AT1 — <nimi>` ja `**Mittaa tavoitteita:** O6.1, O6.2, …` (manifestin objectives-tunnisteet tai tavoitteet sanasta sanaan).
- Yksi taulukko, sarakkeet täsmälleen `| Arviointikohteet | ES | S- | S | S+ |`.
- 3–5 kriteeririviä, täsmälleen tämän suunnitelman nimeämät (ks. Arvioitavat oppitunnit ja rubriikit). Ei lisärivejä, ei "kokonaisvaikutelma"-tyyppistä kaatoluokkaa.
- Loppurivi `**Asteikko:** ES = Hylätty · S- = Työssä on puutteita, mutta hyväksytään · S = Hyväksytty · S+ = Suoritus ylittää odotetun tason.`
- Template-kommentti (`<!-- … -->`) ja placeholderit poistettu.

### H4 Kriteerinimien vastaavuus

`assessment.md`:n `## Arviointikohteet` listaa samat kriteerinimet kuin `rubric.md`:n taulukon ensimmäinen sarake, **samassa järjestyksessä, sanasta sanaan**, ilman tasokuvauksia. Opiskelija näkee, mitä arvioidaan, mutta ei ES/S-/S/S+-tekstejä.

### H5 Osatehtäväviittaukset

`## Mihin viikon tehtäviin tämä nojaa` nimeää osatehtävät id:llä (AT1: 2.1, 2.2, 2.3, 2.4, 2.5; AT2: 6.1, 6.2, 6.3, 6.4; AT3: 8.1-JS, 8.1-CS, 8.2, 8.4 ja esitysohje L24) ja kertoo yhdellä virkkeellä per tehtävä, mikä osa AT:stä syntyy siitä. Viittaukset eivät kirjoita osatehtävän vaiheita uudelleen (max 1–2 virkettä per tehtävä). Manifestin `tasks`-lista ja nämä id:t täsmäävät.

### H6 Palautuksen ajoitus

- AT1: "oppitunnin 6 lopussa (noin 75 minuutin kohdalla) tai viimeistään oppitunnin 7 alussa".
- AT2: "noin oppitunnilla 18".
- AT3: "kirjallinen osa oppitunnin 23 lopussa, 2 minuutin suullinen esitys oppitunnilla 24".
Muut ajoitukset ovat virheitä.

### H7 Laajuus ja muoto

- `assessment.md`: 450–800 sanaa. Sävy ja muoto kuten tehtävä 8.1-JS: "Tavoite."-kappale, numeroidut vaiheet, lyhyet virkkeet, 💡 Vinkki -lohko sallittu. Ei koodilohkoja (AT3) eikä pseudokoodiesimerkkejä (AT2) — esimerkit ovat viikkotehtävissä.
- `rubric.md`: taulukon jokainen solu 1–3 virkettä, havainnoitavaa kieltä ("vähintään yksi riippuvuus on nimetty muodossa X riippuu Y:stä, koska …"), ei "hyvä / erinomainen".

### H8 Rekisteri

Opiskelijayleisö: ammatillinen 2. aste, 15–18 v, golden samplen oletusrekisteri. Sinuttelu, lyhyet virkkeet, konkreettinen esimerkki ennen termiä, ei akateemista fraseologiaa. Rubriikki on opettajalle, mutta samalla selkeällä suomella — ei arviointijargonia.

### H9 Kielletyt termit (Wilhelm greppaa, osuma on blocking)

Koko tuotoksesta (kaikki kuusi tiedostoa):
- `Business College Helsinki`, `BC Helsinki`, `bc.fi`
- `AI-resilientti`, `AI-resilient`, `LLM-resistenssi`, `LLM-resistentti` (sisäisiä termejä — rakenne tekee työn, ei etiketti)
- `Rasmus`, `Linnea`, `Wilhelm`, `Sune`, `Alfred`, `Börje` (putken sisäiset nimet eivät kuulu materiaaliin)
- `Hyväksytty / ei vielä hyväksytty` **rubric.md:ssä** (asteikko on ES/S-/S/S+; assessment.md saa viitata tehtävän 8.1 neljään tarkistukseen, ks. AT3)
- `🟢`, `🟣`, `PAKOLLINEN`, `SYVENTÄVÄ` AT:n **otsikossa** (osatehtäväviittauksissa luokan mainitseminen on sallittua)

### H10 AI-resilienssin rakenteellinen peruste (Linnea toteaa rakenteesta, ei etiketistä)

Jokaisen AT:n `## Mitä palautat ja milloin` + `## Vaiheet` sisältävät alla nimetyt rakenteelliset elementit. Pelkkä "käytä omaa kontekstia" -kehotus ei riitä.

**AT1**
- (a) Pilkottava tehtävä on opiskelijan oma, todellinen tehtävä viikkotehtävästä 2.1, 2.2 tai 2.4 — ei keksitty. IT-tehtävässä artefaktissa on oikeat tuote-, valikko- ja painikenimet, jotka opettaja voi tarkistaa (tehtävän 2.4 vaatimus).
- (b) Artefakti luonnostellaan L6:n itsenäisessä jaksossa ja parikatselmoidaan luokassa (0:55–1:15): reflektion on nimettävä **yksi konkreettinen muutos**, jonka opiskelija teki parin kolmen tarkentavan kysymyksen (tai yksin-vaihtoehdon) jälkeen. Muutos sidotaan artefaktin osatehtävän numeroon.
- (c) Jos LLM:ää on käytetty (tehtävä 2.5), reflektio nimeää yhden hylätyn ja yhden hyväksytyn LLM-haasteen perusteluineen. LLM:n tekstiä ei liitetä artefaktiin.

**AT2**
- (a) Prosessi on opiskelijan oma arkiprosessi (tehtävä 6.1), ja hankala syöte on opiskelijan itse valitsema poikkeustilanne siitä prosessista.
- (b) Jäljitystaulukot tehdään **käsin paperille** L18:n itsenäisessä jaksossa ja palautetaan sellaisenaan (paperi tai kuva). Muodon lukitsee legacy: yksi sarake per muuttuja + tulostesarake, yksi rivi per suoritettu rivi.
- (c) Reflektio nimeää **rivinumeron**, jolla toteutunut ja odotettu tuloste erosivat ensimmäisen kerran (tai rivinumeron, jolla hankala syöte käsiteltiin oikein). Rivinumero sidotaan palautettuun pseudokoodiin.
- (d) Jos LLM:ää on käytetty (tehtävä 6.4), reflektio kertoo, missä kohtaa oma ja LLM:n jäljitys erosivat ja kumpi oli oikeassa uudelleenjäljityksen jälkeen.

**AT3**
- (a) Ohjelma on käännös opiskelijan **omasta** viikon 6 pseudokoodista (AT2:n tai tehtävän 6.1 pseudokoodi). Palautukseen liitetään se pseudokoodi, josta käännös tehtiin — opettaja vertaa AT2:een. Varamalli (8.1:n viisi varapohjaa) on sallittu, mutta se rajaa kriteerin K1 enintään tasolle S.
- (b) Kuvakaappaus on omasta ympäristöstä ja näyttää **molemmat** ajot eri lähtöarvoilla; pohdinta nimeää, mitä muuttujaa muutettiin ajojen välillä.
- (c) Bugi on opiskelijan oma (tahallinen tai vahingossa syntynyt), ja virheilmoitus lainataan sanasta sanaan pohdintaan.
- (d) Suullinen esitys pidetään livenä (tai video / luokkachatti 8.1:n yksin-vaihtoehdon mukaan) ja luokka esittää vertaishavainnon — ymmärrys todennetaan puheesta.

### H11 "Jos teet tämän yksin" -tarve per AT

- **AT1 — tarvitaan.** L6:n parikatselmointi ja tehtävä 2.2/2.4 olettavat parin. Hyväksyttävät vaihtoehdot (vähintään yksi, kuten viikkotehtävissä): 24 tunnin tauko + luku "kollegan silmin" + kolme omaa tarkentavaa kysymystä; viesti luokkachattiin ("mihin osatehtävään jäit jumiin?"); eri laite (IT-tehtävän läpikäynti puhelimella/luokan koneella). Osio kertoo, että reflektion vaadittu "yksi muutos" tulee tällöin valitusta vaihtoehdosta.
- **AT2 — tarvitaan, lyhyt.** Perussuoritus ei tarvitse paria (kaksi jäljitystä ovat testi). Osio sanoo sen suoraan ja antaa 24 tunnin tauon tai välineen vaihdon (puhelin vs. paperi) tehtävän 6.3 luokkakaverin tilalle.
- **AT3 — tarvitaan.** Esitys olettaa yleisön. Vaihtoehdot samat kuin tehtävässä 8.1: 2 minuutin video kameralle tai ohjelma + 3 virkkeen tiivistelmä luokkachattiin; neljä iskua pysyvät samoina. Tehtävän 8.5 kielivertailu ei ole osa AT3:a, joten sitä ei tarvitse korvata.

### H12 Rubriikin kriteerit mittaavat objectives-rivejä

Jokainen kriteeririvi on jäljitettävissä yhteen tai kahteen manifestin `objectives`-riviin (taulukko alla). Kriteeri, joka ei jäljity, hylätään.

### H13 Tasojen aito erottelu

S+ ei ole "enemmän samaa" vaan laadullisesti eri taso (alla per kriteeri "S+ erottuu näin"). S- on hyväksytty mutta puutteellinen, ES on hylätty — kummankin kuvaus on havainnoitava. Linnea hylkää geneeriset tasokuvaukset.

### H14 AT3:n suhde olemassa olevaan hyväksyntämalliin

Tehtävän 8.1 ja L24-esitysrubriikin "neljä tarkistusta" säilyvät **S-tason kynnyksenä**: kaikki neljä täyttyvät = vähintään S. Rubriikki ei ole ristiriidassa niiden kanssa vaan lisää ES/S-/S+-erottelun. `assessment.md` sanoo tämän yhdellä virkkeellä.

### H15 Markdown-validius

Taulukot renderöityvät, ei avoimia koodilohkoja, ei rikkinäisiä viittauksia. Tiedostopolut viittauksissa suhteellisina (esim. `lisamateriaali-l24-esitysrubriikki.md`) tai tehtävä-id:llä, ei absoluuttisina.

---

## Arvioitavat oppitunnit ja rubriikit

Asteikko kaikissa: **ES / S- / S / S+**. Rasmus kirjoittaa tasokuvaukset; alla on se, mitä kunkin kriteerin pitää mitata, ja mikä erottaa S+:n laadullisesti.

### lesson-06 — AT1: Pilko todellinen tehtävä (4 kriteeriä)

| # | Kriteeri (nimi sanasta sanaan) | Mittaa | Mitä mitataan | S+ erottuu näin |
|---|---|---|---|---|
| K1 | Päätehtävä ja tavoite | O6.1 | Päätehtävä on yksi virke; tavoite on erillinen virke, joka kertoo milloin tehtävä on valmis ("mikä on totta lopussa"), ei toista päätehtävää. Tehtävä on todellinen ja tunnistettava. | Tavoite sisältää tarkistettavan ehdon (aika, tila, henkilö: "ennen klo 10", "kollega pääsee kirjautumaan"), ei vain "valmis". |
| K2 | Osatehtävät ja osatavoitteet | O6.2 | 4–8 osatehtävää, jokaisella oma osatavoite yhdellä virkkeellä. Osatavoitteet eroavat toisistaan ja päätavoitteesta. Taso on osatehtävä, ei klikkauslista eikä litteä 30 rivin ohje. | Vähintään yhdessä osatehtävässä on huomio "tämä pitäisi pilkkoa vielä" tai IT-tehtävässä oikeat valikko-/painikenimet, jotka kirjaimellinen seuraaja voisi toteuttaa. |
| K3 | Järjestys ja riippuvuudet | O6.3 | Osatehtävät on numeroitu järjestykseen; vähintään yksi riippuvuus on nimetty muodossa "X riippuu Y:stä, koska Y:n tulos on X:n syöte". | Vähintään kaksi riippuvuutta **ja** vähintään yksi vapaa/rinnakkainen osatehtävä nimetty perusteluineen — pilkkominen ei ole naamioitu tarkistuslista. |
| K4 | Reflektio ja tehty muutos | O6.4 | 3–5 virkettä. Nimeää vaikeimman osatavoitteen ja yhden konkreettisen muutoksen, jonka pari/24h-tauko/luokkachatti/LLM-sparraus aiheutti, sidottuna osatehtävän numeroon. | Reflektio erottaa, oliko epäselvyys osatehtävässä, osatavoitteessa vai niiden välisessä yhteydessä (tehtävän 2.2 kysymys), ja jos LLM:ää käytettiin, nimeää hylätyn haasteen perusteluineen. |

ES-taso kaikissa: elementti puuttuu kokonaan tai tehtävä on selvästi keksitty/yleinen ("asenna ohjelma" ilman nimeä). S-: elementti on, mutta puutteellinen (esim. osatavoitteet kopioivat päätavoitetta; riippuvuus nimetty ilman syytä; reflektio ei nimeä muutosta).

### lesson-18 — AT2: Pseudokoodi ja jäljitys omasta prosessista (5 kriteeriä)

Viisi kriteeriä on perusteltu: AT2 kokoaa kolmen oppitunnin (L16, L17, L18) erilliset tavoitteet, ja jokainen rivi mittaa aidosti eri osaamista.

| # | Kriteeri (nimi sanasta sanaan) | Mittaa | Mitä mitataan | S+ erottuu näin |
|---|---|---|---|---|
| K1 | Pseudokoodin rakenne | O18.1 | 10–20 riviä; kurssin avainsanat ISOIN KIRJAIMIN; vähintään yksi IF ja yksi WHILE/FOR; lohkot sisennetty; prosessi on oma arkiprosessi, ei oppikirjaesimerkki. | Ehto ja toisto ovat prosessin kannalta välttämättömiä (eivät päälle liimattuja), ja syöte–käsittely–tuloste-runko on tunnistettavissa ilman selitystä. |
| K2 | Muuttujien nimeäminen | O18.2 | Jokainen muuttuja on nimetty niin, että nimi kertoo sisällön (`teekuppienMaara`, ei `x`). SET/READ/WRITE-muodot ovat oikein. | Muuttujia on vain tarpeellinen määrä ja väliarvot (kuten `length`, `hasDigit`) tekevät ehdosta luettavan. |
| K3 | Jäljitystaulukot | O18.3 | Kaksi käsin tehtyä taulukkoa: normaali ja hankala syöte. Sarake per muuttuja + tulostesarake, rivi per suoritettu rivi; WHILE-ehdon uudelleentarkistus näkyy. | Hankala syöte on aidosti rajatapaus prosessista (tyhjä, nolla, loppu) ja jäljitys on täydellinen pysähtymiseen asti — ei "…" -oikaisuja. |
| K4 | Bugin paikantaminen ja korjaus | O18.4 | Reflektio tai erillinen merkintä nimeää rivinumeron, jolla toteutunut ja odotettu tuloste erosivat, bugityypin yleiskielellä (tehtävän 6.2 neljä tyyppiä) ja tehdyn korjauksen; tai perustelee jäljityksellä, että hankala syöte toimi. | Korjattu versio on jäljitetty uudelleen ja uusi taulukko on mukana; tai jos bugia ei ollut, opiskelija nimeää toisen hankalan syötteen, joka olisi rikkonut koodin. |
| K5 | Reflektio yleiskielellä | O18.5 | 5 virkettä: mitä pseudokoodi tekee; mikä oli pseudokoodilla vaikeampaa/helpompaa kuin proosalla; mitä jäljitys paljasti, mitä lukeminen ei. | Reflektio sisältää havainnon ulkopuolisesta lukijasta (tehtävä 6.3) tai LLM-jäljityksen erimielisyydestä (tehtävä 6.4) ja sanoo, kumpi oli oikeassa ja miksi. |

ES-taso: pseudokoodi puuttuu, on oikeaa ohjelmointikieltä, tai ehto/toisto puuttuu; jäljitystaulukoita ei ole tai ne ovat selvästi konegeneroituja (ei käsin tehtyjä). S-: rakenne on, mutta jäljitys on vajaa (vain normaali syöte) tai rivinumeroa ei nimetä.

### lesson-24 — AT3: Pseudokoodista toimivaksi ohjelmaksi ja esitys (4 kriteeriä)

| # | Kriteeri (nimi sanasta sanaan) | Mittaa | Mitä mitataan | S+ erottuu näin |
|---|---|---|---|---|
| K1 | Käännös omasta pseudokoodista | O24.1 | 10–25 riviä JS tai C#; vastaa palautettua omaa viikon 6 pseudokoodia rivi riviltä (SET→let/int, IF→if, WHILE→while/for); ohjelma toimii tai epäonnistunut yritys on dokumentoitu virheilmoituksineen. Varamalli → enintään S. | Käännös säilyttää oman pseudokoodin muuttujanimet ja rakenteen, ja opiskelija nimeää yhden kohdan, jossa pseudokoodi ja kieli eivät vastanneet suoraan (esim. REPEAT N TIMES → for-laskuri). |
| K2 | Testaus kahdella lähtöarvolla | O24.2 | Kuvakaappaus näyttää kaksi ajoa eri lähtöarvoilla; pohdinta nimeää muutetun muuttujan ja sen, vastasiko tuloste ennustetta. | Toinen lähtöarvo on rajatapaus (sama henki kuin AT2:n hankala syöte) ja opiskelija kirjaa ennusteen ennen ajoa ja vertaa siihen. |
| K3 | Bugi ja korjaus | O24.3 | Yksi bugi nimetty yleiskielellä, virheilmoitus lainattu sanasta sanaan (tai hiljainen bugi kuvattu tulosteen kautta), korjattu rivi näytetty; 3–5 virkkeen pohdinta. | Opiskelija erottaa syntaksivirheen ja hiljaisen logiikkavirheen (tehtävän 8.4 pätkä B -tyyppi) ja kertoo, kumpi oli vaikeampi löytää ja miksi. |
| K4 | Suullinen esitys | O24.4 | Neljä iskua 2 minuutissa `lisamateriaali-l24-esitysrubriikki.md`:n mukaan (mitä / miten / mikä meni pieleen / miten korjattiin); pidetty livenä tai yksin-vaihtoehdon mukaan. Rubriikki **viittaa** esitysohjeeseen, ei toista sitä. | Esitys vastaa vertaishavaintoon tai opettajan jatkokysymykseen ("mitä tapahtuisi, jos lähtöarvo olisi …") omin sanoin oikein. |

ES-taso: ohjelmaa ei ole eikä epäonnistunutta yritystä ole dokumentoitu; tai esitystä ei ole pidetty missään muodossa. S-: ohjelma toimii ja esitys on pidetty, mutta jokin tehtävän 8.1 neljästä tarkistuksesta on täydennetty jälkikäteen tai kuvakaappaus näyttää vain yhden ajon. S = tehtävän 8.1 kaikki neljä tarkistusta täyttyvät ensimmäisellä kerralla.

---

## Briefing Rasmukselle

Muodon malli on **tehtävä 8.1-JS** (`lahde/viikko-08/opiskelija/opiskelijatehtavat-js.md`): "Tavoite."-kappale, numeroidut vaiheet lyhyinä virkkeinä, "Jos teet tämän yksin", 💡 Vinkki. Golden sample antaa tason ja rekisterin. Älä kopioi kummankaan sisältöä.

Järjestys: AT1 → AT2 → AT3 (jokaisesta ensin `assessment.md`, sitten `rubric.md`, jotta kriteerinimet syntyvät kerran ja kopioituvat sanasta sanaan).

### student/lesson-06/assessment.md — AT1

- H1 `# AT1 — arvioitava tehtävä: Pilko todellinen tehtävä` (otsikkoa saa hioa, muoto ei muutu).
- `## Tavoite`: 3–5 virkettä. Sano, että AT1 on kurssin ensimmäinen arvioitava tehtävä, että se kokoaa viikon 2 tehtävät, ja että arvioija etsii **puolustettavaa**, ei täydellistä pilkkomista (opettajamateriaalin väärinkäsityskorjaus).
- `## Mitä palautat ja milloin`: lista — päätehtävä + tavoite; 4–8 osatehtävää osatavoitteineen; numeroitu järjestys, jossa ≥1 riippuvuus muodossa "X riippuu Y:stä, koska …"; 3–5 virkkeen reflektio. Muoto vapaa: taulukko, kaavio tai tekstirakenne, noin yksi sivu (250–500 sanaa, legacy-arvio). Palautus: L6:n lopussa noin 75 min kohdalla, viimeistään L7:n alussa, opettajan ilmoittamaan kanavaan.
- `## Vaiheet`: 5–7 vaihetta. (1) Valitse oma todellinen tehtävä tehtävästä 2.1, 2.2 tai 2.4 — IT-tehtävä on vahvin ehdokas; arkinen käy. (2) Siisti päätehtävä + tavoite. (3) Osatehtävät ja osatavoitteet, tarkista "mikä on totta, kun tämä on tehty". (4) Järjestä, merkitse riippuvuus ja vapaa osatehtävä (tehtävän 2.3 liike). (5) Parikatselmointi L6:lla: kolme tarkentavaa kysymystä, merkitse yksi muutos. (6) Reflektio, jossa muutos nimetään osatehtävän numerolla. (7) Palauta. Mainitse, että LLM:ää saa käyttää vain tehtävän 2.5 tavalla, ja että LLM:n tekstiä ei liitetä.
- `## Mihin viikon tehtäviin tämä nojaa`: 2.1–2.5 id:llä, yksi virke kustakin ("Tehtävä 2.4 — jos valitsit koulun IT-tehtävän, sen oikeat valikkonimet ovat AT1:n osatehtävien ydin").
- `## Jos teet tämän yksin`: ks. H11.
- `## Arviointikohteet`: neljä kriteerinimeä sanasta sanaan (K1–K4), kunkin alla yksi virke mitä katsotaan. Ei tasokuvauksia.

### teacher/lesson-06/rubric.md — AT1

Template-pohja, 4 riviä K1–K4, `**Mittaa tavoitteita:** O6.1–O6.4`. Tasokuvaukset tämän suunnitelman taulukon mukaan; ES ja S- havainnoitavina.

### student/lesson-18/assessment.md — AT2

- H1 `# AT2 — arvioitava tehtävä: Pseudokoodi ja jäljitys omasta prosessista`.
- `## Tavoite`: AT2 kokoaa viikon 6; "tehtävässä 6.1 tekemäsi työ on se työ, jota AT2 pyytää — ei mitään uutta" (opettajamateriaalin lause, sovita). Ei oikeaa ohjelmointikieltä.
- `## Mitä palautat ja milloin`: pseudokoodi 10–20 riviä kurssin avainsanoilla, ≥1 ehto + ≥1 toisto; kaksi käsin tehtyä jäljitystaulukkoa (normaali + hankala syöte) paperilla tai kuvana; 5 virkkeen reflektio, jossa rivinumero. Palautus noin L18 (luovutus tunnin lopussa).
- `## Vaiheet`: (1) Ota tehtävän 6.1 pseudokoodi tai kirjoita uusi samoilla säännöillä. (2) Tarkista avainsanat, sisennys, muuttujanimet (tehtävän 6.1 vaihe 3). (3) Valitse hankala syöte omasta prosessista. (4) Jäljitä käsin kahdesti L18:n itsenäisessä jaksossa. (5) Ympyröi ensimmäinen eroava rivi, nimeä bugityyppi (tehtävän 6.2 neljä tyyppiä), korjaa ja jäljitä korjattu versio, tai perustele miksi bugia ei ollut. (6) Reflektio 5 virkettä. Jos käytit LLM:ää (6.4), kerro erimielisyys ja kumpi oli oikeassa. (7) Palauta.
- `## Mihin viikon tehtäviin tämä nojaa`: 6.1–6.4 tehtävätiedoston numeroinnilla.
- `## Jos teet tämän yksin`: lyhyt, ks. H11.
- `## Arviointikohteet`: K1–K5 sanasta sanaan.

### teacher/lesson-18/rubric.md — AT2

Template-pohja, 5 riviä K1–K5, `**Mittaa tavoitteita:** O18.1–O18.5`. ES-kuvauksiin: "oikea ohjelmointikieli pseudokoodin sijaan" ja "jäljitystaulukko ei ole käsin tehty" ovat hylkäysperusteita.

### student/lesson-24/assessment.md — AT3

- H1 `# AT3 — arvioitava tehtävä: Pseudokoodista toimivaksi ohjelmaksi`.
- `## Tavoite`: kurssi sulkee silmukan — oma viikon 6 pseudokoodi → toimiva ohjelma → yksi bugi korjattu → selitetty ääneen. Kieliagnostinen: JS tai C#, opiskelijan valinta. Yksi virke: "Tehtävän 8.1 neljä tarkistusta ovat hyväksytyn (S) kynnys; arviointi erottelee lisäksi S-, S ja S+."
- `## Mitä palautat ja milloin`: H3 `### Kirjallinen osa (oppitunnin 23 lopussa)`: lähdekoodi (`at3.js` tai `at3.cs` tai koodilohko), se pseudokoodi josta käännös tehtiin, kuvakaappaus kahdesta ajosta, 3–5 virkkeen pohdinta (mitä ohjelma tekee, mikä bugi, mikä korjaus, virheilmoitus sanasta sanaan). H3 `### Suullinen osa (oppitunnilla 24)`: 2 min, neljä iskua, viittaus esitysohjeeseen `lisamateriaali-l24-esitysrubriikki.md`.
- `## Vaiheet`: kieliagnostinen runko 6–8 vaihetta (valitse pseudokoodi → käännä → aja → toinen lähtöarvo + kuvakaappaus → bugi + korjaus → pohdinta → harjoittele esitys → palauta/esitä). H3 `### JavaScript-polku` ja `### C#-polku` ovat kumpikin **1–2 virkettä**: "Kielikohtaiset vaiheet, käännöstaulukko ja ympäristö (selaimen konsoli / .NET Fiddle) ovat tehtävässä 8.1-JS / 8.1-CS." Ei koodia tähän tiedostoon.
- `## Mihin viikon tehtäviin tämä nojaa`: 8.1-JS/8.1-CS (AT3-ohje), 8.2 (silmukkamallit), 8.4 (virheilmoitusten lukeminen), 8.3 ja 8.5 valinnaisina, sekä AT2/6.1 (lähdepseudokoodi). Mainitse, että varamalli on sallittu mutta rajaa K1:n tasolle S.
- `## Jos teet tämän yksin`: ks. H11, sama kuin 8.1.
- `## Arviointikohteet`: K1–K4 sanasta sanaan.

### teacher/lesson-24/rubric.md — AT3

Template-pohja, 4 riviä K1–K4, `**Mittaa tavoitteita:** O24.1–O24.4`. K4-solut viittaavat esitysohjeen neljään iskuun ja neljään tarkistukseen; eivät toista niiden tekstiä. Lisää taulukon jälkeen yksi virke: "Tehtävän 8.1 neljä tarkistusta täyttyvät = vähintään S."

### Yleiset ohjeet Rasmukselle

- Ei 🟢/🟣 AT-otsikoihin. Ei "AI-resilientti". Ei tilaajan nimeä. Ei putken nimiä.
- Jokainen viittaus osatehtävään on muotoa "tehtävä 2.4" / "tehtävä 6.1" / "tehtävä 8.1-JS"; ei vaiheiden uudelleenkirjoitusta.
- Älä vaadi mitään, mitä viikkotehtävät eivät ole valmistelleet. AT = koonti, ei uusi vaatimus.
- Älä muuta viikkotehtävien numerointia tai tekstiä, vaikka huomaisit virheen; kirjaa se orkestraattorille.

---

## Manifestiluonnos

`/home/claude/oa-at/tuotanto/course.draft.json` — D3-skeeman mukainen osittainen manifesti, joka sisältää vain kolme assessment-oppituntia.

- `course`: slug `ohjelmallinen-ajattelu`, kieli fi, golden sample `~/Kurssit/ai-perusteet/`, `forbidden_terms` H9:n mukaan.
- `modules`: `module-2` (viikko 2 → lesson-06), `module-6` (viikko 6 → lesson-18), `module-8` (viikko 8 → lesson-24). Viikkojen muut oppitunnit eivät ole tässä luonnoksessa; Alfred yhdistää ne kurssin täyteen manifestiin tai legacy-rakenteeseen.
- `lessons`: kolme oppituntia `type=assessment`, `concepts: []` (kokoavia, eivät opeta uutta), `builds_on` legacy-oppitunteihin, `tasks` = AT:n oma id (`AT1`/`AT2`/`AT3`, MANDATORY, assessable=true, ai_resilient=true) sekä osatehtävät, joihin AT nojaa (assessable=false; luokka ja ai_resilient viikkotehtävien mukaan). Skeemassa ei ole erillistä viittauskenttää, joten osatehtävät ovat task-rivejä — ks. avoin kysymys 2.
- `rubric`: `teacher/lesson-06/rubric.md`, `teacher/lesson-18/rubric.md`, `teacher/lesson-24/rubric.md`.

---

## Avoimet kysymykset

1. **AT3:n sijoitus lesson-24:ään vs. lesson-23.** Brief sanoo "L23–L24"; tämä suunnitelma lukitsee manifest-id:n lesson-24 (arviointi täydentyy esityksessä), ja `assessment.md` kertoo kirjallisen palautuksen L23:n lopussa. Jos orkestraattori haluaa `student/lesson-23/assessment.md`, vain polku ja manifest-id vaihtuvat, sisältö ei.
2. **Osatehtävät manifestissa.** Skeeman `tasks`-objekti ei salli lisäkenttiä (`additionalProperties: false`), joten viittaukset osatehtäviin on kirjattu task-riveinä (assessable=false). Nämä tehtävät elävät legacy-viikkotiedostoissa, eivät `student/lesson-XX/student-tasks.md`:ssä. Wilhelmin manifest↔md-tarkistus pitää ohjeistaa resolvoimaan ne `assessment.md`:n `## Mihin viikon tehtäviin tämä nojaa` -osiosta (H5), ei student-tasks.md:stä. Vaihtoehto: orkestraattori karsii osatehtävärivit ja jättää vain AT-rivit.
3. **builds_on viittaa oppitunteihin, joita luonnoksessa ei ole** (lesson-01, -04, -05, -13…-17, -20…-23). Skeema ei vaadi resolvointia, mutta Linnea/Wilhelm saattavat. Alfredin pitää yhdistää tämä osittainen manifesti kurssin täyteen `course.json`:iin tai legacy-viikkorakenteeseen vientivaiheessa.
4. **Olemassa olevan 8.1:n "Hyväksytty / ei vielä hyväksytty" vs. ES/S-/S/S+.** Ratkaisu tässä suunnitelmassa: neljä tarkistusta = S-kynnys (H14). Jos Matti haluaa AT3:n pysyvän puhtaasti hyväksytty/täydennettävä-mallissa, rubriikin K1–K4 supistetaan kaksitasoiseksi — päätös orkestraattorille.
5. **Varamallin vaikutus AT3:n arvosanaan.** Suunnitelma rajaa varamallilla tehdyn K1:n enintään tasolle S. Tämä on uusi linjaus, jota 8.1 ei sano; vahvistettava.
6. **Viikon 6 numerointipoikkeama** (diat 6.1/6.3/6.4/6.5 vs. tiedosto 6.1–6.4). Noudatetaan tiedostoa. Diat olisi hyvä korjata erillisessä ajossa — ei tämän ajon asia.
7. **AT2:n käsin tehdyn jäljitystaulukon palautusmuoto.** Suunnitelma sallii paperin tai kuvan. Jos kurssialusta vaatii tekstiä, vaatimus "käsin tehty" heikkenee ja AI-resilienssi nojaa rivinumero-sidontaan (H10 AT2 c). Vahvistettava palautuskanava.
8. **AT1:n sanamäärähaarukka 250–500** tulee opettajamateriaalin opiskelijakysymysvastauksesta, ei toimeksiannosta. Käytetään ohjeellisena, ei rubriikkikriteerinä.

## Orkestraattorin päätökset avoimiin kysymyksiin (2026-11-04)

1. AT3 pysyy polussa lesson-24 (kirjallinen palautus L23:n lopussa, esitys L24).
2. Osatehtävät pysyvät manifestissa task-riveinä assessable=false; Wilhelm resolvoi ne assessment.md:n "Mihin viikon tehtäviin tämä nojaa" -osiosta.
3. builds_on-viittaukset legacy-oppitunteihin hyväksytään sellaisenaan; tämä on osittainen manifesti.
4. Kaikki kolme AT:ta arvioidaan asteikolla ES / S- / S / S+. Tehtävän 8.1 "hyväksytty / ei vielä hyväksytty" -tarkistus säilyy opiskelijan itsetarkistuksena, S-kynnyksenä.
5. Varamallin käyttö AT3:ssa rajaa kriteerin K1 tasolle S (ei S+). Kirjataan opiskelijalle näkyviin.
6. AT2:n käsin tehty jäljitystaulukko palautetaan paperilla tai valokuvana; molemmat kelpaavat.
