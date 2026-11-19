# Tietokoneelle puhuminen — mitä se oikeasti kuulee?

## Johdanto

Kuvittele, että kahdeksanvuotias serkkusi kävelee keittiöön ja sanot hänelle: "Tee minulle voileipä." Hän tuijottaa sinua. Tasolla on leipää, jääkaapissa on voita, juustoa jossakin ja veitsi laatikossa, jota hänen ei saa avata. Hän on tehnyt tätä isänsä kanssa sata kertaa, mutta juuri nyt, yksin, hän ei tiedä mikä leipä, kuinka paksu, kuorella vai ilman, ja lasketaanko juusto. Niinpä hän ottaa leipäpaketista yhden viipaleen, ojentaa sen sinulle ja kysyy: "Onko tämä voileipä?"

Hän ei ole hämillään siitä, mikä voileipä on. Et vain antanut hänelle tarpeeksi tietoa lähteä liikkeelle.

Tällä viikolla on kyse juuri tuosta välistä — pienestä etäisyydestä sen välillä, mitä tarkoitat ja mitä toinen kuulee. Tietokone elää tuossa välissä pysyvästi. Se ei arvaa mitä tarkoitit; se tekee mitä kirjoitit. Koko kurssi, jonka olet aloittamassa, rakentuu yhden kysymyksen ympärille, ja palaamme siihen monta kertaa:

**Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?**

Ensimmäinen vastaus ei ole "opettele ohjelmointikieli". Se tulee kurssilla myöhemmin. Ensimmäinen vastaus on: totuttele sanomaan *täsmälleen* mitä tarkoitat. Viikon päätteeksi osaat kirjoittaa selkeän, vaiheittaisen arkisen ohjeen, antaa sen sananmukaiselle tulkitsijalle, nähdä missä se hajoaa ja korjata sen. Ei koodia, ei erityisiä työkaluja. Pelkkiä huolellisia virkkeitä ja halua olla väärässä siitä, miten selkeä luulit olevasi.

---

## Oppitunti 1 — Tietokoneelle puhuminen (sananmukainen tulkinta ja monitulkintaisuus)

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

## Oppitunti 2 — Algoritmit arkielämässä

### Mikä algoritmi on?

**Algoritmi** on selkeä sananmukaisten vaiheiden sarja, joka vie sinut nykypaikastasi tavoitteeseen. Tämä on koko määritelmä. Sen ei tarvitse sisältää tietokonetta. Sen ei tarvitse olla pitkä. Sen ei tarvitse käyttää erityisiä sanoja. Isoäidin reseptikortille kirjoitettu resepti on algoritmi. Mielessä käymäsi tarkistuslista, kun lähdet kotoa, on algoritmi. Reitti, jota bussisi ajaa, on algoritmi. Jos sananmukainen tulkitsija voi suorittaa vaiheet ja saavuttaa tavoitteen, sinulla on algoritmi.

Sana kuulostaa tekniseltä, koska kuulemme sen yleensä yhteyksissä "YouTuben algoritmin muutos" tai "TikTokin algoritmi päätti". Nuo algoritmit ovat koodista tehtyjä ja hyvin suuria, mutta ne ovat pohjimmiltaan edelleen selkeiden vaiheiden sarjoja. Algoritmi, jonka olet kohta itse kirjoittamassa, on sama asia, vain lyhyempi.

### Algoritmit, joita jo käytät

Tässä on kolme algoritmia, jotka melkein varmasti suoritat joka päivä ajattelematta niitä sellaisina.

**Resepti — tee maidolla.** Tavoite: kuuma muki teetä maidolla. Syöte: teepussi, vettä, maitoa, sokeria (valinnainen), muki, vedenkeitin. Vaiheet: täytä vedenkeitin kylmällä vedellä, käännä vedenkeitin päälle, laita teepussi mukiin, odota kunnes vedenkeitin kiehuu, kaada vesi mukiin teepussin päälle, odota kolme minuuttia, ota teepussi pois, lisää tilkka maitoa, lisää sokeria jos haluat, sekoita. Tuloste: kuuma muki teetä maidolla.

