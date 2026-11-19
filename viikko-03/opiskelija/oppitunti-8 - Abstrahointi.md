# Oppitunti 8 — Abstrahointi

### Mitä “abstrahointi” tarkoittaa tässä?

Kun piirsit vuokaaviosi, teit valinnan jokaisessa suorakulmiossa. “Tarkista sääennuste” on yksi
laatikko. Se olisi yhtä hyvin voinut olla neljä laatikkoa: “Avaa sääsovellus → lue päivän ennuste
→ katso sateen todennäköisyys → sulje sovellus.” Molemmat kuvaavat samaa toimintaa. Piirsit
yhden laatikon neljän sijasta. Tuo valinta on abstrahointia.
Abstrahointi on liikettä, jossa piilotetaan yksityiskohta, jolla ei ole merkitystä sillä
tasolla, jolla asiaa juuri nyt kuvataan. Piirtämäsi laatikot pysyvät täsmällisinä; et vain
piirrä niitä laatikoita, jotka eivät tällä tasolla auttaisi lukijaa. Abstrahointi ei ole
epämääräisyyttä — “tarkista sää” on täsmällinen sen suhteen, mitä suorittaja tekee. Se vain
piilottaa miten.
Pieni arkinen esimerkki: ajattele bussipysäkkiä koulun lähellä. Bussia odottavalle
matkustajalle pysäkki on kyltti, jossa lukee pysäkin nimi, ja sen alla aikataulu. Se on juuri se
abstraktio, jonka matkustaja tarvitsee. Liikenteenohjauskeskuksen työntekijälle sama pysäkki
on GPS-koordinaatti, tietokannan tunniste ja lista busseista, jotka saapuvat seuraavan 20
minuutin aikana. Näyttölaitteen asentajalle pysäkki on sähkölaatikko ja ruuveja. Sama
fyysinen kohde. Kolme eri abstrahointia. Jokainen oikea eri yleisölle.
Juuri tätä abstrahointi tässä tarkoittaa: sen päättämistä, mitä jätetään pois, jotta kuvaus sopii
yleisölle.

### “Kirjaudu sisään” -painike on abstraktio

Otetaan IT-esimerkki. Avaa koulusi portaali ja katso Kirjaudu sisään -painiketta. Muutama
sana tekstinä ja värillinen suorakulmio. Mitä kaikkea sen sisällä on piilossa?
Kun painat painiketta, sivu lähettää käyttäjätunnuksesi ja salasanasi koulun
tunnistautumispalvelimelle. Palvelin tarkistaa salasanan verraten sitä tallennettuun, salattuun
versioon. Jos tarkistus onnistuu, palvelin palauttaa evästeen (cookie), jonka selain tallentaa;
jokainen seuraava sivu lähettää tämän evästeen mukana, jotta järjestelmä tietää edelleen sinun
olevan sinä. Jos koulu käyttää kirjautumiseen Microsoftia tai Googlea, taustalla tapahtuu lisäksi
usean palvelimen välinen edestakainen viestinvaihto, jota kutsutaan OAuth-tanssiksi — kaikki
tämä samalla kun ruudulla näkyy pyörivä latauskuvake.
Juuri tämän kaiken Kirjaudu sisään -painike ostaa sinulle abstraktiona. Painike tarkoittaa
käyttäjälle: “kirjaudu portaaliin”. Et näe tunnistautumispalvelinta, salasanan tarkistusta,
evästettä etkä OAuth-tanssia. Ne ovat piilossa — yhä olemassa, mutta eivät painikkeessa.
Painike on oikea kuvaus käyttäjälle.
Kuvittele nyt sama painike tietoturva-asiantuntijalle, joka selvittää epäonnistunutta
kirjautumista. Pelkkä Kirjaudu sisään ei enää riitä; asiantuntija tarvitsee pyynnön, vastauksen,
evästeen ja aikaleimat. Sama painike. Kaksi yleisöä. Kaksi oikeaa vastausta.

