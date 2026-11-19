# Oppitunti 24 — Testaa, korjaa yksi virhe, esitä

Tällä oppitunnilla tapahtuu kolme asiaa, ja ne kaikki nojaavat toimivaan ohjelmaan.
• Testaa kahdella eri alkuarvolla.
• Lue yksi oikea virheilmoitus ja korjaa yksi rivi.
• Esitä koko tarina kahdessa minuutissa.

### Käsin testaaminen

Testaaminen tarkoittaa tällä viikolla yhtä hyvin tarkkaa asiaa: aja ohjelma vähintään

### kahdella eri alkuarvolla ja tarkista, että tuloste käy järkeen molemmilla kerroilla. Ei

automaattista testityökalua, ei testikehyksiä, ei uutta sanastoa. Vaihdat vain yhtä numeroa tai
yhtä merkkijonoa ohjelman alusta ja ajat ohjelman uudelleen.
Ikärajatarkistusohjelmassa nämä kaksi arvoa voisivat olla esimerkiksi ja .

```
age = 17 age = 19
```

Ensimmäisen pitäisi tulostaa , toisen . Jos molemmat ajot vastaavat `not allowed allowed`
ennustetta, ohjelma läpäisee käsin tehdyn testin. Jos toinen tulostaa väärän viestin, löysit juuri
virheen.
JavaScript — vaihda yksi rivi ajojen välillä

```javascript
let age = 17; // aja kerran 17:llä, vaihda sitten 19:ään ja aja uudestaan
```

C# — vaihda yksi rivi ajojen välillä

```
int age = 17; // aja kerran 17:llä, vaihda sitten 19:ään ja aja uudestaan
```

AT3:ssa ajat oman ohjelmasi kahdella eri arvolla ja tallennat molemmat tulokset. Yksi
kuvakaappaus, jossa näkyvät molemmat ajot, riittää. Kaksi erillistä kuvakaappausta käy myös.

### Oikean virheilmoituksen lukeminen

Kun tietokone ei ole tyytyväinen, se näyttää virheilmoituksen. Se näyttää aluksi pelottavalta
— pitkältä ja tekniseltä — mutta tämän viikon yksinkertaisissa virheissä viesti osoittaa lähes
aina suoraan oikealle riville.
Tavallinen JavaScript-virhe:

```
Uncaught ReferenceError: scre is not defined
at <anonymous>:3:15
```

Ja sen C#-serkku:

```
error CS0103: The name 'scre' does not exist in the current context
```

Molemmat sanovat pohjimmiltaan saman asian: en tiedä, mikä on. Yleisin syy on `scre`
kirjoitusvirhe. Julistit aiemmin muuttujan nimeltä , mutta myöhemmin kirjoitit . `score scre`
Ratkaisu: etsi sana , kirjoita puuttuva ja aja ohjelma uudestaan. `scre o`
Tämä on juuri tämän kurssin tasoista debuggausta: lue mitä tietokone sanoi, etsi rivi, johon
viesti viittaa, muuta yksi pieni asia ja aja uudelleen.
Kaksi muuta yleistä virhemuotoa tällä viikolla:
• JavaScriptissä siellä missä pitäisi olla voi joskus aiheuttaa hiljaisen väärän `= ===`
vastauksen ilman näkyvää virheilmoitusta. Huomaat sen juuri kahden eri syötteen
testauksessa.
• C#:ssa puuttuva puolipiste näyttää viestin ja kertoo rivin `error CS1002: ; expected`
numeron. Lisää puuttuva , tallenna ja aja uudelleen. `;`
Pysähdy hetkeksi: Valitse yksi ohjelma, jonka kirjoitit oppitunnilla 23. Kirjoita yksi
muuttujan nimi tahallaan väärin ohjelman keskellä. Aja ohjelma. Lue virheilmoitus.
Ennusta ennen korjaamista, mihin sanaan virheilmoitus viittaa. Korjaa sitten
ohjelma ja aja uudelleen.

