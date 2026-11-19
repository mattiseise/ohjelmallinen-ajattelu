# Viikko 3 — Prosessin piirtäminen

Ohjelmallinen ajattelu

1. vuoden ammatillinen ICT-kurssi

---

## Mihin viikko 2 päättyi

- Osaat pilkkoa ongelman päätehtäväksi, osatehtäviksi ja osatavoitteiksi
- AT1 palautettiin tämän viikon alussa
- Tämä viikko kysyy: miten kirjoitan prosessin niin, että joku muu voi suorittaa sen?

---

## Viikon 3 keskeinen viesti

> *"Kun osaat pilkkoa ongelman, seuraava taito on kuvata prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa."*

---

## Mitä tämä viikko harjoittaa

- Oppitunti 7 — yksinkertainen vuokaavio, kurssin ensimmäinen kuva
- Oppitunti 8 — abstraktio: valitseminen, mitä jätetään pois
- Oppitunti 9 — uudelleenkäytettävät ohjeet: funktion idea ilman koodia

---

## Kun lista ei riitä

Aamurutiini toimii tasaisena listana — herätyskello, peseytyminen, pukeutuminen, syöminen, lähtö.

Sillä hetkellä kun ilmaantuu kyllä/ei-kysymys (*"sataako?"*), lista hajoaa.

Vuokaavio on se, miksi lista muuttuu, kun prosessissa on haara.

---

## Neljä muotoa

- **Soikio** — alku / loppu
- **Suorakulmio** — yksi vaihe (toiminto)
- **Vinoneliö** — yksi kyllä/ei-päätös, kaksi lähtevää nuolta
- **Nuoli** — virtaus yhdestä muodosta seuraavaan

Neljä muotoa. Siinä on kuvan koko sanasto.

---

## Vuokaavio "otanko sateenvarjon?"

```
( Alku ) -> [ Tarkista sääennuste ]
   -> < Onko sadetodennäköisyys > 50 % ? >
        Kyllä -> [ Ota sateenvarjo ]
        Ei    -> [ Jätä sateenvarjo ovelle ]
   -> ( Lähde kotoa )
```

Kahdeksan muotoa. Yksi Alku, yksi Loppu, kolme suorakulmiota, yksi vinoneliö, nuolia joka puolella.

---

## ICT-esimerkki — help desk -triage

- *Lue tiketti*
- *Pääseekö käyttäjä nyt kirjautumaan?*
  - Kyllä → sulje tiketti
  - Ei → pyydä käyttäjältä kuvakaappaus

Yksi vinoneliö, kaksi polkua, kaksi eri Loppu-soikiota.

---

## Abstraktio — piilota yksityiskohta, jolla ei ole merkitystä

Abstraktio on **valitsemista, mitä jätetään pois, jotta kuvaus sopii yleisölle**.

Ei epämääräisyyttä — piirtämäsi laatikot pysyvät täsmällisinä.

Ei filosofiaa — bussipysäkki, Kirjaudu sisään -painike, tiedostonimi.

---

## Bussipysäkki on abstraktio

- **Matkustaja** — kyltti, jossa lukee "Puistokatu", ja aikataulu
- **Lähetin** — GPS-koordinaatti, ID-numero, lista busseista
- **Insinööri** — kytkentärasia, virtakaapeli, ruuveja

Sama fyysinen asia. Kolme abstraktiota. Kolme oikeaa vastausta.

---

## "Kirjaudu sisään" -painike on abstraktio

Sen sisälle piilotettuna:

- tunnistuspalvelin
- salasanan tarkistus (salattua tallennetta vasten)
- istuntoeväste
- OAuth-tanssi (jos kirjautuminen menee Microsoftin tai Googlen kautta)

Painike on oikea kuvaus *käyttäjälle*.

---

## Tarkkuustaso seuraa yleisöä

- **Uusi help desk -työntekijä, ensimmäinen päivä** — kuusi suorakulmiota ennen vinoneliötä
- **Vanhempi ICT-järjestelmänvalvoja, kymmenen vuotta talossa** — yksi suorakulmio ennen vinoneliötä

