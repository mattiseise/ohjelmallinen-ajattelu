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

## Alkuperä ja säilytys

Viikkoaineisto, PDF:t, manifesti, tuotantoartefaktit ja historialliset versiot kopioitiin kurssikansion sisareen suhteutetusta lähteestä `../tyokalut/material-pipeline/ohjelmallinen_ajattelu/`. Alkuperäistä lähdehakemistoa ei siirretty, poistettu eikä muokattu. Kurssikansion jo olemassa ollut `AT-tehtavat/` säilytettiin muuttamattomana. Kaikkien 307 mukaan otetun alkuperäisen aineistotiedoston tavut tarkistettiin SHA256-vertailulla.

Vanhoissa suunnitelmissa ja `tuotanto-AT/state.json`-tiedostossa on tuotantoajon konekohtaisia polkuviitteitä. Ne on säilytetty historiana muuttamattomina; niitä ei pidä käyttää tämän repon toimivina polkuasetuksina. `course.at.json` sisältää myös paikallisen vertailukurssin viitteen. Repo ei sisällä koko material-pipeline-työkalua eikä sen muita kursseja.

## Versionhallinnan rajaus

Mukana ovat kaikki kahden lähdekokonaisuuden kurssiaineistot, myös varmuuskopiot ja vanhentuneiksi merkityt versiot. Vain 13 macOS:n `.DS_Store`-metatietotiedostoa jätettiin alkuperäisestä inventaariosta versionhallinnan ulkopuolelle. `.gitignore` estää lisäksi tunnusten, lokien ja väliaikaistiedostojen vahinkolisäyksiä; näitä ei löytynyt mukaan otettavasta aineistosta.

Git-versionhallinta ei ole verkkosivujulkaisu: tähän talteenottoon ei lisätä GitHub Pagesia, Actions-työnkulkuja eikä automaattista deployta. Oppimateriaalin sisällön kehittäminen ja mahdollinen myöhempi julkaisu tehdään erillisinä päätöksinä.
