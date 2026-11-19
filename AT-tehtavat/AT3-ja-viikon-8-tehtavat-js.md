# Viikko 8 — Opiskelijatehtävät (JavaScript)

## Viikon tehtävien yleiskuva

Tällä viikolla on kaksi 🟢 PAKOLLISTA ja kolme 🟣 SYVENTÄVÄÄ JavaScript-tehtävää.
Pakolliset tehtävät ovat vähimmäissuoritus — tee molemmat, jotta läpäiset AT3:n. Syventävät
tehtävät ovat valinnaisia; valitse yksi tai kaksi, jos sinulla on aikaa.
AT3 on tämän viikon keskeinen palautettava työ. Tehtävä 8.1-JS on AT3-ohje. Palautat
lähdekoodin, kuvakaappauksen ja lyhyen pohdinnan oppitunnin L23 lopussa ja pidät 2
minuutin suullisen esityksen oppitunnilla L24. Tehtävä 8.2-JS on pieni silmukkalämmittely
ennen kuin käännät oman pseudokoodisi.
JS toimii selaimesi DevTools-konsolissa ( Macilla, `Cmd + Opt + J Ctrl + Shift + J`
Windowsissa/Linuxissa). “Testaaminen” tarkoittaa ohjelman ajamista kahdella eri arvolla.
“Debuggaaminen” tarkoittaa konsolin virheilmoituksen lukemista ja yhden rivin muuttamista.
🟢

## 🟢 PAKOLLINEN — Tehtävä 8.1-JS — AT3-ohje: käännä viikon 6 pseudokoodisi JavaScriptiksi

Tavoite. Käännä yksi pala omaa viikon 6 pseudokoodiasi pieneksi toimivaksi JavaScript-
ohjelmaksi (noin 10–25 riviä), aja se selaimen konsolissa kahdella eri lähtöarvolla, etsi ja korjaa
yksi bugi sekä valmistele 2 minuutin suullinen esitys. Tämä on AT3.
Tämä on viikon 8 vähimmäissuoritus. Ilman tätä tehtävää AT3:a ei ole.

### Vaiheet

1. Valitse yksi viikon 6 pseudokoodisi (6–20 riviä). Jos et löydä sellaista, käytä
varamallia ja muokkaa arvot: ikärajan tarkistus; salasanan pituustarkistus; pisteistä
palautteeksi; yksinkertainen laskuri (1–5); tervehdys nimellä kolme kertaa.
2. Käännä se rivi riviltä JavaScriptiksi käyttäen -tiedoston `self-study.md`
käännöstaulukkoa. Käytä kovakoodattuja muuttuja-arvoja ohjelman alussa (ei tarvita
-komentoa). Esimerkki:

```javascript
prompt()
let salasana = "hei";
if (salasana.length >= 8) {
console.log("riittävän vahva");
} else {
console.log("liian lyhyt");
}
```

3. Avaa selaimen DevTools-konsoli, liitä ohjelma, paina Enter ja lue tuloste.
4. Aja se kahdella eri lähtöarvolla. Muuta yhtä muuttujaa ohjelman alussa ja aja
kumpikin versio. Ota kuvakaappaus, jossa näkyvät molemmat tulosteet.
5. Etsi ja korjaa yksi bugi. Jos ohjelmasi toimi ensimmäisellä yrityksellä, aiheuta bugi
tahallaan: kirjoita yhden muuttujan nimi väärin tai poista yksi . Aja ohjelma, lue `;`
virheilmoitus ja korjaa takaisin. Nimeä bugi tavallisella kielellä (“Kirjoitin enkä `salasna`
”). `salasana`
6. Tallenna lähdekoodi nimellä tai liitä se palautusmuistiinpanoihin koodilohkona, `at3.js`
jonka kielimerkintä on . `js`
7. Kirjoita 3–5 virkkeen pohdinta, jossa nimeät, mitä ohjelma tekee, minkä bugin löysit
ja minkä korjauksen teit.
8. Valmistele 2 minuutin suullinen esitys oppitunnille L24. Neljä osaa, noin 30 sekuntia
kukin: mitä ohjelma tekee → miten se toimii (muuttujat, , silmukka?) → mikä `if/else`
meni pieleen → miten korjasit sen. Harjoittele puhelimen ajastimella.

