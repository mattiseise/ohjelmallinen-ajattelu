# Linnea — pedagoginen audit, kierros 3 (vain AT3, itsenäistetty versio)

Auditoitu: `materiaali/student/lesson-24/assessment.md` (1299 sanaa), `materiaali/teacher/lesson-24/rubric.md` (ennallaan)
Vertailu: `audit/AT3-v1-ennen-itsenaistamista.md` (840 sanaa)
Päivä: 2026-11-06

## Päätös

**korjattava** — yksi täsmäkorjaus käännöstaulukkoon (molemmat polut) ja yksi täydennys varamalliin. Muuten itsenäistäminen onnistui: tehtävä on tehtävissä tästä tiedostosta, AI-resilienssi säilyy, rubriikki mittaa edelleen O24.1–O24.4. Korjausten jälkeen jatka Wilhelmille ilman uutta Linnea-kierrosta.

---

## (1) Tehtävissä ilman 8.1:tä ja esitysohjetta?

Lähes. Tiedostossa on nyt ympäristö (DevTools / .NET Fiddle), käännöstaulukko, bugin aiheuttaminen esimerkkivirheilmoituksineen, tallennusnimi, esityksen neljä kohtaa, ajoitus, opettajan neljä tarkistusta ja vertaishavainto. Kaksi aukkoa:

**Korjattava 1 — `student/lesson-24/assessment.md`, vaihe 1.** "Saat käyttää tehtävän 8.1 varamallia" — varamalleja (ikärajan tarkistus, salasanan pituustarkistus, pisteistä palautteeksi, laskuri 1–5, tervehdys nimellä kolme kertaa) ei ole tällä sivulla. Juuri se opiskelija, jolla ei ole omaa pseudokoodia, on todennäköisimmin myös se, jolla 8.1 ei ole auki. Lisää viisi varamallia sulkeisiin vaiheeseen 1 (yksi rivi). Samalla "viikon 6 avainsanoilla" → listaa avainsanat sulkeissa (SET, READ, WRITE, IF/ELSE/ENDIF, WHILE/ENDWHILE, FOR/ENDFOR), koska varamalliopiskelija ei välttämättä muista niitä.

**Korjattava 2 — `student/lesson-24/assessment.md`, JavaScript-polku taulukko rivi `SET nimi TO arvo` ja C#-polku vastaava rivi.** Taulukko kääntää SET:n aina muotoon `let nimi = arvo;` / `int nimi = arvo;`. AT2:n pseudokoodissa on pakollinen toisto, ja laskurisilmukassa on lähes aina `SET laskuri TO laskuri - 1` silmukan sisällä. Taulukon mukaan käännettynä se tuottaa JS:ssä `ReferenceError`/`SyntaxError: Identifier has already been declared` ja C#:ssa `CS0136`. Opiskelija saa bugin, jota ohje itse aiheuttaa, eikä sitä voi korjata taulukon avulla. Kun taulukko on tiedoston ainoa käännösohje (8.1:n `self-study.md` ei ole käytössä), tämä on todellinen aukko. Lisää kumpaankin taulukkoon rivi: `SET nimi TO uusi arvo` (muuttuja on jo luotu) → `nimi = uusi arvo;` — ilman `let`/`int`. Yksi rivi, ei lisää kuormaa.

## (2) AI-resilienssi

Säilyy ennallaan: oma pseudokoodi palautetaan ja verrataan AT2:een (tai varamalli pseudokoodiksi kirjoitettuna, S-rajalla); kuvakaappaus omasta ympäristöstä kahdella ajolla; ennuste ennen ajoa omana rivinään; virheilmoitus sanasta sanaan omana rivinään; live-esitys + vertaishavainto + jatkokysymys. Käännöstaulukon ja esimerkkivirheilmoitusten tuominen sivulle ei heikennä mitään näistä — taulukko ei tee työtä opiskelijan puolesta, koska lähdepseudokoodi on hänen omansa.

## (3) Polkujen ja päävaiheiden ristiriidattomuus