### Yksityiskohtaisuuden taso seuraa yleisöä

Tämän oppitunnin sääntö voidaan sanoa näin:

### Oikea yksityiskohtaisuuden taso seuraa yleisöä.

Ennen kuin päätät, mitkä laatikot piirrät, kysy: kuka tämän lukee ja mitä hän tekee sillä?
Vuokaavio tiedostonimen tarkistuksesta aivan uudelle helpdesk-harjoittelijalle ensimmäisenä
päivänä tarvitsee enemmän suorakulmioita — esimerkiksi “avaa tiedostonimikäytäntöjen
ohje”, “etsi nykyinen nimeämistapa”, “tarkista jokainen nimen osa”. Saattaa olla kuusi laatikkoa
ennen vinoneliötä. Sama vuokaavio kokeneelle IT-ylläpitäjälle, joka on tehnyt työtä kymmenen
vuotta, voi sisältää yhden laatikon: “Lue tiedostonimi.” Sama prosessi, sama tavoite, eri yleisö,
eri yksityiskohtaisuuden taso. Molemmat voivat olla oikein.
Kysymykseen “mikä on oikea yksityiskohtaisuuden taso?” ei ole yhtä universaalia vastausta. On
vain vastaus tälle yleisölle.

### Piilottaminen ei ole unohtamista

Abstrahointi on yksityiskohdan piilottamista, eikä piilottaminen ole sama asia kuin

unohtaminen.

Pieni arkinen esimerkki: aamurutiinisi vuokaaviossa on laatikko “Pukeudu”. Tuohon
laatikkoon on piilotettu paljon yksityiskohtia — mitkä vaatteet, missä järjestyksessä. Mikään
tästä ei näy vuokaaviossa, mutta et ole unohtanut sitä. Jos pikku serkkusi kysyy “mitä
‘pukeudu’ tarkoittaa?”, pystyt avaamaan laatikon mielessäsi ja selittämään. Yksityiskohta on
yhä olemassa. Se on arkistoitu, ei poistettu.
IT-versio on sama. Kirjaudu sisään -painike piilottaa OAuth-tanssin. Asiantuntija, joka asensi
koulun portaalin kolme vuotta sitten, on todennäköisesti kirjannut OAuth-vaiheet jonnekin
käyttöohjeeseen tai dokumentaatioon. Piilotettu yksityiskohta on arkistoitu. Piilotettu
tarkoittaa, että on olemassa paikka, josta yksityiskohta löytyy. Unohdettu tarkoittaa, että
sellaista paikkaa ei ole.
Yhteen lauseeseen tiivistetty vaihtokauppa kuuluu näin: hyvä abstraktio piilottaa sen, mikä ei
auta lukijaa tällä tasolla, ja osoittaa, mistä yksityiskohta löytyy, jos lukija tarvitsee sen.
Pysähdy hetkeksi: Valitse yksi ohjelman painike, linkki tai valikkokohta, jota käytät
oikeasti — Discordin Lähetä, Spotifyn Toista, puhelimen Ota kuva tai koulun
portaalin Palauta. Listaa kolme asiaa, jotka ovat sen sisällä piilossa, kun painat sitä.
Ovatko ne piilotettuja (jossain dokumentoituna) vai unohdettuja? Miten voisit
selvittää, kumpi on totta?
Pysähdy hetkeksi: Palaa tehtäväsi 3.1 vuokaavioon oppitunnilta 7. Valitse yksi
suorakulmio. Onko sen yksityiskohtaisuuden taso oikea sinulle, joka piirsit oman
aamusi, vai oikea jollekin toiselle, joka lukisi sen? Jos yleisö on väärä, piirtäisitkö
laatikon eri tavalla oikeaa yleisöä varten?
Vinkki: jos laatikko tuntuu liian suurelta, kysy itseltäsi kaksi kysymystä: kuka tämän lukee? ja
mitä hänen pitää tämän jälkeen tehdä? Usein oikea taso löytyy juuri siitä.
