# Viikko 8 — Opettajan materiaalit

Tämä dokumentti kattaa O22:n, O23:n ja O24:n. Viikon keskeinen viesti: **"Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen JavaScriptiksi tai C#:ksi, ajat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi on lakannut olemasta mystinen asia."** Mitään aidosti uutta ei laskeudu käsitteellisesti — vain silmukka koodissa — mutta kaikki viikolta 1 lähtien kohtaa vihdoin yhdessä pienessä tiedostossa, jonka kukin opiskelija voi puolustaa ääneen.

**AT3 palautetaan ja esitetään tällä viikolla.** O23 on rakennuspäivä: kukin opiskelija kääntää yhden palan omaa viikon 6 pseudokoodiaan JavaScriptiksi tai C#:ksi, ajaa sen, ottaa kuvakaappauksen tulosteesta, kirjoittaa 3–5 lauseen reflektion. Palautus O23:n lopussa. O24 on testaus-ja-esityspäivä: kukin opiskelija pitää **2 minuutin** suullisen esityksen, kattaen mitä ohjelma tekee, miten se toimii, sen yhden bugin ja korjauksen. 2 minuutin aikalohko O24:llä on AT3:n suullinen osuus; hyväksytty / ei-vielä-hyväksytty -tarkistus on kuvattu `self-study.md`:ssä ja AT3-briiffaus-tehtävässä molemmissa student-tasks-tiedostoissa.

Työkalut. JavaScript pyörii selaimen DevTools-konsolissa; C# **.NET Fiddlessä** (`dotnetfiddle.net`). Ei asennuksia. Ei automaattisia testaustyökaluja. "Testaaminen" tarkoittaa ajamista käsin kahdella eri alkuarvolla. "Virheenkorjaus" tarkoittaa virheilmoituksen lukemista ja yhden pienen korjauksen soveltamista.

Ristiviitteet. Täydentävää kalvopakettia `slides-l24-presentation-rubric.md` käytetään O24:llä esitysten välillä muistuttamaan 2 minuutin rakenteesta. Pakollinen tuntiaktiviteetti **Show-and-tell loops** kuuluu O22:n aikalohkoon 55–75 min; **AT3-esitykset** on O24:n aikalohko 55–85 min. Molemmat kuvattu tiedostossa `in-class-tasks.md`.

---

## Viikon 8 oppimistavoitteet (yhdistetty Bloomiin)

Viikko 8 pysyy **Soveltamisen** sisällä ja yhdellä **kevyen Arvioimisen** osuudella O24:llä (opiskelija selittää oman valintansa ja vertaa ratkaisuaan vertaisen ratkaisuun). Kiellettyjä verbejä viikon 8 tavoitteissa: *suunnittele, kehitä, rakenna, luo (Bloom-verbinä), analysoi, suunnittele arkkitehtuuri, optimoi, refaktoroi, arvioi, kritisoi*. "Luo tiedosto" arkipäiväisessä merkityksessä on hyväksyttävää — Bloom-tason *Luominen* on rajauksen ulkopuolella. Viikko 8 on konsolidointia.

### Oppitunti 22 — Silmukat koodissa

- **Ymmärtäminen:** opiskelija osaa **tunnistaa** `for`- tai `while`-silmukan koodissa ja **nimetä** neljä osaa: laskuri, ehto, runko, päivitys.
- **Ymmärtäminen:** opiskelija osaa **lukea** 3–6 rivin silmukan ja **ennustaa**, mitä se tulostaa, kummalla tahansa kielellä.
- **Soveltaminen:** opiskelija osaa **kirjoittaa** lyhyen `for`-silmukan, joka pyörii tunnetun määrän kertoja (laske 1–5, tervehdi nimellä kolme kertaa) valitsemallaan kielellä.
- **Soveltaminen:** opiskelija osaa **yhdistää** `REPEAT N TIMES`- tai `WHILE`-rivin viikon 6 pseudokoodistaan toimivaan `for`- tai `while`-silmukkaan koodissa.

### Oppitunti 23 — Pseudokoodista pieneen ohjelmaan

