# Useampi kuin yksi oikea vastaus — ratkaisujen vertailu

## Johdanto

Kuvittele kaksi ystävää, Maya ja Jonas, jotka tekevät teetä samassa keittiössä samana aamuna. Maya keittää ensin vedenkeittimellä veden, pudottaa sitten teepussin kuppiin ja kaataa vasta sen jälkeen. Jonas pudottaa teepussin kuppiin ensin, keittää sen jälkeen veden ja kaataa lopuksi. Molemmilla on lopulta juotavissa oleva kuppi teetä. Kumpikaan ei tee sitä väärin. He tekevät saman tehtävän kahdessa eri järjestyksessä.

Tähän yllätykseen viikko nojaa. Samaan ongelmaan — *tee juotava kuppi teetä* — on useampi kuin yksi oikea ratkaisu. Ne eroavat vaiheiden järjestyksen ja sen suhteen, mitä jokainen jättää tekijän harkintaan. Kumpikaan ei ole "oikea" abstraktilla tasolla.

Kuvittele nyt kaksi opiskelijaa kävelemässä koulusta kotiin. Toinen oikaisee puiston läpi, toinen kiertää pääkadun. Molemmat ovat suunnilleen yhtä nopeasti kotona. Kaksi pätevää reittiä — ja hiljainen päivittäinen valinta niiden välillä.

Viikon ydinviesti on yksi lause:

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Viikko 4 on **kurssin puolivälin reflektioviikko**. Uutta ohjelmallisen ajattelun perusrakennetta ei esitellä. Raaka-aineena on se, mitä jo rakensit viikoilla 1–3 — algoritmit, ositukset ja AT1, vuokaaviot ja nimetyt lohkot. Mitä lisäämme on tapa *katsoa* tätä työtä. **Oppitunti 10** osoittaa, ettei *"oikea"* ole ainutlaatuinen. **Oppitunti 11** nimeää neljä toimivaa **kriteeriä** — *selkeys*, *tehokkuus*, *toistettavuus*, *virhealttius*. **Oppitunti 12** ottaa kriteerit käyttöön jäsennellyssä **vertaisarviointi- ja revisiointiprotokollassa** todelliselle tuotokselle, jonka teit viikolla 2 tai 3.

Viikolla 4 ei ole AT-palautusta. **AT2 — prosessikuvaus** palautetaan viikon 5 lopussa / viikolla 6, ja vertaisarviointi-revisiointitottumus, jota tällä viikolla harjoittelet, on juuri se, mitä AT2 odottaa. Pidä muistiinpanosi tallessa.

Käytännön huomio. Emme **anna** ratkaisuille numeerisia arvosanoja tällä kurssilla. Neljä kriteeriä ovat *kuvailevia linssejä*, eivät 1–5-rubriikki. *"Resepti A on selkeämpi vaiheessa 3, koska…"* on oikea muoto. *"Resepti A saa 4/5 selkeydestä"* ei.

---

## Oppitunti 10 — Sama ongelma, useita ratkaisuja

### Ongelma ei ole sama asia kuin sen ratkaisu

**Ongelma** on sanoin ilmaistu tavoite: *tee juotava kuppi teetä*, *ehdi kouluun ajoissa*, *pidä palautettavissa oleva varmuuskopio projektikansiosta*. Ongelma kertoo, **mitä** haluat; se ei kerro, **miten** sinne pääsee.

**Ratkaisu** on yksi tapa saavuttaa tavoite — tietty vaiheiden sarja, jonka sananmukainen tulkitsija voi suorittaa. Useimmilla kiinnostavilla ongelmilla on useampi kuin yksi. Mayan tee ja Jonasin tee ovat kaksi ratkaisua samaan ongelmaan. Puistoreitti ja pääkadun reitti ovat kaksi ratkaisua *pääse kotiin* -ongelmaan.

**Pätevä ratkaisu** on sellainen, joka todella saavuttaa tavoitteen. Pätevyys on kyllä/ei-ominaisuus: joko tee on juotavaa tai ei ole, joko varmuuskopio on palautettavissa tai ei. Pätevyys ei kerro, *kuinka hyvin* ratkaisu tekee työnsä — se on, mihin oppitunnin 11 kriteerit ovat.

