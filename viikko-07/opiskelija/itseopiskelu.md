# Itseopiskelu

Palauta mieleen viime viikko. Kirjoitit pseudokoodin pienelle tehtävälle — ehkä teen
tekemiselle, ikärajan tarkistukselle tai salasanan pituuden arvioinnille. Kirjoitit 10–15 riviä,
joissa oli , ja . Piirsit seurantataulukon ja teit kuivaharjoittelun yhdellä `SET IF WHILE`
tavallisella ja yhdellä hankalalla syötteellä. Oppitunnin 18 lopussa teksti teki sen, mitä odotit.
Ystävä olisi voinut lukea sen. Opettaja olisi voinut arvioida sen. AT2 olisi voinut käyttää sitä.
Anna nyt sama paperi tietokoneelle. Se ei tee mitään.
Tietokone ei osaa lukea englanninkielisin avainsanoin kirjoitettua pseudokoodia sen enempää
kuin ostoslistaasi. Se tulkitsee kirjaimellisesti vain tietyn, tarkasti määritellyn sanajoukon,
eikä pseudokoodi kuulu siihen sanajoukkoon. Tämä on se väli, jonka viikko 7 sulkee.
Kurssin keskeinen kysymys on sama kuin viikolla 1:

### Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tämän viikon vastaus on: ohjelmointikielen avulla. Ohjelmointikieli on tiukempi versio siitä
pseudokoodista, jota jo kirjoitit — niin tiukka, että oikea tietokone pystyy ajamaan sen ilman
arvailua. Se ajattelu, jota olet rakentanut kuuden viikon ajan, on jo olemassa. Kieli on vain se
syntaktinen pinta, jolle ajattelu kirjoitetaan.
Tällä viikolla tehdään yksi tärkeä lisäliike: kurssilla esitellään kaksi ohjelmointikieltä, ei vain
yhtä — JavaScript ja C# — rinnakkain. Oppitunti 19 puhuu ohjelmointikielistä ja syntaksista
yleiskielellä ilman toimivaa koodia. Oppitunnit 20 ja 21 näyttävät konkreettisen syntaksin
molemmilla kielillä samaan aikaan. JavaScript toimii selaimesi DevTools-konsolissa. C# toimii
.NET Fiddlessä. Kumpaankaan ei tarvita asennuksia. Ei kehitysympäristöä, ei Node.js:ää,
ei .NET SDK:ta, ei debuggereita eikä testikirjastoja.
Viikon lopussa valitset yhden kielistä, ajat ensimmäisen ohjelmasi, luot muuttujan ja kirjoitat
ensimmäisen -rakenteen. Tällä on merkitystä, koska AT3 tulee ensi viikolla ja pyytää `if/else`
sinua kääntämään yhden oman viikon 6 pseudokoodinpätkäsi pieneksi toimivaksi ohjelmaksi
siinä kielessä, jonka valitset tällä viikolla.
Ajattele näin: pseudokoodi kertoo mitä haluat tapahtuvan. Ohjelmointikieli kertoo sen
samalla tavalla mutta muodossa, jonka oikea tietokone hyväksyy.

## Oppituntikohtainen lukemisto

## Oppitunti 19 - Miksi ohjelmointikieliä on olemassa

### Pseudokoodista ohjelmakoodiin

Viime viikon pseudokoodi oli jo huolellista. Käytit pientä avainsanajoukkoa, sisensit lohkot ja
suljit jokaisen -rakenteen -rivillä. Miksi tämä ei silti vielä riitä? Siksi, että `IF ENDIF`
pseudokoodin lukija ja ohjelmakoodin lukija ovat eri asioita. Pseudokoodi on ihmislukijalle,
ohjelmakoodi oikealle tietokoneelle. Tietokone tunnistaa vain tarkasti määritellyn joukon
sanoja ja merkkejä. Jos sanat eivät kuulu siihen joukkoon, se pysähtyy.
Syntaksi on sopimus siitä, miten nämä sanat ja merkit pitää järjestää. JavaScript ja C# tekevät
saman työn eri sanoin, mutta sama ajattelu siirtyy kielestä toiseen.

### Tulkki ja kääntäjä

Tulkki lukee ja suorittaa koodia rivi kerrallaan. Kääntäjä lukee koko ohjelman, muuntaa sen
toiseen muotoon ja suorittaa vasta sitten. JavaScript näyttää tällä viikolla enemmän tulkin
kieleltä, C# enemmän käännettävältä kieleltä. Opiskelijan arjessa tämä näkyy lähinnä siinä,
miten virheilmoitukset tulevat vastaan.

### Kaksi kieltä, yksi ajattelutapa

JavaScript elää selaimessa. C# elää .NET-maailmassa. Molempien alla kulkee kuitenkin sama
ajattelu: järjestys, ehto, toisto, muuttujat, syöte, käsittely ja tuotos.

