# Viikko 6 — Tuntitehtävät

## Yleiskatsaus

Tämä tiedosto sisältää **tuntiluonteiset, opettajan vetämät** aktiviteetit viikolle 6. Ne ajetaan oppitunnin aikana, ei kotitehtävänä, eikä niitä voi korvata LLM:llä tai monisteella.

- **Aktiviteetti A — "Käsiajo luokkana"** on **PAKOLLINEN**. Se kuuluu **oppitunnin 18 55–80 min lohkoon** ja on ruumiillistettu diagnostiikka AT2-valmiudelle. Koko luokasta tulee jäljityskaavio, yksi opiskelija per muuttuja, ja bugi nousee esiin kaikkien edessä.
- **Aktiviteetti B — "Pseudokoodin vaihto ja jäljitys"** on **VALINNAINEN**. Se sopii **oppitunnin 16 60–80 min pariaktiviteettilohkoon**.

---

## Aktiviteetti A — "Käsiajo luokkana" PAKOLLINEN

**Tavoite.** Luokka suorittaa kollektiivisesti käsiajon, ruumiillistaen jäljityskaavion. Opiskelijat näkevät — eivätkä siksi, että heille kerrottaisiin — että pseudokoodin lukeminen ei löydä sitä, mitä kirjoitettu jäljitys löytää. Tekee oppitunnin 18 ydinviestin fyysisesti näkyväksi juuri ennen AT2-luovutusta.

**Ryhmäkoko.** Koko luokka. Yksi opiskelija per muuttuja, yksi "tulosteen kirjaajana", loput tarkkailijoina, jotka huutavat, kun päivitys jää huomaamatta.

**Ajantarve.** 25 min (oppitunti 18, **55–80 min lohko**). Älä lainaa sitä edeltävältä 30 min itsenäiseltä lohkolta.

**Opettajan valmistautuminen.**

1. **Valitse bugisi.** Suositeltu oletus: **off-by-one** `WHILE`-ehdossa. Vaihtoehdot: väärä vertailu, puuttuva alustus, väärä haara `IF`.
2. **Esikirjoita rikottu pseudokoodi** lapulle — älä improvisoi elävänä. Suositeltu katkelma:

   ```text
   SET counter TO 5
   WHILE counter > 1 DO
     WRITE counter
     SET counter TO counter - 1
   ENDWHILE
   WRITE "LIFT OFF"
   ```

   **Odotettu tuloste (julkista vasta jäljityksen päätyttyä):** `5`, `4`, `3`, `2`, `1`, `LIFT OFF`. **Todellinen tuloste rehellisestä jäljityksestä:** `5`, `4`, `3`, `2`, `LIFT OFF` — `1` puuttuu, koska `counter > 1` pysähtyy askeleen liian aikaisin. Bugin nimi: **off-by-one**.
3. **Päätä roolitus.** Lähtölaskenta-katkelmalle: yksi muuttujaopiskelija `counter`:lle, yksi tulosteen kirjaaja.
4. **Pidä taulu valmiina** sarakeotsikoineen **Rivi · counter · Tuloste**. Tyhjä jäljityskaavio on näyttämö.

**Vaiheittainen fasilitointi.**

1. **Aseta säännöt (2 min).** *"Yksi teistä on muuttuja `counter`. Jokaisen lukemani rivin jälkeen sanot ääneen, mitä `counter` nyt on. Yksi teistä on tulosteen kirjaaja. Loput katsovat ja huutavat, jos muuttujaopiskelija jättää päivityksen tekemättä. Noudatamme pseudokoodia sananmukaisesti."*
2. **Anna roolit (1 min).** Varmista, että molemmilla puhujilla on selkeä ääni ja näkymä taululle.
3. **Lue pseudokoodi ääneen, rivi riviltä, hitaasti (10 min).** Jokaisen rivin jälkeen: muuttujaopiskelija huutaa uuden arvon; tulosteen kirjaaja kirjoittaa kaiken `WRITE`-rivin tulosteen tuloste-sarakkeeseen; sinä täytät Rivi-sarakkeen. **Jokaisen silmukan pohjalla, tarkista `WHILE`-ehto uudelleen ääneen luokkana.** *"Counter on 1. Onko 1 suurempi kuin 1? Ei. Silmukka päättyy."* Bugi nousee esiin tässä.
4. **Julkista odotettu tuloste (1 min).** *Vasta sen jälkeen, kun jäljitys on suoritettu loppuun.* Kirjoita odotettu todellisen viereen taululle. Luokka näkee aukon.
5. **Diagnosoi (4 min).** Kysy: *"Millä rivillä todellinen tuloste lakkasi ensimmäisen kerran täsmäämästä odotetun kanssa? Mitä se rivi sanoo?"* Lue se ääneen. Pyydä opiskelijaa ehdottamaan korjausta (`>` muuttuu `>=`:ksi, tai `> 1` muuttuu `> 0`:ksi).
6. **Sovella korjaus ja jäljitä uudelleen silmukan viimeisestä toistosta (4 min).** Aloita korjauksen yläpuolelta. Tuloste päättyy nyt `1`:een, sitten `LIFT OFF`.
7. **Nimeä bugin tyyppi (2 min).** Kirjoita **"off-by-one"** taululle. *"Tämä on maailman yleisin bugi. Jäljityskaavio löytää sen."*
8. **Lisää juokseville bugilistalle (1 min).** Pidä lista yli O18:n ja viikkoon 7 asti otsikolla *"Bugit, jotka olemme löytäneet käsiajamalla"*. Lisää tämä.

