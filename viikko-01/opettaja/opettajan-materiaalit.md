# Viikko 1 — Opettajan materiaalit

Tämä dokumentti kattaa viikon 1 kaikki kolme oppituntia (L1, L2, L3) samassa paikassa. Viikko rakentuu saman
ydinkysymyksen ympärille, jonka myös opiskelijat näkevät:
“Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?”
Viikko 1 luo käsitteellisen perustan koko 8 viikon kurssille. Tällä viikolla ei vielä oteta käyttöön koodia, vuokaavioita
eikä pseudokoodia. Kolme oppituntia muodostavat yhden kokonaisen kaaren: oppitunti 1 nimeää ongelman
(kirjaimellinen tulkinta ja moniselitteisyys), oppitunti 2 nimeää ratkaisun tuottavan artefaktin (algoritmi), ja oppitunti 3
testaa artefaktia etsimällä ja poistamalla moniselitteisyyttä.
Ristiinviittaukset: oppitunneilla 1 ja 3 käytettävät tuntitehtävät kuvataan tarkemmin saman kansion tiedostossa in-
class-tasks.md. Ristiinviittaukset näkyvät alla tuntikohtaisissa suunnitelmissa.
Ajattele näin: Tämän viikon tavoite ei ole, että opiskelija “osaa ohjelmoida”. Tavoite on, että hän alkaa kuulla omat
ohjeensa kirjaimellisen seuraajan näkökulmasta.

## Viikon 1 oppimistavoitteet (Bloom-taksonomian mukaan)

Viikko 1 pysyy tasoilla Muistaminen ja Ymmärtäminen. Oppitunneilla 2 ja 3 sallitaan kevyt Soveltaminen (lyhyen
arjen algoritmin kirjoittaminen ja epätarkan ohjeen uudelleenkirjoittaminen). Viikon 1 tavoitteissa vältettävät verbit
ovat luoda, rakentaa, suunnitella, kehittää, arvioida, arvostella, analysoida, pilkkoa, abstrahoida, debugata. Nämä
palaavat myöhemmillä viikoilla.

### Oppitunti 1 — Ihmiset, tietokoneet ja ohjeiden tulkitseminen

• Muistaminen: opiskelija osaa määritellä ohjelmallisen ajattelun omin sanoin.
• Ymmärtäminen: opiskelija osaa selittää, että tietokone noudattaa ohjeita kirjaimellisesti.
• Ymmärtäminen: opiskelija osaa antaa yhden arjen esimerkin ja yhden IT-esimerkin siitä, mitä tarkoittaa
“puhua tietokoneelle”.
• Ymmärtäminen: opiskelija osaa tunnistaa, että moniselitteisyys on ohjeen ominaisuus, ei tietokoneen
ominaisuus.

### Oppitunti 2 — Algoritmit arjessa

• Muistaminen: opiskelija osaa määritellä sanan algoritmi omin sanoin.
• Ymmärtäminen: opiskelija osaa tunnistaa algoritmeja arjen tilanteissa (resepti, reitti, aamurutiini).
• Ymmärtäminen: opiskelija osaa kuvata algoritmin neljä osaa: tavoite, syöte, vaiheet ja tuotos.
• Ymmärtäminen: opiskelija osaa verrata kahta saman tavoitteen algoritmia pintatasolla: kumpi on lyhyempi
ja kumpaa on helpompi seurata.
• Kevyt soveltaminen: opiskelija osaa kirjoittaa 5–10 vaiheen arjen algoritmin selkeällä yleiskielellä.

### Oppitunti 3 — Täsmälliset ja epätäsmälliset ohjeet

• Ymmärtäminen: opiskelija osaa tunnistaa moniselitteisiä sanoja lyhyestä ohjeesta.
• Ymmärtäminen: opiskelija osaa selittää, miksi testaaminen paljastaa puutteita nopeammin kuin pelkkä
uudelleenlukeminen.
• Kevyt soveltaminen: opiskelija osaa kirjoittaa uudelleen epätarkan ohjeen niin, että kirjaimellinen
seuraaja pystyy suorittamaan sen.
• Kevyt soveltaminen: opiskelija osaa testata ohjeen toimimalla itse “kirjaimellisena tietokoneena”.
Kurssin korkeammat Bloom-tasot — Analysointi (viikko 4) ja Luominen (viikon 8 arvioitava päätöstehtävä) — eivät
kuulu tarkoituksella tämän viikon tavoitteisiin.