Viikon ensimmäinen liike on pieni mutta tärkeä. **Lopeta olettamasta, että on yksi oikea vastaus.** Ala odottaa kahta tai kolmea pätevää ratkaisua ja ala katsoa tarkasti, miten ne eroavat toisistaan.

### Kaksi pätevää ratkaisua rinnakkain (arkielämästä)

Kaksi teereseptiä. Sama tavoite: juotava kuppi teetä.

| Vaihe | Resepti A (keitä ensin) | Resepti B (hauduta ensin) |
|------|------------------------|---------------------------|
| 1 | Täytä vedenkeitin 250 ml:lla vettä | Laita yksi teepussi kuppiin |
| 2 | Keitä vesi | Täytä vedenkeitin 250 ml:lla vettä |
| 3 | Laita yksi teepussi kuppiin | Keitä vesi |
| 4 | Kaada keitetty vesi pussin päälle | Kaada keitetty vesi pussin päälle |
| 5 | Odota 3 minuuttia, poista pussi | Odota, kunnes väri näyttää oikealta, poista pussi |

Molemmat reseptit ovat viisivaiheisia. Molemmat tuottavat juotavan kupin teetä. Ne eroavat kahdella näkyvällä tavalla. Ensinnäkin vaiheiden 1–3 **järjestyksessä** — Resepti A keittää ennen pussin laittamista, Resepti B laittaa pussin ennen keittämistä. Toiseksi vaiheen 5 **lopettamisvihje** — Resepti A nimeää luvun (*3 minuuttia*), Resepti B nimeää väriarvion.

Ensimmäinen reaktio on usein *"no kumpi on oikein?"* — ja vastaus on *molemmat*. Kiinnostava kysymys ei ole, *kumpi* on oikein, vaan *miten* ne eroavat toisistaan.

### Kaksi pätevää ratkaisua rinnakkain (ICT)

Nyt ICT-vastine. Kaksi tapaa varmuuskopioida sama projektikansio. Sama tavoite: palautettavissa oleva kopio kansiosta.

| Vaihe | Tapa A (USB-kopio) | Tapa B (zip + sähköposti itselle) |
|------|----------------------|----------------------------------|
| 1 | Kytke USB-tikku läppäriin | Klikkaa projektikansiota hiiren oikealla |
| 2 | Avaa projektikansio läppärillä | Valitse *"Pakkaa .zip-tiedostoon"* |
| 3 | Valitse kaikki tiedostot (Ctrl+A) ja paina Ctrl+C | Odota, että zip-tiedosto ilmestyy kansion viereen |
| 4 | Avaa USB-tikku tiedostonhallinnassa | Avaa koulun sähköposti ja aloita uusi viesti |
| 5 | Paina Ctrl+V, odota kopioinnin valmistumista | Liitä zip-tiedosto viestiin |
| 6 | Irrota USB-tikku turvallisesti | Lähetä viesti omaan sähköpostiosoitteeseesi, tallenna *Varmuuskopiot*-kansioon |

Molemmissa on kuusi vaihetta. Molemmat tuottavat palautettavissa olevan kopion. Ne eroavat sen suhteen, missä kopio sijaitsee (fyysinen USB-tikku vs. sähköpostipalvelin), mitä siirretään (monta tiedostoa vs. yksi zip), ja millaisia vahinkoja tekijälle voi sattua.

Tämä on **viikon ammatillinen näkökulma**. Oikeassa 1. vuoden ICT-työssä päätetään, miten kansiollinen projektitiedostoja varmuuskopioidaan — yhtä virallista "oikeaa" tapaa ei ole, ja *mitä tapaa tänään käytetään* on juuri sellainen kysymys, johon kriteerit auttavat sinua vastaamaan.

### Mikä on sama, mikä eri?

Molemmissa esimerkkipareissa toistuvat samanlaiset erot:

- **Vaiheiden järjestys** eroaa (keitä ensin vs. pussi ensin; kopioi tiedostot vs. zippaa ensin).
- **Mitä jää tekijän tehtäväksi** eroaa (kolme minuuttia vs. väri; Ctrl+V vs. liitteen lisääminen sähköpostiin).
- **Mikä voi mennä pieleen** eroaa (pussin vetäminen liian aikaisin vs. USB-tikun irrottamatta jättäminen).
- **Mitä tapahtuu, kun syöte muuttuu** eroaa (Resepti B:n värivihje toimii edelleen vahvemmalla teellä; Tapa A käyttäytyy 500 pienen tiedoston kohdalla aivan eri tavalla kuin Tapa A yhden ison tiedoston kohdalla).

