# Wilhelm — audit, kierros 2 (vain AT3, itsenäistetty versio)

Auditoitu: `materiaali/student/lesson-24/assessment.md`, `materiaali/teacher/lesson-24/rubric.md`
Vasten: `01-suunnitelma.md` H2–H6, H9, H14–H15; orkestraattorin hyväksymät poikkeamat (H7: sanaraja 1400, inline-koodi ja kaksi käännöstaulukkoa sallittu); Linnea r3; lähteet `lahde/viikko-08/opiskelija/opiskelijatehtavat-js.md`, `-csharp.md`, `lisamateriaali-l24-esitysrubriikki.md`, `opettaja/opettajan-materiaalit.md`.
Päivä: 2026-11-06

## Päätös

**approved**

## Blocking-löydökset

Ei löydöksiä.

## Non-blocking-parannukset

1. `student/lesson-24/assessment.md` r. 82: "kääntäjä antaa virheen CS0136". CS0136 tulee, kun nimi määritellään uudelleen sisäkkäisessä lohkossa (silmukan sisällä, Linnean skenaario); samassa lohkossa virhekoodi on CS0128. Ei keksittyä syntaksia, mutta koodi ei kata molempia tapauksia. Ehdotus: "kääntäjä antaa virheen (CS0128 tai CS0136)" tai pelkkä "kääntäjä antaa virheen". Alfred/Börje.
2. Lähteiden käännöstaulukkoa (`self-study.md`, "kahdeksan mallia", opettajan materiaalit r. 85) ei ole `lahde/`-kansiossa, joten taulukoita ei voitu verrata sanasta sanaan lähdetaulukkoon. Verrattu 8.1-JS/8.1-CS:n koodiesimerkkeihin ja kielten syntaksiin (ks. evidenssi). Orkestraattorille tiedoksi: jos alkuperäinen taulukko löytyy, vertaa rivit.
3. `teacher/lesson-24/rubric.md` r. 13 sanoo nyt "Suullisen osan neljä tarkistusta" (Linnean huomio A tehty); K4 S-solu viittaa yhä `lisamateriaali-l24-esitysrubriikki.md`:hen, assessment r. 30 sanoo opettajan heijastavan saman ohjeen. Yhdenmukainen; kirjaan näkyviin.
4. `student/lesson-24/assessment.md` r. 43 "Vaiheet 2–5 tehdään valitsemallasi kielellä": polun vaiheet 1 ja 6 ovat myös kielikohtaisia (Linnean huomio). Ei harhaanjohtava.

## Tarkistettu evidenssi

- **H2-otsikot**: lista merkki merkiltä suunnitelman kuusi otsikkoa → True; H1 `# AT3 — arvioitava tehtävä: …` pitkällä viivalla; H3:t vain `## Mitä palautat ja milloin` (Kirjallinen osa / Suullinen osa) ja `## Vaiheet` (JavaScript-polku / C#-polku) -osioissa, H2-sallittujen mukaisesti.
- **Kriteerinimet** assessment `## Arviointikohteet` ↔ rubriikin 1. sarake: 4/4 sanasta sanaan, sama järjestys. Otsikkorivi `| Arviointikohteet | ES | S- | S | S+ |`, Asteikko-rivi, `**Mittaa tavoitteita:** O24.1–O24.4` ennallaan. Rubriikki muuttunut r1:stä vain rivillä 13 ("Suullisen osan neljä tarkistusta").
- **Kielletyt termit**: manifestin 13 termiä + `resilien|resisten|Hyväksytty / ei vielä|🟢|🟣|PAKOLLINEN|SYVENTÄVÄ` → 0 osumaa molemmissa tiedostoissa. (Lähteen 8.1 "Hyväksytty / ei vielä hyväksytty" ei ole kopioitunut.)
- **Tehtävä-id:t** assessment.md:ssä: 6.1, 8.1, 8.1-JS, 8.1-CS, 8.2, 8.3, 8.4, 8.5 → kaikki löytyvät lähdeotsikoista (JS r. 17/73/120/152/198, CS r. 19/79/127/161/206; 6.1 viikko-06 r. 22). Pätkä B `if (ika = 18)` = JS r. 168–170 sanasta sanaan. Varamallien viisi nimeä = 8.1-JS/CS vaihe 1 sanasta sanaan. Suullisen osan neljä kohtaa, 30 s/kohta, ajastin, "Alle ajan on ok; yli ajan ei", opettajan neljä tarkistusta ja "Nimeä yksi asia, jonka huomasit" = esitysrubriikki r. 12–17, 24–27, 33–38, 51.
- **Käännöstaulukot**: JS-rivit `let nimi = arvo;`, `nimi = uusi arvo;`, `console.log(…)`, `if (…) { } else { }`, `while (…) { }`, `for (let i = 0; i < N; i++) { }` — vastaavat 8.1-JS:n esimerkkiä (`let salasana = "hei"; if (salasana.length >= 8) {…} else {…}`, konsoli, `prompt()` ei tarvita) ja validia JS-syntaksia. C#-rivit `int nimi = arvo;` / `string nimi = "arvo";`, `nimi = uusi arvo;`, `Console.WriteLine(…)`, `if/else`, `while`, `for (int i = 0; i < N; i++)` — vastaavat 8.1-CS:n esimerkkiä (`string salasana = "hei"; … Console.WriteLine`), `Console.ReadLine()` ei tarvita, Main-metodi ja Console-tila (8.1-CS vaihe 3), dotnetfiddle.net (CS r. 12). Virheilmoitukset `ReferenceError: salasna is not defined` (opettajan mat. r. 236 sama muoto), `CS0103: The name 'salasna' does not exist in the current context` (opettajan mat. r. 344 sama muoto), "has already been declared" (oikea JS-teksti). Pikanäppäimet `Cmd + Opt + J` / `Ctrl + Shift + J` = JS r. 12. Linnean korjaukset 1–2 (varamallit + avainsanat vaiheessa 1; `SET nimi TO uusi arvo` -rivi molemmissa taulukoissa ilman let/int) todettu tehdyiksi. Ei keksittyä syntaksia.
- **Taulukot**: rubriikin rivit 6 pipea ×6, assessmentin kaksi käännöstaulukkoa 3 pipea ×9 kumpikin (otsikko, erotin, 7 riviä); ei poikkeamia. Inline-koodi backtick-pareina; ```` ``` ````-määrä 0 molemmissa (ei avoimia lohkoja).
- **Numeroinnit** jatkuvia: Kirjallinen osa 1–5, Suullinen osa 1–4, Vaiheet 1–8, JS-polku 1–6, C#-polku 1–6. Polkujen viittaukset "(vaihe 3)…(vaihe 5)" osuvat päävaiheisiin 3–5.
- **YAML**: ei `---`-alkua kummassakaan. Absoluuttisia polkuja 0. Sanamäärä 1277 (raja 1400). Ajoitus "oppitunnin 23 lopussa" + "oppitunnilla 24" (H6). H14-virke assessment r. 5 ja rubriikki r. 13.

## Seuraava

jatka Alfredille
