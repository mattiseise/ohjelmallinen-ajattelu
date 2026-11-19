# Oppitunti 1 - Puhuminen tietokoneelle

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
hakukoneeseen . Hakukone ei sano “Luulen, että tarkoitit Pythonia.”
pyhton tutorial
Kirjaimellisella tasolla se etsii sivuja, joilla esiintyy sana , jota ei ole olemassa, ja tarjoaa
pyhton
sitä lähimpänä olevia tuloksia. Se tekee täsmälleen sen, mitä kirjoitit.
Esimerkki 4 — puuttuva kauttaviiva. Ohjelma yrittää avata tiedoston polusta
polun sijaan. Sinulle
Users/maria/documentsreport.txt Users/maria/documents/report.txt
ero on yksi kauttaviiva; tietokoneelle ero on siinä, löytyykö oikea kansio vai viitataanko
tiedostonimeen, jota ei ole olemassa. Se ei arvaa. Se ilmoittaa virheestä.
Yhdessäkään näistä esimerkeistä kone ei ole rikki eikä suorittaja ole syyllinen. Ohje oli vain
epäselvempi kuin kirjoittaja itse luuli.

### Tulkinnanvaraisuus on ohjeessa, ei tietokoneessa

Tulkinnanvaraisuus on ohjeen ominaisuus, ei suorittajan ominaisuus. Kun serkkusi
ojensi sinulle leipäviipaleen, tulkinnanvaraisuus oli ilmauksessa “tee minulle voileipä”. Kun
ystäväsi eksyi, tulkinnanvaraisuus oli ilmauksessa “iso puu”. Kun hakukone palautti roskaa
sanalle , tulkinnanvaraisuus oli kirjoitetussa sanassa.
pyhton
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