### Yksi pieni korjaus, yksi uusi ajo

Tällä kurssilla debuggaus tarkoittaa: lue konsolin virheilmoitus ja tee yksi pieni korjaus.
Et tarvitse erillistä debuggaustyökalua. Et tarvitse erityisiä ohjelmistoja tai testikehyksiä. Koko
sykli on tämä:
1. Aja ohjelma.
2. Näe virheilmoitus tai odottamaton tuloste.
3. Lue viesti tai vertaa odotettua ja todellista tulostetta.
4. Etsi vastuullinen rivi.
5. Muuta yksi pieni asia.
6. Aja ohjelma uudelleen.
AT3:ssa sinun pitää tehdä tämä vähintään kerran. Virhe voi olla kirjoitusvirhe, puuttuva
puolipiste, siellä missä pitäisi olla , puuttuva — mikä tahansa käy. Jos ohjelmasi toimi `= == }`
heti ensimmäisellä yrityksellä, aiheuta virhe tahallaan: riko yksi asia, lue viesti ja korjaa se
takaisin.

### 2 minuutin esitys

Oppitunnilla 24 pidät 2 minuutin suullisen esityksen ohjelmastasi. Kaksi minuuttia on lyhyt
aika — noin 200 puhuttua sanaa. Esityksessä on neljä osaa, noin 30 sekuntia kullekin:
1. Mitä ohjelma tekee. Yksi tai kaksi lausetta tavallisella suomella. Esimerkiksi:
“Ohjelmani ottaa salasanan ja tulostaa joko ‘strong enough’ tai ‘too short’ sen mukaan,
kuinka pitkä salasana on.”
2. Miten ohjelma tekee sen. Käy rakenne läpi. Esimerkiksi: “Alussa asetan muuttujan
nimeltä . Sitten ohjelmassa on : jos salasanan pituus on vähintään 8, `password if/else`
ohjelma tulostaa ‘strong enough’, muuten ‘too short’.” Jos ohjelmassasi on silmukka,
nimeä sen neljä osaa: laskuri, ehto, runko, päivitys.
3. Mikä meni pieleen. Nimeä yksi löytämäsi virhe. Esimerkiksi: “Ensimmäisellä
ajokerralla kirjoitin pienellä l-kirjaimella, mutta C#:ssa sen pitää olla `password.length`
isolla L:llä, joten sain virheilmoituksen.” `Length`
4. Miten korjasit virheen. Yksi selkeä lause. Esimerkiksi: “Vaihdoin pienen l-kirjaimen
isoksi L-kirjaimeksi ja ajoin ohjelman uudestaan.”
Siinä ovat sinun kaksi minuuttiasi. Et tarvitse dioja. Et tarvitse sanasta sanaan luettua
käsikirjoitusta. Et tarvitse eleganttia koodia. Sinun pitää vain seistä oman ohjelmasi takana
ja selittää se omin sanoin.
Käytännön vinkki: harjoittele kotona kerran puhelimen ajastimen kanssa. Jos lopetat 45
sekunnissa, jokin esityksen osa puuttuu. Jos puhut yli kaksi minuuttia, luet luultavasti koodia
rivi riviltä — jätä se pois ja puhu enemmän siitä, mitä ohjelma tekee.
Pysähdy hetkeksi: Avaa ohjelmasi ruudulle ja kokeile puhua nämä neljä osaa
ääneen. Ensimmäinen yritys on usein liian lyhyt tai liian pitkä. Toinen on jo paljon
lähempänä oikeaa mittaa. Esitys ei mittaa muistamista vaan sitä, pystytkö seisomaan
oman työsi takana.

### Vertailu luokkakaverin kanssa

