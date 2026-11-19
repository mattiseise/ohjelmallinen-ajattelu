# Viikko 5 — Opettajan materiaalit

Tämä dokumentti kattaa viikon 5 kaikki kolme oppituntia (L13, L14, L15) samassa paikassa. Viikko rakentuu saman
ydinviestin ympärille, jonka opiskelijat näkevät:
“Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: järjestys, ehto ja toisto.”
Viikko 5 nimeää kolme loogista rakennetta, joista jokainen kuvattu prosessi rakentuu, ja harjoituttaa opiskelijoita
tunnistamaan ne arkikielestä ennen kuin he kohtaavat ne koodina viikoilla 6–8. Viikko 5 on myös suora perusta
AT2:lle, joka tulee viikon 5 lopussa / viikon 6 aikana ja pyytää prosessin kuvausta, jossa käytetään nimenomaisesti
kaikkia kolmea rakennetta.
Kolme oppituntia muodostavat yhden kaaren: L13 nimeää oletuksen (järjestys), L14 nimeää testin, joka jakaa polun
(ehto), ja L15 nimeää testin, joka palauttaa polun takaisin (toisto, jolla on pysäytys). Koodia ei esitellä tällä viikolla.
Pseudokoodimainen merkintä ( , , ) on sallittu, mutta sitä

```
if … then … else … for each … repeat until …
```

käsitellään englanninkielisenä lyhenteenä, ei muodollisena kielenä. Varsinainen pseudokoodi tulee viikolla 6.
Ristiinviittaukset: L14:n ja L15:n tuntitehtävät kuvataan saman kansion tiedostossa in-class-tasks.md.
Vinkki opettajalle: Palaa joka tunnilla kysymykseen “mikä on testi?” ja “mikä on pysäytys?”. Nämä kaksi kysymystä
tekevät ehdon ja toiston opiskelijalle konkreettisiksi.

## Viikon 5 oppimistavoitteet (Bloom-taksonomian mukaan)

Viikko 5 pysyy tasoilla Muistaminen ja Ymmärtäminen, ja kaikilla kolmella oppitunnilla sallitaan kevyt
Soveltaminen: ehto ilmaistaan if … then … else … -muodossa, toisto ilmaistaan selkeällä pysäytyksellä, piirretään
pieni päätöspuu ja yhdistetään kaikki kolme rakennetta yhteen prosessikuvaukseen. Viikon 5 tavoitteissa vältettävät
verbit ovat luoda, rakentaa, suunnitella, kehittää, arvioida, arvostella, debugata, optimoida, pilkkoa. Analysoida voi
esiintyä kevyesti syventävissä tehtävissä, mutta ei tavoitteissa. Kurssin korkeammat Bloom-tasot palaavat
myöhemmillä viikoilla.

### Oppitunti 13 — Järjestys: ohjelma etenee vaihe vaiheelta

• Muistaminen: opiskelija osaa määritellä järjestyksen omin sanoin: “tehdään yksi vaihe toisen jälkeen
kiinteässä järjestyksessä”.
• Ymmärtäminen: opiskelija osaa tunnistaa järjestysrungon arjen prosessista (resepti, käyttöönoton
tarkistuslista, aamurutiini).
• Ymmärtäminen: opiskelija osaa selittää, miksi vaiheiden järjestyksellä yleensä on väliä, ja antaa yhden
esimerkin, jossa kahden vaiheen vaihtaminen rikkoo prosessin.
• Kevyt soveltaminen: opiskelija osaa kirjoittaa 6–10 vaiheen järjestyksen tutulle prosessille ja tehdä
järjestyksen näkyväksi numeroinnilla.

### Oppitunti 14 — Ehdot: if-then-else-ajattelu ja päätöspuut

• Muistaminen: opiskelija osaa määritellä ehdon omin sanoin: “testi, joka päättää, mikä vaihe tapahtuu
seuraavaksi”.
• Ymmärtäminen: opiskelija osaa tunnistaa if … then … else … -muodon arjen säännöissä
(salasanasäännöt, tikettien ohjaussäännöt, “jos sataa, mene bussilla”).
• Ymmärtäminen: opiskelija osaa selittää eron muotojen if … then … (ei vaihtoehtoista haaraa) ja if …
then … else … (vaihtoehtoinen haara) välillä.
• Kevyt soveltaminen: opiskelija osaa piirtää yksinkertaisen kaksi- tai kolmihaaraisen päätöspuun tutusta
arjen säännöstä.
• Kevyt soveltaminen: opiskelija osaa ilmaista todellisen elämän säännön luonnollisella kielellä if … then
… else … -muodossa.