### Jos teet tämän yksin

L24-esitys olettaa yleisön. Jos et voi esittää livenä — esimerkiksi sairauden tai hybridiopiskelun
vuoksi — tallenna 2 minuutin video, jossa esittelet ohjelman kameralle, tai lähetä ohjelma ja 3
virkkeen tiivistelmä luokan chattiin. Neljä osaa ovat samat.

### Säilytä muistiinpanosi

Tämä on AT3. Tuo L24:ään neljä tuotosta: lähdekooditiedosto ( ), kuvakaappaus kahdesta `at3.js`
ajosta, 3–5 virkkeen pohdinta, jossa nimeät bugin ja korjauksen, sekä valmius pitää 2 minuutin
suullinen esitys.
AT3 palautetaan L23:n lopussa ja esitetään L24:ssä. Hyväksytty / ei vielä hyväksytty
neljällä tarkistuksella: ohjelma toimii (tai epäonnistunut yrityksesi on dokumentoitu), osaat
nimetä mitä se tekee, yksi bugi–korjaus-pari on kuvattu ja 2 minuutin esitys on pidetty.

## 🟢 PAKOLLINEN — Tehtävä 8.2-JS — Silmukkalämmittely: laske 1:stä 5:een JavaScriptissä

Tavoite. Kirjoita kolme lyhyttä -silmukkaa JavaScriptissä — laske ylöspäin, laske alaspäin, `for`
tervehdi nimellä — jotta silmukkamalli tuntuu käsissä ennen AT3:a.

### Tämä on osa viikon 8 vähimmäissuoritusta.

### Vaiheet

1. Avaa selaimen konsoli. Liitä ja aja:

```javascript
for (let i = 1; i <= 5; i++) {
console.log(i);
}
```

Odotettu tuloste: 1, 2, 3, 4, 5 — yksi per rivi.
2. Muokkaa sitä tulostamaan 5:stä 1:een. Vaihda muotoon , muotoon

```
i = 1 i = 5 i <= 5 i
```

ja muotoon . Aja ohjelma.

```
>= 1 i++ i--
```

3. Muokkaa sitä tulostamaan “Hei, NIMI” kolme kertaa. Korvaa lainausmerkkien
sisällä oleva nimi omalla nimelläsi:

```javascript
for (let i = 0; i < 3; i++) {
console.log("Hei, <nimesi>");
}
```

4. Tallenna kaikki kolme koodinpätkää yhteen tiedostoon ( ) ja `loop-warmup.js`
kirjoita jokaisen yläpuolelle yhden rivin kommentti.

### Säilytä muistiinpanosi

Nämä kolme mallia ovat täsmälleen niitä silmukkamuotoja, joita saatat tarvita AT3-
ohjelmassasi. Pidä samassa kansiossa AT3-tiedostojesi kanssa. `loop-warmup.js`

## 🟣 SYVENTÄVÄ — Tehtävä 8.3-JS — Yhdistä silmukka ja if/else JavaScriptissä

Tavoite. Kirjoita pieni JS-ohjelma, joka käy läpi 5 salasanan listan ja tulostaa jokaiselle
“riittävän pitkä” tai “liian lyhyt”.

### Vaiheet

1. Liitä selaimen konsoliin ja aja:

```javascript
let salasanat = ["hei", "oikeahevonen", "12345", "patteri", "pitkasalasana"];
for (let i = 0; i < salasanat.length; i++) {
if (salasanat[i].length >= 8) {
console.log("riittävän pitkä");
} else {
console.log("liian lyhyt");
}
}
```

