# Oppitunti 3 — Täsmälliset ja epätäsmälliset ohjeet

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
