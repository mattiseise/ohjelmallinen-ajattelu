# Sanasto

## Viikon 5 sanasto

Alla olevat termit kattavat oppitunnit 13, 14 ja 15. Määritelmät ovat tarkoituksella lyhyitä — lue itseopiskelumateriaali esimerkkien näkemiseksi kontekstissa. Yksi termi lopussa (*pseudokoodi*) on esikatsaus viikolle 6, ja se on merkitty sellaiseksi.

### Sekvenssi
Yhden vaiheen tekemistä toisensa perään, kiinteässä järjestyksessä, ellei ohje toisin sano. Sekvenssi on oletusarvoinen liike missä tahansa prosessissa: kun mitään ehtoa ja mitään toistoa ei ole kirjoitettu, sananmukainen tulkitsija käy vaiheet läpi ylhäältä alas. Resepti ja käyttöönottolista ovat molemmat sekvenssejä.

### Vaihe
Yksi yksittäinen toiminta prosessissa. Hyvä vaihe on tarpeeksi pieni, jotta sananmukainen tulkitsija pystyy suorittamaan sen ilman tarkentavaa kysymystä. "Kytke keitin päälle" on vaihe; "tee aamupala" on kokonainen prosessi. (Palautettu viikolta 1, käytetään samalla tavalla.)

### Järjestys
Kunkin vaiheen sijainti sekvenssissä — mikä vaihe tulee ensin, toisena, kolmantena ja niin edelleen. Järjestys merkitsee, kun myöhemmät vaiheet riippuvat aiempien vaiheiden tuloksesta; kiehuvan veden kaataminen ennen teepussin laittoa ei ole sama juoma kuin toisinpäin.

### Riippuvuus
Kevyt, intuitiivinen ajatus siitä, että yksi vaihe tarvitsee aiemman vaiheen tuloksen voidakseen suorittua. Veden kiehauttaminen on sen kaatamisen riippuvuus. Kaksi vaihetta, joiden välillä ei ole riippuvuutta, voidaan joskus vaihtaa rikkomatta prosessia; kahta riippuvuuden omaavaa vaihetta ei voi.

### Ehto
Testi, joka päättää, mikä vaihe tapahtuu seuraavaksi. Ehto on se prosessin hetki, jolloin polku jakautuu kahteen (tai useampaan). "Jos sataa, mene bussilla, muuten kävele" on ehto kahdella haaralla; "jos maito haisee, heitä se pois" on ehto yhdellä haaralla ja ilman vaihtoehtoa.

### Testi (osana ehtoa)
Kysymys, jonka ehto esittää tulkitsijalle. *"Onko salasana lyhyempi kuin 8 merkkiä?"* ja *"Sataako nyt?"* ovat testejä. Hyvä testi on jotain, mitä sananmukainen tulkitsija pystyy oikeasti tarkistamaan; huono testi (*"olenko myöhässä?"*, *"meneekö pieleen?"*) jättää tulkitsijan arvailemaan. (Palautettu viikolta 1 uudessa merkityksessä.)

### Haara
Yksi ehdosta lähtevistä poluista. Kaksihaaraisella ehdolla on *then*-haara ja *else*-haara; kolmihaarainen ehto lisää `else if`-haaran. Jokainen haara päättyy joko vaiheeseen (lehti) tai uuteen ehtoon (syvempi jako).

### Päätöspuu
Kuva ehdosta (tai ehtoketjusta). Juuri on ensimmäinen testi; jokainen haara on mahdollinen vastaus; jokainen lehti on joko lopullinen vaihe tai uusi testi. Päätöspuun piirtäminen paperille on nopein tapa nähdä, onko säännössä oikea määrä haaroja.

### If-then
Ehdon lyhyempi muoto: *jos X on tosi, niin tee A.* Vaihtoehtoa ei ole — jos X on epätosi, tulkitsija ei tee mitään ylimääräistä ja jatkaa eteenpäin. *"Jos saat läksyt valmiiksi ennen päivällistä, voit pelata"* on if-then.

### If-then-else
Ehdon pidempi muoto: *jos X on tosi, niin tee A; muuten tee B.* Tulkitsija tekee aina jommankumman; *else* nimeää vaihtoehdon. *"Jos sataa, mene bussilla, muuten kävele"* on if-then-else.

### Toisto
Saman vaiheen tai vaihejoukon tekemistä useammin kuin kerran, lopetusehdon kanssa, joka kertoo tulkitsijalle, milloin pysähtyä. Toistoa kutsutaan arkisessa tekniikkapuheessa myös *silmukaksi* — molemmat sanat tarkoittavat samaa asiaa tällä kurssilla. "Merkitse jokainen nimi luettelosta" ja "jatka sekoittamista, kunnes sokeri liukenee" ovat molemmat toistoja.

### For-each
Toiston muoto, jossa kohteiden lista on tiedossa etukäteen. *"Jokaiselle nimelle luettelossa, merkitse läsnä tai poissa."* Tulkitsija tekee sisävaiheen kerran jokaiselle listan kohteelle ja pysähtyy, kun lista on lopussa.

### Repeat-until
Toiston muoto, jossa lopetus riippuu siitä, mitä tapahtuu. *"Jatka sekoittamista, kunnes sokeri liukenee."* Tulkitsija tekee sisävaiheen, tarkistaa lopetusehdon ja joko pysähtyy tai toistaa.

### While
Toiston muoto, jossa jatkamisehto tarkistetaan *ennen* jokaista toistoa. *"Niin kauan kuin keitin on vielä kuuma, älä keitä sitä uudelleen."* Heti kun ehto lakkaa olemasta tosi, tulkitsija lakkaa toistamasta.

### Lopetusehto
Rehellinen, havaittavissa oleva testi, joka päättää toiston. "Kunnes sähköposti on tyhjä" on lopetusehto; "kunnes tuntuu valmiilta" ei ole, koska kukaan muu ei pysty tarkistamaan sitä. Jokainen toisto tarvitsee lopetusehdon, jonka tulkitsija pystyy oikeasti näkemään.

### Karannut toisto
Toisto, jonka lopetusehto ei voi koskaan toteutua, joten tulkitsija jatkaisi ikuisesti. *"Toista, kunnes ymmärrät"* on karannut toisto, ellei "ymmärrät"-sanaa korvata jollakin havaittavalla (esim. "kunnes pystyt selittämään sen luokkatoverille yhdellä lauseella"). Turvavyö karanneita toistoja vastaan on rehellinen lopetusehto.

### Pseudokoodi *(katse eteenpäin — viikon 6 keskeinen aihe)*
Tiukempi, sääntöihin sitovampi tapa kirjoittaa prosessikuvauksia paperille — lähempänä koodia, mutta ei vielä koodia. Viikko 5 pysyy löyhässä luonnollisessa kielessä. Viikko 6 lisää muutaman pienen konvention (sisennys, yksinkertaisia muuttujia, käsiajotaulukon), jotka muuttavat tällä viikolla kirjoittamasi kuvaukset pseudokoodiksi. Sinun ei tarvitse vielä tuntea pseudokoodia.