## Oppitunti 20 - Ensimmäiset komennot: tuloste, arvot ja muuttujat

### Tulostaminen konsoliin

JavaScript

```javascript
console.log("Hello, console");
```

C

```csharp
Console.WriteLine("Hello, console");
```

Molemmat tulostavat tekstin konsoliin.

### Muuttujat

JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(name);
console.log(age);
```

C

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(name);
Console.WriteLine(age);
```

Ajatus on molemmissa sama: tee nimetty säiliö, laita siihen arvo ja tulosta arvo.

### Ensimmäinen lasku

JavaScript

```javascript
let age = 16;
let yearsToAdulthood = 18 - age;
console.log("Years until you turn 18:");
console.log(yearsToAdulthood);
```

C

```csharp
int age = 16;
int yearsToAdulthood = 18 - age;
Console.WriteLine("Years until you turn 18:");
Console.WriteLine(yearsToAdulthood);
```

Ajattelu on sama. Vain pinta vaihtuu. `if/else`

## Oppitunti 21 - Ehdot koodissa: if, else ja vertailut

### Pseudokoodista -rakenteeksi

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

### Vertailut

Kummallakin kielellä käytät samoja perusvertailuja: , , , , , .

```
== != > >= < <=
```

### Koko ohjelma

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

Ennusta aina ennen ajoa, mitä ohjelma tulostaa. Tämä on viikon 6 jäljitystavan suora jatko.

---

## AT3-kielen valitseminen

AT3 osuu **viikon 8 loppuun**. Se pyytää sinua ottamaan yhden palan omaa viikon 6 pseudokoodiasi, jossa on `IF/ELSE`, ja kääntämään sen pieneksi ohjelmaksi, joka oikeasti toimii — valitsemallasi kielellä. Palautat alkuperäisen pseudokoodin, ohjelman, yhden virkkeen siitä, minkä viikon 6 palan valitsit ja miksi, sekä kuvakaappauksen tulosteesta kahdella eri syötteellä (yksi normaali, yksi reuna-arvo).

**Valitse kielesi tällä viikolla.** Suositus on: valitse se, joka näyttää vähemmän pelottavalta tätä itseopiskelumateriaalia lukiessasi. Jos `console.log("...")` näyttää sinusta luettavammalta, valitse JavaScript. Jos `Console.WriteLine("...")` ja nimetyt tyypit `string` / `int` tuntuvat enemmän siltä huolelliselta pseudokoodilta, johon totuit viikolla 6, valitse C#. Voit vaihtaa milloin tahansa ennen AT3:n eräpäivää, mutta vaihtaminen aikaisessa vaiheessa on huomattavasti helpompaa kuin myöhässä.

**Arvosana ei riipu siitä, minkä kielen valitset.** Se riippuu ajattelusta — siitä, tekeekö ohjelmasi saman työn kuin pseudokoodisi, ja siitä, pystytkö puhumaan siitä rivi riviltä.

Lyhyt muistutus, jos unohdat: **kumpaakaan kieltä varten ei tarvita asennusta**. JavaScript pyörii selaimen DevTools-konsolissa (`Ctrl+Shift+J` / `Cmd+Opt+J`). C# pyörii **.NET Fiddlessä** osoitteessa `dotnetfiddle.net`, ilman käyttäjätiliä.

---

## Yhteenveto ja mitä seuraavaksi

**Viikon keskeinen viesti:** *Ohjelmointikieli on tapa tehdä ohjeista riittävän täsmällisiä, jotta tietokone voi seurata niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain syntaksi, johon se kirjoitetaan.*

Tällä viikolla ylitit sillan. Tapasit kaksi oikeaa ohjelmointikieltä — JavaScriptin ja C#:n — ja näit ne vierekkäin jokaisen käsitteen kohdalla: tuloste, muuttujat, laskenta, vertailu, `if/else`. Kirjoitit ensimmäisen ohjelman valitsemallasi kielellä. Ajoit sen, ennustit ennen ajamista ja luit tulosteen samalla tavalla kuin viikko 6 opetti sinua lukemaan trace-taulukkoa.

**Viikko 8** päättää kurssin. Se tuo mukaan **silmukat** koodissa — `WHILE` ja `FOR`, jotka tunnet jo viikon 6 pseudokoodista, nyt JavaScriptinä ja C#:na. Se esittelee oikeat **virheilmoitukset** oppimisvälineenä (rikoit ohjelman; mitä tietokone sanoi?). Ja se laskeutuu **AT3**:een — sinun käännöksesi yhdestä viikon 6 pseudokoodin pätkästä pieneksi toimivaksi ohjelmaksi. Kaikki tällä viikolla kirjoittamasi on perusta; säilytä koodisi tallennettuna.

Keskeinen kysymys vielä kerran — ja lue se ääneen, koska viikolla 8 saat lopultakin vastata siihen ohjelmalla, joka tekee täsmälleen sen, mitä sanoit:

> *Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?*
