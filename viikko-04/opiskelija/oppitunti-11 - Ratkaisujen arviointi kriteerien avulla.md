# Oppitunti 11 — Ratkaisujen arviointi kriteerien avulla

### Mausta kriteeriin

Näin usein käy, kun luokalle näytetään kaksi toimivaa ratkaisua. Joku sanoo: “Pidän vain
ensimmäisestä enemmän.” Joku toinen sanoo: “Toinen on se oikea tapa.” Kolmas kohauttaa
olkapäitään. Mikään näistä reaktioista ei auta, koska mikään niistä ei nimeä, millä tavalla
ratkaisu on parempi missä kohtaa. Ne ovat kaikki makua.
Kriteeri on nimetty mittapuu, joka muuttaa maun päättelyksi. Sen sijaan, että sanoisit “Pidän
A:sta enemmän”, sanot: “A on selkeämpi vaiheessa 5, koska ‘3 minuuttia’ kertoo suorittajalle
täsmälleen, milloin pitää lopettaa.” Tuo lause nimeää ominaisuuden (selkeys), osoittaa tietyn
kohdan (vaihe 5) ja antaa konkreettisen syyn. Siitä voi keskustella itse tuotoksen perusteella, ei
päivän fiiliksen perusteella.
Viikon keskeinen liike voidaan kirjoittaa vielä kerran näin:

### Samaan ongelmaan voi olla useampi kuin yksi toimiva ratkaisu. Niiden väliltä

valitseminen ei ole makuasia vaan nimettyjen kriteerien asia.

Siirrytään muodosta “Pidän tästä enemmän” muotoon “tämä on parempi selkeyden kannalta”.
Mielipiteestä nimettyyn ominaisuuteen ja tarkkaan kohtaan.

### Kurssin neljä kriteeriä

Tällä kurssilla käytämme neljää kriteeriä. Ne eivät ole maailman ainoat kriteerit — oikeassa
IT-työssä on myös kustannuksia, saavutettavuutta ja tietoturvaa. Neljä riittää harjoittelemaan
ajattelutapaa. Ensimmäisellä maininnalla ne esiintyvät aina samassa järjestyksessä:

### selkeys, tehokkuus, toistettavuus, virhealttius

Selkeys. Kuinka helppo ratkaisu on lukea kerran ja toteuttaa ilman lisäkysymyksiä. Selkeä
ohje nimeää oikean vaiheen, oikean kohteen ja oikean seuraavan liikkeen; epäselvä ohje jättää
kirjaimellisen suorittajan arvaamaan.
Arki: “lisää teepussi” on selkeämpi kuin “lisää se juttu”.
IT: “tallenna tiedosto nimellä jaetulle asemalle” on selkeämpi kuin `2026-05-20_invoice.pdf`
“tallenna se sinne, minne se kuuluu”.
Tehokkuus. Kuinka vapaa ratkaisu on turhista vaiheista. Tehokas ratkaisu saavuttaa
tavoitteen ilman kiertoteitä, toistoa tai uudelleen tekemistä — kyse ei ole vain nopeudesta vaan
turhien vaiheiden puutteesta.
Arki: veden lämmittäminen kerran on tehokkaampaa kuin keittäminen, jäähdyttäminen ja
uudelleen lämmittäminen.
IT: kansion pakkaaminen kerran zipiksi ja siirtäminen on tehokkaampaa kuin 500 tiedoston
siirtäminen yksitellen.
Toistettavuus. Kuinka luotettavasti ratkaisu tuottaa saman tuloksen toisella, kolmannella ja
kymmenennellä kerralla samalla syötteellä. Toistettava ratkaisu ei riipu suorittajan mielialasta,
muistista tai arvailusta.
Arki: resepti, jossa käytetään aina 200 ml vettä ja yhtä pussia, on toistettavampi kuin “vähän
vettä, maista ja lisää tarvittaessa”.
IT: tallennetulta tarkistuslistalta ajettava varmuuskopio on toistettavampi kuin ratkaisu, jossa
pitää muistaa, missä kansio kulloinkin sijaitsee.
Virhealttius. Kuinka helppoa on tehdä väärä asia ratkaisua noudattaessa. Matala virhealttius
tarkoittaa, että helppoja virheitä on vähän; korkea virhealttius tarkoittaa, että pienikin
lipsahdus vie helposti väärään lopputulokseen.
Arki: “kaada kiehuva vesi pussin päälle ja anna hautua kolme minuuttia” on vähemmän
virhealtis kuin “kaada vesi ja laske vähän aikaa”.
IT: varmuuskopio, jonka tiedostonimessä on päivämäärä, on vähemmän virhealtis kuin
varmuuskopio, joka tallentaa kaiken aina samaan -tiedostoon. `backup.zip`
Huomio sanoista: joissakin oppikirjoissa selkeyttä kutsutaan luettavuudeksi ja matalaa
virhealttiutta robustiudeksi. Tällä kurssilla käytetään yllä olevia neljää nimeä juuri tässä
järjestyksessä ensimmäisellä maininnalla.

