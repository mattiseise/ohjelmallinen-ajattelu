# Viikko 8 — Opettajan materiaalit

Tämä dokumentti kattaa oppitunnit L22, L23 ja L24. Viikon ydinviesti:
“Kurssi sulkee silmukan: otat pseudokoodin, jonka kirjoitit itse viikolla 6, käännät sen JavaScriptiksi tai
C#:ksi, ajat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi ei ole enää mystistä.”
Mitään aidosti uutta käsitteellistä asiaa ei tule — vain sama silmukka koodissa — mutta kaikki viikosta 1 alkaen
kohtaa lopulta yhdessä pienessä tiedostossa, jonka opiskelija pystyy puolustamaan ääneen. AT3 palautetaan ja
esitetään tällä viikolla. L23 on rakentamispäivä: jokainen opiskelija kääntää yhden palan omasta viikon 6
pseudokoodistaan JavaScriptiksi tai C#:ksi, ajaa sen, ottaa kuvakaappauksen tuotoksesta ja kirjoittaa 3–5 virkkeen
reflektion. Palautus on L23:n lopussa. L24 on testaus- ja esityspäivä: jokainen opiskelija pitää 2 minuutin suullisen
esityksen, jossa hän kertoo, mitä ohjelma tekee, miten se toimii, mikä bugi löytyi ja miten se korjattiin.
L24:n 2 minuutin paikka on AT3:n suullinen osa; hyväksytty / ei vielä hyväksytty -tarkistus kuvataan tiedostossa self-
study.md ja AT3-tehtäväohjeessa molemmissa opiskelijatehtävätiedostoissa. Työkalut: JavaScript ajetaan
selaimen DevTools-konsolissa; C# .NET Fiddlessä (dotnetfiddle.net). Ei asennuksia. Ei automaattisia
testaustyökaluja. “Testaus” tarkoittaa käsin ajamista kahdella eri lähtöarvolla. “Debuggaus” tarkoittaa
virheilmoituksen lukemista ja yhden pienen korjauksen tekemistä.
Ristiinviittaukset: lisäpakkaa slides-l24-presentation-rubric.md käytetään L24:ssä esitysten välissä
muistuttamaan 2 minuutin rakenteesta. Pakollinen tuntitehtävä Show-and-tell loops kuuluu L22:n 55–75 minuutin
jaksoon; AT3 presentations on L24:n 55–85 minuutin jakso. Molemmat kuvataan tiedostossa in-class-tasks.md.
Ajattele näin: Viikon 8 tavoite ei ole täydellinen ohjelma. Tavoite on, että opiskelija ymmärtää oman pienen
ohjelmansa niin hyvin, että pystyy ajamaan sen, selittämään sen ja kertomaan yhdestä korjauksesta.

## Viikon 8 oppimistavoitteet (Bloom-taksonomian mukaan)

Viikko 8 pysyy tasolla Soveltaminen, ja L24:ssä on yksi kevyen Arvioinnin osuus: opiskelija selittää oman
valintansa ja vertaa ratkaisuaan parin ratkaisuun. Viikon 8 tavoitteissa vältettävät verbit ovat suunnitella, kehittää,
rakentaa, luoda Bloom-verbimerkityksessä, analysoida, arkkitehturoida, optimoida, refaktoroida, arvostella,
kritisoida. “Luo tiedosto” arkimerkityksessä on ok — ulkopuolelle jätetään Bloom-tason Luominen. Viikko 8 on
kokoamista.

### Oppitunti 22 — Silmukat koodissa

• Ymmärtäminen: opiskelija osaa tunnistaa for- tai while-silmukan koodissa ja nimetä sen neljä osaa:
laskuri, ehto, runko, päivitys.
• Ymmärtäminen: opiskelija osaa lukea 3–6 rivin silmukan ja ennustaa, mitä se tulostaa, kummallakin
kielellä.
• Soveltaminen: opiskelija osaa kirjoittaa lyhyen for-silmukan, joka ajetaan tunnettu määrä kertoja (laske 1–
5, tervehdi nimellä kolme kertaa) valitsemallaan kielellä.
• Soveltaminen: opiskelija osaa liittää oman viikon 6 pseudokoodinsa rivin REPEAT N TIMES tai WHILE
toimivaan for- tai while-silmukkaan koodissa.

