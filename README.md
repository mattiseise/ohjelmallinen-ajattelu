# Ohjelmallinen ajattelu

Yksityinen versionhallintarepo kahdeksan viikon Ohjelmallinen ajattelu -kurssin lähde- ja oheisaineistolle. Tämä on olemassa olevan aineiston talteenotto, ei verkkosivujulkaisu eikä uusi pedagoginen hyväksyntä. Repoon ei kuulu opiskelijoiden palautuksia, henkilötietoja tai arviointituloksia.

## Aineiston rakenne

- `viikko-01/`–`viikko-08/`: viikkokohtaiset opiskelijan ja opettajan materiaalit, tehtävät, sanastot, diat sekä arvioitavien tehtävien ohjeet ja rubriikit.
- `AT-tehtavat/`: erilliset AT1–AT3-tehtäväohjeet ja opettajan tukimateriaalit, mukaan lukien JavaScript-/C#-versiot ja itslearning-HTML. Nämä säilytettiin alkuperäisillä paikoillaan ja muuttamattomina.
- `course.at.json`: arvioitavien tehtävien manifesti; ei koko kurssin julkaisu- tai rakennusasetusta.
- `translations_fi/`: seitsemän aiemmin tuotettua suomenkielistä PDF-koostetta. Niiden sisältö voi edustaa eri työvaihetta kuin Markdown-lähteet.
- `tuotanto-AT/`: AT-aineiston tuotantosuunnitelmat, työtilan kuvaus ja laadunvarmistusmuistiot. Historiallisia tuotantoartefakteja, ei ajettava tuotantoputki.
- `Backup/`: historialliset kurssi- ja viikkoversiot, mukaan lukien vanhat `materiaali/`- ja `julkaisu/`-hakemistot. Nämä ovat vertailu- ja palautusmateriaalia, eivät tämän repon ajantasaiseksi tai julkaistuksi väitetty versio.
- `viikko-01/_obsolete/`, `viikko-06/_obsolete/` ja `viikko-08/opiskelija/itseopiskelu.md.OLD-AGENT-VERSION`: vanhentuneiksi merkityt työversiot säilytettyinä alkuperäisillä suhteellisilla poluillaan.

Aineiston vanhat READMEt, suunnitelmat ja auditoinnit kuvaavat omaa tuotantohetkeään. Niiden maininnat julkaisusta tai valmiudesta eivät tarkoita, että tämä GitHub-repo olisi julkaistu verkkoon tai että kaikki työversiot olisivat keskenään yhtenevät.

## English version / englanninkielinen aineisto

The English materials are preserved in `English/` alongside the Finnish course; they are an existing-material archive, not a newly approved translation or a website deployment.

- `English/computational-thinking-en-week-01/`–`English/computational-thinking-en-week-08/`: eight weekly packages with student and teacher materials under `release/student/week-NN/` and `release/teacher/week-NN/`, plus the production documents and available PDF/HTML/PPTX outputs. Start with each package's `release/README.md` and student `overview.md`.
- `English/computational-thinking-en/`: a separate historical lesson-01 package. It is **not** merged into week 01 and must not be treated as the current eight-week course.

**Readiness / valmiustaso:** sekä FIN- että EN-aineisto on tallennettu versionhallintaan olemassa olevassa muodossaan. EN sisältää kaikkien kahdeksan viikon opiskelija- ja opettaja-aineiston, mutta talteenotto ei varmista sisällöllistä vastaavuutta FIN-version kanssa, pedagogista hyväksyntää, kaikkien tiedostomuotojen yhtenäisyyttä tai rakennettavuutta. Historiallinen lesson-01 ei ole kokonainen vaihtoehtoinen kurssiversio. Tuotantosuunnitelmissa voi olla suomenkielisiä osia.

The original English source is `../tyokalut/material-pipeline/output/computational-thinking-en*` (the historical package and the eight `-week-01`–`-week-08` packages only). All 217 included files were copied byte-for-byte without editing their contents. The 250-file source inventory excluded 29 `.DS_Store` files, two `.tmp` files and two LibreOffice lock files; originals were left untouched.

Historical build scripts (`build_pdf.py`, `build_slides.py`), briefs and audit notes retain machine-specific paths and external production-tool references. Those paths have not been rewritten, the complete toolchain is not bundled, and rebuilding these outputs has **not** been verified. Existing `release` labels and audit conclusions describe their original production stage, not a fresh publication or acceptance decision.

## Alkuperä ja säilytys

Viikkoaineisto, PDF:t, manifesti, tuotantoartefaktit ja historialliset versiot kopioitiin kurssikansion sisareen suhteutetusta lähteestä `../tyokalut/material-pipeline/ohjelmallinen_ajattelu/`. Alkuperäistä lähdehakemistoa ei siirretty, poistettu eikä muokattu. Kurssikansion jo olemassa ollut `AT-tehtavat/` säilytettiin muuttamattomana. Kaikkien 307 mukaan otetun alkuperäisen aineistotiedoston tavut tarkistettiin SHA256-vertailulla.

Vanhoissa suunnitelmissa ja `tuotanto-AT/state.json`-tiedostossa on tuotantoajon konekohtaisia polkuviitteitä. Ne on säilytetty historiana muuttamattomina; niitä ei pidä käyttää tämän repon toimivina polkuasetuksina. `course.at.json` sisältää myös paikallisen vertailukurssin viitteen. Repo ei sisällä koko material-pipeline-työkalua eikä sen muita kursseja.

## Versionhallinnan rajaus

FIN-aineistosta mukana ovat kaikki kahden lähdekokonaisuuden kurssiaineistot, myös varmuuskopiot ja vanhentuneiksi merkityt versiot. Vain 13 macOS:n `.DS_Store`-metatietotiedostoa jätettiin suomenkielisen aineiston alkuperäisestä inventaariosta versionhallinnan ulkopuolelle. EN-aineiston erillinen rajaus on kuvattu yllä. `.gitignore` estää lisäksi tunnusten, lokien, väliaikaistiedostojen ja toimistosovellusten lukkotiedostojen vahinkolisäyksiä.

Git-versionhallinta ei ole verkkosivujulkaisu: tähän talteenottoon ei lisätä GitHub Pagesia, Actions-työnkulkuja eikä automaattista deployta. Oppimateriaalin sisällön kehittäminen ja mahdollinen myöhempi julkaisu tehdään erillisinä päätöksinä.
