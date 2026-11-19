# Itseopiskelu

Kuvittele, että kahdeksanvuotias serkkusi tulee keittiöön ja sanot hänelle: “Tee minulle
voileipä.” Hän katsoo sinua. Tasolla on leipää, jääkaapissa voita, juusto on jossain, ja veitsi on
laatikossa, jota hän ei saa avata. Hän on tehnyt tämän isänsä kanssa sata kertaa, mutta juuri
nyt, yksin, hän ei tiedä, mitä leipää käyttää, kuinka paksun viipaleen ottaa, jätetäänkö reunat
vai ei ja lasketaanko juusto mukaan. Lopulta hän ottaa pussista yhden leipäviipaleen, antaa sen
sinulle ja kysyy: “Onko tämä voileipä?” Hän ei ole sekaisin siitä, mitä voileipä tarkoittaa. Sinä et
vain antanut hänelle tarpeeksi tietoa.
Tämä viikko käsittelee juuri tuota väliä — pientä etäisyyttä sen välillä, mitä tarkoitat, ja sen
välillä, mitä toinen kuulee. Tietokone elää tuossa välissä koko ajan. Se ei arvaa, mitä tarkoitit;
se tekee sen, mitä kirjoitit. Koko kurssi, jonka olet aloittamassa, rakentuu yhden kysymyksen
varaan, ja palaamme siihen monta kertaa: Miten puhun tietokoneelle niin, että se
ymmärtää, mitä haluan sen tekevän? Ensimmäinen vastaus ei ole “opettele
ohjelmointikieli”. Se tulee myöhemmin kurssilla. Ensimmäinen vastaus on: totuttele sanomaan
täsmälleen se, mitä tarkoitat.
Viikon lopussa osaat kirjoittaa selkeän, vaihe vaiheelta etenevän arkisen ohjeen, antaa sen
kirjaimelliselle suorittajalle, nähdä missä ohje hajoaa ja korjata sen. Ei koodia, ei
erikoistyökaluja. Vain huolellisia lauseita ja valmiutta huomata, ettet ollutkaan niin selkeä
kuin ajattelit.
Ajattele näin: tietokone ei ole “hankala” tai “huono ymmärtämään”. Se on vain hyvin
kirjaimellinen. Siksi pieni epäselvyys ohjeessa voi aiheuttaa ison virheen lopputuloksessa.

## Oppituntikohtainen lukemisto

Seuraavat lessonikohtaiset tekstit vastaavat yllä olevan itseopiskeluluettavan sisältöjä. Ne on
säilytetty materiaalipaketissa mukana, jotta sama sisältö on käytettävissä myös
oppitunneittain.

## Oppitunti 1 - Puhuminen tietokoneelle

### Mitä ohjelmallinen ajattelu on?

Ohjelmallinen ajattelu on arkinen tapa pilkkoa tehtävä pieniksi, selkeiksi ja järjestetyiksi
vaiheiksi, jotka kirjaimellinen suorittaja pystyy tekemään ilman arvailua. Se on ajattelua
ohjelmoinnin taustalla, ei ohjelmointia itseään. Käytät tätä taitoa aina, kun kirjoitat toiselle
reittiohjeen: “Käänny bussipysäkiltä vasemmalle, kävele kaksi korttelia, ovi on punainen.” Sama
taito toimii riippumatta siitä, onko suorittaja ihminen vai kone.
Tätä ideaa tutkivat ihmiset nimeävät yleensä neljä pilaria: pilkkominen (suuren ongelman
jakaminen pienempiin osiin), hahmontunnistus (sen huomaaminen, mikä toistuu),
abstrahointi (olennaiseen keskittyminen ja muun piilottaminen) sekä algoritmit (itse
vaiheittaiset ohjeet). Jokainen näistä saa kurssilla oman viikkonsa myöhemmin. Pidä
toistaiseksi mielessä tämä lyhyt versio: ohjelmallinen ajattelu on tapa olla selkeä, vaihe
vaiheelta, kirjaimelliselle suorittajalle.
Tässä kohdassa kannattaa myös purkaa yksi yleinen väärinkäsitys. Ohjelmallinen ajattelu ei ole
sama asia kuin ohjelmointi. Ohjelmointi on yksi paikka, jossa ohjelmallista ajattelua käytetään.
Voit kirjoittaa täysin selkeän algoritmin kananmunan keittämiseen koskematta
näppäimistöön, ja käyttämäsi taito on täsmälleen sama kuin ohjelmoijalla. Näppäimistö tulee
mukaan vasta lopussa.

### Tietokone ottaa sinut kirjaimellisesti