### Oppitunti 15 — Toisto: saman asian tekeminen monta kertaa

• Muistaminen: opiskelija osaa määritellä toiston omin sanoin: “sama vaihe tai vaiheiden lohko tehdään
useammin kuin kerran, ja sillä on selkeä pysäytys”.
• Ymmärtäminen: opiskelija osaa erottaa muodot for each (tunnettu lista), repeat until (pysäytysehto) ja while
(jatkamisehto) arjen tilanteissa.
• Ymmärtäminen: opiskelija osaa tunnistaa toiston tutuissa prosesseissa (sähköpostilaatikon läpikäynti,
läsnäolon merkitseminen, puhelimen lataaminen).
• Kevyt soveltaminen: opiskelija osaa ilmaista todellisen elämän toistuvan toiminnon luonnollisella kielellä ja
lisätä selkeän pysäytys- tai jatkamisehdon.
• Ymmärtäminen: opiskelija osaa huomata eron kertaluonteisen vaiheen ja toistuvan vaiheen välillä
prosessikuvauksessa.

## Viikon 5 yleiset väärinkäsitykset

Alla on vähintään kaksi väärinkäsitystä per oppitunti. Ehkäise niitä silloin, kun ne sopivat luontevasti — useimmat
nousevat itsestään itsenäisen työn aikana tai luokittelupelissä.

### Oppitunnin 13 väärinkäsitykset

Väärinkäsitys: “Järjestys on liian itsestään selvä ollakseen rakennuspalikka.”
Korjaus: Useimmat todelliset bugit syntyvät yhdestä vaihdetusta vaiheesta. Järjestys on oletus — kirjoitetun haaran
tai silmukan puuttuminen — ja juuri oletuksessa tapahtuu rikkoutumisia, koska kukaan ei ajattele testata sitä. Se on
perusta, jonka päällä kaksi muuta rakennetta ovat.
Väärinkäsitys: “Jos en kirjoita ehtoa, prosessissa ei ole päätöksiä.”
Korjaus: Se tarkoittaa, että jokainen vaihe on ehdoton — jokainen vaihe tapahtuu aina kirjoitetussa järjestyksessä.
Järjestys on haarautumisen puuttumista, ei tärkeyden puuttumista. 6-vaiheinen järjestys ilman ehtoja on silti
kokonainen prosessi.

### Oppitunnin 14 väärinkäsitykset

Väärinkäsitys: “if … then … on sama kuin if … then … else ….”
Korjaus: Ilman else-osaa seuraaja ei tee mitään ylimääräistä muuten. else-osan kanssa seuraaja tekee jotakin
muuta epätosella haaralla. “Jos maito haisee pahalta, heitä se pois” ja “Jos maito haisee pahalta, heitä se pois;
muuten kaada sitä kahviin” eivät ole sama ohje.
Väärinkäsitys: “Yhdistelmäehdot ovat edistyneitä, joten minun pitäisi välttää niitä.”
Korjaus: Opiskelijat käyttävät AND- ja OR-ajattelua joka päivä: “jos minulla on bussikortti JA siinä rahaa, voin
mennä bussilla”. Vain symbolit ovat edistyneitä; ajattelu ei ole. Viikolla 5 yhdistelmäehdot pysyvät yleiskielessä;
symbolista logiikkaa ei tule lainkaan.

### Oppitunnin 15 väärinkäsitykset

