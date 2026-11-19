# Prosessin piirtäminen — vuokaaviot, abstraktio ja uudelleenkäytettävät lohkot

## Johdanto

Vietit viime viikon pilkkomalla isoa tehtävää pienempiin — päätehtävä, osatehtävät, osatavoitteet, riippuvuudet. Juuri se työ lähti käsistäsi **AT1**:nä tämän viikon alussa. Avaa AT1-vihkosi ja katso kirjoittamasi ositus. Sinulla on puu pieniä tehtäviä. Kuvittele nyt, että ojennat koko puun uudelle työkaverille ja kävelet pois. Mitä oikeasti annat hänelle? Pelkkä lista osatehtävien nimistä ei riitä — matkan varrella tulee valintoja. Tasainen lista jokaisesta yksittäisestä vaiheesta on liian pitkä yhdelle sivulle. Tarvitset jotakin muuta: kuvan.

Viikon keskeinen viesti on yksi lause:

> *"Kun osaat pilkkoa ongelman, seuraava taito on kuvata prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa."*

Tämä viikko harjoittaa kolmea tiiviisti toisiinsa liittyvää liikettä. **Oppitunti 7** esittelee **yksinkertaisen vuokaavion** — kurssin ensimmäisen kuvan, joka rakentuu neljästä peruskuviosta. **Oppitunti 8** esittelee **abstraktion** — valitsemisen, mitä jätetään pois, jotta kuva sopii yleisölle. Bussipysäkki kaupungin kartalla on abstraktio; "Tallenna"-painike puhelimessasi on abstraktio. **Oppitunti 9** esittelee **funktion** epävirallisen idean — prosessin osan, joka esiintyy monissa vuokaavioissa, nimetään kerran ja uudelleenkäytetään kaikkialla. *"Kirjaa käyttäjä sisään"* on yksi. *"Rekisteröi uusi laite"* on toinen. Viikolla 7 sama idea muuttuu oikeaksi JavaScript-funktioksi. Tällä viikolla se on nimetty laatikko ja yksi lause selkeää suomea sen alla. Ei vielä koodia.

Viikon 1 sananmukaisen tulkitsijan ajattelutapa pätee yhä. Jokaisen laatikon, jokaisen nimetyn lohkon, jokaisen kyllä/ei-polun lukee tulkitsija, joka ottaa sinut sanoistasi kiinni.

Viikolla 3 ei ole AT-palautusta. **AT2 — prosessikuvaus** palautetaan viikon 5 lopussa / viikon 6 aikana, ja tällä viikolla rakentamasi vuokaaviosanasto on juuri sitä, mitä AT2 odottaa.

---

## Oppitunti 7 — Prosessin kuvaaminen ja yksinkertainen vuokaavio

### Kun lista ei riitä

Kuvittele aamurutiinisi normaalina koulupäivänä. Herätyskello, ylösnousu, peseytyminen, pukeutuminen, syöminen, laukku, ulos ovesta. Seitsemän vaihetta tasaisella listalla. Sananmukainen tulkitsija voisi suorittaa tämän tekemättä yhtäkään päätöstä. Lista toimii.

Kuvittele nyt sama aamu, kun jokin on pielessä. *Soiko herätyskello oikeasti?* Jos soi, sinulla on aikaa aamupalalle. Jos ei, kello on jo 8:10 ja joudut jättämään aamupalan väliin. *Sataako?* Jos sataa, ota sateenvarjo mukaan. *Onko jääkaapissa maitoa?* Jos on, muroja; jos ei, paahtoleipää.

Tasainen lista ei pysty pitelemään tätä. *Vaihe 5 — syö aamupala* on nyt useita eri asioita riippuen useiden eri kysymysten vastauksista. Kun prosessissa on kolme tai neljä kysymystä, lista muuttuu lukukelvottomaksi.

Vuokaavio on se, miksi lista muuttuu, kun prosessissa on haaroja. Lista sanoo *tee tämä, sitten tämä*. Vuokaavio sanoo *tee tämä, sitten kysy tämä kysymys, ja vastauksesta riippuen mene tätä tai tuota kautta*. Sillä hetkellä kun prosessissa on kyllä/ei-kysymys, tasainen lista ei enää riitä.

