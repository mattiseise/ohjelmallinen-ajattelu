# Oppitunti 2 — Algoritmit arkielämässä

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
