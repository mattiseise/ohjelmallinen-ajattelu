# Oppitunti 21 — Ehdot koodissa: if, else ja vertailut

(kaksi kieltä rinnakkain)

### Pseudokoodin IF/ELSE oikeaksi koodiksi

Palauta mieleen tuttu pseudokoodi viikon 6 ikärajatarkistuksesta:

```pseudocode
READ age
IF age >= 18 THEN
WRITE "You may enter."
ELSE
WRITE "Sorry, you are not old enough."
ENDIF
```

Tämä on pseudokoodin muoto. Kumpikin kieli kirjoittaa sen hieman eri tavalla, mutta rakenne
— testi, then-lohko, else-lohko — on sama.
JavaScript

```javascript
let age = 16;
if (age >= 18) {
console.log("You may enter.");
} else {
console.log("Sorry, you are not old enough.");
}
```

C

```csharp
int age = 16;
if (age >= 18)
{
Console.WriteLine("You may enter.");
}
else
{
Console.WriteLine("Sorry, you are not old enough.");
}
```

Koodit ovat lähes identtisiä. Molemmat käyttävät sanaa , molemmat kirjoittavat testin `if`
sulkuihin , molemmat käyttävät aaltosulkeita haarojen ympärillä ja molemmissa on

```
( ... ) { ... }
```

sana . Pintatasolla erot ovat käytännössä vain tulostuskomento ja C#:n tyyppisana . `else int`
C#:ssa aaltosulkujen kirjoittaminen omille riveilleen on tavallinen tyyli, JavaScriptissä ne
kirjoitetaan usein samalle riville -sanan kanssa. Tämä on tyyliä, ei ajattelun ero. `if`

### Vertailuoperaattorit

-sulkeiden sisällä kirjoitat vertailun. Vertailu on pieni lauseke, joka on joko tosi tai epätosi — `if`
sama kyllä/ei-testi, jonka kirjoitit viikoilla 5 ja 6, nyt vain symboleina.
Hyvä uutinen: operaattorit ovat käytännössä samat JavaScriptissä ja C#:ssa.
Operaattori Merkitys Esimerkki
yhtä suuri kuin

```
== age == 18
```

eri suuri kuin

```
!= age != 18
```

Operaattori Merkitys Esimerkki
suurempi kuin

```
> age > 18
```

suurempi tai yhtä suuri

```
>= age >= 18
```

kuin
pienempi kuin

```
< age < 18
```

pienempi tai yhtä suuri

```
<= age <= 18
```

kuin
Pieni lisähuomio JavaScriptistä: siinä on myös (kolme yhtäsuuruusmerkkiä), jota `===`
kutsutaan tiukaksi yhtäsuuruudeksi. Tällä viikolla sekä että käyvät käytännössä `== ===`
samoihin esimerkkeihin. Valitse jompikumpi ja jatka.
Vertailun voi tallentaa myös muuttujaan. Vertailun arvo on tällöin boolean eli tai . `true false`
JavaScript

```javascript
let age = 16;
let isAdult = age >= 18;
console.log(isAdult);
```

C

```csharp
int age = 16;
bool isAdult = age >= 18;
Console.WriteLine(isAdult);
```

C# nimeää tyypin ( ); JavaScript päättelee sen itse. Ajatus on taas sama. `bool`

### Koko ikärajatarkistusohjelma

Yhdistetään oppituntien 20 ja 21 asiat yhdeksi pieneksi ohjelmaksi. Määrittelemme iän,
teemme vertailun, haarautamme sen perusteella ja tulostamme toisen kahdesta viestistä. Tämä
on ohjelma, jonka kannattaa säästää muistiinpanoihin, koska AT3 käyttää samaa rakennetta.
JavaScript

```javascript
let age = 16;
if (age >= 18) {
console.log("You may enter.");
console.log("Welcome!");
} else {
let yearsToGo = 18 - age;
console.log("Sorry, you are not old enough.");
console.log("Come back in " + yearsToGo + " years.");
}
```