Sama prosessi. Sama tavoite. Eri yleisö. Eri tarkkuustaso.

Molemmat vuokaaviot ovat oikein.

---

## Uudelleenkäytettävät ohjeet — anna osalle nimi

Kaksi vuokaaviota. Molemmissa on *Avaa portaali → kirjoita käyttäjätunnus → kirjoita salasana → paina Kirjaudu sisään → odota aloitussivua*.

Viisi suorakulmiota, kahdesti.

Tai: yksi nimetty lohko — *"kirjaa käyttäjä sisään"*.

---

## Funktio (viikon 3 merkitys)

- **Nimetty** — lyhyt verbi-ilmaisu
- **Uudelleenkäytettävä** — esiintyy monissa prosesseissa
- **Selkeällä suomella oleva kuvaus** — yksi lyhyt kappale
- **Syöte** — mitä se tarvitsee alkuun
- **Tuloste** — mitä se tuottaa valmiina

Ei vielä koodia. Vain nimetty laatikko ja kappale.

---

## Ammatillinen esimerkki — "rekisteröi uusi laite"

Käytetään joka kerta, kun uusi läppäri, projektori tai kokoushuoneen näyttö saapuu.

Kymmenen laatikon vuokaavio *"perusta uusi kokoushuone"* muuttuu seitsemän laatikon vuokaavioksi, kun *"rekisteröi uusi laite"* on yksi nimetty laatikko.

Viisi piilotettua vaihetta ovat edelleen olemassa — arkistoituna koulun ICT-käsikirjassa.

---

## Viikon 3 sanasto silmäyksellä

- *prosessi, vuokaavio, alku/loppu, vaihe, päätös, nuoli, haara, Kyllä/Ei-polku*
- *abstraktio, tarkkuustaso, piilotettu yksityiskohta, yleisö*
- *uudelleenkäytettävä lohko, nimetty lohko / funktio (viikon 3 merkitys)*
- *vaihtokauppa; ehto* (eteenpäin katsoen — viikko 5)

---

## Must-do-minimi vs. syventävä

**Must-do-minimi**
- Määrittele ydintermit
- Lue pieni vuokaavio ja kuvaa, mitä se tekee
- Piirrä pieni vuokaavio omasta elämästäsi, jossa on päätös
- Nimeä kaksi piilotettua yksityiskohtaa yhden abstraktion sisältä
- Tunnista yksi uudelleenkäytetty osa ja nimeä se

**Syventävä**
- Kirjoita yksi vaihe uudelleen matalammalla tarkkuustasolla
- Etsi kolme uudelleenkäytettävää lohkoa kahdesta prosessista
- LLM-sparrauskumppani abstraktiovalinnoissa

---

## Tämän viikon tehtävät

- Tehtävä 3.1 — Piirrä ensimmäinen vuokaaviosi (PAKOLLINEN)
- Tehtävä 3.3 — Mitä on piilotettu Kirjaudu sisään -painikkeen sisälle? (SYVENTÄVÄ)
- Tehtävä 3.4 — Tunnista uudelleenkäytetty osa (SYVENTÄVÄ)
- Tehtävä 3.5 — Kirjoita vaihe uudelleen matalammalla tarkkuustasolla (SYVENTÄVÄ)

Säilytä muistiinpanosi — ne syöttävät AT2:ta viikon 5 lopussa / viikon 6 aikana.

---

## Mitä seuraavaksi: viikko 4 — vaihtoehtoiset ratkaisut

Useampi kuin yksi pätevä vuokaavio voi päästä samaan tavoitteeseen.

Viikko 4 kysyy: miten vertailet kahta pätevää ratkaisua ja valitset?

Sama vuokaaviotaito; uusi kysymys päälle.

---

## Kertaus — keskeinen viesti vielä kerran

> *"Kun osaat pilkkoa ongelman, seuraava taito on kuvata prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa."*
