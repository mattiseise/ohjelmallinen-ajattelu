# Pseudokoodista koodiin — kaksi kieltä, yksi ajattelutapa

## Johdanto

Kuvittele viime viikko. Kirjoitit pseudokoodia jollekin pienelle tehtävälle — teereseptille, iän rajoitus -tarkistukselle, salasanan pituustestille. Kymmenen tai viisitoista riviä paperilla `SET`-, `IF`- ja `WHILE`-avainsanoilla. Piirsit jäljitystaulukon ja kävit sen käsiajona läpi yhdellä normaalilla ja yhdellä hankalalla syötteellä. Oppituntiin 18 mennessä se teki, mitä odotitkin. Ystävä osasi lukea sen. Opettaja osasi arvioida sen. AT2 vastaanotti sen.

Anna nyt sama paperi tietokoneelle.

Se ei tekisi mitään.

Tietokone ei osaa lukea englanninkielisin avainsanoin kirjoitettua pseudokoodia sen enempää kuin se osaa lukea ostoslistaasi. Se on *tietyn* sanajoukon sananmukainen tulkitsija, eikä pseudokoodi kuulu tuohon joukkoon. Tämä on se kuilu, jonka viikko 7 sulkee. Kurssin keskeinen kysymys on sama, johon olet vastannut viikolta 1 lähtien:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

Vastaus tällä viikolla on **ohjelmointikieli**. Ohjelmointikieli on tiukempi versio siitä pseudokoodista, jonka olet jo kirjoittanut — niin tiukka, että oikea tietokone osaa ajaa sen arvailematta. *Ajattelu*, jonka olet rakentanut kuuden viikon aikana, on jo paikallaan. *Kieli* on vain se syntaksi, jolla se kirjoitetaan.

Yksi siirto vielä tällä viikolla: esittelemme **kaksi** kieltä, emme yhtä — JavaScriptin ja C#:n — rinta rinnan. Oppitunti 19 puhuu ohjelmointikielistä ja syntaksista selkokielisesti ilman toimivaa koodia. Oppitunnit 20 ja 21 näyttävät konkreettisen syntaksin molemmilla kielillä yhtaikaa. JavaScript ajetaan selaimesi DevTools-konsolissa. C# ajetaan **.NET Fiddlessä**. **Kummallekaan ei tarvita asennusta.** Ei IDE:tä, ei Node.js:ää, ei .NET SDK:ta, ei debuggeria, ei testiframeworkkia.

Viikon loppuun mennessä valitset toisen näistä kahdesta kielestä, ajat ensimmäisen ohjelman, esittelet muuttujan ja kirjoitat ensimmäisen `if/else`-rakenteen. Valinnalla on merkitystä: AT3 saapuu ensi viikolla, ja se pyytää kääntämään palan omaa viikon 6 pseudokoodiasi pieneksi ohjelmaksi sillä kielellä, jonka valitset tällä viikolla.

---

## Oppitunti 19 — Miksi ohjelmointikieliä on olemassa *(kieliriippumaton — ei toimivaa koodia tällä oppitunnilla)*

### Pseudokoodista koodiin

Viime viikon pseudokoodi oli jo huolellista. Käytit pientä avainsanajoukkoa, sisennettyjä lohkoja, suljit jokaisen `IF`:n `ENDIF`:llä. Miksi se ei riitä?

Se ei riitä, koska *kenelle* pseudokoodi on tarkoitettu ja *kenelle* koodi on tarkoitettu, ovat eri asioita. Pseudokoodi on tarkoitettu **ihmisseuraajalle**, joka osaa englantia. Tiukimmillaankin pseudokoodi nojaa siihen, että lukija on henkilö — henkilö, joka tietää, mitä "odota" tarkoittaa ja mikä lasketaan "numeroksi". Tietokone ei tuo mitään näistä mukanaan. Se tuntee ne sanat, jotka se on rakennettu tuntemaan, eikä mitään muuta. Jos sivulla olevat sanat eivät kuulu sen pieneen listaan, se pysähtyy.

Siirto pseudokoodista koodiin ei ole valtava älyllinen harppaus. Se on kiristys. Vaihdamme englanninkieliset avainsanasi täsmälleen niihin sanoihin, jotka *yksi tietty tietokonejärjestelmä* tunnistaa. Ajattelu — sekvenssi, ehto, toisto, muuttujat, syöte, käsittely, tuloste — ei muutu lainkaan.

