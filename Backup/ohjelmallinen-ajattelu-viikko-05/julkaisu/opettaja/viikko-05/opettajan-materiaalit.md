# Viikko 5 — Opettajan materiaalit

Tämä asiakirja kattaa kaikki viikon 5 kolme oppituntia (O13, O14, O15) yhdessä paikassa. Se rakentuu saman keskeisen viestin ympärille, jonka opiskelijat näkevät: **"Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto."** Viikko 5 nimeää ne kolme logiikkarakennetta, joista jokainen kuvattu prosessi koostuu, ja harjoittaa opiskelijan tunnistamaan ne arkipuheessa *ennen* niiden kohtaamista koodina viikoilla 6–8. Viikko 5 on myös välitön perustusviikko **AT2:lle**, joka palautetaan viikon 5 lopussa / viikon 6 aikana ja pyytää prosessikuvausta, joka käyttää kaikkia kolmea rakennetta selvästi. Kolme oppituntia muodostavat yhden kaaren — O13 nimeää *oletusarvon* (sekvenssi), O14 nimeää *testin, joka jakaa polun* (ehto), O15 nimeää *testin, joka kierrättää polkua* (toisto lopetuksen kanssa).

Koodia ei tällä viikolla esitellä. Pseudokoodimainen merkintä (`if … then … else …`, `for each …`, `repeat until …`) on sallittu, mutta sitä käsitellään englanninkielisenä lyhennemerkintänä, ei muodollisena kielenä. Varsinainen pseudokoodi tulee viikolla 6.

Ristiviittaukset: oppitunneilla 14 ja 15 käytetyt tuntiaktiviteetit kuvataan tiedostossa `tuntitehtavat.md` samassa kansiossa.

---

## Viikon 5 oppimistavoitteet (kytkettynä Bloomiin)

Viikko 5 pysyy **Muistamisen** ja **Ymmärtämisen** sisällä, ja **kevyt Soveltaminen** on sallittu kaikilla kolmella oppitunnilla (ilmaise ehto muodossa `if … then … else …`; ilmaise toisto selkeällä lopetuksella; piirrä pieni päätöspuu; yhdistä kaikki kolme rakennetta yhdeksi prosessikuvaukseksi). Viikon 5 tavoitteissa kielletyt verbit ovat *luo, rakenna, suunnittele, kehitä, arvioi, tuomitse, debuggaa, optimoi, hajota*. *Analysoida* saa esiintyä kevyesti syventävissä tehtävissä mutta ei tavoitteissa. Kurssin korkeammat Bloom-tasot palaavat myöhemmillä viikoilla.

### Oppitunti 13 — Sekvenssi: ohjelma etenee vaihe vaiheelta

- **Muistaminen:** opiskelija osaa **määritellä** *sekvenssin* omin sanoin "yhden vaiheen tekemiseksi toisensa perään, kiinteässä järjestyksessä".
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** sekvenssirungon arkisessa prosessissa (resepti, käyttöönottolista, aamurutiini).
- **Ymmärtäminen:** opiskelija osaa **selittää**, miksi vaiheiden järjestys yleensä merkitsee, ja antaa yhden esimerkin, jossa kahden vaiheen vaihtaminen rikkoo prosessin.
- **Kevyt Soveltaminen:** opiskelija osaa **kirjoittaa** 6–10 vaiheen sekvenssin tutusta prosessista niin, että järjestys on tehty näkyväksi numeroinnilla.

### Oppitunti 14 — Ehdot: if-then-else -ajattelu ja päätöspuut

- **Muistaminen:** opiskelija osaa **määritellä** *ehdon* omin sanoin "testiksi, joka päättää, mikä vaihe tapahtuu seuraavaksi".
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** `if … then … else …` -muodon arkisista säännöistä (salasanasäännöt, tikettien reititys, *"jos sataa, mene bussilla"*).
- **Ymmärtäminen:** opiskelija osaa **selittää** eron `if … then …` (ei vaihtoehtoa) ja `if … then … else …` (vaihtoehto) välillä.
- **Kevyt Soveltaminen:** opiskelija osaa **piirtää** yksinkertaisen kaksi- tai kolmehaaraisen päätöspuun tutusta arkisesta säännöstä.
- **Kevyt Soveltaminen:** opiskelija osaa **ilmaista** tositilanteen säännön luonnollisella `if … then … else …` -muodossa.

