# Viikko 6 — Ajattelusta koodiin

## Viikon tehtävien yleiskuva

Tällä viikolla on neljä tehtävää. Vihreällä pisteellä merkitty tehtävä (🟢 PAKOLLINEN) on
vähimmäissuoritus — tee se, jotta pysyt mukana ja olet valmis AT2:een, joka palautetaan
noin tämän viikon oppitunnilla 18. Violetilla pisteellä merkityt tehtävät (🟣 SYVENTÄVÄ)
ovat valinnaisia laajennuksia, jotka kaikki vahvistavat samoja taitoja, joita AT2 tarkistaa.
Jokainen tehtävä vie suoraan AT2:een. AT2 pyytää sinua kirjoittamaan pienestä prosessista
lyhyen pseudokoodin, käymään sen paperilla läpi jäljitystaulukon avulla ja selittämään
tavallisella kielellä, mitä kukin osa tekee. Tehtävät 6.1, 6.2 ja 6.3 rakentavat juuri nämä kolme
osaa: pseudokoodin, jäljityksen ja selityksen. Älä heitä mitään pois — pidä paperit yhdessä
kansiossa oppituntiin L18 asti.
Muistutus ennen aloittamista: tämä viikko on kokoava viikko. Pseudokoodi ei ole uusi kieli
ulkoa opeteltavaksi; se on viikon 5 järjestys–ehto–toisto-ajattelua kirjoitettuna vakioituun
muotoon pienellä avainsanajoukolla ( , , , , `SET READ WRITE IF/ELSE/ENDIF`
, ). Ei oikeaa koodia missään. Paperi ja kynä riittävät. `WHILE/ENDWHILE FOR/ENDFOR`
Käsitteet lyhyesti: pseudokoodi on koodia muistuttava tapa kuvata ratkaisu ilman oikean
ohjelmointikielen sääntöjä. Jäljitystaulukko taas näyttää rivi riviltä, miten muuttujien arvot ja
tulosteet muuttuvat.

## Tehtävä 6.1 — Kirjoita tutusta prosessista pseudokoodia 🟢 PAKOLLINEN

Tavoite: Kirjoita lyhyt pseudokoodi prosessista, jota oikeasti teet, ja käy se sitten paperilla läpi
jäljitystaulukon avulla. Tämä on viikon runko ja suora harjoitus AT2:een.
Tämä on viikon 6 tärkein tehtävä. Tehtävät 6.2, 6.3 ja 6.4 syventävät samoja taitoja, mutta tämä
on AT2-harjoitus.

### Vaiheet

1. Valitse prosessi, jota teet itse lähes joka päivä. Teen tekeminen, ilmoitusten
tarkistaminen, repun pakkaaminen, puhelimen lataaminen yön yli, rutiiniviestin
lähettäminen Discordissa. Sen täytyy olla prosessi, jonka kätesi jo osaavat — ei
oppikirjaesimerkki.
2. Kirjoita prosessi pseudokoodina (10–20 riviä). Käytä tunnilla sovittua
avainsanajoukkoa: , , , ja

```pseudocode
SET … TO … READ WRITE IF … THEN … ELSE … ENDIF
```

tai . Vähintään yksi

```pseudocode
WHILE … DO … ENDWHILE FOR each … IN … DO … ENDFOR
```

