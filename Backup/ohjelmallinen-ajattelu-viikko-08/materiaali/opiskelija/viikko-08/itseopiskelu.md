# Silmukan sulkeminen — ensimmäinen oikea ohjelmasi

## Johdanto

Olet saapunut kurssin viimeiselle viikolle. Kahdeksan viikkoa sitten aivan ensimmäinen oppitunti esitti yhden kysymyksen, ja olet työskennellyt sen vastaamiseksi siitä lähtien:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

Seitsemän viikon ajan vastaus tuli paloissa. Viikolla 1 tietokone oli sananmukainen tulkitsija. Viikolla 2 opit pilkkomaan tehtävän pienempiin osiin. Viikoilla 3 ja 4 nimettiin rakennuspalikat: syöte, käsittely, tuloste; sekvenssi, vaihtoehto, toisto. Viikolla 5 esiteltiin täsmälliset ehdot. Viikko 6 oli pseudokoodi — hetki, jolloin ohjeesi lakkasivat olemasta pelkästään huolellisia ja alkoivat näyttää oikealta koodilta. Viikolla 7 ylitettiin lopulta silta JavaScriptiin ja C#:iin: tuloste, muuttujat, `if/else`.

Tällä viikolla vastaus muuttuu konkreettiseksi. Kirjoitat pienen ohjelman valitsemallasi kielellä — JavaScriptillä tai C#:lla — ja ajat sen oikealla koneella. Valitset, mitä ohjelma tekee, omasta **viikon 6 pseudokoodistasi**. Ajat sen kahdella alkuarvolla. Rikot sen (tarkoituksella tai vahingossa), luet virheilmoituksen ja korjaat yhden rivin. Ja oppitunnilla 24 pidät **2 minuutin** suullisen esityksen: mitä se tekee, miten, mikä meni vikaan, miten korjasit. Tämä on **AT3**.

**Tämän viikon keskeinen viesti:** *Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen JavaScriptiksi tai C#:ksi, ajat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi on lakannut olemasta mystinen asia.*

Molemmat kielet ovat ensiluokkaisia tällä viikolla, kuten viikolla 7. Jokainen esimerkki esiintyy kerran JavaScriptillä ja kerran C#:lla, rinnakkain. Lue valitsemasi kielen sarake ensin, mutta vilkaise toista — koodin *muoto* on melkein sama, ja tuon huomaaminen on puolet pointista.

---

## Oppitunti 22 — Silmukat koodissa

### Miksi silmukat ovat olemassa

Viikolla 5 kirjoitit ensimmäiset *toista-kunnes*-lauseesi (`REPEAT … UNTIL the password is long enough`), ja viikolla 6 kirjoitit pseudokoodisilmukoita samanmuotoisina — `WHILE password is too short DO …`, `FOR each item in the list DO …`. Ne olivat jo silmukoita. Puuttui vain tietokone, joka osaisi lukea niitä.

**Silmukka** on muodollinen nimi sille *toista-kunnes*-idealle, jota pseudokoodisi jo käytti — vain nyt toistaja on tietokone, ei ihminen. Ajattelu on identtistä. Mikä muuttuu tällä viikolla, on syntaksi: pieni kiinteä muoto, jonka sekä JavaScript että C# hyväksyvät, ja jossa on neljä nimettyä osaa, joihin voit osoittaa. Tietokone tarvitsee kolme asiaa silmukoidakseen: *Mistä aloitan? Milloin lopetan? Mitä muutan jokaisen toiston välissä?* Silmukka on paikka, jossa nuo kolme vastausta asuvat yhdessä siistissä lohkossa.

> **Pysähdy hetkeksi:** Etsi yksi viikon 6 pseudokoodisivu, jossa kirjoitit `WHILE`, `REPEAT` tai `FOR each`. Lue se. Kirjoita omin sanoin, mikä toistuu ja mikä saa toiston pysähtymään. Nuo kaksi vastausta ovat täsmälleen sitä, mitä `for`- tai `while`-silmukka tarvitsee.

### `for`-silmukan muoto

Tämän viikon hyödyllisin silmukka on **`for`-silmukka**. Käytä sitä, kun tiedät etukäteen, montako kertaa haluat rungon pyörivän — esimerkiksi "tulosta numerot 1–5" tai "sano hei kolme kertaa". Tässä sama yksinkertainen laskuri molemmilla kielillä.

