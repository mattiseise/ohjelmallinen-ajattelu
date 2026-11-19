# Viikko 5 — Tunnilla tehtävät ohjatut tehtävät

## Yleiskuva

Tämä tiedosto sisältää tunnilla tehtävät, opettajan ohjaamat aktiviteetit viikolle 5. Ne tehdään
tunnilla, eivät kotitehtävinä. Viikon tehtävä on tehdä kolme rakennuspalikkaa - järjestys, ehto ja toisto -
helposti tunnistettaviksi tavallisesta kielestä, jotta opiskelijat voivat tuottaa AT2:een valmistavan
tuotoksen.
• Tehtävä A - "Etsi ehto / Etsi silmukka" on PAKOLLINEN. Siinä on kaksi puoliskoa: Etsi ehto
oppitunnilla 14 (kohta 60-80 min, noin 23 min) ja Etsi silmukka oppitunnilla 15 (kohta 58-80 min,
noin 22 min).
• Tehtävä B - "Päätöspuu taululla livenä" on VALINNAINEN, mutta sitä suositellaan oppitunnille
14.
Molemmat vaativat luokkahuoneen vuorovaikutusta: äänestämistä, taululle kirjoittamista ja korjausten
tekemistä kaikkien nähden. Niitä ei voi korvata kotitehtävällä tai LLM:llä.
Vinkki: Tällä viikolla opiskelija oppii näkemään rakenteen tavallisen kielen alta. Älä aloita koodista.
Aloita lauseesta ja kysy: "Mikä on testi?" tai "Milloin tämä loppuu?"

## Tehtävä A - "Etsi ehto / Etsi silmukka" - PAKOLLINEN

Tavoite. Opiskelijat eivät pysty tekemään AT2:een valmistavaa tehtävää luottavaisesti, elleivät he
tunnista kolmea rakennuspalikkaa myös sellaisesta kielestä, jota he eivät itse kirjoittaneet. Tämä peli
tekee tunnistamisesta nopeaa, julkista ja diagnostista.
Ryhmäkoko. Koko luokka.
Tarvittava aika. Kaksi 22-23 minuutin puoliskoa: Etsi ehto oppitunnilla 14 ja Etsi silmukka oppitunnilla
15. Kumpikin puolisko voidaan toteuttaa myös yksinään. Etsi ehto on diagnostisesti tärkeämpi AT2:ta
varten.
Opettajan valmistelut. Valmistele alla olevat kaksi pinoa paperilappuina tai tulostettuna listana. Varaa
taululle kaksi saraketta: yksi kanonisille -uudelleenkirjoituksille ja yksi `if ... then ... else ... for`
-uudelleenkirjoituksille. `each / repeat until / while`

### Pino 1 - Ehdot (luetaan oppitunnilla 14)

Lue jokainen lappu ääneen. Luokka äänestää: ehto vai ei ehtoa. Jos kyseessä on ehto, luokka nimeää
testin.
1. "Jos salasana on alle 8 merkkiä pitkä, hylkää se." - ehto (testi: pituus < 8).
2. "Keitä vesi." - ei ehtoa.
3. "Jos sataa, mene bussilla; muuten kävele." - ehto (testi: sataako nyt?).
4. "Kaada 30 ml maitoa mukiin." - ei ehtoa.
5. "Jos käyttäjä ei ole kirjautunut sisään 90 päivään, poista tili käytöstä." - ehto (testi: viimeisestä
kirjautumisesta > 90 päivää?).
6. "Lisää teelusikallinen sokeria." - ei ehtoa.
7. "Jos saat läksyt valmiiksi ennen päivällistä, voit pelata." - ehto.
8. "Kytke vedenkeitin päälle." - ei ehtoa.
9. "Jos tukipyyntö mainitsee tulostimen, lähetä se Laitetukeen; muuten lähetä se Yleiseen tukeen." -
ehto (oletushaara).
10. "Jos maito haisee pilaantuneelta, heitä se pois." - ehto (yhden haaran ehto, ei else-haaraa).

### Pino 2 - Toistot (luetaan oppitunnilla 15)

Lue jokainen lappu ääneen. Luokka äänestää: toisto vai ei toistoa. Jos kyseessä on toisto, luokka
nimeää pysähtymisehdon.
14
Tunnilla tehtävät ohjatut tehtävät - sivu
1. "Merkitse jokaisen nimiluettelossa olevan nimen kohdalle läsnä tai poissa." - toisto (pysähtyy:
luettelon loppu).
2. "Tee kuppi teetä." - ei toistoa (järjestys eli sekvenssi).
3. "Kun vedenkeitin on vielä kuuma, älä keitä sitä uudelleen." - tarkoituksellinen ansa: sana
kun/while tavallisessa kielessä ei aina tarkoita silmukkaa. Pura taululla.
4. "Toista, kunnes saapuneet-kansio on tyhjä." - toisto (pysähtyy: saapuneet-kansio on tyhjä).
5. "Paina painiketta kerran." - ei toistoa.
6. "Päätä jokaisen puhelimessa olevan kuvan kohdalla, pitäisikö se poistaa." - toisto.
7. "Päivitä sivua, kunnes paikka on vapaa." - toisto (varo loputtoman odottamisen tapausta).
8. "Avaa ulko-ovi." - ei toistoa.
9. "Niin kauan kuin juna ei ole saapunut, tarkista laiturinäyttöä." - toisto (nosta esiin loputtoman
odottamisen mahdollisuus).
10. "Tarkista jokaisen taulukon rivin kohdalla, että päivämääräsarake ei ole tyhjä." - toisto.

### Vaiheittainen ohjaus

