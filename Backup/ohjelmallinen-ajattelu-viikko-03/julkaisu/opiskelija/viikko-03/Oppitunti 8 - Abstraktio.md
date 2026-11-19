# Oppitunti 8 — Abstraktio

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