> **Pysähdy hetkeksi:** Ota yksi pala viikon 6 pseudokoodia, jonka kirjoitit. Lue se ääneen. Huomaa, mitä rivejä tuntematon voi noudattaa vain siksi, että hän on ihminen — esimerkiksi `wait`, `the user enters their age`, `display a friendly message`. Juuri nämä rivit tarvitsevat täsmällisen, tietokoneen hyväksymän sanan oikeassa koodissa.

### Mitä syntaksi on?

**Syntaksi** on sääntö siitä, *miten sanat täytyy järjestää*, jotta lukija osaa jäsentää ne. Jokaisella kielellä on syntaksi, ei vain ohjelmointikielillä.

**Esimerkki — englannin vs. suomen sanajärjestys.** Englanniksi sanot "the red car." Suomeksi sanot "punainen auto." Syntaksi — adjektiivin ja substantiivin järjestys — on vain erilainen sopimus. Jos kirjoitat "car red" englanniksi, lukija silti arvaa, mitä tarkoitit, koska ihmiset ovat anteliaita. Tietokone ei ole.

**Esimerkki — automaatti.** Automaatti hyväksyy tietyn muotoisia kolikoita ja hylkää muut. Jos painat nappia ennen kolikon syöttämistä, mitään ei tapahdu. Koneen *syntaksi* on "kolikko ensin, sitten nappi". Kokeile toisessa järjestyksessä, etkä saa juomaa; saat kolikkosi takaisin.

**Esimerkki — tiedostopolku.** `Users/maria/documents/report.txt` on kelvollinen polku. `Users/maria/documents report.txt` (välilyönnillä ja ilman kauttaviivaa) ei ole — eikä tietokone sano "luulen, että tarkoitit documents-kansion tiedostoa." Se sanoo "ei tällaista tiedostoa." Kauttaviiva on osa syntaksia.

Ohjelmointikielen syntaksi on tasan tällainen sääntö, vain enemmän sitä: mitkä sanat ovat olemassa, missä järjestyksessä ne saavat esiintyä, mitkä välimerkit niiden ympärillä on oltava, mikä lasketaan lauseen lopuksi. Jos koodisi noudattaa sääntöjä, tietokone osaa ajaa sen. Jos yksi pilkku tai lainausmerkki on väärässä paikassa, tietokone pysähtyy ja tulostaa **virheilmoituksen**, joka näyttää, mihin se jäi jumiin.

Tämä ei ole ansa. Tämä on sopimus. Korjaa se yksi kohta, johon virheilmoitus osoittaa, ja se ajaa.

### Tulkki ja kääntäjä — yksi kappale kumpaisesta, epämuodollinen

Kohtaat tällä viikolla kaksi sanaa "sille jutulle, joka lukee koodin ja saa sen ajamaan": *tulkki* ja *kääntäjä*. Ero ei ole nyt tärkeä; nimet ovat.

**Tulkki** lukee koodisi rivi kerrallaan ja ajaa kunkin rivin sitä mukaa. JavaScript selaimessa tulkataan tällä tavalla: selain lukee `console.log("Hello")`:n, ajaa sen, näkee seuraavan rivin, ajaa senkin. Ei ole erillistä "tee ensin ohjelma, sitten aja se" -vaihetta. Kirjoitat rivin, painat Enter ja näet tuloksen.

**Kääntäjä** lukee koko ohjelmasi kerralla, kääntää sen matalamman tason muotoon, jonka tietokone osaa ajaa nopeammin, ja ajaa sitten tämän käännetyn version. C# toimii näin: online-ympäristö (tai oikea .NET-työkalu) kääntää C#-koodisi ensin joksikin muuksi ja ajaa sen sitten. Sinun näkökulmastasi opiskelijana tällä viikolla ero on enimmäkseen näkymätön — painat Run-nappia, ja hetken kuluttua näet tulosteen. Pääpaikka, jossa *huomaat* eron, on virheilmoituksissa: C#-virhe osoittaa usein "tämä ei käänny" ennen kuin se edes yrittää ajaa, kun taas JS-virhe ilmestyy usein, kun koodi on jo ajossa.

Sinun ei tarvitse muistaa tätä eroa. Tiedä vain ne kaksi sanaa; näet molemmat.

### Kaksi kieltä, yksi ajattelutapa

Tällä kurssilla tutustutaan kahteen oikeaan ohjelmointikieleen rinta rinnan, alkaen tältä viikolta.