2. Ennusta tuloste ennen Enterin painamista. Viisi riviä, yksi per salasana.
3. Vertaa ennustetta todellisuuteen. Jos jokin rivi yllätti, etsi salasana, josta se tuli, ja
selitä miksi.
4. Kirjoita 3 virkkeen pohdinta siitä, mitä ohjelma tekee ja mitä lisäisit siihen
seuraavaksi.

### Säilytä muistiinpanosi

Jos AT3-ohjelmassasi on ja saat sen valmiiksi aikaisin, liitä tämä koodinpätkä `if/else`
luonnollisena laajennuksena. Säilytä se AT3-kansiossa.
🟣

## SYVENTÄVÄ — Tehtävä 8.4-JS — Lue oikea virheilmoitus ja korjaa se (JS)

Tavoite. Lue kolme oikeaa JavaScript-virheilmoitusta ja tee jokaiseen yksi pieni korjaus, jotta
ensimmäinen yllättävä virhe AT3:ssa ei pysäytä sinua.

### Vaiheet

1. Liitä jokainen alla oleva koodinpätkä selaimen konsoliin yksi kerrallaan.
Jokaisessa on täsmälleen yksi virhe.

```javascript
// Pätkä A
let pisteet = 75;
if (pisteeet >= 50) {
console.log("läpäisit");
}
// Pätkä B
let ika = 17;
if (ika = 18) {
console.log("täysi-ikäinen");
}
// Pätkä C
for (let i = 0; i < 3; i++) {
console.log("Hei");
```

2. Kopioi jokaisesta pätkästä tarkka virheilmoitus. Pätkä B tulostaa odottamattoman
tuloksen — se on hiljainen bugi, ei virheilmoitus. Nimeä rivi ja korjaus tavallisella
kielellä. Tee korjaus ja aja uudelleen.
3. Valinnainen LLM-sparrausvaihe. Liitä yksi virheilmoitus ja koodinpätkä LLM:ään
tällä kehotteella:

```
Selitä, mitä tämä JavaScript-virhe tarkoittaa, mutta älä kerro,
miten se korjataan. Haluan löytää korjauksen itse.
<liitä virheilmoitus + koodinpätkä tähän>
```

Jos LLM antaa korjauksen silti, hylkää vastaus ja kirjoita korjaus omin sanoin. Älä liitä LLM:n
tuotosta sellaisenaan muistiinpanoihisi.

### Säilytä muistiinpanosi

Pieni kirjasto JS-virheistä, jonka kirjoitat ylös nyt, nopeuttaa L24-hetkeä AT3:ssa, kun sinun
täytyy lukea oikea virheilmoitus ja tehdä yksi pieni korjaus.

## 🟣 SYVENTÄVÄ — Tehtävä 8.5-JS — Vertaa C#-luokkakaverin kanssa

Tavoite. Lue luokkakaverin C#-ohjelma ja kirjoita 3–5 virkettä eroista sekä yksi asia, joka on
sama.

### Vaiheet

1. Etsi luokkakaveri, joka käytti AT3:ssa C#:a. Näyttäkää toisillenne ohjelmanne.
2. Lue hänen ohjelmansa rivi riviltä. Tunnista jokaisen C#-rivin JS-vastine.
3. Kirjoita 3–5 virkettä eroista (puolipisteet, vs , / `Console.WriteLine console.log int`
vs , C#:n isolla alkavat metodinimet) ja yksi asia, joka on sama `string let`
(silmukkarakenne, , tavoite). `if/else`

### Jos teet tämän yksin

Jos C#-luokkakaveria ei ole saatavilla, lue -tiedoston yhden esimerkin C#-versio `self-study.md`
(ohjelmat A–E) ja kirjoita samat 3–5 virkettä vertaamalla sitä saman sivun JS-versioon.

### Säilytä muistiinpanosi

Liitä 3–5 virkettä AT3-kansioosi. Ne eivät ole osa hyväksymistarkistusta, mutta ne terävöittävät
L24-esitystä: opiskelija, joka osaa nimetä yhden asian toisesta kielestä, ymmärtää paremmin
myös oman valintansa.
