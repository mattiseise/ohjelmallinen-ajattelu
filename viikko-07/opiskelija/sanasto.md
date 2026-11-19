# Viikko 7 — Pseudokoodista koodiin

## Viikon 7 sanasto

Alla olevat termit liittyvät oppitunteihin 19, 20 ja 21. Määritelmät ovat tarkoituksella lyhyitä —
katso esimerkit itseopiskelumateriaalista. Kaksi termiä ( ja ) `console.log Console.WriteLine`
ovat kielikohtaisia rinnakkaismerkintöjä. Lopun termi (silmukka) on ennakkokatsaus viikkoon
8.

### Ohjelmointikieli

Joukko sanoja ja sääntöjä, joita tietokone pystyy lukemaan ja suorittamaan. JavaScript ja C#
ovat tällaisia kieliä. Ohjelmointikieli eroaa pseudokoodista siinä, että tietokone itse pystyy
tulkitsemaan tai kääntämään sen, ei vain ihminen. Ajattelu — järjestys, ehto, toisto — on sama
kuin pseudokoodissa; kieli on vain se täsmällinen muoto, jonka ajattelu saa.

### Syntaksi

Sääntö siitä, miten sanat ja merkit pitää järjestää ohjelmointikielessä. Mitkä sanat ovat
olemassa, missä järjestyksessä ne voivat esiintyä, mitä välimerkkejä niiden ympärillä täytyy
olla ja mistä lause päättyy. Syntaksia noudattava koodi toimii. Syntaksin rikkova koodi
pysähtyy virheilmoitukseen. Syntaksi on se, mitä tietokone lukee; ajattelu on se, mitä sinä
kirjoitat.

### Komento

Yksi yksittäinen ohje, jonka tietokone pystyy suorittamaan. on komento:

```javascript
console.log("Hello")
```

tulosta teksti Hello konsoliin. on komento: tee muuttuja nimeltä , tyyppiä ,

```
int age = 16; age int
```

ja laita siihen arvo . Ohjelmat ovat komentojen jonoja yksi toisensa jälkeen. `16`

### Tulkki (epämuodollinen)

Ohjelma, joka lukee koodisi rivi kerrallaan ja suorittaa jokaisen rivin sitä mukaa kuin lukee
sitä. Selaimen JavaScript toimii näin: liitä rivi konsoliin, paina Enter, näe tulos. Erillistä
rakenna ensin, aja sitten -vaihetta ei ole.

### Kääntäjä (epämuodollinen)

Ohjelma, joka lukee koko koodin kerralla, muuntaa sen alemmalle tasolle ja suorittaa vasta
sitten muunnetun version. C# käännetään ennen suorittamista. Opiskelijan näkökulmasta
tärkein ero tällä viikolla on, että kääntäjä voi kieltäytyä käynnistymästä lainkaan, jos koodissa
on syntaksivirhe.

### Konsoli

Pieni tekstialue, johon ohjelma tulostaa tuotosta ja josta se joskus lukee syötettä. Selaimen
DevTools-konsoli on paikka, johon JavaScript tulostaa. .NET Fiddlen tulosruutu on paikka,
johon C# tulostaa. Konsoli on se paikka, johon viikon 6 pseudokoodin lopulta päätyy `WRITE`
oikeassa ohjelmassa.

### Tuotos

Se, mitä ohjelma lähettää nähtäväksi — tekstirivi konsoliin, luku tai kyllä/ei-arvo.
JavaScriptissä tuotosta kirjoitetaan komennolla . C#:ssa käytetään

```javascript
console.log(...)
```

. Tuotos on tapa, jolla ohjelma vastaa takaisin.

```csharp
Console.WriteLine(...)
```

### Muuttuja

Nimetty säiliö yhdelle arvolle, joka voi vaihtua ohjelman suorituksen aikana. (Sama ajatus kuin
viikolla 6, nyt oikeassa kielessä.) JavaScriptissä: . C#:ssa: . Nimi

```javascript
let age = 16; int age = 16; age
```

pysyy samana; sisältö voi vaihtua. Hyvä muuttujan nimi kertoo, mitä arvo tarkoittaa.

### Arvo