#### JavaScript

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

#### C#

```csharp
for (int i = 1; i <= 5; i++) {
    Console.WriteLine(i);
}
```

Molemmat ohjelmat tulostavat:

```text
1
2
3
4
5
```

Pätkät ovat lähes identtiset. Molemmat käyttävät avainsanaa `for`, kolmea pientä palaa pyöreissä sulkeissa puolipistein erotettuina ja aaltosulkeisen rungon. Ainoat pintaerot ovat täsmälleen ne viikolta 7: `let` vs. `int` ja `console.log` vs. `Console.WriteLine`.

### Laskuri, ehto, runko, päivitys

`for`-silmukan sulkujen sisällä on kolme pientä palaa. Lisää aaltosulkeinen lohko perään, ja `for`-silmukalla on neljä nimettyä osaa:

- **Laskuri** — pieni muuttuja, yleensä `i`, joka pitää kirjaa siitä, kuinka pitkälle silmukka on edennyt. Yllä olevassa pätkässä laskuri alkaa arvosta `1`.
- **Ehto** — kyllä/ei-testi, joka suoritetaan *ennen* jokaista toistoa. Niin kauan kuin ehto on tosi, silmukka ajaa rungon vielä kerran. Yllä oleva ehto on `i <= 5` — "niin kauan kuin laskuri on edelleen 5 tai alle, jatka".
- **Runko** — aaltosulkeinen lohko. Mitä tahansa kirjoitatkin tähän, tapahtuu kerran per toisto. Yllä oleva runko on vain `console.log(i);` (tai `Console.WriteLine(i);`), joten jokainen toisto tulostaa nykyisen laskurin.
- **Päivitys** — mikä muuttuu jokaisen toiston välissä. Yleensä se lisää yhden laskuriin. Yllä oleva päivitys on `i++`, joka on lyhennys "kasvata `i`:tä yhdellä".

Lue silmukka ääneen kerran: "**Laskuri** alkaa 1:stä. **Ehto**: niin kauan kuin laskuri on 5 tai alle. **Runko**: tulosta laskuri. **Päivitys**: lisää yksi laskuriin." Molemmat kielet sallivat sinun lukea sen täsmälleen tässä järjestyksessä.

Jos laskuri ei koskaan muutu — jos unohdit `i++`:n — ehto pysyy totena ikuisesti eikä silmukka koskaan pysähdy. Tämä on bugi nimeltä **ikuinen silmukka**, ja nimeämme sen hetken päästä.

### `while`-silmukan muoto

`for` on silmukka, jota käytät, kun tiedät, montako kertaa. **`while`** on silmukka, jota käytät, kun tiedät *pysäytysehdon* mutta et tarkkaa toistojen määrää — "kysy, kunnes salasana on tarpeeksi pitkä", "jatka, kun teetä on vielä kupissa". Muoto on jopa yksinkertaisempi kuin `for`:n: pelkkä ehto suluissa ja runko aaltosulkeissa.

#### JavaScript

```js
let count = 0;
while (count < 3) {
  console.log("Hello");
  count = count + 1;
}
```

#### C#

```csharp
int count = 0;
while (count < 3) {
    Console.WriteLine("Hello");
    count = count + 1;
}
```

Molemmat ohjelmat tulostavat:

```text
Hello
Hello
Hello
```

Lue while-silmukka selkeällä suomella: "niin kauan kuin `count` on alle 3, tulosta `Hello`, sitten lisää yksi `count`:iin." Huomaa, että laskuri (`count`), ehto (`count < 3`), runko (`console.log("Hello")`) ja päivitys (`count = count + 1`) ovat kaikki edelleen siellä — ne on vain hajotettu silmukan ympärille sen sijaan, että ne olisi pakattu sulkuihin. `while`-silmukka on `for`-silmukka, jonka neljä osaa on siirretty ympäri luettavuuden vuoksi.

Pieni kompromissi: `while` on joustavampi, mutta sinun on muistettava päivittää laskuri itse rungon sisällä. `for`-silmukka laittaa päivityksen sulkuihin, missä se on vaikea unohtaa. Useimmat tämän viikon ohjelmat ovat onnellisempia `for`-silmukoina; tartu `while`-silmukkaan vain silloin, kun "kunnes" on luonnollisempi kuin "toista N kertaa".

### Kun silmukka pyörii ikuisesti

