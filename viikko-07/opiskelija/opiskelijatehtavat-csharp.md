# Viikko 7 — Opiskelijatehtävät (C#)

## Tämän viikon C#-tehtävien yleiskuva

Tällä viikolla on neljä tehtävää C#-polussa. Vihreällä pisteellä merkitty tehtävä (🟢
PAKOLLINEN) on vähimmäissuoritus — tee se, jotta pysyt mukana. Kolme violetilla pisteellä
merkittyä tehtävää (🟣 SYVENTÄVÄ) ovat valinnaisia laajennuksia; valitse yksi tai kaksi, jos
sinulla on aikaa.
Kaikki tällä viikolla kirjoittamasi on raaka-ainetta AT3:een, joka tulee viikon 8 lopussa. AT3
pyytää sinua kääntämään palan omaa viikon 6 pseudokoodiasi pieneksi ohjelmaksi sillä kielellä,
jonka valitset tällä viikolla. Tallenna koodisi.
IDE-asennusta ei tarvita. Ei -komentoa, ei Visual Studiota, ei .NET SDK:n asennusta. `dotnet new`
C# toimii tällä viikolla pienessä verkkoympäristössä samassa selaimessa, jossa luet tätä. Tällä
viikolla ei ole testikehystä; ajat koodin, luet tulosteen ja vertaat sitä ennusteeseesi.
Ajattele näin: viikon 6 pseudokoodissa kirjoitit “mitä pitäisi tapahtua”. Nyt kirjoitat
ensimmäisen oikean ohjelman, joka saa tietokoneen tekemään sen.

### Näin avaat verkkopohjaisen C#-ympäristön

• Oletus — .NET Fiddle. Mene selaimessa osoitteeseen . Tiliä ei tarvita. `dotnetfiddle.net`
Valitse yläreunasta Console. Liitä koodirivisi -metodin aaltosulkeiden sisään ja `Main`
paina Run. Tuloste näkyy alemmassa laatikossa.
• Vaihtoehto — sharplab.io. Sama idea, hieman eri ulkoasu — myös selainpohjainen, ei
tiliä.
• Vaihtoehto — Replit (C#-mallipohja). Selainpohjainen, kirjautuminen mahdollinen
mutta ei aina pakollinen.
Valitse yksi ja käytä samaa ympäristöä koko viikon.
🟢

## PAKOLLINEN — Ensimmäinen konsoliohjelmasi (C#)

Tavoite: Aja ensimmäinen C#-ohjelmasi verkkoympäristössä. Ohjelma tulostaa tervehdyksen,
määrittelee muuttujan ja tekee pienen laskun. Tämä on C#-polun viikon 7 vähimmäissuoritus.
Tämän tehtävän lopussa säilyttämäsi kuvakaappaus on juuri sellainen tuotos, jota AT3 käyttää
ensi viikolla.

### Vaiheet

1. Avaa .NET Fiddle osoitteessa . Valitse yläreunasta Console. Näet `dotnetfiddle.net`
pienen mallipohjan, jossa on -metodi. `Main`
2. Tulosta tervehdys omalla oikealla nimelläsi. Kirjoita -metodin sisään alla `Main`
oleva rivi ja käytä lainausmerkeissä omaa oikeaa nimeäsi:

```csharp
Console.WriteLine("Hei, <nimesi>");
```

Paina Run. Jos näkyviin tulee punainen virhe, tarkista puolipiste ja kirjainkoko kohdassa
. `Console.WriteLine`
3. Määrittele muuttuja iällesi ja tulosta se. Lisää kaksi riviä ja korvaa

```
<oikea ikäsi>
```

omalla numerollasi:

```csharp
int ika = <oikea ikäsi>;
Console.WriteLine(ika);
```

4. Laske vuodet täysi-ikäisyyteen ja tulosta tulos. Lisää vielä kaksi riviä:

```csharp
int vuosiaTaysiIkaisyteen = 18 - ika;
Console.WriteLine(vuosiaTaysiIkaisyteen);
```

Jos olet jo 18-vuotias tai vanhempi, luku on nolla tai negatiivinen — se on oikein.
5. Ota kuvakaappaus tulostelaatikosta, jossa näkyvät kaikki kolme tulostetta oikeassa
järjestyksessä. Liitä se viikon 7 muistiinpanotiedostoon.
6. Kirjoita 2–3 virkkeen pohdinta. Yksi asia, joka yllätti C#:ssa (esimerkiksi se, että
tyyppi piti nimetä etukäteen), ja yksi asia, joka toimi juuri niin kuin ennustit. `int`

### Säilytä muistiinpanosi

Säilytä kuvakaappaus, koodirivit ja pohdinta samassa kansiossa. AT3 tulee viikon 8 lopussa ja
pyytää pientä ohjelmaa, joka rakentuu täsmälleen tämän muodon päälle — muuttuja, lasku,
tuloste. Tämän koodin uudelleenkäyttö AT3:ssa on suositeltavaa.