### Neljän kriteerin soveltaminen teerespteihin

Palataan oppitunnin 10 teeresepteihin, nyt kriteerien läpi katsottuna.
Kriteeri Resepti A (keitä ensin) Resepti B (hauduta ensin)
Selkeys Vaihe 5 nimeää luvun (3 Vaihe 5 nimeää värin, jonka
minuuttia). Kirjaimellinen suorittajan täytyy osata
suorittaja lopettaa oikeaan arvioida. Uusi suorittaja voi
aikaan. lopettaa liian aikaisin tai
liian myöhään.
Tehokkuus Viisi vaihetta, yksi keitto, Viisi vaihetta, yksi keitto,
yksi haudutus — ei turhia yksi haudutus — ei turhia
vaiheita. vaiheita.
Toistettavuus Sama 200 ml ja sama 3 Sama vedenkeitin, mutta
minuuttia → sama juoma väriarvio muuttuu päivän
maanantaina ja perjantaina. mukaan → juoma vaihtelee.
Virhealttius Vaikea mennä pieleen, jos Riski ottaa pussi pois liian
suorittajalla on kello. aikaisin tai liian myöhään,
jos suorittaja on uusi teen
tekijä.
Lue taulukkoa solu kerrallaan. Resepti A on selkeämpi vaiheessa 5, koska 3 minuuttia kertoo
täsmälleen, milloin pitää lopettaa. Reseptit ovat yhtä tehokkaita — sama määrä vaiheita.
Resepti A on toistettavampi, koska kello toimii samalla tavalla maanantaina ja perjantaina,
mutta värin arviointi ei. Resepti A on myös vähemmän virhealtis uudelle suorittajalle;
kokeneelle teenjuojalle ero pienenee.
Huomaa, mitä taulukko ei tee. Se ei anna resepti A:lle arvosanaa 4/5. Se ei julista
kokonaisvoittajaa. Se käy yhden kriteerin kerrallaan, sanoo yhden konkreettisen asian per solu
ja pysähtyy siihen.

### Neljän kriteerin soveltaminen varmuuskopiointimenetelmiin

