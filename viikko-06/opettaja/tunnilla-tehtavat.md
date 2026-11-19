# Viikko 6 — Tunnilla tehtävät ohjatut tehtävät

## Yleiskuva

Tämä tiedosto sisältää tunnilla tehtävät, opettajan ohjaamat aktiviteetit viikolle 6. Ne tehdään
tunnilla, eivät kotitehtävinä, eikä niitä voi korvata LLM:llä tai monisteella.
• Tehtävä A - "Kuivaharjoitus koko luokan kanssa" on PAKOLLINEN. Se kuuluu oppitunnin 18
kohtaan 55-80 min ja toimii kehollisena diagnostiikkana AT2-valmiudelle. Koko luokasta tulee
seurantataulukko, yksi opiskelija per muuttuja, ja virhe nousee esiin kaikkien edessä.
• Tehtävä B - "Pseudokoodin vaihto ja jäljitys" on VALINNAINEN. Se sopii oppitunnin 16
parityökohtaan 60-80 min.
Vinkki: Käytä aluksi termiä kuivaharjoitus (dry run) ja sano heti, mitä se tarkoittaa: ohjelma käydään
läpi käsin rivi riviltä ilman, että sitä suoritetaan koneella. Näin opiskelija näkee, että kyse on taidosta, ei
uudesta ohjelmointikielestä.

## Tehtävä A - "Kuivaharjoitus koko luokan kanssa" - PAKOLLINEN

Tavoite. Luokka suorittaa kuivaharjoituksen yhdessä ja esittää seurantataulukkoa kehollisesti.
Opiskelijat näkevät - eivät vain kuule - että pseudokoodin lukeminen ei paljasta sitä, minkä kirjoitettu
seuranta paljastaa. Tämä tekee oppitunnin 18 keskeisen viestin fyysisesti näkyväksi juuri ennen AT2:n
käsittelyä.
Ryhmäkoko. Koko luokka. Yksi opiskelija per muuttuja, yksi "tulosteen kirjaajana" ja loput
havainnoijina, jotka huutavat, jos päivitys jää väliin.
Tarvittava aika. 25 min (oppitunti 18, kohta 55-80 min). Älä ota aikaa tehtävää edeltävästä 30
minuutin itsenäisen työn osasta.
Opettajan valmistelut.
1. Valitse virhe. Suositeltu oletus: off-by-one-virhe eli yhden pykälän virhe -ehdossa. `WHILE`
Vaihtoehtoja: väärä vertailu, puuttuva alustaminen, väärä -haara. `IF`
2. Kirjoita rikkinäinen pseudokoodi etukäteen lapulle. Älä improvisoi sitä livenä. Suositeltu pätkä:

```pseudocode
SET counter TO 5
WHILE counter > 1 DO
WRITE counter
SET counter TO counter - 1
ENDWHILE
WRITE "LIFT OFF"
```

Odotettu tuloste (kerro vasta seurannan jälkeen): , , , , , . `5 4 3 2 1 LIFT OFF`
Todellinen tuloste uskollisesta seurannasta: , , , , - puuttuu, koska

```
5 4 3 2 LIFT OFF 1 counter > 1
```

pysähtyy yhden askeleen liian aikaisin. Virheen nimi: off-by-one.
3. Päätä roolit. Lähtölaskentapätkässä tarvitaan yksi muuttujaopiskelija muuttujalle ja yksi `counter`
tulosteen kirjaaja.
4. Valmistele taulu otsikoilla Rivi · counter · Tuloste. Tyhjä seurantataulukko on tehtävän näyttämö.

### Vaiheittainen ohjaus

