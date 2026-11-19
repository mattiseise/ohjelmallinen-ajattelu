# Oppitunti 19 — Miksi ohjelmointikieliä on olemassa

(kieliriippumaton oppitunti — ei vielä toimivaa koodia)

### Pseudokoodista ohjelmakoodiin

Viime viikon pseudokoodi oli jo huolellista. Käytit pientä avainsanajoukkoa, sisensit lohkot ja
suljit jokaisen -rakenteen -rivillä. Miksi tämä ei silti vielä riitä? `IF ENDIF`
Siksi, että pseudokoodin lukija ja ohjelmakoodin lukija ovat eri asioita. Pseudokoodi on tehty
ihmislukijalle, joka ymmärtää englantia ja pystyy täydentämään vähän puuttuvaa
taustatietoa. Tietokone ei tuo mukanaan tätä joustavuutta. Se tuntee vain ne sanat ja merkit,
joille se on rakennettu. Jos sivulla olevat sanat eivät kuulu tähän tarkkaan joukkoon, tietokone
pysähtyy.
Siirtyminen pseudokoodista koodiin ei ole valtava älyllinen loikka. Se on kiristyminen.
Vaihdat omat englanninkieliset avainsanasi niihin täsmällisiin sanoihin ja merkkeihin, jotka
yksi tietty tietokonejärjestelmä tunnistaa. Ajattelu — järjestys, ehto, toisto, muuttujat, syöte,
käsittely, tuotos — ei muutu lainkaan.
Pysähdy hetkeksi: Ota yksi oma viikon 6 pseudokoodinpätkäsi ja lue se ääneen.
Huomaa, mitkä rivit toimivat vain siksi, että lukija on ihminen — esimerkiksi , `wait`
käyttäjä kirjoittaa ikänsä tai näytä ystävällinen viesti. Juuri nämä kohdat tarvitsevat
oikeassa koodissa tarkemman, tietokoneen hyväksymän vastineen.

### Mitä syntaksi on?

Syntaksi on sääntö siitä, miten sanat ja merkit pitää järjestää, jotta lukija pystyy tulkitsemaan
tekstin oikein. Jokaisessa kielessä on syntaksi, ei vain ohjelmointikielissä.
Esimerkki — englanti ja suomi. Englanniksi sanotaan the red car. Suomeksi sanotaan
punainen auto. Syntaksi — esimerkiksi sanajärjestys — on eri sopimus eri kielessä. Jos kirjoitat
englanniksi car red, ihminen voi silti usein arvata, mitä tarkoitit, koska ihmiset ovat joustavia.
Tietokone ei ole.
Esimerkki — limsa-automaatti. Juoma-automaatti hyväksyy vain tietyn muotoiset kolikot ja
tietyn toimintajärjestyksen. Jos painat nappia ennen kolikon syöttämistä, mitään ei tapahdu.
Automaatin syntaksi on: kolikko ensin, nappi vasta sitten.
Esimerkki — tiedostopolku. on toimiva polku. `Users/maria/documents/report.txt`
(välilyönti, mutta ei kauttaviivaa) ei ole. Tietokone ei sano: `Users/maria/documents report.txt`
“luulen, että tarkoitit sitä tiedostoa documents-kansiossa”. Se sanoo, ettei tiedostoa löydy.
Kauttaviiva on osa syntaksia.
Ohjelmointikielen syntaksi on täsmälleen tällaisten sääntöjen kokonaisuus: mitkä sanat ovat
sallittuja, missä järjestyksessä ne saavat esiintyä, mitä välimerkkejä täytyy olla ympärillä ja
mistä yksi lause loppuu. Jos koodisi noudattaa sääntöjä, tietokone voi ajaa sen. Jos yksikin
pilkku, lainausmerkki tai sulku on väärässä paikassa, tietokone pysähtyy ja näyttää

virheilmoituksen.

Tämä ei ole ansa. Tämä on sopimus. Korjaa kohta, jonka virheilmoitus osoittaa, ja koodi voi taas
toimia.

### Tulkki ja kääntäjä — epämuodollisesti