Mikään näistä eroista ei ole virhe. Kaikki ovat todellisia. Ne ovat se **muoto**, johon oppitunti 11 antaa sinulle sanaston.

> **Pysähdy hetkeksi:** Valitse yksi tuttu tehtävä, jonka teet useimpina päivinä — aamupala, kouluun valmistautuminen, päivän ensimmäiseen verkkokurssiin liittyminen. Kirjoita vaiheet kahdella tavalla. Keitä ensin vs. hauduta ensin. Sovellus ensin vs. selain ensin. Reppu selässä vs. reppu lattialla. Tavoittele kahta pätevää vaihtoehtoa, kummassakin viidestä kahdeksaan vaihetta. Älä vielä valitse voittajaa — huomaa vain, että molemmat toimivat ja että ne eivät ole sama.

---

## Oppitunti 11 — Ratkaisujen arviointikriteerit

### Mausta kriteeriin

Näin käy usein, kun esität luokalle kaksi pätevää ratkaisua. Joku sanoo *"pidän vain ensimmäisestä enemmän."* Joku toinen sanoo *"toinen on oikea tapa."* Kolmas kohauttaa olkapäitään. Mikään näistä reaktioista ei kerro kenellekään mitään hyödyllistä, koska kukaan ei nimeä, *mikä* tekee yhdestä ratkaisusta paremman *missä*. Kaikki ovat makua.

**Kriteeri** on nimetty mittapuu, joka muuttaa maun perusteluksi. Sen sijaan, että sanot *"pidän A:sta enemmän"*, sanot *"A on selkeämpi vaiheessa 5, koska *3 minuuttia* kertoo tekijälle täsmälleen, milloin pysähtyä."* Tämä lause nimeää ominaisuuden (*selkeys*), osoittaa tiettyyn paikkaan (*vaihe 5*) ja antaa konkreettisen syyn. Se on lause, josta voi kiistellä — tai jonka kanssa voi olla samaa mieltä — tuotoksen perusteella, ei sen perusteella, miltä tuntuu tänään.

Viikon ydinliike, kirjoitettuna vielä kerran:

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Siirryt muodosta *"pidän tästä enemmän"* muotoon *"tämä on parempi selkeydessä"*. *Mielipiteestä* muotoon *nimetty ominaisuus + tietty paikka*. Se on koko liike.

### Tämän kurssin neljä kriteeriä

Tällä kurssilla työskentelemme **neljällä** kriteerillä. Ne eivät ole ainoat kriteerit maailmassa — *kustannus*, *saavutettavuus*, *tietoturva* ovat olemassa oikeassa ICT-elämässä. Neljä riittää tottumuksen harjoitteluun. Ne esiintyvät tässä lukitussa järjestyksessä ensimmäisellä mainintakerralla: **selkeys**, **tehokkuus**, **toistettavuus**, **virhealttius**.

**Selkeys:** Kuinka helppoa ratkaisua on lukea kerran ja toimia sen mukaan ilman kysymyksiä. Selkeä ohje nimeää oikean vaiheen, oikean kohteen ja oikean seuraavan liikkeen; epäselvä jättää viikon 1 sananmukaisen tulkitsijan arvuuttelemaan. Arkielämästä: *"lisää teepussi"* on selkeämpää kuin *"lisää se juttu"*. ICT: *"tallenna tiedosto nimellä `2026-05-20_lasku.pdf` jaettuun asemaan"* on selkeämpää kuin *"tallenna se sinne, minne se kuuluu"*.

**Tehokkuus:** Kuinka vapaa ratkaisu on hukatuista vaiheista. Tehokas ratkaisu saavuttaa tavoitteen ilman kiertoteitä, kaksoissuoritusta tai uudelleentyötä — *ei hukattuja vaiheita*, ei pelkästään *nopea*. Arkielämästä: veden kuumentaminen kerran on tehokkaampaa kuin keittäminen, jäähdyttäminen ja uudelleenkeittäminen. ICT: kansion pakkaaminen kerran ja zipin lataaminen on tehokkaampaa kuin 500 tiedoston lataaminen yksi kerrallaan.

