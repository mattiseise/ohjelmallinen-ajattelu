# Viikko 6 — Opettajan materiaalit

Tämä dokumentti kattaa kaikki kolme viikon 6 oppituntia (O16, O17, O18) yhdessä paikassa. Se rakentuu saman ydinviestin ympärille, jonka opiskelijat näkevät: **"Pseudokoodi on silta arkikielen ja oikean koodin välillä: tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida."** Viikko 6 on kurssin ohjelmallisen ajattelun puoliskon synteesiviikko. Kaikki viikoilta 1–5 — selkeä sekvenssi, abstraktio, ehdot ja toisto — yhdistyy yhdeksi täsmällisemmäksi notaatioksi, ja koodin paperilla lukemisen vähän harjoiteltua taitoa harjoitellaan ensi kertaa.

**AT2 palautetaan tämän viikon oppitunnin 18 tienoilla.** Se pyytää lyhyttä pseudokoodia pienestä prosessista, jäljityskaaviota yhdelle normaalille ja yhdelle hankalalle syötteelle, sekä lyhyttä reflektiota arkikielellä. O16–O18:n kaari on AT2-raaka-aineen tehdas: O16 tuottaa pseudokoodin, O17 teroittaa muuttujat ja syöte/käsittely/tuloste-rungon, O18 tuottaa jäljityksen ja nostaa bugit pintaan.

Mikään oikea ohjelmointikieli ei esiinny missään tällä viikolla. Pseudokoodin avainsanat ovat ISOIN KIRJAIMIN jaettuja kurssikonventioita, ei kieli, jota tietokone voi ajaa. Testaaminen tarkoittaa käsiajoa paperilla jäljityskaavion avulla, piste. Oikea koodi saapuu viikolla 7.

Ristiviittaukset: täydentävää kalvosarjaa `kalvot-o16-pseudokoodin-lapikaynti.md` käytetään O16:n luento-osion aikana. Pakollinen tuntiaktiviteetti *Käsiajo luokkana* on kuvattu tiedostossa `tuntitehtavat.md` ja kuuluu O18:n 55–80 min lohkoon.

---

## Viikon 6 oppimistavoitteet (kartoitettuna Bloomiin)

Viikko 6 pysyy **Ymmärtämisen** ja **Soveltamisen** sisällä. Kielletyt verbit viikon 6 tavoitteille: *arvioida, tuomita, suunnitella, luoda, rakentaa, kehittää, abstrahoida, pilkkoa* — ne kuuluvat viikoille 4 ja 8. Kevyttä Analysointia (bugin tyypin nimeäminen) esiintyy vain syventävissä tehtävissä, ei koskaan ensisijaisena tavoitteena.

### Oppitunti 16 — Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon

- **Ymmärtäminen:** opiskelija osaa **määritellä** *pseudokoodin* omin sanoin ja **verrata** sitä arkikieleen ja oikeaan ohjelmointikieleen.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** kolme rakennuspalikkaa, jotka kohdattiin jo viikolla 5 — sekvenssin, ehdon, toiston — lyhyestä pseudokoodista.
- **Soveltaminen:** opiskelija osaa **kirjoittaa** 10–20 rivin pseudokoodin tutusta prosessista käyttäen pientä kiinteää avainsanajoukkoa (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`).
- **Ymmärtäminen:** opiskelija osaa **selittää**, miksi pseudokoodi on luotettavampaa jaettavaa kuin englanninkielinen proosa, kun on kyse ohjeesta, jota tietokone lopulta suorittaa.

### Oppitunti 17 — Syöte, käsittely, tuloste ja muuttujan idea

- **Ymmärtäminen:** opiskelija osaa **kuvata** pseudokoodin syöte → käsittely → tuloste -rungon.
- **Ymmärtäminen:** opiskelija osaa **määritellä** *muuttujan* omin sanoin: nimetyn säilön yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen aikana.
- **Soveltaminen:** opiskelija osaa **käyttää** `SET variableName TO value`-, `READ variableName`- ja `WRITE variableName`-rakenteita oikein pseudokoodissa.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, että muuttujan *nimen* tulisi kuvata, mitä se pitää sisällään.

### Oppitunti 18 — Pseudokoodin testaaminen: käsiajo ja virheiden etsiminen

- **Ymmärtäminen:** opiskelija osaa **selittää**, mikä jäljityskaavio on ja miksi käsiajo paperilla löytää bugeja, joita uudelleenlukeminen ei.
- **Soveltaminen:** opiskelija osaa **käsiajaa** lyhyen pseudokoodin rivi riviltä jäljityskaavion avulla, päivittäen jokaisen muuttujan jokaisella askeleella.
- **Soveltaminen:** opiskelija osaa **löytää** vähintään yhden bugin tarkoituksellisesti rikotusta pseudokoodista käsiajamalla sen.
- **Soveltaminen:** opiskelija osaa **korjata** bugin ja käsiajaa korjatun pseudokoodin vahvistaakseen odotetun tulosteen.

---

## Viikon 6 yleisiä virhekäsityksiä

Vähintään kaksi virhekäsitystä per oppitunti. Ennakoi niitä siellä, missä ne sopivat luonnollisesti — useimmat nousevat itsestään esiin itsenäisen työn lohkon tai luokan käsiajon aikana.

### Oppitunnin 16 virhekäsityksiä

**Virhekäsitys:** *"Pseudokoodi on ohjelmointikieli."*
**Korjaus:** Pseudokoodi on jaettu kirjoituskonventio, ei kieli, jota tietokone voi ajaa. `SET counter TO 5` -käskylle ei ole tulkkia. Ihmislukija (tai kääntäjä) on aina mukana ketjussa. Jaettujen avainsanojen idea on, että jokainen lukija huoneessa tulkitsee saman muodon samalla tavalla.

**Virhekäsitys:** *"On olemassa yksi oikea pseudokoodi."*
**Korjaus:** Eri opettajat ja oppikirjat käyttävät eri avainsanajoukkoja. Jotkut suosivat pienaakkosista `if`:ää, jotkut suosivat `:=`:tä sijoitukseen. Tämä kurssi käyttää yhtä kiinteää joukkoa, jotta huone lukee toistensa pseudokoodia samalla tavalla. Oikeassa työpaikassa jokainen tiimi valitsee yhden joukon ja pysyy siinä.

### Oppitunnin 17 virhekäsityksiä

**Virhekäsitys:** *"Muuttuja on sama kuin numero."*
**Korjaus:** Muuttuja on nimetty säilö. Tänään se pitää numeroa; huomenna sama muuttuja saattaa pitää eri numeroa, kyllä/ei-arvoa tai lyhyttä merkkijonoa. Säilö on muuttuja; sisällä oleva arvo on erillinen asia. Yhdistä etiketöidyn laatikon metaforaan joka kerta.

**Virhekäsitys:** *"Muuttujan nimellä ei ole väliä."*
**Korjaus:** `x` ja `passwordLength` tekevät täsmälleen saman asian kuvitellulle tietokoneelle, mutta hyvin eri asioita seuraavalle pseudokoodin lukijalle (joka on usein huomisen-sinä). Pseudokoodin koko idea on, että tuntematon voi lukea sitä. Huono nimi heittää sen pois.

### Oppitunnin 18 virhekäsityksiä

**Virhekäsitys:** *"Jos pseudokoodi lukee oikein, se on oikein."*
**Korjaus:** Lukeminen ei löydä off-by-onea, vääriä vertailuja tai puuttuvia alustuksia. Silmä liukuu niiden yli. Vain jäljityskaavio pakottaa jokaisen rivin julistamaan, mitä jokainen muuttuja on sen suorittamisen jälkeen. Se on koko idea.

**Virhekäsitys:** *"Jäljityskaavio on tyhjäntoimitusta — voin käsiajaa sen päässä."*
**Korjaus:** Päässä jäljittäminen on täsmälleen se paikka, jossa bugit selviävät. Taulukko pakottaa jokaisen askeleen paperille, ja muuttujan uuden arvon kirjoittamisen toimenpide on se, jossa aivot löytävät sen, mitä silmä jätti huomaamatta. Opiskelijat, jotka jättävät taulukon välistä, ovat opiskelijoita, jotka palauttavat AT2:n löytymättömällä off-by-onella.

**Bonusvirhekäsitys:** *"Pseudokoodi on sama kuin koodi, joten voisin yhtä hyvin kirjoittaa oikeaa koodia."*
**Korjaus:** Ei vielä. Pseudokoodi kuorii syntaksimelun pois, jotta rakenne on näkyvissä. Sama opiskelija, joka ensi viikolla kirjoittaa oikeaa koodia luottavaisesti, on opiskelija, joka rakensi pseudokoodirutiinin tällä viikolla. Pseudokoodivaiheen ohittaminen on ajatteluvaiheen ohittamista.

---

## Oppitunti 16 — 90 minuutin suunnitelma

**Aihe.** Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon.

**Tämän oppitunnin ydinviesti (yksi lause).** Pseudokoodi ei ole uusi kieli ulkoa opettelua varten — se on niitä asioita, joita jo kirjoitat, muutamilla yhteisillä sanoilla ja kiinteällä muodolla, jotta tuntematon voi lukea sen samalla tavalla kuin sinä.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: opettaja lukee yhden lyhyen englanninkielisen ohjeen ääneen (ehdotus: tee-resepti, neljä lausetta). Luokka tiivistää sen taululle pseudokoodimaiseen muotoon, rivi riviltä, käyttäen vain sanoja, jotka he ovat jo kuulleet aiempina viikkoina. | Koko luokka |
| 0:10–0:30 | Opettajan syöte: määrittele *pseudokoodi*; esittele pieni avainsanajoukko (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). **Aja täydentävä kalvosarja `kalvot-o16-pseudokoodin-lapikaynti.md` täällä kokonaan** — se kävelee tee-reseptin englannista valmiiseen annotoituun pseudokoodiin. | Luento |
| 0:30–1:00 | **Itsenäinen työ** (30 min): jokainen opiskelija aloittaa tehtävän 6.1 — pseudokoodin kirjoittaminen tutusta prosessista, jota hän tekee itse. Vain kirjoittaminen tällä oppitunnilla; käsiajo odottaa O18:aa. | Itsenäinen |
| 1:00–1:20 | Pariaktiviteetti: opiskelijat vaihtavat luonnoksia ja lukevat toistensa pseudokoodia hiljaa, alleviivaten yhden epäselvän rivin ja ympyröiden yhden muuttujan nimen, joka ei kuvaa mitä se pitää sisällään. | Pari |
| 1:20–1:28 | Koko luokan purku: kerää kolme esimerkkiriviä vaihdosta; kirjoita yhdessä uudelleen taululle. Yhdistä O16:n ydinviestiin. | Koko luokka |
| 1:28–1:30 | Päätös: yhden rivin esikatselu oppitunnista 17 — *"Seuraavaksi nimeämme paikan, jossa pseudokoodi pitää asioita, jotka sen täytyy muistaa suorituksen aikana."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** O16 ei käytä mitään aktiviteettia tiedostosta `tuntitehtavat.md`. Pakollinen tuntiaktiviteetti kuuluu O18:aan.

**Mitä sanot ääneen.** *"Olet kirjoittanut tällaista viikosta 1 lähtien. Pseudokoodi on samaa ajattelua muutamilla jaetuilla sanoilla päällä. `SET` on vain *pussissa on nyt*. `IF` on vain *testi, joka jakaa polun*. `WHILE` on vain *jatka tämän tekemistä, kunnes pysähdys tapahtuu*. Jaettujen sanojen idea on, että jokainen lukija tässä huoneessa tulkitsee saman rivin samalla tavalla."*

**Materiaalit.** Taulu ja kynä; paperi ja kynät; täydentävä kalvosarja `kalvot-o16-pseudokoodin-lapikaynti.md` näytöllä luento-osion aikana. Ei tekniikkaa opiskelijoilta.

**Slide cues — pääsarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **4** (*Mikä pseudokoodi on?*) näytöllä, kun taulu kantaa elävää englanti → pseudokoodi -tiivistystä.
- **Luento (0:10–0:30):** pääsarjan kalvot **4 → 7**: *Mikä pseudokoodi on?* · *Pieni avainsanojen joukko* · *Englanti vs. pseudokoodi — teen keittäminen* · *Sekvenssi · ehto · toisto*. **Kalvojen 5 ja 6 välissä, vaihda täydentävään kalvosarjaan `kalvot-o16-pseudokoodin-lapikaynti.md` ja aja se päästä päähän** (6 lyhyttä kalvoa, ~10 min) — se kävelee tee-esimerkin kokonaan. Palaa pääsarjan kalvolle 6 vierekkäisluokse.
- **Itsenäinen työ (0:30–1:00):** jätä pääsarjan kalvo **5** (*Pieni avainsanojen joukko*) näytölle hiljaiseksi referenssikortiksi.
- **Pariaktiviteetti (1:00–1:20):** ei kalvoja; työ paperilla.
- **Purku (1:20–1:28):** ei kalvoja. Käytä taulua kolmeen uudelleenkirjoitukseen.
- **Päätös (1:28–1:30):** ei kalvoja.

---

## Oppitunti 17 — 90 minuutin suunnitelma

**Aihe.** Syöte, käsittely, tuloste ja muuttujan idea.

**Tämän oppitunnin ydinviesti (yksi lause).** Pseudokoodiohjelma on lähes aina pieni kone, joka ottaa syötettä, tekee sille jotain ja tuottaa tulostetta — ja muuttuja on paikka, jossa se pitää asioita, jotka sen täytyy muistaa suorituksen aikana.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: nimeä kolme oikean maailman "muuttujaa" huoneesta (taulun päivämäärä, nykyinen puhuja, lounasruoka). Pohjusta etiketöidyn laatikon metafora ennen avainsanan saapumista. | Koko luokka |
| 0:10–0:30 | Opettajan syöte: määrittele *muuttuja*; kävele syöte → käsittely → tuloste -runko; kirjoita salasanan vahvuuden esimerkki taululle, rivi riviltä, käyttäen `SET`-, `READ`-, `IF/ELSE/ENDIF`- ja `WRITE`-rakenteita. Pidä tauko ja nimeä kukin rivi syötteeksi, käsittelyksi tai tulosteeksi. | Luento |
| 0:30–1:00 | **Itsenäinen työ** (30 min): jokainen opiskelija ottaa O16:n pseudokoodinsa ja (a) merkitsee syöte-, käsittely- ja tuloste-osiot; (b) korvaa nimeämättömät arvot nimetyillä muuttujilla; (c) alleviivaa minkä tahansa muuttujan nimen, joka ei kuvaa mitä se pitää sisällään. | Itsenäinen |
| 1:00–1:20 | Pariaktiviteetti: parit jäljittävät toistensa syöte/käsittely/tuloste-rungon paperilla — löydätkö, missä käsittely tapahtuu? Missä syöte päättyy? Merkitse parin pseudokoodiin. | Pari |
| 1:20–1:28 | Koko luokan purku: yksi esimerkki taululla. Missä käsittelylohko alkoi ja päättyi? Mikä muuttujan nimi piti kirjoittaa uudelleen? | Koko luokka |
| 1:28–1:30 | Päätös: esikatsele O18 ja AT2. *"Seuraavalla oppitunnilla testaamme pseudokoodin. AT2 palautetaan seuraavan oppitunnin loppupuolella."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** O17 ei käytä mitään aktiviteettia tiedostosta `tuntitehtavat.md`. O17:lle ei toimiteta täydentävää kalvosarjaa; salasanan vahvuuden esimerkki on tarpeeksi lyhyt kävellä elävänä taululla, ja pääsarjan kalvo 11 kantaa sen kertausta varten.

**Mitä sanot ääneen.** *"Katso mitä tahansa pseudokoodia, jonka kirjoitit viime oppitunnilla. Siinä on osa, jossa se pyytää jotain ulkopuolelta — se on syöte. Siinä on osa, jossa se päättää tai laskee tai vertaa — se on käsittely. Siinä on osa, jossa se kertoo ulkopuolelle jotain takaisin — se on tuloste. Useimmassa hyödyllisessä pseudokoodissa on kaikki kolme. Keskimmäinen osa on, missä muuttujat ansaitsevat palkkansa."* Kävele salasanan vahvuuden esimerkki: lue salasana, laske sen pituus, aseta `isStrong` arvoon YES jos pituus on vähintään 8 ja se sisältää numeron, muutoin NO; kirjoita tulos.

**Materiaalit.** Taulu ja kynä; paperi ja kynät; pääsarja näytöllä.

**Slide cues — pääsarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **8** (*Syöte → käsittely → tuloste*) näytöllä, kun luokka nimeää huoneessa olevia muuttujia.
- **Luento (0:10–0:30):** pääsarjan kalvot **8 → 11**: *Syöte → käsittely → tuloste* · *Mikä muuttuja on?* · *Hyvä muuttujan nimi* · *Ammatillinen esimerkki — salasanan vahvuus*. Viivy kalvolla 11; kävele jokainen salasanan esimerkin rivi taululle sen viereen.
- **Itsenäinen työ (0:30–1:00):** jätä kalvo **9** (*Mikä muuttuja on?*) näytölle hiljaiseksi referenssiksi.
- **Pariaktiviteetti (1:00–1:20):** ei kalvoja; parit työskentelevät paperilla.
- **Purku (1:20–1:28):** ei kalvoja; käytä taulua.
- **Päätös (1:28–1:30):** kalvo **15** (*AT2 — palautetaan oppitunnin 18 tienoilla*) rauhalliseen esikatseluun.

---

## Oppitunti 18 — 90 minuutin suunnitelma

**Aihe.** Pseudokoodin testaaminen: käsiajo ja virheiden etsiminen. **AT2 palautetaan tämän oppitunnin tienoilla.**

**Tämän oppitunnin ydinviesti (yksi lause).** Pseudokoodi ei ole valmis, kun se näyttää oikealta; se on valmis, kun jäljityskaavio todistaa, että se tuottaa odotetun tulosteen, mukaan lukien vähintään yhdellä hankalalla syötteellä.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: taulu-demo jäljityskaaviosta 4 rivin pseudokoodikatkelmalle (ehdotus: kahden arvon vaihto väliaikaisen muuttujan avulla). Opettaja kirjoittaa; luokka huutaa jokaisen uuden arvon. | Koko luokka |
| 0:10–0:25 | Opettajan syöte: määrittele *käsiajo*; näytä, miten jäljityskaavio piirretään (sarakkeet = rivi, jokainen muuttuja, tuloste); nimeä, mikä lasketaan bugiksi (todellinen tuloste eroaa odotetusta tulosteesta). Linkki takaisin viikon 1 "sananmukaiseen robottiin" — opiskelija näyttelee sananmukaista robottia omalle pseudokoodilleen, paperilla. | Luento |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija käsiaja omaa tehtävän 6.1 pseudokoodiaan yhdellä normaalilla syötteellä ja yhdellä hankalalla syötteellä, piirtäen jäljityskaavion käsin. | Itsenäinen |
| 0:55–1:20 | **PAKOLLINEN opettajan vetämä tuntiaktiviteetti — *Käsiajo luokkana*** (Aktiviteetti A tiedostossa `tuntitehtavat.md`, ~25 min). Opettaja kirjoittaa tarkoituksellisesti rikotun lyhyen pseudokoodin taululle; luokasta tulee jäljityskaavio, yksi opiskelija per muuttuja, huutavat päivitykset rivi riviltä. Bugi nousee esiin. Luokka korjaa sen taululla. | Koko luokka |
| 1:20–1:28 | AT2-luovutus: 5 minuuttia siitä, mitä AT2 odottaa (pseudokoodi pienestä prosessista, jäljityskaavio yhdelle normaalille ja yhdelle hankalalle syötteelle, lyhyt reflektio), 3 minuuttia selventäville kysymyksille. Rauhallinen tahti. | Koko luokka |
| 1:28–1:30 | Päätös: yhden rivin esikatselu viikolle 7 — *"Ensi viikolla sama pseudokoodimuoto muuttuu pieneksi ohjelmaksi oikealla kielellä, jonka ajat selaimessa."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** 55–80 min lohko on **Aktiviteetti A — *Käsiajo luokkana*** tiedostosta `tuntitehtavat.md`. Valmistele rikottu pseudokoodi lappuun tai muistiinpanoihin ennen tuntia. Aktiviteetti B (*Pseudokoodin vaihto ja jäljitys*) samasta tiedostosta on valinnainen ja sopii O16:n 1:00–1:20 lohkoon, jos luento jää lyhyeksi.

**Mitä sanot ääneen.** *"Luit oman pseudokoodisi viime oppitunnilla ja se näytti hyvältä. Tänään testaamme sen. Jäljityskaavio on testi. Kirjoitat alas, mitä jokainen muuttuja on jokaisen rivin jälkeen. Kun teet tämän rehellisesti, kaksi asiaa tapahtuu: ensiksi, pseudokoodi joka näytti hyvältä, osoittautuu joskus vääräksi, ja toiseksi, pseudokoodi jonka epäilit olevan väärä, osoittautuu hyväksi. Kummassakin tapauksessa opit jotain, mitä silmä ei voisi."* AT2-luovutukseen: *"AT2 on yksi pseudokoodi pienestä prosessista, jäljityskaavio yhdelle normaalille ja yhdelle hankalalle syötteelle, ja viiden lauseen reflektio. Tehtävissä 6.1 ja 6.2 tekemäsi työ on sitä työtä, jota AT2 pyytää. Ei mitään uutta."*

**Materiaalit.** Taulu ja kynä; paperi ja kynät; rikottu pseudokoodi tiedoston `tuntitehtavat.md` Aktiviteetti A:sta valmiina kirjoitettavaksi taululle 0:55 kohdalla.

**Slide cues — pääsarja `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **12** (*Mikä käsiajo on?*) näytöllä, kun taulu kantaa elävää arvojen vaihdon jäljitystä.
- **Luento (0:10–0:25):** pääsarjan kalvot **12 → 14**: *Mikä käsiajo on?* · *Jäljityskaavio* · *Bugin löytäminen — todellinen vs. odotettu tuloste*. Viivy kalvolla 13; jäljityskaavio ruudulla ja elävä demo taululla vahvistavat toisiaan.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **13** (*Jäljityskaavio*) näytölle hiljaiseksi referenssiksi taulukon muodolle.
- **Tuntiaktiviteetti (0:55–1:20):** ei kalvoja. Käsiajo elää taululla — se on oppitunti.
- **AT2-luovutus (1:20–1:28):** kalvo **15** (*AT2 — palautetaan oppitunnin 18 tienoilla*).
- **Päätös (1:28–1:30):** kalvo **19** (*Mitä tulee seuraavaksi — viikko 7: ensimmäinen oikea koodi*) yhden rivin esikatseluun, sitten kalvo **20** (*Kertaus — keskeinen kysymys vielä kerran*), jotta opiskelijat lähtevät sanatarkalla keskeisellä kysymyksellä.

---

## Fasilitointivinkkejä

### Ennen mitään kolmesta tunnista

- **Testaa ydinviesti itselläsi.** Lue se ääneen hitaasti: *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."* Se esiintyy sanatarkasti vähintään yhdellä kalvolla. Peilaa sitä omassa puheessasi vähintään kahdesti oppituntia kohden; se on viikon selkäranka.
- **Esikirjoita taulun asettelu.** O16:lle, luonnostele englanti → pseudokoodi -rinnakkainen teelle. O17:lle, luonnostele salasanan vahvuuden esimerkki syöte/käsittely/tuloste-laatikoineen. O18:lle, luonnostele tyhjä jäljityskaavio kolmella nimetyllä sarakkeella (rivi, muuttuja, tuloste). Eläväksi piirtäminen on hyvä; eläväksi ajatteleminen on riskialtista.
- **Lue `tuntitehtavat.md` päästä päähän ennen oppituntia 18.** Aktiviteetti A — *Käsiajo luokkana* — vaatii rikotun pseudokoodin valmistetuksi etukäteen. Päätä, mitä bugin tyyppiä käytät (off-by-one `WHILE`-ehdossa on suositeltu oletus — helppo esitellä, helppo korjata, vaikea havaita pelkällä lukemisella).

### Tunnin aikana

- **Vaadi ISOJEN KIRJAINTEN avainsanoja.** `SET`, `IF`, `WHILE` isoin kirjaimin; kaikki muu pienin. Visuaalinen kontrasti on puoli luettavuudesta, joka on ilmaista. Opiskelijat, jotka kirjoittavat `set` ja `if`, menettävät sen.
- **Vaadi, että opiskelijat lukevat pseudokoodia ääneen käsiajon aikana.** Ääni löytää sen, mitä silmä jättää huomaamatta. *"WHILE counter is greater than one, do…"* — kuultuna ääneen, off-by-one tulee kuultavaksi.
- **Älä anna opiskelijoiden kirjoittaa pseudokoodia uudelleen samalla kun he jäljittävät.** Jäljitä ensin yhdelle sivulle; korjaa erilliselle sivulle. Niiden sekoittaminen on tapa, jolla bugit piilotetaan.
- **Suojele 30 minuutin itsenäistä lohkoa.** Se on osa, jonka paineen alla olevat opettajat leikkaavat ensimmäisenä, ja se on paikka, jossa AT2-valmius rakennetaan. Jos luento venyy, leikkaa luennosta, älä itsenäisestä työstä.
- **Käytä taulua jäljityskaavioille, ei kalvoja.** Kalvot pohjustavat kysymyksen; jäljityksen on tapahduttava elävänä. Ruumiillistettu jäljitys O18:ssa on oppitunti — kalvo ei voi tehdä sitä, mitä liikkuva kynä taululla tekee.
- **Yhdistä jokainen uusi termi takaisin viikkoihin 1 ja 5.** Viikko 6 on synteesi. *Muuttuja* on etiketöity laatikko (viikon 1 selkeä nimeäminen). *Jäljityskaavio* on sananmukainen robotti lukemassa rivi riviltä (viikko 1). *Sekvenssi, ehto, toisto* ovat viikon 5 kolme rakennetta. Mikään ei ilmestynyt ilman edeltäjää.
- **Kun opiskelijat väittelevät jäljityskaavion kanssa, kysy kolme kysymystä järjestyksessä:** *"Mitä rivi 4 sanoi? Lue se ääneen. Mitä muuttuja nyt yhtä rivin 4 jälkeen?"* Väittely häviää aina.

---

## Vastauksia yleisiin opiskelijakysymyksiin

- *"Onko pseudokoodi oikea kieli?"* — Ei. Se on jaettu kirjoituskonventio. Eri opettajat käyttävät eri avainsanajoukkoja. Käytämme tällä kurssilla yhtä kiinteää joukkoa, jotta jokainen lukija huoneessa tulkitsee saman rivin samalla tavalla.
- *"Voiko tietokone ajaa pseudokoodia?"* — Ei suoraan. Ihmisen tai kääntäjän on käännettävä se ensin oikeaksi kieleksi. Viikko 7 on se, jossa käännös alkaa.
- *"Pitääkö käyttää näitä täsmällisiä avainsanoja?"* — Tällä kurssilla kyllä — jotta luemme toistemme pseudokoodia samalla tavalla. Oikeassa työpaikassa jokainen tiimi valitsee yhden joukon ja pysyy siinä.
- *"Mitä AT2 oikeasti haluaa minulta?"* — Lyhyt pseudokoodi (10–20 riviä) pienestä valitsemastasi prosessista, jäljityskaavio yhdelle normaalille ja yhdelle hankalalle syötteelle, ja viiden lauseen reflektio siitä, mitä jäljityksesi löysi. Ei mitään uutta tehtävien 6.1 ja 6.2 ulkopuolella.
- *"Mitä jos jäljityskaavioni on eri mieltä pseudokoodini kanssa?"* — Luota jäljitykseen yli pään. Sitten joko pseudokoodissa on bugi tai jäljityksessä on bugi. Tee jäljitys uudelleen tuoreelle sivulle; kumpi siirtyy, oli väärä.
- *"Onko `WRITE` sama kuin `PRINT`?"* — Tällä kurssilla, kyllä. Käytämme `WRITE`:tä johdonmukaisesti; jotkut oppikirjat käyttävät `PRINT`:iä. Valitse yksi ja pysy siinä.
- *"Mitä jos muuttujani on kyllä/ei?"* — Sitten se on edelleen muuttuja. `SET isStrong TO YES` on täsmälleen samanlainen `SET` kuin `SET counter TO 0`. Muuttuja ei välitä, mitä siinä on; lukija välittää.

---

## Formatiivisen arvioinnin vinkkejä

Viikko 6 johtaa suoraan AT2:een, joten formatiivisten tarkistusten rooli on tehdä ymmärrys näkyväksi *ennen* AT2-määräaikaa. Käytä yhtä tai kahta per oppitunti.

### Oppituntikohtaiset epämuodolliset tarkistukset

- **Oppitunti 16 — poistumislippu (3 min, tunnin lopussa).** Jokainen opiskelija kirjoittaa yhden lauseen: *"Nimeä yksi avainsana O16:n joukosta ja yksi rivi, jolla käytit sitä."* Selaa läpi matkalla O17:ään. Jos useammat kuin muutamat opiskelijat eivät osaa nimetä avainsanaa omassa pseudokoodissaan, käy avainsanakortti uudelleen läpi O17:n alussa.
- **Oppitunti 17 — post-it-keräys.** Jokainen opiskelija kirjoittaa yhden muuttujan pseudokoodistaan ja yhden arvon, jonka se voisi pitää. Lue kolme satunnaisesti; luokka löytää huonon nimen. Luokan yli oleva kuvio kertoo, onko nimirehellisyys laskeutunut.
- **Oppitunti 17 — tauluäänestys.** Näytä kolme lyhyttä katkelmaa taululla ja kysy, mikä niistä on selkein syöte/käsittely/tuloste-runko. Käsien malli näyttää, onko kolmiosainen muoto näkyvissä opiskelijoille vielä.
- **Oppitunti 18 — pariraportointi itsenäisen työn lopussa.** Jokainen pari raportoi yhden asian, jonka jäljitys löysi, mitä lukeminen ei. Jos useimmat parit sanovat *"ei mitään"*, jäljitykset eivät luultavasti olleet rehellisiä — paina lempeästi ja kylvä uudelleen arvojen vaihdon demolla.
- **Oppitunti 18 — yhden minuutin paperi viikon lopussa.** *"Yhdellä lauseella, mitä jäljityskaavio tekee, mitä uudelleenlukeminen ei?"* Vastaukset kertovat sinulle, ennen kuin AT2 laskeutuu, kuka on sisäistänyt O18:n ydinviestin ja kuka edelleen uskoo, että päässä jäljittäminen riittää.

### Mitä kuuntelet viikon yli

Kolme lausetta, jotka merkitsevät aitoa ymmärrystä viikon 6 päätteeksi:

- *"Mitä muuttuja on tämän rivin jälkeen?"* (kun lukee pseudokoodia ääneen).
- *"Antaa kun jäljitän sen paperilla."* (kun tuloste näyttää epäilyttävältä).
- *"Todellinen eroaa odotetusta rivillä 4."* (kun raportoi bugin — rivinumero, ei fiilis).

Jos nämä lauseet ilmestyvät opiskelijoiden puheeseen O18:n päätteeksi, AT2 laskeutuu ilman kertausta. Jos eivät, O18:n AT2-luovutuksen hyödyllisimmät 5 minuuttia on jäljityskaavion muodon kertaus. *Käsiajo luokkana* -aktiviteetti tiedostossa `tuntitehtavat.md` on viikon keskeinen diagnostiikka — luokka, joka saa bugin kiinni luottavaisesti, on luokka, joka on valmis AT2:een.
