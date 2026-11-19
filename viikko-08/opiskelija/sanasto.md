# Viikko 8 — Suljetaan silmukka

## Viikon 8 sanasto

Alla olevat termit liittyvät oppitunteihin 22, 23 ja 24. Määritelmät ovat tarkoituksella lyhyitä —
katso esimerkit itseopiskelumateriaalista. Kun termillä on eri kirjoitusasu JavaScriptissä ja
C#:ssa, molemmat muodot näytetään rinnakkain. Useat lopun termeistä on merkitty muodossa
kurssin päätös — uudelleen aiemmilta viikoilta; näissä merkinnöissä kerrotaan, mikä
termissä on tällä viikolla uutta.

### Silmukka

Ohjausrakenne, joka suorittaa koodilohkon useita kertoja lopetusehdon avulla. Tapasit
ajatuksen viikolla 5 muodossa , ja viikolla 6 kirjoitit sen pseudokoodina `TOISTA … KUNNES`
`WHILE`- ja `FOR each`-muodoissa. Tällä viikolla sama ajatus näkyy oikeassa ohjelmakoodissa sanoina `for` ja `while` sekä JavaScriptissä että C#:ssa. Silmukka on muodollinen nimi sille toista-kunnes -ajatukselle, jota pseudokoodisi jo käytti.

### `for` *(silmukan avainsana sekä JavaScriptissä että C#:ssa)*

Silmukkasana, jota käytät silloin, kun tiedät etukäteen, montako kertaa rungon pitää toistua. Molemmilla kielillä perusmuoto on sama:

```
for (alku; ehto; päivitys) { … runko … }
```

Esimerkiksi:

```javascript
for (let i = 1; i <= 5; i++) { console.log(i); }
for (int i = 1; i <= 5; i++) { Console.WriteLine(i); }
```

Ainoa ero on `let` JavaScriptissä ja `int` C#:ssa sekä tulostuskomento.

### `while` *(silmukan avainsana sekä JavaScriptissä että C#:ssa)*

Silmukkasana, jota käytät silloin, kun tiedät lopetusehdon, mutta et tarkkaa kierrosmäärää. Muoto on:

```
while (ehto) { … runko … }
```

Ehto tarkistetaan ennen jokaista kierrosta; niin kauan kuin ehto on tosi, runko suoritetaan uudelleen. Ohjelmoijan vastuulla on muuttaa rungon sisällä jotakin sellaista, että ehto muuttuu lopulta epätodeksi — muuten silmukka jatkuu ikuisesti.

### Laskuri

Pieni muuttuja, yleensä nimeltään (joskus ), joka seuraa sitä, kuinka pitkälle silmukka `i count`
on ehtinyt. Laskuri alkaa jostakin arvosta, ehto tarkistaa sitä ja päivitys muuttaa sitä.
Rakenteessa laskuri on , joka alkaa arvosta .

```javascript
for (let i = 1; i <= 5; i++) i 1
```

### Ehto (uudelleen viikolta 5; uusi käyttö viikolla 8 silmukoiden sisällä)

Pieni lauseke, joka on joko tosi tai epätosi. Viikolla 5 käytit ehtoja -rakenteissa, ja `IF/ELSE`
viikolla 7 kirjoitit ne oikeaan koodiin vertailuoperaattoreiden avulla ( , , ). Tällä viikolla

```
== >= <
```

samat ehdot elävät myös - ja -silmukoissa — silmukka jatkuu niin kauan kuin ehto `for while`
on tosi.

### Runko (silmukan)

Koodilohko, joka suoritetaan kerran joka kierroksella — se osa, joka on silmukan otsikon
jälkeisten aaltosulkeiden sisällä. Kaikki rungon sisään kirjoitettu tapahtuu joka `{ … }`
kierroksella. Rungossa voi olla tulostusta, sijoituksia ja jopa -rakenne. `if/else`

### Iteraatio

Yksi silmukan rungon suoritus. Silmukalla on viisi iteraatiota,

```javascript
for (let i = 1; i <= 5; i++) { … }
```

koska runko suoritetaan viisi kertaa. Sana iteraatio on vain muodollinen nimi yhdelle
toistokierrokselle.

### Ääretön silmukka

Silmukka, jonka ehto ei koskaan muutu epätodeksi, joten runko jatkaa ikuisesti. Tavallisin syy
on päivityksen unohtaminen: laskuri ei koskaan muutu. Selaimen konsolissa tulostetta alkaa
valua ruudulle, kunnes sivu jumiutuu; puolestaan katkaisee suorituksen `dotnetfiddle.net`
hetken kuluttua. Ratkaisu on varmistaa, että rungon sisällä tapahtuu jotakin, joka muuttaa
ehdossa testattavaa arvoa.

### Lähdekoodi

