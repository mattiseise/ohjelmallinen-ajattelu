# Viikko 8 — Opiskelijatehtävät (C#)

## Viikon tehtävien yleiskuva

Tällä viikolla on kaksi 🟢 PAKOLLISTA ja kolme 🟣 SYVENTÄVÄÄ C#-tehtävää. Pakolliset
tehtävät ovat vähimmäissuoritus — tee molemmat, jotta läpäiset AT3:n. Syventävät tehtävät
ovat valinnaisia; valitse yksi tai kaksi, jos sinulla on aikaa.
AT3 on tämän viikon keskeinen palautettava työ. Tehtävä 8.1-CS on AT3-ohje. Palautat
lähdekoodin, kuvakaappauksen ja lyhyen pohdinnan oppitunnin L23 lopussa ja pidät 2
minuutin suullisen esityksen oppitunnilla L24. Tehtävä 8.2-CS on pieni silmukkalämmittely
ennen kuin käännät oman pseudokoodisi.
C# toimii .NET Fiddlessä ( ); asennusta ei tarvita. “Testaaminen” tarkoittaa `dotnetfiddle.net`
ohjelman ajamista kahdella eri arvolla. “Debuggaaminen” tarkoittaa kääntäjän
virheilmoituksen lukemista ja yhden rivin muuttamista.
Muistutus: AT3 ei vaadi suurta ohjelmaa. Hyvä pieni ohjelma, jonka ymmärrät ja osaat selittää,
on parempi kuin suuri ohjelma, jota et pysty puolustamaan.
🟢

## 🟢 PAKOLLINEN — Tehtävä 8.1-CS — AT3-ohje: käännä viikon 6 pseudokoodisi C#:ksi

Tavoite. Käännä yksi pala omaa viikon 6 pseudokoodiasi pieneksi toimivaksi C#-ohjelmaksi
(noin 10–25 riviä), aja se .NET Fiddlessä kahdella eri lähtöarvolla, etsi ja korjaa yksi bugi sekä
valmistele 2 minuutin suullinen esitys. Tämä on AT3.
Tämä on viikon 8 vähimmäissuoritus. Ilman tätä tehtävää AT3:a ei ole.

### Vaiheet

1. Valitse yksi viikon 6 pseudokoodisi (6–20 riviä). Jos et löydä sellaista, käytä
varamallia ja muokkaa arvot: ikärajan tarkistus; salasanan pituustarkistus; pisteistä
palautteeksi; yksinkertainen laskuri (1–5); tervehdys nimellä kolme kertaa.
2. Käännä se rivi riviltä C#:ksi käyttäen -tiedoston käännöstaulukkoa. `self-study.md`
Käytä kovakoodattuja muuttuja-arvoja ohjelman alussa (ei tarvita -

```
Console.ReadLine()
```

komentoa). Esimerkki:

```csharp
string salasana = "hei";
if (salasana.Length >= 8) {
Console.WriteLine("riittävän vahva");
} else {
Console.WriteLine("liian lyhyt");
}
```

3. Avaa .NET Fiddle, valitse Console, liitä koodi -metodiin ja paina Run. `Main`
4. Aja se kahdella eri lähtöarvolla. Muuta yhtä muuttujaa ohjelman alussa ja aja
kumpikin versio. Ota kuvakaappaus, jossa näkyvät molemmat tulosteet.
5. Etsi ja korjaa yksi bugi. Jos ohjelmasi toimi ensimmäisellä yrityksellä, aiheuta bugi
tahallaan: kirjoita yhden muuttujan nimi väärin tai poista yksi . Paina Run, lue `;`
kääntäjän tai ajonaikainen ilmoitus ja korjaa se takaisin. Nimeä bugi tavallisella kielellä
(“Kirjoitin enkä ; kääntäjä sanoi CS0103”). `salasna salasana`
6. Tallenna lähdekoodi nimellä tai liitä se palautusmuistiinpanoihin `at3.cs`
koodilohkona, jonka kielimerkintä on . `csharp`
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