## Viikon 1 yleiset väärinkäsitykset

Jokaiselle oppitunnille on alla vähintään kaksi väärinkäsitystä. Puutu heti oppitunnin 1 alussa ensimmäiseen
väärinkäsitykseen (“tietokone on tyhmä”), koska se on yleisin ja haitallisin, jos se jää elämään.

### Oppitunnin 1 väärinkäsitykset

Väärinkäsitys: “Tietokone on tyhmä.”
Korjaus: Tietokone on kirjaimellinen, ei tyhmä. Kirjaimellisella seuraajalla ei ole mielipidettä siitä, onko ohje
järkevä. Se tekee täsmälleen sen, minkä sanat mahdollistavat. Vaadi sanaa kirjaimellinen ensimmäisestä minuutista
lähtien ja korjaa lempeästi sanat tyhmä tai dumb, kun niitä ilmestyy opiskelijoiden puheeseen. Koko kurssi rakentuu
tämän uudelleenkehystyksen varaan: jos opiskelija pitää sanan “tyhmä” sanavarastossaan, hän jatkaa helposti
ajattelua, jossa koneen “olisi pitänyt tietää”, mitä hän tarkoitti.
Vinkki: Voit sanoa: “Tietokone ei arvaa. Se seuraa sitä, mitä kirjoitit — ei sitä, mitä tarkoitit.”
Väärinkäsitys: “Ohjelmallinen ajattelu on vain ohjelmointia.”
Korjaus: Ohjelmallinen ajattelu on ohjelmoinnin taustalla oleva ajattelutapa: otetaan ongelma, nimetään mikä on
pysyvää ja mikä vaihtelee, ja ilmaistaan ratkaisu selkeinä vaiheina. Ohjelmointi on yksi paikka, jossa ohjelmallista
ajattelua käytetään, mutta se ei ole ainoa paikka. Resepti, help deskin toimintaohje ja paloharjoituksen ohje ovat
kaikki ohjelmallisen ajattelun muotoja. Ohjelmointi tulee kunnolla mukaan viikolla 7.

### Oppitunnin 2 väärinkäsitykset

Väärinkäsitys: “Algoritmit ovat vain tietojenkäsittelytieteilijöitä varten.”
Korjaus: Jokainen resepti on algoritmi. Jokainen bussireittiohje on algoritmi. Jokainen aamurutiini on algoritmi. Sana
algoritmi nimeää jotakin, mitä opiskelijat tekevät jo valmiiksi. Oppitunti antaa nimen taidolle, joka heillä jo on; se ei
opeta täysin uutta taitoa.
Väärinkäsitys: “Algoritmin täytyy olla pitkä, jotta se lasketaan algoritmiksi.”
Korjaus: Kolme selkeää vaihetta voi olla pätevä algoritmi, jos ne saavuttavat tavoitteen ilman moniselitteisyyttä.
Pituus ei ole kriteeri; selkeys ja tavoitteen saavuttaminen ovat. Vastaavasti 30-vaiheinen ohje, joka on täynnä
epämääräisiä sanoja, on huono algoritmi.

### Oppitunnin 3 väärinkäsitykset

