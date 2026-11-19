# Viikko 6 — Opiskelijatehtävät

## Viikon tehtävien yleiskatsaus

Tällä viikolla on **neljä tehtävää**. Vihreällä pisteellä merkitty tehtävä (🟢 PAKOLLINEN) on **must-do-minimi** — tee se loppuun pysyäksesi luokan tahdissa ja ollaksesi valmis **AT2:lle, joka palautetaan tämän viikon oppitunnin 18 tienoilla**. Violetilla pisteellä merkityt tehtävät (🟣 SYVENTÄVÄT) ovat valinnaisia laajennuksia, jotka kaikki teroittavat samoja taitoja, joita AT2 tarkistaa.

Jokainen tehtävä syöttää suoraan AT2:een. AT2 pyytää sinua kirjoittamaan lyhyen pseudokoodin pienestä prosessista, käsiajamaan sen paperilla jäljityskaaviolla, ja selittämään arkikielellä, mitä kukin osa tekee. Tehtävät 6.1, 6.2 ja 6.3 rakentavat täsmälleen nuo kolme palaa: pseudokoodisi, jäljityksesi ja selityksesi. **Älä heitä mitään pois** — säilytä paperisi yhdessä kansiossa O18:aan asti.

Muistutus ennen kuin aloitat: tämä viikko on synteesiviikko. Pseudokoodi ei ole uusi kieli ulkoa opettelua varten; se on viikon 5 sekvenssi-ehto-toisto-ajattelua kirjoitettuna kiinteässä muodossa pienellä avainsanajoukolla (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). Ei oikeaa koodia missään. Paperi ja kynä riittävät.

---

## Tehtävä 6.1 — Pseudokoodaa tuttu prosessi 🟢 PAKOLLINEN

**Tavoite:** Kirjoita lyhyt pseudokoodi prosessista, jota teet itse, ja käsiaja se sitten paperilla jäljityskaaviolla. Tämä on viikon selkäranka ja suora syöttäjä AT2:lle.

Tämä on viikon 6 tärkein tehtävä. Tehtävät 6.2, 6.3 ja 6.4 syventävät samoja taitoja, mutta tämä *on* AT2-harjoitus.

### Vaiheet

1. **Valitse prosessi, jota teet itse lähes joka päivä.** Teen keittäminen, ilmoitusten tarkistaminen, repun pakkaaminen, puhelimen lataaminen yön yli, rutiinisanoman lähettäminen Discordissa. Sen on oltava prosessi, jonka kätesi jo osaavat — ei oppikirjaesimerkki.
2. **Kirjoita prosessi pseudokoodina (10–20 riviä).** Käytä luokan avainsanajoukkoa: `SET … TO …`, `READ`, `WRITE`, `IF … THEN … ELSE … ENDIF`, ja `WHILE … DO … ENDWHILE` tai `FOR each … IN … DO … ENDFOR`. **Vähintään yksi ehto ja vähintään yksi toisto vaaditaan.** Sisennä jokainen lohkon runko kahdella välilyönnillä.
3. **Nimeä muuttujasi rehellisesti.** `SET cupsOfTea TO 1` kertoo seuraavalle lukijalle, mitä varten rivi on; `SET x TO 1` ei.
4. **Käsiaja pseudokoodisi yhdellä *normaalilla* syötteellä.** Piirrä jäljityskaavio: yksi sarake per muuttuja, yksi mahdolliselle tulosteelle, yksi rivi per suoritettu rivi. Kävele alas rivi riviltä.
5. **Käsiaja se uudelleen yhdellä *hankalalla* syötteellä** — jotain puuttuu, jotain ylimääräistä: vedenkeitin on tyhjä, tepussukko on lopussa, puhelimessa on 1 % akkua. Tuore taulukko.
6. **Vertaa kahta jäljitystä.** Jos hankala tapaus ei käyttäytynyt niin kuin halusit, se on bugi — ympyröi rivi, jolla jäljitys ja odotuksesi ensimmäisen kerran erkanevat.
7. **Kirjoita 3–5 lauseen reflektio.** Mikä oli vaikeampaa ilmaista pseudokoodina kuin arkikielellä? Mikä oli helpompaa? Toiko hankalan syötteen jäljitys esiin jotain, jonka englanninkielinen proosa peitti?

### If you are doing this alone

Tämä tehtävä ei oleta paria — kaksi jäljitystäsi ovat testi. Saadaksesi toisen silmäparin ilman luokkakaveria, käytä **24 tunnin taukoa**: kirjoita pseudokoodi tänään, käsiaja se huomenna lukematta uudelleen reflektiota. Päivän vanha sinä on yllättävän sananmukainen seuraaja. Voit myös jäljittää sen kerran puhelimella ja kerran paperilla seuraavana päivänä — välineen vaihto löytää asioita, joiden yli silmä liukui ensimmäisellä kerralla.