**JavaScript** (usein lyhennettynä **JS**) on selaimen kieli. Jokaisessa selaimessa, jota olet koskaan käyttänyt — Chrome, Firefox, Edge, Safari — on JavaScript-tulkki sisäänrakennettuna. Tuo tulkki on yhden näppäimistöoikotien päässä juuri nyt, **DevTools-konsolissa**. JavaScriptiä käytetään tekemään verkkosivuista vuorovaikutteisia (nappulat, valikot, live-päivitykset) ja se ajetaan myös palvelimilla (työkalulla nimeltä Node.js, jota emme käytä tällä viikolla).

**C#** (lausutaan "C sharp") on yksi Microsoftin rakentaman **.NET**-alustan pääkielistä. C#:lla rakennetaan työpöytäsovelluksia, web-palvelimia, mobiilisovelluksia ja — työkalun **Unity** kautta — hyvin suurta osaa maailman videopeleistä. .NET:iä ei tarvitse asentaa tällä viikolla; online-ympäristö **.NET Fiddle** (osoitteessa `dotnetfiddle.net`) ajaa C#-koodia selaimessasi ilman tiliä.

Kaksi kieltä, kaksi kotia, yksi ajattelutapa. Ajattelu — *sekvenssi, ehto, toisto, muuttujat, syöte, käsittely, tuloste* — on se, mikä matkustaa. Syntaksi on se, mitä kukin kieli päätti tehdä pinnalla.

### Miksi tämä on tärkeää IT-ammattilaiselle

Tulet lukemaan enemmän koodia kuin kirjoitat. Urasi aikana kosket todennäköisesti kolmea, neljää, viittä eri ohjelmointikieltä — koska työ vaihtuu, tiimi vaihtuu, projekti vaihtuu. IT-ihmiset, jotka jäävät jumiin, ajattelevat itsestään "JavaScript-ihmisinä" tai "C#-ihmisinä". IT-ihmiset, jotka pärjäävät hyvin, käsittelevät jokaista uutta kieltä uutena pintana tutun pohjan päällä.

Ensimmäisen ohjelmointikokemuksesi ankkurointi **kahteen** kieleen tarkoituksella tekee tuon siirron ilmiselväksi ensimmäisestä päivästä lähtien. Kun näet `console.log("Hello")`:n vieressä `Console.WriteLine("Hello")`:n, kaksi asiaa tulee väistämättömäksi: kyllä, sanat eroavat; ei, tietokoneen tekemä työ ei ole erilainen. Tuo oivallus on arvokkain asia, jonka viikko 7 antaa sinulle.

> **Pysähdy hetkeksi:** Ilman, että vielä kirjoitat koodia, kirjoita yksi lause muistiinpanoihisi, joka päättää tämän ajatuksen: *"Ohjelmointikieltä tarvitaan, ei pelkkää pseudokoodia, koska…"* — vastaa omin sanoin. Sitten lue vastaus takaisin. Jos siinä mainitaan sana *tietokone* jossain, olet luultavasti ymmärtänyt.

---

## Oppitunti 20 — Ensimmäiset käskyt: tuloste, arvot, muuttujat *(kaksikielinen; kaikki rinta rinnan)*

Tämä on oppitunti, jolla kirjoitat ensimmäisen oikean koodisi. Kaikki alla esiintyy kahdesti — kerran JavaScriptissä, kerran C#:ssa. Valitse yksi kieli oikeasti ajamiseen, mutta lue molemmat — side-by-side on oppitunti.

### Tuloste: konsolille puhuminen

Pienin mahdollinen ohjelma on sellainen, joka tulostaa tekstiä. Pseudokoodissa kirjoitit viime viikolla `WRITE "Hello"`. Tässä sama rivi kummallakin kielellä.

#### JavaScript

```javascript
console.log("Hei, konsoli");
```

#### C#

```csharp
Console.WriteLine("Hei, konsoli");
```

Lue kaksi riviä rinnakkain. JavaScriptissä tulostusfunktiota kutsutaan nimellä `console.log`. C#:ssa sitä kutsutaan nimellä `Console.WriteLine`. Molemmat ottavat yhden palan tekstiä lainausmerkeissä ja tulostavat sen konsoliin. Molemmat päättyvät puolipisteeseen `;`. (JavaScript ei tiukasti *vaadi* puolipistettä — se on lempeä — mutta pidämme sen jokaisessa esimerkissä rinnakkaisuuden vuoksi C#:n kanssa. C# vaatii sen; yhden unohtaminen on käännösvirhe.)