ehto ja vähintään yksi toisto vaaditaan. Sisennä jokaisen lohkon sisältö kahdella
välilyönnillä.
3. Nimeä muuttujat rehellisesti. kertoo seuraavalle `SET teekuppienMaara TO 1`
lukijalle, mitä rivi varten on; ei kerro. `SET x TO 1`
4. Käy pseudokoodi käsin läpi yhdellä normaalilla syötteellä. Piirrä jäljitystaulukko:
yksi sarake jokaiselle muuttujalle, yksi mahdolliselle tulosteelle ja yksi rivi jokaiselle
suoritetulle riville. Etene rivi riviltä.
5. Käy se uudelleen läpi yhdellä hankalalla syötteellä — jotakin puuttuu tai jotakin
on liikaa: vedenkeitin on tyhjä, teepurkki on loppu, puhelimen akku on 1 %. Tee uusi
taulukko.
6. Vertaa kahta jäljitystä. Jos hankala tapaus ei käyttäytynyt niin kuin halusit, se on bugi
— ympyröi rivi, jolla jäljitys ja odotuksesi eroavat ensimmäisen kerran.
7. Kirjoita 3–5 virkkeen pohdinta. Mikä oli vaikeampaa ilmaista pseudokoodilla kuin
tavallisella kielellä? Mikä oli helpompaa? Paljastiko hankalan syötteen jäljitys jotakin,
jonka proosateksti piilotti?

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse paria — kaksi jäljitystäsi ovat testi. Saat toisen silmäparin ilman
luokkakaveria käyttämällä 24 tunnin väliä: kirjoita pseudokoodi tänään ja käy se huomenna
läpi lukematta pohdintaasi uudelleen. Päivän vanha sinä on yllättävän kirjaimellinen suorittaja.
Voit myös jäljittää kerran puhelimella ja kerran paperilla seuraavana päivänä — välineen
vaihtuminen löytää asioita, jotka silmä ohitti ensimmäisellä kerralla.
Vinkki: vastusta halua kirjoittaa oikealta koodilta näyttävää tekstiä. ISOT avainsanat
ja tavalliset suomenkieliset arvot ovat juuri sitä, mitä kurssi haluaa. Oikea koodi tulee
ensi viikolla, ja pseudokoodin avainsanat vastaavat sitä siististi.

### Säilytä muistiinpanosi

Säilytä pseudokoodisi, molemmat jäljitystaulukot ja pohdintasi yhdessä kansiossa. AT2
palautetaan noin tämän viikon oppitunnilla 18, ja se pyytää juuri tätä tuotosta: lyhyt
pseudokoodi pienestä prosessista, jäljitystaulukko yhdelle normaalille ja yhdelle hankalalle
syötteelle sekä lyhyt pohdinta. Tehtävä 6.1 on täysimittainen AT2-harjoitus.

## Tehtävä 6.2 — Etsi bugi 🟣 SYVENTÄVÄ

Tavoite: Ota tarkoituksella rikkinäinen pseudokoodi, käy se läpi, tunnista bugi, korjaa se ja
jäljitä uudelleen. AT2:n pohdinta pyytää nimeämään, mikä meni pieleen — tämä tehtävä on
harjoitus siihen.

### Rikkinäinen pseudokoodi

Tämän pitäisi laskea alaspäin viidestä yhteen ja sen jälkeen kirjoittaa . Täsmälleen `LÄHTÖ`

yksi rivi on väärin.

```pseudocode
SET laskuri TO 5
WHILE laskuri > 1 DO
WRITE laskuri
SET laskuri TO laskuri - 1
ENDWHILE
WRITE "LÄHTÖ"
```

Odotettu tuloste on:

```
5
4
3
2
1
LÄHTÖ
```

### Vaiheet