Väärinkäsitys: “Silmukka on vain monta kertaa kirjoitettu järjestys.”
Korjaus: Silmukka on yksi lause sekä pysäytysehto. Jos kirjoitat “tarkista seuraava kuva, tarkista seuraava kuva…”
sata kertaa, et ole ymmärtänyt toistoa. for each ja repeat until sanovat yhdellä rivillä: “sama asia uudestaan,
selkeällä pysäytyksellä”.
Väärinkäsitys: “repeat until pysähtyy aina.”
Korjaus: Se pysähtyy vain, jos pysäytysehto voidaan oikeasti havaita ja saavuttaa. “Toista, kunnes ymmärrät” ei ole
pysäytys — kirjaimellinen seuraaja ei voi tarkistaa sitä. Rehelliset toistot tarvitsevat havaittavan pysäytyksen, ja
monet tarvitsevat myös turvapysäytyksen (“…tai pysähdy 10 yrityksen jälkeen”) karkaavan tapauksen varalle.
Bonusväärinkäsitys: “for each on järjestyksen laji, koska se on vain vaihelista.”
Korjaus: for each on toisto — sama vaihe tehdään kerran jokaiselle listan asialle. Lista on pysäytys: seuraaja
pysähtyy, kun asioita ei ole enää. Yksi lause, ei monta.

## Oppitunti 13 — 90 minuutin suunnitelma

Aihe. Järjestys: ohjelma etenee vaihe vaiheelta.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Järjestys on oletus — kun mitään muuta ei sanota, tee A, sitten
B, sitten C on se, mitä kirjaimellinen seuraaja tekee, joten kirjoittamasi järjestys on järjestys, jonka saat.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: ryhmä nimeää ääneen kolme arjen järjestystä. Todennäköisiä vastauksia: teeresepti, aamurutiini, reitti kouluun. Opettaja kirjoittaa ne taululle ja vaihtaa kahden vaiheen paikkaa yhdessä niistä, esimerkiksi “kaada kiehuva vesi ennen kuin laitat teepussin”. Kysy ryhmältä, mitä tapahtuu. | Koko ryhmä |
| 0:10–0:25 | Opettajan osuus: määrittele järjestys; käy yksi arjen järjestys (tee tai aamurutiini) ja yksi IT-järjestys (käyttöönoton tarkistuslista yleiskielellä) rinnakkain. Nimeä järjestys ja riippuvuus epämuodollisesti. | Opetuspuhe |
| 0:25–0:55 | Itsenäinen työ (30 min): jokainen opiskelija kirjoittaa 6–10 vaiheen järjestyksen tutulle prosessille, jota hän oikeasti tekee, ja numeroi jokaisen vaiheen. Sivun alkuun nimetään selvästi tavoite, syöte ja tuotos. Tämä on tehtävän 5.1 avausliike — ehdot ja toisto lisätään L14:ssä ja L15:ssä. | Itsenäinen |
| 0:55–1:15 | Parityö: opiskelijat vaihtavat järjestyksiä ja yrittävät rikkoa parin prosessin vaihtamalla kahden vaiheen paikkaa, joiden pari ajattelee ehkä vielä toimivan. Kirjoittaja merkitsee jokaisen vaihdon: “järjestyksellä on väliä” tai “järjestyksellä ei ole väliä”. | Pari |
| 1:15–1:25 | Koko ryhmän purku: kerää 2–3 tapausta, joissa järjestyksellä todella oli väliä; rakenna taululle kaksisarake “järjestyksellä on väliä / järjestyksellä ei ole väliä”. Kytke L13:n ydinviestiin. | Koko ryhmä |
| 1:25–1:30 | Lopetus: yhden virkkeen ennakko oppitunnista 14 — “Seuraavaksi nimeämme hetken, jolloin prosessi jakautuu kahteen.” | Koko ryhmä |
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. L13 ei käytä tuntitehtävää tiedostosta . Parityö on paikallinen tälle `in-class-tasks.md`
oppitunnille. Tehtävä A (luokittelupeli) alkaa L14:ssä.
Mitä sanot ääneen. “Järjestys on kolmesta rakennuspalikasta helpoin — ja aliarvostetuin, koska kukaan ei huomaa
sitä ennen kuin se rikkoutuu. Katsotaan, mitä tapahtuu, kun vaihdan kahden vaiheen paikan.” Vaihda kaksi vaihetta
teereseptissä (vesi ennen teepussia). Pidä tauko. “Seuraaja teki täsmälleen sen, mitä uusi järjestys sanoi — ja tee
meni pieleen. Järjestys on oletus; oletuksessa bugit piilevät.”
Materiaalit. Taulu ja tussi; paperia ja kyniä; teknologiaa ei tarvita.
Diavihjeet — pääpakka . `slides.md`
• Lämmittely (0:00–0:10): ei dioja. Taulu kantaa kolme järjestystä ja vaihdetun version.
• Opettajan osuus (0:10–0:25): pääpakan diat 4 → 6: Järjestys — oletusliike · Kun järjestyksellä on väliä ·
Järjestys työssä — käyttöönoton tarkistuslista. Käytä eniten aikaa diaan 5; vaihto on kohta, jossa oppi
asettuu.
• Itsenäinen työ (0:25–0:55): jätä dia 4 näkyviin hiljaiseksi muistutukseksi viikon 1 tavoite–syöte–vaiheet–
tuotos-rakenteesta.
• Parityö (0:55–1:15): ei dioja; parit työskentelevät paperilla.
• Purku (1:15–1:25): ei dioja. Käytä taulua “järjestyksellä on väliä / järjestyksellä ei ole väliä”
-kaksisarakkeeseen.
• Lopetus (1:25–1:30): ei dioja.

