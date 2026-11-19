# Oppitunti 1 — Tietokoneelle puhuminen (sananmukainen tulkinta ja monitulkintaisuus)

### Mitä ohjelmallinen ajattelu on?

Ohjelmallinen ajattelu on arkinen tapa pilkkoa tehtävä pieniin, selkeisiin, järjestettyihin vaiheisiin, jotka sananmukainen tulkitsija voi suorittaa ilman arvailua. Se on ohjelmoinnin *takana* oleva ajattelu, ei itse ohjelmointi. Teet sitä joka kerta, kun kirjoitat ohjeita jollekin toiselle: "Käänny vasemmalle bussipysäkin kohdalla, kävele kaksi korttelia, ovi on punainen." Olipa tulkitsija ihminen tai kone, sama taito pätee.

Tätä ideaa tutkivat ihmiset nimeävät yleensä neljä pilaria: **ositus** (suuren ongelman pilkkominen pienempiin), **mallien tunnistaminen** (toistuvan huomaaminen), **abstraktio** (oleelliseen keskittyminen ja muun ohittaminen) sekä **algoritmit** (itse vaiheittaiset ohjeet). Jokainen näistä saa oman viikkonsa myöhemmin kurssilla. Pidä toistaiseksi mielessä lyhyt versio: *ohjelmallinen ajattelu on tapa olla selkeä, vaiheittain, sananmukaiselle tulkitsijalle.*

Tämä on myös hyvä hetki selventää yleinen sekaannus. Ohjelmallinen ajattelu **ei** ole sama kuin ohjelmointi. Ohjelmointi on yksi paikka, jossa käytät ohjelmallista ajattelua. Voit kirjoittaa täydellisen selkeän algoritmin kananmunan keittämiseen koskematta näppäimistöön, ja taito, jota silloin käytit, on täsmälleen sama, jota ohjelmoija käyttää. Näppäimistöosuus tulee viimeisenä.

### Tietokone ottaa sinut sananmukaisesti

Aloitetaan kokonaan tietokoneiden ulkopuolelta.

**Esimerkki 1 — voileipä.** Pyydät pientä serkkuasi tekemään voileivän. Hän on halukas, hän keskittyy ja hän luottaa sinuun. Mutta hän ei ole koskaan tehnyt sellaista yksin. Sanoit "tee minulle voileipä" — et sanonut mikä leipä, montako viipaletta, mitä väliin tai pitääkö se leikata kahtia. Hän tekee ensimmäisen asian, joka sopii sanomiisi sanoihin: ojentaa sinulle leipäviipaleen. Hän seuraa sinua sananmukaisesti. Leipä ei ole väärinkäsitys sanasta "voileipä"; se on se osa sanasta "voileipä", josta hän oli varma.

**Esimerkki 2 — iso puu.** Ystäväsi, joka ei ole koskaan käynyt naapurustossasi, kysyy miten päästä taloosi. Sanot: "Kävele alas katuani, käänny ison puun kohdalla, ja se on kolmas ovi vasemmalla." Kolme viikkoa myöhemmin hän kertoo eksyneensä. Miksi? Koska sinulle "iso puu" on ilmiselvä — se on kulmassa oleva, valkorunkoinen — mutta hänelle jokainen puu sillä kadulla näytti suunnilleen samankokoiselta. "Iso" ei ollut mittayksikkö; se oli muisto, joka oli sinulla mutta ei hänellä.

Nyt ICT-puolelta.

**Esimerkki 3 — kirjoitusvirheellinen haku.** Haluat Python-tutoriaalin ja kirjoitat hakukoneeseen `pyhton tutorial`. Hakukone ei sano "tarkoititko Pythonia". (Nykyiset sanovat, koska niitä on koulutettu arvaamaan, mutta sen alla oleva raaka täsmäytyskerros ei.) Sananmukaisella tasolla se etsii sivuja, jotka sisältävät sanan `pyhton`, jota ei ole olemassa, ja antaa sinulle sen, mikä tulee lähimmäksi. Se tekee täsmälleen mitä kirjoitit.

