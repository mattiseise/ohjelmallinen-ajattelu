# Viikko 5 — Kolme perusliikettä: järjestys, ehto ja toisto

## Viikon 5 sanasto

Alla olevat termit liittyvät oppitunteihin 13, 14 ja 15. Määritelmät ovat tarkoituksella lyhyitä —
katso esimerkit itseopiskelumateriaalista. Lopun termi (pseudokoodi) on ennakkokatsaus
viikkoon 6.

### Järjestys

Yhden vaiheen tekeminen toisen jälkeen kiinteässä järjestyksessä, ellei ohje sano muuta.
Järjestys on jokaisen prosessin oletusliike: kun mitään ehtoa tai toistoa ei ole kirjoitettu,
kirjaimellinen suorittaja kulkee vaiheet ylhäältä alas. Resepti ja julkaisutarkistuslista ovat
molemmat järjestyksiä.

### Vaihe

Yksi yksittäinen toiminto prosessissa. Hyvä vaihe on niin pieni, että kirjaimellinen suorittaja
voi toteuttaa sen ilman tarkentavaa kysymystä. “Laita vedenkeitin päälle” on vaihe; “tee
aamiainen” on kokonainen prosessi. (Viikolta 1 tuttu käsite, nyt samassa merkityksessä.)

### Järjestys (vaiheiden)

Kunkin vaiheen paikka vaihejonossa — mikä tulee ensimmäiseksi, toiseksi, kolmanneksi ja
niin edelleen. Järjestyksellä on merkitystä silloin, kun myöhemmät vaiheet riippuvat aiempien
vaiheiden tuloksista. Kiehuvan veden kaataminen ennen teepussin laittamista ei tuota samaa
juomaa kuin toinen järjestys.

### Riippuvuus

Kevyt, intuitiivinen ajatus siitä, että yksi vaihe tarvitsee aiemman vaiheen tuloksen ennen kuin
se voi alkaa. Veden keittäminen on riippuvuus veden kaatamiselle. Kaksi vaihetta, joilla ei ole
riippuvuutta toisiinsa, voivat joskus vaihtaa paikkaa prosessin rikkoutumatta; kaksi vaihetta,
joilla on riippuvuus, eivät voi.

### Ehto

Testi, joka päättää mikä vaihe tapahtuu seuraavaksi. Ehto on hetki prosessissa, jossa kulku
jakautuu kahteen tai useampaan reittiin. “Jos sataa, mene bussilla, muuten kävele” on kahden
haaran ehto; “jos maito haisee pahalta, heitä se pois” on yhden haaran ehto, jossa
vaihtoehtoista toimintaa ei ole kirjoitettu.

### Testi (ehdon osana)

Kysymys, jonka ehto esittää suorittajalle. “Onko salasana lyhyempi kuin 8 merkkiä?” ja “Sataako
nyt?” ovat testejä. Hyvä testi on sellainen, jonka kirjaimellinen suorittaja voi oikeasti tarkistaa;
huono testi (“myöhästynkö?”, “meneekö tämä pieleen?”) jättää tilaa arvailulle. (Viikolta 1 tuttu
käsite, nyt uudessa merkityksessä.)

### Haara

Yksi ehdon ulostuloreiteistä. Kahden haaran ehdolla on then-haara ja else-haara; kolmen
haaran rakenteessa voi olla lisäksi . Jokainen haara päättyy joko vaiheeseen (lehteen) tai `else if`
uuteen ehtoon (syvempään jakautumiseen).

### Päätöspuu

Kuva ehdoista tai ehtoketjusta. Juuri on ensimmäinen testi; jokainen haara on mahdollinen
vastaus; jokainen lehti on joko lopullinen vaihe tai uusi testi. Päätöspuun piirtäminen paperille
on nopein tapa nähdä, onko säännössä oikea määrä haaroja.

### Jos–niin

Ehdon lyhyempi muoto: jos X on totta, tee A. Vaihtoehtoista haaraa ei ole — jos X ei ole tosi,
suorittaja ei tee mitään ylimääräistä vaan jatkaa eteenpäin. “Jos saat läksyt tehtyä ennen
ruokaa, saat pelata” on jos–niin-rakenne.

### Jos–niin–muuten

Ehdon pidempi muoto: jos X on totta, tee A; muuten tee B. Suorittaja tekee aina jomman
kumman; muuten nimeää vaihtoehdon. “Jos sataa, mene bussilla, muuten kävele” on jos–niin–
muuten-rakenne.

### Toisto

Saman vaiheen tai vaihejoukon tekeminen useamman kuin yhden kerran siten, että mukana
on lopetusehto, joka kertoo milloin pitää lopettaa. Arkisessa IT-puheessa toistosta käytetään
myös sanaa silmukka — tällä kurssilla ne tarkoittavat samaa. “Merkitse jokainen nimi
läsnäololistaan” ja “jatka sekoittamista, kunnes sokeri on liuennut” ovat molemmat toistoja.

### Jokaiselle (for-each)

Toiston muoto, jossa käsiteltävien kohteiden lista on tiedossa etukäteen. “Merkitse jokainen
nimi rekisterissä läsnä tai poissa olevaksi.” Suorittaja tekee rungon kerran jokaista listan kohtaa
varten ja lopettaa, kun lista loppuu.

### Toista kunnes

Toiston muoto, jossa lopetus riippuu siitä, mitä matkan varrella tapahtuu. “Jatka sekoittamista,
kunnes sokeri liukenee.” Suorittaja tekee rungon, tarkistaa lopetusehdon ja joko pysähtyy tai
jatkaa.

### Niin kauan kuin (while)

Toiston muoto, jossa jatkumisehto tarkistetaan ennen jokaista kierrosta. “Niin kauan kuin
vedenkeitin on vielä kuuma, älä keitä sitä uudelleen.” Heti kun ehto ei enää ole totta, toisto
loppuu.

### Lopetusehto

Rehellinen, havaittava testi, joka päättää toiston. “Kunnes saapuneet-kansio on tyhjä” on
lopetusehto; “kunnes tuntuu valmiilta” ei ole, koska kukaan muu ei voi tarkistaa sitä. Jokainen
toisto tarvitsee lopetusehdon, jonka suorittaja voi oikeasti nähdä.

### Karkaava toisto

Toisto, jonka lopetusehto ei voi koskaan muuttua todeksi, joten suorittaja jatkaisi loputtomiin.
“Toista kunnes ymmärrät” on karkaava toisto, ellei ymmärtää muuteta joksikin havaittavaksi,
kuten “kunnes pystyt selittämään asian takaisin luokkakaverille yhdellä lauseella”. Rehellinen
lopetusehto on suoja karkaavaa toistoa vastaan.

### Pseudokoodi (ennakkokatsaus — viikon 6 keskeinen aihe)

Tiukempi, sääntöihin sidotumpi tapa kirjoittaa prosessikuvauksia paperille — lähempänä
koodia, mutta ei vielä varsinaista koodia. Viikko 5 pysyy löyhässä luonnollisessa kielessä.
Viikko 6 lisää muutaman pienen käytännön (sisennys, yksinkertaiset muuttujat,
seurantataulukko), jotka muuttavat tällä viikolla kirjoittamasi kuvaukset pseudokoodiksi.
Sinun ei tarvitse vielä osata pseudokoodia.