Väärinkäsitys: “Epätarkka tarkoittaa vain lyhyttä.”
Korjaus: Pitkä ohje voi silti olla epätarkka. Lyhyt ohje voi olla täysin täsmällinen. Epätarkkuus tarkoittaa sitä, onko
kirjaimellisella seuraajalla useampi kuin yksi puolustettava tapa toimia, ei sitä, kuinka monta sanaa ohjeessa
on.
Väärinkäsitys: “Jos ohje kuulostaa oikealta, kun luen sen, se on oikea.”
Korjaus: Oman ohjeen lukeminen itselle harvoin paljastaa moniselitteisyyttä, koska tiedät jo, mitä tarkoitit. Vain
testaaminen kirjaimellisella seuraajalla — luokkakaverilla, sisaruksella tai itselläsi 24 tuntia myöhemmin —
paljastaa aukot. Siksi oppitunnin 3 keskeinen toiminta on kirjaimellisena tietokoneena toimiminen.
Bonusväärinkäsitys, joka ilmestyy usein oppitunnilla 1 tai 3: “Jos lisään ‘ole kiltti’ tai ‘ystävällisesti’, tietokone
toimii mukavammin.”
Korjaus: Kirjaimellisella seuraajalla ei ole kohteliaisuuskanavaa. Sanat ole kiltti ja ystävällisesti eivät lisää eivätkä
vähennä kirjaimellista merkitystä, elleivät ympäröivät verbit muutu. Tämä on myös hyvä hetki huomauttaa, että
ihmisten kohteliaisuuskäytännöt eivät siirry suoraan kirjaimelliseen ohjeiden seuraamiseen.

## Oppitunti 1 — 90 minuutin suunnitelma

Aihe. Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Tietokone on ohjeiden kirjaimellinen seuraaja, joten
lopputuloksen ratkaisee ohjeen laatu — ei koneen älykkyys.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: 5 minuutin “kirjaimellinen Opettajan demo + koko ryhmä
robotti livenä” -demo yhdellä lapulla,
esimerkiksi “Hae minulle tuoli”. Sen
jälkeen opettaja kirjoittaa
ydinkysymyksen taululle.
0:10–0:25 Opettajan osuus: määrittele Opetuspuhe
ohjelmallinen ajattelu ensin omin sanoin
ja anna sen jälkeen lyhyt koko kurssin
määritelmä. Nimeä neljä klassista
pilaria: pilkkominen, mallien
tunnistaminen, abstraktio ja algoritmit.
Kerro, että jokaiselle tulee oma tuleva
viikkonsa.
0:25–0:55 Itsenäinen työ (30 min): jokainen Itsenäinen
opiskelija luonnostelee 6–10 vaiheen
ohjeen henkilökohtaiseen tehtävään,
jota hän oikeasti tekee. Ei seuraajaa
vielä — tämä on tehtävän 1.1
kirjoitusvaihe.
0:55–1:15 Parityö: opiskelijat vaihtavat luonnoksia Pari
ja lukevat toistensa ohjeet
kirjaimellisesti. Vastaanottaja alleviivaa
jokaisen vaiheen, joka on avoin
useammalle kuin yhdelle tulkinnalle.
Kirjoittaja katsoo ja pidättäytyy
selittämästä.
1:15–1:25 Koko ryhmän purku: rakenna taululle Koko ryhmä
“Arki vs. IT” -jako. Kerää 3–4 arjen
esimerkkiä kirjaimellisesta
väärinymmärryksestä (sisaruksen
voileipä, epäselvät reittiohjeet,
automaattinen tekstinkorjaus) ja 3–4 IT-
esimerkkiä (kirjoitusvirhe
hakulauseessa, tiedostopolku, josta
puuttuu kauttaviiva).
1:25–1:30 Lopun reflektiokysymys taululle sekä Koko ryhmä
yhden virkkeen ennakko oppitunnista 2.
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. Alun lämmittely käyttää yhden lapun tehtävästä A tiedostossa . Koko tehtävä `in-class-tasks.md`
A säästetään oppitunnille 3.
Mitä sanot ääneen lämmittelyssä. “Kohta yksi teistä esittää tietokonetta viiden minuutin ajan. Tietokone tekee vain
sen, mitä sanat sanovat — ei enempää eikä vähempää. Yleisön tehtävä on huomata hetki, jolloin yksi sana voikin
tarkoittaa useampaa asiaa.” Toteuta demo. Vastusta houkutusta purkaa sitä pitkästi; yksi virke riittää: “Huomatkaa,
että moniselitteisyys oli ohjeessa, ei vapaaehtoisessa.” Koko purku tehdään oppitunnilla 3.
Materiaalit. Taulu ja tussi; yksi moniselitteinen ohje paperilapulla; tulostettu lista neljästä pilarista nimeltä (moniste
vapaaehtoinen). Tällä tunnilla ei tarvita teknologiaa.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): ei dioja. Kirjaimellisen robotin demo tapahtuu livenä; dia kilpailisi sen kanssa.
• Opettajan osuus (0:10–0:25): pääpakan diat 4 → 7: Mitä ohjelmallinen ajattelu on? · Tietokone ottaa sinut
kirjaimellisesti · “Tee voileipä” — mikä voisi mennä pieleen? · Moniselitteisyys on ohjeessa, ei
tietokoneessa. Käy yksi dia noin 3–4 minuutissa. Pysähdy diaan 7 riittävän pitkäksi aikaa, jotta
uudelleenkehystys ehtii asettua.
• Itsenäinen työ (0:25–0:55): ei dioja näytölle. Opiskelijat tarvitsevat rauhallista kirjoitusaikaa ja tyhjän taulun.
• Parityö (0:55–1:15): jätä dia 7 näkyviin hiljaiseksi muistutukseksi siitä, että moniselitteisyys on ohjeessa, ei
seuraajassa.
• Purku (1:15–1:25): dia 5 on hyödyllinen, jos opiskelijoiden on vaikea keksiä arki- ja IT-esimerkkejä. Muuten
rakenna kaksisarakkeinen taulu alusta asti.
• Lopetus (1:25–1:30): ei dioja. Lopeta taululla.
Viikon 1 pääpakka riittää oppitunnin 1 opetusosuuteen. Lisäpakkaa ei tarvita.

