# Viikko 8 — Suljetaan silmukka

---

## Viikko 8 - Silmukka sulkeutuu

Ohjelmallinen ajattelu
Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi

---

## Mitä tällä viikolla tapahtuu

• Oppitunti 22 - silmukat koodissa: `for` ja `while`, rinnakkain JavaScriptissä ja C#:ssa.
• Oppitunti 23 - rakentamispäivä: käännä viikon 6 pseudokoodisi pieneksi toimivaksi
ohjelmaksi.
• Oppitunti 24 - testaa, korjaa yksi bugi, esitä: AT3 palautetaan ja esitetään luokassa.
• > *Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen
JavaScriptiksi tai C#:ksi, suoritat sen, löydät yhden bugin, korjaat sen ja selität, miten se
toimii. Ohjelmointi ei ole enää mystistä.* ---

## Silmukat - muoto (JS ja C# rinnakkain)

JavaScript

```javascript
for (let i = 1; i <= 5; i++) {
console.log(i);
}
```

C#

```csharp
for (int i = 1; i <= 5; i++)
{
Console.WriteLine(i);
}
```

### Vinkki: molemmat tulostavat luvut 1, 2, 3, 4 ja 5. ---

## Laskuri, ehto, runko, päivitys

• `for`-silmukassa on neljä nimettyä osaa:
• Laskuri - `i`, alkaa arvosta 1.
• Ehto - `i <= 5`, tarkistetaan ennen jokaista toistoa.
• Runko - aaltosulkeiden lohko, suoritetaan kerran per toisto.
• Päivitys - `i++`, muuttaa laskuria toistojen välissä.
• Lue ääneen: *"Laskuri alkaa yhdestä; niin kauan kuin se on 5 tai alle, tulosta laskuri ja lisää
yksi."*

### Ajattele näin: silmukka on toisto, jossa pysäytysehto on kirjoitettu näkyviin. ---

## `while`-silmukka (JS ja C# rinnakkain)

JavaScript

```javascript
let count = 0;
while (count < 3) {
console.log("Hei");
count = count + 1;
}
```

C#

```csharp
int count = 0;
while (count < 3)
{
Console.WriteLine("Hei");
count = count + 1;
}
```

### Vinkki: `while` tarkistaa ehdon ennen jokaista kierrosta. ---

## Kun silmukka pyörii ikuisesti

• Jos laskuri ei koskaan muutu, ehto ei koskaan muutu epätodeksi ja runko jatkaa suoritusta.
• Selaimen konsoli - sivu jumittuu; selain varoittaa, että skripti on hidas.
• .NET Fiddle - ajo aikakatkeaa muutaman sekunnin jälkeen.
• Korjaus: varmista, että jokin rungon sisällä muuttaa arvoa, jota ehto testaa.

### Esimerkki: jos `count = count + 1` puuttuu, `count < 3` pysyy totena ikuisesti. ---

## Omasta pseudokoodista omaksi ohjelmaksi

Oppitunti 23 on rakentamispäivä. Mitään uutta ei tule.
Valitset yhden osan viikon 6 pseudokoodistasi (6-20 riviä). Käännät sen rivi riviltä taulukon
avulla. Suoritat sen. Tallennat tiedoston.
Ajattelu oli jo tehty viikolla 6. Tällä viikolla työ on enimmäkseen muodon vaihtamista.

### Tee näin: käännä ensin vain pieni toimiva osa. Laajenna vasta sen jälkeen. ---

## Käännöstaulukko

```javascript
Pseudokoodi | JavaScript | C#
-------------------------|-------------------------------------|---------------------------------------
WRITE "Hello" | console.log("Hello"); |
Console.WriteLine("Hello");
SET x TO 5 | let x = 5; | int x = 5;
IF x >= 18 THEN … | if (x >= 18) { … } | if (x >= 18) {
… }
REPEAT N TIMES | for (let i = 0; i < N; i++) { … } | for (int i = 0;
i < N; i++) { … }
WHILE test DO … | while (test) { … } | while (test) {
… }
```

### Vinkki: älä käännä ajatusta uudelleen alusta. Etsi vastaava muoto.

---

## Silmukka + if/else — salasanatarkistus (JS ja C# rinnakkain)

JavaScript

```javascript
let passwords = ["hi", "correcthorse", "12345678"];
for (let i = 0; i < 3; i++) {
if (passwords[i].length >= 8) {
console.log("tarpeeksi pitkä");
} else {
console.log("liian lyhyt");
}
}
```

C#

```csharp
string[] passwords = {"hi", "correcthorse", "12345678"};
for (int i = 0; i < 3; i++)
{
if (passwords[i].Length >= 8) Console.WriteLine("tarpeeksi pitkä");
else Console.WriteLine("liian lyhyt");
}
```

### Vinkki: rakenne (silmukka, ehto, haarautuminen) on sama. Vain pintasanat eroavat.

---

## Tallenna, suorita, katso tuloste

• JavaScript - selaimen DevTools-konsolissa:
• `Cmd + Opt + J` (Mac) tai `Ctrl + Shift + J` (Win/Linux)
• Liitä, paina Enter, lue tuloste.
• Tallenna koodi `.js`-tiedostona.
• C# - verkossa toimivassa .NET-ajoympäristössä:
• Avaa `dotnetfiddle.net`, valitse Console.
• Liitä `Main`-metodiin, paina Run.
• Tallenna koodi `.cs`-tiedostona.
• Ota kuvakaappaus ajosta.

