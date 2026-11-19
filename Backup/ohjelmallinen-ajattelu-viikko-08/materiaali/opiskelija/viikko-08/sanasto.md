# Sanasto

## Viikon 8 sanasto

Alla olevat termit kattavat oppitunnit 22, 23 ja 24. Määritelmät ovat tarkoituksella lyhyitä — lue itseopiskeluteksti esimerkkien kontekstiin. Missä termillä on eri pinta JavaScriptissä ja C#:ssa, molemmat muodot näytetään rinnakkain. Useat lopussa olevat termit on merkitty **kurssin loppukoonti — palautettu mieleen aiemmilta viikoilta**; niissä kohdissa selitys nostaa esiin, mikä on uutta tällä viikolla.

### Silmukka

Ohjausrakenne, joka pyörittää koodilohkoa useita kertoja peräkkäin pysäytysehdon kanssa. Tapasit idean viikolla 5 (`REPEAT … UNTIL`) ja kirjoitit sen viikon 6 pseudokoodissa muodossa `WHILE` ja `FOR each`. Tällä viikolla sama idea saapuu oikeana koodina muodossa `for` ja `while` sekä JavaScriptissä että C#:ssa. Silmukka on muodollinen nimi sille *toista-kunnes*-idealle, jota pseudokoodisi jo käytti.

### `for` *(silmukan avainsana sekä JavaScriptissä että C#:ssa)*

Silmukan avainsana, jota käytät, kun tiedät etukäteen, montako kertaa haluat rungon pyörivän. Molemmat kielet kirjoittavat sen samalla tavalla: `for (aloitus; ehto; päivitys) { … runko … }`. Esimerkki, rinnakkain:

```js
for (let i = 1; i <= 5; i++) { console.log(i); }
```

```csharp
for (int i = 1; i <= 5; i++) { Console.WriteLine(i); }
```

Ainoa ero on `let` JS:ssä versus `int` C#:ssa ja tulostuskäsky.

### `while` *(silmukan avainsana sekä JavaScriptissä että C#:ssa)*

Silmukan avainsana, jota käytät, kun tiedät *pysäytysehdon* mutta et tarkkaa toistojen määrää. Muoto: `while (ehto) { … runko … }`. Ehto tarkistetaan **ennen** jokaista toistoa; niin kauan kuin se on tosi, runko pyörii vielä kerran. Sinä olet vastuussa siitä, että muutat jotakin rungon sisällä, jotta ehto eventuaalisesti muuttuu epätodeksi — muutoin silmukka pyörii ikuisesti.

### Laskuri

Pieni muuttuja, yleensä `i` (joskus `count`), joka pitää kirjaa siitä, kuinka pitkälle silmukka on edennyt. Laskuri alkaa jostakin arvosta, ehto testaa sen, päivitys muuttaa sitä. Lauseessa `for (let i = 1; i <= 5; i++)` laskuri on `i`, alkaen arvosta `1`.

### Ehto *(palautettu mieleen viikolta 5; uudelleenkäytetty viikolla 8 silmukoissa)*

Pieni lauseke, joka on joko tosi tai epätosi. Tapasit ehdot viikolla 5 `IF/ELSE`:n sisällä ja kirjoitit ne koodissa viime viikolla vertailuoperaattoreilla (`==`, `>=`, `<`). Tällä viikolla samat ehdot asuvat myös `for`- ja `while`-silmukoissa — silmukka pyörittää runkoa **niin kauan kuin** ehto on tosi.

### Runko *(silmukan)*

Koodilohko, joka pyörii kerran per toisto — osa aaltosulkeiden `{ … }` välissä silmukan otsikon jälkeen. Mitä tahansa laitatkin runkoon, tapahtuu joka kerralla. Runko voi sisältää tulostuskäskyjä, sijoituksia ja jopa `if/else`:n.

### Iteraatio

Yksi silmukan rungon ajo. Silmukalla `for (let i = 1; i <= 5; i++) { … }` on viisi iteraatiota, koska runko pyörii viisi kertaa. Sana *iteraatio* on vain muodollinen nimi "yhdelle toistolle".

### Ikuinen silmukka

Silmukka, jonka ehto ei koskaan muutu epätodeksi, joten runko jatkaa pyörimistä ikuisesti. Yleisin syy on päivitysvaiheen unohtaminen (laskuri ei koskaan muutu). Selaimen konsolissa näet tulosteen vyöryvän, kunnes sivu jumiutuu; `dotnetfiddle.net`:ssä ajo katkeaa aikakatkaisun vuoksi muutaman sekunnin kuluttua. Korjaus on varmistaa, että jokin rungon sisällä muuttaa arvoa, jota ehto testaa.