> Vinkki: vastusta kiusausta kirjoittaa oikealta näyttävää koodia. ISOJEN KIRJAINTEN avainsanat ja arkikieliset arvot ovat juuri sitä, mitä kurssi haluaa. Oikea koodi saapuu ensi viikolla, ja pseudokoodin avainsanat kartoittuvat siihen puhtaasti.

### Keep your notes

Säilytä pseudokoodisi, molemmat jäljityskaaviot ja reflektiosi yhdessä kansiossa. **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla**, ja se pyytää täsmälleen tätä tuotosta — lyhyttä pseudokoodia pienestä prosessista, jäljityskaaviota yhdelle normaalille ja yhdelle hankalalle syötteelle ja lyhyttä reflektiota. Tehtävä 6.1 on AT2-harjoitus täysimittakaavaisena.

---

## Tehtävä 6.2 — Etsi bugi 🟣 SYVENTÄVÄ

**Tavoite:** Ota tarkoituksellisesti rikottu pseudokoodi, käsiaja se, tunnista bugi, korjaa se ja jäljitä uudelleen. AT2:n reflektio pyytää sinua nimeämään, mikä meni pieleen — tämä tehtävä on harjoitus.

### Rikkinäinen pseudokoodi

Tämän on tarkoitus laskea 5:stä 1:een ja sitten kirjoittaa `LIFT OFF`. **Täsmälleen yksi rivi on väärin.**

```text
SET counter TO 5
WHILE counter > 1 DO
  WRITE counter
  SET counter TO counter - 1
ENDWHILE
WRITE "LIFT OFF"
```

**Odotettu tuloste** on:

```text
5
4
3
2
1
LIFT OFF
```

### Vaiheet

1. **Ennusta tuloste lukemalla.** Ennen jäljitystä kirjoita ylös, mitä luulet sen tulostavan. Säilytä tämä ennustus.
2. **Käsiaja se paperilla.** Sarakkeet: rivinumero, `counter`, tuloste. Kävele jokainen rivi. Älä ohita `WHILE`-uudelleentarkistusta silmukan pohjalla.
3. **Vertaa todellista tulostetta (jäljityksestäsi) odotettuun.** Missä ne ensimmäisen kerran eroavat?
4. **Nimeä bugi arkikielellä.** Valitse: *off-by-one*, *väärä vertailu*, *puuttuva alustus*, *väärä haara*. Yksi lause perusteluksi.
5. **Korjaa pseudokoodi** (usein yksi merkki) ja kirjoita korjattu versio rikkinäisen viereen.
6. **Jäljitä korjaus tuoreelle taulukolle.** Vahvista, että todellinen tuloste täsmää nyt odotettuun.
7. **Kirjoita 3–5 lausetta** siitä, mitä jäljitys löysi ja mitä alkuperäinen lukutapasi jätti huomaamatta.

### If you are doing this alone

Tämä tehtävä ei oleta paria — jäljityskaavio on pari. Jos haluat järkevyystarkistuksen, postaa jäljityksesi (ei bugin nimeä) luokan chatissa: *"Täsmääkö todellinen tulosteeni sinun kanssasi?"*

> Vinkki: kun todellinen ja odotettu ovat eri mieltä, älä aloita muokkaamalla pseudokoodia. Aloita jäljittämällä uudelleen *tuoreelle* sivulle. Puolet ajasta bugi on jäljityksessäsi.

### Keep your notes

Säilytä ennustuksesi, molemmat jäljityskaaviot, nimeämäsi bugin tyyppi ja korjattu pseudokoodisi. **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla**, ja AT2 pyytää sinua kommentoimaan vähintään yhtä bugia, jonka olet löytänyt käsiajamalla.

---

## Tehtävä 6.3 — Jäljitä luokkakaverin pseudokoodi 🟣 SYVENTÄVÄ

**Tavoite:** Harjoittele lukemaan pseudokoodia, jota et itse kirjoittanut. Taito kertoo, onko oma pseudokoodisi *luettavaa* — ja luettavuus on täsmälleen sitä, mitä AT2 tarkistaa.

### Vaiheet

1. **Vaihda tehtävän 6.1 pseudokoodia luokkakaverin kanssa.** Älä kerro toisillenne, mikä prosessi on.
2. **Lue hiljaa. Ennen jäljitystä kirjoita yhden lauseen arvaus** siitä, mitä prosessia se kuvaa.
3. **Käsiaja se jäljityskaaviolla** yhdelle kirjoittajan ehdottamalle syötteelle ja yhdelle keksimällesi hankalalle syötteelle.
4. **Vertaa kirjoittajan kanssa.** Täsmäsikö tulosteesi? Oliko tavoite arvattavissa askeleista vai jouduitko kysymään? Mitä riviä luit eniten uudestaan?
5. **Vaihtakaa rooleja.** He jäljittävät sinun pseudokoodisi; sinä vertaat. Kumpikin pitää molemmat jäljitykset.
6. **Kirjoita 3–5 lausetta** siitä, mikä avainsana (`IF`, `WHILE`, `FOR`) teki tavoitteesta arvattavimman luokkakaverisi pseudokoodissa, ja mikä muuttujan nimi kantoi eniten merkitystä.

