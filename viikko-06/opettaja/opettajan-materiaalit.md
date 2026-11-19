# Viikko 6 — Opettajan materiaalit

Tämä dokumentti kattaa viikon 6 kaikki kolme oppituntia (L16, L17, L18) samassa paikassa. Viikko rakentuu saman
ydinviestin ympärille, jonka opiskelijat näkevät:
“Pseudokoodi on silta arkisen englannin ja oikean koodin välillä: riittävän täsmällistä, jotta tietokone voisi
tarvittaessa seurata sitä, ja riittävän luettavaa, jotta sen voi jakaa myös ei-ohjelmoijalle.”
Viikko 6 on kurssin ohjelmallisen ajattelun puolikkaan synteesiviikko. Kaikki viikoilta 1–5 — selkeä järjestys,
abstraktio, ehdot ja toisto — kootaan yhteen tarkempaan merkintätapaan. Samalla harjoitellaan ensimmäistä kertaa
liian vähän harjoiteltua taitoa: koodin lukemista paperilla.
AT2 palautetaan noin tämän viikon oppitunnin 18 kohdalla. Se pyytää lyhyen pseudokoodin pienelle prosessille,
jäljitystaulukon yhdelle normaalille ja yhdelle hankalalle syötteelle sekä lyhyen reflektion yleiskielellä. L16–L18-kaari
on AT2:n raaka-ainetehdas: L16 tuottaa pseudokoodin, L17 tarkentaa muuttujat ja syöte–käsittely–tuotos-rungon,
L18 tuottaa jäljityksen ja nostaa mahdolliset bugit esiin.
Tällä viikolla ei käytetä oikeaa ohjelmointikieltä. Pseudokoodin avainsanat ovat ISOIN KIRJAIMIN kirjoitettuja
yhteisiä kurssikäytäntöjä, eivät kieli, jota tietokone voi suorittaa. Testaaminen tarkoittaa kuivaharjoittelua paperilla
jäljitystaulukon avulla, piste. Oikea koodi tulee viikolla 7.
Ristiinviittaukset: lisäpakkaa slides-l16-pseudocode-walkthrough.md käytetään L16:n opetusosuudessa.
Pakollinen tuntitehtävä Yhteinen kuivaharjoittelu kuvataan tiedostossa in-class-tasks.md, ja se kuuluu L18:n 55–
80 minuutin jaksoon.
Ajattele näin: Pseudokoodi ei ole uusi taikasana. Se on tapa kirjoittaa jo opitut rakenteet niin, että jokainen luokassa
lukee ne samalla tavalla.

## Viikon 6 oppimistavoitteet (Bloom-taksonomian mukaan)

Viikko 6 pysyy tasoilla Ymmärtäminen ja Soveltaminen. Viikon 6 tavoitteissa vältettävät verbit ovat arvioida,
arvostella, suunnitella, luoda, rakentaa, kehittää, abstrahoida, pilkkoa — ne kuuluvat viikoille 4 ja 8. Kevyt
Analysointi (bugityypin nimeäminen) esiintyy vain syventävissä tehtävissä, ei päätavoitteena.

### Oppitunti 16 — Pseudokoodi: luonnollisesta kielestä tarkempaan muotoon

• Ymmärtäminen: opiskelija osaa määritellä pseudokoodin omin sanoin ja erottaa sen arkikielisestä
ohjeesta sekä oikeasta ohjelmointikielestä.
• Ymmärtäminen: opiskelija osaa tunnistaa viikon 5 kolme rakennuspalikkaa — järjestys, ehto ja toisto —
lyhyestä pseudokoodista.
• Soveltaminen: opiskelija osaa kirjoittaa 10–20 rivin pseudokoodin tutusta prosessista käyttäen pientä
kiinteää avainsanajoukkoa (SET, READ, WRITE, IF/ELSE/ENDIF, WHILE/ENDWHILE,
FOR/ENDFOR).
• Ymmärtäminen: opiskelija osaa selittää, miksi pseudokoodi on luotettavampi jakaa kuin proosamuotoinen
englanti, kun ohjeen on tarkoitus joskus päätyä tietokoneen suoritettavaksi.

### Oppitunti 17 — Syöte, käsittely, tuotos ja muuttujan idea