**Toistettavuus:** Kuinka luotettavasti ratkaisu tuottaa saman tuloksen toisella, kolmannella ja kymmenennellä kerralla, samalla syötteellä. Toistettava ratkaisu ei riipu tekijän mielialasta, muistista tai arvailusta. Arkielämästä: resepti, joka käyttää aina 200 ml:aa ja yhtä pussia, on toistettavampi kuin *"hieman vettä, maistele"*. ICT: varmuuskopio, joka pyörii tallennetusta tarkistuslistasta, on toistettavampi kuin sellainen, joka riippuu siitä, että muistaa, missä kansio tällä kuukaudella sijaitsee.

**Virhealttius:** Kuinka helppoa on tehdä *väärää* asiaa ratkaisua seuratessa. Matala virhealttius tarkoittaa vähän jalkaan-ampumisen tilaisuuksia; korkea virhealttius tarkoittaa, että seuraava ihminen linjalla on yhden lipsahduksen päässä väärästä lopputuloksesta. Arkielämästä: *"kaada kiehuva vesi pussin päälle ja anna olla kolme minuuttia"* on vähemmän virhealtis kuin *"kaada vesi päälle, laske vähän"*. ICT: varmuuskopio, joka nimeää päivämäärän tiedostonimeen, on vähemmän virhealtis kuin sellainen, joka kirjoittaa joka kerta saman `backup.zip`-tiedoston päälle.

Huomautus sanoista. Jotkut oppikirjat käyttävät *luettavuutta* selkeyden sijaan tai *kestävyyttä* matalan virhealttiuden sijaan. **Tällä kurssilla pidämme yllä olevat neljä nimeä**, tuossa lukitussa järjestyksessä ensimmäisellä mainintakerralla.

### Neljän kriteerin soveltaminen kahteen teereseptiin

Nyt takaisin oppitunnin 10 kahteen teereseptiin, tällä kertaa kriteerit linssinä.

| Kriteeri | Resepti A (keitä ensin) | Resepti B (hauduta ensin) |
|---|---|---|
| **Selkeys** | Vaihe 5 nimeää luvun (3 minuuttia). Sananmukainen tulkitsija pysähtyy oikeaan aikaan. | Vaihe 5 nimeää värin, joka tekijän on tiedettävä. Uusi tekijä voi pysähtyä liian aikaisin tai liian myöhään. |
| **Tehokkuus** | Viisi vaihetta, yksi keitto, yksi haudutus — ei hukattuja vaiheita. | Viisi vaihetta, yksi keitto, yksi haudutus — ei hukattuja vaiheita. |
| **Toistettavuus** | Sama 200 ml ja sama 3 minuuttia → sama juoma maanantaina ja perjantaina. | Sama vedenkeitin, sama väriarvio → juoma riippuu päivän silmästä. |
| **Virhealttius** | Vaikea mennä pieleen, jos tekijällä on kello. | Riski vetää pussi liian aikaisin tai liian myöhään, jos tekijä on tuore teejuomari. |

Lue solu solulta. Resepti A on **selkeämpi vaiheessa 5**, koska *3 minuuttia* kertoo tekijälle täsmälleen, milloin pysähtyä. Kaksi reseptiä ovat **yhtä tehokkaita** — sama vaiheiden määrä. Resepti A on **toistettavampi**, koska kello on sama maanantaina ja perjantaina, mutta väriarvio ei ole. Resepti A on myös **vähemmän virhealtis** uudelle tekijälle; kokeneelle teejuomarille ero kapenee.

Huomaa, mitä taulukko *ei* tee. Se ei anna Reseptille A pistemäärää 4/5. Se ei julista kokonaisvoittajaa. Se kulkee yhden kriteerin kerrallaan, sanoo yhden konkreettisen asian solua kohden ja pysähtyy siihen.

### Neljän kriteerin soveltaminen kahteen varmuuskopiotapaan

Nyt ICT-vastine. Kaksi varmuuskopiotapaa, neljä kriteeriä.