## Oppitunti 14 — 90 minuutin suunnitelma

Aihe. Ehdot: if-then-else-ajattelu ja päätöspuut.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Ehto on testi, joka jakaa prosessin polun kahteen tai useampaan
osaan, ja testin nimeäminen yleiskielellä riittää tekemään jaon näkyväksi kirjaimelliselle seuraajalle.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: opettaja kirjoittaa taululle sanallisen arjen säännön — “Jos sataa, mene bussilla, muuten kävele.” Ryhmä piirtää puun paperille 2 minuutissa. Opettaja piirtää sen jälkeen kanonisen version taululle. | Koko ryhmä |
| 0:10–0:30 | Opettajan osuus: määrittele ehto; käy läpi `if … then …`, `if … then … else …` ja `if … then … else if … then … else …`. Kävele yksi päätöspuu alusta loppuun (sateenvarjosääntö). Jos lisäpakka `slides-l14-decision-trees.md` on mukana, käytä se tässä kokonaan. | Opetuspuhe |
| 0:30–0:57 | Itsenäinen työ (27 min): jokainen opiskelija laajentaa L13-järjestystään lisäämällä vähintään yhden ehdon, jossa testi on nimetty yleiskielellä muodossa `if … then … else …`. Hän myös piirtää ehdon pieneksi puuksi. | Itsenäinen |
| 0:57–1:20 | PAKOLLINEN opettajajohtoinen tuntitehtävä — “Etsi if” (tehtävän A ensimmäinen puolisko tiedostossa `in-class-tasks.md`, noin 23 min). Opettaja lukee lyhyitä arki- ja IT-lauseita; ryhmä äänestää ehto / ei ehtoa ja nimeää testin jokaisesta. Rajatapaukset kirjoitetaan uudelleen taululla. | Koko ryhmä |
| 1:20–1:28 | Koko ryhmän purku: mitkä lauseet olivat vaikeimpia luokitella? Missä testi oli piilossa arkisen sanamuodon takana? | Koko ryhmä |
| 1:28–1:30 | Lopetus: yhden virkkeen ennakko oppitunnista 15 — “Seuraavaksi nimeämme hetken, jolloin vaihe tapahtuu useammin kuin kerran.” | Koko ryhmä |
Itsenäisen työn jakso: 27 minuuttia (30 % 90 minuutista). Täyttää 30–50 % -säännön alarajan. Suojele tätä
jaksoa — jos opetusosuus venyy, leikkaa opetusosuudesta, älä itsenäisestä työstä.
Ristiinviittaukset. 57–80 minuutin jakso on tehtävän A ensimmäinen puolisko tiedostossa in-class-tasks.md
(Find the if). Valmistele tiedoston pino 1 etukäteen. Jos haluat käyttää tehtävää B (Live decision tree on the board)
osana opetusosuutta, vaihda se 30–55 minuutin jaksoon ja lyhennä itsenäistä työtä 5 minuutilla, mutta älä mene
alle 27 minuutin.
Mitä sanot ääneen. “Ehto on testi, joka jakaa polun. Jos testi on tosi, seuraaja menee yhtä tietä; jos ei, toista — tai
ilman elseä seuraaja vain jatkaa eteenpäin. Hyvässä ehdossa on kolme asiaa: rehellinen testi, jonka seuraaja voi
oikeasti tarkistaa; nimetty toiminto tosi-haarassa; ja nimetty toiminto — tai selkeä ‘ei mitään ylimääräistä’ — epätosi-
haarassa.” Käy sateenvarjosääntö taululla: “jos sataa nyt, ota sateenvarjo; muuten jos ennuste lupaa sadetta, ota
sateenvarjo; muuten jätä se kotiin.” Piirrä kolmihaarainen puu.
Vinkki opiskelijalle: Ehto alkaa yleensä kysymyksellä, johon voi vastata kyllä/ei tai valita yhden useasta
vaihtoehdosta. Kirjoita ensin kysymys, vasta sitten haarat.
Materiaalit. Taulu ja tussi; paperia ja kyniä; pino 1 tiedostosta in-class-tasks.md valmiina lappuina tai tulostettuna
listana. Jos toimitat slides-l14-decision-trees.md -pakan, pidä se valmiina opetusosuutta varten.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): dia 7 (Ehto — testi, joka jakaa polun) näkyviin, kun ryhmä piirtää sateenvarjopuun
paperille.
• Opettajan osuus (0:10–0:30): pääpakan diat 7 → 10: Ehto — testi, joka jakaa polun · if … then … else …
· Päätöspuu — jaon piirtäminen · Ehto työssä — salasanan tarkistus. Jos lisäpakka on mukana, käytä
slides-l14-decision-trees.md alusta loppuun pääpakan diojen 9 ja 10 välissä — se käy
sateenvarjopuun hitaasti läpi ja peilaa sen IT-kirjautumisesimerkkiin.
• Itsenäinen työ (0:30–0:57): jätä dia 8 näkyviin hiljaiseksi viitteeksi if … then … else … -muodosta.
• Tuntitehtävä (0:57–1:20): ei dioja. Luokittelupeli elää taululla.
• Purku (1:20–1:28): ei dioja; käy taulun uudelleenkirjoitetut rajatapaukset läpi.
• Lopetus (1:28–1:30): ei dioja. Jos et toimita lisäpakkaa slides-l14-decision-trees.md, pääpakan dia 9
kantaa yksin päätöspuuvisuaalin. Kävele se hitaasti; muu opetus nojaa siihen.

