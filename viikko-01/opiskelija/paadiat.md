# Viikko 1 — Tietokoneelle puhuminen

---

## Viikko 1 - Miten puhun tietokoneelle

Ohjelmallinen ajattelu
Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi
Lisätty pedagoginen tuki on merkitty sanoilla Vinkki, Esimerkki, Ajattele näin tai Tee näin.
KESKEINEN KYSYMYS
Miten puhun tietokoneelle niin, että se ymmärtää,
mitä haluan sen tekevän? ---

## Mitä tällä viikolla harjoitellaan

• Oppitunti 1 - tietokone tulkitsee ohjeet kirjaimellisesti
• Oppitunti 2 - algoritmi on arkinen nimi selkeille vaiheittaisille ohjeille
• Oppitunti 3 - täsmällinen vai epätarkka: etsitään monitulkintaisuutta ja testataan ohjeita

### Ajattele näin: tällä viikolla et vielä "koodaa", vaan opettelet antamaan ohjeita niin tarkasti, että

koodi voi myöhemmin syntyä niistä. ---

## Mitä ohjelmallinen ajattelu tarkoittaa?

Ohjelmallinen ajattelu tarkoittaa tapaa pilkkoa tehtävä pieniin, selkeisiin ja oikeassa
järjestyksessä oleviin vaiheisiin, jotka kirjaimellinen suorittaja voi tehdä arvaamatta mitään.
Se on ohjelmoinnin taustalla oleva ajattelutapa - ei vielä itse ohjelmointia.

### Esimerkki: ennen kuin kirjoitat ohjelman, sinun täytyy ymmärtää, mitä ohjelman pitää tehdä

vaihe vaiheelta. ---

## Tietokone ottaa ohjeesi kirjaimellisesti

Pyydät kahdeksanvuotiasta serkkuasi: "Tee minulle voileipä."
Hän antaa sinulle yhden leipäviipaleen.
Hän ei ole ymmällään. Sinä et vain antanut hänelle tarpeeksi tietoa.

### Ajattele näin: tietokone toimii usein vielä serkkuakin kirjaimellisemmin. Se ei täytä puuttuvia

kohtia mielessään. ---

## "Tee voileipä" - mikä voi mennä pieleen?

• Mikä leipä?
• Kuinka monta viipaletta?
• Mitä laitetaan väliin?
• Leikataanko puoliksi vai ei?
• Onko yksi leipäviipale voileipä?
• Kirjaimellisen suorittajan täytyy päättää jokainen näistä, jos ohje ei kerro vastausta.

### Vinkki: kun ohjeessa on kohta, jonka joku voisi ymmärtää kahdella tavalla, ohjetta pitää

tarkentaa. ---

## Monitulkintaisuus on ohjeessa, ei tietokoneessa

Tietokone on kirjaimellinen. Se tekee täsmälleen sen, mitä on kirjoitettu.
Kun jokin menee rikki, ensimmäinen kysymys ei ole: "Mikä tässä koneessa on vialla?"
Parempi kysymys on: "Missä minä olin epäselvä?"

### Ajattele näin: bugi ei aina tarkoita, että tietokone teki väärin. Se voi tarkoittaa, että ohje oli

puutteellinen. ---

## Algoritmi - nimi asialle, jota jo teet

Algoritmi on selkeä, kirjaimellisesti seurattava vaiheiden sarja, joka vie tunnetusta syötteestä
tunnettuun lopputulokseen.
Resepti on algoritmi. Koulumatka on algoritmi. Aamurutiinisi on algoritmi.

### Esimerkki: "avaa selain → kirjoita osoite → paina Enter" on pieni algoritmi. ---

## Algoritmin osat

• Tavoite - mitä yrität saada aikaan lopuksi
• Syöte - mistä aloitat
• Vaiheet - toiminnot oikeassa järjestyksessä
• Tuloste - mitä lopussa oikeasti syntyy

### Vinkki: jos jokin näistä puuttuu, algoritmia on vaikea testata. ---

## Kaksi algoritmia, yksi tavoite

Reitti A: kävele Park Streetille, nouse bussiin 12, jää pois Market-pysäkillä ja kävele kaksi
korttelia itään.
Reitti B: kävele viisitoista minuuttia raitiovaunupysäkille, nouse raitiovaunuun 4 ja jää pois
School Squarella.
Sama tavoite. Molemmat ovat oikein. Kaksi kelvollista algoritmia.

### Huomaa: ohjelmoinnissa sama ongelma voidaan usein ratkaista monella tavalla. ---

## Täsmällinen vs. epätarkka ohje

