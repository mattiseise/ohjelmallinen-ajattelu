# Oppitunti 1 — Puhuminen tietokoneelle (kirjaimellinen tulkinta ja tulkinnanvaraisuus)

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
Vinkki: jos jokin käsite tuntuu abstraktilta, kysy itseltäsi: “Voisinko selittää tämän myös
esimerkillä keittiöstä, koulumatkasta tai puhelimen käytöstä?” Jos vastaus on kyllä, olet jo
lähellä ymmärtämistä.

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
hakukoneeseen . Hakukone ei sano “Luulen, että tarkoitit Pythonia.” (Nykyiset `pyhton tutorial`
hakukoneet tekevät näin usein, koska niitä on opetettu arvaamaan, mutta niiden perusosuma
toimii silti kirjaimellisemmin.) Kirjaimellisella tasolla hakukone etsii sivuja, joilla esiintyy sana
, jota ei ole olemassa, ja tarjoaa sitä lähimpänä olevia tuloksia. Se tekee täsmälleen sen, `pyhton`
mitä kirjoitit.
Esimerkki 4 — puuttuva kauttaviiva. Ohjelma yrittää avata tiedoston polusta
polun sijaan. Sinulle

```
Users/maria/documentsreport.txt Users/maria/documents/report.txt
```

ero on yksi kauttaviiva; tietokoneelle ero on siinä, löytyykö oikea kansio vai viitataanko
tiedostonimeen, jota ei ole olemassa. Se ei yritä arvata paremmin. Se ilmoittaa virheestä.
Yhdessäkään näistä neljästä esimerkistä kone ei ole rikki eikä suorittaja ole syyllinen. On
olemassa ohje, ja ohje oli epäselvempi kuin kirjoittaja luuli.

### Tulkinnanvaraisuus on ohjeessa, ei tietokoneessa

Tämä on koko viikon käsitteellinen käännekohta, joten se kannattaa sanoa hitaasti:
tulkinnanvaraisuus on ohjeen ominaisuus, ei suorittajan ominaisuus. Kun serkkusi
ojensi sinulle leipäviipaleen, tulkinnanvaraisuus oli ilmauksessa “tee minulle voileipä”. Kun
ystäväsi eksyi, tulkinnanvaraisuus oli ilmauksessa “iso puu”. Kun hakukone palautti roskaa
sanalle , tulkinnanvaraisuus oli kirjoitetussa sanassa. `pyhton`
Tämä on tärkeää, koska arkinen refleksi on usein päinvastainen. Kun ohje epäonnistuu,
ihmiset syyttävät konetta ja sanovat, ettei se ymmärrä. Tuo kehys on väärä, ja kun siitä päästää
irti, koko kurssi helpottuu. Tietokone on kirjaimellinen. Se tekee juuri sen, mitä on kirjoitettu,
ja tämä on itse asiassa sen vahvuus — jos kirjoitat selkeän ohjeen, voit luottaa siihen, että
tietokone seuraa sitä samalla tavalla joka kerta.
Kun jokin menee pieleen, oikea kysymys ei siis ole “miksi tämä kone ei tajua?” vaan “missä
kohtaa oma ohjeeni oli epäselvä?” Tuohon toiseen kysymykseen on vastauksia. Ensimmäiseen
ei juuri ole.
Esimerkki: jos ohjelma ei löydä tiedostoa, ongelma ei usein ole ohjelmassa vaan
tiedostonimessä, polussa tai siinä, mitä ohjelmalle kerrottiin.

## Miksi tämä on tärkeää IT-ammattilaiselle

Saatat miettiä, miksi ensimmäisen vuoden ICT-opiskelijan pitäisi pohtia voileipiä ja puita.
Lyhyt vastaus kuuluu näin: IT-ammattilainen käyttää suuren osan päivästä ohjeiden
kirjoittamiseen. Ohjeita koneille (kun myöhemmin kirjoitat koodia). Ohjeita kollegoille (tiketti,
luovutusmuistio, vaiheittainen korjausohje). Ohjeita loppukäyttäjille (käyttöohje, chatbot-
vastaus, helpdesk-viesti, README).
Kaikilla näillä on sama perusrakenne, ja ne rikkoutuvat samalla tavalla: sana, joka sinulle
tuntuu itsestään selvältä, osoittautuukin epäselväksi toiselle ihmiselle. Kun asiakas kirjoittaa
tukipyyntöön “se ei toimi”, hän antaa sinulle epäselvän ohjeen. Kun vastaat “oletko kokeillut
käynnistää uudelleen?” kertomatta mitä pitäisi käynnistää uudelleen, annat sinä hänelle
epäselvän ohjeen. Koko ala toimii pienten, selkeiden lauseiden varassa, ja ne ihmiset, jotka
kirjoittavat niitä hyvin, erottuvat nopeasti.
Pysähdy hetkeksi: Mieti yhtä tilannetta tältä viikolta, jossa annoit ystävälle,
sisarukselle tai vanhemmalle selkeän ohjeen — ja yhtä tilannetta, jossa annoit
epäselvän ohjeen. Mikä niiden ero oli? Puuttuiko jokin sana, oletitko liikaa toisen
ennakkotiedoista vai jätitkö jonkin luvun täsmentämättä?