### Oppitunti 15 — Toisto: saman asian tekeminen monta kertaa

- **Muistaminen:** opiskelija osaa **määritellä** *toiston* omin sanoin "saman vaiheen tai vaihejoukon tekemisenä useammin kuin kerran, selkeällä lopetuksella".
- **Ymmärtäminen:** opiskelija osaa **erottaa** *for each* (tunnettu lista), *repeat until* (lopetusehto) ja *while* (jatkamisehto) arkisissa tilanteissa.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** toiston tutuissa prosesseissa (sähköpostien läpikäynti, läsnäolon merkitseminen, puhelimen lataaminen).
- **Kevyt Soveltaminen:** opiskelija osaa **ilmaista** tositilanteen toistuvan toiminnon luonnollisella kielellä selkeällä lopetus- tai jatkamisehdolla.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** eron kerralleen tehtävän vaiheen ja toistuvan vaiheen välillä prosessikuvauksessa.

---

## Yleisiä virhekäsityksiä viikolle 5

Vähintään kaksi virhekäsitystä per oppitunti tulee tässä. Ennakoi niitä, missä se sopii luontevasti — useimmat nousevat itse esiin itsenäisen työskentelyn lohkossa tai luokitteluleikissä.

### Oppitunnin 13 virhekäsitykset

**Virhekäsitys:** "Sekvenssi on liian itsestäänselvä laskettavaksi rakennuspalikaksi."
**Korjaus:** Suurin osa todellisista bugeista tulee yhdestä vaihdetusta vaiheesta. Sekvenssi on *oletusarvo* — kirjoitetun haaran tai silmukan puuttuminen — ja oletusarvossa asiat menevät rikki, koska kukaan ei ajattele testata sitä. Se on perusta, jonka päällä muut kaksi rakennetta istuvat.

**Virhekäsitys:** "Jos en kirjoita ehtoa, prosessissa ei ole päätöksiä."
**Korjaus:** Se tarkoittaa, että jokainen vaihe on ehdoton — jokainen vaihe tapahtuu aina, kirjoitetussa järjestyksessä. Sekvenssi on *haarautumisen puute*, ei tärkeyden puute. Kuusi vaihetta sisältävä sekvenssi ilman ehtoja on silti täydellinen prosessi.

### Oppitunnin 14 virhekäsitykset

**Virhekäsitys:** "`if … then …` on sama kuin `if … then … else …`."
**Korjaus:** Ilman `else`-haaraa tulkitsija ei tee mitään ylimääräistä muutoin. `else`-haaran kanssa tulkitsija tekee jotain muuta epätosi-haarassa. *"Jos maito haisee, heitä se pois"* ja *"Jos maito haisee, heitä se pois; muuten kaada se kahviisi"* eivät ole sama ohje.

**Virhekäsitys:** "Yhdistetyt ehdot ovat edistynyttä ja minun pitäisi välttää niitä."
**Korjaus:** Opiskelijat käyttävät AND-sanaa ja OR-sanaa joka päivä — *"jos minulla on kortti JA siinä on rahaa, voin mennä bussilla"*. Vain *symbolit* ovat edistynyttä; *ajattelu* ei ole. Yhdistetyt ehdot pysyvät selkokielisessä muodossa viikolla 5; symbolista logiikkaa ei näy lainkaan.

### Oppitunnin 15 virhekäsitykset

**Virhekäsitys:** "Silmukka on vain sekvenssi, joka on kirjoitettu monta kertaa."
**Korjaus:** Silmukka on yksi lause ja lopetusehto. Jos kirjoitat *"tarkista seuraava valokuva, tarkista seuraava valokuva …"* 100 kertaa, et ole ymmärtänyt toistoa. `for each` ja `repeat until` sanovat *"sama asia, uudelleen, selkeällä lopetuksella"* yhdellä rivillä.

**Virhekäsitys:** "`repeat until` pysähtyy aina."
**Korjaus:** Se pysähtyy, jos ja vain jos lopetusehto pystytään oikeasti havaitsemaan ja saavuttamaan. *"Toista, kunnes ymmärrät"* ei ole lopetus — sananmukainen tulkitsija ei pysty sitä tarkistamaan. Rehelliset toistot tarvitsevat havaittavissa olevan lopetuksen, ja monet myös *turvalopetuksen* (*"…tai pysähdy 10 yrityksen jälkeen"*) karannutta tapausta varten.