## Oppitunti 15 — 90 minuutin suunnitelma

Aihe. Toisto: saman asian tekeminen monta kertaa.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Toisto on tapa sanoa “sama asia uudestaan, selkeällä
pysäytyksellä” — ja pysäytyksen nimeäminen yleiskielellä erottaa hyödyllisen toiston karkaavasta toistosta.
| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: ryhmä nimeää kolme toistoa, joita he ovat tehneet tähän mennessä tänään. Todennäköisiä vastauksia: hampaiden harjaus, liikennevalojen ohittaminen, chatin päivittäminen uusien viestien varalta. Opettaja kirjoittaa ne taululle. | Koko ryhmä |
| 0:10–0:28 | Opettajan osuus: määrittele toisto; näytä kolme muotoa (`for each` / `repeat until` / `while`) yhdellä esimerkillä per muoto. Esittele ajatus “pysäytysehto on turvavyö” ja karkaava toisto. | Opetuspuhe |
| 0:28–0:58 | Itsenäinen työ (30 min): jokainen opiskelija lisää toiston omaan L13+L14-prosessiinsa ja kirjoittaa selkeän pysäytysehdon. Hän kirjoittaa myös yhden virkkeen siitä, miltä karkaava tapaus näyttäisi ja miten turvapysäytys korjaisi sen. | Itsenäinen |
| 0:58–1:20 | Suositeltu opettajajohtoinen tuntitehtävä — “Etsi silmukka” (tehtävän A toinen puolisko tiedostossa `in-class-tasks.md`, noin 22 min). Opettaja lukee lyhyitä arki- ja IT-lauseita; ryhmä äänestää toisto / ei toistoa ja nimeää pysäytysehdon jokaisesta. | Koko ryhmä |
| 1:20–1:28 | Koko ryhmän purku: kerää kolme karkaavaa tapausta (“toista kunnes ymmärrät”, “kun sivu latautuu edelleen”, “jokaiselle listan asialle”). Keskustelkaa, miltä rehellinen pysäytys näyttäisi kullekin. | Koko ryhmä |
| 1:28–1:30 | Lopetus: ennakko viikosta 6 — “Ensi viikolla tiukennamme nämä luonnollisen kielen kuvaukset paperilla vähän lähemmäs koodia. Sitä kutsutaan pseudokoodiksi.” Mainitse, että AT2 tulee viikon lopussa / viikon 6 aikana. | Koko ryhmä |
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 58–80 minuutin jakso on tehtävän A toinen puolisko tiedostossa in-class-tasks.md (Find the
loop). Valmistele pino 2 etukäteen. Tehtävä A on viikon pakollinen tehtävä — jos suoritit L14-puoliskon, kannattaa
suorittaa myös L15-puolisko sekä symmetrian vuoksi että siksi, että pinon 2 while-kompastuslappu on diagnostinen
hetki kertaluonteinen vaihe vs. toistuva vaihe -väärinkäsitykselle.
Mitä sanot ääneen. “Toisto on kolmas rakennuspalikka ja vaarallisin, koska jokainen toisto voi jatkua ikuisesti, jos
pysäytys on epärehellinen. Kolme muotoa: for-each, kun lista tunnetaan; repeat-until, kun pysäytys riippuu jostakin
tapahtuvasta asiasta; while, kun testi tarkistetaan ennen jokaista toistoa. Kaikki kolme tarvitsevat pysäytyksen, jonka
kirjaimellinen seuraaja voi oikeasti havaita.” Kirjoita sitten taululle “toista kunnes ymmärrät”: “Mistä seuraaja tietää,
milloin pysähtyä?” Hiljaisuus on oppitunti. Käännä se muotoon “…tai pysähdy 10 yrityksen jälkeen” turvavyöksi.
Materiaalit. Taulu ja tussi; paperia ja kyniä; pino 2 tiedostosta in-class-tasks.md valmiina lappuina tai tulostettuna
listana.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): ei dioja. Kerää toistot taululle.
• Opettajan osuus (0:10–0:28): pääpakan diat 11 → 14: Toisto — tee uudestaan, pysäytyksellä · Kolme
toiston muotoa · Toisto työssä — sähköpostilaatikon läpikäynti · Pysäytysehto on turvavyö.
Sähköpostilaatikko-dia on se, johon kannattaa viipyä; sano ääneen, että se käyttää kaikkia kolmea
rakennuspalikkaa yhtä aikaa.
• Itsenäinen työ (0:28–0:58): jätä dia 12 näkyviin hiljaiseksi viitteeksi kolmelle muodolle (for each / repeat
until / while).
• Tuntitehtävä (0:58–1:20): ei dioja. Luokittelupeli elää taululla.
• Purku (1:20–1:28): ei dioja; kirjoita ryhmän keräämät kolme karkaavaa tapausta taululle.
• Lopetus (1:28–1:30): dia 18 (Mitä seuraavaksi: viikko 6 — pseudokoodi) yhden virkkeen ennakoksi, sitten
dia 19 (Kertaus — ydinviesti), jotta opiskelijat lähtevät sanasta sanaan -viestin kanssa.