Nyt IT-peili. Kaksi varmuuskopiointitapaa, neljä kriteeriä.
Menetelmä B (zip +
Kriteeri Menetelmä A (USB-kopio) sähköposti itselle)
Selkeys Jokainen vaihe nimeää Jokainen vaihe nimeää
konkreettisen konkreettisen
käyttöliittymätoiminnon käyttöliittymätoiminnon
Menetelmä B (zip +
Kriteeri Menetelmä A (USB-kopio) sähköposti itselle)
(kytke, valitse kaikki, paina (hiiren oikea, Pakkaa .zipiksi,
Ctrl+V, irrota). liitä, lähetä itselle).
Tehokkuus Monet tiedostot kopioidaan Yksi zip-tiedosto luodaan ja
yksitellen — hidas kansiolle, siirretään kerran —
jossa on paljon pieniä vähemmän turhia siirtoja.
tiedostoja.
Toistettavuus Jos USB-muisti ei ole Sähköpostipalvelin on
mukana, prosessi pysähtyy; käytettävissä koulussa aina;
lopputulos riippuu sama prosessi toimii millä
muistamisesta. tahansa kannettavalla.
Virhealttius Vanhan varmuuskopion Jokainen sähköposti
ylikirjoittaminen on helppoa, päiväytyy automaattisesti —
jos kohdekansiota ei nimetä vanha varmuuskopio katoaa
uudelleen. vahingossa harvemmin.
Lue riveittäin, ei sarakkeittain. Menetelmät ovat suunnilleen yhtä selkeitä — molemmat
nimeävät konkreettiset toiminnot. Menetelmä B on tehokkaampi kansiolla, jossa on paljon
pieniä tiedostoja. Menetelmä B on toistettavampi eri laitteilla, koska sähköpostipalvelin on
aina käytettävissä, mutta USB-laite ei välttämättä ole. Menetelmä B on myös vähemmän
virhealtis aiempien varmuuskopioiden säilyttämisessä, koska sähköposti ei ylikirjoita edellistä
tiedostoa samalla tavalla.
Tämä on yksi vertailu yhdelle syötteelle. Jos kansio sisältäisi 50 GB videotiedostoja, kuva voisi
muuttua — zip-vaihe hidastuisi ja sähköposti ei ehkä hyväksyisi liitettä. Vertailu riippuu

syötteestä.

### Vaihtokaupat — kun kriteerit vetävät eri suuntiin

Vaihtokauppa tarkoittaa tilannetta, jossa kaksi kriteeriä vetää eri suuntiin niin, että yhden
parantaminen vie jotakin toisesta. Resepti B on vähemmän selkeä vaiheessa 5, mutta yhtä
tehokas kuin resepti A ja saattaa olla kokeneelle teenjuojalle miellyttävämpi. Menetelmä A on
helpompi selittää ensimmäisenä päivänä (USB on konkreettinen esine, jonka voi pitää
kädessä), mutta menetelmä B on tehokkaampi ja toistettavampi päivittäisessä käytössä.
Vaihtokauppa ei ole ongelma, joka pitäisi ratkaista pois. Se on vertailun muoto. Yleisin virhe on
julistaa silti voittaja. Vastusta tätä. Nimeä vaihtokauppa.
Esimerkiksi:
“Resepti A on selkeämpi. Resepti B voi olla nopeampi kokeneelle tekijälle. Oikea valinta riippuu
siitä, onko suorittaja tehnyt tämän ennen.”
Tuo lause on analyysi. Yhden ratkaisun ei tarvitse voittaa kaikissa kriteereissä. Neljä kriteeriä
ovat kuvailevia linssejä, eivät tulostaulukko.
Pysähdy hetkeksi: Valitse oppitunnin 10 kaksi vaihtoehtoista ohjetta, jotka kirjoitit.
Tee nelirivinen taulukko — yksi rivi per kriteeri. Kirjoita kuhunkin soluun yksi lyhyt
lause ja nimeä mahdollisuuksien mukaan tarkka vaihe. Sinun ei tarvitse valita
voittajaa. Huomaa, mitkä kriteerit vetävät vastakkaisiin suuntiin.
Pysähdy hetkeksi: Mieti ohjelmistoa, jota käytät lähes päivittäin — chat-sovellus,
suoratoistopalvelu tai koulun portaali. Valitse yksi ominaisuus, jolla on kaksi
käyttötapaa (haku kirjoittamalla vs. kategorian klikkaaminen; pikanäppäin
vs. valikko). Kumpi tapa on selkeämpi uudelle käyttäjälle? Kumpi on tehokkaampi
päivittäiselle käyttäjälle? Mistä kriteeristä sovelluksen kehittäjä todennäköisesti
välittää eniten?