Huomaa tuossa reseptissä neljä asiaa: **tavoite** (mihin pyrit), **syöte** (millä aloitat), **vaiheiden** sarja ja **tuloste** (mitä saat, kun algoritmi päättyy). Lähes jokaisessa algoritmissa, jonka kohtaat — arkisessa tai ICT:ssä — on nämä neljä osaa.

**Reitti — kotoa kouluun.** Tavoite: saapua kouluun ajoissa. Syöte: sinä, laukkusi, bussikorttisi, kellonaika keittiön kellossa, kotiovesi. Vaiheet: lähde kotoa klo 7:50, kävele Puistokadun bussipysäkille, ota bussi 12 keskustan suuntaan, jää pois pysäkillä nimeltä Tori, kävele kaksi korttelia itään, sisään pääportista. Tuloste: sinä, koulun sisällä, ajoissa.

**Aamurutiini.** Tavoite: lähteä kotoa valmiina päivään. Syöte: sinä, nukkumassa, sängyssä; herätyskello; vaatteet; aamupala keittiössä. Vaiheet: herätyskello soi, sammuta se, nouse sängystä, käy suihkussa, pukeudu, syö aamupala, pese hampaat, pakkaa laukku, laita kengät jalkaan, lähde. Tuloste: sinä, pukeutunut, syönyt, matkalla.

Mitään näistä ei ole kirjoitettu koodilla. Niiden ei tarvitse olla. Ne ovat silti algoritmeja, koska jokainen niistä kuvaa selkeän sananmukaisten vaiheiden sarjan tunnetusta syötteestä tunnettuun tulosteeseen.

Sama muoto esiintyy myös ICT-yhteydessä. Kuvittele ensimmäisen linjan help-desk-käsikirjoitus tilanteeseen "käyttäjä ei pysty kirjautumaan sisään". Tavoite: saada käyttäjä kirjautuneeksi. Syöte: käyttäjätunnus, virheilmoitus jonka hän näki, tietokone jolla hän on. Vaiheet: pyydä käyttäjää kirjoittamaan käyttäjätunnus hitaasti samalla kun katsot, tarkista onko caps lock päällä, pyydä häntä yrittämään vielä kerran, jos epäonnistuu nollaa hänen salasanansa, lähetä uusi hänen henkilökohtaiseen sähköpostiinsa, pyydä häntä kirjautumaan uudella salasanalla, pyydä häntä vaihtamaan se ensimmäisellä kirjautumisella. Tuloste: kirjautunut käyttäjä ja suljettu tiketti. Sama muoto: tavoite, syöte, vaiheet, tuloste.

> **Pysähdy hetkeksi:** Katso yllä olevaa aamurutiinin algoritmia. Jos sinun pitäisi antaa se sananmukaiselle tulkitsijalle — vaikkapa pölynimurirobotille, jolla on kädet — mikä vaihe hajoaisi ensimmäisenä? Onko se "nouse sängystä"? "Käy suihkussa"? "Pakkaa laukku"? Valitse yksi ja kirjoita yhdellä lauseella, miksi sananmukainen tulkitsija jäisi siinä jumiin.

### Kaksi algoritmia samaan tavoitteeseen

Yleinen virhe, kun ihmiset tapaavat sanan "algoritmi" ensimmäistä kertaa, on ajatella, että jokaista tavoitetta varten on yksi oikea algoritmi ja sinun tehtäväsi on löytää se. Ei pidä paikkaansa. Useimpiin arkisiin tavoitteisiin on useita kelvollisia algoritmeja, ja kaikki niistä toimivat.

Otetaan teeresepti uudelleen. Jotkut laittavat maidon ensin ja kaatavat kuuman veden päälle. Jotkut laittavat maidon viimeiseksi, sen jälkeen kun pussi on hautunut. Molemmat päättyvät kuumaan mukilliseen teetä, jossa on maitoa. Molemmat ovat oikein. Ne ovat eri algoritmeja samaan tavoitteeseen.

Tai otetaan reitti kotoa kouluun. Voit kävellä Puistokadun bussipysäkille ja ottaa bussin 12. Tai voit kävellä viisitoista minuuttia pidempään ja ottaa raitiovaunun. Tai aurinkoisena päivänä voit pyöräillä. Kolme erilaista algoritmia, sama tavoite: sinä, koulun sisällä, ajoissa.