• Ymmärtäminen: opiskelija osaa kuvata pseudokoodin syöte → käsittely → tuotos -rungon.
• Ymmärtäminen: opiskelija osaa määritellä muuttujan omin sanoin: nimetty säiliö yhdelle arvolle, joka voi
muuttua pseudokoodin suorituksen aikana.
• Soveltaminen: opiskelija osaa käyttää muotoja SET variableName TO value, READ variableName
ja WRITE variableName oikein pseudokoodissa.
• Ymmärtäminen: opiskelija osaa tunnistaa, että muuttujan nimen pitäisi kuvata, mitä se sisältää.

### Oppitunti 18 — Pseudokoodin testaaminen: kuivaharjoittelu ja virheiden löytäminen

• Ymmärtäminen: opiskelija osaa selittää, mikä jäljitystaulukko on ja miksi paperilla kuivaharjoittelu löytää
bugeja, joita uudelleenlukeminen ei löydä.
• Soveltaminen: opiskelija osaa kuivaharjoitella lyhyen pseudokoodin rivi riviltä jäljitystaulukon avulla ja
päivittää jokaisen muuttujan jokaisen vaiheen jälkeen.
• Soveltaminen: opiskelija osaa löytää vähintään yhden bugin tarkoituksella rikotusta pseudokoodista
kuivaharjoittelemalla.
• Soveltaminen: opiskelija osaa korjata bugin ja kuivaharjoitella korjatun pseudokoodin varmistaakseen
odotetun tuotoksen.

## Viikon 6 yleiset väärinkäsitykset

Alla on vähintään kaksi väärinkäsitystä per oppitunti. Ehkäise ne luontevissa kohdissa — useimmat nousevat
itsenäisen työn aikana tai yhteisessä kuivaharjoittelussa.

### Oppitunnin 16 väärinkäsitykset

Väärinkäsitys: “Pseudokoodi on ohjelmointikieli.”
Korjaus: Pseudokoodi on yhteinen kirjoituskäytäntö, ei kieli, jota tietokone voi suorittaa. Ei ole tulkkia, joka suorittaisi
rivin SET counter TO 5. Ihmislukija tai kääntäjä on aina välissä. Yhteisten avainsanojen tarkoitus on, että jokainen
lukija samassa huoneessa tulkitsee saman muodon samalla tavalla.
Väärinkäsitys: “On olemassa yksi oikea pseudokoodi.”
Korjaus: Eri opettajat ja oppikirjat käyttävät erilaisia avainsanajoukkoja. Jotkut suosivat pientä if-sanaa, toiset
käyttävät :=-merkintää sijoitukseen. Tällä kurssilla käytämme yhtä kiinteää joukkoa, jotta huone lukee toistensa
pseudokoodia samalla tavalla. Todellisessa työpaikassa jokainen tiimi valitsee yhden tavan ja pysyy siinä.

### Oppitunnin 17 väärinkäsitykset

Väärinkäsitys: “Muuttuja on sama asia kuin numero.”
Korjaus: Muuttuja on nimetty säiliö. Tänään siinä on numero; huomenna sama muuttuja voi sisältää eri numeron,
kyllä/ei-arvon tai lyhyen merkkijonon. Säiliö on muuttuja; sen sisällä oleva arvo on eri asia. Palaa merkitty laatikko
-vertauskuvaan joka kerta.
Väärinkäsitys: “Muuttujan nimellä ei ole väliä.”
Korjaus: x ja passwordLength tekevät kuvitteelliselle tietokoneelle täsmälleen saman asian, mutta seuraavalle
pseudokoodia lukevalle ihmiselle (usein huomisen sinulle) aivan eri asian. Pseudokoodin koko tarkoitus on, että
vieras ihminen voi lukea sen. Huono nimi heittää tämän hyödyn pois.

### Oppitunnin 18 väärinkäsitykset