Epätarkka: "Tallenna tiedosto tavalliseen paikkaan."
Täsmällinen: "Tallenna `report-may.docx` jaetun aseman kansioon `Team/Reports/2026/May`."
Pituus ei ole tärkein asia. Tärkeää on se, kuinka monta arvausta suorittajalle jää.

### Vinkki: hyvä ohje ei ole välttämättä pitkä - se on sellainen, ettei sitä tarvitse arvata. ---

## Monitulkintaisuuden metsästys - neljä mallia

• Epämääräiset substantiivit - *tiedosto, juttu, sähköposti*
• Viittaavat sanat - *täällä, siellä, se, hän*
• Suhteellinen aika - *myöhemmin, pian, lounaan jälkeen*
• Epämääräiset määrät - *vähän, jonkin verran, muutama*
• Kun huomaat jonkin näistä, kysy: voisiko kirjaimellinen suorittaja tehdä tämän useammalla
kuin yhdellä tavalla?

### Tee näin: ympyröi ensin epäselvä sana, kirjoita sen viereen tarkempi vaihtoehto. ---

## Testaaminen kirjaimellisena robottina

Kirjoitit ohjeen. Tiedät, mitä tarkoitit.
Kun luet ohjeen uudelleen, luet helposti sen, mitä tarkoitit - et sitä, mitä oikeasti kirjoitit.
Ainoa korjaus: anna ohje oikealle suorittajalle tai seuraa sitä itse niin kuin et muistaisi, mitä
tarkoitit.

### Vinkki: testaa ohje sanasta sanaan. Älä tee mitään sellaista, mitä ohje ei suoraan käske. ---

## Reunatapaukset (kevyt aloitus)

"Avaa jääkaappi ja ota maito."
Mitä jos maitoa ei ole? Mitä jos maitoja on kaksi? Mitä jos toinen on vanhentunut?
Ohje toimii tavallisessa tilanteessa. Se ei kerro, mitä tehdään muissa tilanteissa.
Esimerkki IT-alalta: "avaa tiedosto" toimii, jos tiedosto on olemassa. Reunatapaus on: mitä jos
tiedosto puuttuu tai sinulla ei ole oikeuksia avata sitä? ---

## Viikon 1 sanasto yhdellä silmäyksellä

• ohjelmallinen ajattelu, ohje, tietokone kirjaimellisena suorittajana
• algoritmi, tavoite, syöte, vaihe, tuloste
• kirjaimellinen tulkinta, monitulkintaisuus, täsmällisyys
• epätarkka ohje, reunatapaus, ohjeen testaaminen

### Vinkki: opettele termit esimerkin avulla. Esimerkiksi "syöte" = se, mitä annetaan alussa. ---

## Vähimmäistaso vs. syventäminen

• Vähimmäistaso
• Määrittele viisi ydintermiä.
• Kirjoita lyhyt arkinen algoritmi.
• Etsi ja korjaa yksi monitulkintainen sana.
• Syventäminen
• Anna ohjeesi oikealle suorittajalle.
• Ammatillinen näkökulma: help desk -ohje.
• Sparraa LLM:n eli kielimallin kanssa käyttäen rakennettua promptia.
• Huomaa ja kuvaa yksi reunatapaus. ---

## Tämän viikon tehtävät

• Tehtävä 1.1 - Kirjaimellinen robotti -peli (PAKOLLINEN)
• Tehtävä 1.2 - Etsi monitulkintaisuus (SYVENTÄVÄ)
• Tehtävä 1.3 - Kaksi algoritmia, yksi tavoite (SYVENTÄVÄ)
• Tehtävä 1.4 - Ammatillinen näkökulma: help desk -ohje (SYVENTÄVÄ)
• Säilytä muistiinpanosi - niitä käytetään AT1-tehtävässä viikon 2 lopussa.

### Tee näin: kirjoita jokaisesta tehtävästä ainakin yksi havainto: "mikä oli epäselvää" ja "miten

tarkensin sen". ---

## Seuraavaksi: Viikko 2 - pilkkominen

Kun tehtävä on liian iso yhdelle algoritmille, pilkot sen pienemmiksi osiksi.
Kirjaimellisen suorittajan ajattelutapa pysyy samana. Ohjeista tulee vain pidempiä.

### Ajattele näin: iso IT-tehtävä, kuten "ota uusi käyttäjä käyttöön", koostuu monesta

pienemmästä tehtävästä. KESKEINEN KYSYMYS
Miten puhun tietokoneelle niin, että se ymmärtää,
mitä haluan sen tekevän?