**Purkukysymyksiä.**

- Millä rivillä todellinen tuloste poikkesi ensimmäisen kerran odotetusta? Mistä tiesit?
- Olisitko voinut havaita tämän bugin lukemalla pseudokoodia uudelleen ilman jäljitystä?
- Miksi *off-by-one* on hyödyllisempi nimi kuin *"silmukka oli väärin"*?
- Jos oman tehtävän 6.1 pseudokoodissasi on `WHILE` tai `FOR`, missä off-by-one voisi piileskellä siellä?

**Miksi vaatii luokkahuoneen.** Jokaisella opiskelijalla on tehtävä. Muuttujaopiskelija *sanoo* uuden arvon ääneen — ääni löytää sen, mitä silmä jättää huomaamatta. Yhteinen taulu ja elävä ero odotetun ja todellisen tulosteen välillä ovat koko idea.

**Ristiviittaus.** Tämä on **oppituntisuunnitelman 18 55–80 min lohko** tiedostossa `opettajan-materiaalit.md`. Bugin nimi (*off-by-one*) syöttää suoraan AT2-reflektion sanastoon 80–88 min kohdalla.

---

## Aktiviteetti B — "Pseudokoodin vaihto ja jäljitys" VALINNAINEN

**Tavoite.** Opiskelijat huomaavat, onko heidän oma pseudokoodinsa *luettavaa* ulkopuoliselle ihmiselle. Itse kirjoittamattoman pseudokoodin lukeminen on taito, jota AT2 tarkistaa epäsuorasti pyytäessään selkokielisiä selityksiä.

**Ryhmäkoko.** Parit. (Pariton määrä: yksi kolmen ryhmä.)

**Ajantarve.** 20 min (oppitunti 16, **60–80 min pariaktiviteettilohko**).

**Opettajan valmistautuminen.**

1. Taululla vaihtoa koskevat säännöt.
2. 3–4 varaprosessia opiskelijoille, joiden luonnos on liian lyhyt — teen keittäminen, puhelimen lataaminen yön yli, rutiinisanoman lähettäminen Discordissa.
3. Paperia ja kynä per opiskelija. Ei tekniikkaa.

**Vaiheittainen fasilitointi.**

1. **Selitä vaihto (2 min).** *"Vaihdatte aiemmin kirjoittamanne pseudokoodin. Et nimeä prosessia. Parisi lukee sen hiljaa, kirjoittaa yhden lauseen arvauksen tavoitteesta, ja sitten jäljittää sen yhdelle valitsemallesi syötteelle."*
2. **Anna paperit (1 min).** Ei sanallisia vihjeitä.
3. **Hiljainen arvauslause (3 min).** Jokainen lukija kirjoittaa *"Mielestäni tämä pseudokoodi käsittelee ___."* sivun alalaitaan **ennen** kuin jäljitys alkaa.
4. **Jäljitä yhdelle kirjoittajan valitsemalle syötteelle (5 min).** Erilliselle paperille, piirrä pieni jäljityskaavio. Noudata pseudokoodia sananmukaisesti. Ei kysymyksiä jäljityksen aikana.
5. **Paljastus ja keskustelu (2 min).** Kirjoittaja nimeää tavoitteen. Yhdessä vastatkaa: *"Tuottiko jäljitys odotetun tulosteen? Oliko tavoite arvattavissa pelkistä askeleista?"* Merkitse **se yksi rivi, jonka lukija luki eniten uudestaan** — se on uudelleenkirjoituksen ehdokas.
6. **Vaihtakaa rooleja (5 min).** Sama silmukka.
7. **Koko luokan purku (2 min).** Kysy kahdelta parilta: *"Mikä avainsana teki tavoitteesta arvattavimman — `IF`, `WHILE` vai `FOR`?"* Yleensä `IF` kantaa tavoitteen. Yhdistä: **rehelliset muuttujien nimet + näkyvä `IF` ovat luettavuuden vipuvarret**.

**Purkukysymyksiä.**

- Tuottiko parisi jäljitys odotetun tulosteen? Jos ei, oliko aukko hänen jäljityksessään vai sinun pseudokoodissasi?
- Mitä yhtä riviä parisi luki eniten uudestaan? Mikä muutos saisi rivin lukemaan puhtaasti ensimmäisellä kerralla?
- Oliko tavoite arvattavissa pelkistä askeleista vai vasta paljastuksen jälkeen?

**Miksi vaatii luokkahuoneen.** Hiljainen arvauslause pakottaa lukijan sitoutumaan ennen kuin hän voi pyytää apua. Yhteinen paperi ja elävä paljastus ovat se, mitä LLM ei voi korvata.

**Ristiviittaus.** Tämä on **oppituntisuunnitelman 16 60–80 min lohko** tiedostossa `opettajan-materiaalit.md`. Jos opettajan on pudotettava yksi aktiviteetti tällä viikolla, pudota aktiviteetti B — **aktiviteetti A kantaa viikon 6 ydinviestin** ja on AT2-valmiuden diagnostiikka.