| Kriteeri | Tapa A (USB-kopio) | Tapa B (zip + sähköposti itselle) |
|---|---|---|
| **Selkeys** | Jokainen vaihe nimeää konkreettisen käyttöliittymätoiminnon (*kytke*, *valitse kaikki*, *paina Ctrl+V*, *irrota*). | Jokainen vaihe nimeää konkreettisen käyttöliittymätoiminnon (*oikea klikkaus*, *Pakkaa .zip:iin*, *liitä*, *lähetä itselle*). |
| **Tehokkuus** | Monta tiedostoa kopioidaan yksi kerrallaan — hidasta pienien tiedostojen kansiossa. | Yksi zip-tiedosto luodaan ja siirretään kerran — vähemmän hukattuja siirtoja. |
| **Toistettavuus** | Jos USB-tikku ei ole kytkettynä, prosessi pysähtyy; tulos riippuu siitä, että muistaa USB-tikun. | Sähköpostipalvelin on aina käytettävissä koulusta; sama prosessi toimii millä tahansa läppärillä. |
| **Virhealttius** | Helppo kirjoittaa vanhan varmuuskopion päälle, jos tekijä ei nimeä kohdekansiota uudelleen. | Jokainen sähköposti päivätään automaattisesti — aiempaa varmuuskopiota on vaikea hukata vahingossa. |

Lue poikittain, älä alaspäin. Tavat ovat suunnilleen **yhtä selkeitä** — molemmat nimeävät konkreettisia käyttöliittymätoimintoja. Tapa B on **tehokkaampi monien pienien tiedostojen kansion kohdalla** (yksi zip-siirto monen sijaan). Tapa B on **toistettavampi laitteiden välillä** (sähköpostipalvelin on aina paikalla; USB-tikku ei välttämättä ole). Tapa B on **vähemmän virhealtis** vanhojen varmuuskopioiden säilyttämisessä, koska jokainen sähköposti on päivätty eikä vanhaa kirjoiteta päälle.

Tämä on yksi vertailu, tämänkaltaiselle kansiolle. 50 GB:n videokansiolle kuva muuttuu — zip-vaihe hidastuu ja sähköposti ei ehkä hyväksy liitettä. **Vertailu riippuu syötteestä.**

### Kompromissit — kun kriteerit vetävät eri suuntiin

Kompromissi on tilanne, jossa kaksi kriteeriä vetävät eri suuntiin, niin että yhden parantaminen tarkoittaa toisen heikentämistä. Resepti B on **vähemmän selkeä vaiheessa 5**, mutta on **yhtä tehokas** kuin Resepti A, ja voi olla miellyttävämpi kokeneelle teejuomarille. Tapa A on **yksinkertaisempi selittää** ensimmäisenä päivänä (USB-tikku on jotain, jota voi pitää kädessä), mutta Tapa B on **tehokkaampi ja toistettavampi** päivittäisessä käytössä.

Kompromissit eivät ole ratkaistava ongelma — ne ovat vertailun *muoto*. Yleisin virhe on julistaa silti voittaja. Vastusta sitä. **Nimeä kompromissi.** *"Resepti A on selkeämpi; Resepti B on nopeampi sille, joka tietää, miltä teen pitäisi näyttää. Oikea valinta riippuu siitä, onko tekijä tehnyt tätä ennen."* Tuo lause on analyysi.

Yksittäisen ratkaisun ei tarvitse voittaa joka kriteerillä. Neljä kriteeriä ovat kuvailevia linssejä, eivät tulostaulu.

> **Pysähdy hetkeksi:** Ota yllä olevan ensimmäisen Pysähdy-kohdan O10-vaihtoehtoiset menettelysi. Rakenna neljärivinen taulukko — yksi rivi kriteeriä kohden. Täytä lyhyt lause soluun, nimeä tietty vaihe, kun voit. Sinua ei pyydetä valitsemaan voittajaa. Huomaa, mitkä kriteerit vetävät vastakkaisiin suuntiin.

> **Pysähdy hetkeksi:** Mieti ohjelmistoa, jota käytät useimpina päivinä — chat-sovellus, suoratoistopalvelu, koulun portaali. Valitse yksi ominaisuus, jolla on kaksi käyttötapaa (hakusanan kirjoittaminen vs. kategorian klikkaaminen; pikanäppäin vs. valikko). Kumpi on selkeämpi uudelle käyttäjälle? Kumpi on tehokkaampi päivittäiskäyttäjälle? Kummasta kriteeristä kehittäjä luultavasti välittää enemmän?

---

## Oppitunti 12 — Oman ratkaisun parantaminen ja vertaispalaute

### Miksi oma ratkaisu on vaikein nähdä selvästi