**Bonus-virhekäsitys:** "`for each` on eräänlainen sekvenssi, koska se on vain lista vaiheita."
**Korjaus:** `for each` on toisto — *sama* vaihe tehtynä kerran per kohde. Lista on lopetus: tulkitsija pysähtyy, kun kohteita ei ole enää. Yksi lause, ei monta.

---

## Oppitunti 13 — 90-minuutin suunnitelma

**Aihe.** Sekvenssi: ohjelma etenee vaihe vaiheelta.

**Tämän oppitunnin keskeinen viesti (yksi lause).** Sekvenssi on oletusarvo — kun mitään muuta ei sanota, *tee A, sitten B, sitten C* on se, mitä sananmukainen tulkitsija tekee, joten kirjoittamasi järjestys on se järjestys, jonka saat.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: luokka nimeää kolme arkista sekvenssiä ääneen (todennäköiset vastaukset: teeresepti, aamurutiini, koulumatka). Opettaja kirjoittaa ne taululle, sitten **vaihtaa kaksi vaihetta** yhdessä niistä (esim. *"kaada kiehuva vesi ennen teepussin laittoa"*) ja kysyy luokalta, mitä tapahtuu. | Koko luokka |
| 0:10–0:25 | Opettajan input: määrittele *sekvenssi*; käy yksi arkinen sekvenssi (tee tai aamurutiini) ja yksi ICT-sekvenssi (käyttöönottolista selkokielellä) rinnakkain. Nimeä *järjestys* ja *riippuvuus* epämuodollisesti. | Luento |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija kirjoittaa 6–10 vaiheen sekvenssin tutusta prosessista, jota he oikeasti tekevät, numeroiden jokaisen vaiheen. He nimeävät selvästi **tavoitteen**, **syötteen** ja **tulosteen** alkuun. Tämä on avaussiirto tehtävälle 5.1 — ehdot ja toisto lisätään O14:ssä ja O15:ssä. | Itsenäinen |
| 0:55–1:15 | Paritehtävä: opiskelijat vaihtavat sekvenssejä ja yrittävät **rikkoa** parin prosessin vaihtamalla kaksi vaihetta, joiden pari ajattelee voivansa silti toimia. Kirjoittaja merkitsee jokaisen vaihdon *"järjestys merkitsee"* tai *"järjestys ei merkitse"*. | Pari |
| 1:15–1:25 | Koko luokan purku: kerää 2–3 tapausta, joissa järjestys oikeasti merkitsi; rakenna "järjestys merkitsee / järjestys ei merkitse" -kaksisarakkeinen taulu. Yhdistä O13:n keskeiseen viestiin. | Koko luokka |
| 1:25–1:30 | Päätös: yhden rivin esikatsaus oppitunnille 14 — *"Seuraavaksi nimeämme hetken, jolloin prosessi jakautuu kahtia."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** O13 ei käytä mitään tuntiaktiviteettia tiedostosta `tuntitehtavat.md`. Paritehtävä on paikallinen tälle oppitunnille. Aktiviteetti A (luokitteluleikki) alkaa O14:ssä.

**Mitä sanot ääneen.** *"Sekvenssi on helpoin kolmesta rakennuspalikasta — ja eniten aliarvioitu, koska kukaan ei huomaa sitä ennen kuin se menee rikki. Katsokaa, mitä tapahtuu, kun vaihdan kaksi vaihetta."* Vaihda kaksi vaihetta teereseptissä (kaada vesi ennen teepussia). Pidä tauko. *"Tulkitsija teki täsmälleen sen, mitä uusi järjestys sanoi — ja tee on väärin. Sekvenssi on oletusarvo; oletusarvossa bugit piileksivät."*

**Materiaalit.** Taulu ja tussi; paperia ja kyniä; teknologiaa ei tarvita.

