# Viikko 7 — Opiskelijatehtävät (JavaScript)

## Tämän viikon JavaScript-tehtävien yleiskuva

Tällä viikolla on neljä tehtävää JavaScript-polussa. Vihreällä pisteellä merkitty tehtävä (🟢
PAKOLLINEN) on vähimmäissuoritus — tee se, jotta pysyt mukana. Kolme violetilla pisteellä
merkittyä tehtävää (🟣 SYVENTÄVÄ) ovat valinnaisia laajennuksia; valitse yksi tai kaksi, jos
sinulla on aikaa.
Kaikki tällä viikolla kirjoittamasi on raaka-ainetta AT3:een, joka tulee viikon 8 lopussa. AT3
pyytää sinua kääntämään palan omaa viikon 6 pseudokoodiasi pieneksi ohjelmaksi sillä kielellä,
jonka valitset tällä viikolla. Tallenna koodisi.
IDE-asennusta ei tarvita. JavaScript toimii selaimesi DevTools-konsolissa. Tällä viikolla ei ole
testikehystä; ajat koodin, luet tulosteen ja vertaat sitä ennusteeseesi.

### Näin avaat JavaScript-konsolin

• Mac: missä tahansa selaimessa. `Cmd + Opt + J`
• Windows / Linux: missä tahansa selaimessa. `Ctrl + Shift + J`
• Tai: napsauta sivua hiiren oikealla, valitse Inspect tai Tarkista, ja avaa Console-
välilehti.
Liitä rivi, paina Enter ja lue, mitä ilmestyy.
🟢

## PAKOLLINEN — Ensimmäinen konsoliohjelmasi (JS)

Tavoite: Aja ensimmäinen JavaScript-ohjelmasi selaimen konsolissa. Ohjelma tulostaa
tervehdyksen, määrittelee muuttujan ja tekee pienen laskun. Tämä on JavaScript-polun viikon 7
vähimmäissuoritus.
Tämän tehtävän lopussa säilyttämäsi kuvakaappaus on juuri sellainen tuotos, jota AT3 käyttää
ensi viikolla.

### Vaiheet

1. Avaa konsoli missä tahansa selaimessa yllä olevan ohjeen avulla.
2. Tulosta tervehdys omalla oikealla nimelläsi. Kirjoita alla oleva rivi käyttäen
lainausmerkeissä omaa oikeaa nimeäsi ja paina Enter:

```javascript
console.log("Hei, <nimesi>");
```

Jos mitään ei näy, tarkista lainausmerkit ja piste kohdassa . `console.log`
3. Määrittele muuttuja iällesi ja tulosta se. Korvaa omalla numerollasi:

```javascript
<oikea ikäsi>
let ika = <oikea ikäsi>;
console.log(ika);
```

4. Laske vuodet täysi-ikäisyyteen ja tulosta tulos. Samassa konsoli-istunnossa:

```javascript
let vuosiaTaysiIkaisyteen = 18 - ika;
console.log(vuosiaTaysiIkaisyteen);
```

Jos olet jo 18-vuotias tai vanhempi, luku on nolla tai negatiivinen — se on oikein.
5. Ota kuvakaappaus konsolista, jossa näkyvät kaikki kolme tulostetta oikeassa
järjestyksessä. Liitä se viikon 7 muistiinpanotiedostoon.
6. Kirjoita 2–3 virkkeen pohdinta. Yksi asia, joka yllätti sinut, ja yksi asia, joka toimi
juuri niin kuin ennustit.

### Säilytä muistiinpanosi

Säilytä kuvakaappaus, kolme koodiriviä ja pohdinta samassa kansiossa. AT3 tulee viikon 8
lopussa ja pyytää pientä ohjelmaa, joka rakentuu täsmälleen tämän muodon päälle —
muuttuja, lasku, tuloste. Tämän koodin uudelleenkäyttö AT3:ssa on suositeltavaa.

## 🟣 SYVENTÄVÄ — Ensimmäinen if/else (JS)

Tavoite: Kirjoita 6-rivinen JavaScript-ohjelma, joka käyttää -rakennetta ja tulostaa `if/else`
jommankumman kahdesta viestistä muuttujan arvon perusteella. Tämä on L21-itseopiskelun
ohjelma omissa käsissäsi.

### Vaiheet

1. Liitä konsoliin alla oleva ohjelma:

```javascript
let ika = 16;
if (ika >= 18) {
console.log("Saat tulla sisään.");
} else {
console.log("Valitettavasti et ole tarpeeksi vanha.");
}
```

2. Ennusta ennen ajamista. Kun , mitä odotat konsolin tulostavan? Kirjoita se