## Oppitunti 2 — 90 minuutin suunnitelma

Aihe. Algoritmit arjessa: vaiheittaiset ohjeet ilman koodia.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Algoritmi on arkinen nimi selkeälle kirjaimellisten vaiheiden
sarjalle, ja algoritmin kirjoittamista voi harjoitella kuka tahansa ilman koodia.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: pyydä ryhmää huutamaan Koko ryhmä
kolme algoritmia arjesta. Kerää ne
taululle. Todennäköisiä vastauksia:
resepti, bussireitti, hampaiden harjaus.
Vastusta tarvetta korjata “vääriä”
vastauksia; kaikki järkevät vastaukset
kelpaavat.
0:10–0:25 Opettajan osuus: määrittele algoritmi, Opetuspuhe
nimeä neljä osaa — tavoite, syöte,
vaiheet, tuotos — ja käy yksi taulun
esimerkeistä läpi näiden neljän osan
kautta.
0:25–1:00 Itsenäinen työ (35 min): jokainen Itsenäinen
opiskelija kirjoittaa oman
aamualgoritminsa tai jonkin muun tutun
arjen algoritmin 7–12 numeroituna
vaiheena. Sivun alkuun nimetään
erikseen tavoite, syöte, vaiheet ja
tuotos.
1:00–1:20 Parityö: opiskelijat vaihtavat algoritmeja. Pari
Lukija ennustaa tuotoksen pelkkien
vaiheiden perusteella — kysymättä
kirjoittajalta. Sen jälkeen pari vertaa
ennustetta tarkoitukseen ja keskustelee
siitä, mitkä vaiheet olivat riittävän
tarkkoja paljastamaan tavoitteen. Tämä
on lyhennetty versio tehtävästä B
tiedostossa in-class-tasks.md; käytä
täyttä versiota, jos aikaa on.
1:20–1:28 Koko ryhmän purku: kerää yksi havainto Koko ryhmä
kolmelta parilta. Millainen vaihe oli
riittävän täsmällinen, jotta tavoite kävi
ilmeiseksi? Millainen vaihe oli liian
epämääräinen auttaakseen?
1:28–1:30 Kahden virkkeen ennakko oppitunnista Koko ryhmä
3.
Itsenäisen työn jakso: 35 minuuttia (39 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 60–80 minuutin jakso käyttää tehtävää B tiedostosta in-class-tasks.md (Algorithm relay).
Mitä sanot ääneen opetusosuudessa. “Algoritmilla on neljä osaa. Tavoite kertoo, mitä lopussa halutaan. Syöte
kertoo, mitä täytyy olla ennen kuin voi aloittaa. Vaiheet kertovat, mitä tehdään ja missä järjestyksessä. Tuotos
kertoo, mitä on olemassa, kun vaiheet on tehty. Jos jokin näistä puuttuu, algoritmi on keskeneräinen.” Käy sen
jälkeen läpi yksi taulun esimerkeistä, esimerkiksi pikanuudeleiden tekeminen: tavoite — kulhollinen kuumia
nuudeleita; syöte — vedenkeitin, vettä, nuudelipakkaus, kulho, haarukka; vaiheet — lueteltuna; tuotos — kulhollinen
syöntivalmiita kuumia nuudeleita. Älä lisää viidettä osaa, kuten esiehtoja tai jälkiehtoja. Neljä riittää viikolle 1.
Esimerkki opiskelijalle: “Tavoite: lähetän opettajalle tiedoston. Syöte: valmis tiedosto, opettajan sähköpostiosoite,
nettiyhteys. Vaiheet: avaa sähköposti, kirjoita osoite, liitä tiedosto… Tuotos: opettaja saa tiedoston.”
Materiaalit. Taulu ja tussi. Paperia ja kyniä. Ei teknologiaa.
Diavihjeet — pääpakka slides.md + lisäpakka.
• Lämmittely (0:00–0:10): ei dioja. Kerää arjen algoritmit taululle livenä.
• Opettajan osuus (0:10–0:25): pääpakan diat 8 → 10: Algoritmi — nimi sille, mitä jo teet · Algoritmin osat
(tavoite · syöte · vaiheet · tuotos) · Kaksi algoritmia, yksi tavoite. Etene hitaasti diassa 9 — neljän osan
täytyy jäädä mieleen.
• Saatavilla oleva lisäpakka: slides-l2-algorithm-walkthrough.md (6 lyhyttä diaa) käy neljä osaa läpi
yhden konkreettisen esimerkin avulla (pikanuudeleiden tekeminen). Käytä tämä heti dian 9 jälkeen, jos
ryhmä tarvitsee kokonaisen esimerkin ennen oman kirjoittamisen aloittamista. Ohita se, jos taululla
tehty läpikäynti riittää.
• Itsenäinen työ (0:25–1:00): jätä dia 9 näkyviin hiljaiseksi malliksi (tavoite · syöte · vaiheet · tuotos). Muuten
ei dioja.
• Parityö (1:00–1:20): ei dioja; parit työskentelevät paperilla.
• Purku (1:20–1:28): ei dioja. Pysy taululla.
• Lopetus (1:28–1:30): ei dioja.

## Oppitunti 3 — 90 minuutin suunnitelma

Aihe. Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Ohje ei ole valmis silloin, kun se kuulostaa oikealta; se on valmis
silloin, kun kirjaimellinen seuraaja pystyy suorittamaan sen ilman kysymyksiä.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: kirjoita taululle kaksi lyhyttä Koko ryhmä
moniselitteistä ohjetta, esimerkiksi
“Tallenna tiedosto tavalliseen paikkaan”
ja “Vastaa hänelle siitä”. Ryhmä
nimeää, mikä on moniselitteistä, ja
ehdottaa tarkempaa versiota. Pidä
tempo kevyenä.
0:10–0:25 Opettajan osuus: määrittele täsmällinen Opetuspuhe
ja epätäsmällinen selkeällä yleiskielellä.
Käy läpi neljä tavallista
moniselitteisyyden mallia: epämääräiset
substantiivit (“tiedosto”), osoittavat sanat
(“täällä”, “tuolla”, “hänelle”), suhteellinen
aika (“myöhemmin”, “pian”) ja
epämääräinen määrä (“vähän”, “jonkin
verran”). Yksi esimerkki per malli.
0:25–0:55 Itsenäinen työ (30 min): jokainen Itsenäinen
opiskelija ottaa oppitunnin 2
aamualgoritminsa ja kirjoittaa sen
uudelleen poistaen moniselitteisyyttä.
Opiskelija ympyröi jokaisen muutetun
sanan ja kirjoittaa viereen yhden
virkkeen syyn.
0:55–1:20 Opettajajohtoinen tuntitehtävä: Tehtävä Koko ryhmä
A — “Kirjaimellinen robotti livenä”
tiedostosta in-class-tasks.md.
Vapaaehtoinen esittää kirjaimellista
tietokonetta kolmen valmiin lapun
avulla; ryhmä purkaa jokaisen;
uudelleenkirjoitukset tulevat taululle;
jokainen opiskelija lisää lopun minuutilla
yhden moniselitteisen sticky note
Aika Toiminta Muoto
-ohjeen.
1:20–1:28 Koko ryhmän purku: mikä neljästä Koko ryhmä
moniselitteisyyden mallista näkyi eniten
liveharjoituksessa? Kytke lyhyesti
takaisin L1-ajatukseen: moniselitteisyys
on ohjeessa, ei seuraajassa.
1:28–1:30 Ennakko viikkoon 2 — pilkkominen — Koko ryhmä
yhdellä virkkeellä: “Ensi viikolla
käsittelemme ongelmia, jotka ovat liian
suuria yhdelle algoritmille.”
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 55–80 minuutin jakso on tehtävän A täysi versio tiedostosta in-class-tasks.md. Lue tiedosto
ennen oppituntia: siinä on tarkat valmisteltavat paperilaput ja purkukysymykset.
Mitä sanot ääneen opetusosuudessa. “On neljä sanaryhmää, jotka aiheuttavat melkein aina moniselitteisyyttä.
Ensimmäinen on epämääräinen substantiivi: ‘tiedosto’, ‘painike’, ‘paikka’. Mikä tiedosto? Toinen on sana, joka
osoittaa johonkin, mitä lukija ei näe: ‘täällä’, ‘tuolla’, ‘tämä’, ‘hänelle’. Osoittaminen ilman sormea ei toimi kirjoitetussa
ohjeessa. Kolmas on suhteellinen aika: ‘myöhemmin’, ‘pian’, ‘lounaan jälkeen’. Pian milloin? Neljäs on
epämääräinen määrä: ‘vähän’, ‘jonkin verran’, ‘tarpeeksi’. Nämä neljä eivät ole ainoita moniselitteisyyden lähteitä,
mutta ne nappaavat suurimman osan siitä, mitä käytännössä näette.” Kirjoita neljä mallia taululle ja pidä ne
näkyvissä lopputunnin ajan.
Vinkki opiskelijalle: Jos ohjeessa on sana, jonka voisi korvata kysymyksellä “mikä?”, “missä?”, “milloin?” tai “kuinka
paljon?”, se kannattaa tarkentaa.
Materiaalit. Kolme valmista moniselitteistä ohjelappua tehtävään A. Taulu ja tussi. Sticky note -lappuja (yksi nippu
per rivi). Paperia ja kyniä.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): ei dioja; moniselitteiset ohjeet kirjoitetaan taululle, jotta ryhmä voi ehdottaa
uudelleenkirjoituksia.
• Opettajan osuus (0:10–0:25): pääpakan diat 11 → 14: Täsmälliset vs. epätäsmälliset ohjeet ·
Moniselitteisyyden metsästys — neljä mallia · Testaaminen kirjaimellisena robottina · Reunatapaukset (kevyt
johdanto). Dia 12 sisältää neljä mallia; kopioi ne myös taululle, jotta ne pysyvät näkyvissä, kun dia etenee.
• Itsenäinen työ (0:25–0:55): jätä dia 12 näkyviin viitteeksi, kun opiskelijat etsivät moniselitteisyyttä omasta
oppitunnin 2 algoritmistaan.
• Tuntitehtävä (0:55–1:20): ei dioja. Kirjaimellisen robotin demo elää luokkahuoneessa, ei seinällä.
• Purku (1:20–1:28): ei dioja; keskustele neljästä mallista taululla olevan liveaineiston perusteella.
• Lopetus (1:28–1:30): dia 18 (Mitä seuraavaksi: viikko 2 — pilkkominen) yhden virkkeen ennakkona, sitten
dia 19 (Kertaus — ydinkysymys) lähettämään opiskelijat oikean ajatuksen kanssa ulos.
Viikon 1 pääpakka riittää oppitunnin 3 opetusosuuteen. Lisäpakkaa ei tarvita.

