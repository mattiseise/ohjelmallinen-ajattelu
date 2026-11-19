# Viikko 7 — Tunnilla tehtävät ohjatut tehtävät

## Yleiskuva

Tämä tiedosto sisältää tunnilla tehtävät, opettajan ohjaamat aktiviteetit viikolle 7. Ne tehdään
tunnilla, eivät kotitehtävinä, eikä niitä voi korvata LLM:llä tai monisteella.
Molemmat tehtävät on suunniteltu toimimaan kielisekoitteisessa luokassa: osa opiskelijoista käyttää
JavaScriptiä ja osa C#:a samaan aikaan. Se on tarkoitus, ei ongelma.
• Tehtävä A - "Konsoliviesti" on PAKOLLINEN. Se kuuluu oppitunnin 20 kohtaan 55-75 min.
Jokainen opiskelija - sekä JS- että C#-opiskelija - näkee ja ennustaa molempien kielten koodipätkiä,
ja vertailu on tehtävän opetus.
• Tehtävä B - "Käännä naapurisi koodi" on VALINNAINEN. Se sopii oppitunnin 21
parityökohtaan 60-80 min.
Vinkki: Pidä viestin ydin lyhyenä: ajattelu on samaa, syntaksi muuttuu. Kun opiskelija sanoo "C# on
vaikeampi", palauta keskustelu siihen, mikä osa oikeasti muuttui: avainsanat, tulostuskomento tai
muuttujan ilmoittaminen.

## Tehtävä A - "Konsoliviesti" - PAKOLLINEN