Tällä on merkitystä, koska myöhemmin kurssilla alamme kysyä: "Onko jokin näistä algoritmeista *parempi* kuin toinen?" — ja jotta voit kysyä tämän kysymyksen, sinun on ensin hyväksyttävä, että useampi kuin yksi niistä voi olla kelvollinen. Toistaiseksi: huomaa kun sinä ja kaveri ratkaisette saman arkisen ongelman eri tavoin. Teillä molemmilla on toimivat algoritmit. Kumpikaan ei ole väärässä.

### Ensimmäisen algoritmin kirjoittaminen selkeällä suomella

Ennen kuin luet eteenpäin, kokeile tätä. Kirjoita paperille tai muistiinpanosovellukseen algoritmi, jota seuraat valmistaessasi mukillisen teetä, valmistautuessasi aamulla tai lähettäessäsi Discord-viestiä kaverille. Käytä selkeää suomea. Numeroi vaiheet. Yritä kirjoittaa viidestä kymmeneen vaiheeseen. Ennen kuin aloitat, kirjoita tavoite ylimmäs. Ennen vaiheita kirjoita mistä aloitat (syöte). Vaiheiden jälkeen kirjoita mihin päädyt (tuloste).

Jos huomaat kirjoittavasi vaiheen kuten "tee tavallinen juttu vedenkeittimellä", pysähdy ja pilko se pienemmiksi, sananmukaisemmiksi vaiheiksi. Sananmukainen tulkitsija ei tiedä, mikä "tavallinen juttu" on.

Tämä on sama toiminta, jonka muutat viikon tehtäväksi 1.1. Älä murehdi tyylikkyydestä. Murehdi selkeydestä.

> **Pysähdy hetkeksi:** Kun kirjoitit vaiheita, oliko paikkoja, joissa olit lähellä kirjoittaa sanoja kuten "tavallisesti", "yleensä", "se oikea" tai "se jota aina käytät"? Nuo sanat ovat varoitusvaloja. Sananmukaisella tulkitsijalla ei ole "tavallisesti". Ympyröi ne.

---

## Oppitunti 3 — Täsmälliset ja epätäsmälliset ohjeet

### Mitä "epätäsmällinen" tarkoittaa tässä?

**Epätäsmällinen** (tai **monitulkintainen**) ohje on sellainen, jota useampi kuin yksi sananmukainen tulkitsija voi suorittaa useammalla kuin yhdellä tavalla ja silti uskoa noudattaneensa sitä. Huomaa, ettei määritelmä sano mitään pituudesta. Hyvin lyhyt ohje voi olla täydellisen selkeä ("sulje ovi"). Hyvin pitkä voi olla toivottoman epäselvä, jos se käyttää koko ajan epämääräisiä sanoja.

Tässä on lyhyt ohje. Lue se kerran ja kysy itseltäsi, kuinka monta eri asiaa sananmukainen tulkitsija saattaisi tehdä sillä: *"Tallenna tiedosto tavalliseen paikkaan."*

Mikä on "tiedosto"? Se, joka sinulla on auki? Se, jota katsoit viisi minuuttia sitten? Se, jonka kollegasi mainitsi chatissa? Mikä on "tavallinen paikka"? Työpöytäsi? Jaettu levy? Kansio nimeltä `inbox`, jonka olet luvannut järjestää? Kuusi sanaa ja useita mahdollisia merkityksiä.

Selkeämpi versio voisi olla: *"Tallenna tiedosto `raportti-toukokuu.docx` (juuri nyt auki Wordissa) jaetun levyn kansioon `Tiimi/Raportit/2026/Toukokuu`."* Uusi versio on pidempi, mutta jättää tulkitsijalle vain yhden asian tehtäväksi.

### Monitulkintaisuuden jahtaaminen

Monitulkintaisuus arkisessa kielessä esiintyy yleensä muutamissa tunnistettavissa muodoissa. Kun tiedät mitä etsiä, alat huomata sitä kaikkialla.