## Fasilitointivinkit

### Ennen jokaista kolmesta oppitunnista

• Testaa ydinkysymys ensin itselläsi. Lue se ääneen kerran, hitaasti. Jos et muista sitä ulkoa, kun kävelet
luokkaan, opiskelijatkaan eivät omaksu sitä. Sanamuoto — “Miten puhun tietokoneelle niin, että se
ymmärtää, mitä haluan sen tekevän?” — näkyy diakannessa kahdesti; käytä samaa puheessasi.
• Luonnostele taulun rakenne etukäteen. Oppitunnille 1 hahmottele muistiinpanoihin “Arki vs. IT”
-kaksisarakkeinen ruudukko. Oppitunnille 2 hahmottele algoritmin neljä osaa. Oppitunnille 3 hahmottele
neljä moniselitteisyyden mallia. On hyvä piirtää tämä taululle livenä; on riskialtista miettiä sitä livenä.
• Lue alusta loppuun ennen oppituntia 1. Tehtävä A esiintyy viikon aikana kahdesti ja `in-class-tasks.md`
tarvitsee valmiit paperilaput. Jos opetatte yhdessä, sopikaa erikseen, kuka vastaa tehtävästä A — se toimii
paremmin, kun yhdellä henkilöllä on siitä omistajuus.

