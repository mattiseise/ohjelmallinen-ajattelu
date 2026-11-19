# Sanasto

## Viikon 7 sanasto

Alla olevat termit kattavat oppitunnit 19, 20 ja 21. Määritelmät ovat tarkoituksella lyhyitä — lue itseopiskelu kontekstuaalisia esimerkkejä varten. Kaksi termiä (`console.log` ja `Console.WriteLine`) ovat kielikohtaisia merkintöjä paritettuna rinta rinnan. Yksi termi lopussa (*silmukka*) on viikon 8 ennakko, merkittynä sellaiseksi.

### Ohjelmointikieli

Sanojen ja sääntöjen joukko, jonka tietokone osaa lukea ja ajaa. JavaScript ja C# ovat kaksi tällaista kieltä. Ohjelmointikieli eroaa pseudokoodista siinä, että tietokone itse osaa tulkata tai kääntää sen, ei vain ihmislukija. Ajattelu — sekvenssi, ehto, toisto — on sama kuin pseudokoodissa; kieli on vain se täsmällinen muoto, jonka se saa.

### Syntaksi

Sääntö siitä, *miten sanat täytyy järjestää* ohjelmointikielessä. Mitkä sanat ovat olemassa, missä järjestyksessä ne saavat esiintyä, mitkä välimerkit niiden ympärillä on oltava, mihin lause päättyy. Syntaksia noudattava koodi ajaa. Syntaksin rikkova koodi pysähtyy virheilmoituksella. Syntaksi on se, mitä tietokone lukee; ajattelu on se, mitä kirjoitat.

### Käsky

Yksittäinen ohje, jonka tietokone osaa suorittaa. `console.log("Hello")` on käsky: "tulosta teksti *Hello* konsoliin." `int age = 16;` on käsky: "tee muuttuja nimeltä `age`, tyyppinä `int`, ja laita siihen `16`." Ohjelmat ovat käskyjen sekvenssejä, yksi toisensa jälkeen.

### Tulkki *(epämuodollinen)*

Ohjelma, joka lukee koodisi rivi kerrallaan ja ajaa kunkin rivin sitä mukaa. JavaScript selaimessa tulkataan: liimaa rivi konsoliin, paina Enter, näe tulos. Ei erillistä "rakenna sitten aja" -vaihetta.

### Kääntäjä *(epämuodollinen)*

Ohjelma, joka lukee koko koodisi kerralla, kääntää sen matalamman tason muotoon, jonka tietokone osaa ajaa nopeammin, ja ajaa sitten tämän käännetyn version. C# käännetään ennen ajamista. Opiskelijan näkökulmasta tällä viikolla pääero on siinä, että kääntäjä voi kieltäytyä edes käynnistymästä, jos koodissasi on syntaksivirhe.

### Konsoli

Pieni tekstialue, johon ohjelma tulostaa tulostetta ja (joskus) lukee syötettä. Selaimen **DevTools-konsoli** on paikka, johon JavaScript tulostaa. **.NET Fiddlen** tulostelaatikko on paikka, johon C# tulostaa. Konsoli on se paikka, johon viikon 6 pseudokoodin `WRITE` vihdoin laskeutuu — oikealle ruudulle, oikeassa ohjelmassa.

### Tuloste

Sitä, mitä ohjelma lähettää näkyväksi — rivi tekstiä konsolissa, numero, kyllä/ei. JavaScriptissä kirjoitat tulosteen `console.log(...)`:lla. C#:ssa `Console.WriteLine(...)`:lla. Tuloste on se, miten ohjelma puhuu takaisin.

### Muuttuja

Nimetty säilö yhdelle arvolle, joka voi muuttua ohjelman ajon aikana. *(Sama idea kuin viikolla 6, nyt oikeassa kielessä.)* JavaScriptissä: `let age = 16;`. C#:ssa: `int age = 16;`. Nimi `age` pysyy samana; sisällä oleva arvo voi muuttua. Hyvä muuttujan nimi kuvaa, mitä arvo tarkoittaa.

### Arvo

Todellinen sisältö, joka on tallennettuna muuttujaan tietyllä hetkellä — pala tekstiä (`"Lyra"`), kokonaisluku (`16`), kyllä/ei (`true`). Muuttuja on merkitty laatikko; arvo on se, mitä laatikon sisällä on juuri nyt.