JavaScript-version ajaminen: avaa selain, paina `Cmd+Opt+J` Macillä tai `Ctrl+Shift+J` Windowsilla / Linuxilla (tai napsauta hiiren oikealla missä tahansa sivulla, valitse **Tarkasta**, klikkaa sitten **Konsoli**-välilehteä). Liimaa rivi sisään, paina Enter, lue tuloste.

C#-version ajaminen: avaa `dotnetfiddle.net` selaimessasi. Valitse "Console" yläosasta. Liimaa rivi editoriin `Main`-metodin sisään (template antaa sinulle sellaisen). Paina Run-nappia. Tuloste ilmestyy alempaan laatikkoon.

Kaksi eri ympäristöä, kaksi hieman erilaista sanaa, sama yksi työ: tulosta yksi rivi.

### Muuttujat: arvon nimeäminen

Viime viikolla kirjoitit `SET passwordLength TO 7`. Oikeassa kielessä vastine on **muuttujan esittely** ja arvon **sijoitus**.

#### JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(name);
console.log(age);
```

#### C#

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(name);
Console.WriteLine(age);
```

Sama idea kummallakin puolella: tee merkitty säilö, laita arvo sisään, sitten tulosta arvo. Erot ovat pinnassa.

JavaScriptissä kirjoitat `let` jokaisen uuden muuttujan eteen. **Et** kerro JavaScriptille, minkä tyyppinen arvo menee sisään — JavaScript päättelee sen itse arvosta (`"Lyra"` on tekstiä, `16` on numero).

C#:ssa kirjoitat arvon **tyypin** ensin: `string` tekstille, `int` kokonaisluvulle. C# haluaa sinun sitoutuvan etukäteen siihen, minkä tyyppistä asiaa muuttuja pitää sisällään. Tämä ei ole eri ajattelutapa — se on yksi ylimääräinen sana. Sana *tyyppi* tulee tärkeäksi myöhemmin opinnoissasi; tällä viikolla kirjoita vain `string`, kun arvo on tekstiä, ja `int`, kun se on kokonaisluku, ja se riittää.

Molemmat kielet käyttävät `=`-merkkiä sijoitukseen — sama symboli, jota pseudokoodi käytti muodossa `SET x TO 7` (vain kirjoitettuna eri tavalla). Ja molemmat kielet antavat sinun tulostaa muuttujan välittämällä sen nimen tulostusfunktiolle — ei lainausmerkkejä muuttujan nimen ympärillä, koska pyydät säilön *sisällä* olevaa arvoa, et sanaa "name".

> **Pysähdy hetkeksi:** Katso yllä olevia kahta katkelmaa. Mitkä rivimuodot pidät ensisilmäyksellä helpompina lukea — JavaScriptin `let name = "Lyra";` vai C#:n `string name = "Lyra";`? Oikeaa vastausta ei ole; kiinnitä huomiota rehelliseen reaktioosi, sillä se on vihje siitä, mikä kieli valita tämän viikon tehtäviin.

### Ensimmäinen laskutoimitus

Viime viikon pseudokoodi käytti sijoituksia kuten `SET total TO unitPrice * quantity`. Oikeat kielet tekevät saman; aritmeettiset operaattorit (`+`, `-`, `*`, `/`) ovat samat kummallakin puolella.

Punainen lanka loppuviikolle on: **kuinka monta vuotta sinulla on jäljellä, kunnes täytät 18?** Annetun iän perusteella laske `18 - age` ja tulosta tulos.

#### JavaScript

```javascript
let age = 16;
let yearsToAdulthood = 18 - age;
console.log("Vuosia 18-vuotiaaksi:");
console.log(yearsToAdulthood);
```

#### C#

```csharp
int age = 16;
int yearsToAdulthood = 18 - age;
Console.WriteLine("Vuosia 18-vuotiaaksi:");
Console.WriteLine(yearsToAdulthood);
```

Lue nämä yhdessä. Algoritmi on identtinen: *tee age, laske erotus, tulosta otsikko, tulosta tulos.* Sanat eroavat — `let` vs `int`, `console.log` vs `Console.WriteLine` — mutta vaiheet ovat rinnakkain yksi yhteen. Vaihda `age = 16` omaksi iäksesi, aja se, ja ohjelma kertoo, montako vuotta sinulla on jäljellä 18-vuotiaaksi.

