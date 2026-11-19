# Viikko 7 — Pseudokoodista koodiin

Ohjelmallinen ajattelu

1. vuoden ammatillinen ICT-kurssi

Kaksi kieltä, yksi ajattelutapa — JavaScript ja C# rinta rinnan.

---

## Keskeinen kysymys vielä kerran

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla vastaamme siihen vihdoin — koodina.

---

## Mitä tämä viikko harjoittaa

- Oppitunti 19 — **miksi** ohjelmointikieli on olemassa ja mitä *syntaksi* tarkoittaa (ei vielä toimivaa koodia)
- Oppitunti 20 — ensimmäiset käskyt **JavaScriptillä ja C#:lla** rinta rinnan: tuloste, arvot, muuttujat
- Oppitunti 21 — ensimmäiset päätökset **JavaScriptillä ja C#:lla** rinta rinnan: `if`, `else`, vertailut

---

## Miksi ohjelmointikieli?

Pseudokoodi on tarkoitettu **ihmisseuraajalle**, joka osaa englantia.

Oikea koodi on tarkoitettu **tietokoneelle**: kiinteän sanalistan sananmukaiselle tulkitsijalle.

Ajattelu on sama. Sanat kiristyvät.

---

## Mitä syntaksi on?

Sääntö siitä, *miten sanat täytyy järjestää*, jotta lukija osaa jäsentää ne.

- Arjessa: englanniksi sanomme "the red car"; suomeksi "punainen auto" — eri sanajärjestys.
- IT:ssä: `Users/maria/documents/report.txt` on kelvollinen polku; sama välilyönnillä ja ilman kauttaviivaa ei ole.

Tietokone ei ole antelias. Jos syntaksi on rikki, se pysähtyy ja kertoo missä.

---

## Kaksi kieltä, jotka kohtaamme

- **JavaScript** — ajetaan jokaisessa selaimessa (Chrome, Firefox, Edge, Safari). Verkkosivut, Node.js-palvelimet.
- **C#** — ajetaan .NET:ssä. Työpöytäsovellukset, web-palvelimet, pelit (Unity).

Näet molemmat, jokaisen käsitteen, rinta rinnan.

> *Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone osaa noudattaa niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain se syntaksi, jolla se kirjoitetaan.*

---

## Hello, console — rinta rinnan

#### JavaScript

```javascript
console.log("Hei, konsoli");
```

#### C#

```csharp
Console.WriteLine("Hei, konsoli");
```

Sama työ — tulosta yksi rivi. Eri sanat, sama idea.

---

## Selainkonsolin avaaminen (JavaScript)

- Mac: `Cmd + Opt + J`
- Windows / Linux: `Ctrl + Shift + J`
- Tai: hiiren oikea klikkaus → **Tarkasta** → **Konsoli**-välilehti

Liimaa rivi JavaScriptiä, paina Enter, lue tuloste.

---

## Online-C#-ympäristön avaaminen

- Mene osoitteeseen **`dotnetfiddle.net`** millä tahansa selaimella.
- Valitse **Console** yläosasta.
- Liimaa C#-koodi `Main`-metodin sisään, paina **Run**.

Ei tiliä, ei asennusta. Myös `sharplab.io` ja Replit toimivat.

---

## Muuttujat — rinta rinnan

#### JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(age);
```

#### C#

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(age);
```

C# nimeää tyypin (`string`, `int`); JavaScript päättelee sen. Yksi ylimääräinen sana, sama ajattelu.

---

## Ensimmäinen laskutoimitus — rinta rinnan

#### JavaScript

```javascript
let age = 16;
let years = 18 - age;
console.log(years);
```

#### C#

```csharp
int age = 16;
int years = 18 - age;
Console.WriteLine(years);
```

Algoritmi on identtinen: *tee age, laske erotus, tulosta tulos.*

---

## Ennusta ennen ajamista

Katso jokaista riviä. **Ennen** Run-painikkeen klikkaamista kirjoita, mitä odotat.

Sitten aja se. Vertaa ennustusta todellisuuteen.

Jos ne eroavat, rivi, jossa ne eroavat ensin, on bugisi.

Tämä on viikon 6 käsiajo, nyt koodissa.

---

## Vertailuoperaattorit

| Operaattori | Merkitys                  |
|-------------|---------------------------|
| `==`        | yhtä kuin                 |
| `!=`        | eri kuin                  |
| `>`         | suurempi kuin             |
| `>=`        | suurempi tai yhtä suuri   |
| `<`         | pienempi kuin             |
| `<=`        | pienempi tai yhtä suuri   |

Olennaisesti identtiset JavaScriptissä ja C#:ssa.

---

## Ensimmäinen if/else — rinta rinnan (iän rajoitus -tarkistus)

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
} else {
  console.log("Olen pahoillani, ei vielä.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18) {
    Console.WriteLine("Pääset sisään.");
} else {
    Console.WriteLine("Olen pahoillani, ei vielä.");
}
```

Sama `if`, sama `>=`, sama `else`, samat aaltosulkeet. Ajattelu on se, mikä kantaa.

---

## Tehtävät tällä viikolla

- **Yksi** must-do-minimi-tehtävä valitsemallasi kielellä — tulosta, esittele, laske, `if/else`.
- 2–3 syventävää tehtävää: tee se toisella kielellä; käännä viikon 6 pseudokoodi; riko se tarkoituksella.
- Katso `student-tasks-js.md` ja `student-tasks-csharp.md`.

Tallenna koodisi — **AT3 saapuu viikon 8 lopussa** ja käyttää sitä uudelleen.

---

## Kielen valinta AT3:lle

- Valitse se, joka näyttää vähemmän pelottavalta side-by-side-kalvoilla.
- Voit vaihtaa milloin tahansa.
- AT3:n arvosana ei riipu siitä, minkä kielen valitset.
- Asennusta ei tarvita: selainkonsoli (JS) tai .NET Fiddle (C#).

---

## Mitä tulee seuraavaksi — viikko 8

- **Silmukat** koodissa — viikon 6 `WHILE` / `FOR` saapuvat muodossa `while` / `for`, rinta rinnan.
- **Oikeat virheilmoitukset** oppimisen työkaluna.
- **AT3** — käännä yksi pala omaa viikon 6 pseudokoodiasi pieneksi ajettavaksi ohjelmaksi.

---

## Yhteenveto — keskeinen kysymys vielä kerran

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla: **ohjelmointikielellä** — JavaScriptillä tai C#:lla, rinta rinnan, ilman asennusta.

Ajattelu on se asia. Syntaksi on sopimus.