### Lähdekoodi

Ohjelmasi teksti, ennen kuin se ajetaan — `.js`-tiedoston (JavaScript) tai `.cs`-tiedoston (C#) sisältö. Lähdekoodi on se, mitä palautat AT3:ta varten. Se on ihmisluettavaa. Tulkki tai kääntäjä lukee sen ja joko ajaa sen tai tulostaa virheen.

### Aja *(ohjelma)*

Saada tietokone suorittamaan kirjoittamasi lähdekoodi. JavaScriptissä ajat koodin liittämällä sen selaimen DevTools-konsoliin ja painamalla Enter; C#:ssa painat **Run**-nappia .NET Fiddlessä. Kun olet ajanut ohjelman, luet sen **tulosteen** (tai sen **virheilmoituksen**).

### Virheilmoitus

Teksti, jonka tietokone tulostaa, kun se ei voi ymmärtää koodiasi. Viesti nimeää, mikä meni vikaan (usein puuttuva sana, väärin kirjoitettu nimi, puuttuva puolipiste) ja osoittaa riviin, joka sen aiheutti. Esimerkki: `ReferenceError: scre is not defined` (JS) tai `CS0103: The name 'scre' does not exist in the current context` (C#). Virheilmoitukset eivät ole epäonnistumisia; ne ovat tietokoneen tapa kertoa sinulle, mihin katsoa.

### Bugi

Rivi lähdekoodissasi, joka saa ohjelman joko kaatumaan virheilmoitukseen tai tulostamaan väärin. Bugit tämän kurssin tasolla ovat lähes aina pieniä — kirjoitusvirhe, puuttuva puolipiste, `=` siellä, missä `==` kuuluisi olla. Bugi on **sinun koodissasi**, ei tietokoneessa.

### Korjaus

Yksi pieni muutos, jonka teet lähdekoodiin, jotta bugi katoaa. Korjaus on tyypillisesti yksi merkki (lisää `o` sanaan `scre`), yksi symboli (vaihda `=` muotoon `==`) tai yksi näppäilys (lisää puuttuva `;`). Korjauksen soveltamisen jälkeen ajat ohjelman uudelleen ja tarkistat uuden tulosteen.

### Testi *(palautettu mieleen viikolta 1; uudelleenkäytetty viikolla 8 oikealla ohjelmalla)*

Ohjelman ajaminen käsin vähintään kahdella eri alkuarvolla ja sen tarkistaminen, että tuloste on järkeenkäypä joka kerta. Viikolla 1 "testasit" ohjeen antamalla sen sananmukaiselle tulkitsijalle; tällä viikolla testaat ohjelmaa vaihtamalla yhden numeron tai merkkijonon alussa ja painamalla Run. Mitään automaattista testaustyökalua ei käytetä.

### Esitys

Lyhyt, suullinen selitys ohjelmastasi — mitä se tekee, miten se tekee sen, mikä meni vikaan, miten korjasit sen. AT3:lle esitys on **2 minuutin** pituinen ja pidetään luokassa oppitunnilla 24. Esitys on AT3:n **suullinen osuus**.

### Konkatenaatio

Toiminto, jossa kaksi tekstipalaa (tai teksti ja numero) yhdistetään yhdeksi tekstipalaksi `+`:lla. `"Hello, " + name` tuottaa `"Hello, Aino"`, jos `name` on `"Aino"`. Sekä JavaScript että C# käyttävät `+`:aa tähän samalla tavalla.

### Algoritmi *(kurssin loppukoonti — palautettu mieleen viikolta 1)*

Selkeä sarja sananmukaisia vaiheita, joka vie sinut tunnetusta syötteestä tunnettuun tulosteeseen. Tapasit sanan viikolla 1 arkikielisenä nimenä selkeille ohjeille, kirjoitit algoritmeja pseudokoodina viikolla 6, ja tällä viikolla vihdoin annat sellaisen oikealle tietokoneelle JavaScript- tai C#-lähdekoodina. Ajattelu ei ole muuttunut viikolta 1; se mikä muuttuu, on se, kuka algoritmia seuraa — ensin ihminen, sitten pseudokoodi paperilla, nyt oikea kone.

### Pseudokoodi *(kurssin loppukoonti — palautettu mieleen viikolta 6)*

Siltakieli, jota kirjoitit viikolla 6: täsmällisempi kuin suomi, vähemmän tiukka kuin oikea koodi. Tällä viikolla pseudokoodi on AT3:n **lähtökohta** — valitset yhden palan omaa viikon 6 pseudokoodiasi ja käännät sen rivi riviltä JavaScriptiin tai C#:iin käyttäen itseopiskelutekstin käännöstaulukkoa.