**Esimerkki 4 — puuttuva kauttaviiva.** Ohjelma yrittää avata tiedoston polusta `Users/maria/documentsreport.txt` polun `Users/maria/documents/report.txt` sijaan. Sinulle ero on yksi kauttaviiva; tietokoneelle se on ero kansion, jonka se löytää, ja tiedostonimen, josta se ei ole koskaan kuullut, välillä. Se ei yritä kovempaa; se ilmoittaa virheestä.

Kaikissa neljässä esimerkissä ei ole rikkinäistä konetta eikä syyllistä tulkitsijaa. On ohje, ja ohje oli vähemmän selkeä kuin sanoja ajatteli.

### Monitulkintaisuus on ohjeessa, ei tietokoneessa

Tämä on koko viikon käsitteellinen käännekohta, joten se kannattaa sanoa hitaasti: **monitulkintaisuus on ohjeen ominaisuus, ei tulkitsijan.** Kun serkkusi ojensi sinulle leipäviipaleen, monitulkintaisuus oli sanoissa "tee minulle voileipä". Kun ystäväsi eksyi, monitulkintaisuus oli sanoissa "iso puu". Kun hakukone palautti roskaa sanasta `pyhton`, monitulkintaisuus oli kirjoitetussa sanassa.

Tällä on merkitystä, koska kulttuurinen refleksi on päinvastainen. Kun ohje epäonnistuu, ihmiset usein syyttävät konetta ja sanovat, ettei se ymmärrä heitä. Tuo asetelma on väärä, ja kun päästät siitä irti, koko kurssi helpottuu. Tietokone on **sananmukainen**. Se tekee täsmälleen mitä on kirjoitettu, ja se on itse asiassa sen vahvuus — jos osaat kirjoittaa selkeän ohjeen, voit luottaa siihen, että tietokone seuraa sitä samalla tavalla joka kerta.

Joten kun jokin menee pieleen, kysymys, jonka opit esittämään, ei ole "miksi tämä kone ei ymmärrä", vaan "missä kohdassa ohjettani olin epäselvä". Tähän jälkimmäiseen kysymykseen on vastauksia. Ensimmäiseen ei ole.

### Miksi tällä on merkitystä ICT-ammattilaiselle

Saatat ihmetellä, miksi ensimmäisen vuoden ammatillisen ICT-opiskelijan pitää ajatella voileipiä ja puita. Tässä lyhyt versio: ICT-ammattilainen viettää suurimman osan päivästään kirjoittaen ohjeita. Ohjeita koneille (kun lopulta kirjoitat koodia). Ohjeita kollegoille (tiketti, luovutusmuistio, vaiheittainen korjaus). Ohjeita loppukäyttäjille (käyttöohje, chatbotin vastaus, help desk -vastaus, README). Kaikilla näillä on sama muoto, ja kaikki hajoavat samalla tavalla: sana, joka tuntui sinulle ilmiselvältä, osoittautuu epäselväksi toisella puolella olevalle henkilölle.

Kun asiakas kirjoittaa tukitikettiin "ei toimi", hän antaa sinulle epäselvän ohjeen. Kun vastaat "oletko kokeillut käynnistää uudelleen" sanomatta *mitä* uudelleenkäynnistää, annat hänelle sellaisen. Koko ala pyörii pienillä selkeillä virkkeillä, ja ihmiset, jotka osaavat kirjoittaa niitä hyvin, erottuvat nopeasti joukosta.

> **Pysähdy hetkeksi:** Mieti yhtä tilannetta tällä viikolla, jossa annoit selkeän ohjeen kaverille, sisarukselle tai vanhemmalle — ja yhtä tilannetta, jossa annoit epäselvän. Mikä oli ero? Oliko se puuttuva sana, oletus siitä mitä toinen jo tiesi, vai numero, jota et täsmentänyt?

---