Tämä on AT3. Tuo L24:ään neljä tuotosta: lähdekooditiedosto ( ), kuvakaappaus kahdesta `at3.cs`
ajosta, 3–5 virkkeen pohdinta, jossa nimeät bugin ja korjauksen, sekä valmius pitää 2 minuutin
suullinen esitys.
AT3 palautetaan L23:n lopussa ja esitetään L24:ssä. Hyväksytty / ei vielä hyväksytty
neljällä tarkistuksella: ohjelma toimii (tai epäonnistunut yrityksesi on dokumentoitu), osaat
nimetä mitä se tekee, yksi bugi–korjaus-pari on kuvattu ja 2 minuutin esitys on pidetty.

## 🟢 PAKOLLINEN — Tehtävä 8.2-CS — Silmukkalämmittely: laske 1:stä 5:een C#:ssa

Tavoite. Kirjoita kolme lyhyttä -silmukkaa C#:ssa, jotta silmukkamalli tuntuu käsissä ennen `for`
AT3:a.

### Tämä on osa viikon 8 vähimmäissuoritusta.

### Vaiheet

1. Avaa .NET Fiddle, valitse Console, liitä -metodiin ja paina Run:

```csharp
Main
for (int i = 1; i <= 5; i++) {
Console.WriteLine(i);
}
```

Odotettu tuloste: 1, 2, 3, 4, 5 — yksi per rivi.
2. Muokkaa sitä tulostamaan 5:stä 1:een. Vaihda muotoon , muotoon

```
i = 1 i = 5 i <= 5 i
```

ja muotoon . Paina Run.

```
>= 1 i++ i--
```

3. Muokkaa sitä tulostamaan “Hei, NIMI” kolme kertaa. Korvaa lainausmerkkien
sisällä oleva nimi omalla nimelläsi:

```csharp
for (int i = 0; i < 3; i++) {
Console.WriteLine("Hei, <nimesi>");
}
```

4. Tallenna kaikki kolme koodinpätkää yhteen tiedostoon ( ) ja `loop-warmup.cs`
kirjoita jokaisen yläpuolelle yhden rivin kommentti.

### Säilytä muistiinpanosi

Nämä kolme mallia ovat täsmälleen niitä silmukkamuotoja, joita saatat tarvita AT3-
ohjelmassasi. Pidä samassa kansiossa AT3-tiedostojesi kanssa. `loop-warmup.cs`

## 🟣 SYVENTÄVÄ — Tehtävä 8.3-CS — Yhdistä silmukka ja if/else C#:ssa

Tavoite. Kirjoita pieni C#-ohjelma, joka käy läpi 5 salasanan listan ja tulostaa jokaiselle
“riittävän pitkä” tai “liian lyhyt”.
Huomio taulukosta. on merkkijonojen lista. hakee siitä ensimmäisen `string[] salasanat[0]`
arvon; kertoo arvojen määrän. `salasanat.Length`

### Vaiheet

1. Liitä .NET Fiddlessä -metodin sisään ja aja:

```csharp
Main
string[] salasanat = { "hei", "oikeahevonen", "12345", "patteri", "pitkasalasana" };
for (int i = 0; i < salasanat.Length; i++) {
if (salasanat[i].Length >= 8) {
Console.WriteLine("riittävän pitkä");
} else {
Console.WriteLine("liian lyhyt");
}
}
```

2. Ennusta tuloste ennen Run-painikkeen painamista. Viisi riviä, yksi per salasana.
3. Vertaa ennustetta todellisuuteen. Jos jokin rivi yllätti, etsi salasana, josta se tuli, ja
selitä miksi.
4. Kirjoita 3 virkkeen pohdinta siitä, mitä ohjelma tekee ja mitä lisäisit siihen
seuraavaksi.

### Säilytä muistiinpanosi