Jos aikaa jää oppitunnilla 24 esitysten jälkeen, etsi luokkakaveri, joka käytti toista
ohjelmointikieltä. Lukekaa toistenne ohjelmat. Kirjoittakaa 3–5 lausetta siitä, mikä näyttää
erilaiselta — esimerkiksi puolipisteet kaikkialla C#:ssa mutta vain käytäntönä JavaScriptissä,
vs. , ja vs. , isolla alkavat metodinimet C#:ssa — ja

```javascript
Console.WriteLine console.log int string let
```

yksi lause siitä, mikä näyttää samalta: silmukat ja -rakenteet ovat hämmästyttävän `if/else`
saman näköisiä. Juuri tämä on koko kahden kielen rinnakkain näyttämisen pointti.

## Miten AT3 arvioidaan

AT3 arvioidaan muodossa hyväksytty / ei vielä hyväksytty. Ei numeroarvosanaa, ei pitkää
pistetaulukkoa. Vain lyhyt tarkistuslista.

### Palautat:

• lähdekoodin ( - tai -tiedoston, tai selkeästi aidatun koodilohkon oikealla `.js .cs`
kielitunnisteella)
• kuvakaappauksen ohjelman ajosta vähintään yhdellä odotetulla tulosteella
• 3–5 lauseen kirjallisen pohdinnan, jossa nimeät löytämäsi virheen ja tekemäsi
korjauksen
• 2 minuutin suullisen esityksen oppitunnilla 24, jossa käyt läpi yllä nimetyt neljä osaa

### Opettaja tarkistaa neljä asiaa:

• ohjelma toimii (tai epäonnistunut yritys on dokumentoitu virheilmoituksineen)
• osaat sanoa yleiskielellä, mitä ohjelma tekee
• yksi virhe–korjaus-pari on dokumentoitu
• 2 minuutin esitys on pidetty
Jos jokin näistä neljästä puuttuu, työ on ei vielä hyväksytty, ja opettaja kertoo, mitä pitää
vielä täydentää. Tässä ei ole häpeää — se tarkoittaa vain, että yksi pieni asia puuttuu vielä.

## Yhteenveto — silmukka sulkeutuu kurssin keskeiseen kysymykseen

Kahdeksan viikkoa sitten tämä kurssi alkoi yhdellä kysymyksellä. Olet vastannut siihen
pieninä paloina joka viikko. Nyt pystyt vastaamaan siihen kokonaisena, omin sanoin, toimiva
ohjelma kädessäsi.
Sama kysymys vielä kerran, täsmälleen samassa muodossa kuin viikolla 1:

### Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla vastaat siihen tekemällä sen. Otat itse kirjoittamasi viikon 6 pseudokoodin ja
käännät sen JavaScriptiksi tai C#:ksi. Luot muuttujan. Kirjoitat -rakenteen. Kirjoitat - `if/else for`
silmukan. Painat Run. Jos tietokone ei ole tyytyväinen, se näyttää virheilmoituksen, joka
osoittaa yhtä väärää riviä, ja sinä korjaat juuri sen rivin. Sitten nouset luokan eteen ja kerrot
kahdessa minuutissa, mitä ohjelmasi tekee ja miten korjasit virheen.
Tämä on ohjelmointia tällä tasolla. Ei taikuutta. Ei mysteeriä. Vain pieni, huolellinen tiedosto
ohjeita, joka tekee täsmälleen sen mitä kirjoitit. Kaikki, mitä loput opinnot lisäävät tämän
päälle — uusia kieliä, suurempia projekteja, kirjastoja, kehyksiä ja tiimityötä — rakentuu
edelleen saman asian päälle: kirjaimellinen tietokone seuraa ohjeita, jotka sinä kirjoitit, ja
kertoo tekstinä, jos jokin ei ole jäsentynyt oikein.
Ohjelmointi ei ole enää mystinen asia.
Säilytä AT3:n lähdekooditiedosto. Avaa se uudelleen puolen vuoden päästä. Se näyttää pieneltä.
Juuri siinä on asian ydin — sinä kirjoitit sen itse.
Tervetuloa kurssin keskeisen kysymyksen toiselle puolelle.