**Ikuinen silmukka** on silmukka, jonka ehto ei koskaan muutu epätodeksi, joten runko jatkaa pyörimistä eikä ohjelma koskaan pääty. Yleisin syy on päivitysvaiheen unohtaminen.

```js
let count = 0;
while (count < 3) {
  console.log("Hello");
  // puuttuu: count = count + 1;
}
```

```csharp
int count = 0;
while (count < 3) {
    Console.WriteLine("Hello");
    // puuttuu: count = count + 1;
}
```

Selaimen konsolissa näet tulosteen vyöryvän, kunnes sivu jumiutuu; .NET Fiddlessä ajo katkeaa aikakatkaisun vuoksi muutaman sekunnin kuluttua viestillä, kuten *"The process was terminated"*. Kumpikaan ei ole vaarallinen — sulje välilehti, jos tarvitsee — mutta *korjaus* on sama molemmissa kielissä: varmista, että jokin rungon sisällä muuttaa arvoa, jota ehto tarkistaa.

Jos ohjelmasi näyttää jumiutuvan ensimmäisellä ajolla, todennäköisin syy on juuri tämä: silmukka, jonka laskuri ei koskaan päivity.

> **Pysähdy hetkeksi:** Katso yllä olevaa `for`-silmukkaa (laskuri 1:stä 5:een). Mitä tapahtuisi, jos vaihtaisit `i++`:n `i--`:ksi? Ennusta tuloste ajamatta sitä. Sitten jäljitä mielessäsi: muuttuuko ehto `i <= 5` koskaan epätodeksi? Jos ei, millainen bugi tämä on?

---

## Oppitunti 23 — Pseudokoodista pieneen ohjelmaan

Rakennuspäivä. Mitään uutta käsitettä ei tule. Käännät yhden palan omaa viikon 6 pseudokoodiasi rivi riviltä JavaScriptiin tai C#:iin. Ajattelu on tehty; työ on enimmäkseen korvaamista.

### Valitse yksi pala viikon 6 pseudokoodiasi

Avaa viikon 6 muistiinpanosi. Valitse **yksi** pätkä — ikätarkistus, salasanan pituuden tarkistus, pisteet palautteeksi, laskuri, tervehdys. Optimi on **6–20 riviä**. Jos suosikkisi on isompi, valitse *yksi osa* siitä, joka tekee yhden selkeän työn alusta loppuun.

Jos et löydä palaa viikon 6 pseudokoodista (tai hukkasit sivun), valitse yksi näistä varamalleista ja mukauta arvot omaan kontekstiisi:

- **Ikätarkistus.** Aseta ikä; jos se on 18 tai yli, tulosta "allowed"; muuten tulosta "not allowed".
- **Salasanan pituuden tarkistus.** Aseta salasana; jos se on 8 merkkiä tai enemmän, tulosta "strong enough"; muuten tulosta "too short".
- **Pisteet palautteeksi.** Aseta pisteet; jos se on 80 tai yli, tulosta "great work"; jos 50 tai yli, tulosta "you passed"; muuten tulosta "try again".
- **Yksinkertainen laskuri.** Tulosta numerot 1–5 käyttäen `for`-silmukkaa.
- **Tervehdys nimellä.** Aseta nimi; käytä `for`-silmukkaa tulostamaan "Hello, NAME" kolme kertaa.

### Käännöstaulukko

Useimmilla pseudokoodiriveillä on yksi selkeä muoto JavaScriptissä ja C#:ssa. Tämän pienen taulukon ulkoaopettelu tekee oppitunnista 23 lähes mekaanisen.

| Pseudokoodikuvio                | JavaScript                                    | C#                                                |
|---------------------------------|-----------------------------------------------|---------------------------------------------------|
| `WRITE "Hello"`                 | `console.log("Hello");`                       | `Console.WriteLine("Hello");`                     |
| `SET x TO 5`                    | `let x = 5;`                                  | `int x = 5;`                                      |
| `SET name TO "Aino"`            | `let name = "Aino";`                          | `string name = "Aino";`                           |
| `IF x >= 18 THEN … ELSE …`      | `if (x >= 18) { … } else { … }`               | `if (x >= 18) { … } else { … }`                   |
| `REPEAT N TIMES`                | `for (let i = 0; i < N; i++) { … }`           | `for (int i = 0; i < N; i++) { … }`               |
| `WHILE x < 3 DO …`              | `while (x < 3) { … }`                         | `while (x < 3) { … }`                             |
| `INCREASE x BY 1`               | `x = x + 1;`  *(tai `x++;`)*                  | `x = x + 1;`  *(tai `x++;`)*                      |
| `IF x EQUALS 5 THEN …`          | `if (x === 5) { … }`  *(tai `==`)*            | `if (x == 5) { … }`                               |

