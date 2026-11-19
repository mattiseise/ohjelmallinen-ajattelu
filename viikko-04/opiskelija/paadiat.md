# Viikko 4 — Ratkaisujen vertaileminen

---

## Viikko 4 - Ratkaisujen vertailu

Ohjelmallinen ajattelu
Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi

---

## Keskeinen viesti

> Useampi kuin yksi kelvollinen ratkaisu voi ratkaista saman ongelman. Niiden välillä
valitseminen ei ole makuasia - se perustuu nimettyihin kriteereihin.
Tämä on koko viikon tärkein lause muistaa.

### Ajattele näin: "pidän tästä" ei vielä riitä perusteluksi. Kerro, millä perusteella pidät sitä

parempana. ---

## Mihin viikko 4 sijoittuu

• Viikot 1-3 - algoritmit (V1), pilkkominen + AT1 (V2), vuokaaviot ja abstraktio (V3)
• Viikko 4 - kurssin puolivälin reflektio: vertaa ja korjaa sitä, mitä olet jo rakentanut.
• Viikot 5-8 - logiikkarakenteet (V5), pseudokoodi + AT2 (V6), JavaScript (V7), silmukat + AT3 (V8)
• Tällä viikolla ei tule uutta ohjelmallisen ajattelun perusrakennetta. Raaka-aineena on oma
työsi viikoilta 2 ja 3. ---

## Ongelma ei ole sama asia kuin ratkaisu

Ongelma on tavoite: "tee juotava kupillinen teetä", "varmista, että projektikansiosta on
palautettava varmuuskopio".
Ratkaisu on yksi tapa saavuttaa tavoite - ne vaiheet, jotka kirjoitat muistiin.
Yksi ongelma. Monta mahdollista ratkaisua. Kaikki voivat olla kelvollisia.

### Vinkki: älä arvioi ratkaisua ennen kuin tavoite on selvä. ---

## Kaksi tapaa tehdä teetä

```
Vaihe | Resepti A (keitä ensin) | Resepti B (hauduta ensin)
1 | Täytä vedenkeitin 250 ml vedellä | Laita yksi teepussi kuppiin
2 | Keitä vesi | Täytä vedenkeitin 250 ml vedellä
3 | Laita yksi teepussi kuppiin | Keitä vesi
4 | Kaada kiehuva vesi pussin päälle | Kaada kiehuva vesi pussin päälle
5 | Odota 3 minuuttia, poista pussi | Odota, kunnes väri näyttää
oikealta, poista pussi
```

Molemmat tuottavat juotavan kupillisen teetä. Ne eroavat järjestyksessä ja siinä, mitä
käyttäjän täytyy itse arvioida. ---

## Kaksi tapaa varmuuskopioida projektikansio

```
Vaihe | Tapa A (USB-kopio) | Tapa B (zip + sähköposti)
1 | Liitä USB-muisti kannettavaan | Napsauta projektikansiota
oikealla
2 | Avaa projektikansio | Valitse "Pakkaa .zip-muotoon"
3 | Valitse kaikki tiedostot, paina Ctrl+C | Odota, että zip-tiedosto
ilmestyy
4 | Avaa USB-muisti | Avaa koulun sähköposti
5 | Paina Ctrl+V ja odota kopiointia | Liitä zip ja lähetä se
itsellesi
6 | Poista USB-muisti turvallisesti | Tallenna viesti Backups-
kansioon
```

Molemmat tuottavat palautettavan varmuuskopion. Ne eroavat siinä, missä kopio sijaitsee ja
mikä voi mennä pieleen. ---

## Mikä on samaa, mikä erilaista?

• Sama - molemmat saavuttavat tavoitteen ja molemmat ovat kelvollisia.
• Erilaista - *vaiheiden järjestys* muuttuu (keitä ensin vs. hauduta ensin).
• Erilaista - mitä *jätetään käyttäjän arvioitavaksi* (laske kolme minuuttia vs. arvioi väri).
• Erilaista - mikä voi *mennä pieleen* (teepussin unohtaminen vs. USB-muistin turvallisen
poistamisen unohtaminen).
• Viimeinen lista on kriteerien alku.

