# Viikko 2 — Ongelman pilkkominen

---

## Viikko 2 - Ongelmien pilkkominen

Ohjelmallinen ajattelu
Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi

---

## Mitä käsittelimme viikolla 1

• Tietokone seuraa ohjeita kirjaimellisesti.
• Algoritmi on selkeä sarja kirjaimellisia vaiheita.
• Monitulkintaisuus on ohjeessa, ei suorittajassa.

### Vinkki: viikon 2 taito rakentuu viikon 1 päälle. Ensin tarvitaan selkeitä vaiheita, sitten isompi

tehtävä pilkotaan niiksi. ---

## Tämän viikon keskeinen viesti

> "Iso ongelma muuttuu hallittavaksi, kun nimeät päätehtävän, sen osatehtävät ja
järjestyksen, jossa niiden täytyy tapahtua."

### Ajattele näin: älä yritä ratkaista koko isoa tehtävää kerralla. Etsi ensin sen osat. ---

## Mitä pilkkominen tarkoittaa?

Pilkkominen eli dekomponointi tarkoittaa, että tehtävä on liian iso yhdeksi suoraksi
vaihelistaksi, joten jaat sen päätehtäväksi, jolla on tavoite, sekä pieneksi joukoksi osatehtäviä,
joilla jokaisella on oma osatavoite.
Se on suunnittelutaito. Vaiheet ovat yhä olemassa alla - ne ovat vain hallittavan kokoisia.

### Esimerkki: "aseta uusi työasema käyttöön" voi sisältää käyttäjätilin, ohjelmien asennuksen,

verkon testauksen ja ohjeistuksen. ---

## Päätehtävä, osatehtävät ja tavoite

• Päätehtävä - mitä olet tekemässä, yhtenä virkkeenä
• Tavoite - mikä on totta lopussa, yhtenä virkkeenä
• Osatehtävä - pienempi tehtävä päätehtävän alla
• Osatavoite - yhden osatehtävän tavoite, kapeampi kuin päätavoite

### Vinkki: hyvä osatehtävä alkaa usein verbillä: kerää, tarkista, luo, lähetä, testaa. ---

## Arkiesimerkki - aamiaisen tekeminen neljälle

• Päätehtävä: tee aamiainen neljälle klo 9.30 mennessä.
• *Päätä ruokalista.*
• *Tarkista jääkaappi.*
• *Valmista lämmin ruoka.*
• *Valmista kylmät ruoat.*
• *Valmista juomat.*
• *Kata pöytä.*
• *Kutsu kaikki pöytään.*

### Ajattele näin: jokainen kursivoitu kohta voisi olla oma pieni algoritminsa. ---

## IT-esimerkki - käyttäjätilin luominen

• Päätehtävä: luo uuden opiskelijan käyttäjätili koulun alustalle.
• *Kerää opiskelijan tiedot.*
• *Valitse käyttäjätunnus.*
• *Luo tili ylläpitotyökalussa.*
• *Lähetä vahvistus.*
• Neljä pientä osatehtävää, joilla jokaisella on oma osatavoite.

### Vinkki: osatavoite voisi olla esimerkiksi "opiskelijalla on toimiva käyttäjätunnus". ---

## Miksi tehtäviä kannattaa pilkkoa?

• Voit kirjoittaa jokaisesta osatehtävästä siistin pienen algoritmin.
• Voit antaa eri osatehtäviä eri ihmisille.
• Voit tarkistaa työn osatehtävä kerrallaan - tarkistuspisteinä.
Esimerkki IT-työssä: yksi henkilö voi luoda käyttäjätilin, toinen asentaa ohjelmat ja kolmas
testata kirjautumisen. ---

## Jotkin osatehtävät riippuvat toisista

Riippuvuus tarkoittaa yhteyttä, jossa yksi osatehtävä tarvitsee toisen osatehtävän tuloksen
ennen kuin se voi alkaa.
"Syö paahtoleipä" riippuu tehtävästä "paahda leipä".
Ilman paahtimen tulosta syömistehtävällä ei ole syötettä.
Ajattele näin IT:ssä: et voi lähettää käyttäjälle kirjautumisohjeita ennen kuin käyttäjätili on
luotu. ---

## Jotkin osatehtävät ovat riippumattomia

"Kata pöytä" ei riipu tehtävästä "valmista lämmin ruoka". Kumpi tahansa järjestys toimii.
Tällä kurssilla kutsumme tällaisia tehtäviä rinnakkaisiksi arkisessa merkityksessä: ne voisivat
tapahtua samaan aikaan.
Varsinaista samanaikaista suoritusta eli concurrency-käsitettä ei esitellä tällä viikolla.

### Vinkki: jos kaksi osatehtävää eivät tarvitse toistensa tulosta, ne ovat usein rinnakkaisia. ---

## Osatehtävien järjestäminen - syntymäpäiväjuhlat