Väärinkäsitys: “Jos pseudokoodi näyttää oikein luettuna, se on oikein.”
Korjaus: Lukeminen ei nappaa yhtä-poikkeamia, vääriä vertailuja tai puuttuvia alustuksia. Silmä liukuu niiden yli.
Vain jäljitystaulukko pakottaa jokaisen rivin sanomaan, mikä jokaisen muuttujan arvo on rivin jälkeen. Siinä on koko
pointti.
Väärinkäsitys: “Jäljitystaulukko on turhaa työtä — voin kuivaharjoitella päässä.”
Korjaus: Päässä jäljittäminen on juuri se paikka, johon bugit jäävät henkiin. Taulukko pakottaa jokaisen vaiheen
paperille, ja muuttujan uuden arvon kirjoittaminen on se hetki, jossa aivot huomaavat sen, minkä silmä ohitti.
Opiskelijat, jotka ohittavat taulukon, ovat juuri niitä, jotka palauttavat AT2:n löytämättömän yhden verran pieleen
-bugin kanssa.
Bonusväärinkäsitys: “Pseudokoodi on sama kuin koodi, joten voin yhtä hyvin kirjoittaa oikeaa koodia.”
Korjaus: Ei vielä. Pseudokoodi poistaa syntaksikohinan, jotta rakenne näkyy. Sama opiskelija, joka kirjoittaa ensi
viikolla oikeaa koodia itsevarmasti, on se opiskelija, joka rakensi pseudokooditavan tällä viikolla.
Pseudokoodivaiheen ohittaminen on ajatteluvaiheen ohittamista.

## Oppitunti 16 — 90 minuutin suunnitelma

Aihe. Pseudokoodi: luonnollisesta kielestä tarkempaan muotoon.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Pseudokoodi ei ole uusi ulkoa opeteltava kieli — se on niitä
asioita, joita jo kirjoitat, muutamalla yhteisellä sanalla ja kiinteällä muodolla niin, että vieras ihminen lukee sen
samalla tavalla kuin sinä.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: opettaja lukee ääneen yhden lyhyen englanninkielisen ohjeen, esimerkiksi neljän virkkeen teereseptin. Ryhmä tiivistää sen taululla pseudokoodimaiseksi muodoksi rivi riviltä käyttäen vain sanoja, jotka he ovat kuulleet aiemmilla viikoilla. | Koko ryhmä |
| 0:10–0:30 | Opettajan osuus: määrittele pseudokoodi; esittele pieni avainsanajoukko (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). **Käytä lisäpakka `slides-l16-pseudocode-walkthrough.md` tässä kokonaan** — se kuljettaa teereseptin englannista valmiiksi annotoiduksi pseudokoodiksi. | Opetuspuhe |
| 0:30–1:00 | **Itsenäinen työ** (30 min): jokainen opiskelija aloittaa tehtävän 6.1 — pseudokoodin kirjoittamisen tutulle prosessille, jota hän itse tekee. Tällä tunnilla vain kirjoitetaan; kuivaharjoittelu odottaa L18:aan. | Itsenäinen |
| 1:00–1:20 | Parityö: opiskelijat vaihtavat luonnoksia ja lukevat toistensa pseudokoodit hiljaa. He alleviivaavat yhden epäselvän rivin ja ympyröivät yhden muuttujan nimen, joka ei kuvaa sisältöään. | Pari |
| 1:20–1:28 | Koko ryhmän purku: kerää kolme esimerkkiriviä vaihdosta; kirjoittakaa ne yhdessä uudelleen taululla. Kytke L16:n ydinviestiin. | Koko ryhmä |
| 1:28–1:30 | Lopetus: yhden virkkeen ennakko oppitunnista 17 — *"Seuraavaksi nimeämme paikan, jossa pseudokoodi säilyttää asiat, jotka sen täytyy muistaa suorituksen aikana."* | Koko ryhmä |
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. L16 ei käytä tehtävää tiedostosta in-class-tasks.md. Pakollinen tuntitehtävä kuuluu L18:aan.
Mitä sanot ääneen. “Olette kirjoittaneet tällaista jo viikosta 1 lähtien. Pseudokoodi on sama ajattelu muutamalla
yhteisellä sanalla. SET on vain ‘pussissa on nyt tämä’. IF on vain ‘testi, joka jakaa polun’. WHILE on vain ‘jatka
tätä, kunnes pysäytys tapahtuu’. Yhteisten sanojen tarkoitus on, että jokainen lukija tässä huoneessa tulkitsee
saman rivin samalla tavalla.”
Esimerkki: SET cups TO 1 voidaan lukea ääneen: “Aseta muuttuja cups arvoon 1.” Ääneen lukeminen auttaa
erottamaan avainsanan ja muuttujan nimen.
Materiaalit. Taulu ja tussi; paperia ja kyniä; lisäpakka slides-l16-pseudocode-walkthrough.md näytölle
opetusosuuden aikana. Opiskelijat eivät tarvitse teknologiaa.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): dia 4 (Mitä pseudokoodi on?) näkyviin samalla, kun taulu kantaa live-tiukennuksen
englannista pseudokoodiksi.
• Opettajan osuus (0:10–0:30): pääpakan diat 4 → 7: Mitä pseudokoodi on? · Pieni avainsanajoukko ·
Englanti vs. pseudokoodi — teen tekeminen · Järjestys · ehto · toisto. Dian 5 ja 6 välissä vaihda
lisäpakkaan slides-l16-pseudocode-walkthrough.md ja käytä se alusta loppuun (6 lyhyttä diaa,
noin 10 min) — se käy tee-esimerkin kokonaan läpi. Palaa pääpakan diaan 6 rinnakkaiseen sulkemiseen.
• Itsenäinen työ (0:30–1:00): jätä pääpakan dia 5 (Pieni avainsanajoukko) näkyviin hiljaiseksi viitekortiksi.
• Parityö (1:00–1:20): ei dioja; työskennellään paperilla.
• Purku (1:20–1:28): ei dioja. Käytä taulua kolmeen uudelleenkirjoitukseen.
• Lopetus (1:28–1:30): ei dioja.

