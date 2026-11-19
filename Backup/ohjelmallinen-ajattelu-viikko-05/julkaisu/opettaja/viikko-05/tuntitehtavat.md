# Viikko 5 — Tuntitehtävät

## Yleiskatsaus

Tämä tiedosto sisältää **opettajavetoiset, luokassa pidettävät** aktiviteetit viikolle 5. Ne tehdään tunnilla, ei kotitehtävänä. Viikon tehtävä on tehdä kolmen rakennuspalikan — *sekvenssi, ehto, toisto* — tunnistaminen helpoksi todellisesta kielestä, jotta opiskelijat voivat tuottaa AT2-syöttötuotoksen.

- **Aktiviteetti A — "Etsi if / Etsi silmukka"** on **PAKOLLINEN**. Kaksi puolikasta: *Etsi if* oppitunnilla 14 (60–80 min slot, ~23 min); *Etsi silmukka* oppitunnilla 15 (58–80 min slot, ~22 min).
- **Aktiviteetti B — "Live-päätöspuu taululle"** on **VALINNAINEN** mutta suositeltava oppitunnille 14.

Molemmat vaativat live-vuorovaikutusta luokassa — äänestyksiä, taululle kirjoittamista, uudelleenkirjoituksia kaikkien edessä. Niitä ei voi korvata kotitehtävällä tai LLM:llä.

---

## Aktiviteetti A — "Etsi if / Etsi silmukka" 🟢 PAKOLLINEN

**Tavoite.** Opiskelijat eivät pysty suorittamaan AT2-syöttötehtävää itsevarmasti, ellei heillä ole kykyä tunnistaa kolmea rakennuspalikkaa kielestä, jota he eivät ole itse kirjoittaneet. Tämä peli tekee tunnistamisesta nopeaa, julkista ja diagnostista.

**Ryhmäkoko.** Koko luokka. **Tarvittava aika.** Kaksi puolikasta 22–23 min: *Etsi if* oppitunnilla 14, *Etsi silmukka* oppitunnilla 15. Kumpikin puolikas voi ajaa yksin; *Etsi if* -puolikas on AT2:n kannalta diagnostisempi.

**Opettajan valmistautuminen.** Valmista alla olevat kaksi pinoa (paperilappuja tai tulostettu lista). Kaksi saraketta taulutilaa — yksi kanonisille `if … then … else …` -uudelleenkirjoituksille, toinen `for each / repeat until / while` -uudelleenkirjoituksille.

### Pino 1 — Ehdot (luetaan oppitunnilla 14)

Lue jokainen lappu ääneen. Luokka äänestää: *ehto* tai *ei ehtoa*. Jos ehto, luokka nimeää testin.

1. *"Jos salasana on lyhyempi kuin 8 merkkiä, hylkää se."* — **ehto** (testi: *pituus < 8*).
2. *"Keitä vesi."* — **ei ehtoa**.
3. *"Jos sataa, mene bussilla; muuten kävele."* — **ehto** (testi: *sataako nyt?*).
4. *"Kaada 30 ml maitoa mukiin."* — **ei ehtoa**.
5. *"Jos käyttäjä ei ole kirjautunut sisään 90 päivään, deaktivoi tili."* — **ehto** (testi: *viimeinen kirjautuminen > 90 päivää?*).
6. *"Lisää teelusikallinen sokeria."* — **ei ehtoa**.
7. *"Jos saat läksyt valmiiksi ennen päivällistä, voit pelata."* — **ehto**.
8. *"Kytke keitin päälle."* — **ei ehtoa**.
9. *"Jos tiketissä mainitaan tulostin, lähetä se Hardware-tiimille; muuten lähetä se General Supportille."* — **ehto** (oletushaara).
10. *"Jos maito haisee, heitä se pois."* — **ehto** (yksihaarainen, ei else).

### Pino 2 — Toistot (luetaan oppitunnilla 15)

Lue jokainen lappu ääneen. Luokka äänestää: *toisto* tai *ei toistoa*. Jos toisto, luokka nimeää **lopetusehdon**.

1. *"Jokaiselle nimelle luettelossa, merkitse läsnä tai poissa."* — **toisto** (lopetus: luettelon loppu).
2. *"Tee kuppi teetä."* — **ei toistoa** (sekvenssi).
3. *"Niin kauan kuin keitin on vielä kuuma, älä keitä sitä uudelleen."* — **tahallinen ansa**: *while* suomessa ei aina tarkoita silmukkaa. Pohdinta taululle.
4. *"Toista, kunnes sähköposti on tyhjä."* — **toisto** (lopetus: *sähköposti tyhjä*).
5. *"Paina nappia kerran."* — **ei toistoa**.
6. *"Jokaiselle valokuvalle puhelimella, päätä pitäisikö se poistaa."* — **toisto**.
7. *"Päivitä sivua, kunnes paikka on vapaa."* — **toisto** (huomioi karannut tapaus).
8. *"Avaa ulko-ovi."* — **ei toistoa**.
9. *"Niin kauan kuin juna ei ole saapunut, tarkista laiturin tulostaulua."* — **toisto** (merkitse karannut tapaus).
10. *"Jokaiselle taulukon riville, tarkista että päivämääräsarake ei ole tyhjä."* — **toisto**.