Väärässä järjestyksessä: osta kakku, päätä päivämäärä, musiikki, vieraslista, lähetä kutsut,
siivoa, naposteltavat, koristele.
Perusteltu järjestys: päätä päivämäärä → vieraslista → lähetä kutsut → (kakku, naposteltavat,
siivous, koristelu ja musiikki sijoittuvat sinne, mihin ne sopivat).
Jotkin osatehtävät lukittuvat paikoilleen riippuvuuksien takia. Toiset ovat vapaampia.

### Tee näin: merkitse ensin tehtävät, jotka eivät voi alkaa ennen jotakin muuta. ---

## IT-esimerkki - tiedoston jakaminen

• *Etsi dokumentti.*
• *Tunnista luokan ryhmä.*
• *Aseta jakamisoikeudet.*
• *Kopioi jakolinkki* - riippuu käyttöoikeuksista.
• *Kirjoita sähköpostin viesti* - ei riipu linkistä.
• *Lähetä sähköposti* - riippuu sekä linkistä että viestistä.

### Vinkki: jos linkki kopioidaan ennen oikeuksien asettamista, vastaanottaja ei ehkä pääse

tiedostoon.

---

## Todellisen IT-tehtävän pilkkominen — oppitunnin 6 ennakko

> *"Ota uuden kollegan sähköpostitili käyttöön hänen uudella kannettavallaan ennen hänen klo 10.00 alkavaa työpäiväänsä."*

Päätehtävä, tavoite, 6 osatehtävää, 4 riippuvuutta ja yksi vapaa haara: kannettavan valmistelu voi kulkea rinnakkain tilin luomisen kanssa.

Ajattele näin: tässä tehtävässä aika on osa tavoitetta. Valmista pitää olla ennen klo 10.00.

---

## Kaksi kelvollista pilkkomista samasta tehtävästä

Toinen kollega voi pilkkoa saman tehtävän eri tavalla: hän voi yhdistää kaksi osatehtävää,
koska hänen työkalunsa tekee molemmat yhdellä napsautuksella, tai jakaa yhden tehtävän
kahdeksi, koska hänen koulussaan ne kuuluvat eri ihmisille.
Molemmat voivat olla kelvollisia. Viikko 4 palaa kysymykseen: "miten kahta kelvollista
ratkaisua vertaillaan".

### Huomaa: eri ratkaisu ei automaattisesti ole väärä. ---

## Viikon 2 sanasto yhdellä silmäyksellä

• *pilkkominen / dekomponointi*, *päätehtävä*, *osatehtävä*, *osatavoite*
• *tavoite* (kerrataan), *järjestys* (kerrataan)
• *riippuvuus*, *järjestys*, *edellytys*, *rinnakkainen*
• *ylätehtävä*, *hierarkia*
• *AT1*; *abstraktio* (ennakkoon - viikko 3)

### Vinkki: hierarkia tarkoittaa tässä "mikä kuuluu minkäkin alle". ---

## Tämän viikon tehtävät

• Tehtävä 2.1 - Pilko yksi tehtävä omasta viikostasi (PAKOLLINEN).
• Tehtävä 2.2 - Pilko parin kanssa ja testaa uudelleen (PAKOLLINEN).
• Tehtävä 2.3 - Järjestys ja riippuvuudet (SYVENTÄVÄ).
• Tehtävä 2.4 - Ammatillinen näkökulma: pilko oman koulun IT-tehtävä (SYVENTÄVÄ).
• Tehtävä 2.5 - Sparrauskumppani: haasta oma pilkkomisesi (SYVENTÄVÄ).

### Tee näin: kirjoita jokaisesta osatehtävästä myös osatavoite. Älä tyydy pelkkään tehtävälistaan. ---

## AT1 - ensimmäinen arvioitava tehtävä

• Palautetaan oppitunnin 6 lopussa.
• Tuo artefakti eli työn tuotos, jossa on:
• päätehtävä ja sen tavoite
• 4-8 osatehtävää osatavoitteineen
• järjestys, jossa vähintään yksi riippuvuus on nimetty selvästi
• 3-5 virkkeen reflektio
• Tämän viikon muistiinpanot ovat raaka-aineesi.

### Vinkki: artefakti voi olla esimerkiksi taulukko, kaavio tai selkeä tekstirakenne. ---

## Seuraavaksi: Viikko 3 - abstraktio ja vuokaaviot

Viikko 3 lisää abstraktion: piilotat yksityiskohdat, joita et juuri sillä hetkellä tarvitse.
Lisäksi käyttöön tulee prosessin ensimmäinen kuva: yksinkertainen vuokaavio (alku, loppu,
nuolet). Ei vielä koodia.

### Ajattele näin: vuokaavio näyttää, miten vaiheista kuljetaan eteenpäin. ---

## Kertaus - viikon keskeinen viesti vielä kerran

> "Iso ongelma muuttuu hallittavaksi, kun nimeät päätehtävän, sen osatehtävät ja
järjestyksen, jossa niiden täytyy tapahtua."
