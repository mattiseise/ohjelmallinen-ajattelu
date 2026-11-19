# Oppitunti 20 — Ensimmäiset komennot: tuloste, arvot ja muuttujat

(kaksi kieltä rinnakkain)
Tällä oppitunnilla kirjoitat ensimmäisen oikean ohjelmakoodisi. Kaikki alla oleva näkyy
kahdesti — kerran JavaScriptinä ja kerran C#:na. Valitse yksi kieli, jolla oikeasti kokeilet,
mutta lue myös toinen. Juuri rinnakkaisuus on osa oppimista.

### Tulostaminen konsoliin

Pienin mahdollinen ohjelma on ohjelma, joka tulostaa tekstiä. Viime viikolla kirjoitit
pseudokoodissa . Tässä sama ajatus molemmilla kielillä. `WRITE "Hello"`
JavaScript

```javascript
console.log("Hello, console");
```

C

```csharp
Console.WriteLine("Hello, console");
```

Lue rivit vierekkäin. JavaScriptissä tulostuskomennon nimi on . C#:ssa se on `console.log`
. Molemmat ottavat lainausmerkkien sisällä olevan tekstin ja tulostavat sen `Console.WriteLine`
konsoliin. Molemmat päättyvät puolipisteeseen . JavaScript ei sitä aina pakota, mutta tällä `;`
kurssilla pidämme puolipisteen mukana, jotta vertailu C#:aan pysyy helpompana. C#:ssa
puolipiste on pakollinen.
JavaScript-version ajaminen: avaa selain, paina Macilla tai Windowsissa/Linuxissa `Cmd+Opt+J`
(tai avaa hiiren oikealla Tarkastele/Inspect ja valitse Console). Liitä koodi, `Ctrl+Shift+J`
paina Enter ja katso tuloste.
C#-version ajaminen: avaa selaimessa . Valitse yläreunasta Console. Liitä `dotnetfiddle.net`
koodi editoriin -metodin sisälle. Paina Run. Tuloste ilmestyy alempaan ruutuun. `Main`
Kaksi ympäristöä, kaksi hieman eri sanaa, sama tehtävä: tulosta yksi rivi.

### Muuttujat: arvon nimeäminen

Viime viikolla kirjoitit . Oikeassa ohjelmointikielessä vastaava `SET passwordLength TO 7`
ajatus on muuttujan määrittely ja arvon sijoittaminen siihen.
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

Ajatus on sama kummallakin puolella: tee nimetty säiliö, laita siihen arvo ja tulosta arvo. Erot
näkyvät pinnalla. JavaScriptissä kirjoitat uuden muuttujan eteen . Et kerro erikseen, mitä `let`
tyyppiä arvo on — JavaScript päättelee sen arvosta ( on tekstiä, on luku). C#:ssa taas `"Lyra" 16`
kirjoitat muuttujan eteen tyypin: tekstille, kokonaisluvulle. `string int`
Tämä ei ole eri ajattelutapa. Se on yksi lisäsana.
Molemmat kielet käyttävät merkkiä arvon sijoittamiseen. Ja molemmilla kielillä muuttujan `=`
voi tulostaa antamalla sen nimen tulostuskomennolle. Muuttujan nimen ympärille ei tule
lainausmerkkejä, koska silloin pyytäisit tietokonetta tulostamaan sanan name, et muuttujan
sisällä olevaa arvoa.
Pysähdy hetkeksi: Kumpi näyttää sinusta ensi silmäyksellä helpommin luettavalta:
JavaScriptin vai C#:n ? Oikeaa vastausta ei

```javascript
let name = "Lyra"; string name = "Lyra";
```

ole. Huomaa vain oma reaktiosi — se auttaa kielivalinnassa.

### Ensimmäinen lasku

Viime viikon pseudokoodissa käytit sijoituksia kuten . `SET total TO unitPrice * quantity`
Oikeat ohjelmointikielet tekevät saman. Perusoperaattorit ( , , , ) näyttävät samoilta `+ - * /`
molemmilla kielillä.
Tämän viikon juokseva esimerkki on: montako vuotta sinulla on 18 ikävuoteen? Annetusta
iästä lasketaan ja tulostetaan tulos. `18 - age`
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

Lue nämä vierekkäin. Algoritmi on identtinen: tee muuttuja , laske erotus , tulosta `age 18 - age`
otsikko, tulosta tulos. Sanat ovat erilaisia — vs. , vs. — `let int console.log Console.WriteLine`
mutta askeleet vastaavat toisiaan yksi yhteen.
Voit myös yhdistää otsikon ja numeron samalle riville -merkillä. `+`
JavaScript

```javascript
let age = 16;
console.log("You have " + (18 - age) + " years to go.");
```

C

```csharp
int age = 16;
Console.WriteLine("You have " + (18 - age) + " years to go.");
```

Tässä yhdistää tekstin ja numeron yhdeksi tulostettavaksi tekstiksi. Tätä kutsutaan `+`

konkatenaatioksi.

### Tulosteen lukeminen

Tällä viikolla tärkein virheenetsintätyökalusi on tulosteen lukeminen. Ei breakpointteja, ei
askeltavaa debuggeria, ei testikehyksiä. Jos ohjelma tulostaa sen, mitä odotit, se toimi. Jos se
tulostaa jotain muuta, ero odotetun ja todellisen välillä on virhe — ja se on virhe omassa
koodissasi, aivan kuten viikko 6 opetti sinua ajattelemaan.
Jos mitään ei näy, ohjelma ei ehkä koskaan päässyt tulostusriville asti. Ehkä se pysähtyi
aiemmin virheeseen. Ehkä ajoit väärän tiedoston. Ehkä et painanut Run. Jos näkyvissä on
virheilmoitus, lue se. Tulkki tai kääntäjä osoittaa usein suoraan ongelmakohtaan.

### Ajattelu on sama

Tässä on sivulta sivulle kulkeva tärkein yhteenveto. Molemmat ohjelmat tekevät tämän:
1. luo muuttujan ja laita siihen luku `age`
2. luo muuttujan ja laita siihen `yearsToAdulthood 18 - age`
3. tulosta otsikko
4. tulosta arvo
Tämä on algoritmi. Se on JavaScriptissä sama algoritmi kuin C#:ssa. Erot ( vs. , `let int`
vs. , puolipiste pakollinen vs. käytäntönä) ovat syntaksia. `console.log Console.WriteLine`
Syntaksi on sopimus, jonka teet yhden tietyn tietokonejärjestelmän kanssa. Ajattelu on se
varsinainen asia.
Pysähdy hetkeksi: Mitä tapahtuisi, jos liittäisit JavaScript-koodin .NET Fiddleen tai
C#-koodin selaimen JavaScript-konsoliin? Kokeile, jos haluat. Saatava virheilmoitus
kertoo kielellä: “tämä ei ole minun syntaksiani”.