### Sijoitus

Toiminta, jossa arvo laitetaan muuttujaan. Sekä JavaScript että C# kirjoittavat sen `=`:lla. `let age = 16;` (JS) ja `int age = 16;` (C#) ovat sijoituksia. Pseudokoodi `SET age TO 16` on sama idea eri pinnassa.

### Merkkijono (string)

Pala tekstiä, kirjoitettuna lainausmerkkien väliin. `"Hello, console"` on merkkijono. `"16"` on myös merkkijono, vaikka se näyttää numerolta — lainausmerkit tekevät siitä tekstiä. Sekä JavaScript että C# käyttävät kaksoislainausmerkkejä. Sana *string* on lyhennys "string of characters" -ilmauksesta (merkkijono).

### Int / numero

Kokonaisluku, käytettynä koodissa arvona ilman lainausmerkkejä. C# kutsuu tätä tyyppiä **`int`**:ksi (lyhennys sanasta *integer*) ja pyytää sinua nimeämään sen, kun esittelet muuttujan: `int age = 16;`. JavaScript kutsuu sitä yksinkertaisesti **numeroksi** ja päättelee sen arvosta: `let age = 16;`. `16` on int / numero; `"16"` on merkkijono.

### Ehto

Pieni lauseke, joka on joko tosi tai epätosi, kirjoitettuna `if`:n pyöreiden sulkeiden sisään. `age >= 18` on ehto. Ehdon koko pointti on se, että `if/else` voi ottaa eri haaran riippuen siitä, onko ehto tosi. *(Uudelleenvierailtuna viikolta 6 — sama idea, nyt koodissa.)*

### If / else

Ohjausrakenne, joka ajaa yhden koodilohkon, jos ehto on tosi, ja toisen lohkon, jos se on epätosi. Sekä JavaScriptissä että C#:ssa: `if (test) { ... } else { ... }`. `else`-osa on valinnainen — `if` yksin on kelvollista koodia. *(Uudelleenvierailtuna viikolta 6 — sama idea, nyt koodissa.)*

### Vertailuoperaattori

Symboli, joka vertaa kahta arvoa ja tuottaa tosi/epätosi-tuloksen. Tällä kurssilla käytetyt kuusi ovat `==` (yhtä kuin), `!=` (eri kuin), `>` (suurempi kuin), `>=` (suurempi tai yhtä suuri), `<` (pienempi kuin), `<=` (pienempi tai yhtä suuri). Nämä kuusi ovat olennaisesti identtiset JavaScriptissä ja C#:ssa. (JavaScriptissä on myös `===`, joka on tiukempi yhtäsuuruuden muoto; kumpikin muoto toimii siihen, mitä tällä viikolla teemme.)

### `console.log` *(JavaScript)*

JavaScript-käsky, joka tulostaa konsoliin. `console.log("Hello")` tulostaa `Hello`:n omalle rivilleen. Voit antaa sille merkkijonon, numeron, muuttujan tai useampia arvoja pilkulla erotettuna. Se on pääasiallinen tapa, jolla JavaScript-ohjelma näyttää sinulle, mitä tapahtuu.

### `Console.WriteLine` *(C#)*

C#-käsky, joka tulostaa konsoliin. `Console.WriteLine("Hello");` tulostaa `Hello`:n omalle rivilleen, jonka jälkeen tulee rivinvaihto. Osa `WriteLine` on yksi sana, isolla `W`:llä ja isolla `L`:llä on merkitystä. Puolipiste lopussa on pakollinen C#:ssa.

### Silmukka *(eteenpäin katsova — viikon 8 keskeinen aihe)*

Ohjausrakenne, joka ajaa koodilohkoa useita kertoja peräkkäin pysäytysehdolla. Tapasit idean viikon 6 pseudokoodissa muodossa `WHILE` ja `FOR`. Ensi viikolla sama idea saapuu JavaScriptiin ja C#:aan muodossa `while` ja `for`, rinta rinnan. Tällä viikolla et tarvitse kirjoittaa silmukoita koodissa — termi on tässä, jotta sana ei ole uusi viikolla 8.