Tämä riittää kaiken viikolla 6 kirjoittamasi kääntämiseen. Rakenne oli jo paikoillaan; taulukko antaa vain oikeat pintasanat tietylle kielelle.

### Kaksi esimerkkiä työn ääressä — rinnakkain

**Ikätarkistus.** *Viikon 6 pseudokoodi: aseta ikä arvoon 17; jos ikä on 18 tai enemmän, tulosta "allowed", muuten tulosta "not allowed".*

#### JavaScript

```js
let age = 17;
if (age >= 18) {
  console.log("allowed");
} else {
  console.log("not allowed");
}
```

#### C#

```csharp
int age = 17;
if (age >= 18) {
    Console.WriteLine("allowed");
} else {
    Console.WriteLine("not allowed");
}
```

Molemmat tulostavat `not allowed`. Vaihda `17` arvoon `19`, ja molemmat tulostavat `allowed`. Pätkät ovat rivi-rivi-vastaavia.

**Tervehdys nimellä (silmukka plus muuttuja).** *Viikon 6 pseudokoodi: toista 3 kertaa: tulosta "Hello, name".*

#### C#

```csharp
string name = "Aino";
for (int i = 0; i < 3; i++) {
    Console.WriteLine("Hello, " + name);
}
```

#### JavaScript

```js
let name = "Aino";
for (let i = 0; i < 3; i++) {
  console.log("Hello, " + name);
}
```

Molemmat tulostavat `Hello, Aino` kolme kertaa. `+` tekstin ja muuttujan välillä toimii samalla tavalla molemmissa kielissä — sana sille, mitä `+` tekee tässä, on **konkatenaatio**, palojen liimaaminen yhdeksi tekstipalaksi.

Yleinen yhden merkin ansa, joka kannattaa huomata nyt (ennen oppitunnin 24 virheen lukemista): merkkijonon **pituus** kirjoitetaan `name.length` (pieni l) JavaScriptissä ja `name.Length` (iso L) C#:ssa. Niiden sekoittaminen on juuri se kirjoitusvirhe, joka tuottaa huomenna lukemiasi virheilmoituksia.

### Tallenna, aja, näe tuloste

**JavaScript — selaimen konsolissa:** avaa mikä tahansa verkkosivu; paina `Cmd + Opt + J` (Mac) tai `Ctrl + Shift + J` (Win/Linux); liitä koodisi, paina Enter, lue tuloste. Tallenna sama koodi tavallisena tekstitiedostona `.js`-päätteellä — se on **lähdekoodisi** AT3:lle.

**C# — online-.NET-ajurissa:** avaa `dotnetfiddle.net`; valitse ylhäältä **Console**; liitä koodisi `Main`-metodiin; paina **Run**, lue tuloste. Tallenna sama koodi tavallisena tekstitiedostona `.cs`-päätteellä — se on lähdekoodisi AT3:lle.

Ota **kuvakaappaus** ajosta tulosteen näkyessä. Tämä kuvakaappaus on yksi AT3:n tuotoksista.

> **Pysähdy hetkeksi:** Katso juuri kirjoittamaasi ohjelmaa (tai ohjelmaa, jota olet kirjoittamassa). Lue se kerran, rivi riviltä, *ääneen*, selkeällä suomella. Jos osaat kertoa, mitä kukin rivi tekee katsomatta taulukkoa, olet valmis esittämään sen 2 minuutissa oppitunnilla 24. Jos kompastut riviin, se on rivi, joka kannattaa lukea uudelleen ennen esitystä.

### Kun ruutu on tyhjä tai hiljainen

Jos ajat ohjelmasi eikä mitään tapahdu, tarkista tylsät syyt ensin:

- **Painoitko oikeasti Run / Enter?** Yleisin syy.
- **Liitititkö vain osan ohjelmasta?** Erityisesti .NET Fiddlessä koodisi on oltava `Main`-metodin sisällä.
- **Onko tulostusrivillä kirjoitusvirhe?** `console.Log` (iso L) on JavaScriptin virhe; C#:ssa `Console.Writeline` (pieni `l`) ei myöskään ole olemassa — sen on oltava `Console.WriteLine`.
- **Pysähtyikö ohjelma aiemmin virheeseen?** Vieritä ylöspäin. Punainen viesti tyhjän tilan yläpuolella *on* ongelma — oppitunti 24 opettaa lukemaan näitä.

Jos mikään näistä ei ole syy, lisää `console.log("got here");` (tai `Console.WriteLine("got here");`) lähelle alkua. Jos "got here" tulostuu, ohjelma pyörii; puuttuva tuloste on jossain alempana.

> **Pysähdy hetkeksi:** Vertaa käännettyä ohjelmaasi alkuperäiseen viikon 6 pseudokoodiin. Aseta ne vierekkäin. Ympyröi niiden rivien osat, jotka ovat kirjaimellisesti samoja — muuttujanimet, numerot, avainsanat kuten `if`. Ympyröiden määrä yllättää sinut. Loput palat ovat syntaksia; ympyrät ovat sitä ajattelua, johon kurssi on kouluttanut sinua viikolta 1 lähtien.

---

## Oppitunti 24 — Testaa, korjaa yksi bugi, esitä

Kolme asiaa laskeutuu tähän, ja kaikki riippuvat ohjelmasta, joka pyörii. **Testaa** kahdella alkuarvolla. **Lue** yksi oikea virheilmoitus ja **korjaa** yksi rivi. **Esitä** koko tarina 2 minuutissa.

### Käsin testaaminen

"Testaaminen" tällä viikolla tarkoittaa yhtä tiettyä asiaa: **aja ohjelma ainakin kahdella eri alkuarvolla ja tarkista, että tuloste on järkeenkäypä joka kerta.** Ei automaattista testaustyökalua, ei testikehystä, ei erikoissanastoa. Pelkkä yhden numeron tai merkkijonon vaihtaminen alussa ja Run-napin painaminen.

Yllä olevassa ikätarkistusohjelmassa kaksi arvoa voivat olla `age = 17` ja `age = 19`. Ensimmäisen pitäisi tulostaa `not allowed`; toisen `allowed`. Jos molemmat ajot vastaavat sitä, mitä ennustit, ohjelma läpäisee käsitestisi. Jos toinen tulostaa väärän viestin, olet juuri löytänyt bugin.

#### JavaScript — vaihda yksi rivi ajojen välissä

```js
let age = 17;   // aja ensin arvolla 17, vaihda sitten arvoon 19 ja aja uudelleen
```

#### C# — vaihda yksi rivi ajojen välissä

```csharp
int age = 17;   // aja ensin arvolla 17, vaihda sitten arvoon 19 ja aja uudelleen
```

AT3:ta varten ajat oman ohjelmasi kahdella eri arvolla ja kaappaat molemmat tulosteet (yksi kuvakaappaus, jossa molemmat ajot näkyvät, käy; kaksi kuvakaappaustakin käy).

### Oikean virheilmoituksen lukeminen

Kun tietokone ei ole tyytyväinen, se tulostaa **virheilmoituksen**. Se näyttää pelottavalta ensimmäisellä kerralla — pitkä, tekninen — mutta tämän viikon yksinkertaisille bugeille viesti osoittaa lähes aina suoraan riviin, joka kaipaa muutosta.

Yleinen JavaScript-virhe:

```text
Uncaught ReferenceError: scre is not defined
    at <anonymous>:3:15
```

Ja sen C#-serkku:

```text
error CS0103: The name 'scre' does not exist in the current context
```

Molemmat viestit sanovat saman asian: *En tiedä, mikä `scre` on.* Syy on lähes aina kirjoitusvirhe — jossain ylempänä ohjelmassasi määrittelit `score`-muuttujan ja jossain myöhemmin kirjoitit `scre` (puuttuva `o`). Korjaus: etsi `scre`, kirjoita puuttuva `o`, aja uudelleen.

Tämä on **virheenkorjaus tämän kurssin tasolla**: lue, mitä tietokone kertoi, etsi rivi, josta se puhui, muuta yksi pieni asia, aja uudelleen.