- **Soveltaminen:** opiskelija osaa **valita** yhden palan omaa viikon 6 pseudokoodiaan, joka on oikean kokoinen käännettäväksi (6–20 riviä).
- **Soveltaminen:** opiskelija osaa **kääntää** kyseisen pseudokoodin toimivaksi JavaScript- tai C#-ohjelmaksi, jossa on noin 10–25 riviä, käyttäen käännöstaulukkoa `self-study.md`:stä.
- **Soveltaminen:** opiskelija osaa **ajaa** ohjelman selaimen konsolissa (JS) tai `dotnetfiddle.net`:ssä (C#) ja **vahvistaa** vähintään yhden odotetun tulosteen.
- **Soveltaminen:** opiskelija osaa **tallentaa** lähdekoodin `.js`- tai `.cs`-tiedostona (tai selvästi merkittynä pätkänä AT3-palautukseen liitettynä).

### Oppitunti 24 — Testaa, korjaa yksi bugi, esitä

- **Soveltaminen:** opiskelija osaa **testata** ohjelmaa ajamalla sitä vähintään **kahdella** eri alkuarvolla ja vertaamalla tulostetta ennustukseen.
- **Soveltaminen:** opiskelija osaa **lukea** oikean konsolin tai kääntäjän virheilmoituksen ja **paikantaa** sen rivin, johon se osoittaa.
- **Soveltaminen:** opiskelija osaa **soveltaa** yhtä pientä korjausta ja ajaa uudelleen.
- **Kevyt Arvioiminen:** opiskelija osaa **selittää** ohjelmaa luokalle **2 minuutissa**, kattaen mitä se tekee, miten se toimii, mikä meni vikaan ja miten se korjattiin.
- **Kevyt Arvioiminen:** opiskelija osaa **vertailla** omaa ratkaisuaan vertaisen ratkaisuun (valinnaisesti toisella kielellä) selkeällä suomella — eri valintoja, sama tavoite.

---

## Yleiset virhekäsitykset viikolle 8

Vähintään kaksi virhekäsitystä per oppitunti, kullakin *Correction:* -rivi. Nämä ovat ne, jotka nousevat yleisimmin esiin päätösviikolla; käsittele ne ennen kuin virhekäsitys muodostuu esteeksi AT3:lle.

### Oppitunnin 22 virhekäsitykset

**Virhekäsitys:** *"Silmukka on monimutkainen asia, jonka vain ohjelmoijat ymmärtävät."*
**Correction:** Silmukka on muodollinen nimi sille "toista 3 kertaa" -kuviolle, jota luokka on kirjoittanut pseudokoodissa viikolta 5 lähtien. Ajattelu ei ole muuttunut; syntaksi on ainoa uusi asia. Näytä yksi viikon 6 `REPEAT`-rivi ja sen `for`-silmukkakäännös rinnakkain — yleensä riittävää.

**Virhekäsitys:** *"Tarvitset `while`:n; `for` on edistyneempi."*
**Correction:** Aloittelijoille päinvastoin on totta. `for`-silmukka pakkaa kaikki neljä osaa yhteen siistiin otsikkoon, jossa päivitystä on vaikea unohtaa. `while`-silmukka on riippuvainen siitä, että muistat päivittää laskuria rungon sisällä — klassinen ikuisen silmukan ansa. Suosittele `for`:ia AT3:lle, ellei opiskelijalla ole aidosti "kunnes"-kuvio.

### Oppitunnin 23 virhekäsitykset

**Virhekäsitys:** *"Pseudokoodi ja koodi ovat täysin erilaisia."*
**Correction:** Suurin osa työstä on englanninkielisten sanojen korvaamista kielen syntaksilla — rakenne on jo paikoillaan. Käännöstaulukko `self-study.md`:ssä kattaa kahdeksan yleistä kuviota ja riittää kaikkeen, mitä viikko 6 tuotti. Jos opiskelija väittää pseudokoodinsa olevan "liian erilaista käännettäväksi", istu hänen kanssaan ja ympyröi kunkin rivin osat, jotka ovat kirjaimellisesti samoja: muuttujanimet, numerot, `if`, `else`.

**Virhekäsitys:** *"Jos ohjelmani ei tulosta mitään, jokin on rikki."*
**Correction:** Useammin opiskelija ei painanut Run, tai liitti vain osan ohjelmasta (.NET Fiddle tarvitsee koodia `Main`:in sisällä), tai tulostusrivillä on kirjoitusvirhe (`console.Log` isolla L, `Console.Writeline` pienellä l). `self-study.md`:n osio `## When the screen is empty or silent` luettelee tylsät syyt järjestyksessä.

### Oppitunnin 24 virhekäsitykset

**Virhekäsitys:** *"Virheenkorjaus tarvitsee erikoistyökalun."*
**Correction:** Tällä tasolla virheenkorjaus on viestin lukemista ja yhden rivin muuttamista. Ei erikoisohjelmistoa, ei automatisoitua testaustyökalua. Sano tämä ääneen O24:llä: *"Virheenkorjaus on lukemista ja korjaamista, ei työkaluja."* Edistyneempiä työkaluja on myöhemmillä kursseilla; O24:n harjoitus on tekstin lukemista ja yhden merkin muuttamista.

**Virhekäsitys:** *"Jos ohjelma pyörii, se on oikein."*
**Correction:** Pyöriminen ja oikein oleminen eivät ole sama asia. JS-ohjelma `=`:llä `==`:n sijaan pyörii usein hiljaa ja tulostaa väärän vastauksen. Siksi AT3 vaatii **kaksi** alkuarvoa: toinen ajo pyydystää hiljaisen bugin. Näytä `if (age = 18)` O24:n lämmittelyssä — se pyörii, tulostaa "adult" kaikilla iillä.

**Virhekäsitys:** *"2 minuutin esityksen on oltava ulkoa opeteltu käsikirjoitus."*
**Correction:** Ei sen tarvitse olla. Neljä kohtaa (mitä / miten / mikä meni vikaan / miten korjasin) ovat rakenne, ei käsikirjoitus. Opiskelija, joka seisoo oman avoimen ohjelmansa vieressä ja puhuu omin sanoin, on täsmälleen tavoite. Rubriikkikalvopaketti luettelee, mitä **ei** vaadita: täydellistä koodia, hienoja kalvoja, ulkoa opeteltuja sanoja.

---

## Oppitunti 22 — 90 minuutin suunnitelma

**Aihe.** Silmukat koodissa: `for` ja `while` JavaScriptissä ja C#:ssa rinnakkain, neljä osaa, ikuisen silmukan ansa, viikon 6 pseudokoodin silta.

**Tämän oppitunnin keskeinen viesti (yhdellä lauseella).** Silmukka on muodollinen nimi sille *toista-kunnes*-idealle, jota pseudokoodisi jo käytti — vain nyt toistaja on tietokone, ei ihminen.

| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: laita kaksi viikon 6 pseudokoodin "toista"-riviä taululle (`REPEAT 5 TIMES: print N` ja `WHILE password is too short DO ASK AGAIN`). Kysy luokalta: *"Miltä luulet näiden näyttävän oikeassa koodissa?"* Kerää kolme arvausta; älä korjaa vielä. | Koko luokka |
| 0:10–0:25 | Opettajan luento: käy Ohjelma D (laskuri 1:stä 5:een) läpi JS:ssä ja C#:ssa rinnakkain projektorilla. Aja kumpikin. Nimeä neljä osaa (laskuri, ehto, runko, päivitys) osoittamalla niihin. Sitten näytä `while`-muoto lyhyesti count = 0 / count < 3 -esimerkillä. | Luento |
| 0:25–0:55 | **ITSENÄINEN TYÖ (30 min):** jokainen opiskelija tekee tehtävän 8.2 valitsemallaan kielellä (laske 1–5; käännä 5:stä alas 1:een; tervehdi nimellä kolme kertaa). Kolme pätkää yhteen tiedostoon. Opettaja kiertää. | Itsenäinen |
| 0:55–1:15 | **PAKOLLINEN tuntiaktiviteetti — *Show-and-tell loops*** (Aktiviteetti A tiedostossa `in-class-tasks.md`, ~20 min). Kukin pari (tai sooloopiskelija) ajaa silmukkansa live luokan edessä, lukee tulosteen ääneen ja luokka nimeää neljä osaa yhdelle näytetyistä silmukoista. Sekoitettu JS ja C# tarkoituksella. | Koko luokka |
| 1:15–1:25 | Koko luokan loppukeskustelu: kerää yksi "helppo" ja yksi "outo" hetki per kieli taululle. Nosta esiin ikuisen silmukan vaara kerran — näytä, mitä `i++`:n unohtaminen tekee näytöllä. | Koko luokka |
| 1:25–1:30 | Sulkeminen + O23:n ennakko: *"Huominen on rakennuspäivä. Valitse, minkä viikon 6 pseudokoodin käännät — tuo se paperilla."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 % -säännön.

**Ristiviitteet.** Aikalohko 55–75 min on **Aktiviteetti A — *Show-and-tell loops*** tiedostosta `in-class-tasks.md`. Pidä tehtävä 8.2 valmiina projektorilla varalla, jos opiskelija saapuu ilman kolmea pätkäänsä.

**Kalvovihjeet — pääkalvopaketti `slides.md`.**

- **Lämmittely (0:00–0:10):** kalvo **1** (otsikko) näytöllä, kun taulu kantaa live-keskustelua viikon 6 pseudokoodista.
- **Luento (0:10–0:25):** kalvot **2** (*Mitä tällä viikolla laskeutuu*), **3** (*Silmukat — muoto (JS ja C# rinnakkain)*), **4** (*Laskuri, ehto, runko, päivitys*), **5** (*`while`-silmukka (JS ja C# rinnakkain)*). Viivy kalvolla 4; neljän osan nimeäminen on O22:n kärki.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **3** näytölle hiljaisena viittauksena laskurisilmukalle.
- **Tuntiaktiviteetti (0:55–1:15):** ei kalvoa; live-silmukat huoneessa ovat kalvo.
- **Loppukeskustelu (1:15–1:25):** kalvo **6** (*Kun silmukka pyörii ikuisesti*) laskeuttamaan ikuisen silmukan vaaran.
- **Sulkeminen (1:25–1:30):** ei kalvoja.

---

## Oppitunti 23 — 90 minuutin suunnitelma

**Aihe.** AT3:n rakennuspäivä. Jokainen opiskelija kääntää yhden palan omaa viikon 6 pseudokoodiaan toimivaksi JavaScript- tai C#-ohjelmaksi ja palauttaa lähdekoodin sekä kuvakaappauksen oppitunnin lopussa.

**Tämän oppitunnin keskeinen viesti (yhdellä lauseella).** Pseudokoodin kääntäminen ohjelmointikieleen on enimmäkseen englanninkielisten sanojen korvaamista kielen syntaksilla — rakenne oli jo paikoillaan.

| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: kierros huoneessa, kukin opiskelija nimeää — yhdellä lauseella — viikon 6 pseudokoodin, jonka aikoo kääntää tänään. Opettaja huomaa kaikki, jotka eivät ole vielä valinneet, ja ohjaa heidät tehtävän 8.1 varamalleille. | Koko luokka |
| 0:10–0:25 | Opettajan luento: käännöstaulukko projektorilla. Käy Ohjelma A (ikätarkistus) päästä päähän, pseudokoodi → JS → C#, molemmat kielet rinnakkain. Sitten käy yksi silmukkavariantti (Ohjelma E, tervehdys nimellä kolme kertaa). | Luento |
| 0:25–1:05 | **ITSENÄINEN TYÖ (40 min):** jokainen opiskelija kääntää valitsemansa viikon 6 pseudokoodin valitsemallaan kielellä, ajaa sen, ajaa sen uudelleen toisella alkuarvolla, ottaa kuvakaappauksen. Opettaja kiertää ja vastaa yksilöllisiin kysymyksiin. | Itsenäinen |
| 1:05–1:20 | Paritarkistus: kukin opiskelija näyttää parilleen ohjelmansa ja tulosteen. Pari kysyy kaksi kysymystä: *"Mitä tämä rivi tekee?"* ja *"Mitä muutit kahden ajon välissä?"* Ei korjauksia vielä — se on O24. | Pari |
| 1:20–1:28 | Koko luokan loppukeskustelu: kerää tyypilliset kipupisteet (puolipisteet C#:ssa, iso L vs. pieni l `.Length`/`.length`:ssä, puuttuvat sulkevat aaltosulkeet). Vahvista, että jokaisella on lähdekooditiedosto ja kuvakaappaus tallennettuna. | Koko luokka |
| 1:28–1:30 | O24:n ennakko: *"Huomenna testaat, korjaat yhden bugin ja esität. Tuo lähdekooditiedostosi ja kuvakaappauksesi — ne ovat AT3."* | Koko luokka |

**Itsenäisen työn lohko: 40 minuuttia (44 % 90 minuutista).** Täyttää 30–50 % -säännön.

**Ristiviitteet.** O23:lle ei ole sijoitettu pakollista tuntiaktiviteettia tiedostosta `in-class-tasks.md`. Valinnaista Aktiviteettia C (*Käännöskilpailu*) tiedostosta `in-class-tasks.md` voidaan käyttää aikalohkossa 1:05–1:20 paritarkistuksen sijaan luokille, jotka valmistuvat aikaisin.

**Kalvovihjeet — pääkalvopaketti `slides.md`.**

- **Lämmittely (0:00–0:10):** kalvo **7** (*Pseudokoodistasi ohjelmaksi*) näytöllä, kun opiskelijat nimeävät pseudokoodipalansa ääneen.
- **Luento (0:10–0:25):** kalvo **8** (*Käännöstaulukko*) taulukon läpikäyntiin, sitten lyhyesti takaisin kalvolle **3** (*Silmukat — muoto*), kun silmukkavariantti tulee esiin, ja kalvo **9** (*Silmukka + if/else — salasanan tarkistus*), jos opiskelijan pseudokoodi yhdistää ne.
- **Itsenäinen työ (0:25–1:05):** jätä kalvo **8** (*Käännöstaulukko*) näytölle hiljaiseksi viittaukseksi. Kalvo **10** (*Tallenna, aja, näe tuloste*) itsenäisen lohkon viimeisten viiden minuutin aikana muistuttaa opiskelijoita, miten kuvakaappaus otetaan.
- **Paritarkistus (1:05–1:20):** ei kalvoja; parit katsovat toistensa ohjelmia.
- **Loppukeskustelu (1:20–1:28):** ei kalvoja; käytä taulua kipupistelistalle.
- **O24:n ennakko (1:28–1:30):** ei kalvoja.

---

## Oppitunti 24 — 90 minuutin suunnitelma

**Aihe.** Testaa AT3-ohjelma kahdella alkuarvolla, lue yksi oikea virheilmoitus ja sovella yhtä pientä korjausta, pidä **2 minuutin** suullinen esitys luokassa. Kurssin sulkeminen.

**Tämän oppitunnin keskeinen viesti (yhdellä lauseella).** Virheenkorjaus tällä tasolla tarkoittaa sen lukemista, mitä tietokone kertoi, sen yhden rivin löytämistä, josta se puhui, ja yhden pienen muutoksen tekemistä — erikoistyökaluja ei tarvita.

| Aika | Toiminta | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: laita yksi JavaScript-virhe (`Uncaught ReferenceError: scre is not defined`) ja yksi C#-virhe (`error CS0103: The name 'scre' does not exist in the current context`) taululle rinnakkain. Kysy luokalta: *"Mitä kumpikin kertoo sinulle?"* Päädy lopputulokseen *"molemmat sanovat 'en tiedä, mikä `scre` on' — sinulla on kirjoitusvirhe, jossa tarkoitit `score`:a."* | Koko luokka |
| 0:10–0:25 | Opettajan luento: virheilmoituksen lukeminen (yksi JS, yksi C#, molemmat käyty näytöllä). Yhden-pienen-korjauksen-yhden-uuden-ajon-silmukka nimettynä eksplisiittisesti. Sitten käy **2 minuutin esityksen runko**: neljä kohtaa, ~30 sekuntia kukin — mitä / miten / mikä meni vikaan / miten korjasin. Käytä rubriikkikalvopakettia `slides-l24-presentation-rubric.md` tässä, kokonaisuudessaan. | Luento |
| 0:25–0:55 | **ITSENÄINEN TYÖ (30 min):** jokainen opiskelija testaa ohjelmaansa kahdella eri alkuarvolla, laukaisee tarkoituksella tai vahingossa yhden virheen, lukee viestin, soveltaa yhtä pientä korjausta, viimeistelee 3–5 lauseen reflektion ja harjoittelee 2 minuutin esityksen kerran puhelimen ajastimella. Opettaja kiertää ja vahvistaa kunkin opiskelijan valmiuden. | Itsenäinen |
| 0:55–1:25 | **PAKOLLINEN tuntiaktiviteetti — *AT3-esitykset*** (Aktiviteetti B tiedostossa `in-class-tasks.md`, ~30 min). Kukin opiskelija pitää **2 minuutin** esityksen ohjelmastaan opettajan kutsumassa järjestyksessä. Käytä näkyvää puhelimen ajastinta heijastettuna seinälle. Jokaisen esityksen jälkeen luokka vastaa yhteen vertaispalautekehotteeseen: *"Nimeä yksi asia, jonka huomasit."* | Koko luokka |
| 1:25–1:30 | Kurssin sulkeminen: lue kurssin keskeinen kysymys ääneen kalvolta 18 — *"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"* Kiitä luokkaa. Muistuta opiskelijoita säilyttämään AT3-lähdetiedostonsa; avata se uudelleen puolen vuoden kuluttua. | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 % -säännön.

**Luokkakoko-huomautus.** 30 minuutin esitysaikalohko sopii ~12 hengen luokalle, jossa kullakin on 2 minuuttia plus 30 sekuntia siirtymää. Isommalle luokalle ks. *Facilitation tips* alla kaksi mukautusta (jaa kahteen yhtäaikaiseen ryhmään apuopettajan kanssa, tai kierrätä kahden O24-tyylisen istunnon yli). Palautettu lähdekoodi plus kuvakaappaus kattaa jo kirjallisen osuuden poissaolijoille; suullinen osuus on se, joka tarvitsee live-aikalohkon.

**Ristiviitteet.** Aikalohko 55–85 min on **Aktiviteetti B — *AT3-esitykset*** tiedostosta `in-class-tasks.md`. Tämä **on** AT3:n suullinen osuus. Täydentävä kalvopaketti `slides-l24-presentation-rubric.md` heijastetaan esitysten välillä muistuttamaan 4-kohdan / 2 minuutin rakenteesta.

**Kalvovihjeet — pääkalvopaketti `slides.md` ja täydentävä `slides-l24-presentation-rubric.md`.**

- **Lämmittely (0:00–0:10):** kalvot **11** (*Oikean virheilmoituksen lukeminen (JavaScript)*) ja **12** (*Oikean virheilmoituksen lukeminen (C#)*) rinnakkain projektorilla, kun taulu kantaa live-keskustelua "mitä se kertoo sinulle?".
- **Luento (0:10–0:25):** kalvo **13** (*Yksi pieni korjaus, yksi uusi ajo*) laskeuttamaan virheenkorjaus-on-lukemista-ei-työkaluja -kehyksen, sitten kalvo **14** (*2 minuutin esityksesi*) neljän kohdan rungolle. Sitten siirry täydentävälle kalvopaketille `slides-l24-presentation-rubric.md` ja käy kaikki 4–6 kalvoa päästä päähän, jotta opiskelijat näkevät rubriikin kerran ennen harjoitusta.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **14** näytölle hiljaiseksi viittaukseksi neljälle kohdalle harjoituksen aikana.
- **AT3-esitykset (0:55–1:25):** heijasta täydentävää kalvopakettia `slides-l24-presentation-rubric.md` esitysten välillä rauhallisena muistutuksena; **älä** heijasta kalvoja opiskelijan esityksen päälle. Tiedoston `slides-l24-presentation-rubric.md` läpäisykriteerikalvo on hyödyllisin jätettävä näytölle.
- **Kurssin sulkeminen (1:25–1:30):** kalvo **18** (*Silmukan sulkeminen — viikko 1, vielä kerran*) niin että luokka lähtee sanatarkasti keskeisen kysymyksen kanssa, sitten kalvo **19** (*Kiitos ja mitä seuraavaksi*).

---

## Fasilitointivinkkejä

### 2 minuutin esitysten pitäminen aikataulussa

- **Käytä näkyvää puhelimen ajastinta**, heijastettuna seinälle tai pidettynä opiskelijan ajanottajan toimesta. Näkyvä ajastin itse muokkaa huonetta.
- **Aseta kova katto klo 2:30** pehmeällä kilkutuksella klo 2:00. Opiskelija, joka jatkaa yli 2:30:n, leikataan lempeästi pois — seuraava esittäjä nousee.
- **Tilaa huone ennen aikalohkon alkua.** Etukäteen ilmoitettu järjestys pitää siirtymät 20–30 sekunnissa.
- **Vertaispalautekysymys — *"Nimeä yksi asia, jonka huomasit"* — esitetään kerran per esitys**, koko luokalle. Yksi lyhyt vastaus; ei keskustelua.

### Sellaisen opiskelijan käsittely, jonka ohjelma ei koskaan toiminut

- **Kohdista esitys bugiin, jota hän ei pystynyt korjaamaan, ja siihen, mitä hän kokeili.** Läpäisykriteeri hyväksyy dokumentoidun epäonnistuneen yrityksen — opiskelija nimeää virheilmoituksen ja yrittämänsä korjauksen. Se lasketaan.
- **Pidä sama neljän kohdan rakenne**, mutta viimeisistä kohdista tulee "mikä meni vikaan / mitä yritin".
- **Merkitse ei-vielä-hyväksytty, kun ei ole lainkaan dokumentoitua yritystä.** Tarjoa yhden viikon uudelleen palautusikkuna.

### Kaksikielisen luokan hallinta

- **Ryhmitä JS- ja C#-opiskelijat vierekkäisiin pöytiin** O23:n paritarkistuksen aikalohkossa.
- **Heijasta molemmat kielet rinnakkain jokaisella koodikalvolla.** Visuaalinen rinnakkaisuus tekee puolet työstä.
- **Kun .NET Fiddle on hidas** (jaettu koulun Wi-Fi), salli palautus kotoa — kuvakaappaus plus lähdekoodi kattaa sen; 2 minuutin esitys voidaan pitää ilman live-demoa.

### Ujon esittäjän auttaminen

- **2 minuutin esitys on AT3:n suullinen osuus**, ei-neuvoteltavissa. Mutta muoto on joustava: vakavasti epämukava opiskelija voi esittää pienessä kolmen hengen ryhmässä (opettaja plus kaksi vertaisajia). Neljä kohtaa ovat samat; yleisö on pienempi.
- **Nauhoitetun videon vaihtoehto** tehtävän 8.1 "Jos teet tämän yksin" -osiossa on poissaolijoille, ei tunnilla välttelemiseen.

---

## Vastauksia yleisiin opiskelijoiden kysymyksiin

- *"Voinko käyttää `console.log`:ia vahingossa C#-ohjelmassani?"* — Et; kääntäjä hylkää sen viestillä `error CS0103: The name 'console' does not exist in the current context`. C# käyttää muotoa `Console.WriteLine` (iso C, iso W, iso L). Jos näet CS0103:n sanan `console` pienaakkosilla, tämä on tapahtunut. Lisää iso C.
- *"Miksi C#-ohjelmani sanoo `CS0103`?"* — Kääntäjä ei tunne yhtä käyttämääsi nimeä. Se on lähes aina kirjoitusvirhe: `scre` `score`:n sijaan, `console` `Console`:n sijaan, `Writeline` (pieni l) `WriteLine`:n sijaan. Etsi rivi, jonka viesti nimeää; väärä sana on siinä.
- *"Mitä jos viikon 6 pseudokoodini on liian iso?"* — Valitse yksi osa siitä, joka tekee yhden selkeän työn alusta loppuun (6–20 riviä on optimi). Koko ohjelman ei tarvitse olla siinä. Jos viikon 6 pseudokoodisi puuttuu tai on hukassa, valitse yksi viidestä varamallista tehtävässä 8.1 (ikä, salasana, pisteet, laskuri, tervehdys) ja mukauta arvot omaan kontekstiisi. Se lasketaan AT3:ksi.
- *"Pitääkö minun pitää esitys, jos olen ujo?"* — Kyllä; 2 minuutin suullinen on AT3:n suullinen osuus eikä AT3:a voi läpäistä ilman sitä. Mutta yleisö voi olla pieni (opettaja plus kaksi vertaisajia huoneen kulmassa) ja muoto on keskusteleva — neljä kohtaa ovat rakenne, eivät ulkoa opeteltu käsikirjoitus. Puhu opettajan kanssa O23:lla, jos koko luokalle esittäminen on este.
- *"Voinko käyttää ChatGPT:tä ohjelman kirjoittamiseen?"* — Voit käyttää LLM:ää sparrauskumppanina — esimerkiksi selittämään virheilmoitusta — mutta palauttamasi ohjelman on oltava sellainen, jonka osaat lukea rivi riviltä ja käydä luokan kanssa läpi 2 minuutissa. Opiskelija, joka liittää LLM:n tulosteen ymmärtämättä sitä, jää kiinni esityksessä; neljä kohtaa vaativat opiskelijan nimeämään, mitä kukin rivi tekee. Tehtävässä 8.4 on eksplisiittinen LLM-sparraus-vaihe kehotteella, joka *ei* pyydä korjausta; tämä on tarkoitettu käyttötapa.
- *"Mitä lasketaan 'yhdeksi bugiksi'?"* — Kirjoitusvirhe (väärin kirjoitettu muuttujan nimi), puuttuva puolipiste (C#), puuttuva sulkeva aaltosulje, `=` siellä, missä `==` oli tarkoitettu, isokirjainmissmatch (`length` vs `Length`). Mikä tahansa näistä käy. Bugin on oltava sellainen, jonka osaat nimetä selkeällä suomella; "ohjelmani vain ei toiminut" ei riitä.
- *"Tarvitseeko minun asentaa mitään?"* — Ei. JavaScript pyörii selaimen DevTools-konsolissa (`Cmd + Opt + J` / `Ctrl + Shift + J`). C# pyörii `dotnetfiddle.net`:ssä ilman tiliä. Molemmat ovat samat työkalut, joita käytit viikolla 7.

---

## Formatiivisen arvioinnin vinkkejä

Viikko 8 on viimeinen viikko. Formatiiviset tarkistukset eivät tässä valmistaudu tulevaan arviointiin; ne vahvistavat, että AT3 on raiteilla ja että kurssin keskeiseen kysymykseen on todella vastattu kunkin opiskelijan osalta. Kolme nopeaa tarkistusta viikon yli, plus yksi loppukohta O24:n lopussa.

### Oppituntikohtaiset epäviralliset tarkistukset

- **Oppitunti 22 — poistumislippu (3 min, tunnin lopussa).** Kukin opiskelija kirjoittaa yhdelle riville `for`-silmukan neljä osaa. Laskuri, ehto, runko, päivitys. Lue neljä satunnaisesti ääneen. Luokka, joka nimeää kaikki neljä oikein, on valmis O23:n rakennuspäivään.
- **Oppitunti 23 — vahvistuskierros.** 40 minuutin itsenäisen lohkon aikana opettaja käy jokaisen opiskelijan luona vähintään kerran. Vahvista kaksi asiaa: (a) ohjelma pyöri yhdellä alkuarvolla, (b) kuvakaappaus on olemassa. Opiskelija, joka on jumissa 20 minuuttia itsenäistä työtä, on se, joka tarvitsee väliintuloa, ei se, joka vielä kirjoittaa.
- **Oppitunti 23 — parin raportointi.** Aikalohkon 1:05–1:20 paritarkistuksen lopussa kukin pari antaa yhden havainnon yhdellä lauseella: *"Yksi asia, jonka parini ohjelma tekee hyvin; yksi asia, jonka muuttaisin omassani nähtyäni hänen."* Kuvio läpi huoneen kertoo, osaavatko opiskelijat lukea koodia, joka ei ole heidän omaansa — keskeinen viikon 8 siirto.
- **Oppitunti 24 — valmiustarkistus klo 0:55.** Juuri ennen esitysten alkua, kysy luokalta: *"Käden nostolla, kuinka monella teistä on ohjelma, joka pyörii, kuvakaappaus ja 3 lauseen reflektio valmiina?"* Kädet, jotka eivät nouse, ovat opiskelijoita, joiden luona käyt ensin 30 minuutin itsenäisen lohkon aikana. Kukaan ei esitä ilman kolmea artefaktia kädessä.
- **Oppitunti 24 — yhden minuutin paperi lopussa.** *"Yhdellä lauseella: vastasiko kurssi keskeiseen kysymykseensä sinun osaltasi?"* (*"Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?"*) Tämä on loppukohta. Luokka, jossa useimmat opiskelijat vastaavat "kyllä, ja tässä on ohjelma kädessäni", on saavuttanut kurssin tavoitteen.

### Mitä kuuntelet viikon aikana

O24:n loppuun mennessä kolme lausetta merkitsevät aitoa kurssitason ymmärrystä:

- *"Ohjelmani tekee X ja tässä syy, miksi kukin rivi on siellä"* — sanottuna ilman epäröintiä opiskelijan toimesta, joka esittää omaa ohjelmaansa.
- *"Virheilmoitus sanoi scre — se on rivi, jossa minulla oli `scre` `score`:n sijaan — lisäsin `o`:n ja se toimi"* — bugi-ja-korjaus-tarina, ei mysteeriä.
- *"Se on saman muotoinen C#:ssa kuin JavaScriptissä — käytin vain `int`:iä `let`:n sijaan ja `Console.WriteLine`:a `console.log`:n sijaan"* — kaksikielinen siirto laskeutui.

Jos nuo kolme lausetta esiintyvät opiskelijoiden puheessa O24:llä, kurssi on tehnyt työnsä. 2 minuutin esitysaikalohko on diagnoosi ja juhla samanaikaisesti.