Sama muutos tapahtuu help deskillä. *"Lähettikö käyttäjä kuvakaappauksen?"* Jos kyllä, liitä se ja jatka. Jos ei, pyydä se ensin. Tasainen lista ei voi piirtää tuota kysymystä. Vuokaavio voi.

### Neljä muotoa

Tämän kurssin vuokaavio käyttää täsmälleen neljää muotoa. Jokaisella on yksi tehtävä.

- **Alku / Loppu (soikio).** Soikio, joka aloittaa tai päättää vuokaavion. Jokaisessa vuokaaviossa on täsmälleen yksi **Alku**-soikio ja vähintään yksi **Loppu**-soikio. Alku-soikio kertoo, mistä prosessi alkaa; Loppu-soikio kertoo, mihin yksi polku päättyy.
- **Vaihe (suorakulmio).** Suorakulmio sisältää yhden toiminnon — *"Tarkista sääennuste"*, *"Tallenna tiedosto"*, *"Lähetä tiketti käyttäjälle"*. Yksi suorakulmio, yksi toiminto. Jos suorakulmio osoittautuu tarkoittavan kolmea eri asiaa, joko jaat sen kolmeksi suorakulmioksi tai piilotat ne nimetyn lohkon sisään (oppitunti 9).
- **Päätös (vinoneliö).** Vinoneliö sisältää yhden kyllä/ei-kysymyksen — *"Onko sadetodennäköisyys yli 50 %?"*, *"Vastaako tiedostonimi käytäntöä?"*, *"Pääseekö käyttäjä kirjautumaan?"*. Päätösvinoneliöstä lähtee täsmälleen kaksi nuolta, yksi kummallekin vastaukselle, ja jokaisella nuolella on oma merkintänsä (yleensä *Kyllä / Ei*).
- **Nuoli / virtaus.** Nuolet osoittavat järjestyksen, jossa tulkitsija liikkuu vuokaaviossa. Jokaisesta muodosta lähtee vähintään yksi nuoli paitsi Loppu-soikiosta. Päätösvinoneliöistä lähtee täsmälleen kaksi.

Neljä muotoa. Siinä on kuvan koko sanasto. Tämän oppitunnin taito ei ole muistaa lisää muotoja; se on käyttää näitä neljää hyvin.

Tässä on hyvin pieni vuokaavio, joka käyttää kaikkia neljää. Se on aamun sateenvarjopäätös prosessina piirrettynä:

```
   ( Alku )
       |
       v
[ Tarkista sääennuste ]
       |
       v
< Onko sadetodennäköisyys > 50 % ? >
   /                            \
  Kyllä                          Ei
   |                              |
   v                              v
[ Ota sateenvarjo ]      [ Jätä sateenvarjo ovelle ]
   \                              /
    \                            /
     v                          v
        ( Lähde kotoa )
```

Lue se ylhäältä. Alku. Tarkista ennuste. Kysy vinoneliössä oleva kysymys. Jos vastaus on kyllä, ota sateenvarjo. Jos ei, jätä se ovelle. Joka tapauksessa lähde kotoa. Vuokaaviossa on yksi Alku-soikio, yksi Loppu-soikio, kaksi suorakulmiota ennen vinoneliötä ja yksi sen jälkeen kummallakin polulla. Kahdeksan muotoa. Haara on koko syy, miksi tämä on vuokaavio eikä lista.

### Vuokaavion lukeminen

Vuokaavion lukeminen on nuolten seuraamista. Aloitat Alku-soikiosta. Jokaisen suorakulmion kohdalla teet, mitä siinä sanotaan. Jokaisen vinoneliön kohdalla kysyt kysymyksen ja otat sen nuolen, jonka merkintä vastaa vastausta. Pysähdyt, kun saavut Loppu-soikioon.