### Tunnin aikana

• Aloita aina arjen esimerkillä. Linjaus on selvä: arjen esimerkki ennen IT-esimerkkiä. Jos opiskelija tarjoaa
ensin IT-esimerkin, hyväksy se, mutta liitä siihen arjen esimerkki ennen etenemistä.
• Vaadi sanaa kirjaimellinen. Aina kun opiskelija sanoo tietokone on tyhmä, vaihda sana lempeästi:
“Kirjaimellinen — tietokone on kirjaimellinen. Tyhmä on sellainen, jonka olisi pitänyt tietää paremmin.
Tietokoneella ei koskaan ollut mahdollisuutta tietää.” Kaksi tai kolme korjausta oppitunnilla 1 riittää yleensä
koko viikolle.
• Pidä hiljaisuus, kun annat lapun vapaaehtoiselle. Uudet opettajat alkavat helposti selostaa
vapaaehtoisen toimintaa. Älä tee niin. Hiljaisuus on oppitunti.
• Käytä taulua uudelleenkirjoituksiin, älä dioja. Diat asettavat kysymyksen; uudelleenkirjoituksen täytyy
tapahtua taululla, jotta ryhmä näkee siirtymän moniselitteisestä täsmälliseen livenä.
• Vahdi aikaa 30–50 % -säännön vuoksi. Itsenäinen työ on se osa, jonka opettajat paineessa leikkaavat
ensin. Suojele sitä. Yllä olevat aikataulut antavat 30–35 minuuttia per oppitunti; älä leikkaa alle 27 minuutin.