1. Ennusta tuloste lukemalla. Ennen kuin jäljität, kirjoita ylös, mitä luulet pseudokoodin
tulostavan. Säilytä ennuste.
2. Käy se paperilla läpi. Sarakkeet: rivinumero, , tuloste. Käy jokainen rivi läpi. `laskuri`
Älä ohita -ehdon uudelleentarkistusta silmukan lopussa. `WHILE`
3. Vertaa todellista tulostetta, jonka sait jäljityksestä, odotettuun tulosteeseen.
Missä ne eroavat ensimmäisen kerran?
4. Nimeä bugi tavallisella kielellä. Valitse jokin näistä: off-by-one-virhe, väärä vertailu,
puuttuva alustaminen, väärä haara. Kirjoita yksi virke siitä, miksi.
5. Korjaa pseudokoodi (usein yksi merkki riittää) ja kirjoita korjattu versio rikkinäisen
viereen.
6. Jäljitä korjaus uudella taulukolla. Varmista, että todellinen tuloste vastaa nyt
odotettua.
7. Kirjoita 3–5 virkettä siitä, mitä jäljitys paljasti sellaista, mikä jäi ensimmäisellä
lukemisella huomaamatta.

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse paria — jäljitystaulukko on parisi. Jos haluat varmistuksen, lähetä
jäljityksesi (ei bugin nimeä) luokan chattiin: “Vastaako todellinen tuloste teidän tulostettanne?”
Vinkki: kun todellinen ja odotettu tuloste eroavat, älä aloita muokkaamalla
pseudokoodia. Aloita jäljittämällä uudelleen puhtaalle sivulle. Noin puolet ajasta bugi
on omassa jäljityksessäsi.

### Säilytä muistiinpanosi

Säilytä ennusteesi, molemmat jäljitystaulukot, nimetyn bugityypin selitys ja korjattu
pseudokoodisi. AT2 palautetaan noin oppitunnilla 18, ja siinä pyydetään kommentoimaan
vähintään yhtä bugia, jonka löysit käsin läpikäynnillä.

## Tehtävä 6.3 — Jäljitä luokkakaverin pseudokoodi 🟣 SYVENTÄVÄ

Tavoite: Harjoittele lukemaan pseudokoodia, jota et ole itse kirjoittanut. Taito kertoo, onko
oma pseudokoodisi luettavaa — ja luettavuus on juuri sitä, mitä AT2 tarkistaa.

### Vaiheet

1. Vaihda tehtävän 6.1 pseudokoodi luokkakaverin kanssa. Älkää kertoko toisillenne,
mikä prosessi on kyseessä.
2. Lue hiljaa. Kirjoita ennen jäljitystä yhden virkkeen arvaus siitä, mitä prosessia
pseudokoodi kuvaa.
3. Käy se läpi jäljitystaulukolla yhdellä syötteellä, jonka kirjoittaja ehdottaa, ja yhdellä
hankalalla syötteellä, jonka keksit itse.
4. Vertaa kirjoittajan kanssa. Vastasko tulosteesi? Oliko tavoite arvattavissa vaiheista,
vai jouduitko kysymään? Minkä rivin luit uudelleen kaikkein useimmin?
5. Vaihtakaa rooleja. Hän jäljittää sinun pseudokoodisi; sinä vertaat. Kumpikin säilyttää
molemmat jäljitykset.
6. Kirjoita 3–5 virkettä siitä, mikä avainsana ( , , ) teki tavoitteen `IF WHILE FOR`
helpoimmin arvattavaksi luokkakaverin pseudokoodissa ja mikä muuttujan nimi kantoi
eniten merkitystä.

### Jos teet tämän yksin

Jos sinulla ei ole luokkakaveria, jonka kanssa vaihtaa, tee tehtävä menneelle itsellesi. Käytä
24 tunnin väliä: jäljitä aiemmin kirjoittamaasi pseudokoodia (tehtävä 6.1 tai viikon 5
harjoituksen pseudokoodiversio) seuraavana päivänä lukematta pohdintaasi uudelleen. Muita
toimivia vaihtoehtoja: lähetä pseudokoodisi luokan chattiin ja pyydä jotakuta jäljittämään se;
jäljitä kerran puhelimella ja kerran paperilla päivää myöhemmin. Henkilön, päivän tai välineen
vaihtaminen riittää.
Vinkki: jos luet yhtä riviä jäljityksen aikana yli kaksi kertaa, merkitse se — se rivi on
ehdokas uudelleenkirjoitukseen.

### Säilytä muistiinpanosi