**Epämääräiset substantiivit.** "Anna minulle se juttu." "Avaa tiedosto." "Vastaa sähköpostiin." Kaikissa näissä substantiivi (*juttu, tiedosto, sähköposti*) ei ole tarpeeksi tarkka osoittamaan yhtä esinettä. Korjaus: nimeä esine suoraan tai kuvaile se niin, että vain yksi esine sopii.

**Deiktiset sanat** (sanat, jotka riippuvat puhujan sijainnista). "Laita se tähän." "Vie tuo tuonne." "Lähetä se hänelle." *Tässä, tuolla, se, hän* riippuvat kontekstista, jota tulkitsija ei välttämättä jaa. Korjaus: korvaa deiktinen sana todellisella sijainnilla, esineellä tai henkilöllä.

**Suhteellinen aika.** "Aja skripti lounaan jälkeen." "Teen sen myöhemmin." "Lähetä se pian." *Lounaan jälkeen, myöhemmin, pian* tarkoittavat eri asioita eri ihmisille ja eri päivinä. Korjaus: nimeä tietty kellonaika tai tietty tapahtuma ilman monitulkintaisuutta ("klo 14:00 stand-upin jälkeen").

**Epämääräiset määrät.** "Lisää vähän maitoa." "Tee napista vähän isompi." "Vastaa muutamaan niistä." *Vähän, jonkin verran, muutama* ovat vaihteluvälejä, eivät lukuja. Korjaus: anna numero, mitta tai selkeä yläraja ("lisää 30 ml maitoa", "tee napista 24 pikseliä korkea", "vastaa kolmeen ensimmäiseen").

Samat neljä mallia esiintyvät ICT-yhteyksissä lähes sanasta sanaan. *Epämääräiset substantiivit:* "tallenna se kansioon" (mihin kansioon?). *Deiktiset:* "kirjaudu sisään täällä" (missä, millä sivulla?). *Suhteellinen aika:* "deployment menee ulos myöhemmin tänään" (ennen vai jälkeen klo 16:00 demoa?). *Epämääräiset määrät:* "lataus kestää hetken" (minuutin? tunnin?).

Kun luet jonkun muun kirjoittamaa ohjetta — tai sellaista, jonka kirjoitit itse viisi minuuttia sitten — näiden neljän mallin läpikäyminen mielessäsi on yksi nopeimmista monitulkintaisuusjahdeista, joita voit tehdä.

### Ohjeiden testaaminen toimimalla sananmukaisena tietokoneena

On olemassa yksi tekniikka, joka voittaa kaikki muut tekniikat oman ohjeen monitulkintaisuuden löytämisessä: **testaa se toimimalla itse sananmukaisena tulkitsijana.**

Oman ohjeen lukeminen ei riitä. Kun kirjoitit sen, tiesit mitä tarkoitit. Joten kun luet sen takaisin, luet mitä tarkoitit, et mitä kirjoitit. Aivosi täydentävät puuttuvat sanat automaattisesti. Ainoa tapa rikkoa tuo tapa on seurata ohjetta yksi vaihe kerrallaan, ilman muistia siitä mitä tarkoitit, niin kuin robotti tekisi. Jokaisessa vaiheessa kysyt: "Voinko tehdä tämän useammalla kuin yhdellä tavalla? Antoiko edellinen vaihe minulle sen, mitä tarvitsen tämän tekemiseen?"

Tästä on kyse viikon tehtävässä 1.1. Tehtävässä 1.1 kirjoitat ohjeen, annat sen todelliselle tulkitsijalle ja katsot kun hän jää jumiin. Oppitunnin 3 toisella puoliskolla "sananmukaisen tulkitsijan" tuntiharjoituksessa teet tämän livenä luokkakaverin kanssa, joka näyttelee sananmukaista tietokonetta.

Kun teet tämän ensimmäistä kertaa, yllätyt. Ohjeet, joista olit varma että ne ovat selkeitä, osoittautuvatkin sisältävän kolme tai neljä kohtaa, joissa tulkitsijan on arvattava. Se on normaalia. Jokainen ICT-ammattilainen huomaa sen ensimmäistä kertaa kirjoittaessaan ohjeen todelliselle käyttäjälle. Korjaus ei koskaan ole kirjoittaa pidempi ohje; se on kirjoittaa *sananmukaisempi*.