**Kalvovihjeet — päälinen kalvosarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** ei kalvoja. Taulu kantaa kolme sekvenssiä ja vaihdetun version.
- **Luento (0:10–0:25):** päälinen kalvosarja, kalvot **4 → 6**: *Sekvenssi — oletusarvoinen liike* · *Kun järjestys merkitsee* · *Sekvenssi työssä — käyttöönottolista*. Vietä eniten aikaa kalvolla 5; vaihto on se, missä oppi laskeutuu.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **4** näytölle hiljaisena muistutuksena tavoite–syöte–vaiheet–tuloste-rakenteesta, joka kannetaan viikolta 1.
- **Paritehtävä (0:55–1:15):** ei kalvoja; parit työskentelevät paperilla.
- **Purku (1:15–1:25):** ei kalvoja. Käytä taulua "järjestys merkitsee / järjestys ei merkitse" -kaksisarakkeiseen keräykseen.
- **Päätös (1:25–1:30):** ei kalvoja.

---

## Oppitunti 14 — 90-minuutin suunnitelma

**Aihe.** Ehdot: if-then-else -ajattelu ja päätöspuut.

**Tämän oppitunnin keskeinen viesti (yksi lause).** Ehto on testi, joka jakaa prosessin polun kahtia (tai useampaan), ja testin nimeäminen selkokielellä riittää tekemään jaon näkyväksi sananmukaiselle tulkitsijalle.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: opettaja kirjoittaa taululle suullisen arkisäännön — *"Jos sataa, mene bussilla, muuten kävele."* Luokka piirtää puun paperille 2 minuutissa. Opettaja piirtää kanonisen version taululle jälkeenpäin. | Koko luokka |
| 0:10–0:30 | Opettajan input: määrittele *ehto*; käy läpi `if … then …`, `if … then … else …` ja `if … then … else if … then … else …`. Käy yksi päätöspuu päästä päähän (sateenvarjosääntö). **Jos lisäkalvosarja `kalvot-o14-paatospuut.md` toimitetaan, aja se täällä kokonaan.** | Luento |
| 0:30–0:57 | **Itsenäinen työ** (27 min): jokainen opiskelija laajentaa O13-sekvenssiään lisäämällä vähintään yhden ehdon `if … then … else …` -testillä, joka on nimetty selkokielellä. He piirtävät myös ehdon pieneksi puuksi. | Itsenäinen |
| 0:57–1:20 | **PAKOLLINEN opettajavetoinen tuntiaktiviteetti** — *"Etsi if"* (Aktiviteetti A:n ensimmäinen puolikas tiedostossa `tuntitehtavat.md`, ~23 min). Opettaja lukee lyhyitä arki/ICT-lauseita; luokka äänestää *ehto / ei ehtoa* ja nimeää testin. Rajatapaukset uudelleenkirjoitetaan taululle. | Koko luokka |
| 1:20–1:28 | Koko luokan purku: mitkä lauseet olivat vaikeimpia luokitella? Missä testi oli piilossa arkisen sanamuodon taakse? | Koko luokka |
| 1:28–1:30 | Päätös: yhden rivin esikatsaus oppitunnille 15 — *"Seuraavaksi nimeämme hetken, jolloin vaihe tapahtuu useammin kuin kerran."* | Koko luokka |

**Itsenäisen työn lohko: 27 minuuttia (30 % 90 minuutista).** Täyttää 30–50 %:n säännön alarajalla. Suojaa tätä lohkoa — jos luento venyy, leikkaa luentoa, ei itsenäistä työtä.

**Ristiviittaukset.** 57–80 minuutin slot on Aktiviteetti A:n ensimmäinen puolikas tiedostossa `tuntitehtavat.md` (*Etsi if*). Pino 1 kyseisestä tiedostosta on valmisteltava etukäteen. Jos haluat ajaa Aktiviteetti B:n (*Live-päätöspuu taululle*) osana luentoa, vaihda se 30–55 min slottiin ja lyhennä itsenäisen työn osuutta 5 minuutilla kompensoinniksi (mutta **älä mene alle 27 minuutin**).

**Mitä sanot ääneen.** *"Ehto on testi, joka jakaa polun. Jos testi on tosi, tulkitsija menee yhteen suuntaan; jos ei, toiseen — tai ilman else-haaraa tulkitsija vain jatkaa. Kolme asiaa tekee hyvän ehdon: rehellinen testi, jonka tulkitsija pystyy oikeasti tarkistamaan, nimetty toiminta tosi-haarassa ja nimetty toiminta — tai selkeä 'ei mitään ylimääräistä' — epätosi-haarassa."* Käy sateenvarjosääntö taululla: *"jos juuri nyt sataa, ota sateenvarjo; muuten jos ennuste lupaa sadetta, ota sateenvarjo; muuten jätä kotiin."* Piirrä kolmehaarainen puu.