Kokeile sateenvarjovuokaaviota läpikäydyllä vastauksella. Ennuste sanoo 70 %:n sadetodennäköisyyttä. *Alku.* Tarkista ennuste. Osu vinoneliöön ja kysy *"onko sadetodennäköisyys > 50 %?"* — kyllä, 70 % on yli 50 %. Ota Kyllä-nuoli. Ota sateenvarjo. Lähde kotoa. Yksi läpiajo prosessista.

Kuvittele nyt, että ennuste sanoo 20 %. Sama vuokaavio, tällä kertaa Ei-nuoli, sateenvarjo jää ovelle. Kaksi pätevää läpiajoa, molemmat päättyvät samaan Loppu-soikioon. Sitä haara antaa sinulle.

Vuokaavio on oikein, kun **jokainen polku** sen läpi päätyy Loppu-soikioon. Nuoli, joka karkaa paperin laidan yli, jättää tulkitsijan jumiin.

### Ensimmäisen vuokaavion piirtäminen

Valitse yksi tuttu prosessi omasta elämästäsi, jossa on vähintään yksi kyllä/ei-kysymys: *"otanko sateenvarjon?"*, *"meneekö bussilla vai kävellen?"*, *"mikä laturi sopii tähän laitteeseen?"*, *"tallennanko tämän tiedoston päivämäärällä nimessä?"*. Valitse sellainen, jossa vastaus muuttuu päivästä toiseen.

Paperilla tai tabletilla piirrä neljä muotoa lyijykynällä. Alku-soikio ylös. Suorakulmiot toiminnoille, jotka teet aina. Vinoneliö siihen, missä joudut tekemään kyllä/ei-päätöksen. Kaksi nuolta vinoneliöstä, kumpikin merkitty. Suorakulmiot kummallekin haaralle. Loppu-soikio (tai kaksi, jos haarat päätyvät eri paikkoihin). Enintään kahdeksan muotoa — jos tarvitset enemmän, tarkkuustaso on liian matala ja oppitunti 8 auttaa.

Kun kaavio on piirretty, seuraa sitä silmilläsi Alusta Loppuun kummallakin haaralla. Teitkö oikeasti, mitä vuokaavio sanoo, tänä aamuna? Jos teit, vuokaavio on rehellinen. Jos et, korjaa vuokaavio — älä aamua.

Tämä on **Tehtävän 3.1** työ. Piirrä vuokaavio, allekirjoita ja päivää se, ja säilytä siitä valokuva AT2-muistiinpanoihisi.

> **Pysähdy hetkeksi:** Katso tähänastista aamuasi tänään. Oliko siinä hetki, jolloin teit kyllä/ei-päätöksen sitä ajattelematta (sateenvarjo, bussi tai kävely, kuuma vai kylmä juoma)? Voisitko kuvata sen päätöksen yhtenä vinoneliönä, josta lähtee kaksi nuolta? Mitä ne kaksi nuolta oikeasti tekivät tänään?

### ICT-esimerkit

Kaksi lyhyttä ICT-prosessia vuokaavioina piirrettynä.

**Help desk -triage.** Käyttäjä avaa tiketin sanoen *"En pääse kirjautumaan"*. Ensimmäisen tason agentin täytyy päättää, mitä seuraavaksi.

```
   ( Alku — tiketti vastaanotettu )
        |
        v
[ Lue tiketin teksti ]
        |
        v
< Pääseekö käyttäjä nyt kirjautumaan? >
   /                              \
  Kyllä                            Ei
   |                                |
   v                                v
[ Sulje tiketti ]       [ Pyydä käyttäjältä kuvakaappaus ]
   |                                |
   v                                v
( Suljettu )                  ( Odota vastausta )
```

Yksi päätösvinoneliö, kaksi polkua, kaksi eri Loppu-soikiota. *"Pääseekö käyttäjä nyt kirjautumaan?"* johtaa rehellisesti kahteen lopputulokseen.

**Tiedostonimien tarkistus.** Ennen kuin tallennat dokumentin jaetulle asemalle, koulun käytäntö sanoo, että tiedosto on nimettävä muotoon `2026-05-20_lasku-001.pdf`.