### Tee näin: kirjoita ensin erot neutraalisti, vasta sitten arvioi niitä. ---

## Mausta kriteeriin

"Pidän vain resepti A:sta enemmän." - makuasia.
"Resepti A on selkeämpi vaiheessa 5, koska 3 minuuttia kertoo suorittajalle täsmälleen, milloin
lopettaa." - kriteeri on nimetty.
> Useampi kuin yksi kelvollinen ratkaisu voi ratkaista saman ongelman. Niiden välillä
valitseminen ei ole makuasia - se perustuu nimettyihin kriteereihin.
Kriteeri on nimetty mittapuu. Kun nimeät sen, "parempi" lakkaa olemasta tunne ja muuttuu
vertailuksi. ---

## Neljä kriteeriä

• Ensimmäisellä mainintakerralla aina tässä järjestyksessä: selkeys · tehokkuus · toistettavuus ·
virhealttius.
• Selkeys - kirjaimellinen suorittaja voi lukea ohjeen kerran ja tietää, mitä tehdä.
• Tehokkuus - ratkaisu saavuttaa tavoitteen ilman hukattuja vaiheita.
• Toistettavuus - sama syöte, sama tulos, joka kerta.
• Virhealttius - ohjetta seuratessa on vaikea tehdä väärä asia.
• Neljä kriteeriä. Samat neljä nimeä kaikkialla.

### Vinkki: arvioi yksi kriteeri kerrallaan. ---

## Selkeys kahdessa teereseptissä

Resepti A - "Odota 3 minuuttia, poista pussi." Numero. Kirjaimellinen suorittaja lopettaa
oikeaan aikaan.
Resepti B - "Odota, kunnes väri näyttää oikealta, poista pussi." Suorittajan täytyy tietää, miltä
oikea väri näyttää. Se on yksi ylimääräinen sanomaton asia.
Molemmat saavuttavat tavoitteen. Resepti A on selkeämpi vaiheessa 5, koska se nimeää
konkreettisen ajan.

### Ajattele näin: selkeys vähentää arvaamista. ---

## Tehokkuus kahdessa varmuuskopiointitavassa

Tapa A (USB-kopio) kopioi jokaisen tiedoston yksitellen. Jos kansiossa on 500 pientä tiedostoa,
kopiointi kestää pidempään kuin pelkkä datan määrä antaisi olettaa.
Tapa B (zip + sähköposti) pakkaa kansion ensin yhdeksi tiedostoksi ja siirtää yhden tiedoston
kerran.
Molemmat saavuttavat tavoitteen. Tapa B on tehokkaampi kansiolle, jossa on paljon pieniä
tiedostoja - siirrossa on vähemmän hukattuja vaiheita. ---

## Toistettavuus ja virhealttius - nopeat esimerkit

Toistettavuus. Resepti A käyttää aina 200 ml vettä ja kolmea minuuttia - sama juoma
maanantaina ja perjantaina. "Vähän vettä, maista" tuottaa eri juoman joka kerta.
Virhealttius. Tapa A voi ylikirjoittaa aiemman USB-varmuuskopion, jos et nimeä kansiota
uudelleen; yksi lipsahdus ja eilinen kopio on poissa. Tapa B säilyttää sähköpostissa
päivämäärällisen kopion jokaisesta varmuuskopiosta - sitä on vaikeampi hukata vahingossa.