## 🟣 SYVENTÄVÄ — Ensimmäinen if/else (C#)

Tavoite: Kirjoita 6-rivinen C#-ohjelma, joka käyttää -rakennetta ja tulostaa `if/else`
jommankumman kahdesta viestistä muuttujan arvon perusteella. Tämä on L21-itseopiskelun
ohjelma omissa käsissäsi.

### Vaiheet

1. Liitä .NET Fiddlessä -metodin sisään alla oleva ohjelma:

```csharp
Main
int ika = 16;
if (ika >= 18)
{
Console.WriteLine("Saat tulla sisään.");
}
else
{
Console.WriteLine("Valitettavasti et ole tarpeeksi vanha.");
}
```

2. Ennusta ennen ajamista. Kun , mitä odotat tulostelaatikkoon ilmestyvän?

```
ika = 16
```

Kirjoita se ylös ennen kuin painat Run.
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

## 🟣 SYVENTÄVÄ — Käännä viikon 6 pseudokoodisi (C#)

Tavoite: Ota yksi oma viikon 6 pseudokoodisi, jossa on , ja muuta se pieneksi C#- `IF/ELSE`
ohjelmaksi, joka toimii .NET Fiddlessä.
Tämä on tiedoston AT3-muotoisin tehtävä. Kun teet sen nyt, AT3 on puoliksi kirjoitettu ennen
kuin se julkaistaan.

### Vaiheet

1. Valitse yksi viikon 6 pseudokoodisi, jossa on tai . Paras vaihtoehto on se, `IF IF/ELSE`
jonka kirjoitit oikeasti itse.
2. Kopioi pseudokoodi muistiinpanotiedostoosi.
3. Käännä se C#:ksi rivi riviltä:
– → tai , jos arvo on

```
READ <jotakin> int <jotakin> = <valitsemasi arvo>; string
```

tekstiä.
– → .

```
IF … THEN if (…) {
```

– → .

```
ELSE } else {
```

– → .

```csharp
WRITE "…" Console.WriteLine("…");
```

– → .

```pseudocode
ENDIF }
```

4. Liitä C#-koodi -metodin sisään ja paina Run. Lue punainen virheilmoitus, jos `Main`
sellainen tulee — kääntäjä osoittaa yleensä suoraan rivin ja kertoo, mistä sanasta se ei
pitänyt.
5. Tallenna pseudokoodi ja C# vierekkäin muistiinpanoihisi. Tämä on täsmälleen
sellainen tuotos, jota AT3 pyytää.

### Säilytä muistiinpanosi

Säilytä pseudokoodi ja C# vierekkäin. AT3 tulee viikon 8 lopussa ja käyttää tätä tuotosta
suoraan.
🟣

## SYVENTÄVÄ — Riko ohjelma tahallaan (C#)

Tavoite: Lisää yksi virhe kerrallaan toimivaan ohjelmaasi ensimmäisestä if/else-tehtävästä ja
lue tarkka kääntäjän ilmoitus, jonka C# tulostaa.
Tarkoitus on lukea oikeita kääntäjän viestejä, jotta ensimmäinen yllättävä virhe AT3:ssa ei
pysäytä sinua. C# on tässä JavaScriptiä tiukempi: monet ongelmat näkyvät käännösvirheenä
ennen kuin ohjelma edes yrittää käynnistyä, mikä on oikeastaan ystävällistä.

### Vaiheet

1. Aloita toimivasta -ohjelmasta, jonka teit tehtävässä Ensimmäinen if/else (C#). `if/else`
Varmista, että se toimii yhä puhtaasti.
2. Riko se kolmella tavalla, yksi kerrallaan, ja kopioi tarkka kääntäjän ilmoitus:
– Unohda puolipiste. Poista rivin lopusta. (Tämä on klassinen C#-

```
; int ika = 16
```

käännösvirhe, jota JavaScript ei välttämättä huomaisi.)
– Sekoita aaltosulkeet. Poista -haaran sulkeva . `if }`
– Kirjoita tulostusfunktion nimi väärin. Muuta muotoon `Console.WriteLine`
. `Console.WriteLin`
3. Korjaa jokainen virhe ennen kuin lisäät seuraavan.
4. Pohdinta (2–3 virkettä): mikä virheilmoitus oli selkein? Mikä oli hämmentävä?
Osoittiko jokin ilmoitus väärälle riville?

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse paria — kääntäjä on sparrauskumppanisi. Jos haluat toisen
mielipiteen, lähetä yksi virheilmoitus luokan chattiin: “Onko joku muu nähnyt tämän C#:ssa?”

### Säilytä muistiinpanosi

Säilytä kolme rikottua riviä ja kolme tarkkaa kääntäjän ilmoitusta. AT3 tulee viikon 8 lopussa
ja siihen liittyy vähintään yksi virheilmoitus, jota et ole nähnyt ennen — pieni kirjasto C#-
virheistä auttaa sinua selviämään siitä nopeammin.