### Rajatapaukset (lempeä esittely)

Ohje voi olla täysin selkeä tavanomaisessa tapauksessa ja silti hajota epätavallisessa. Epätavallista tilannetta kutsutaan **rajatapaukseksi**.

Otetaan pieni ohje: *"Avaa jääkaappi ja ota maito."* Jos jääkaapissa on maitoa, ohje toimii. Mutta entä jos maitoa ei ole? Entä jos on kaksi pakettia ja yksi on viimeisen käyttöpäivän ylittänyt? Entä jos paketti on ovessa eikä hyllyllä? Nämä ovat rajatapauksia. Ne eivät tarkoita, että ohje on huono. Ne tarkoittavat, ettei ohje sano mitä tehdä, kun maailma ei ole siinä muodossa, jota kirjoittaja odotti.

Kestävämpi versio voisi sanoa: *"Avaa jääkaappi. Jos hyllyllä on maitopaketti, ota se. Jos niitä on useampi kuin yksi, ota se, jolla on aikaisin viimeinen käyttöpäivä. Jos niitä ei ole yhtään, kerro minulle."*

Sinun ei tarvitse ennakoida jokaista rajatapausta viikolla 1. Sinun täytyy vain alkaa huomata, että niitä on olemassa. Myöhemmin kurssilla (erityisesti viikolla 5, kun tapaat "jos/niin/muuten"-ajattelun) opit käsittelemään niitä tarkoituksellisesti. Toistaiseksi, kun kirjoitat algoritmin, kysy itseltäsi kerran: "Entä jos maailma ei ole siinä muodossa, jota odotin? Mitä tulkitsijani silloin tekisi?"

> **Pysähdy hetkeksi:** Ota aamurutiinin algoritmi, jonka kirjoitit (tai aiot kirjoittaa) oppitunnilla 2. Löydä yksi rajatapaus — tilanne, jossa jokin vaihe ei toimisi sellaisena kuin se on kirjoitettu. (Ei sopivia vaatteita? Ei kuumaa vettä? Herätyskello ei soinut?) Kirjoita yhdellä lauseella, mitä tulkitsijasi pitäisi siinä tilanteessa tehdä.

---

## Yhteenveto ja mitä seuraavaksi

Aloitit tämän viikon kysymyksellä: **Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?** Sinulla on nyt ensimmäinen vastaus kolmessa osassa.

Ensinnäkin, **tietokone seuraa ohjeita sananmukaisesti.** Tietokone on tarkka, ei luova. Kun jokin menee pieleen, kysymys ei ole mikä koneessa on vialla, vaan missä olit epäselvä.

Toiseksi, **algoritmi on arkinen nimi selkeälle sananmukaisten vaiheiden sarjalle.** Käytät algoritmeja joka päivä ajattelematta. Taito, jota tällä kurssilla kehität, on taito kirjoittaa algoritmeja, joita sananmukainen tulkitsija voi todella suorittaa.

Kolmanneksi, **ohjeet eivät ole valmiit, kun ne kuulostavat oikealta.** Ne ovat valmiit, kun sananmukainen tulkitsija voi suorittaa ne kysymättä. Ohjeen testaaminen — antamalla se todelliselle tulkitsijalle tai toimimalla itse sananmukaisena tulkitsijana — on ainoa luotettava tapa löytää epäselvät osat.

**Viikolla 2** pidämme sananmukaisen tulkitsijan ajattelutavan, mutta tartumme uuteen ongelmaan: mitä teet, kun tehtävä on liian iso mahtumaan yhteen algoritmiin? Vastaus on **ositus** — ongelman pilkkominen pienempiin ongelmiin, jotka voit ratkaista yksi kerrallaan. Tällä viikolla kirjoittamasi ohjeet ovat olleet riittävän pieniä, ettei ositusta ole tarvittu. Ensi viikolla ne suurenevat.

Säilytä tämän viikon tehtäviä koskevat muistiinpanosi. Käytät niitä uudelleen, erityisesti ensimmäisessä arvioitavassa tehtävässä viikon 2 lopussa.