Voit myös yhdistää otsikon ja numeron yhdelle riville liittämällä tekstiä ja numeroita `+`:lla. Molemmat kielet sallivat tämän:

#### JavaScript

```javascript
let age = 16;
console.log("Sinulla on " + (18 - age) + " vuotta jäljellä.");
```

#### C#

```csharp
int age = 16;
Console.WriteLine("Sinulla on " + (18 - age) + " vuotta jäljellä.");
```

Huomaa, että `+` tekstin ja numeron välissä on *sama operaattorisymboli* molemmilla kielillä — sen tehtävä on liimata palaset yhteen yhdeksi tekstipalaksi. Tämän asian sana on **yhdistäminen** (concatenation). C#:lla on myös siistimpi muoto nimeltä **string interpolation** (`$"Sinulla on {18 - age} vuotta jäljellä."`), ja JavaScriptillä on samanlainen muoto nimeltä **template literal**; molemmat ovat valinnaisia tällä viikolla ja on listattu sanastossa "eteenpäin katsovina".

### Tulosteen lukeminen

Tällä viikolla ainoa debugger-työkalusi on *tulosteen lukeminen*. Ei breakpointia, ei step-through-debuggeria, ei testiframeworkkia. Jos ohjelma tulostaa, mitä odotit, se toimi. Jos se tulostaa jotain muuta, ero odotetun ja todellisen välillä on bugi — ja se on bugi *sinun koodissasi*, juuri sillä tavalla, jolla viikko 6 opetti sinut katsomaan.

Jos mitään ei ilmesty, ohjelma ei päässyt tulostusriville. Ehkä se pysähtyi aiemmin virheilmoitukseen; ehkä ajoit väärän tiedoston; ehkä unohdit painaa Run. Lue virheilmoitus, jos sellainen on — tulkki tai kääntäjä yleensä osoittaa suoraan ongelmaan.

### Ajattelu on sama

Tässä side-by-side-yhteenveto. Molemmat ohjelmat tekevät tämän:

1. Tekevät muuttujan nimeltä `age` ja laittavat siihen numeron.
2. Tekevät muuttujan nimeltä `yearsToAdulthood` ja laittavat siihen arvon `18 - age`.
3. Tulostavat otsikon.
4. Tulostavat arvon.

Tämä on algoritmi. Se on identtinen JavaScriptissä ja identtinen C#:ssa. Erot (`let` vs `int`, `console.log` vs `Console.WriteLine`, puolipisteet pakollisia vs sopimuksesta) ovat **syntaksia**. Syntaksi on se sopimus, jonka teet yhden tietyn tietokoneen kanssa. Ajattelu on se asia.

> **Pysähdy hetkeksi:** Jos vaihtaisit kaksi katkelmaa keskenään — kirjoittaisit JavaScript-koodin .NET Fiddleen tai C#-koodin selainkonsoliin — mitä luulet, että tapahtuisi? Kokeile. Saamasi virhe on kielen tapa sanoa "tämä ei ole minun syntaksiani." Lue, mitä se sanoo.

---

## Oppitunti 21 — Ehdot koodissa: if, else, vertailut *(kaksikielinen; kaikki rinta rinnan)*

### Pseudokoodin IF/ELSE:stä koodin if/else:ksi

Tuo eteen pala pseudokoodia, jonka olet nähnyt nyt monta kertaa — iän rajoitus -tarkistus:

```text
READ age
IF age >= 18 THEN
  WRITE "Pääset sisään."
ELSE
  WRITE "Olen pahoillani, et ole tarpeeksi vanha."
ENDIF
```