## Oppitunti 17 — 90 minuutin suunnitelma

Aihe. Syöte, käsittely, tuotos ja muuttujan idea.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Pseudokoodiohjelma on melkein aina pieni kone, joka ottaa
syötteen, tekee sille jotakin ja tuottaa tuotoksen — ja muuttuja on paikka, jossa se säilyttää asiat, jotka sen täytyy
muistaa suorituksen aikana.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: nimeä kolme todellisen maailman "muuttujaa" luokassa (taululla oleva päivämäärä, tämänhetkinen puhuja, lounaslista). Rakenna merkitty laatikko -vertaus ennen avainsanan esittelyä. | Koko ryhmä |
| 0:10–0:30 | Opettajan osuus: määrittele muuttuja; käy syöte → käsittely → tuotos -runko läpi; kirjoita salasanan vahvuusesimerkki taululle rivi riviltä käyttäen `SET`, `READ`, `IF/ELSE/ENDIF` ja `WRITE`. Pysähdy nimeämään jokainen rivi syötteeksi, käsittelyksi tai tuotokseksi. | Opetuspuhe |
| 0:30–1:00 | **Itsenäinen työ** (30 min): jokainen opiskelija ottaa L16-pseudokoodinsa ja (a) merkitsee syöte-, käsittely- ja tuotososat; (b) korvaa nimettömät arvot nimetyillä muuttujilla; (c) alleviivaa jokaisen muuttujan nimen, joka ei kuvaa sisältöään. | Itsenäinen |
| 1:00–1:20 | Parityö: parit jäljittävät toistensa syöte–käsittely–tuotos-rungon paperilla — näetkö, missä käsittely tapahtuu? Missä syöte loppuu? Merkitse parin pseudokoodiin. | Pari |
| 1:20–1:28 | Koko ryhmän purku: yksi esimerkki taululle. Missä käsittelylohko alkoi ja loppui? Mikä muuttujan nimi piti kirjoittaa uudelleen? | Koko ryhmä |
| 1:28–1:30 | Lopetus: ennakko L18:sta ja AT2:sta. *"Seuraavalla tunnilla testaamme pseudokoodin. AT2 palautetaan noin seuraavan tunnin lopussa."* | Koko ryhmä |
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. L17 ei käytä tehtävää tiedostosta in-class-tasks.md. L17:ään ei toimiteta lisäpakkaa;
salasanan vahvuusesimerkki on tarpeeksi lyhyt käveltäväksi livenä taululla, ja pääpakan dia 11 kantaa sen
kertaukseen.
Mitä sanot ääneen. “Katsokaa mitä tahansa pseudokoodia, jonka kirjoititte viime tunnilla. Siinä on kohta, jossa se
pyytää jotakin ulkopuolelta — se on syöte. Siinä on kohta, jossa se päättää, laskee tai vertaa — se on käsittely.
Siinä on kohta, jossa se kertoo ulkopuolelle jotakin takaisin — se on tuotos. Useimmissa hyödyllisissä
pseudokoodeissa on kaikki kolme. Keskiosa on se kohta, jossa muuttujat ansaitsevat palkkansa.” Käy salasanan
vahvuusesimerkki läpi: lue salasana, laske sen pituus, aseta isStrong arvoon YES, jos pituus on vähintään 8 ja se
sisältää numeron, muuten NO; kirjoita tulos.
Vinkki opiskelijalle: Hyvä muuttujan nimi vastaa kysymykseen “mitä tässä säilytetään?” Esimerkiksi length on
parempi kuin x, ja passwordLength on vielä parempi, jos pseudokoodissa on muitakin pituuksia.
Materiaalit. Taulu ja tussi; paperia ja kyniä; pääpakka näytöllä.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): dia 8 (Syöte → käsittely → tuotos) näkyviin, kun ryhmä nimeää muuttujia luokasta.
• Opettajan osuus (0:10–0:30): pääpakan diat 8 → 11: Syöte → käsittely → tuotos · Mikä on muuttuja? ·
Hyvä muuttujan nimi · Ammatillinen esimerkki — salasanan vahvuus. Viivy diassa 11; käy jokainen
salasanan esimerkin rivi läpi taululla dian vieressä.
• Itsenäinen työ (0:30–1:00): jätä dia 9 (Mikä on muuttuja?) näkyviin hiljaiseksi viitteeksi.
• Parityö (1:00–1:20): ei dioja; parit työskentelevät paperilla.
• Purku (1:20–1:28): ei dioja; käytä taulua.
• Lopetus (1:28–1:30): dia 15 (AT2 — palautetaan noin oppitunnilla 18) rauhalliseen ennakkoon.