### Vaihe vaiheelta fasilitointi

1. **Aseta säännöt (2 min).** *"Luen lyhyen lauseen. Te äänestätte: ehto / ei ehtoa (O14) tai toisto / ei toistoa (O15). Jos se on ehto, nimetkää **testi**. Jos se on toisto, nimetkää **lopetusehto**."*
2. **Lue jokainen lappu, ota äänestys, nimeä testi tai lopetus, kirjoita kanoninen muoto taululle.** ~90 sekuntia per lappu.
3. **Pohdi rajatapauksia (1–2 min kukin).** Erimielisyys on opetus.
4. **Päätös (2 min).** *"Mikä lappu oli vaikein luokitella, ja miksi?"* Yhdistä AT2:een: *"AT2-prosessikuvauksessanne jokaisen ehdon ja toiston on oltava niin näkyvissä, että tuntematon voisi äänestää siitä kuten juuri teimme."*

### Pohdintakysymyksiä

- Oliko lappua, jossa **testi oli piilotettu** arkiseen ilmaukseen?
- Oliko toistoa, jonka **lopetus oli havaitsemattomissa**?
- Osoittautuiko jokin *while*-lause **ei oikeaksi** silmukaksi?

**Miksi tämä vaatii luokan.** Julkinen äänestys ja live-uudelleenkirjoitus opettaa taidon, jota työpaperi ei pysty. Opiskelijat oppivat näkemään rakenteen kielessä, jota he eivät ole itse kirjoittaneet — juuri sitä AT2 pyytää.

**Ristiviittaus.** Nimetty kohdassa `## Oppitunti 14 — 90-minuutin suunnitelma` (60–80 min) ja `## Oppitunti 15 — 90-minuutin suunnitelma` (58–80 min) tiedostossa `opettajan-materiaalit.md`.

---

## Aktiviteetti B — "Live-päätöspuu taululle" 🟣 VALINNAINEN

**Tavoite.** Käy yksi päätöspuu rauhassa läpi, päästä päähän, luokan edessä — opiskelijat näkevät *rehellisiä testejä* ja *nimettyjä haaroja* ennen kuin piirtävät omat.

**Tarvittava aika.** 20 min. Mahtuu oppitunnin 14 slottiin 30–55 min vaihtoehtona osalle luennosta.

**Opettajan valmistautuminen.** Valitse yksi sääntö, jonka koko luokka tuntee (koulun myöhästymispolitiikka; *"pitäisikö ottaa sateenvarjo tänään?"*). Pidä ICT-peilikuva takataskussa (esim. *"pitäisikö tämä kirjautumisyritys estää?"*). Jos toimitat `kalvot-o14-paatospuut.md`, tämä aktiviteetti on sen pari.

### Vaihe vaiheelta fasilitointi

1. **Kirjoita sääntö taululle (2 min).** Lue se ääneen.
2. **Tunnista juurikysymys (3 min).** *"Mikä on ensimmäinen testi, jonka tulkitsija ajaa?"* Kirjoita se huipulle.
3. **Haarauta (3 min).** *"Mitkä ovat mahdolliset vastaukset?"* Piirrä viivat.
4. **Testi jokaisessa haarassa (5 min).** *"Mitä tapahtuu lehdessä, vai odottaako siellä toinen testi?"*
5. **Tunnista huono testi (4 min).** *"Pystyisikö sananmukainen tulkitsija oikeasti tarkistamaan tämän testin?"* Paina epämääräisiä haaroja — *"olenko myöhässä?"* ei ole rehellinen ennen kuin siitä tulee *"onko aika yli 8:15?"*. **Kirjoita uudelleen taululle.**
6. **Yhdistä AT2:een (2 min).** *"Jokaisen AT2-tuotoksenne ehdon takana on tällainen puu piilossa."*
7. **Valinnainen — ICT-peilikuva (1 min).** Jos lisäkalvosarja on näytöllä, osoita login-estoesimerkkiä: *"Sama muoto, eri ympäristö."*

### Pohdintakysymyksiä

- Olivatko luokassa kaikki samaa mieltä juurikysymyksestä?
- Oliko haaraa, jossa testi oli epämääräinen? Miten uudelleenkirjoitus muutti merkitystä?

**Miksi VALINNAINEN.** Päällekkäinen Aktiviteetti A:n kanssa. Jos sinulla on aikaa vain yhdelle, aja Aktiviteetti A — se kattaa sekä ehdot että toistot ja on diagnostisempi.

**Ristiviittaus.** Nimetty kohdassa `## Oppitunti 14 — 90-minuutin suunnitelma` (30–55 min slot) tiedostossa `opettajan-materiaalit.md`.

---

## Miten nämä aktiviteetit kytkeytyvät tiedostoon `opettajan-materiaalit.md`

- **Aktiviteetti A (PAKOLLINEN)** — O14-suunnitelma, 60–80 min (*Etsi if*); O15-suunnitelma, 58–80 min (*Etsi silmukka*).
- **Aktiviteetti B (VALINNAINEN)** — O14-suunnitelma, 30–55 min.

Jos opettajan on pakko jättää yksi pois, jätä Aktiviteetti B pois. Aktiviteetti A on viikon kalibrointihetki.