1. Aseta säännöt (2 min). Sano: "Yksi teistä on muuttuja . Jokaisen lukemani rivin jälkeen `counter`
sanot ääneen, mikä on nyt. Yksi teistä kirjaa tulosteen. Muut katsovat ja huutavat, jos `counter`
muuttujaopiskelijalta jää päivitys väliin. Seuraamme pseudokoodia kirjaimellisesti."
2. Jaa roolit (1 min). Varmista, että molemmat puhujat kuuluvat hyvin ja näkevät taulun.
3. Lue pseudokoodi ääneen, rivi riviltä ja hitaasti (10 min). Jokaisen rivin jälkeen
muuttujaopiskelija sanoo uuden arvon; tulosteen kirjaaja kirjoittaa kaiken -komennolla `WRITE`
tulostettavan tulostesarakeeseen; sinä täytät Rivi-sarakkeen. Tarkista jokaisen
silmukkakierroksen lopussa `WHILE`-ehto ääneen luokan kanssa. Sano esimerkiksi: "Counter
on 1. Onko 1 suurempi kuin 1? Ei. Silmukka loppuu." Virhe tulee näkyviin tässä.
17
Tunnilla tehtävät ohjatut tehtävät - sivu
4. Kerro odotettu tuloste (1 min). Tee tämä vasta, kun seuranta on valmis. Kirjoita odotettu tuloste
todellisen viereen taululle. Luokka näkee eron.
5. Diagnosoi (4 min). Kysy: "Millä rivillä todellinen tuloste lakkasi ensimmäisen kerran vastaamasta
odotettua tulostetta? Mitä sillä rivillä lukee?" Lue se ääneen. Pyydä opiskelijaa ehdottamaan
korjausta: muuttuu muotoon tai muuttuu muotoon .

```
> >= > 1 > 0
```

6. Tee korjaus ja jäljitä viimeisestä silmukkakierroksesta alkaen uudelleen (4 min). Aloita
korjausta edeltävältä riviltä. Tuloste päättyy nyt arvoon ja sitten . `1 LIFT OFF`
7. Nimeä virhetyyppi (2 min). Kirjoita taululle off-by-one. Sano: "Tämä on yksi maailman
tavallisimmista virheistä. Seurantataulukko löytää sen."
8. Lisää jatkuvaan virhelistaan (1 min). Pidä oppitunnista 18 viikkoon 7 jatkuvaa listaa otsikolla
"Virheet, jotka löysimme kuivaharjoittelemalla". Lisää tämä virhe listaan.
Ajattele näin: Seurantataulukko pakottaa sinut kysymään jokaisella rivillä: "Mikä muuttui?" Pelkkä
lukeminen saa virheen helposti näyttämään oikealta, koska aivot täyttävät puuttuvan kohdan.
Purkuun sopivia kysymyksiä.
• Millä rivillä todellinen tuloste erosi ensimmäisen kerran odotetusta tulosteesta? Mistä tiesit sen?
• Olisitteko voineet huomata virheen lukemalla pseudokoodin uudelleen ilman seurantataulukkoa?
• Miksi off-by-one on hyödyllisempi nimi kuin "silmukka oli väärin"?
• Jos omassa tehtävän 6.1 pseudokoodissasi on tai , mihin kohtaan off-by-one voisi `WHILE FOR`
piiloutua?
Miksi tehtävä vaatii luokkahuoneen. Jokaisella opiskelijalla on tehtävä. Muuttujaopiskelija sanoo
uuden arvon ääneen - ääni huomaa sen, minkä silmä ohittaa. Jaettu taulu sekä odotetun ja todellisen
tulosteen elävä ero ovat tehtävän ydin.
Viittaus. Tämä on oppitunnin 18 suunnitelman kohta 55-80 min tiedostossa `teacher-`
. Virheen nimi (off-by-one) siirtyy suoraan AT2:n reflektiokieleen kohdassa 80-88 min. `materials.md`

## Tehtävä B - "Pseudokoodin vaihto ja jäljitys" - VALINNAINEN