Ohjelman teksti sellaisena kuin sinä kirjoitit sen ennen suorittamista — -tiedoston sisältö `.js`
JavaScriptissä tai -tiedoston sisältö C#:ssa. Lähdekoodi on se, mitä palautat AT3:ssa. Se on `.cs`
ihmiselle luettavaa. Tulkki tai kääntäjä joko suorittaa sen tai näyttää virheilmoituksen.

### Ajaa (ohjelma)

Saada tietokone suorittamaan kirjoittamasi lähdekoodi. JavaScriptiä ajat liittämällä sen
selaimen DevTools-konsoliin ja painamalla Enter. C#-ohjelman ajat painamalla Run-painiketta
.NET Fiddlessä. Ajamisen jälkeen luet joko ohjelman tuotoksen tai sen virheilmoituksen.

### Virheilmoitus

Teksti, jonka tietokone näyttää, kun se ei pysty ymmärtämään koodiasi. Virheilmoitus kertoo,
mikä meni pieleen (esimerkiksi puuttuva sana, kirjoitusvirhe tai puuttuva puolipiste) ja
osoittaa rivin, joka aiheutti ongelman. Esimerkki: (JS) tai `ReferenceError: scre is not defined`
(C#). Virheilmoitukset eivät

```
CS0103: The name 'scre' does not exist in the current context
```

ole epäonnistumisia; ne ovat tietokoneen tapa kertoa, mistä kannattaa etsiä vikaa.

### Virhe

Rivi tai kohta lähdekoodissasi, joka saa ohjelman joko kaatumaan virheilmoitukseen tai
tulostamaan väärän tuloksen. Tämän kurssin tasolla virheet ovat lähes aina pieniä —
kirjoitusvirhe, puuttuva puolipiste, siellä missä pitäisi olla . Virhe on omassa koodissasi, `= ==`
ei tietokoneessa.

### Korjaus

Yksi pieni muutos, jonka teet lähdekoodiin, jotta virhe katoaa. Korjaus on tyypillisesti yksi
merkki (lisää sanaan ), yksi symboli (vaihda muotoon ) tai yksi näppäinpainallus

```
o scre = ==
```

(lisää puuttuva ). Korjauksen jälkeen ohjelma ajetaan uudelleen ja uusi tulos tarkistetaan. `;`

### Testaaminen (uudelleen viikolta 1; uusi käyttö viikolla 8 oikeassa ohjelmassa)

Ohjelman ajaminen käsin vähintään kahdella eri alkuarvolla ja sen tarkistaminen, että tuloste
on järkevä molemmilla kerroilla. Viikolla 1 testasit ohjetta antamalla sen kirjaimelliselle
suorittajalle; tällä viikolla testaat ohjelmaa vaihtamalla yhtä numeroa tai merkkijonoa
ohjelman alussa ja painamalla Run. Erillistä automaattista testityökalua ei käytetä.

### Esitys

Lyhyt puhuttu selitys omasta ohjelmastasi — mitä se tekee, miten se tekee sen, mikä meni
pieleen ja miten korjasit sen. AT3:ssa esitys kestää 2 minuuttia ja pidetään oppitunnilla 24.
Esitys on AT3:n suullinen osa.

### Konkatenaatio

Toiminto, jossa kaksi tekstinpätkää (tai teksti ja numero) yhdistetään yhdeksi tekstiksi - `+`
merkillä. tuottaa tekstin , jos on . Sekä JavaScript

```
"Hello, " + name "Hello, Aino" name "Aino"
```

että C# käyttävät tähän samaa -merkkiä. `+`

### Algoritmi (kurssin päätös — uudelleen viikolta 1)

Selkeä sarja kirjaimellisia vaiheita, joka vie tunnetusta syötteestä tunnettuun tuotokseen.
Viikolla 1 algoritmi oli arkinen nimi selkeille ohjeille. Viikolla 6 kirjoitit algoritmeja
pseudokoodina. Tällä viikolla annat algoritmin oikealle tietokoneelle JavaScript- tai C#-
lähdekoodina. Ajattelu ei ole muuttunut viikosta 1; muuttunut on vain se, kuka algoritmia
seuraa — ensin ihminen, sitten paperilla oleva pseudokoodi, nyt oikea kone.

### Pseudokoodi (kurssin päätös — uudelleen viikolta 6)

Silta-kieli, jota kirjoitit viikolla 6: täsmällisempää kuin tavallinen kieli, mutta vapaampaa kuin
oikea ohjelmakoodi. Tällä viikolla pseudokoodi on AT3:n lähtöpiste — valitset yhden oman
viikon 6 pseudokoodinpätkäsi ja käännät sen rivi riviltä JavaScriptiksi tai C#:ksi
itseopiskelumateriaalin käännöstaulukon avulla.