Se konkreettinen sisältö, joka muuttujassa on tietyllä hetkellä — tekstinpätkä ( ), `"Lyra"`
kokonaisluku ( ) tai kyllä/ei-arvo ( ). Muuttuja on nimetty laatikko; arvo on se, mitä `16 true`
laatikon sisällä juuri nyt on.

### Sijoitus

Toiminto, jossa arvo laitetaan muuttujaan. Sekä JavaScript että C# käyttävät tähän merkkiä . `=`
(JS) ja (C#) ovat sijoituksia. Pseudokoodin on sama

```javascript
let age = 16; int age = 16; SET age TO 16
```

ajatus eri pinnalla.

### Merkkijono

Tekstinpätkä, joka kirjoitetaan lainausmerkkien sisään. on merkkijono. Myös `"Hello, console"`
on merkkijono, vaikka se näyttää luvulta — lainausmerkit tekevät siitä tekstiä. Sekä `"16"`
JavaScript että C# käyttävät kaksoislainausmerkkejä. Sana string tarkoittaa kirjaimellisesti
merkkijonoa.

### Int / number

Kokonaisluku, jota käytetään ohjelmassa arvona ilman lainausmerkkejä. C# kutsuu tätä
tyyppiä nimellä (sanasta integer) ja pyytää sinua nimeämään tyypin, kun luot muuttujan: `int`
. JavaScript kutsuu sitä vain number-arvoksi ja päättelee tyypin arvosta:

```javascript
int age = 16; let age =
```

. on luku; on merkkijono. `16; 16 "16"`

### Ehto

Pieni lauseke, joka on joko tosi tai epätosi ja joka kirjoitetaan -rakenteen sulkeiden sisään. `if`
on ehto. Ehdon tarkoitus on antaa -rakenteelle peruste valita eri haara.

```
age >= 18 if/else
```

(Viikolta 6 tuttu ajatus, nyt oikeassa ohjelmakielessä.)

### If / else

Ohjausrakenne, joka suorittaa yhden koodilohkon, jos ehto on tosi, ja toisen lohkon, jos ehto on
epätosi. Molemmilla kielillä muoto on . -osa on valinnainen —

```
if (test) { ... } else { ... } else
```

pelkkä on myös sallittu. (Viikolta 6 tuttu ajatus, nyt koodina.) `if`

### Vertailuoperaattori

Symboli, joka vertaa kahta arvoa ja tuottaa tosi/epätosi-tuloksen. Tällä kurssilla käytetään
kuutta vertailuoperaattoria: (yhtä suuri), (eri suuri), (suurempi), (suurempi tai yhtä

```
== != > >=
```

suuri), (pienempi), (pienempi tai yhtä suuri). Nämä kuusi ovat käytännössä samat `< <=`
JavaScriptissä ja C#:ssa. (JavaScriptissä on lisäksi `===`, tiukempi yhtäsuuruus, mutta tällä viikolla kummallakin muodolla pärjää.)

### `console.log` *(JavaScript)*

JavaScriptin komento, joka tulostaa konsoliin. `console.log("Hello")` tulostaa `Hello` omalle rivilleen. Komennolle voi antaa merkkijonon, luvun, muuttujan tai useita pilkuilla erotettuja arvoja. Se on JavaScriptin tärkein tapa näyttää, mitä ohjelmassa tapahtuu.

### `Console.WriteLine` *(C#)*

C#:n komento, joka tulostaa konsoliin. `Console.WriteLine("Hello");` tulostaa `Hello` omalle rivilleen ja lisää rivinvaihdon. `WriteLine` on yksi sana, ja isot kirjaimet `W` ja `L` merkitsevät. Loppupuolen puolipiste on C#:ssa pakollinen.

### Silmukka (ennakkokatsaus — viikon 8 keskeinen aihe)

Ohjausrakenne, joka suorittaa koodilohkon useita kertoja lopetusehdon avulla. Törmäsit tähän
ajatukseen viikon 6 pseudokoodissa sanoina ja . Ensi viikolla sama ajatus saapuu `WHILE FOR`
JavaScriptiin ja C#:aan sanoina ja . Tällä viikolla sinun ei vielä tarvitse kirjoittaa `while for`
silmukoita oikeaan koodiin — termi on mukana siksi, ettei sana ole uusi viikolla 8.
