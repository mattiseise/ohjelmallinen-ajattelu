# Viikko 7 — Pseudokoodista koodiin

Ohjelmallinen ajattelu

Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi

Kaksi kieltä, yksi tapa ajatella — JavaScript ja C# rinnakkain.

---

## Keskeinen kysymys, vielä kerran

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla vastaamme siihen vihdoin — koodilla.

---

## Mitä tällä viikolla harjoitellaan

• Oppitunti 19 - miksi ohjelmointikieli on olemassa ja mitä *syntaksi* tarkoittaa (ei vielä
toimivaa koodia).
• Oppitunti 20 - ensimmäiset komennot JavaScriptissä ja C#:ssa rinnakkain: tuloste, arvot,
muuttujat.
• Oppitunti 21 - ensimmäiset päätökset JavaScriptissä ja C#:ssa rinnakkain: `if`, `else`, vertailut.

### Vinkki: katso kahta kieltä rinnakkain. Etsi sama ajatus, vaikka kirjoitusasu muuttuu. ---

## Miksi ohjelmointikieli?

Pseudokoodi on ihmistä varten: ihminen lukee englanninkielisiä ohjeita.
Oikea koodi on tietokonetta varten: se on kiinteän sanalistan kirjaimellinen tulkitsija.
Ajattelu on sama. Sanat tiukentuvat.

### Ajattele näin: ohjelmointikieli ei muuta ongelmaa, vaan tekee ohjeesta koneelle suoritettavan. ---

## Mitä syntaksi tarkoittaa?

• Syntaksi on sääntö siitä, *miten sanat täytyy järjestää*, jotta lukija voi jäsentää ne.
• Arki: englanniksi sanotaan "the red car", suomeksi "punainen auto" - eri sanajärjestys.
• IT: `Users/maria/documents/report.txt` on kelvollinen polku; sama välilyönnillä ja ilman
vinoviivaa ei ole.
• Tietokone ei ole armollinen. Jos syntaksi on rikki, se pysähtyy ja kertoo missä.

### Vinkki: virheilmoitus on usein kartta syntaksivirheen luo. ---

## Kaksi kieltä, joihin tutustumme

• JavaScript - toimii jokaisessa selaimessa (Chrome, Firefox, Edge, Safari). Verkkosivut,
Node.js-palvelimet.
• C# - toimii .NET-alustalla. Työpöytäsovellukset, verkkopalvelimet, pelit (Unity).
• Näet molemmat, jokaisen käsitteen, rinnakkain.
• > *Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone voi seurata niitä
arvaamatta. Ajattelu on sitä, mitä olemme tehneet koko kurssin; kieli on vain syntaksi, johon
ajatus kirjoitetaan.* ---

## Hei, konsoli - rinnakkain

JavaScript

```javascript
console.log("Hei, konsoli");
```

C#

```csharp
Console.WriteLine("Hei, konsoli");
```

### Vinkki: molemmat rivit tekevät saman asian: ne kirjoittavat tekstin näkyviin. ---

## Selaimen konsolin avaaminen (JavaScript)

• Mac: `Cmd + Opt + J`
• Windows / Linux: `Ctrl + Shift + J`
• Tai: napsauta oikealla → Inspect / Tarkista → Console-välilehti
• Liitä yksi rivi JavaScriptiä, paina Enter ja lue tuloste.

### Tee näin: kokeile ensin yhtä `console.log`-riviä ennen pidempää koodia. ---

## Verkossa toimivan C#-ympäristön avaaminen

• Mene selaimessa osoitteeseen `dotnetfiddle.net`.
• Valitse ylhäältä Console.
• Liitä C#-koodi `Main`-metodin sisään ja paina Run.
• Ei tiliä, ei asennusta. Myös `sharplab.io` ja Replit toimivat.

### Vinkki: jos et näe tulostetta, tarkista, että koodi on Main-lohkon sisällä. ---

## Muuttujat - rinnakkain

JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(age);
```

C#

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(age);
```

### Ajattele näin: JavaScript antaa muuttujan tyypin päätellä itse; C# haluaa tyypin näkyviin,

esimerkiksi `int` tai `string`. ---

## Ensimmäinen lasku - rinnakkain

JavaScript

```javascript
let age = 16;
let years = 18 - age;
console.log(years);
```

C#

```csharp
int age = 16;
int years = 18 - age;
Console.WriteLine(years);
```

### Vinkki: ennusta ensin tuloste. Tässä `years` saa arvon 2. ---

## Ennusta ennen kuin suoritat

Katso jokaista riviä. Ennen kuin painat Run, kirjoita, mitä odotat tapahtuvan.
Suorita sitten. Vertaa ennustetta todellisuuteen.
Jos ne eivät täsmää, ensimmäinen rivi, jossa ne eroavat, on bugisi.
Tämä on viikon 6 kuivaharjoittelua - nyt koodilla.

### Tee näin: älä vain "katso mitä käy". Kirjoita ennuste ylös ennen ajoa. ---

## Vertailuoperaattorit

```
Operaattori | Merkitys
-----------|---------------------------
== | yhtä suuri kuin
!= | eri suuri kuin
> | suurempi kuin
>= | suurempi tai yhtä suuri kuin
< | pienempi kuin
<= | pienempi tai yhtä suuri kuin
```

### Vinkki: `=` asettaa arvon monissa kielissä, mutta `==` vertailee arvoja. ---

## Ensimmäinen if/else - rinnakkain (ikärajatarkistus)

JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
} else {
  console.log("Valitettavasti et vielä.");
}
```

C#

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("Pääset sisään.");
}
else
{
    Console.WriteLine("Valitettavasti et vielä.");
}
```

Sama `if`, sama `>=`, sama `else`, samat aaltosulkeet. Ajattelu on se, joka kantaa.

---

## Tämän viikon tehtävät

• Yksi pakollisen vähimmäistason tehtävä valitsemallasi kielellä: tulosta, määrittele muuttuja,
laske, käytä `if/else`-rakennetta.
• 2-3 syventävää tehtävää: tee sama toisella kielellä, käännä viikon 6 pseudokoodi, riko koodi
tahallaan.
• Katso tiedostot `student-tasks-js.md` ja `student-tasks-csharp.md`.
• Tallenna koodisi - AT3 tulee viikon 8 lopussa ja käyttää sitä uudelleen.

### Tee näin: valitse ensin yksi kieli. Toista kieltä voi käyttää syventämiseen. ---

## Kielen valitseminen AT3:een

• Valitse se, joka näyttää rinnakkaisilla dioilla vähemmän pelottavalta.
• Voit vaihtaa milloin tahansa.
• AT3:n arvosana ei riipu siitä, minkä kielen valitset.
• Asennusta ei tarvita: selaimen konsoli (JS) tai .NET Fiddle (C#).

### Vinkki: helpoin kieli on se, jolla saat ajatuksesi toimimaan nyt. ---

## Seuraavaksi - Viikko 8

• Silmukat koodissa - viikon 6 `WHILE` / `FOR` saapuvat muotoina `while` / `for`, rinnakkain.
• Oikeat virheilmoitukset oppimisen työkaluna.
• AT3 - käännät yhden oman viikon 6 pseudokoodisi pieneksi toimivaksi ohjelmaksi.

### Vinkki: säilytä toimiva ja rikkinäinen versio. Virheen korjaaminen on osa näyttöä.

---

## Kertaus - keskeinen kysymys, vielä kerran

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla: ohjelmointikielellä — JavaScriptillä tai C#:lla, rinnakkain, ilman asennusta.

Ajattelu on tärkeintä. Syntaksi on sopimus.