## Fasilitointivinkit

### Ennen jokaista kolmesta oppitunnista

• Testaa ydinviesti itselläsi ensin. Lue se ääneen kerran, hitaasti: “Lähes mikä tahansa prosessi voidaan
kuvata kolmella rakennuspalikalla: järjestys, ehto ja toisto.” Se näkyy sanasta sanaan vähintään yhdessä
diassa ja vähintään kerran tiedostossa self-study.md. Peilaa sitä omassa puheessasi vähintään kahdesti
per oppitunti; se on viikon selkäranka.
• Luonnostele taulun rakenne. L13:lle luonnostele “järjestyksellä on väliä / järjestyksellä ei ole väliä”
-kaksisarake. L14:lle luonnostele sateenvarjopäätöspuu ja salasanasääntö. L15:lle luonnostele
sähköpostilaatikon läpikäynti, jossa näkyvät kaikki kolme rakennuspalikkaa yhtä aikaa. Livepiirtäminen on
hyvä; liveajattelu on riskialtista.
• Lue in-class-tasks.md alusta loppuun ennen oppituntia 14. Tehtävä A esiintyy kahdessa puoliskossa
— pino 1 L14:ssä ja pino 2 L15:ssä — ja tarvitsee laput tai tulostetun listan etukäteen.