## Oppitunti 18 — 90 minuutin suunnitelma

Aihe. Pseudokoodin testaaminen: kuivaharjoittelu ja virheiden löytäminen. AT2 palautetaan noin tämän
oppitunnin kohdalla.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Pseudokoodi ei ole valmis silloin, kun se näyttää oikealta; se on
valmis, kun jäljitystaulukko osoittaa, että se tuottaa odotetun tuotoksen myös vähintään yhdellä hankalalla syötteellä.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: tauludemo jäljitystaulukosta 4-riviselle pseudokoodipätkälle, esimerkiksi kahden arvon vaihtaminen väliaikaisella muuttujalla. Opettaja kirjoittaa; ryhmä huutaa jokaisen uuden arvon. | Koko ryhmä |
| 0:10–0:25 | Opettajan osuus: määrittele kuivaharjoittelu; näytä, miten jäljitystaulukko piirretään (sarakkeet = rivi, jokainen muuttuja, tuotos); nimeä, mikä lasketaan bugiksi (todellinen tuotos eroaa odotetusta tuotoksesta). Kytke viikon 1 "kirjaimelliseen robottiin" — opiskelija esittää kirjaimellista robottia omalle pseudokoodilleen paperilla. | Opetuspuhe |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija kuivaharjoittelee oman tehtävän 6.1 pseudokoodinsa yhdellä normaalilla syötteellä ja yhdellä hankalalla syötteellä ja piirtää jäljitystaulukon käsin. | Itsenäinen |
| 0:55–1:20 | **PAKOLLINEN opettajajohtoinen tuntitehtävä — *Yhteinen kuivaharjoittelu*** (tehtävä A tiedostossa `in-class-tasks.md`, noin 25 min). Opettaja kirjoittaa taululle tarkoituksella rikotun lyhyen pseudokoodin; ryhmästä tulee jäljitystaulukko, yksi opiskelija per muuttuja, ja he sanovat päivitykset ääneen rivi riviltä. Bugi nousee esiin. Ryhmä korjaa sen taululla. | Koko ryhmä |
| 1:20–1:28 | AT2:n luovutus: 5 minuuttia siitä, mitä AT2 odottaa (pseudokoodi pienelle prosessille, jäljitystaulukko yhdelle normaalille ja yhdelle hankalalle syötteelle, lyhyt reflektio), 3 minuuttia tarkentaville kysymyksille. Rauhallinen tempo. | Koko ryhmä |
| 1:28–1:30 | Lopetus: yhden virkkeen ennakko viikosta 7 — *"Ensi viikolla sama pseudokoodin muoto muuttuu pieneksi ohjelmaksi oikeassa kielessä, jota ajat selaimessa."* | Koko ryhmä |
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 55–80 minuutin jakso on Tehtävä A — Yhteinen kuivaharjoittelu tiedostosta in-class-
tasks.md. Valmistele rikottu pseudokoodi lapulle tai muistiinpanoihisi ennen tuntia. Tehtävä B (Pseudokoodin
vaihto ja jäljitys) samasta tiedostosta on valinnainen ja sopii L16:n 1:00–1:20-jaksoon, jos opetusosuus jää lyhyeksi.
Mitä sanot ääneen. “Luitte oman pseudokoodinne viime tunnilla ja se näytti hyvältä. Tänään testaamme sen.
Jäljitystaulukko on testi. Kirjoitatte ylös, mitä jokainen muuttuja on jokaisen rivin jälkeen. Kun teette tämän
rehellisesti, tapahtuu kaksi asiaa: ensinnäkin pseudokoodi, joka näytti hyvältä, osoittautuu joskus vääräksi, ja
toiseksi pseudokoodi, jonka epäilit ehkä olevan väärin, osoittautuu toimivaksi. Kummassakin tapauksessa opit
jotakin, mitä silmä ei pystynyt kertomaan.” AT2:n luovutuksessa: “AT2 on yksi pseudokoodi pienelle prosessille,
jäljitystaulukko yhdelle normaalille ja yhdelle hankalalle syötteelle sekä viiden virkkeen reflektio. Tehtävissä 6.1 ja
6.2 tekemänne työ on se työ, jota AT2 pyytää. Ei mitään uutta.”
Materiaalit. Taulu ja tussi; paperia ja kyniä; in-class-tasks.md-tiedoston tehtävän A rikottu pseudokoodi valmiina
taululle kirjoitettavaksi kohdassa 0:55.
Diavihjeet — pääpakka . `slides.md`
• Lämmittely (0:00–0:10): dia 12 (Mitä kuivaharjoittelu on?) näkyviin samalla, kun taulu kantaa kahden arvon
vaihtamisen livejäljityksen.
• Opettajan osuus (0:10–0:25): pääpakan diat 12 → 14: Mitä kuivaharjoittelu on? · Jäljitystaulukko · Bugin
löytäminen — todellinen vs. odotettu tuotos. Viivy diassa 13; näytön jäljitystaulukko ja taulun live-demo
vahvistavat toisiaan.
• Itsenäinen työ (0:25–0:55): jätä dia 13 (Jäljitystaulukko) näkyviin hiljaiseksi viitteeksi taulukon muodosta.
• Tuntitehtävä (0:55–1:20): ei dioja. Kuivaharjoittelu elää taululla — se on oppitunti.
• AT2-luovutus (1:20–1:28): dia 15 (AT2 — palautetaan noin oppitunnilla 18).
• Lopetus (1:28–1:30): dia 19 (Mitä seuraavaksi — viikko 7: ensimmäinen oikea koodi) yhden virkkeen
ennakoksi, sitten dia 20 (Kertaus — ydinkysymys vielä kerran), jotta opiskelijat lähtevät sanasta sanaan
-ydinkysymyksen kanssa.