```
   ( Alku )
       |
       v
[ Katso tiedostonimi ]
       |
       v
< Vastaako tiedostonimi käytäntöä? >
   /                              \
  Vastaa                       Ei vastaa
   |                                |
   v                                v
[ Tallenna jaetulle asemalle ]   [ Nimeä tiedosto ensin uudelleen ]
   |                                |
   v                                v
( Tallennettu )            [ Tallenna jaetulle asemalle ]
                                    |
                                    v
                              ( Tallennettu )
```

Huomaa kaksi asiaa. Haarojen merkinnät ovat *Vastaa / Ei vastaa* — sääntö on *jokaisella haaralla on lyhyt merkintä*, ja *Vastaa* lukee selvemmin kuin *Kyllä* tässä yhteydessä. Molemmat haarat päätyvät lopulta *Tallennettu*-Loppu-soikioon, mutta Ei vastaa -polulla on ylimääräinen vaihe.

> **Pysähdy hetkeksi:** Valitse yksi ICT-tehtävä, jonka olet oikeasti tehnyt — sovelluksen asennus, tiedoston jakaminen, videopuheluun liittyminen. Onko siinä piilossa kyllä/ei-kysymys, jonka teet sitä ajattelematta? Miltä vinoneliö näyttäisi?

---

## Oppitunti 8 — Abstraktio

### Mitä "abstraktio" tarkoittaa tässä

Kun piirsit vuokaaviosi, teit valinnan jokaisessa suorakulmiossa. *"Tarkista sääennuste"* on yksi laatikko. Se olisi voinut yhtä hyvin olla neljä: *"Avaa sääsovellus → lue tämän päivän ennuste → katso sadetodennäköisyys → sulje sovellus"*. Molemmat kuvaavat samaa toimintoa. Piirsit yhden laatikon neljän sijaan. **Tuo valinta on abstraktio.**

Abstraktio on liike, jossa **piilotetaan se yksityiskohta, jolla ei ole merkitystä sillä tasolla, jolla kuvailet**. Piirtämäsi laatikot pysyvät täsmällisinä; valitset vain, ettet piirrä laatikoita, jotka eivät auttaisi lukijaa tällä tasolla. Abstraktio ei ole epämääräisyyttä — *"tarkista sää"* on täsmällinen siitä, *mitä* tulkitsija tekee. Se vain piilottaa *miten*.

Pieni arkielämän esimerkki. Kuvittele kaupungin bussipysäkki — vaikkapa Puistokadun pysäkki, se koulusi lähellä. Bussia odottavalle matkustajalle bussipysäkki on kyltti, jossa lukee "Puistokatu", ja sen alla aikataulu. Tuo on abstraktio, jonka matkustaja tarvitsee. Kaupungin valvontakeskuksen bussilähetille sama pysäkki on GPS-koordinaatti, ID-numero tietokannassa ja lista seuraavan 20 minuutin sisällä saapuvista busseista. Aikataulunäyttöä vaihtavalle insinöörille se on sähkökytkentärasia ja joukko ruuveja. Sama fyysinen asia. Kolme abstraktiota, kukin oikea eri yleisölle.

Tämä abstraktio on tässä: valitaan, mitä jätetään pois, jotta kuvaus sopii yleisölle.

### "Kirjaudu sisään" -painike on abstraktio

Nyt ICT-esimerkki. Avaa koulusi portaali ja katso *Kirjaudu sisään* -painiketta. Kolme sanaa tekstiä ja värillinen suorakulmio.

Mitä sen sisälle on piilotettu? Kun painat painiketta, sivu lähettää käyttäjätunnuksesi ja salasanasi koulun tunnistuspalvelimelle. Palvelin tarkistaa salasanan tallennettua, salattua versiota vasten. Jos tarkistus menee läpi, palvelin lähettää takaisin *evästeen*, jonka selain tallentaa; jokainen sivu, jonka jälkeenpäin avaat, sisältää evästeen, joten järjestelmä tietää, että olet edelleen sinä. Jos koulu kirjautuu Microsoftin tai Googlen kautta, mukaan tulee myös kolmen palvelimen välinen edestakaisin OAuth-tanssi, joka kaikki tapahtuu, kun pyörivä ympyrä on edelleen ruudulla.