Aloitetaan kokonaan ilman tietokoneita.
Esimerkki 1 — voileipä. Pyydät pientä serkkuasi tekemään voileivän. Hän on halukas, hän
kuuntelee ja luottaa sinuun. Mutta hän ei ole koskaan tehnyt sitä yksin. Sinä sanoit “tee
minulle voileipä” — et kertonut, mitä leipää käytetään, montako viipaletta otetaan, mitä väliin
laitetaan tai leikataanko se kahtia. Hän tekee ensimmäisen asian, joka sopii niihin sanoihin,
jotka oikeasti sanoit: hän antaa sinulle leipäviipaleen. Hän seuraa ohjetta kirjaimellisesti. Leipä
ei ole väärinkäsitys sanasta voileipä; se on se osa sanasta, josta hän oli varma.
Esimerkki 2 — iso puu. Ystävä, joka ei ole koskaan käynyt kotikadullasi, kysyy reittiä
luoksesi. Sanot: “Kävele minun katuni päähän, käänny ison puun kohdalla ja taloni on kolmas
ovi vasemmalla.” Kolme viikkoa myöhemmin hän kertoo eksyneensä. Miksi? Koska sinulle “iso
puu” on ilmeinen — se kulmassa oleva vaaleakaarnainen puu — mutta hänelle kaikki kadun
puut näyttivät suunnilleen saman kokoisilta. Iso ei ollut mitta, vaan sinun muistosi.
Sitten IT-puolelle.
Esimerkki 3 — kirjoitusvirhe hakukoneessa. Haluat Python-opastuksen ja kirjoitat
hakukoneeseen . Hakukone ei sano “Luulen, että tarkoitit Pythonia.” `pyhton tutorial`
Kirjaimellisella tasolla se etsii sivuja, joilla esiintyy sana , jota ei ole olemassa, ja tarjoaa `pyhton`
sitä lähimpänä olevia tuloksia. Se tekee täsmälleen sen, mitä kirjoitit.
Esimerkki 4 — puuttuva kauttaviiva. Ohjelma yrittää avata tiedoston polusta
polun sijaan. Sinulle

```
Users/maria/documentsreport.txt Users/maria/documents/report.txt
```

ero on yksi kauttaviiva; tietokoneelle ero on siinä, löytyykö oikea kansio vai viitataanko
tiedostonimeen, jota ei ole olemassa. Se ei arvaa. Se ilmoittaa virheestä.
Yhdessäkään näistä esimerkeistä kone ei ole rikki eikä suorittaja ole syyllinen. Ohje oli vain
epäselvempi kuin kirjoittaja itse luuli.

### Tulkinnanvaraisuus on ohjeessa, ei tietokoneessa

Tulkinnanvaraisuus on ohjeen ominaisuus, ei suorittajan ominaisuus. Kun serkkusi
ojensi sinulle leipäviipaleen, tulkinnanvaraisuus oli ilmauksessa “tee minulle voileipä”. Kun
ystäväsi eksyi, tulkinnanvaraisuus oli ilmauksessa “iso puu”. Kun hakukone palautti roskaa
sanalle , tulkinnanvaraisuus oli kirjoitetussa sanassa. `pyhton`
Ihmiset syyttävät helposti konetta ja sanovat, ettei se ymmärrä. Tämä kehys on väärä.
Tietokone on kirjaimellinen, ja juuri siksi siihen voi luottaa. Jos kirjoitat selkeän ohjeen,
tietokone seuraa sitä samalla tavalla joka kerta. Kun jokin menee pieleen, kysy: “Missä kohtaa
oma ohjeeni oli epäselvä?”

## Miksi tämä on tärkeää IT-ammattilaiselle

IT-ammattilainen kirjoittaa koko ajan ohjeita: koneille, kollegoille ja käyttäjille. Helpdesk-
vastaus, README, käyttöönotto-ohje ja tiketti ovat kaikki samaa perhettä. Jos sana on epäselvä,
koko toiminta voi mennä väärään suuntaan. Selkeä kirjoittaminen on siksi ammatillinen taito,
ei vain koulutehtävä.
Pysähdy hetkeksi: Mieti yhtä selkeää ja yhtä epäselvää ohjetta tältä viikolta. Mikä
teki toisesta onnistuneen ja toisesta hankalan?

## Oppitunti 2 - Algoritmit arjessa Mitä algoritmi on?

Algoritmi on selkeä sarja kirjaimellisia vaiheita, jotka vievät sinut lähtötilanteesta kohti
tavoitetta. Sen ei tarvitse olla koodia. Sen ei tarvitse olla pitkä. Jos kirjaimellinen suorittaja
pystyy seuraamaan vaiheita ja pääsemään tavoitteeseen, kyseessä on algoritmi.

### Algoritmeja, joita käytät jo nyt

### Resepti — tee maidolla.

Tavoite: kuuma mukillinen teetä maidolla.
Syöte: teepussi, vesi, maito, sokeri (valinnainen), muki ja vedenkeitin.
Vaiheet: täytä vedenkeitin kylmällä vedellä, laita se päälle, laita teepussi mukiin, odota että vesi
kiehuu, kaada vesi mukiin, odota kolme minuuttia, ota teepussi pois, lisää maitoa, lisää sokeria
halutessasi, sekoita.
Tuotos: kuuma mukillinen teetä maidolla.