## Fasilitointivinkit

### Ennen jokaista kolmesta oppitunnista

• Testaa ydinviesti itselläsi. Lue se hitaasti ääneen: “Pseudokoodi on silta arkisen englannin ja oikean
koodin välillä: riittävän täsmällistä, jotta tietokone voisi tarvittaessa seurata sitä, ja riittävän luettavaa, jotta
sen voi jakaa myös ei-ohjelmoijalle.” Se näkyy sanasta sanaan vähintään yhdessä diassa. Peilaa sitä
omassa puheessasi vähintään kahdesti per oppitunti; se on viikon selkäranka.
• Luonnostele taulun rakenne etukäteen. L16:lle tee tee-esimerkin englanti → pseudokoodi -rinnastus.
L17:lle luonnostele salasanan vahvuusesimerkki syöte/käsittely/tuotos-laatikoilla. L18:lle luonnostele tyhjä
jäljitystaulukko, jossa on kolme nimettyä saraketta: rivi, muuttuja, tuotos. Livepiirtäminen on hyvä; liveajattelu
on riskialtista.
• Lue in-class-tasks.md alusta loppuun ennen oppituntia 18. Tehtävä A — Yhteinen kuivaharjoittelu —
tarvitsee rikotun pseudokoodin etukäteen. Päätä, mitä bugityyppiä käytät. Suositeltu oletus on yhden verran
pieleen -virhe WHILE-ehdossa: helppo tuoda sisään, helppo korjata, vaikea huomata pelkällä lukemisella.