Tuon abstraktion Kirjaudu sisään -painike sinulle ostaa. Painike tarkoittaa *"kirjaudu portaaliin"*. Et näe tunnistuspalvelinta, salasanan tarkistusta, evästettä etkä OAuth-tanssia. Ne ovat **piilotettuja** — yhä olemassa, mutta eivät painikkeessa. Painike on oikea kuvaus *käyttäjälle*.

Kuvittele nyt sama painike sellaisena kuin se näkyy tietoturvainsinöörille, joka tutkii epäonnistunutta sisäänkirjautumista. *Kirjaudu sisään* ei riitä siellä; insinööri tarvitsee pyynnön, vastauksen, evästeen, aikaleimat. Sama painike. Kaksi yleisöä. Kaksi oikeaa vastausta.

### Tarkkuustaso seuraa yleisöä

Tässä nyrkkisääntö, joka pitää oppitunnin kasassa. **Oikea tarkkuustaso seuraa yleisöä.**

Ennen kuin päätät *mitkä laatikot piirrät*, kysy *kuka tämän lukee ja mitä hän tekee sillä?*

Tiedostonimien tarkistuksen vuokaavio aivan uudelle help desk -työntekijälle ensimmäisenä päivänä tarvitsee enemmän suorakulmioita — *"avaa tiedostonimisäännöt-dokumentti"*, *"katso nykyinen käytäntö"*, *"tarkista nimen jokainen osa"*. Ehkä kuusi suorakulmiota ennen vinoneliötä.

Saman tarkistuksen vuokaaviossa vanhemmalle ICT-järjestelmänvalvojalle, joka on ollut talossa kymmenen vuotta, on yksi suorakulmio: *"Lue tiedostonimi"*. Sama prosessi, sama tavoite, eri yleisö, eri tarkkuustaso. Molemmat ovat oikein. Kysymyksellä *"mikä on oikea tarkkuustaso?"* ei ole universaalia vastausta — vain vastaus *tälle yleisölle*.

### Piilottaminen vs. unohtaminen

Abstraktio on yksityiskohdan **piilottamista**, ja piilottaminen ei ole sama kuin **unohtaminen**.

Pieni arkielämän esimerkki. Aamurutiinisi vuokaaviossa on suorakulmio, jossa lukee *"Pukeudu"*. Olet piilottanut tuohon suorakulmioon paljon yksityiskohtaa — mitkä vaatteet, missä järjestyksessä. Mitään niistä ei ole vuokaaviossa, mutta et ole unohtanut mitään niistä. Jos pikkuserkkusi kysyy *"mitä 'pukeudu' tarkoittaa?"*, voit avata suorakulmion mielessäsi ja vastata. Yksityiskohta on yhä siellä. Se on **arkistoitu**, ei poistettu.

Unohtaminen on, kun kirjoitat *"pukeudu"* etkä enää tiedä, mitä se tarkoittaa. Sananmukainen tulkitsija avaa laatikon eikä löydä mitään sisältä.

ICT-versio. Kirjaudu sisään -painike piilottaa OAuth-tanssin. Koulun portaalin kolme vuotta sitten pystyttäneellä insinöörillä on OAuth-vaiheet kirjoitettuna jonnekin runbookiin. Piilotettu yksityiskohta on arkistoitu. *Piilotettu* tarkoittaa, että on paikka, johon katsoa. *Unohdettu* tarkoittaa, että ei ole.

Vaihtokauppa yhdessä lauseessa: hyvä abstraktio piilottaa sen, mikä ei auta lukijaa tällä tasolla, **ja osoittaa, mihin yksityiskohta on arkistoitu** niille lukijoille, jotka sitä tarvitsevat.