Kaksi muuta virhemuotoa, joita saatat kohdata. **JavaScript** `=`:llä `===`:n sijaan ei yleensä näytä virheilmoitusta vaan hiljaisen väärän vastauksen — havaitset sen *testaamalla kahdella arvolla* ja huomaamalla, että toinen on väärin. **C#** puuttuvalla puolipisteellä tulostaa `error CS1002: ; expected` ja kertoo rivinumeron. Lisää `;` kyseisen rivin loppuun, tallenna, aja uudelleen.

> **Pysähdy hetkeksi:** Valitse yksi ohjelma, jonka kirjoitit oppitunnilla 23. Logiikkaa muuttamatta kirjoita tarkoituksella muuttujan nimi väärin jossain ohjelman keskellä. Aja se. Lue virheilmoitus. Ennusta, ennen kuin korjaat sen, täsmälleen mihin sanaan ohjelmassasi viesti osoittaa. Sitten korjaa se ja aja uudelleen. Ensimmäisellä kerralla, kun teet tämän, virheilmoitusten mystisyys katoaa.

### Yksi pieni korjaus, yksi uusi ajo

"Virheenkorjaus" tällä kurssilla on **konsolin virheilmoituksen lukemista ja yhden pienen korjauksen soveltamista**. Se ei ole debuggerityökalu eikä pysäytä-ohjelma-rivi-riviltä -työkalu. Mitään erikoisohjelmistoa ei tarvitse asentaa. Mitään testauskehystä ei tarvitse opetella. Koko silmukka on:

1. Aja ohjelma.
2. Näe virheilmoitus *tai* odottamaton tuloste.
3. Lue viesti (tai vertaa odotettua ja todellista tulostetta rivi riviltä).
4. Etsi vastuussa oleva rivi.
5. Muuta yksi pieni asia.
6. Aja ohjelma uudelleen.