### If you are doing this alone

Jos sinulla ei ole luokkakaveria, jonka kanssa vaihtaa, aja tehtävä **menneisyyden itseäsi** vastaan. Käytä 24 tunnin taukoa: jäljitä aiemmin kirjoittamasi pseudokoodi (tehtävä 6.1, tai uudelleenkoodattu viikon 5 harjoitus) seuraavana päivänä lukematta uudelleen reflektiotasi. Vaihtoehdot, jotka myös toimivat: postaa pseudokoodisi luokan chatissa ja pyydä jotakuta jäljittämään; jäljitä kerran puhelimella ja kerran paperilla päivää myöhemmin. Mikä tahansa henkilön, päivän tai laitteen vaihto kelpaa.

> Vinkki: jos luet jotain yhtä riviä yli kahdesti jäljityksen aikana, merkitse se — se rivi on ehdokas uudelleenkirjoitukselle.

### Keep your notes

Säilytä arvauslauseesi, molemmat jäljityskaaviot ja vertailusi. **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla**, ja AT2:n reflektio palkitsee opiskelijoita, jotka osaavat sanoa, mitkä osat heidän pseudokoodistaan olivat helppoja ja mitkä vaikeita ulkopuolisen lukijan seurata. Tehtävä 6.3 antaa sinulle oikean ulkopuolisen lukijan.

---

## Tehtävä 6.4 — LLM harjoituskumppanina omaa jäljitystäsi vastaan 🟣 SYVENTÄVÄ

**Tavoite:** Käytä LLM:ää haastamaan oma käsiajosi. Harjoittele kohtelemaan LLM:ää harjoituskumppanina, ei opettajana.

### Vaiheet

1. **Aloita tehtävän 6.1 työstäsi** — pseudokoodistasi ja käsijäljityksestäsi hankalalle syötteelle.
2. **Liitä vain pseudokoodisi** (ei jäljitystäsi) LLM:ään alla olevalla kehotteella.
3. **Vertaa LLM:n ennustamaa jäljitystä omaasi, rivi riviltä.**
4. **Missä erotte mielipiteissä, jäljitä uudelleen käsin kolmannen kerran.** Päätä kumpi on oikeassa ja kirjoita yksi lause syystä.
5. **Kirjoita 4–6 lausetta** siitä, missä sinä ja LLM olitte eri mieltä, kuka oli oikeassa uudelleenjäljityksen jälkeen, ja mitä se kertoo pseudokoodistasi tai LLM:n lukutavasta.

### Esimerkkikehote

```text
You are my sparring partner, not my teacher. I am a vocational ICT
student practising how to dry-run pseudocode with a trace table.

Below is my pseudocode. The keywords SET, READ, WRITE, IF, ELSE,
ENDIF, WHILE, ENDWHILE, FOR, ENDFOR are shared course conventions,
not a real programming language.

[paste your pseudocode here]

Predict the trace for this input: [paste your awkward input here]

Show your trace as a table: one row per executed line, one column
per variable, plus a column for output. No prose explanations.

Do not assume your trace is correct. I will compare it to my own
hand trace and decide. If a line looks ambiguous, name the line
number — but do not rewrite my pseudocode for me.
```

**Älä hyväksy LLM:n jäljitystä totena.** Kohtele jokaista erimielisyyttä kysymyksenä.

### If you are doing this alone

Tämä tehtävä ei oleta ihmiskumppania — LLM on tilalla. Jos haluat myös ihmislukijan, postaa pseudokoodisi (ei jäljitystäsi) luokan chatissa: *"Jäljittäisikö joku tämän käsin?"* Kolme jäljitystä — sinun, LLM:n, luokkakaverin — ja mikä tahansa kahden välinen erimielisyys on pseudokoodisi mielenkiintoisin rivi.

> Vinkki: LLM:t ovat usein yhden toiston pielessä `WHILE`-silmukan sisällä. Jos eroatte täsmälleen yhdellä rivillä, tarkista pysäytysehto ensin.

### Keep your notes

Säilytä pseudokoodisi, käsijäljityksesi, LLM:n jäljitys ja kuka-oli-oikeassa-päätöskappaleesi. **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla**, ja opiskelija, joka pystyy osoittamaan hetken, jolloin hän jäljitti LLM:n yli, saa vahvan kappaleen AT2-reflektioon.