### Tunnin aikana

• Vaadi kanonisia nimiä. Järjestys, ehto, toisto. Synonyymit (valinta, haara, silmukka, iteraatio) ovat
ohimennen ok, mutta parita ne aina ensimmäisellä kerralla kanoniseen nimeen.
• Aloita aina arjen esimerkillä. Salasanan tarkistussääntö, sähköpostilaatikon läpikäynti ja käyttöönoton
tarkistuslista tulevat vasta teereseptin, “jos sataa, mene bussilla” -säännön ja “merkitse jokainen nimi
läsnäololistaan” -esimerkin jälkeen. Jos opiskelija tarjoaa ensin IT-esimerkin, hyväksy se, mutta liitä mukaan
arjen esimerkki ennen etenemistä.
• Suojele itsenäisen työn jaksoa. Viikko 5 rakentaa AT2:ta syöttävän artefaktin kolmen oppitunnin aikana.
Jos 90 minuutin suunnitelma lipsuu, leikkaus tulee purusta tai opetusosuudesta, ei itsenäisestä työstä. Älä
mene alle 27 minuutin per oppitunti.
• Älä lipsu koodiin. Kun opiskelija kirjoittaa paperille if (x > 0) {, kirjoita se lempeästi taululle muotoon “jos x
on suurempi kuin 0, niin …” yleiskielellä. Koodi tulee viikolla 7.
• Nimeä testi, älä vastausta. Kun opiskelija piirtää päätöspuun epämääräisellä haaralla kuten “jos se menee
pieleen”, kysy: “minkä tarkan testin kirjaimellinen seuraaja tekisi tietääkseen, että se meni pieleen?”
• Rehelliset pysäytykset. Kun opiskelija kirjoittaa “toista kunnes valmis”, kysy: “mistä seuraaja tietää, että se
on valmis?” Jos vastaus on “se vain tietää”, pysäytys ei ole vielä rehellinen.
• Vältä infinite loop -kauhutarinaa. Kurssin sisäiset ilmaukset ovat karkaava toisto ja ei rehellistä pysäytystä.
Infinite loop tulee, kun koodi tulee.

## Vastauksia yleisiin opiskelijakysymyksiin

• “Onko if … then … sama kuin if … then … else …?” — Ei. Ilman else-osaa seuraaja ei tee muuten mitään
ylimääräistä. else-osan kanssa seuraaja tekee epätosella haaralla jotakin eriä. Molemmat muodot ovat
kelvollisia; ne sanovat eri asioita.
• “Voiko ehdolla olla enemmän kuin kaksi haaraa?” — Kyllä, muodolla else if. Kolme tai neljä haaraa on
normaalia: “jos sataa, mene bussilla; muuten jos olet myöhässä, juokse; muuten kävele.” Yli viisi haaraa
tarkoittaa usein, että sääntö piilottaa syvemmän rakenteen.
• “Onko for each silmukka vai järjestys?” — Silmukka. Se tekee saman asian kerran jokaiselle listan alkiolle,
ja lista on pysäytysehto. Yksi lause, ei monta.
• “Mitä jos repeat until voisi jatkua ikuisesti?” — Lisää turvapysäytys: “…tai pysähdy 10 yrityksen jälkeen”,
“…tai pysähdy 30 minuutin jälkeen”. Jokaisessa rehellisessä toistossa on vähintään yksi havaittava
pysäytys. Turvapysäytys on osa suunnittelua, ei anteeksipyyntö.
• “Tuleeko tämä AT2:een?” — Kyllä. Artefakti, jonka rakennat L13:ssa, L14:ssa ja L15:ssa, on AT2-artefakti
pienemmässä mittakaavassa. AT2 tulee viikon 5 lopussa / viikon 6 aikana. Säilytä muistiinpanot.
• “Saanko käyttää koodia AT2:ssa?” — Et vielä. AT2 on luonnollista kieltä, jossa if … then … else … ja for
each / repeat until / while toimivat vapaana, englanninkielistyylisenä merkintänä. Pseudokoodi tulee
ensi viikolla. AT2 arvioi ajattelua, ei syntaksia.
• “Mitä eroa on while- ja repeat until -muodoilla?” — while X, keep doing … tarkistaa testin ennen jokaista
toistoa: jos X on jo epätosi, seuraaja tekee sisäisen vaiheen nolla kertaa. repeat … until X tekee sisäisen
vaiheen vähintään kerran ja tarkistaa vasta sitten. Lue oma silmukkasi ääneen ja kysy: “tekeekö seuraaja
ensimmäisellä kerralla mitään?”

## Formatiivisen arvioinnin vinkit

Viikolla 5 ei ole omaa summatiivista arviointia — summatiivinen artefakti on AT2, joka palautetaan viikon 5
lopussa / viikon 6 aikana. Formatiivisten tarkistusten tehtävä on tehdä ymmärrys näkyväksi ajoissa, jotta opiskelijat,
jotka sekoittavat kolme rakennuspalikkaa, voidaan auttaa ennen AT2:ta. Käytä yksi tai kaksi per oppitunti.

### Oppituntikohtaiset epämuodolliset tarkistukset

• Oppitunti 13 — poistumislappu (3 min tunnin lopussa). Jokainen opiskelija kirjoittaa yhden virkkeen
vastauksena: “Nimeä yhden tänään suorittamasi prosessin järjestysrunko.” Silmäile laput matkalla L14:ään;
jos useampi kirjoittaa “minulla ei ole sellaista”, palaa L13:n ydinviestiin L14:n alussa.
• Oppitunti 14 — tauluäänestys. Näytä taululla kolme lyhyttä sääntöä, esimerkiksi “jos sinulla on bussikortti
JA siinä rahaa, mene bussilla”, “jos maito haisee pahalta, heitä se pois”, “jos sataa, mene bussilla, muuten
kävele”. Kysy, missä on eniten haaroja päätöspuussa. Käsien jakauma kertoo, näkevätkö opiskelijat
rakenteen arkisen sanamuodon alla.
• Oppitunti 14 — sticky note -keruu tehtävän A lopussa. Jokainen opiskelija kirjoittaa yhden
moniselitteisen ehdon, jonka hän on kuullut tai sanonut tällä viikolla. Lue 3 satunnaisesti; ryhmä ehdottaa
rehellisen testin jokaiseen.
• Oppitunti 15 — sticky note -keruu. Jokainen opiskelija kirjoittaa yhden karkaavan toiston, jonka hän on
kuullut tai sanonut tällä viikolla (“toista kunnes ymmärrät”, “kun sivu latautuu edelleen”). Lue 3 satunnaisesti;
ryhmä ehdottaa turvapysäytyksen jokaiseen.
• Oppitunti 15 — yhden minuutin paperi viikon lopussa. “Nimeä yhdessä virkkeessä rakennuspalikka,
jonka tunnistat helpoimmin, ja se, jonka tunnistat vaikeimmin.” Koko ryhmän malli kertoo, mitä kannattaa
kerrata viikon 6 ensimmäisen viiden minuutin aikana.

### Mitä kuuntelet koko viikon ajan

Kolme lausetta, jotka merkitsevät aitoa ymmärrystä viikon 5 loppuun mennessä:
• “Missä testi on?” kun opiskelija lukee ehtoa.
• “Mikä on pysäytys?” kun opiskelija lukee toistoa.
• “Järjestys on selkäranka — ehto ja toisto riippuvat siitä.”
Jos nämä ilmaukset näkyvät opiskelijoiden puheessa L15:n loppuun mennessä, AT2 voi tulla ilman korjaavaa
kertausta. Jos ei, viikon 6 hyödyllisimmät 5 minuuttia ovat kolmen rakennuspalikan kertaus ennen pseudokoodin
tuloa. Luokittelupeli (tehtävä A tiedostossa in-class-tasks.md) on viikon keskeinen diagnostiikka. Ryhmä, joka
äänestää varmasti kompastuslappuihin, on valmis AT2:een.