1. Aseta säännöt (2 min). Sano: "Luen lyhyen väitteen. Te äänestätte: ehto / ei ehtoa (L14) tai toisto /
ei toistoa (L15). Jos se on ehto, nimetkää testi. Jos se on toisto, nimetkää pysähtymisehto."
2. Lue jokainen lappu, ota äänestys, nimeä testi tai pysähtymisehto ja kirjoita kanoninen muoto
taululle. Noin 90 sekuntia per lappu.
3. Pura rajatapaukset (1-2 min per tapaus). Erimielisyys on oppimisen paikka.
4. Lopetus (2 min). Kysy: "Mikä lappu oli vaikein luokitella ja miksi?" Yhdistä AT2:een: "AT2:n
prosessikuvauksessa jokaisen ehdon ja toiston pitää olla niin näkyvä, että vieras ihminen voisi
äänestää siitä kuten me äsken."
Ajattele näin: Ehdossa etsitään kysymystä, johon voi vastata kyllä/ei tai valita haaran. Toistossa
etsitään sääntöä, jonka perusteella samaa asiaa tehdään monta kertaa, sekä pysähtymisehtoa, joka
kertoo milloin lopetetaan.

### Purkuun sopivia kysymyksiä

• Oliko lappu, jossa testi oli piilossa arkisen muotoilun sisällä?
• Oliko toisto, jonka pysähtymisehto ei ollut havaittavissa?
• Osoittautuiko jokin while/kun/niin kauan kuin -lause ei-oikeaksi silmukaksi?
Miksi tehtävä vaatii luokkahuoneen. Julkinen äänestys ja elävä uudelleenkirjoitus opettavat taidon,
jota pelkkä moniste ei opeta. Opiskelijat oppivat näkemään rakenteen kielestä, jota he eivät itse
kirjoittaneet - juuri sitä AT2 pyytää.
Viittaus. Nimetty tiedostossa kohdissa

```
teacher-materials.md ## Lesson 14 - 90-minute plan
```

(60-80 min) ja (58-80 min). `## Lesson 15 - 90-minute plan`

## Tehtävä B - "Päätöspuu taululla livenä" - VALINNAINEN

Tavoite. Käykää yksi päätöspuu hitaasti alusta loppuun koko luokan edessä. Opiskelijat näkevät
rehelliset testit ja nimetyt haarat ennen kuin he piirtävät omansa.
Tarvittava aika. 20 min. Sopii oppitunnin 14 kohtaan 30-55 min vaihtoehdoksi osalle luentoa.
Opettajan valmistelut. Valitse yksi sääntö, jonka luokka tuntee (koulun myöhästymiskäytäntö tai
"pitäisikö minun ottaa sateenvarjo tänään?"). Pidä takataskussa IT-peili, esimerkiksi "pitäisikö tämä
kirjautumisyritys estää?". Jos käytät pakettia , tämä tehtävä toimii `slides-l14-decision-trees.md`
sen parina.

### Vaiheittainen ohjaus

1. Kirjoita sääntö taululle (2 min). Lue se ääneen.
2. Tunnista juurikysymys (3 min). Kysy: "Mikä on ensimmäinen testi, jonka seuraaja tekee?" Kirjoita
se ylös ylimmäksi.
15
Tunnilla tehtävät ohjatut tehtävät - sivu
3. Haarautuminen (3 min). Kysy: "Mitkä ovat mahdolliset vastaukset?" Piirrä haarat.
4. Testi jokaisessa haarassa (5 min). Kysy: "Mitä tapahtuu lehdessä, vai odottaako siellä uusi testi?"
5. Huomaa huono testi (4 min). Kysy: "Voisiko kirjaimellinen seuraaja oikeasti tarkistaa tämän
testin?" Painota epämääräisiä haaroja. Esimerkiksi "myöhästynkö?" ei ole rehellinen testi, ennen
kuin se muuttuu muotoon "onko kello yli 8:15?". Kirjoita korjaus taululle.
6. Yhdistä AT2:een (2 min). Sano: "Jokaisen AT2-tuotoksen ehdon takana piilee tällainen
päätöspuu."
7. Valinnainen IT-peili (1 min). Jos lisädiapaketti on näytöllä, osoita kirjautumisen estämisen
esimerkkiä: "Sama muoto, eri tilanne."
Vinkki: "Rehellinen testi" tarkoittaa testiä, jonka seuraaja voi oikeasti tarkistaa ilman arvaamista.
Esimerkiksi "onko salasana vahva?" on epämääräinen; "onko salasana vähintään 12 merkkiä ja
sisältääkö se numeron?" on tarkistettava.

### Purkuun sopivia kysymyksiä

• Oliko luokka samaa mieltä juurikysymyksestä?
• Oliko haarassa epämääräinen testi? Miten korjaus muutti merkitystä?
Miksi valinnainen. Tehtävä menee osittain päällekkäin tehtävän A kanssa. Jos aikaa on vain yhteen,
tee tehtävä A: se kattaa sekä ehdot että toistot ja toimii paremmin diagnostisesti.
Viittaus. Nimetty tiedostossa kohdassa

```
teacher-materials.md ## Lesson 14 - 90-minute plan
```

(30-55 min).

## Miten nämä tehtävät liittyvät tiedostoon `teacher-materials.md`

• Tehtävä A (PAKOLLINEN) - oppitunnin 14 suunnitelma, 60-80 min (Etsi ehto); oppitunnin 15
suunnitelma, 58-80 min (Etsi silmukka).
• Tehtävä B (VALINNAINEN) - oppitunnin 14 suunnitelma, 30-55 min. Jos opettajan on jätettävä yksi
tehtävä pois, jätä tehtävä B. Tehtävä A on viikon kalibrointihetki.
16
Tunnilla tehtävät ohjatut tehtävät - sivu