C

```csharp
int age = 16;
if (age >= 18)
{
Console.WriteLine("You may enter.");
Console.WriteLine("Welcome!");
}
else
{
int yearsToGo = 18 - age;
Console.WriteLine("Sorry, you are not old enough.");
Console.WriteLine("Come back in " + yearsToGo + " years.");
}
```

Rivi riviltä ohjelmat vastaavat toisiaan. Erot ovat samat kuin aiemminkin: vs. , `let int`
vs. , aaltosulkujen tyyli. Muuten rakenne on yhteinen. `console.log Console.WriteLine`

### Ennusta ennen ajoa

Tämä on sama liike kuin viikolla 6. Ennen kuin painat Run, lue koodi rivi riviltä, ennusta
tuloste ja kirjoita ennuste ylös. Vasta sitten aja ohjelma ja vertaa todellista tulostetta
ennusteeseesi.
Yllä olevassa ohjelmassa, kun , ennusteen pitäisi olla:

```
age = 16
Sorry, you are not old enough.
Come back in 2 years.
```

Aja ohjelma. Saatko täsmälleen tämän? Jos kyllä, viikolla 6 harjoiteltu jäljitystapa on siirtynyt
oikeaan koodiin — ja se on viikon arvokkain siirto. Jos et, ensimmäinen kohta, jossa ennuste ja
todellisuus eroavat, on oikea paikka aloittaa tutkiminen.
Vaihda sitten arvoksi , ennusta uudestaan ja aja uudestaan. Ohjelman pitäisi

```
age = 16 age = 19
```

mennä toiseen haaraan. Jos molemmat ajot vastaavat ennustetta, ohjelma tekee sen, mitä
kirjoitit.
Pysähdy hetkeksi: Ota kynä ja ympyröi pseudokoodista ja valitsemastasi oikeasta
kielestä ne osat, jotka ovat aivan kirjaimellisesti samoja ajatuksia. Yllättävän moni
asia pysyy samana. Erot ovat syntaksia. Ympyröidyt kohdat ovat ajattelua.

### AT3-kielen valitseminen

AT3 tulee viikon 8 lopussa. Siinä otat yhden oman viikon 6 pseudokoodinpätkäsi, jossa on
, ja muutat sen pieneksi ohjelmaksi, joka oikeasti toimii — valitsemallasi kielellä. `IF/ELSE`
Palautat alkuperäisen pseudokoodin, ohjelman, lyhyen perustelun siitä, minkä pseudokoodin
valitsit ja miksi, sekä kuvakaappauksen kahdesta eri syötteestä (yksi tavallinen, yksi hankala).
Valitse kielesi tällä viikolla. Hyvä ohje on: valitse se, joka näyttää tämän
itseopiskelumateriaalin perusteella vähemmän pelottavalta. Jos näyttää

```javascript
console.log("...")
```

sinusta luontevammalta, valitse JavaScript. Jos taas sekä nimetyt

```csharp
Console.WriteLine("...")
```

tyypit ja tuntuvat lähempänä viikon 6 huolellista pseudokoodia, valitse C#. `string int`
Voit vaihtaa kieltä myöhemmin, mutta aikainen vaihto on aina helpompi kuin myöhäinen.
Arvosana ei riipu siitä, kumman kielen valitset. Se riippuu ajattelusta — tekeekö
ohjelmasi saman työn kuin pseudokoodisi ja osaatko puhua siitä rivi riviltä.
Muistutus vielä kerran: kumpaankaan kieleen ei tarvita asennuksia. JavaScript toimii
selaimen DevTools-konsolissa ( / ). C# toimii .NET Fiddlessä `Ctrl+Shift+J Cmd+Opt+J`
osoitteessa ilman käyttäjätunnusta. `dotnetfiddle.net`