> **Pysähdy hetkeksi:** Valitse yksi painike, linkki tai valikkokohta jossakin oikeasti käyttämässäsi ohjelmassa — Discordin "Lähetä", Spotifyn "Toista", puhelimesi "Ota kuva", koulun portaalin "Lähetä". Listaa kolme asiaa, jotka piiloutuvat sen sisälle, kun painat sitä. Ovatko ne kolme asiaa piilotettuja (arkistoitu jonnekin) vai unohdettuja? Miten saisit selville, kumpia ne ovat?

> **Pysähdy hetkeksi:** Ota oppitunnin 7 Tehtävän 3.1 vuokaaviosi. Valitse yksi suorakulmio. Onko tarkkuustaso siinä suorakulmiossa oikea *sinulle, joka piirrät omaa aamuasi*, vai onko se itse asiassa oikea *jollekulle toiselle*, joka lukisi sen? Jos se on väärä yleisö, piirtäisitkö suorakulmion eri tavalla oikealle yleisölle?

---

## Oppitunti 9 — Uudelleenkäytettävät ohjeet: funktion idea ilman koodia

### Kun sama osa toistuu

Katso kahta vuokaaviota rinnakkain.

Ensimmäinen on *"ensimmäinen päivä uudessa koulussa"*. Jossakin keskivaiheilla on osa: *Avaa koulun portaali → kirjoita käyttäjätunnus → kirjoita salasana → paina Kirjaudu sisään → odota aloitussivua*. Viisi suorakulmiota.

Toinen on *"palauta tehtävä verkossa"*. Alkupuolella sama osa esiintyy: *Avaa koulun portaali → kirjoita käyttäjätunnus → kirjoita salasana → paina Kirjaudu sisään → odota aloitussivua*.

Voisit piirtää sen joka kerta uudelleen. Kolmannen vuokaavion kohdalla käsi on väsynyt ja sivu on täynnä, ennen kuin pääset kiinnostavaan kohtaan. Parempi liike on olemassa. **Anna osalle nimi.**

### Anna osalle nimi

Nimi on lyhyt verbi-ilmaisu, joka sanoo, *mitä osa tekee*, ei *miten se sen tekee*. Yllä olevan osan nimi on *"kirjaa käyttäjä sisään"*. Kolme sanaa. Koko osa verbi-ilmaisuna.

Hyvä nimi läpäisee yksinkertaisen testin. Joku, joka ei ole ikinä nähnyt alkuperäistä viittä suorakulmiota, voi lukea *"kirjaa käyttäjä sisään"* ja tietää, mitä odottaa: tämän laatikon lopussa käyttäjä on kirjautunut sisään. Hän ei tiedä, *miten* — se on piilotettu. Mutta hän tietää, *mitä*, ja hän tietää, *milloin laatikko on valmis*.

Lisää nimiä arjen ja ICT:n maailmoista: *"nimeä tiedosto uudelleen"*, *"varmuuskopioi laite"*, *"nollaa salasana"*, *"rekisteröi uusi laite"*, *"lähetä ilmoitus vanhemmalle"*. Jokainen on verbi-ilmaisu, joka kertoo, mitä tapahtuu.

Huono nimi epäonnistuu testissä. *"Tee se juttu"* ei kerro kenellekään mitään. *"Vaihe 7"* on vain numero. Sääntö on *verbi-ilmaisu, joka sanoo, mitä se tekee*.

Nyt toinen vuokaavio, jossa nimetty lohko on viiden suorakulmion paikalla:

```
   ( Alku — opiskelija haluaa palauttaa tehtävän )
        |
        v
[ kirjaa käyttäjä sisään ]   <-- yksi nimetty lohko, ei viisi suorakulmiota
        |
        v
[ Etsi tehtävä kurssilistasta ]
        |
        v
[ Lataa tiedosto ]
        |
        v
[ Klikkaa palauta ]
        |
        v
( Palautettu )
```

Yhteensä viisi vuokaaviomuotoa. Alkuperäisessä olisi ollut yhdeksän. Vuokaavio mahtuu sivulle, lukija näkee kiinnostavan kohdan selvästi, ja *"kirjaa käyttäjä sisään"* sisältää edelleen kaikki viisi alkuperäistä vaihetta — ne vain elävät erillisessä kuvauksessa vuokaavion alla.