### Tunnin aikana

• Vaadi ISOIN KIRJAIMIN kirjoitettuja avainsanoja. SET, IF, WHILE isolla; kaikki muu pienellä.
Visuaalinen kontrasti on ilmaista luettavuutta. Opiskelijat, jotka kirjoittavat set ja if, menettävät sen.
• Vaadi, että opiskelijat lukevat pseudokoodin ääneen kuivaharjoittelussa. Ääni nappaa sen, minkä silmä
ohittaa. “WHILE counter is greater than one, do…” — ääneen kuultuna yhden verran pieleen -virhe alkaa
kuulua.
• Älä anna opiskelijoiden kirjoittaa pseudokoodia uudelleen jäljittäessään sitä. Jäljitä ensin yhdellä
sivulla; korjaa eri sivulla. Näiden sekoittaminen piilottaa bugit.
• Suojele 30 minuutin itsenäistä jaksoa. Se on se osa, jonka paineessa opettajat leikkaavat ensin, ja siinä
rakennetaan AT2-valmius. Jos opetus venyy, leikkaa opetusosuudesta, älä itsenäisestä työstä.
• Käytä jäljitystaulukoihin taulua, älä dioja. Diat asettavat kysymyksen; jäljityksen täytyy tapahtua livenä.
L18:n kehollinen jäljitys on oppitunti — dia ei tee sitä, mitä liikkuva tussi taululla tekee.
• Kytke jokainen uusi termi takaisin viikkoihin 1 ja 5. Viikko 6 on synteesi. Muuttuja on merkitty laatikko
(viikon 1 selkeä nimeäminen). Jäljitystaulukko on kirjaimellinen robotti, joka lukee rivi riviltä (viikko 1).
Järjestys, ehto, toisto ovat viikon 5 kolme rakennetta. Mikään uusi ei ilmesty ilman ennakkotietoa.
• Kun opiskelijat väittelevät jäljitystaulukon kanssa, kysy kolme kysymystä tässä järjestyksessä: “Mitä
rivi 4 sanoi? Lue se ääneen. Mitä muuttuja on rivin 4 jälkeen?” Taulukko voittaa aina.

## Vastauksia yleisiin opiskelijakysymyksiin