**Materiaalit.** Taulu ja tussi; paperia ja kyniä; Pino 1 tiedostosta `tuntitehtavat.md` valmistettuna lappuina tai tulostettuna listana. Jos toimitat `kalvot-o14-paatospuut.md`, pidä se valmiina näytöllä luento-osuutta varten.

**Kalvovihjeet — päälinen kalvosarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **7** (*Ehto — testi, joka jakaa polun*) näytöllä, kun luokka piirtää sateenvarjopuun paperille.
- **Luento (0:10–0:30):** päälinen kalvosarja, kalvot **7 → 10**: *Ehto — testi, joka jakaa polun* · *`if … then … else …`* · *Päätöspuu — jakautumisen piirtäminen* · *Ehto työssä — salasanan tarkistus*. **Jos lisäkalvosarja toimitetaan, aja `kalvot-o14-paatospuut.md` päästä päähän päälisen kalvojen 9 ja 10 välissä** — se käy sateenvarjopuun hitaasti ja peilaa sen ICT-loginiin.
- **Itsenäinen työ (0:30–0:57):** jätä kalvo **8** näytölle hiljaiseksi viitteeksi `if … then … else …` -muodosta.
- **Tuntiaktiviteetti (0:57–1:20):** ei kalvoja. Luokitteluleikki elää taululla.
- **Purku (1:20–1:28):** ei kalvoja; puhu rajatapauksista taulun uudelleenkirjoitusten pohjalta.
- **Päätös (1:28–1:30):** ei kalvoja.

Jos et toimita lisäkalvosarjaa `kalvot-o14-paatospuut.md`, päälisen kalvon **9** kantaa päätöspuun visualisointi yksinään. Käy se hitaasti; luento nojaa siihen yhteen kalvoon.

---

## Oppitunti 15 — 90-minuutin suunnitelma

**Aihe.** Toisto: saman asian tekeminen monta kertaa.

**Tämän oppitunnin keskeinen viesti (yksi lause).** Toisto on tapa sanoa *"sama asia, uudelleen, selkeällä lopetuksella"* — ja lopetuksen nimeäminen selkokielellä on se, mikä erottaa hyödyllisen toiston karanneesta.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: luokka huutaa kolme toistoa, joita he ovat tehneet tähän mennessä tänään (todennäköisesti: hampaiden harjaus, liikennevalojen ohittaminen, chatin päivittäminen uusien viestien vuoksi). Opettaja kirjoittaa ne taululle. | Koko luokka |
| 0:10–0:28 | Opettajan input: määrittele *toisto*; näytä kolme muotoa (`for each` / `repeat until` / `while`) yhdellä esimerkillä per muoto. Esittele *"lopetusehto on turvavyö"* ja karannut toisto -ajatus. | Luento |
| 0:28–0:58 | **Itsenäinen työ** (30 min): jokainen opiskelija lisää toiston O13+O14-prosessiinsa ja kirjoittaa selkeän lopetusehdon. He myös kirjoittavat yhden lauseen, joka kuvaa miltä karannut tapaus näyttäisi ja miten turvalopetus sen korjaisi. | Itsenäinen |
| 0:58–1:20 | **Suositeltava opettajavetoinen tuntiaktiviteetti** — *"Etsi silmukka"* (Aktiviteetti A:n toinen puolikas tiedostossa `tuntitehtavat.md`, ~22 min). Opettaja lukee lyhyitä arki/ICT-lauseita; luokka äänestää *toisto / ei toistoa* ja nimeää lopetusehdon. | Koko luokka |
| 1:20–1:28 | Koko luokan purku: kerää kolme karannutta tapausta ("toista, kunnes ymmärrät", "niin kauan kuin sivu vielä latautuu", "jokaiselle asialle listalla"). Pohdi, miltä rehellinen lopetus näyttäisi kullekin. | Koko luokka |
| 1:28–1:30 | Päätös: esikatsaus viikolle 6 — *"Ensi viikolla tiivistämme nämä luonnollisen kielen kuvaukset hieman lähemmäs koodia, paperilla. Sitä kutsutaan pseudokoodiksi."* Mainitse, että AT2 palautetaan tämän viikon lopussa / viikon 6 aikana. | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** 58–80 minuutin slot on Aktiviteetti A:n toinen puolikas tiedostossa `tuntitehtavat.md` (*Etsi silmukka*). Pino 2 kyseisestä tiedostosta on valmisteltava etukäteen. Aktiviteetti A on pakollinen koko viikon ajan — jos ajoit O14-puolikkaan, sinun pitäisi ajaa O15-puolikas myös, sekä symmetrian vuoksi että koska Pino 2:n *while*-ansalapus on diagnostinen hetki *kerralleen tehtävän vaiheen vs. toistuvan vaiheen* virhekäsitykselle.