Tavoite. Opiskelijat selvittävät, onko heidän oma pseudokoodinsa ulkopuolisen ihmisen luettavissa.
Pseudokoodin lukeminen, jota et ole itse kirjoittanut, on taito, jota AT2 tarkistaa epäsuorasti
pyytäessään selityksiä selkeällä yleiskielellä.
Ryhmäkoko. Parit. Jos opiskelijoita on pariton määrä, yksi kolmen hengen ryhmä.
Tarvittava aika. 20 min (oppitunti 16, parityökohta 60-80 min).
Opettajan valmistelut.
1. Kirjoita taululle vaihdon säännöt.
2. Valmistele 3-4 varaprosessia opiskelijoille, joiden oma luonnos on liian lyhyt: teen tekeminen,
puhelimen lataaminen yön yli, rutiiniviestin lähettäminen Discordissa.
3. Varaa paperi ja kynä jokaiselle opiskelijalle. Ei teknologiaa.

### Vaiheittainen ohjaus

1. Selitä vaihto (2 min). Sano: "Vaihdätte aiemmin kirjoittamanne pseudokoodin. Ette nimeä
prosessia. Pari lukee sen hiljaa, kirjoittaa yhden virkkeen arvauksen tavoitteesta ja jäljittää sen
yhdelle syötteelle, jonka kirjoittaja valitsee."
2. Anna paperit toiselle (1 min). Ei suullisia vihjeitä.
3. Hiljainen arvausvirke (3 min). Jokainen lukija kirjoittaa paperin alareunaan "Luulen, että tämä
pseudokoodi liittyy asiaan ___" ennen kuin mikään jäljitys alkaa.
4. Jäljitys yhdelle kirjoittajan valitsemalle syötteelle (5 min). Piirrä erilliselle paperille pieni
seurantataulukko. Seuraa pseudokoodia kirjaimellisesti. Ei kysymyksiä jäljityksen aikana.
5. Paljastus ja keskustelu (2 min). Kirjoittaja nimeää tavoitteen. Vastatkaa yhdessä: "Tuottiko jäljitys
odotetun tulosteen? Oliko tavoite arvattavissa pelkkien vaiheiden perusteella?" Merkitkää yksi rivi,
jonka lukija luki uudelleen useimmin - se on korjausehdokas.
18
Tunnilla tehtävät ohjatut tehtävät - sivu
6. Roolien vaihto (5 min). Sama prosessi toiseen suuntaan.
7. Koko luokan purku (2 min). Kysy kahdelta parilta: "Mikä avainsana teki tavoitteen helpoimmin
arvattavaksi - , vai ?" Usein kantaa tavoitetta. Yhdistä: rehelliset muuttujanimet + `IF WHILE FOR IF`
näkyvä `IF` ovat luettavuuden vipuja.
Vinkki: Pyydä opiskelijaa merkitsemään eniten uudelleen luettu rivi tähdellä. Se antaa kirjoittajalle
konkreettisen korjauskohdan ilman, että parin tarvitsee osata antaa pitkää palautetta.
Purkuun sopivia kysymyksiä.
• Tuottiko parisi jäljitys sen tulosteen, jota odotit? Jos ei, oliko ero hänen jäljityksessään vai sinun
pseudokoodissasi?
• Minkä yhden rivin pari luki eniten uudelleen? Mikä muutos tekisi rivistä selkeän ensimmäisellä
lukukerralla?
• Oliko tavoite arvattavissa pelkkien vaiheiden perusteella vai vasta paljastuksen jälkeen?
Miksi tehtävä vaatii luokkahuoneen. Hiljainen arvausvirke pakottaa lukijan sitoutumaan ennen kuin
hän voi pyytää apua. Jaettu paperi ja elävä paljastus ovat asioita, joita LLM ei voi korvata.
Viittaus. Tämä on oppitunnin 16 suunnitelman kohta 60-80 min tiedostossa `teacher-`
. Jos opettajan on jätettävä jokin viikon tehtävä pois, jätä tehtävä B: tehtävä A kantaa `materials.md`
viikon 6 keskeisen viestin ja toimii AT2-valmiuden diagnostisena tehtävänä.
19
Tunnilla tehtävät ohjatut tehtävät - sivu