Säilytä arvausvirkkeesi, molemmat jäljitystaulukot ja vertailusi. AT2 palautetaan noin
oppitunnilla 18, ja AT2:n pohdinta palkitsee opiskelijaa, joka osaa sanoa, mitkä pseudokoodin
osat olivat ulkopuoliselle lukijalle helppoja ja mitkä vaikeita seurata. Tehtävä 6.3 antaa sinulle
oikean ulkopuolisen lukijan.
🟣

## Tehtävä 6.4 — LLM sparrauskumppanina omaa jäljitystäsi vastaan SYVENTÄVÄ

Tavoite: Käytä LLM:ää haastamaan omaa käsin tehtyä läpikäyntiäsi. Harjoittelet käsittelemään
LLM:ää sparrauskumppanina, et opettajana.

### Vaiheet

1. Aloita tehtävän 6.1 työstäsi — pseudokoodistasi ja hankalan syötteen käsin
tekemästäsi jäljityksestä.
2. Liitä LLM:ään vain pseudokoodisi (ei omaa jäljitystäsi) alla olevalla kehotteella.
3. Vertaa LLM:n ennustamaa jäljitystä omaasi rivi riviltä.
4. Jos olette eri mieltä, jäljitä käsin kolmannen kerran. Päätä, kumpi on oikeassa, ja
kirjoita yksi virke siitä, miksi.
5. Kirjoita 4–6 virkettä siitä, missä kohtaa sinä ja LLM olitte eri mieltä, kumpi oli
oikeassa uudelleenjäljityksen jälkeen ja mitä se kertoo pseudokoodistasi tai LLM:n
lukutavasta.

### Esimerkkikehote

```javascript
Olet sparrauskumppanini, et opettajani. Olen ammatillisen ICT-alan
opiskelija ja harjoittelen pseudokoodin käsin läpikäyntiä
jäljitystaulukon avulla. Alla on pseudokoodini. Avainsanat SET, READ,
WRITE, IF, ELSE, ENDIF, WHILE, ENDWHILE, FOR, ENDFOR ovat kurssin
yhteisiä käytäntöjä, eivät oikeaa ohjelmointikieltä.
[liitä pseudokoodisi tähän]
Ennusta jäljitys tälle syötteelle: [liitä hankala syötteesi tähän]
Näytä jäljitys taulukkona: yksi rivi per suoritettu rivi, yksi sarake
per muuttuja sekä sarake tulosteelle. Ei proosamuotoisia selityksiä.
Älä oleta, että jäljityksesi on oikea. Vertaan sitä omaan käsin tehtyyn
jäljitykseeni ja päätän. Jos jokin rivi näyttää epäselvältä, nimeä
rivinumero — mutta älä kirjoita pseudokoodiani uudelleen puolestani.
```

Älä hyväksy LLM:n jäljitystä totuutena. Käsittele jokaista erimielisyyttä kysymyksenä.

### Jos teet tämän yksin

Tämä tehtävä ei tarvitse ihmiskumppania — LLM toimii sellaisena. Jos haluat myös
ihmislukijan, lähetä pseudokoodisi (ei jäljitystäsi) luokan chattiin: “Voisiko joku jäljittää tämän
käsin?” Kolme jäljitystä — omasi, LLM:n ja luokkakaverin — sekä mikä tahansa kahden
välinen erimielisyys tekee pseudokoodin kiinnostavimman rivin näkyväksi.
Vinkki: LLM:t erehtyvät usein yhdellä kierroksella -silmukan sisällä. Jos ero `WHILE`
on täsmälleen yksi rivi, tarkista ensin pysähtymisehto.

### Säilytä muistiinpanosi

Säilytä pseudokoodisi, käsin tehty jäljityksesi, LLM:n jäljitys ja kappale, jossa päätät kumpi oli
oikeassa. AT2 palautetaan noin oppitunnilla 18, ja opiskelijalla, joka osaa osoittaa kohdan,
jossa hän jäljitti paremmin kuin LLM, on vahva kappale AT2-pohdintaan.