**Mitä sanot ääneen.** *"Toisto on kolmas rakennuspalikka ja vaarallisin, koska jokainen toisto voi pyöriä ikuisesti, jos sen lopetus on epärehellinen. Kolme muotoa: for-each, kun tiedät listan; repeat-until, kun lopetus riippuu jostain, mitä tapahtuu; while, kun testi tarkistetaan ennen jokaista toistoa. Kaikki kolme tarvitsevat lopetuksen, jonka sananmukainen tulkitsija pystyy oikeasti havaitsemaan."* Kirjoita sitten *"toista, kunnes ymmärrät"* taululle: *"Miten tulkitsija tietäisi, milloin pysähtyä?"* Hiljaisuus on oppi. Käännä *"…tai pysähdy 10 yrityksen jälkeen"* turvavyöksi.

**Materiaalit.** Taulu ja tussi; paperia ja kyniä; Pino 2 tiedostosta `tuntitehtavat.md` valmistettuna lappuina tai tulostettuna listana.

**Kalvovihjeet — päälinen kalvosarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** ei kalvoja. Kerää toistoja taululle.
- **Luento (0:10–0:28):** päälinen kalvosarja, kalvot **11 → 14**: *Toisto — tekeminen uudelleen, lopetuksella* · *Toiston kolme muotoa* · *Toisto työssä — sähköpostien läpikäynti* · *Lopetusehto on turvavyö*. Sähköpostien läpikäynti -kalvolla kannattaa viipyä; merkitse selkeästi, että sähköpostien läpikäynti käyttää kaikkia kolmea rakennuspalikkaa yhdellä kertaa.
- **Itsenäinen työ (0:28–0:58):** jätä kalvo **12** näytölle hiljaiseksi viitteeksi kolmesta muodosta (`for each` / `repeat until` / `while`).
- **Tuntiaktiviteetti (0:58–1:20):** ei kalvoja. Luokitteluleikki elää taululla.
- **Purku (1:20–1:28):** ei kalvoja; käytä taulua kolmen karanneen tapauksen kirjoittamiseen, joita luokka kerää.
- **Päätös (1:28–1:30):** kalvo **18** (*Mitä seuraavaksi: viikko 6 — pseudokoodi*) yhden rivin esikatselulle, sitten kalvo **19** (*Yhteenveto — keskeinen viesti*), jotta opiskelijat lähtevät sananmukaisen rivin kanssa.

---

## Fasilitointivinkit

### Ennen mitä tahansa kolmesta tunnista

- **Testaa keskeinen viesti itselläsi ensin.** Lue se ääneen kerran, hitaasti: *"Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto."* Se esiintyy sananmukaisesti vähintään yhdellä kalvolla ja vähintään kerran tiedostossa `itseopiskelu.md`. Peilaa sitä omassa puheessasi vähintään kahdesti per oppitunti; se on viikon selkäranka.
- **Esikirjoita taulun asettelu.** O13:lle hahmottele "järjestys merkitsee / järjestys ei merkitse" -kaksisarakkeinen ruudukko. O14:lle hahmottele sateenvarjopäätöspuu ja salasanasääntö. O15:lle hahmottele sähköpostien läpikäynti -kulkukaavio, joka näyttää kaikki kolme rakennuspalikkaa yhdellä kertaa. Tämän piirtäminen elävänä on hyvä; sen ajatteleminen elävänä on riskialtista.
- **Lue `tuntitehtavat.md` päästä päähän ennen oppituntia 14.** Aktiviteetti A esiintyy kahtena puolikkaana — Pino 1 O14:ssä, Pino 2 O15:ssä — ja tarvitsee laput (tai tulostetun listan) valmiina.