## Vastauksia yleisiin opiskelijakysymyksiin

• “Onko Google algoritmi?” — Kyllä, Google-haku toteutetaan algoritmeilla — monilla algoritmeilla, myös
moderneilla koneoppimismenetelmillä. Viikolla 1 opiskelijalle riittävä vastaus on: kyllä, algoritmi arjen
merkityksessä — vaiheiden sarja, joka ottaa syötteen (hakusi) ja tuottaa tuotoksen (tuloslistan). Syvempi
selitys kuuluu myöhemmille viikoille.
• “Miksi automaattinen tekstinkorjaus ei ymmärrä minua?” — Koska automaattinen tekstinkorjaus on omalla
tavallaan myös kirjaimellinen: se noudattaa sääntöjä siitä, mitkä kirjainjonot näyttävät miltäkin sanoilta, eikä
sillä ole käsitystä siitä, mitä tarkoitit. Käytä tätä sillaksi ajatukseen “moniselitteisyys on ohjeessa, ei
tietokoneessa”.
• “Tuleeko tämä arvioitavaan tehtävään?” — Viikolla 1 ei ole arvioitavaa tehtävää. AT1 tulee viikon 2 lopussa.
Tällä viikolla tehdyt muistiinpanot ovat AT1:n raaka-ainetta; se on rehellinen vastaus.
• “Tarvitsenko tietokonetta kotitehtävään?” — Et. Tehtävät 1.1 ja 1.4 voi tehdä paperilla, kynällä ja halukkaalla
seuraajalla. Tehtäviin 1.2 ja 1.3 tarvitaan vain paperia. Ainoa “tietokone”, jonka viikko 1 tarvitsee, on
luokkahuoneessa oleva kirjaimellinen tietokone.
• “Saanko käyttää ChatGPT:tä?” — Saat sillä tavalla kuin tehtävä 1.2 kuvaa: sparrauskumppanina, joka tökkii
ajatteluasi. Et saa liittää sen tuottamaa tekstiä suoraan palautukseksi. Erityisesti tehtävää 1.1 ei voi
teeskennellä LLM:n avulla, koska se vaatii oikean seuraajan ja havaittavan artefaktin.