### Vinkki: virhealttius kysyy, kuinka helppo käyttäjän on mokata. Kompromissit - kun kriteerit vetävät eri suuntiin
Resepti A voittaa selkeydessä, koska kolme minuuttia on täsmällinen.
Resepti B voi voittaa tehokkuudessa, koska se keittää vain kerran ja käyttää väriä
pysäytysmerkkinä, jonka kokenut teenjuoja näkee yhdellä vilkaisulla.
"Paras" valinta riippuu suorittajasta. Kompromissin nimeäminen on analyysia. Voittajaa ei
tarvitse kruunata.

### Ajattele näin: ammattilainen ei aina valitse yhtä ratkaisua kaikille, vaan ratkaisun tilanteeseen. ---

## Vertaisarvioinnin käytäntö

Kolme vaihetta. Aina tässä järjestyksessä.
1. Kriteerit - lue parin artefakti hiljaa. Kirjoita yksi virke jokaisesta kriteeristä: selkeys,
tehokkuus, toistettavuus, virhealttius.
2. Palaute - valitse kaksi hyödyllisintä virkettä. Kummassakin nimetään kriteeri ja tietty vaihe.
3. Korjaus - tekijä muuttaa alkuperäisestä työstä yhden tai kaksi konkreettista asiaa
palautteen perusteella ja kirjoittaa 3-5 virkkeen muutosmuistiinpanon.
Ei arvosanoja. Ei numeroita. Ei "paras"-leimaa. ---

## Palaute, jota toinen voi käyttää

• Kolme lyhyttä sääntöä.
• Nimeä kriteeri. *"Tämä on epäselvä"* → *"Tämä on epäselvä vaiheessa 3, koska sana
tiedosto ei kerro, mikä tiedosto."*
• Yksi konkreettinen kohta. *"Koko juttu on liian pitkä"* → *"Vaiheet 4 ja 5 toistavat vaiheen
2."*
• Arvioi artefaktia, älä ihmistä.
• Ehdotus on vapaaehtoinen mutta tervetullut: *"ehkä vaiheet 4 ja 5 voisi yhdistää"*.

### Vinkki: hyvä palaute auttaa seuraavaa versiota syntymään. ---

## Tämän viikon tehtävät

• Tehtävä 4.1 - PAKOLLINEN (vähimmäistaso) - vertaisarviointi neljällä kriteerillä omasta viikon
2 tai viikon 3 artefaktista.
• Tehtävä 4.3 - SYVENTÄVÄ - varmuuskopiointitavat kriteeri kerrallaan (ammatillinen).
• Tehtävä 4.4 - SYVENTÄVÄ - help desk -makro: pitkä vs. lyhyt (ammatillinen, valinnainen
LLM-sparraus).
• Tehtävä 4.5 - SYVENTÄVÄ - uuden käyttäjän perehdytys: tili ensin vai kierros ensin
(ammatillinen).
• Säilytä vertaispalautteesi ja korjauksesi - niitä käytetään AT2:ssa viikon 5 lopussa / viikon 6
aikana.

### Tee näin: kirjoita palautteeseen aina kriteerin nimi. ---

## Seuraavaksi: Viikko 5 - logiikkarakenteet

Viikko 5 muuttaa oppitunnin 7 vinoneliön muodolliseksi ehdoksi, jossa on if / then / else, ja
esittelee silmukat: tee, katso, muuta, tee uudelleen.
Tällä viikolla harjoiteltu vertaisarvioinnin ja korjaamisen tapa on täsmälleen sitä, mitä AT2
kysyy - pidä muistiinpanot tallessa.

### Vinkki: koodin korjaaminen on samaa ajattelua kuin ohjeen korjaaminen. ---

## Kertaus - keskeinen viesti vielä kerran

> Useampi kuin yksi kelvollinen ratkaisu voi ratkaista saman ongelman. Niiden välillä
valitseminen ei ole makuasia - se perustuu nimettyihin kriteereihin.
Neljä kriteeriä: selkeys · tehokkuus · toistettavuus · virhealttius. Samat neljä nimeä. Sama
kiinteä järjestys. Kuvaile, älä arvosanota.