Tavoite. Luokka ennustaa kuuden pienen koodipätkän tulosteen - kolme JavaScriptillä, kolme C#:lla -
ennen kuin opettaja suorittaa jokaisen livenä. Opiskelijat näkevät, eivät vain kuule, että ajattelu on
sama molemmissa kielissä ja vain syntaksi muuttuu. Tämä on viikon 7 vastalääke väärinkäsitykselle
"C# on vaikeampi kuin JS".
Ryhmäkoko. Koko luokka. Jokainen opiskelija kirjoittaa oman ennusteensa; opettaja suorittaa jokaisen
koodipätkän projektorilla.
Tarvittava aika. 20 min (oppitunti 20, kohta 55-75 min). Älä ota aikaa tehtävää edeltävästä 30
minuutin itsenäisen työn osasta.
Opettajan valmistelut.
1. Avaa molemmat ympäristöt rinnakkain projektorille ennen tuntia: selaimen DevTools-konsoli
toiselle puolelle ja toiselle puolelle. Pidä C#:n -runko valmiiksi näkyvillä `dotnetfiddle.net Main`
Fiddlessä.
2. Valmistele kuusi koodipätkää etukäteen, joko kopioituna muistiinpanotiedostoon tai numeroiduille
korteille. Suositeltu oletussarja (kolme JS, kolme C#, tässä järjestyksessä):

```javascript
// Snippet 1 (JS)
let x = 5;
let y = 3;
console.log(x + y);
// Snippet 2 (JS)
let name = "Lyra";
console.log("Hello, " + name);
// Snippet 3 (JS)
let age = 17;
if (age >= 18) console.log("adult");
else console.log("minor");
// Snippet 4 (C#)
int x = 5;
int y = 3;
Console.WriteLine(x + y);
// Snippet 5 (C#)
string name = "Lyra";
Console.WriteLine("Hello, " + name);
// Snippet 6 (C#)
int age = 17;
if (age >= 18) Console.WriteLine("adult");
else Console.WriteLine("minor");
```

20
Tunnilla tehtävät ohjatut tehtävät - sivu
Paritus on tarkoituksellinen: pätkä 1 <-> 4, 2 <-> 5, 3 <-> 6. Sama tehtävä, eri pinta.
3. Päätä koodipätkien järjestys. Vaihtele (1, 4, 2, 5, 3, 6), jos haluat vahvimman rinnakkaisvertailun,
tai ryhmittele (1, 2, 3 ja sitten 4, 5, 6), jos luokkasi tarvitsee ensin JS-kehyksen ja sitten C#-
kehyksen. Vaihtelu on oletussuositus.
4. Valmistele taululle kaksisarakkeinen kirjanpito: Ennusti oikein | Tuloste yllätti. Viestitehtävän
aikana tehdyt tukkimiehenkirjanpidot kertovat reaaliajassa, lukeeko luokka koodia vai arvaako se.

### Vaiheittainen ohjaus

1. Aseta säännöt (2 min). Sano: "Näytän kuusi pientä koodipätkää, yhden kerrallaan. Kolme on
JavaScriptiä, kolme C#:a. Jokaisesta pätkästä kirjoitatte - paperille tai chattiin - täsmälleen, mitä
arvelette konsolin tulostavan, ennen kuin painan Run. Sitten suoritan sen. Sen jälkeen katsomme
eron, jos sellainen on. Tavoite ei ole olla oikeassa; tavoite on lukea koodia rivi riviltä."
2. Näytä pätkä 1 ruudulla (2 min). Lue se kerran ääneen. Anna opiskelijoille 30 sekuntia. Suorita
pätkä. Lue tuloste ääneen. Kysy yhdeltä opiskelijalta: "Mitä ennustit?" Tee merkintä oikeaan
taulusarakkeeseen.
3. Toista pätkille 2-6 (yhteensä noin 15 min), vaihdellen JS:n ja C#:n välillä. Oletusjärjestys on 1, 4,
2, 5, 3, 6. Jokaiselle pätkälle:
• 20 sekuntia hiljaista ennustamista,
• suoritus livenä,
• tulosteen lukeminen ääneen,
• yksi opiskelija kertoo vapaaehtoisesti, mitä kirjoitti,
• luokka vertaa ja opettaja merkitsee taululle.
4. Päätä vertailu (1 min). Osoita taulua ja sano: "Ajattelu oli sama pätkissä 1 ja 4. Sama pätkissä 2 ja
5. Sama pätkissä 3 ja 6. Joka kerta muuttui vain sanat. Tätä tarkoittaa lause: syntaksi on sopimus,
ajattelu on asia."
Ajattele näin: Syntaksi tarkoittaa ohjelmointikielen kirjoitustapaa. Logiikka tarkoittaa sitä, mitä ohjelma
tekee. Tässä tehtävässä logiikka pysyy samana ja syntaksi vaihtuu.
Purkuun sopivia kysymyksiä (käytä 1-2 oppitunnin 20 purussa 1:15-1:25, ei viestin sisällä):
• Mikä pari (1<->4, 2<->5 tai 3<->6) tuntui selvimmin "ihan samalta"?
• Ennustiko joku oikein pätkän toisella kielellä?
• Mikä yksi C#-sana piti tarkistaa? Mikä yksi JS-sana?
Miksi tehtävä vaatii luokkahuoneen. Elävä ennusta-ja-suorita-rytmi ja välitön vertailu
luokkakavereihin ovat tehtävän ydin. Tätä ei voi tehdä kotitehtävänä samalla tavalla.
Viittaus. Tämä on oppitunnin 20 suunnitelman kohta 55-75 min tiedostossa `teacher-`
. Tässä kohdassa rakennettu "me näimme" -taulu tuodaan takaisin purkuun kohdassa `materials.md`
1:15-1:25.

## Tehtävä B - "Käännä naapurisi koodi" - VALINNAINEN

Tavoite. JS-opiskelija ja C#-opiskelija kääntävät toistensa -koodin omaan kieleensä käsin, `if/else`
ilman LLM:ää. Opiskelijat huomaavat, että käännös on enimmäkseen sanasta sanaan ja jäljelle jäävät
erot ovat pieniä.
Ryhmäkoko. Parit: yksi JS-opiskelija ja yksi C#-opiskelija. Jos opiskelijoita on pariton määrä, yksi
kolmen hengen ryhmä, jossa kahta käyttää samaa kieltä.
Tarvittava aika. 20 min (oppitunti 21, parityökohta 60-80 min).
Opettajan valmistelut.
1. Taululle kirjoitettu ohje käännöstehtävän säännöistä.
2. Paperi ja kynä jokaiselle opiskelijalle. Ei kannettavia itse käännöksen aikana.
3. Varalla oleva `if/else`-pätkä, jos opiskelijalla ei vielä ole oman tehtävän koodia. Mikä tahansa
itseopiskelun ikäraja- toimii. `if/else`
21
Tunnilla tehtävät ohjatut tehtävät - sivu

### Vaiheittainen ohjaus

1. Parita kielten yli (2 min). Jokaisessa parissa on yksi JS-opiskelija ja yksi C#-opiskelija.
2. Vaihda `if/else`-koodi (1 min). Jokainen antaa toiselle toimivan koodinsa tehtävästä First if/else. Ei
suullisia vihjeitä.
3. Käännä käsin (8 min). Jokainen kirjoittaa - paperille, ei koneella - toisen opiskelijan koodin omalla
kielellään. Jos sanasta sanaan -käännös ei toimi, ympyröi rivi.
4. Suorita käännökset (5 min). Nyt kannettavat sallitaan. Jokainen testaa käännöksensä omassa
ympäristössään kopioimalla sen sinne.
5. Paljastus ja keskustelu (2 min). Parit vertaavat ympyröimiään kohtia. Mitkä rivit kääntyivät
suoraan?
6. Koko luokan purku (2 min). Kysy kahdelta parilta: "Mikä yksi sana muuttui eniten? Mikä ei
muuttunut lainkaan?" Odotettu havainto: <-> / , <-> `let int string console.log`
. , , , , eivät muuttuneet.

```csharp
Console.WriteLine if else >= { }
```

Vinkki: Käsin kääntäminen hidastaa työtä tarkoituksella. Se pakottaa opiskelijan lukemaan koodin
rakenteen, ei vain kopioimaan tai pyytämään tekoälyä tekemään käännöstä.
Purkuun sopivia kysymyksiä.
• Mitkä rivit käänsit empimättä?
• Mitkä rivit saivat sinut pysähtymään ja ajattelemaan?
Miksi tehtävä vaatii luokkahuoneen. Kielten välinen pari on olemassa vain luokassa. Elävä käsin
kääntäminen on se osa, jota LLM ei voi korvata.
Viittaus. Tämä on oppitunnin 21 suunnitelman kohta 60-80 min tiedostossa `teacher-`
. Jos opettajan on jätettävä jokin viikon tehtävä pois, jätä tehtävä B: tehtävä A kantaa `materials.md`
viikon 7 keskeisen viestin ja toimii AT3-valmiuden diagnostisena tehtävänä.
22
Tunnilla tehtävät ohjatut tehtävät - sivu