• “Onko pseudokoodi oikea kieli?” — Ei. Se on yhteinen kirjoituskäytäntö. Eri opettajat käyttävät eri
avainsanoja. Me käytämme tällä kurssilla yhtä kiinteää joukkoa, jotta jokainen luokassa lukee saman rivin
samalla tavalla.
• “Voiko tietokone ajaa pseudokoodia?” — Ei suoraan. Ihmisen tai kääntäjän täytyy ensin muuttaa se oikeaksi
kieleksi. Viikko 7 on paikka, jossa tämä käännös alkaa.
• “Täytyykö käyttää juuri näitä avainsanoja?” — Tällä kurssilla kyllä, jotta voimme lukea toistemme
pseudokoodia samalla tavalla. Oikeassa työpaikassa jokainen tiimi valitsee yhden tavan ja pysyy siinä.
• “Mitä AT2 oikeasti haluaa minulta?” — Lyhyen pseudokoodin (10–20 riviä) itse valitsemastasi pienestä
prosessista, jäljitystaulukon yhdelle normaalille ja yhdelle hankalalle syötteelle sekä viiden virkkeen
reflektion siitä, mitä jäljitys löysi. Ei mitään tehtävien 6.1 ja 6.2 yli.
• “Mitä jos jäljitystaulukko on eri mieltä pseudokoodini kanssa?” — Luota jäljitykseen enemmän kuin päähäsi.
Silloin joko pseudokoodissasi on bugi tai jäljityksessäsi on bugi. Tee jäljitys uudelle sivulle; se joka muuttuu,
oli väärässä.
• “Onko WRITE sama kuin PRINT?” — Tällä kurssilla kyllä. Käytämme johdonmukaisesti WRITE-sanaa;
osa oppikirjoista käyttää PRINT-sanaa. Valitse yksi ja pysy siinä.
• “Mitä jos muuttujani on kyllä/ei-arvo?” — Se on silti muuttuja. SET isStrong TO YES on täsmälleen
samanlainen SET kuin SET counter TO 0. Muuttuja ei välitä, mitä sen sisällä on; lukija välittää.

## Formatiivisen arvioinnin vinkit

Viikko 6 johtaa suoraan AT2:een, joten formatiivisten tarkistusten tehtävä on tehdä ymmärrys näkyväksi ennen
AT2:n määräaikaa. Käytä yksi tai kaksi per oppitunti.

### Oppituntikohtaiset epämuodolliset tarkistukset

• Oppitunti 16 — poistumislappu (3 min tunnin lopussa). Jokainen opiskelija kirjoittaa yhden virkkeen:
“Nimeä yksi L16:n avainsana ja yksi rivi, jolla käytit sitä.” Silmäile matkalla L17:ään. Jos useampi opiskelija
ei pysty nimeämään avainsanaa omasta pseudokoodistaan, palaa avainsanakorttiin L17:n alussa.
• Oppitunti 17 — sticky note -keruu. Jokainen opiskelija kirjoittaa yhden muuttujan omasta
pseudokoodistaan ja yhden arvon, jonka se voisi sisältää. Lue kolme satunnaisesti; ryhmä löytää huonon
nimen. Koko ryhmän malli kertoo, onko nimien rehellisyys asettunut.
• Oppitunti 17 — tauluäänestys. Näytä taululla kolme lyhyttä pätkää ja kysy, missä on selkein
syöte/käsittely/tuotos-runko. Käsien jakauma näyttää, näkyykö kolmen osan muoto opiskelijoille vielä.
• Oppitunti 18 — parien raportointi itsenäisen työn lopussa. Jokainen pari raportoi yhden asian, jonka
jäljitys huomasi ja lukeminen ohitti. Jos suurin osa pareista sanoo “ei mitään”, jäljitykset eivät
todennäköisesti olleet rehellisiä — työnnä lempeästi takaisin ja kylvä uudelleen kahden arvon vaihtamisen
demolla.
• Oppitunti 18 — yhden minuutin paperi viikon lopussa. “Mitä jäljitystaulukko tekee yhdessä virkkeessä
sellaista, mitä uudelleenlukeminen ei tee?” Vastaukset kertovat ennen AT2:n tuloa, kuka on sisäistänyt
L18:n ydinviestin ja kuka uskoo yhä päässä jäljittämisen riittävän.

### Mitä kuuntelet koko viikon ajan

Kolme lausetta, jotka merkitsevät aitoa ymmärrystä viikon 6 loppuun mennessä:
• “Mikä muuttujan arvo on tämän rivin jälkeen?” kun pseudokoodia luetaan ääneen.
• “Jäljitetään se paperilla.” kun tuotos näyttää epäilyttävältä.
• “Todellinen eroaa odotetusta rivillä 4.” kun bugista raportoidaan — rivinumero, ei tunne.
Jos nämä ilmaukset näkyvät opiskelijoiden puheessa L18:n loppuun mennessä, AT2 tulee ilman korjaavaa
kertausta. Jos ei, L18:n AT2-luovutuksen hyödyllisimmät 5 minuuttia ovat jäljitystaulukon muodon kertaus. Yhteinen
kuivaharjoittelu on viikon keskeinen diagnostiikka.