Jos AT3-ohjelmassasi on ja saat sen valmiiksi aikaisin, liitä tämä koodinpätkä `if/else`
laajennuksena. Säilytä se AT3-kansiossa.

## 🟣 SYVENTÄVÄ — Tehtävä 8.4-CS — Lue oikea virheilmoitus ja korjaa se (C#)

Tavoite. Lue kolme oikeaa C#-kääntäjän tai ajonaikaista ilmoitusta ja tee jokaiseen yksi pieni
korjaus, jotta ensimmäinen yllättävä virhe AT3:ssa ei pysäytä sinua.

### Vaiheet

1. Liitä jokainen alla oleva koodinpätkä .NET Fiddlen -metodiin yksi `Main`
kerrallaan. Jokaisessa on täsmälleen yksi virhe.

```csharp
// Pätkä A
int pisteet = 75;
if (pisteeet >= 50) {
Console.WriteLine("läpäisit");
}
// Pätkä B
int ika = 17
if (ika >= 18) {
Console.WriteLine("täysi-ikäinen");
}
// Pätkä C
for (int i = 0; i < 3; i++) {
Console.WriteLine("Hei");
```

2. Kopioi jokaisesta pätkästä tarkka kääntäjän ilmoitus (se alkaa muodolla ). `error CS…`
Nimeä rivi ja korjaus tavallisella kielellä. Tee korjaus ja aja uudelleen.
3. Valinnainen LLM-sparrausvaihe. Liitä yksi virheilmoitus ja koodinpätkä LLM:ään
tällä kehotteella:

```
Selitä, mitä tämä C#-kääntäjän virhe tarkoittaa, mutta älä kerro,
miten se korjataan. Haluan löytää korjauksen itse.
<liitä virheilmoitus + koodinpätkä tähän>
```

Jos LLM antaa korjauksen silti, hylkää vastaus ja kirjoita korjaus omin sanoin. Älä liitä LLM:n
tuotosta sellaisenaan muistiinpanoihisi.

### Säilytä muistiinpanosi

Pieni kirjasto C#-virhekoodeista (CS0103, CS1002, …), jonka kirjoitat ylös nyt, nopeuttaa L24-
hetkeä AT3:ssa, kun sinun täytyy lukea oikea kääntäjän ilmoitus ja tehdä yksi pieni korjaus.

## 🟣 SYVENTÄVÄ — Tehtävä 8.5-CS — Vertaa JS-luokkakaverin kanssa

Tavoite. Lue luokkakaverin JavaScript-ohjelma ja kirjoita 3–5 virkettä eroista sekä yksi asia,
joka on sama.

### Vaiheet

1. Etsi luokkakaveri, joka käytti AT3:ssa JavaScriptiä. Näyttäkää toisillenne ohjelmanne.
2. Lue hänen ohjelmansa rivi riviltä. Tunnista jokaisen JS-rivin C#-vastine.
3. Kirjoita 3–5 virkettä eroista (C#:ssa puolipisteet kaikkialla vs. JS:ssä usein valinnaisia;
vs ; / vs ; C#:n isolla alkavat metodinimet)

```javascript
Console.WriteLine console.log int string let
```

ja yksi asia, joka on sama (silmukkarakenne, , tavoite). `if/else`

### Jos teet tämän yksin

Jos JS-luokkakaveria ei ole saatavilla, lue -tiedoston yhden esimerkin JavaScript- `self-study.md`
versio (ohjelmat A–E) ja kirjoita samat 3–5 virkettä vertaamalla sitä saman sivun C#-versioon.

### Säilytä muistiinpanosi

Liitä 3–5 virkettä AT3-kansioosi. Ne eivät ole osa hyväksymistarkistusta, mutta ne terävöittävät
L24-esitystä: opiskelija, joka osaa nimetä yhden asian toisesta kielestä, ymmärtää paremmin
myös oman valintansa.