Tällä viikolla kohtaat kaksi sanaa sille asialle, joka lukee koodiasi ja saa sen käyntiin: tulkki ja
kääntäjä.
Tulkki lukee koodia rivi kerrallaan ja suorittaa rivit sitä mukaa kun niitä luetaan. Selaimessa
ajettava JavaScript toimii näin: selain lukee rivin , suorittaa sen, siirtyy

```javascript
console.log("Hello")
```

seuraavaan riviin ja suorittaa sen. Ei ole erillistä rakenna ensin, aja vasta sitten -vaihetta.
Kääntäjä lukee koko ohjelman ensin, muuntaa sen alemmantasoiseksi muodoksi, jota
tietokone voi suorittaa nopeammin, ja vasta sitten ajaa tämän muunnetun version. C# toimii
tällä periaatteella. Verkkoalusta tai oikea .NET-työkalu kääntää koodisi ensin ja suorittaa sen
vasta sitten.
Opiskelijan näkökulmasta ero näkyy tällä viikolla lähinnä virheilmoituksissa. C# voi ilmoittaa
jo ennen suorittamista: “tätä ei voi kääntää”. JavaScript näyttää virheen usein vasta ohjelman
käynnistyessä. Sinun ei tarvitse osata tätä eroa vielä tarkasti. Riittää, että tunnistat sanat, kun
ne tulevat vastaan.

### Kaksi kieltä, yksi ajattelutapa

Tällä kurssilla kohdataan kaksi oikeaa ohjelmointikieltä rinnakkain.
JavaScript (usein lyhyesti JS) on verkkoselaimen kieli. Jokaisessa käyttämässäsi selaimessa —
Chromessa, Firefoxissa, Edgessä, Safarissa — on JavaScript-tulkki valmiina. Se on käytännössä
yhden pikanäppäimen päässä sinusta juuri nyt DevTools-konsolissa. JavaScriptiä käytetään
verkkosivujen toiminnallisuuteen: nappeihin, valikoihin, päivittyviin näkymiin. Sitä käytetään
myös palvelimilla esimerkiksi Node.js:n avulla, mutta siihen ei mennä tällä viikolla.
C# (lausutaan see sharp) on yksi Microsoftin .NET-alustan pääkielistä. C#:lla tehdään
työpöytäsovelluksia, verkkopalveluita, mobiilisovelluksia ja myös suuri osa maailman
videopeleistä esimerkiksi Unityn kautta. Sinun ei tarvitse asentaa .NET:iä; verkossa toimiva
.NET Fiddle ajaa C#-koodia selaimessa ilman käyttäjätunnusta.
Kaksi kieltä, kaksi kotipaikkaa, yksi ajattelutapa. Ajattelu — järjestys, ehto, toisto, muuttujat,
syöte, käsittely, tuotos — siirtyy kielestä toiseen. Syntaksi on se, minkä kukin kieli on
päättänyt pinnalleen.

### Miksi tämä on tärkeää IT-ammattilaiselle?

IT-ammattilaisena luet urallasi enemmän koodia kuin kirjoitat. Todennäköisesti kohtaat urasi
aikana kolme, neljä tai viisi eri ohjelmointikieltä, koska työ vaihtuu, tiimi vaihtuu tai projekti
vaihtuu. Ihmiset, jotka jäävät jumiin, alkavat ajatella itseään “JavaScript-ihmisenä” tai “C#-
ihmisenä”. Ihmiset, jotka pärjäävät hyvin, näkevät jokaisen uuden kielen vain uutena pintana
tutun pohjan päällä.
Siksi kaksi kieltä rinnakkain heti ensimmäisessä ohjelmointikokemuksessa on hyödyllistä. Kun
näet ja vierekkäin, kaksi asiaa käy

```javascript
console.log("Hello") Console.WriteLine("Hello")
```

väistämättä selväksi: kyllä, sanat ovat erilaisia; ei, tietokoneelle annettu työ ei ole erilainen.
Tämä oivallus on yksi viikon 7 tärkeimmistä anneista.
Pysähdy hetkeksi: Kirjoita vihkoosi yksi lause, joka jatkaa ajatusta:
“Ohjelmointikieltä tarvitaan, ei pelkkää pseudokoodia, koska…” Jos lauseessasi näkyy
sana tietokone, olet todennäköisesti oikeilla jäljillä.