```
ika = 16
```

ylös ennen kuin painat Enter.
3. Aja ohjelma. Vertaa ennustetta todellisuuteen.
4. Muuta iäksi 19 ja aja uudelleen. Tee ennuste taas ensin. Tulosteen pitäisi vaihtaa
haaraa.
5. Ota kuvakaappaus molemmista ajoista. Tallenna ne ennustemuistiinpanojen
viereen.

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse paria. Jos haluat toisen silmäparin, käytä 24 tunnin väliä: ennusta
tuloste tänään ja aja ohjelma huomenna lukematta ennustetta uudelleen.

### Säilytä muistiinpanosi

Säilytä ohjelma, molemmat ennusteet ja molemmat kuvakaappaukset. AT3 tulee viikon 8
lopussa ja pyytää pientä -ohjelmaa, joka rakentuu täsmälleen tämän muodon päälle. `if/else`
Tämä tehtävä on AT3:n kenraaliharjoitus.

## 🟣 SYVENTÄVÄ — Käännä viikon 6 pseudokoodisi (JS)

Tavoite: Ota yksi oma viikon 6 pseudokoodisi, jossa on , ja muuta se pieneksi `IF/ELSE`
JavaScript-ohjelmaksi, joka toimii konsolissa.
Tämä on tiedoston AT3-muotoisin tehtävä. Kun teet sen nyt, AT3 on puoliksi kirjoitettu ennen
kuin se julkaistaan.

### Vaiheet

1. Valitse yksi viikon 6 pseudokoodisi, jossa on tai . Paras vaihtoehto on se, `IF IF/ELSE`
jonka kirjoitit oikeasti itse.
2. Kopioi pseudokoodi muistiinpanotiedostoosi.
3. Käännä se JavaScriptiksi rivi riviltä:
– → tässä vaiheessa.

```javascript
READ <jotakin> let <jotakin> = <valitsemasi arvo>;
```

– → .

```
IF … THEN if (…) {
```

– → .

```
ELSE } else {
```

– → .

```javascript
WRITE "…" console.log("…");
```

– → .

```pseudocode
ENDIF }
```

4. Liitä JavaScript konsoliin ja aja se. Lue mahdollinen virheilmoitus — tulkki osoittaa
yleensä suoraan rivin.
5. Tallenna pseudokoodi ja JavaScript vierekkäin muistiinpanoihisi. Tämä on
täsmälleen sellainen tuotos, jota AT3 pyytää.

### Säilytä muistiinpanosi

Säilytä pseudokoodi ja JS vierekkäin. AT3 tulee viikon 8 lopussa ja käyttää tätä tuotosta
suoraan.

## 🟣 SYVENTÄVÄ — Riko ohjelma tahallaan (JS)

Tavoite: Lisää yksi virhe kerrallaan toimivaan ohjelmaasi ensimmäisestä if/else-tehtävästä ja
lue tarkka virheilmoitus, jonka JavaScript-moottori tulostaa.
Tarkoitus on lukea oikeita virheilmoituksia, jotta ensimmäinen yllättävä virhe AT3:ssa ei
pysäytä sinua.

### Vaiheet

1. Aloita toimivasta -ohjelmasta, jonka teit tehtävässä Ensimmäinen if/else (JS). `if/else`
Varmista, että se toimii yhä puhtaasti.
2. Riko se kolmella tavalla, yksi kerrallaan, ja kopioi tarkka virheilmoitus, jonka
konsoli tulostaa:
– Unohda lainausmerkki. Muuta muotoon `"Saat tulla sisään." "Saat tulla`
eli jätä sulkeva lainausmerkki pois. `sisään.`
– Unohda sulkeva aaltosulje. Poista viimeinen . `}`
– Kirjoita tulostusfunktion nimi väärin. Muuta muotoon `console.log`
. `consle.log`
3. Korjaa jokainen virhe ennen kuin lisäät seuraavan.
4. Pohdinta (2–3 virkettä): mikä virheilmoitus oli selkein? Mikä oli hämmentävä?
Osoittiko jokin ilmoitus väärälle riville?

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse paria — konsoli on sparrauskumppanisi. Jos haluat toisen mielipiteen,
lähetä yksi virheilmoitus luokan chattiin: “Onko joku muu nähnyt tämän JS:ssä?”

### Säilytä muistiinpanosi

Säilytä kolme rikottua riviä ja kolme tarkkaa virheilmoitusta. AT3 tulee viikon 8 lopussa ja
siihen liittyy vähintään yksi virheilmoitus, jota et ole nähnyt ennen — pieni kirjasto JS-
virheistä auttaa sinua selviämään siitä nopeammin.