## Formatiivisen arvioinnin vinkit

Viikolla 1 ei ole summatiivista arviointia. Formatiivisten tarkistusten tehtävä on tehdä opiskelijoiden ymmärrys
näkyväksi varhain, jotta väärinkäsityksiä voidaan korjata ennen viikon 2 pilkkomis-käsitettä. Käytä yhdellä
oppitunnilla yksi tai kaksi seuraavista; älä yritä käyttää kaikkia.

### Oppituntikohtaiset epämuodolliset tarkistukset

• Oppitunti 1 — poistumislappu (3 min tunnin lopussa). Jokainen opiskelija kirjoittaa yhden virkkeen
vastauksena kysymykseen: “Mitä omin sanoin tarkoittaa, että tietokone on kirjaimellinen?” Kerää laput,
silmäile ne matkalla oppitunnille 2 ja aloita oppitunti 2 lukemalla ääneen kaksi nimetöntä vahvaa vastausta.
Vääriä vastauksia ei korjata julkisesti; yllä oleva väärinkäsitysten lista kertoo, mitä kannattaa palata
käsittelemään oppitunnin 2 lämmittelyssä.
• Oppitunti 1 — tauluäänestys. Näytä kolme väitettä: (a) “Tietokone on tyhmä.” (b) “Tietokone on
kirjaimellinen.” (c) “Se riippuu.” Jokainen nostaa kätensä yhden puolesta. Käsien jakauma kertoo, onko
ydinuudelleenkehystys mennyt perille; vahva (a)- tai (c)-äänestys tarkoittaa, että asiaan täytyy palata ennen
etenemistä.
• Oppitunti 2 — parien raportointi (2 min parityön jälkeen). Pyydä kahta paria nimeämään yksi kohta parin
algoritmista, joka oli selkeä, ja yksi kohta, joka oli epämääräinen. Kuuntele, käyttävätkö opiskelijat sanoja
tavoite, syöte, vaiheet, tuotos — se on onnistumisen merkki.
• Oppitunti 2 — yhden minuutin paperi. Tunnin lopuksi: “Kirjoita yksi algoritmi, jota käytit tänään mutta jota
et ennen tätä tuntia ajatellut algoritmina.” Lue kolme oppitunnin 3 alussa lämmittelynä.
• Oppitunti 3 — sticky note -keruu. Tehtävä A päättyy jo sticky noteihin; säilytä ne. Opiskelijoiden
kirjoittamien moniselitteisten ohjeiden malli on itsessään arvio siitä, kuinka hyvin he tunnistavat
moniselitteisyyttä omassa kielessään.
• Oppitunti 3 — poistumislappu. “Nimeä moniselitteisyyden malli, jonka löydät helpoimmin, ja se, jonka
löydät vaikeimmin.” Käytä vastauksia viikon 2 lämmittelyesimerkkien valintaan.

### Mitä kuuntelet koko viikon ajan

Kaksi lausetta, jotka merkitsevät aitoa ymmärrystä viikon 1 loppuun mennessä, ovat:
• “Ohje on moniselitteinen” — ei “tietokone on väärässä”.
• “Testaan sen kirjaimellisella seuraajalla” — ei “luen sen uudelleen”.
Jos nämä kaksi ilmausta näkyvät opiskelijoiden puheessa oppituntiin 3 mennessä, viikko 1 on tehnyt tehtävänsä ja
viikko 2 (pilkkominen) voi rakentua sen päälle ilman korjaavaa kertausta.