Viikolla 1 opit, että sananmukainen tulkitsija ottaa ohjeesi täsmälleen niin kuin kirjoitit ne. Vaikeus on, että **omassa päässäsi** oleva sananmukainen tulkitsija ei ole olemassa, kun luet omaa työtäsi uudelleen — pääsi tietää, mitä tarkoitit, ja täyttää hiljaa aukot. Luet *"tarkista tiedosto"* ja lisäät *"se Downloads-kansiossa, päivätty tänään"* huomaamatta. Lukijalla, joka ei ole sinä, ei ole tuota pään-täyttäjää.

Neljä kriteeriä ovat tapa lukea omaa työtäsi *jonkun toisen silmin*. Käymällä selkeyden, tehokkuuden, toistettavuuden ja virhealttiuden läpi yksi kerrallaan pakotat itsesi kysymään ne kysymykset, joita vieras kysyisi. Vielä parempi: oikea pari, joka lukee tuotostasi, esittää vielä tarkempia kysymyksiä, koska hän todella ei voi nähdä, mitä tarkoitit. **Siihen vertaisarviointi on.**

Tämä oppitunti on viikon työllinen oppitunti. Sen päätyttyä olet lukenut parin tuotoksen, kirjoittanut hänelle kaksi kriteerillä nimettyä palautetta, saanut palautetta takaisin ja **korjannut** yhden omista olemassa olevista viikon 2 tai 3 tuotoksistasi. Viikolla 4 ei luoda uutta tuotosta.

### Vertaisarviointiprotokolla (kriteerit → palaute → revisio)

Protokolla on kolmivaiheinen, tässä lukitussa järjestyksessä.

1. **Arvioija lukee parin tuotoksen hiljaa.** Kerran läpi, ilman puhumista, neljä kriteeriä mielessä. Arvioija kirjoittaa sitten **yhden lauseen kriteeriä kohden** lukitussa järjestyksessä — selkeys, tehokkuus, toistettavuus, virhealttius. Jokainen lause on joko *"Vahva X:ssä, koska…"* tai *"Voisi parantua X:ssä, koska…"*, nimeää kriteerin ja osoittaa tiettyyn vaiheeseen tai lohkoon.

2. **Arvioija luovuttaa yhteensä kaksi palautetta** — ei neljää. Neljästä kirjoittamastaan lauseesta hän valitsee *kaksi hyödyllisintä* ja antaa ne tekijälle. Kumpikin nimeää kriteerin.

3. **Tekijä korjaa sitten tuotosta** toimiakseen ainakin yhden kahdesta palautteesta mukaan. Revisio on muutos alkuperäiseen — ei aivan uusi tuotos eikä alusta-uudelleenkirjoitus. Tekijä kirjoittaa 3–5 lauseen **muutosmuistion**, jossa nimetään, mikä muuttui ja mikä kriteeri ohjasi muutosta.

Tämä on koko protokolla. Kaksi palautetta sisään, yksi revisio ulos, yksi muutosmuistio, joka nimeää kriteerin. Muoto pysyy samana luokassa parin kanssa, yksin 24 tunnin vanhan itsesi kanssa ja (viikolla 5/6) AT2:n sisällä.

### Palaute, jota joku voi todella käyttää

Kolme lyhyttä sääntöä mille tahansa kriteerillä nimetylle palautteelle.

- **Nimeä aina kriteeri.** *"Tämä on epäselvää"* on makua valeasussa. *"Tämä on epäselvää vaiheessa 3, koska sana *tiedosto* ei kerro, mistä tiedostosta on kyse"* on lause, johon tekijä voi tarttua.
- **Yksi konkreettinen kohta, ei yleinen vaikutelma.** *"Kokonaisuus on liian pitkä"* ei johda toimintaan. *"Vaiheet 4 ja 5 toistavat vaihetta 2"* osoittaa tiettyyn paikkaan.
- **Ehdotus on valinnainen mutta tervetullut.** *"Ehkä voisit yhdistää vaiheet 4 ja 5 muuhun"* on hyödyllinen. On ihan sopivaa jättää *miten* tekijälle; tärkeintä on, että *mitä* on nimetty.

Ja yksi sääntö, joka menee kaikkien kolmen alle: **kritisoi tuotosta, älä ihmistä.** *"Tämä vaihe on epäselvä"* on palautetta. *"Sinä olet epäselvä"* ei ole.