### Reitti — kotoa kouluun.

Tavoite: saapua kouluun ajoissa.
Syöte: sinä, reppu, bussikortti, kellonaika, ulko-ovi.
Vaiheet: lähde kotoa ajoissa, kävele pysäkille, nouse oikeaan bussiin, jää pois oikealla pysäkillä,
kävele koululle, mene sisään pääovesta.
Tuotos: sinä koulussa ajoissa.

### Aamurutiini.

Tavoite: lähteä kotoa päivän valmiina.
Syöte: sinä sängyssä, herätys, vaatteet, aamupala keittiössä.
Vaiheet: herätys soi, sammuta se, nouse, peseydy, pukeudu, syö, harjaa hampaat, pakkaa reppu,
laita kengät jalkaan, lähde.
Tuotos: sinä valmiina lähtöön.
Sama rakenne näkyy myös IT-tilanteessa: tavoite, syöte, vaiheet ja tuotos.
Pysähdy hetkeksi: Mikä aamurutiinin vaihe olisi vaikein kirjaimelliselle
suorittajalle? Perustele yhdellä lauseella.

### Kaksi algoritmia samaan tavoitteeseen

Samaan tavoitteeseen voi olla useita toimivia algoritmeja. Tee voidaan tehdä lisäämällä maito
ennen hautumista tai vasta sen jälkeen. Kouluun voi mennä bussilla, ratikalla tai pyörällä.
Nämä voivat kaikki olla toimivia ratkaisuja samaan tavoitteeseen.
Myöhemmin kurssilla kysymme, onko jokin ratkaisu parempi kuin toinen. Tämän kysymyksen
esittämiseksi pitää ensin hyväksyä, että useampi kuin yksi ratkaisu voi olla pätevä.

### Ensimmäisen algoritmin kirjoittaminen tavallisella kielellä

Kirjoita paperille tai muistiinpanoihin algoritmi siitä, miten teet kupin teetä, valmistaudut
aamulla tai lähetät Discord-viestin ystävälle. Käytä tavallista suomea. Numeroi vaiheet.
Tavoittele 5–10 vaihetta. Kirjoita mukaan tavoite, syöte ja tuotos.
Jos huomaat kirjoittavasi “tee se tavallinen juttu”, pysähdy ja pilko vaihe tarkemmiksi osiksi.
Kirjaimellinen suorittaja ei tiedä, mikä tavallinen on.
Pysähdy hetkeksi: Yrititkö käyttää sanaa “yleensä” tai “oikea”? Jos kyllä, merkitse se
epäselväksi kohdaksi.

## Oppitunti 3 - Täsmälliset ja epätäsmälliset ohjeet

### Mitä “epätäsmällinen” tarkoittaa tässä yhteydessä?

Epätäsmällinen eli tulkinnanvarainen ohje on sellainen, jonka useampi kirjaimellinen
suorittaja voisi toteuttaa eri tavoilla ja silti uskoa toimineensa oikein. Lyhyys tai pituus ei
ratkaise selkeyttä. Ohje “sulje ovi” voi olla täysin selkeä. Ohje “tallenna tiedosto tavalliseen
paikkaan” voi olla hyvin epäselvä.

### Tulkinnanvaraisuuden metsästäminen

Epäselvyys näkyy usein neljässä muodossa:
• epämääräinen substantiivi: “avaa tiedosto”
• deiktinen sana: “laita se tähän”
• suhteellinen aika: “tee se myöhemmin”
• epämääräinen määrä: “lisää vähän maitoa”
Korjaus on aina sama suuntaan vievä liike: tee ohjeesta tarkempi, nimeä kohde, aika, paikka tai
määrä.

### Ohjeiden testaaminen toimimalla kirjaimellisena tietokoneena

Paras tapa löytää epäselvyys omasta ohjeesta on testata sitä kirjaimellisena suorittajana. Älä
lue ohjetta niin kuin kirjoittaja lukee sen. Lue se niin kuin robotti lukisi sen: ilman oletuksia ja
ilman taustatietoja.
Kysy jokaisessa vaiheessa:
• voinko tehdä tämän useammalla tavalla?
• sainko edellisestä vaiheesta kaiken, mitä nyt tarvitsen?

### Reunatapaukset

Reunatapaus on epätavallinen tilanne, jossa muuten toimiva ohje ei enää kerro, mitä pitäisi
tehdä. Esimerkiksi ohje “avaa jääkaappi ja ota maito” ei kerro mitään siitä, mitä tehdään, jos
maitoa ei ole.
Pysähdy hetkeksi: Etsi omasta algoritmistasi yksi reunatapaus. Kirjoita yhdellä
lauseella, mitä suorittajan pitäisi siinä tilanteessa tehdä.