Tuo on pseudokoodin muoto. Kumpikin kieli kirjoittaa sen hieman eri tavalla, mutta rakenne — *testi, then-lohko, else-lohko* — on täsmälleen sama.

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
} else {
  console.log("Olen pahoillani, et ole tarpeeksi vanha.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("Pääset sisään.");
}
else
{
    Console.WriteLine("Olen pahoillani, et ole tarpeeksi vanha.");
}
```

Kaksi katkelmaa ovat lähes identtiset. Molemmat käyttävät avainsanaa `if`, molemmat laittavat testin pyöreisiin sulkeisiin `( ... )`, molemmat ympäröivät kunkin haaran aaltosulkeilla `{ ... }`, molemmat käyttävät avainsanaa `else`. Ainoat pintaerot ovat tulostusfunktio ja tyyppisana `int`. Aaltosulkeiden muotoilu C#:ssa on tapana laittaa uudelle riville; JS:ssä se on tapana laittaa samalle riville `if`:n kanssa. Tämä on tyyliä, ei sääntöjä.

### Vertailuoperaattorit

Sulkeiden sisään `if`:n jälkeen kirjoitat **vertailun**. Vertailu on pieni lauseke, joka on joko *tosi* tai *epätosi* — sama kyllä/ei-testi, jonka kirjoitit viikoilla 5 ja 6, vain symboleina. Hyvä uutinen: operaattorit ovat olennaisesti samat JavaScriptissä ja C#:ssa.

| Operaattori | Merkitys                  | Esimerkki (JS tai C#) |
|-------------|---------------------------|-----------------------|
| `==`        | yhtä kuin                 | `age == 18`           |
| `!=`        | eri kuin                  | `age != 18`           |
| `>`         | suurempi kuin             | `age > 18`            |
| `>=`        | suurempi tai yhtä suuri   | `age >= 18`           |
| `<`         | pienempi kuin             | `age < 18`            |
| `<=`        | pienempi tai yhtä suuri   | `age <= 18`           |

Yksi pieni lisähuomio JavaScriptistä: siinä on myös `===` (kolme yhtäsuuruusmerkkiä), jota kutsutaan **tiukaksi yhtäsuuruudeksi**. Kaikkeen mitä teemme tällä viikolla, sekä `==` että `===` toimivat samalla tavalla; molemmat ovat hyvin. Käytä sitä, joka tuntuu luontevalta, ja jatka. (Kohtaat hienovaraisuuden myöhemmin opinnoissasi; se ei muuta mitään tällä viikolla.)

Vertailu sinänsä voidaan myös laittaa muuttujaan. Vertailun arvo on **boolean** — joko `true` tai `false`. Molemmat kielet käyttävät sanoja `true` ja `false` (pienillä kirjaimilla) tähän.

#### JavaScript

```javascript
let age = 16;
let isAdult = age >= 18;
console.log(isAdult);
```

#### C#

```csharp
int age = 16;
bool isAdult = age >= 18;
Console.WriteLine(isAdult);
```

C# nimeää tyypin (`bool`); JavaScript päättelee sen arvosta. Sama idea, yksi ylimääräinen sana C#:ssa.

### Yhteen koottuna — iän rajoitus -tarkistus

Yhdistä nyt kaikki oppitunneista 20 ja 21 yhdeksi pieneksi ohjelmaksi. Esittelemme iän, lasketaan vertailu, haarautetaan sen perusteella, ja tulostetaan toinen kahdesta viestistä. Tämä on ohjelma, jonka tallennat muistiinpanoihisi — AT3 käyttää sitä uudelleen.

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
  console.log("Tervetuloa!");
} else {
  let yearsToGo = 18 - age;
  console.log("Olen pahoillani, et ole tarpeeksi vanha.");
  console.log("Palaa " + yearsToGo + " vuoden kuluttua.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("Pääset sisään.");
    Console.WriteLine("Tervetuloa!");
}
else
{
    int yearsToGo = 18 - age;
    Console.WriteLine("Olen pahoillani, et ole tarpeeksi vanha.");
    Console.WriteLine("Palaa " + yearsToGo + " vuoden kuluttua.");
}
```

Rivi riviltä kaksi ohjelmaa ovat yhteneviä. Erot ovat täsmälleen ne erot, jotka olet jo nimennyt: `let` vs `int`, `console.log` vs `Console.WriteLine`, aaltosulkeiden sijoittelu. Kaikki muu — `if`, `>=`, `else`, aaltosulkeet, sijoitus — on samaa.

### Ennusta ennen ajamista

Tämä on sama siirto, jota harjoittelit viikolla 6. **Ennen** kuin klikkaat Run, lue jokainen rivi, ennusta tuloste, kirjoita ennustus ylös. Sitten aja ja vertaa ennustusta todellisuuteen.

Yllä olevalle ohjelmalle, kun `age = 16`, ennustus on:

```text
Olen pahoillani, et ole tarpeeksi vanha.
Palaa 2 vuoden kuluttua.
```

Aja ohjelma. Saitko täsmälleen tämän? Jos kyllä, käsiajotapasi viikolta 6 on nyt käsiajotapasi koodissa, ja tämä on viikon arvokkain siirto. Jos ei, rivi, jossa ennustus ja todellisuus ensimmäisen kerran erosivat, on rivi, jota kannattaa katsoa.

Vaihda sitten `age = 16` arvoon `age = 19`, ennusta uudelleen ja aja uudelleen. Tulosteen tulisi muuttua *toiseen* haaraan. Jos molemmat ajot vastaavat ennustuksiasi, ohjelma tekee, mitä kirjoitit.

> **Pysähdy hetkeksi:** Katso yllä olevaa `if/else`-lohkoa ja oppitunnin alussa olevaa pseudokoodia. Ota kynä ja ympyröi paperilla ne osat, jotka *kirjaimellisesti ovat samat sanat* pseudokoodissa ja valitsemassasi oikeassa kielessä. Ympyröiden määrä yllättää sinut. Loput osat ovat syntaksia; ympyrät ovat ajattelua.

---

## Kielen valinta AT3:lle

AT3 saapuu **viikon 8 lopussa**. Se pyytää sinua ottamaan yhden palan omaa viikon 6 pseudokoodiasi, jossa on `IF/ELSE`, ja muuttamaan sen pieneksi ohjelmaksi, joka oikeasti ajaa — valitsemallasi kielellä. Palautat alkuperäisen pseudokoodin, ohjelman, lauseen siitä, minkä viikon 6 palan poimit ja miksi, ja kuvakaappauksen tulosteesta kahdelle syötteelle (yksi normaali, yksi hankala).

**Valitse kieli tällä viikolla.** Suositus on: valitse se, joka näyttää vähemmän pelottavalta, kun luet tätä itseopiskelua. Jos `console.log("...")` näyttää sinusta luettavammalta, valitse JavaScript. Jos `Console.WriteLine("...")` ja nimetyt tyypit `string` / `int` tuntuvat enemmän siltä huolelliselta pseudokoodilta, johon totuit viikolla 6, valitse C#. Voit vaihtaa milloin tahansa ennen AT3:n eräpäivää, mutta on paljon helpompi vaihtaa aikaisin kuin myöhään.

**Arvosana ei riipu siitä, minkä kielen valitset.** Se riippuu ajattelusta — siitä, tekeekö ohjelmasi saman työn kuin pseudokoodisi, ja siitä, osaatko puhua siitä rivi riviltä.

Lyhyt muistutus, jos unohdat: **kummallekaan kielelle ei tarvita asennusta**. JavaScript ajetaan selaimesi DevTools-konsolissa (`Ctrl+Shift+J` / `Cmd+Opt+J`). C# ajetaan **.NET Fiddlessä** osoitteessa `dotnetfiddle.net`, ilman tiliä.

---

## Yhteenveto ja mitä tulee seuraavaksi

**Tämän viikon keskeinen viesti:** *Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone osaa noudattaa niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain se syntaksi, jolla se kirjoitetaan.*

Tällä viikolla ylitit sillan. Tapasit kaksi oikeaa ohjelmointikieltä — JavaScriptin ja C#:n — ja näit ne vierekkäin jokaisessa käsitteessä: tuloste, muuttujat, laskutoimitus, vertailu, `if/else`. Kirjoitit ensimmäisen ohjelman valitsemallasi kielellä. Ajoit sen, ennustit ennen ajamista ja luit tulosteen sillä tavalla, jolla viikko 6 opetti sinut lukemaan jäljitystaulukkoa.

**Viikko 8** päättää kurssin. Se tuo mukaan **silmukat** koodissa — `WHILE`:n ja `FOR`:n, jotka jo tunnet viikon 6 pseudokoodista, nyt JavaScriptissä ja C#:ssa. Se esittelee oikeat **virheilmoitukset** oppimisen työkaluna (rikoit ohjelman; mitä tietokone sanoi?). Ja se laskeutuu **AT3**:n — käännöksesi yhdestä viikon 6 pseudokoodikatkelmasta pieneksi ajettavaksi ohjelmaksi. Kaikki, mitä kirjoitit tällä viikolla, on pohja; pidä koodisi tallessa.

Keskeinen kysymys vielä kerran — ja lue se ääneen, koska viikolla 8 saat vihdoin vastata siihen ohjelmalla, joka tekee tarkalleen sen, mitä sanoit:

> *Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?*