### Oppitunti 23 — Pseudokoodista pieneksi ohjelmaksi

• Soveltaminen: opiskelija osaa valita omasta viikon 6 pseudokoodistaan yhden sopivan kokoisen palan
käännettäväksi (6–20 riviä).
• Soveltaminen: opiskelija osaa kääntää pseudokoodin noin 10–25 rivin toimivaksi JavaScript- tai C#-
ohjelmaksi käyttäen self-study.md-tiedoston käännöstaulukkoa.
• Soveltaminen: opiskelija osaa ajaa ohjelman selaimen konsolissa (JS) tai dotnetfiddle.net-ympäristössä
(C#) ja vahvistaa vähintään yhden odotetun tuotoksen.
• Soveltaminen: opiskelija osaa tallentaa lähdekoodin .js- tai .cs-tiedostona tai selkeästi nimettynä pätkänä
AT3-palautukseen.

### Oppitunti 24 — Testaa, korjaa yksi bugi, esitä

• Soveltaminen: opiskelija osaa testata ohjelman ajamalla sen vähintään kahdella eri lähtöarvolla ja
tarkistamalla tuotoksen ennustetta vasten.
• Soveltaminen: opiskelija osaa lukea oikean konsoli- tai kääntäjävirheilmoituksen ja paikantaa rivin, johon
se osoittaa.
• Soveltaminen: opiskelija osaa tehdä yhden pienen korjauksen ja ajaa uudelleen.
• Kevyt arviointi: opiskelija osaa selittää ohjelman luokalle 2 minuutissa, kertoen mitä se tekee, miten se
toimii, mikä meni pieleen ja miten se korjattiin.
• Kevyt arviointi: opiskelija osaa verrata omaa ratkaisuaan parin ratkaisuun (halutessa eri kielellä)
yleiskielellä: eri valinnat, sama tavoite.

## Viikon 8 yleiset väärinkäsitykset

Alla on vähintään kaksi väärinkäsitystä per oppitunti, jokaisella Korjaus: -kohta. Nämä nousevat yleisimmin
päätösviikolla; käsittele ne ennen kuin niistä tulee este AT3:lle.

### Oppitunnin 22 väärinkäsitykset

Väärinkäsitys: “Silmukka on monimutkainen asia, jota vain ohjelmoijat ymmärtävät.”
Korjaus: Silmukka on muodollinen nimi “toista 3 kertaa” -mallille, jota ryhmä on kirjoittanut pseudokoodissa viikosta
5 alkaen. Ajattelu ei ole muuttunut; vain syntaksi on uusi. Näytä yksi viikon 6 REPEAT-rivi ja sen for-
silmukkakäännös rinnakkain — se riittää yleensä.
Väärinkäsitys: “Tarvitsen while-silmukan; for on edistyneempi.”
Korjaus: Aloittelijalle asia on usein päinvastoin. for-silmukka pakkaa kaikki neljä osaa siistiin otsikkoon, jossa
päivitystä on vaikeampi unohtaa. while-silmukka riippuu siitä, että laskuri päivitetään rungon sisällä — klassinen
loputtoman silmukan ansa. Suosittele AT3:een for-silmukkaa, ellei opiskelijalla aidosti ole “kunnes”-mallia.

### Oppitunnin 23 väärinkäsitykset

Väärinkäsitys: “Pseudokoodi ja koodi ovat täysin eri asioita.”
Korjaus: Suurin osa työstä on englanninkielisten sanojen korvaamista kielen syntaksilla — rakenne oli jo olemassa.
-tiedoston käännöstaulukko kattaa kahdeksan yleistä mallia ja riittää kaikkeen, mitä viikko 6 tuotti. `self-study.md`
Jos opiskelija väittää, että hänen pseudokoodinsa on “liian erilainen käännettäväksi”, istu hänen kanssaan ja
ympyröi jokaisen rivin ne osat, jotka ovat kirjaimellisesti samoja: muuttujien nimet, numerot, if, else.
Väärinkäsitys: “Jos ohjelmani ei tulosta mitään, jokin on rikki.”
Korjaus: Useammin opiskelija ei painanut Run-painiketta, liitti vain osan ohjelmasta (.NET Fiddle tarvitsee koodin
Main-sisään), tai tulostusrivillä on kirjoitusvirhe (console.Log isolla L:llä, Console.Writeline pienellä l:llä). self-
study.md-tiedoston osio ## When the screen is empty or silent listaa tylsät syyt järjestyksessä.

### Oppitunnin 24 väärinkäsitykset

Väärinkäsitys: “Debuggaus tarvitsee erikoistyökalun.”
Korjaus: Tällä tasolla debuggaus on viestin lukemista ja yhden rivin muuttamista. Ei erikoisohjelmaa, ei
automaattista testaustyökalua. Sano tämä ääneen L24:ssä: “Debuggaus on lukemista ja korjaamista, ei työkalun
käyttöä.” Edistyneempiä työkaluja tulee myöhemmillä kursseilla; L24-harjoitus on tekstin lukemista ja yhden merkin
muuttamista.
Väärinkäsitys: “Jos ohjelma käynnistyy, se on oikein.”
Korjaus: Käynnistyminen ja oikein oleminen eivät ole sama asia. JS-ohjelma, jossa on = silloin kun piti olla ==, voi
usein käynnistyä hiljaa ja tulostaa väärän vastauksen. Siksi AT3 vaatii kaksi lähtöarvoa: toinen ajo nappaa hiljaisen
bugin. Näytä L24-lämmittelyssä if (age = 18) — se käynnistyy ja tulostaa “adult” mille tahansa iälle.
Väärinkäsitys: “2 minuutin esityksen täytyy olla ulkoa opeteltu käsikirjoitus.”
Korjaus: Ei tarvitse. Neljä iskua (mitä / miten / mikä meni pieleen / miten korjasin) ovat rakenne, eivät käsikirjoitus.
Opiskelija, joka seisoo avoimen ohjelmansa vieressä ja puhuu omin sanoin, on juuri tavoitetila. Rubriikkipakka listaa
myös sen, mitä ei vaadita: täydellistä koodia, hienoja dioja, ulkoa opeteltuja sanoja.

## Oppitunti 22 — 90 minuutin suunnitelma

Aihe. Silmukat koodissa: for ja while JavaScriptissä ja C#:ssa rinnakkain, neljä osaa, loputtoman silmukan ansa ja
viikon 6 pseudokoodisilta.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Silmukka on muodollinen nimi repeat-until-idealle, jota
pseudokoodisi jo käytti — nyt vain tietokone, ei ihminen, tekee toiston.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: kirjoita taululle kaksi viikon Koko ryhmä
6 pseudokoodin “repeat”-riviä (REPEAT
5 TIMES: print N ja WHILE password is
too short DO ASK AGAIN). Kysy
ryhmältä: “Miltä arvelette näiden
näyttävän oikeassa koodissa?” Kerää
kolme arvausta; älä vielä korjaa.
0:10–0:25 Opettajan osuus: käy Program D Opetuspuhe
(laskuri 1:stä 5:een) JS:llä ja C#:lla
rinnakkain projektorilla. Aja molemmat.
Nimeä neljä osaa (laskuri, ehto, runko,
päivitys) osoittamalla niitä. Näytä sitten
while-muoto lyhyesti esimerkillä count =
0 / count < 3.
0:25–0:55 ITSENÄINEN TYÖ (30 min): jokainen Itsenäinen
opiskelija tekee tehtävän 8.2
valitsemallaan kielellä (laske 1–5;
käännä 5:stä 1:een; tervehdi nimellä
kolme kertaa). Kolme pätkää yhteen
tiedostoon. Opettaja kiertää.
0:55–1:15 PAKOLLINEN tuntitehtävä — Show- Koko ryhmä
and-tell loops (tehtävä A tiedostossa
in-class-tasks.md, noin 20 min).
Jokainen pari tai yksin työskentelevä
opiskelija ajaa silmukkansa livenä
luokan edessä, lukee tuotoksen ääneen,
ja huone nimeää yhden näytetyn
silmukan neljä osaa. JS ja C# sekaisin
tarkoituksella.
1:15–1:25 Koko ryhmän purku: kerää yksi “helppo” Koko ryhmä
ja yksi “outo” hetki per kieli taululle.
Nosta loputtoman silmukan vaara esiin
kerran — näytä näytöllä, mitä i++-
päivityksen unohtaminen tekee.
1:25–1:30 Lopetus + L23-ennakko: “Huomenna on Koko ryhmä
rakentamispäivä. Valitse, minkä viikon 6
pseudokoodin käännät — tuo se
paperilla.”
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 55–75 minuutin jakso on Tehtävä A — Show-and-tell loops tiedostosta in-class-tasks.md.
Pidä tehtävä 8.2 valmiina projektorilla varapohjaksi, jos opiskelija saapuu ilman kolmea pätkäänsä.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): dia 1 (otsikko) näkyviin samalla, kun taulu kantaa viikon 6
pseudokoodikeskustelua.
• Opettajan osuus (0:10–0:25): diat 2 (Mitä tällä viikolla tulee), 3 (Silmukat — muoto JS:ssä ja C#:ssa
rinnakkain), 4 (Laskuri, ehto, runko, päivitys), 5 (while-silmukka JS:ssä ja C#:ssa rinnakkain). Viivy diassa
4; neljän osan nimeäminen on L22:n kääntöpiste.
• Itsenäinen työ (0:25–0:55): jätä dia 3 näkyviin hiljaiseksi viitteeksi laskurisilmukalle.
• Tuntitehtävä (0:55–1:15): ei diaa; luokan live-silmukat ovat dia.
• Purku (1:15–1:25): dia 6 (Kun silmukka jatkuu ikuisesti) loputtoman silmukan vaaran asettamiseen.
• Lopetus (1:25–1:30): ei dioja.

## Oppitunti 23 — 90 minuutin suunnitelma

Aihe. AT3:n rakentamispäivä. Jokainen opiskelija kääntää yhden palan omaa viikon 6 pseudokoodiaan toimivaksi
JavaScript- tai C#-ohjelmaksi ja palauttaa lähdekoodin sekä kuvakaappauksen tunnin lopussa.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Pseudokoodin kääntäminen ohjelmointikielelle on enimmäkseen
englanninkielisten sanojen korvaamista kielen syntaksilla — rakenne oli jo olemassa.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: kierros luokassa, jokainen Koko ryhmä
opiskelija nimeää yhdessä virkkeessä
viikon 6 pseudokoodin, jonka hän aikoo
kääntää tänään. Opettaja merkitsee
muistiin ne, jotka eivät ole vielä
valinneet, ja ohjaa heidät tehtävän 8.1
varapohjiin.
0:10–0:25 Opettajan osuus: käännöstaulukko Opetuspuhe
projektorille. Käy Program A (ikärajan
tarkistus) alusta loppuun: pseudokoodi
→ JS → C#, molemmat kielet
rinnakkain. Käy sitten yksi
silmukkavariantti (Program E, tervehdys
nimellä kolme kertaa).
0:25–1:05 ITSENÄINEN TYÖ (40 min): jokainen Itsenäinen
opiskelija kääntää valitsemansa viikon 6
pseudokoodin valitsemalleen kielelle,
ajaa sen, ajaa sen uudelleen toisella
lähtöarvolla ja ottaa kuvakaappauksen.
Opettaja kiertää ja vastaa yksilöllisiin
kysymyksiin.
1:05–1:20 Paritarkistus: jokainen näyttää parille Pari
ohjelman ja tuotoksen. Pari kysyy kaksi
kysymystä: “Mitä tämä rivi tekee?” ja
“Mitä muutit kahden ajon välillä?” Ei
korjauksia vielä — se on L24.
1:20–1:28 Koko ryhmän purku: kerää tyypilliset Koko ryhmä
kipukohdat (puolipisteet C#:ssa, iso L
vs. pieni l .Length / .length, puuttuvat
sulkevat aaltosulkeet). Varmista, että
jokainen on tallentanut lähdekoodin ja
kuvakaappauksen.
1:28–1:30 L24-ennakko: “Huomenna testaat, Koko ryhmä
korjaat yhden bugin ja esität. Tuo
lähdekooditiedosto ja kuvakaappaus —
ne ovat AT3.”
Itsenäisen työn jakso: 40 minuuttia (44 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. L23:een ei sijoiteta pakollista tuntitehtävää tiedostosta . Valinnainen tehtävä `in-class-tasks.md`
C (Translation race) tiedostosta voidaan käyttää 1:05–1:20 paritarkistusjaksossa ryhmille, jotka `in-class-tasks.md`
valmistuvat aikaisin.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): dia 7 (Pseudokoodistasi ohjelmaksi) näkyviin, kun opiskelijat nimeävät
pseudokoodipalansa ääneen.
• Opettajan osuus (0:10–0:25): dia 8 (Käännöstaulukko) taulukon läpikäyntiin, sitten lyhyesti takaisin diaan 3
(Silmukat — muoto), kun silmukkavariantti tulee esiin, ja dia 9 (Silmukka + if/else — salasanatarkistus), jos
opiskelijan pseudokoodi yhdistää niitä.
• Itsenäinen työ (0:25–1:05): jätä dia 8 (Käännöstaulukko) näkyviin hiljaiseksi viitteeksi. Dia 10 (Tallenna,
aja, näe tuotos) itsenäisen jakson viimeisellä viidellä minuutilla muistuttaa kuvakaappauksen ottamisesta.
• Paritarkistus (1:05–1:20): ei dioja; parit katsovat toistensa ohjelmia.
• Purku (1:20–1:28): ei dioja; käytä taulua kipukohtalistaan.
• L24-ennakko (1:28–1:30): ei dioja.

## Oppitunti 24 — 90 minuutin suunnitelma

Aihe. Testaa AT3-ohjelma kahdella lähtöarvolla, lue yksi oikea virheilmoitus ja tee yksi pieni korjaus, pidä 2
minuutin suullinen esitys luokassa. Kurssin päätös.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Debuggaus tällä tasolla tarkoittaa, että luet, mitä tietokone kertoi,
etsit sen rivin, josta se puhui, ja teet yhden pienen muutoksen — erikoistyökaluja ei tarvita.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: kirjoita taululle rinnakkain Koko ryhmä
yksi JavaScript-virhe (Uncaught
ReferenceError: scre is not defined) ja
yksi C#-virhe (error CS0103: The name
'scre' does not exist in the current
context). Kysy ryhmältä: “Mitä kumpikin
kertoo?” Päädy vastaukseen:
“molemmat sanovat ‘en tiedä, mikä scre
on’ — sinulla on kirjoitusvirhe kohdassa,
jossa tarkoitit score.”
0:10–0:25 Opettajan osuus: virheilmoituksen Opetuspuhe
lukeminen (yksi JS, yksi C#, molemmat
näytöllä). Nimeä yksi pieni korjaus ja
yksi uudelleenajo -silmukka selvästi.
Käy sitten läpi 2 minuutin esityksen
rakenne: neljä iskua, noin 30 sekuntia
kukin — mitä / miten / mikä meni
pieleen / miten korjasin. Käytä tässä
rubriikkipakka slides-l24-presentation-
rubric.md kokonaan.
0:25–0:55 ITSENÄINEN TYÖ (30 min): jokainen Itsenäinen
opiskelija testaa ohjelmansa kahdella eri
lähtöarvolla, tahallaan tai vahingossa
laukaisee yhden virheen, lukee viestin,
tekee yhden pienen korjauksen,
viimeistelee 3–5 virkkeen reflektion ja
harjoittelee 2 minuutin esityksen kerran
puhelimen ajastimella. Opettaja kiertää
ja kuittaa jokaisen valmiuden.
0:55–1:25 PAKOLLINEN tuntitehtävä — AT3 Koko ryhmä
presentations (tehtävä B tiedostossa
in-class-tasks.md, noin 30 min).
Jokainen opiskelija pitää 2 minuutin
esityksen ohjelmastaan opettajan
kutsumassa järjestyksessä. Käytä
näkyvää puhelinajastinta seinälle
projisoituna. Jokaisen esityksen jälkeen
huone vastaa yhteen
vertaispalautekehotteeseen: “Nimeä
yksi asia, jonka huomasit.”
1:25–1:30 Kurssin päätös: lue kurssin ydinkysymys Koko ryhmä
ääneen dia 18:sta — “Miten puhun
tietokoneelle niin, että se ymmärtää,
mitä haluan sen tekevän?” Kiitä ryhmää.
Muistuta opiskelijoita säilyttämään AT3-
lähdekoodi; avatkaa se uudelleen
kuuden kuukauden päästä.
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ryhmäkokohuomio. 30 minuutin esityspaikka riittää noin 12 opiskelijan ryhmälle, kun jokaisella on 2 minuuttia ja
siirtymään 30 sekuntia. Isommalle ryhmälle katso alla Fasilitointivinkit kahdesta sovelluksesta: jaa kahteen
samanaikaiseen ryhmään yhteisopettajan kanssa tai kierrätä esitykset kahden L24-tyylisen session yli. Lähdekoodi
ja kuvakaappaus kattavat jo poissaolijoiden kirjallisen osan; suullinen osa tarvitsee livepaikan.
Ristiinviittaukset. 55–85 minuutin jakso on Tehtävä B — AT3 presentations tiedostosta in-class-tasks.md.
Tämä on AT3:n suullinen osa. Lisäpakka slides-l24-presentation-rubric.md projisoidaan esitysten välissä
muistutuksena 4 iskun / 2 minuutin rakenteesta.
Diavihjeet — pääpakka slides.md ja lisäpakka slides-l24-presentation-rubric.md.
• Lämmittely (0:00–0:10): diat 11 (Oikean virheilmoituksen lukeminen (JavaScript)) ja 12 (Oikean
virheilmoituksen lukeminen (C#)) rinnakkain projektorille samalla, kun taulu kantaa livekeskustelua “mitä se
kertoo?”.
• Opettajan osuus (0:10–0:25): dia 13 (Yksi pieni korjaus, yksi uudelleenajo) asettamaan kehys debuggaus-
on-lukemista-ei-työkalua, sitten dia 14 (Sinun 2 minuutin esityksesi) neljän iskun rungolle. Vaihda sen
jälkeen lisäpakkaan slides-l24-presentation-rubric.md ja käy kaikki 4–6 diaa alusta loppuun, jotta
opiskelijat näkevät rubriikin kerran ennen harjoittelua.
• Itsenäinen työ (0:25–0:55): jätä dia 14 näkyviin hiljaiseksi viitteeksi neljälle iskulle harjoittelun aikana.
• AT3-esitykset (0:55–1:25): projisoi slides-l24-presentation-rubric.md esitysten välissä rauhalliseksi
muistutukseksi; älä projisoi dioja opiskelijan esityksen päälle. slides-l24-presentation-rubric.md-pakan
hyväksymiskriteeridia on hyödyllisin jätettäväksi näkyviin.
• Kurssin päätös (1:25–1:30): dia 18 (Silmukan sulkeminen — viikko 1 vielä kerran) niin, että ryhmä lähtee
sanasta sanaan -ydinkysymyksen kanssa, sitten dia 19 (Kiitos, ja mitä seuraavaksi).

## Fasilitointivinkit

### 2 minuutin esitysten pitäminen aikataulussa

• Käytä näkyvää puhelinajastinta, projisoituna seinälle tai opiskelija-ajastajan kädessä. Näkyvä ajastin saa
huoneen itse tiivistämään.
• Aseta kova katkaisu 2:30 kohdalle ja pehmeä merkkiääni 2:00 kohdalle. Jos opiskelija jatkaa yli 2:30,
keskeytä lempeästi — seuraava esittäjä tulee.
• Järjestä huone ennen esityspaikan alkua. Ennalta ilmoitettu järjestys pitää siirtymät 20–30 sekunnissa.
• Vertaispalautekysymys — “Nimeä yksi asia, jonka huomasit” — kysytään kerran per esitys koko
huoneelta. Yksi lyhyt vastaus; ei keskustelua.

### Opiskelija, jonka ohjelma ei koskaan käynnistynyt

• Kohdista esitys bugiin, jota hän ei saanut korjattua, ja siihen, mitä hän yritti. Hyväksymiskriteeri
hyväksyy dokumentoidun epäonnistuneen yrityksen — opiskelija nimeää virheilmoituksen ja korjauksen, jota
yritti. Se lasketaan.
• Pidä sama 4 iskun rakenne, mutta viimeiset iskut ovat “mikä meni pieleen / mitä yritin”.
• Merkitse ei-vielä-hyväksytty, jos dokumentoitua yritystä ei ole lainkaan. Tarjoa yhden viikon
uudelleenpalautusikkuna.

### Kahden kielen huoneen hallinta

• Ryhmitä JS- ja C#-opiskelijat vierekkäisiin pöytiin L23:n paritarkistusjaksossa.
• Projisoi molemmat kielet rinnakkain jokaisella koodidialla. Visuaalinen rinnakkaisuus tekee puolet
työstä.
• Kun .NET Fiddle on hidas yhteisen koulun Wi-Fin vuoksi, salli palautus kotoa — kuvakaappaus ja
lähdekoodi kattavat sen; 2 minuutin esityksen voi pitää ilman live-demoa.

### Ujon esittäjän tukeminen

• 2 minuutin esitys on AT3:n suullinen osa, eikä siitä voi neuvotella pois. Muoto on kuitenkin joustava:
erittäin epämukava opiskelija voi esittää pienryhmälle, jossa on opettaja ja kaksi vertaista. Neljä iskua ovat
samat; yleisö on pienempi.
• Tallennetun videon vaihtoehto tehtävän 8.1 kohdassa “If you are doing this alone” on poissaolijoille, ei
luokassa välttelyyn.

## Vastauksia yleisiin opiskelijakysymyksiin

• “Voinko vahingossa käyttää console.log C#-ohjelmassa?” — Et onnistuneesti; kääntäjä hylkää sen
virheellä error CS0103: The name 'console' does not exist in the current context. C# käyttää
Console.WriteLine (iso C, iso W, iso L). Jos näet CS0103:n ja sanan console pienellä, juuri tämä
tapahtui. Lisää iso C.
• “Miksi C#-ohjelmani sanoo CS0103?” — Kääntäjä ei tunne jotakin käyttämääsi nimeä. Se on melkein aina
kirjoitusvirhe: scre sanan score sijaan, console sanan Console sijaan, Writeline pienellä l:llä sanan
WriteLine sijaan. Etsi rivi, jonka viesti nimeää; väärä sana on siinä.
• “Mitä jos viikon 6 pseudokoodini on liian iso?” — Valitse siitä yksi osa, joka tekee yhden selkeän työn alusta
loppuun (6–20 riviä on hyvä kohta). Koko ohjelman ei tarvitse olla mukana. Jos viikon 6 pseudokoodi
puuttuu tai on hukassa, valitse yksi tehtävän 8.1 viidestä varapohjasta (ikä, salasana, pisteet, laskuri,
tervehdys) ja sovita arvot omaan tilanteeseesi. Se lasketaan AT3:ksi.
• “Täytyykö minun pitää esitys, jos olen ujo?” — Kyllä; 2 minuutin suullinen osuus on AT3:n suullinen osa,
eikä AT3:a voi läpäistä ilman sitä. Mutta yleisö voi olla pieni (opettaja ja kaksi vertaista luokan nurkassa) ja
muoto keskusteleva — neljä iskua ovat rakenne, eivät ulkoa opeteltu käsikirjoitus. Puhu opettajalle L23:ssa,
jos koko ryhmälle esittäminen on este.
• “Saanko käyttää ChatGPT:tä ohjelman kirjoittamiseen?” — Voit käyttää LLM:ää sparrauskumppanina,
esimerkiksi virheilmoituksen selittämiseen, mutta palautettavan ohjelman täytyy olla sellainen, jonka pystyt
lukemaan rivi riviltä ja kävelemään huoneelle läpi 2 minuutissa. Opiskelija, joka liittää LLM:n tuottamaa
koodia ymmärtämättä sitä, jää kiinni esityksessä; neljä iskua vaativat opiskelijaa nimeämään, mitä jokainen
rivi tekee. Tehtävässä 8.4 on erillinen LLM-sparrausvaihe, jonka kehotteessa ei pyydetä korjausta; se on
tarkoitettu käyttö.
• “Mikä lasketaan ‘yhdeksi bugiksi’?” — Kirjoitusvirhe (väärin kirjoitettu muuttujan nimi), puuttuva puolipiste
(C#), puuttuva sulkeva aaltosulje, = siinä missä piti olla ==, kirjainkoon ristiriita (length vs. Length). Mikä
tahansa näistä kelpaa. Bugin täytyy olla sellainen, jonka pystyt nimeämään yleiskielellä; “ohjelmani ei vain
toiminut” ei riitä.
• “Tarvitsenko asennuksia?” — Et. JavaScript toimii selaimen DevTools-konsolissa (Cmd + Opt + J / Ctrl +
Shift + J). C# toimii dotnetfiddle.net-ympäristössä ilman tiliä. Molemmat ovat samoja työkaluja, joita
käytit viikolla 7.

## Formatiivisen arvioinnin vinkit

Viikko 8 on viimeinen viikko. Formatiiviset tarkistukset eivät enää valmistele tulevaa arviointia; ne varmistavat, että
AT3 on raiteillaan ja että kurssin ydinkysymykseen on todella vastattu jokaisen opiskelijan kohdalla. Käytä kolme
nopeaa tarkistusta viikon aikana sekä yksi sulkeva tarkistus L24:n lopussa.

### Oppituntikohtaiset epämuodolliset tarkistukset

• Oppitunti 22 — poistumislappu (3 min tunnin lopussa). Jokainen opiskelija kirjoittaa yhdelle riville for-
silmukan neljä osaa: laskuri, ehto, runko, päivitys. Lue neljä satunnaisesti ääneen. Ryhmä, joka nimeää
kaikki neljä oikein, on valmis L23:n rakentamispäivään.
• Oppitunti 23 — kiertävä kuittaus. 40 minuutin itsenäisen jakson aikana opettaja käy jokaisen opiskelijan
luona vähintään kerran. Kuittaa kaksi asiaa: (a) ohjelma käynnistyi yhdellä lähtöarvolla, (b) kuvakaappaus
on olemassa. Opiskelija, joka on jumissa 20 minuutin itsenäisen työn jälkeen, tarvitsee väliintuloa, ei
opiskelija, joka yhä kirjoittaa.
• Oppitunti 23 — parien raportointi. 1:05–1:20 paritarkistusjakson lopussa jokainen pari antaa yhden
havainnon yhdessä virkkeessä: “Yksi asia, jonka parini ohjelma tekee hyvin; yksi asia, jonka muuttaisin
omassani hänen ohjelmansa nähtyäni.” Huoneen malli kertoo, pystyvätkö opiskelijat lukemaan koodia, joka
ei ole heidän omaansa — keskeinen viikon 8 siirtotaito.
• Oppitunti 24 — valmiustarkistus kohdassa 0:55. Juuri ennen esitysten alkua kysy huoneelta: “Käsi ylös,
kuinka monella on ohjelma, joka toimii, kuvakaappaus ja 3 virkkeen reflektio valmiina?” Kädet, jotka eivät
nouse, ovat opiskelijoita, joiden luo menet ensin 30 minuutin itsenäisen jakson aikana. Kukaan ei esitä ilman
näitä kolmea artefaktia kädessään.
• Oppitunti 24 — yhden minuutin paperi lopussa. “Yhdessä virkkeessä: vastasiko kurssi sinulle
ydinkysymykseensä?” (“Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?”) Tämä
on sulkeva tarkistus. Ryhmä, jossa useimmat vastaavat “kyllä, ja tässä on ohjelma kädessäni”, on
saavuttanut kurssin tavoitteen.

### Mitä kuuntelet koko viikon ajan

L24:n loppuun mennessä kolme lausetta merkitsee aitoa kurssitason ymmärrystä:
• “Ohjelmani tekee X, ja tässä on miksi jokainen rivi on siinä” — opiskelija sanoo tämän epäröimättä
esittäessään omaa ohjelmaansa.
• “Virheilmoitus sanoi scre — se oli rivi, jossa kirjoitin scre enkä score — lisäsin o:n ja se toimi” — bugi ja
korjaus -kertomus ilman mysteeriä.
• “Se on sama muoto C#:ssa kuin JavaScriptissä — käytin vain int-sanaa let-sanan sijaan ja
Console.WriteLine-riviä console.log-rivin sijaan” — kahden kielen siirto on asettunut.
Jos nämä kolme ilmausta näkyvät opiskelijoiden puheessa L24:ssä, kurssi on tehnyt tehtävänsä. 2 minuutin
esityspaikka on sekä diagnostiikka että juhla samaan aikaan.