### Tee näin: nimeä tiedosto niin, että tunnistat version, esimerkiksi `at3-v1.js`. ---

## Oikean virheilmoituksen lukeminen (JavaScript)

```
Uncaught ReferenceError: scre is not defined
at <anonymous>:3:15
```

Yleiskielellä: "En tiedä, mikä `scre` on."
Syy: ylempänä määrittelit `score`, mutta myöhemmin kirjoitit `scre` (o puuttuu).
Korjaus: etsi `scre`, kirjoita puuttuva `o` ja suorita uudelleen.

### Vinkki: virheilmoituksen rivinumero on ensimmäinen paikka, josta kannattaa katsoa. ---

## Oikean virheilmoituksen lukeminen (C#)

```
error CS0103: The name 'scre' does not exist in the current context
```

Sama bugi, sama korjaus. C# ei suostu kääntymään ennen kuin korjaat kirjoitusasun.
Toinen yleinen C#-virhe: `error CS1002: ; expected`
Yleiskielellä: puolipiste puuttuu.

### Vinkki: C# on tarkka puolipisteistä. Jos näet CS1002, katso rivin loppua. ---

## Yksi pieni korjaus, yksi uusi ajo

• Tätä "debuggaus" tarkoittaa tällä kurssilla.
• Ei debugger-työkalua.
• Ei pysäytä-ohjelma-rivi-kerrallaan -työkalua.
• Ei testauskehystä.
• Lue viesti → etsi rivi → muuta yksi pieni asia → suorita uudelleen.
• Teet tämän vähintään kerran AT3:ssa.

### Ajattele näin: hyvä korjaus on pieni ja testattava. ---

## Kahden minuutin esityksesi

Neljä kohtaa, noin 30 sekuntia kukin:
1. Mitä ohjelma tekee (yleiskielellä).
2. Miten se tekee sen (muuttujat, `if/else`, silmukka).
3. Mikä meni pieleen (yksi bugi nimeltä).
4. Miten korjasit sen (se yksi rivi, jota muutit).
Ajoita puhelimella. Kaksi minuuttia on lyhyt - tähtää mieluummin alle kuin yli.

### Vinkki: harjoittele kerran ääneen ennen esitystä. ---

## Pakollinen vähimmäistaso vs. syventäminen

• Pakollinen vähimmäistaso - jokainen opiskelija lähtee viikolta 8 mukanaan:
• pieni ohjelma, joka on käännetty omasta viikon 6 pseudokoodista
• kaksi ajoa, kaksi tulostetta, yksi löydetty ja korjattu bugi
• kahden minuutin suullinen esitys luokassa
• Syventäminen (valinnainen):
• yhdistä silmukka ja `if/else`
• vertaa ohjelmaasi luokkakaverin toisella kielellä tehtyyn versioon
• lisää syöte komennolla `prompt()` tai `Console.ReadLine()`

### Vinkki: vähimmäistaso riittää hyväksyttyyn. Syventävät kohdat ovat sinulle, jos haluat enemmän.

---

## Tämän viikon tehtävät (katso oman kielesi tehtävätiedosto)

• Tehtävä 8.1 *(PAKOLLINEN)* - AT3-ohje: käännä viikon 6 pseudokoodisi
(`student-tasks-js.md` tai `student-tasks-csharp.md`).
• Tehtävä 8.2 *(PAKOLLINEN)* - silmukkalämmittely: laske 1-5.
• Tehtävä 8.3 *(SYVENTÄVÄ)* - silmukka + if/else-salasanatarkistus.
• Tehtävä 8.4 *(SYVENTÄVÄ)* - lue oikea virheilmoitus ja korjaa se.
• Tehtävä 8.5 *(SYVENTÄVÄ)* - vertaile luokkakaverin kanssa, joka käyttää toista kieltä.

### Tee näin: kirjaa jokaisesta ajosta, mikä oli syöte ja mikä oli tuloste. ---

## Miten AT3 arvioidaan

• Hyväksytty / täydennettävä neljän tarkistuksen perusteella:
• Ohjelma toimii tai yritys on dokumentoitu virheilmoituksen kanssa.
• Osaat nimetä yleiskielellä, mitä ohjelma tekee.
• Yksi bugi-korjaus-pari on dokumentoitu reflektiossa.
• Kahden minuutin esitys pidettiin oppitunnilla 24.
• Ei numeroarvosanaa. Ei muuta rubriikkia kuin tämä tarkistuslista.

### Vinkki: jos jokin kohta puuttuu, tiedät täsmälleen, mitä täydentää. ---

## Silmukka sulkeutuu - viikko 1 vielä kerran

Kurssi alkoi yhdellä kysymyksellä:
> Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?
Olet vastannut siihen. Et teoriassa - vaan toimiva ohjelma kädessäsi.
Ohjelmointi ei ole enää mystistä.

### Ajattele näin: tästä alkaa varsinainen harjoittelu, ei loppu. ---

## Kiitos, ja mitä seuraavaksi?

Tämä oli ohjelmallinen ajattelu - perusta sen ohjelmoinnin alla, jota teet lopuissa opinnoissasi.
Säilytä AT3-lähdetiedostosi. Lue se uudelleen kuuden kuukauden päästä. Se näyttää pieneltä.
Se on tarkoituskin - sinä kirjoitit sen.
Tervetuloa keskeisen kysymyksen toiselle puolelle.