### Tunnin aikana

- **Vaadi kanonisia nimiä.** *Sekvenssi, ehto, toisto.* Synonyymit (valinta, haara, silmukka, iteraatio) ovat hyväksyttäviä ohimennen, mutta pari ne aina kanonisen nimen kanssa ensimmäisellä kerralla.
- **Johda arkisella esimerkillä. Aina.** Salasanasääntö, sähköpostien läpikäynti ja käyttöönottolista saapuvat **arkisen** esimerkin **jälkeen** — teereseptin, *"jos sataa, mene bussilla"* ja *"merkitse jokainen nimi luettelosta"* jälkeen. Jos opiskelija tarjoaa ICT-esimerkin ensin, hyväksy se mutta pari se arkisella ennen jatkamista.
- **Suojaa itsenäisen työn lohkoa.** Viikko 5 rakentaa AT2-syöttötuotoksen kolmen oppitunnin yli. Jos 90-minuutin suunnitelma liukuu, leikkaus tulee purusta tai luennosta, ei itsenäisestä työstä. Älä mene alle 27 minuutin per oppitunti.
- **Älä lipsahda koodiin.** Kun opiskelija kirjoittaa `if (x > 0) {` paperilleen, kirjoita se taululle pehmeästi uudelleen muotoon *"jos x on suurempi kuin 0, niin …"* selkokielellä. Koodi tulee viikolla 7.
- **Nimeä testi, älä vastaus.** Kun opiskelija piirtää päätöspuun epämääräisellä haaralla kuten *"jos menee pieleen"*, paina: *"mikä täsmällinen testi sananmukainen tulkitsija ajaisi tietääkseen, että meni pieleen?"*
- **Rehelliset lopetukset.** Kun opiskelija kirjoittaa *"toista kunnes valmis"*, kysy: *"miten tulkitsija tietää, että on valmis?"* Jos vastaus on *"hän vain tietää"*, lopetus ei ole vielä rehellinen.
- **Vastusta *infinite loop* -kauhuajatusta.** *Karannut toisto* ja *ei rehellistä lopetusta* ovat kurssin sisäiset ilmaukset. *Infinite loop* saapuu, kun koodikin saapuu.

---

## Vastauksia yleisiin opiskelijakysymyksiin

- *"Onko `if … then …` sama kuin `if … then … else …`?"* — Ei. Ilman `else`-haaraa tulkitsija ei tee mitään ylimääräistä muutoin. `else`-haaran kanssa tulkitsija tekee jotain muuta epätosi-haarassa. Molemmat muodot ovat päteviä; ne sanovat eri asioita.
- *"Voiko ehdolla olla enemmän kuin kaksi haaraa?"* — Kyllä, `else if`-haaralla. Kolme tai neljä haaraa on normaalia — *"jos sataa, mene bussilla; muuten jos olet myöhässä, juokse; muuten kävele."* Yli viisi tarkoittaa yleensä, että sääntö piilottaa syvemmän rakenteen.
- *"Onko `for each` silmukka vai sekvenssi?"* — Silmukka. Se tekee saman asian kerran jokaiselle listan kohteelle, ja lista on lopetusehto. Yksi lause, ei monta.
- *"Mitä jos `repeat until` voisi pyöriä ikuisesti?"* — Lisää turvalopetus: *"…tai pysähdy 10 yrityksen jälkeen"*, *"…tai pysähdy 30 minuutin jälkeen"*. Jokaisella rehellisellä toistolla on vähintään yksi havaittavissa oleva lopetus. Turvalopetus on osa suunnittelua, ei anteeksipyyntö.
- *"Onko tämä AT2:ssa?"* — Kyllä. Tuotos, jonka rakennat O13:n, O14:n ja O15:n yli, on AT2-tuotos pienemmässä mittakaavassa. **AT2 palautetaan viikon 5 lopussa / viikon 6 aikana.** Säilytä muistiinpanosi.
- *"Voinko käyttää koodia AT2:ssa?"* — Et vielä. AT2 on luonnollista kieltä, jossa `if … then … else …` ja `for each / repeat until / while` ovat löyhää, englanninkielistä merkintää. Pseudokoodi saapuu ensi viikolla. AT2:ta arvioidaan *ajattelusta*, ei syntaksista.
- *"Mikä on ero *while*- ja *repeat until* -muotojen välillä?"* — `while X, jatka tekemistä …` tarkistaa testin **ennen** jokaista toistoa: jos X on jo epätosi, tulkitsija tekee sisävaiheen nolla kertaa. `repeat … until X` ajaa sisävaiheen **vähintään kerran**, sitten tarkistaa. Lue oma silmukkasi ääneen ja kysy: *"ensimmäisellä kierroksella, tekeekö tulkitsija mitään?"*