### Palautteen vastaanottaminen, kun et ole samaa mieltä

Sinun ei ole pakko toimia jokaisen palautteen mukaan. Sinun **on** harkittava se ja kyettävä sanomaan, mihin kriteeriin se viittaa ja miksi se ei mielestäsi päde tässä. *"Pari sanoi, että vaihe 3 on epäselvä, mutta vaihe 3 nimeää tarkan tiedoston. Selkeyskriteeri on tässä kunnossa."* Tämä on hyvä syy pitää vaihe 3 ennallaan — se on kriteerillä nimetty ja rehellinen.

Mitä et saa tehdä, on **puolustaa** tuotostasi suoran kyselytuokion aikana. Kyselytuokio on palautteen **selventämistä** varten (*"tarkoitatko vaihetta 3 vai vaihetta 4?"*), ei väittelyä. Päätös toimia tai hylätä palaute tehdään revisiovaiheessa, ei vaihdossa.

### Katse AT2:ta kohti

**AT2 — prosessikuvaus** osuu viikon 5 lopulle / viikolle 6. AT2 pyytää sinua kuvaamaan prosessin kirjallisesti, antamaan sen parille, vastaanottamaan palautetta ja **korjaamaan sen** ennen palautusta. Tämä on täsmälleen sama kierros, jota harjoittelit viikolla 4.

Pidä kaksi asiaa tästä viikosta:

- Kaksi kriteerillä nimettyä palautetta, jotka sait viikon 2 tai 3 tuotoksestasi.
- Revisiosi ja 3–5 lauseen muutosmuistio.

AT2 pyytää sinua **toistamaan saman kierroksen viikon 5/6 tuotokselle**. Sanasto — *kriteeri*, *selkeys*, *tehokkuus*, *toistettavuus*, *virhealttius*, *kompromissi*, *revisio* — on täsmälleen sitä, mitä AT2 odottaa.

> **Pysähdy hetkeksi:** Avaa nyt viikon 2 osituksesi (AT1) tai viikon 3 vuokaaviosi. Kävele neljä kriteeriä mielessäsi — selkeys ensin, sitten tehokkuus, sitten toistettavuus, sitten virhealttius — ja kirjoita itsellesi yksi kriteerillä nimetty kommentti kustakin. Ympyröi sitten kaksi hyödyllisintä. Ne ovat ne kaksi palautetta, jotka 24 tunnin vanha itsesi antaisi sinulle. Osoittaako jokin niistä tiettyyn vaiheeseen, jota voisit korjata aloittamatta alusta?

---

## Yhteenveto ja mitä seuraavaksi

Viikko 4 lisäsi yhden tottumuksen olemassa olevien tuotostesi päälle. Opit, että saman ongelman voi ratkaista useammalla kuin yhdellä pätevällä menettelyllä (O10), että neljä nimettyä kriteeriä — **selkeys, tehokkuus, toistettavuus, virhealttius** — muuttavat maun perusteluksi (O11), ja että jäsennelty vertaisarviointi- ja revisiokierros oikealle, jo tehdylle tuotokselle on oman työn parantamisen moottori (O12). Ei uutta primitiiviä. Ei koodia. Ei arvosanoja. Vain terävämpi tapa katsoa edessäsi olevaa työtä.

Viikon ydinviesti, vielä kerran, sanasta sanaan:

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Jos osaat nimetä neljä kriteeriä, vertailla kahta lyhyttä ratkaisua kriteeri kerrallaan kirjallisesti, antaa parille kaksi kriteerillä nimettyä palautetta ja korjata yhden omista tuotoksistasi 3–5 lauseen muutosmuistion kanssa, olet tehnyt sen liikkeen, johon viikko 4 valmensi.

**Viikolla 5** kysymys muuttuu jälleen. Viikko 5 esittelee **logiikkarakenteet**: O7:n vinoneliö muuttuu muodolliseksi **ehdoksi** (*if / then / else*) ja uusi primitiivi saapuu — **silmukka** (tee, katso, muuta, tee uudelleen). Silmukkaa kutsutaan myös *iteraatioksi*, ja vertaisarviointi- ja revisiokierros, jota tällä viikolla harjoittelit, on sen aivan ensimmäinen versio. AT2 osuu viikon 5 lopulle / viikolle 6. Tällä viikolla pitämäsi muistiinpanot uudelleenkäytetään siellä.