Ei ristiriitoja. Päävaihe 2 → polun vaihe 2 (taulukko), päävaihe 3 → polun 3 (ennuste ennen Enteriä/Runia), päävaihe 4 → polun 4, päävaihe 5 → polun 5 ("polkusi vaiheen 5 tapaan" osuu oikeaan), polun vaihe 6 (tallennus) → kirjallisen osan kohta 1. Virke "Vaiheet 2–5 tehdään valitsemallasi kielellä" on hieman kapea (polun vaiheet 1 ja 6 ovat myös kielikohtaisia), mutta ei johda harhaan. Hiljaisen bugin esimerkki `if (ika = 18)` on nyt sivulla, joten viittaus 8.4:ään ei ole enää välttämätön.

**Huomio A — terminologia:** Tavoite ja vinkki sanovat "suullisen osan neljä tarkistusta", rubriikin loppuvirke "tehtävän 8.1 neljä tarkistusta". Sama sisältö, eri nimi; opettaja, joka lukee molemmat, voi luulla niitä eri listoiksi. Yhdenmukaista rubriikin rivi 13 muotoon "Suullisen osan (tehtävän 8.1) neljä tarkistusta". Ei edellytä kierrosta.

## (4) Kuorma 15–18-vuotiaalle

1299 sanaa on kaksinkertainen H7:n haarukkaan (450–800) nähden, mutta lukukelpoinen, koska rakenne kantaa: opiskelija lukee Tavoitteen, Mitä palautat, päävaiheet ja **yhden** polun — toinen polku (n. 180 sanaa) ja viittausosio ohitetaan. Tehollinen lukukuorma on noin 1000 sanaa, mikä vastaa tehtävää 8.1 + esitysohjetta yhdessä. Ei karsittavaa, joka ei samalla rikkoisi itsenäisyyttä. Kaksi kevennystä, jotka eivät vie sisältöä: (a) "Mihin viikon tehtäviin tämä nojaa" voi lyhentyä kolmeen virkkeeseen, koska sivu ei enää nojaa niihin; (b) Suullisen osan kappale on yksi 90 sanan tekstimöhkäle — pilko kahdeksi (ajoitus / opettajan neljä tarkistusta). Huomioita, ei vaatimuksia.

**Huomio B — H7-kontrakti:** suunnitelma sanoi "ei koodilohkoja (AT3)" ja "ei koodia tähän tiedostoon"; nyt sivulla on käännöstaulukot ja inline-koodia. Orkestraattori hyväksyi itsenäistämisen, joten tämä on tietoinen poikkeama — Wilhelmin H7-tarkistus pitää ohjeistaa hyväksymään se, ettei se kaadu siihen.

## (5) Rubriikki ja arviointikohteet

Rubriikki ennallaan; neljä kriteerinimeä täsmäävät arviointikohteisiin sanasta sanaan ja samassa järjestyksessä. K1 ↔ O24.1 (varamallipolku yhdessä solussa, r2:n korjaus tehty), K2 ↔ O24.2, K3 ↔ O24.3, K4 ↔ O24.4. S+ laadullisesti eri taso jokaisessa. Arviointikohteiden K4-virke "suullisen osan ohjeen mukaan" osoittaa nyt tähän sivuun, rubriikin K4 S edelleen `lisamateriaali-l24-esitysrubriikki.md`:hen — sisältö sama, ja sivu sanoo, että opettaja heijastaa saman ohjeen. Kelpaa.

---

## Korjausvaatimukset Rasmukselle

1. Vaihe 1: viisi varamallia ja kurssin avainsanat sulkeisiin (yksi–kaksi riviä).
2. JS- ja C#-käännöstaulukot: lisärivi `SET nimi TO uusi arvo` (muuttuja jo luotu) → `nimi = uusi arvo;` ilman `let`/`int`.
3. Huomiot A–B ja kuormakevennykset harkinnan mukaan.

## Seuraava

palauta Rasmukselle korjattavaksi (kaksi täsmäkorjausta) → sen jälkeen jatka Wilhelmille; Wilhelmille tieto H7-poikkeamasta