---

## Formatiivisen arvioinnin vinkit

Viikolla 5 ei ole omaa **summatiivista arviointia** — summatiivinen tuotos on AT2, joka palautetaan viikon 5 lopussa / viikon 6 aikana. Formatiivisten tarkistusten rooli on tehdä ymmärtäminen näkyväksi varhain, jotta opiskelijoita, jotka vielä sekoittavat kolme rakennuspalikkaa, voidaan auttaa ennen AT2:n laskeutumista. Käytä yhtä tai kahta per oppitunti.

### Oppituntikohtaisia epämuodollisia tarkistuksia

- **Oppitunti 13 — exit ticket (3 min, tunnin lopussa).** Jokainen opiskelija kirjoittaa yhden lauseen, joka vastaa: *"Nimeä yhden tänään ajamasi prosessin sekvenssirunko."* Selaa tikettejä matkalla O14:lle; jos enemmän kuin muutama sanoo *"minulla ei ole sellaista"*, palaa O13:n keskeiseen viestiin O14:n alussa.
- **Oppitunti 14 — tauluäänestys.** Näytä kolme lyhyttä sääntöä taululla (esim. *"jos sinulla on bussikortti JA siinä on rahaa, voit mennä bussilla"*, *"jos maito haisee, heitä se pois"*, *"jos sataa, mene bussilla, muuten kävele"*) ja kysy luokalta, kummalla on **eniten haaroja** päätöspuussaan. Käsien kohotusten kuvio kertoo, näkevätkö opiskelijat rakennetta arkisen ilmauksen alla.
- **Oppitunti 14 — tarralappujen keräys Aktiviteetti A:n päätyttyä.** Jokainen opiskelija kirjoittaa yhden epämääräisen ehdon, jonka on kuullut tai sanonut tällä viikolla. Lue 3 satunnaisesti; luokka ehdottaa rehellistä testiä kullekin.
- **Oppitunti 15 — tarralappujen keräys.** Jokainen opiskelija kirjoittaa yhden *karanneen toiston*, jonka on kuullut tai sanonut tällä viikolla ("toista, kunnes ymmärrät", "niin kauan kuin sivu vielä latautuu"). Lue 3 satunnaisesti; luokka ehdottaa turvalopetusta kullekin.
- **Oppitunti 15 — minuuttipaperi viikon lopussa.** *"Yhdellä lauseella, nimeä rakennuspalikka, jonka tunnistat helpoimmin, ja se, jonka tunnistat vaikeimmin."* Luokan halki kulkeva kuvio kertoo, mitä palata viikon 6 ensimmäisinä 5 minuuttina.

### Mitä kuuntelet koko viikon ajan

Kolme ilmausta, jotka merkitsevät aitoa ymmärrystä viikon 5 lopussa:

- *"Missä testi on?"* (kun lukee ehtoa).
- *"Mikä on lopetus?"* (kun lukee toistoa).
- *"Sekvenssi on selkäranka — ehto ja toisto roikkuvat siinä."*

Jos nämä ilmaukset esiintyvät opiskelijoiden puheessa O15:n loppuun mennessä, AT2 voi laskeutua ilman korjauksia. Jos eivät, viikon 6 hyödyllisimmät 5 minuuttia on kolmen rakennuspalikan kertaus ennen pseudokoodin saapumista.

Luokitteluleikki (Aktiviteetti A tiedostossa `tuntitehtavat.md`) on viikon keskeinen diagnoosi. Luokka, joka äänestää itsevarmasti ansalappujen kohdalla, on luokka, joka on valmis AT2:een.