### Mitä "funktio" tarkoittaa tämän viikon merkityksessä

Viikolla 3 **funktio** määritellään epävirallisesti **nimetyksi, uudelleenkäytettäväksi prosessin osaksi, joka kuvataan selkeällä suomella ja jolla on selkeä syöte ja selkeä tuloste**. Viisi asiaa pidettäväksi mielessä:

- **Nimetty** — lyhyt verbi-ilmaisu nimenä.
- **Uudelleenkäytettävä** — esiintyy useammassa kuin yhdessä isommassa prosessissa.
- **Prosessin osa** — joukko vaiheita ryhmiteltynä, yleensä 3–8.
- **Selkeällä suomella oleva kuvaus** — lyhyt kappale siitä, mitä osa tekee.
- **Syöte ja tuloste** — mitä se tarvitsee alkuun ja mitä se tuottaa valmiina.

*"Kirjaa käyttäjä sisään"* -kuvaus:

> **kirjaa käyttäjä sisään** — Vie käyttäjän ei-kirjautuneesta tilasta kirjautuneeseen tilaan. Käyttäjä avaa portaalin, kirjoittaa käyttäjätunnuksensa ja salasanansa, painaa Kirjaudu sisään ja odottaa aloitussivua.
> **Syöte:** käyttäjällä on voimassa oleva käyttäjätunnus ja salasana.
> **Tuloste:** käyttäjä on kirjautunut sisään ja portaalin aloitussivu on näytöllä.

Tuo on koko "funktio" viikon 3 merkityksessä. **Ei koodia, ei sulkeita, ei paluuarvoja.** Se kaikki tulee viikolla 7. Tällä viikolla funktio on nimetty laatikko vuokaaviossa ja kappale sen alla.

Toinen esimerkki:

> **nimeä tiedosto uudelleen koulun käytäntöön** — Ottaa tiedoston, jolla on jokin nimi, ja tuottaa tiedoston, jonka nimi noudattaa koulun päivämäärä-ja-aihe-käytäntöä.
> **Syöte:** tiedosto on olemassa; käyttäjä tietää päivämäärän ja yksisanaisen aiheen.
> **Tuloste:** tiedoston nimi on muotoa `VVVV-KK-PP_aihe.lopppää`.

Jokaisella nimetyllä lohkolla on selkeä syöte, selkeä tuloste ja yhden kappaleen kuvaus. AT2 pyytää sinua kirjoittamaan tämän muodon — joten kannattaa harjoitella sitä nyt.

### Ammatillinen esimerkki — "rekisteröi uusi laite"

Tämän viikon ICT-esimerkki, johon nojataan, on **"rekisteröi uusi laite"**. Aina kun uusi läppäri, projektori tai kokoushuoneen näyttö saapuu kouluun, joku ajaa saman osan: tarra sarjanumerolla, merkintä laitehakemistoon, asenna vakio-ohjelmistopaketti, tarkista verkko. Noin kahdeksan vaihetta, joka kerta, jokaiselle uudelle laitteelle.

Vuokaavio *"perusta uusi kokoushuone"* -prosessille ilman nimettyä lohkoa:

```
( Alku ) → [ Tilaa näyttö ] → [ Vastaanota näyttö ] → [ Tarra sarjanumerolla ]
   → [ Lisää merkintä laitehakemistoon ] → [ Asenna vakio-ohjelmistot ] → [ Tarkista verkko ]
   → [ Asenna seinälle ] → [ Vedä kaapeli läppäritelakkaan ] → [ Testaa testiläppärillä ]
   → ( Valmis )
```

Kymmenen laatikkoa. Puolet on "rekisteröi laite" -vaiheita. ICT-päällikkö, joka välittää kokoushuoneesta, joutuu silmäilemään viisi rekisteröi-laite-laatikkoa ennen kuin saavuttaa kiinnostavan kohdan.

Sama vuokaavio nimetyn lohkon kanssa:

```
( Alku ) → [ Tilaa näyttö ] → [ Vastaanota näyttö ] → [ rekisteröi uusi laite ]
   → [ Asenna seinälle ] → [ Vedä kaapeli läppäritelakkaan ] → [ Testaa testiläppärillä ]
   → ( Valmis )
```

Seitsemän laatikkoa. Nimetty lohko kantaa viisi piilotettua vaihetta. Piilotetut vaiheet ovat edelleen olemassa — ne elävät "rekisteröi uusi laite" -kuvauksessa, joka on arkistoitu koulun ICT-käsikirjaan harjoittelijalle, joka oikeasti joutuu ajamaan tuon lohkon.

### Vaihtokauppa yhdessä lauseessa

Nimetty lohko **piilottaa yksityiskohdan**, jotta tämän tason lukijat eivät huku, **mutta yksityiskohtaa tarvitsevan lukijan täytyy tietää, mistä katsoa**. Oppitunnin 8 abstraktio koski sitä, *mitkä laatikot ansaitsevat tulla piirretyiksi*; oppitunnin 9 nimetyt lohkot ovat sama liike korkeammalla zoomaustasolla — yksi laatikko, joka edustaa kokonaista alivuokaaviota.

Silta viikkoon 7. Siellä *"kirjaa käyttäjä sisään"* muuttuu oikeaksi JavaScript-funktioksi. Verbi-ilmaisusta tulee funktion nimi; selkeällä suomella oleva syöte ja tuloste muuttuvat parametreiksi ja paluuarvoiksi; osasta tulee koodia. Mutta *muoto* — nimetty, uudelleenkäytettävä osa, jolla on syöte ja tuloste — on se, jonka rakennat tällä viikolla, suomeksi, lyijykynällä.

> **Pysähdy hetkeksi:** Katso Tehtävän 3.1 vuokaaviotasi ja kaikkia muita tällä viikolla piirtämiäsi vuokaavioita. Onko niissä kolmen tai neljän laatikon osa, jonka epäilet esiintyvän myös jossakin toisessa tekemässäsi prosessissa? Kirjoita sille verbi-ilmaisu nimeksi nyt, ennen kuin luet eteenpäin.

---

## Yhteenveto ja mitä seuraavaksi

Viikko 3 lisäsi yhden liikkeen viikon 2 osituksen päälle. Opit kuvaamaan tehtävän vuokaaviona neljällä muodolla, valitsemaan oikean tarkkuustason yleisölle ja tunnistamaan toistuvia prosessin osia ja antamaan niille uudelleenkäytettäviä nimiä. Viikon 1 sananmukaisen tulkitsijan ajattelutapa pätee yhä jokaisessa laatikossa: jokainen suorakulmio sanoo yhden asian, jokainen vinoneliö kysyy yhden kysymyksen, jokainen nuoli menee yhteen paikkaan.

Viikon keskeinen viesti vielä kerran, sanasta sanaan:

> *"Kun osaat pilkkoa ongelman, seuraava taito on kuvata prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa."*

Jos osaat piirtää pienen vuokaavion, valita tarkkuustason yleisölle ja nimetä yhden uudelleenkäytettävän osan, olet tehnyt sen liikkeen, jonka viikko 3 harjoitti.

**Viikolla 4** kysymys muuttuu. Tähän asti olet kirjoittanut *yhden* hyvän kuvauksen prosessista. Viikko 4 kysyy: *mitä jos samalle tavoitteelle on useampi kuin yksi pätevä vuokaavio?* Piirrät kaksi pätevää vuokaaviota samalle tehtävälle, vertailet niitä yksinkertaisilla kriteereillä ja harjoittelet vertaispalautetta.

Säilytä Tehtävän 3.1 vuokaaviosi, nimetyt lohkot -muistiinpanosi ja abstraktiopohdintasi. Tämän viikon sanasto — *vuokaavio*, *päätös*, *abstraktio*, *tarkkuustaso*, *uudelleenkäytettävä lohko*, *nimetty lohko / funktio* — on juuri sitä, mitä **AT2 — prosessikuvaus** odottaa viikon 5 lopussa / viikon 6 aikana.