AT3:ta varten sinun on tehtävä tämä vähintään kerran. Bugi voi olla kirjoitusvirhe, puuttuva puolipiste (C#), `=` `==`:n sijaan, puuttuva `}` — mikä tahansa käy. Jos ohjelmasi pyöri ensimmäisellä yrityksellä, **laukaise** bugi tarkoituksella: riko yksi asia, lue viesti, korjaa se takaisin.

### 2 minuutin esityksesi

Oppitunnilla 24 pidät **2 minuutin** suullisen esityksen ohjelmastasi luokalle. Kaksi minuuttia on lyhyt — noin 200 puhuttua sanaa. Esityksellä on **neljä kohtaa**, noin 30 sekuntia kukin:

1. **Mitä ohjelma tekee.** Lause tai kaksi selkeällä suomella. *"Ohjelmani ottaa salasanan ja tulostaa joko 'strong enough' tai 'too short' sen pituudesta riippuen."*
2. **Miten se tekee sen.** Käy rakenne läpi. *"Ylhäällä asetan muuttujan nimeltä `password`. Sitten on `if/else`: jos salasanan pituus on 8 tai enemmän, se tulostaa 'strong enough', muuten 'too short'."* Jos ohjelmassasi on silmukka, nimeä neljä osaa (laskuri, ehto, runko, päivitys).
3. **Mikä meni vikaan.** Nimeä se yksi bugi, jonka löysit. *"Ensimmäisellä ajolla olin kirjoittanut `password.length` pienellä l:llä, mutta koodini oli C#, jossa sen pitää olla iso L, joten sain CS0103-virheen."*
4. **Miten korjasit sen.** Yksi lause. *"Vaihdoin pienen l:n isoksi L:ksi tuolla yhdellä rivillä ja ajoin ohjelman uudelleen."*

Siinä on 2 minuuttiasi. Ei kalvoja, ei sanasta sanaan luettavaa käsikirjoitusta, ei tarvetta tyylikkääseen koodiin. **Seisot oman ohjelmasi vieressä** ja selität sen omin sanoin.

Käytännön vinkki: harjoittele kerran kotona puhelimen ajastimella. Jos lopetat 45 sekunnissa, jätät yhden kohdan ohi. Jos menet yli 2 minuutin, luet luultavasti koodia rivi riviltä — leikkaa se ja puhu siitä, mitä ohjelma *tekee*.

> **Pysähdy hetkeksi:** Avaa ohjelmasi näytölle nyt. Kokeile neljää kohtaa ääneen, ajastimen kanssa, jos sinulla on sellainen. Ensimmäinen kerta on luultavasti joko liian lyhyt tai liian pitkä. Toinen kerta on lähes aina lähempänä. Esitys ei ole ulkoa muistamisen testi — se on testi siitä, pystytkö seisomaan oman työsi takana.

### Luokkakaverin kanssa vertailu

Jos sinulla on aikaa O24:llä (esitysten jälkeen), etsi luokkakaveri, joka käytti **toista** kieltä. Lukekaa toistenne ohjelmat. Kirjoita 3–5 lausetta selkeällä suomella eroista — puolipisteet kaikkialla C#:ssa vs. valinnaiset JS:ssä, `Console.WriteLine` vs. `console.log`, `int` / `string` vs. `let`, isot alkukirjaimet C#:n metodien nimissä — ja yhdestä asiasta, joka on sama: silmukka ja `if/else` näyttävät lähes identtisiltä molemmilla puolilla. Tuo viimeinen huomio on koko pointti siitä, että näit molemmat.

---

## Miten AT3 arvioidaan

AT3 on **hyväksytty / ei-vielä-hyväksytty**. Ei numeroarvosanaa, ei muuta matriisia kuin lyhyt tarkistuslista.

**Palautat:**

- **Lähdekoodin** (`.js`- tai `.cs`-tiedoston tai selvästi aidatun pätkän oikealla kielitunnisteella).
- **Kuvakaappauksen** ohjelman ajosta vähintään yhdellä odotetulla tulosteella.
- **3–5 lauseen kirjallisen reflektion**, jossa nimeät sen yhden bugin, jonka löysit, ja sen yhden korjauksen, jonka teit.
- **2 minuutin suullisen esityksen** luokassa oppitunnilla 24 kattaen yllä olevat neljä kohtaa.

**Opettaja tarkistaa neljä asiaa:**

- Ohjelma pyörii (tai epäonnistunut yrityksesi on dokumentoitu virheilmoituksineen).
- Osaat nimetä selkeällä suomella, mitä ohjelma tekee.
- Yksi bugi-ja-korjaus-pari on dokumentoitu.
- 2 minuutin esitys on pidetty.

Jos jokin neljästä puuttuu, työ on **ei-vielä-hyväksytty** ja opettaja kertoo sinulle, mikä korjata. Ei-vielä-hyväksytty ei ole häpeä; se tarkoittaa vain, että on yksi pieni asia vielä tehtävänä.

---

## Yhteenveto — silmukan sulkeminen keskeisessä kysymyksessä

Kahdeksan viikkoa sitten tämä kurssi avautui yhdellä kysymyksellä. Olet vastannut siihen, paloissa, joka viikko siitä lähtien. Nyt osaat vastata siihen kokonaan, omin sanoin, toimivan ohjelman kanssa kädessäsi. Tässä se on vielä kerran — samalla sanamuodolla, joka sillä on ollut viikolta 1 lähtien:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

Vastaat siihen tällä viikolla tekemällä sen. Otat itse viikolla 6 kirjoittamasi pseudokoodin ja käännät sen JavaScriptiksi tai C#:ksi. Esittelet muuttujan. Kirjoitat `if/else`:n. Kirjoitat `for`-silmukan. Painat Run-nappia. Jos tietokone ei ole tyytyväinen, se tulostaa virheilmoituksen, joka osoittaa sen yhden rivin, jonka teit väärin, ja korjaat sen yhden rivin. Sitten seisot luokan edessä ja sanot, 2 minuutissa, mitä ohjelmasi tekee ja miten korjasit asian, joka meni vikaan.

Tämä on ohjelmointia, tällä tasolla. Ei taikuutta. Ei mysteeriä. Pieni, huolellinen ohjetiedosto, joka tekee täsmälleen sen, mitä sanoit. Kaikki, mitä loput koulutuksestasi lisää — useampia kieliä, isompia projekteja, kirjastoja, kehyksiä, tiimityötä — istuu tämän saman yhden asian päällä: sananmukainen tietokone, joka noudattaa sinun kirjoittamiasi ohjeita, kertoen sinulle selvänä tekstinä, kun jokin ei jäsenny.

Ohjelmointi on lakannut olemasta mystinen asia. Säilytä AT3-lähdetiedostosi. Avaa se uudelleen puolen vuoden kuluttua. Se näyttää pieneltä. Se on pointti — sinä kirjoitit sen.

Tervetuloa keskeisen kysymyksen toiselle puolelle.
