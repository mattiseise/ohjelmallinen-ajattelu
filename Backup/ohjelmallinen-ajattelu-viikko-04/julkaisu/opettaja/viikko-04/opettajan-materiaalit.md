# Viikko 4 — Opettajan materiaalit

Tämä dokumentti kattaa oppitunnit 10, 11 ja 12 — **ratkaisujen vertailu** -viikon. O10 osoittaa, että yhden ongelman voi ratkaista useammalla kuin yhdellä pätevällä tavalla. O11 nimeää neljä toimivaa kriteeriä: **selkeys · tehokkuus · toistettavuus · virhealttius**. O12 ottaa ne käyttöön jäsennellyssä vertaisarviointi- ja revisiointiprotokollassa viikon 2 ja 3 aikana tehtyihin tuotoksiin.

Viikon 1 sananmukaisen tulkitsijan ajattelutapa, viikon 2 osituksen sanasto ja viikon 3 vuokaaviosanasto pysyvät voimassa. Viikko 4 ei esittele **uutta ohjelmallisen ajattelun primitiiviä**. Sen raaka-aine on opiskelijoilla jo olevat tuotokset. Jos opiskelija saapuu ilman tuotosta, käytä `opiskelijatehtavat.md`:hen painettua varatuotosparia.

Viikko 4 ei tuota **AT-palautusta**. Jokainen tämän viikon tehtävä syöttää **AT2:ta — prosessikuvaus**, joka palautetaan viikon 5 lopussa / viikolla 6. AT2 pyytää eksplisiittisesti itsekorjausvaihetta palautteen jälkeen. Tämä tottumus on täsmälleen se, mitä O12 valmentaa. Vertaisarviointi- ja revisiointisilmukka uudelleenkäytetään myös AT3:ssa (viikko 8).

Ristiinviitteet: oppitunneilla 10 ja 12 käytetyt tuntiaktiviteetit on kuvattu tiedostossa `tuntitehtavat.md`. **Aktiviteetti A — Vertaisarviointi neljällä kriteerillä** (pakollinen) on oppitunnin 12 22–52 min:n aikaikkunassa; **Aktiviteetti B — Vaihteluetsintä** (valinnainen) on oppitunnin 10 55–75 min:n aikaikkunassa.

---

## Viikon 4 oppimistavoitteet (Bloomiin kartoitettuina)

Viikko 4 pysyy **Ymmärtämisen** sisällä, kevyen **Analysoinnin** kanssa kolmessa tietyssä paikassa — O10(d), O11(d) ja O12(b) — joissa opiskelijat *vertailevat kahta ratkaisua kriteeri kerrallaan* tai *tunnistavat heikkouksia kriteerikohtaisesti*. Kielletyt verbit viikon 4 tavoitteissa: *arvioi, tuomitse, arvostele, pisteytä, järjestä, luokittele, päätä kumpi on paras, luo, rakenna, suunnittele, kehitä, debuggaa*. Verbi *vertaa* on kevyttä Analysointia vain silloin, kun se on kriteerillä nimettyä.

### Oppitunti 10 — Sama ongelma, useita ratkaisuja

- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, että samalla ongelmalla voi olla useampi kuin yksi oikea ratkaisu.
- **Ymmärtäminen:** opiskelija osaa **kuvata** tavallisin sanoin, miten kaksi pätevää ratkaisua voi erota vaiheissaan, niiden järjestyksessä tai siinä, mitä ne jättävät käyttäjälle.
- **Ymmärtäminen:** opiskelija osaa **antaa** yhden arkielämän esimerkin ja yhden ICT-esimerkin kahdesta pätevästä ratkaisusta.
- **Kevyt Analysointi:** opiskelija osaa **tunnistaa** vähintään kaksi tapaa, joilla annetut kaksi ratkaisua eroavat toisistaan.

### Oppitunti 11 — Ratkaisujen arviointikriteerit

- **Ymmärtäminen:** opiskelija osaa **määritellä** neljä toimivaa kriteeriä omin sanoin: selkeys, tehokkuus, toistettavuus, virhealttius.
- **Ymmärtäminen:** opiskelija osaa **selittää**, että kriteeri muuttaa *"pidän tästä enemmän"* muotoon *"tämä on parempi X:ssä"*.
- **Ymmärtäminen:** opiskelija osaa **soveltaa** neljää kriteeriä pieneen läpityöstettyyn esimerkkiin.
- **Kevyt Analysointi:** opiskelija osaa **vertailla** kahta ratkaisua kriteeri kerrallaan ja **tunnistaa**, kumpi on vahvempi millä kriteerillä.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, ettei yksittäisen ratkaisun tarvitse voittaa joka kriteerillä — kriteerit voivat vetää eri suuntiin.

### Oppitunti 12 — Oman ratkaisun parantaminen ja vertaispalaute

- **Ymmärtäminen:** opiskelija osaa **soveltaa** neljän kriteerin rubriikkia jäsennellyssä vertaisarviointiprotokollassa parin olemassa olevaan tuotokseen.
- **Kevyt Analysointi:** opiskelija osaa **tunnistaa** vähintään kaksi konkreettista heikkoutta parin ratkaisussa, kriteerillä nimettyinä.
- **Ymmärtäminen:** opiskelija osaa **kirjoittaa uudelleen** yhden omista olemassa olevista viikon 2 tai 3 ratkaisuistaan kahden tietyn vertaispalautteen huomioimiseksi. (Revisio, ei uusi luomus.)
- **Ymmärtäminen:** opiskelija osaa **kuvata** 3–5 lauseessa, mikä muuttui ja miksi, viitaten kuhunkin muutokseen ohjanneeseen kriteeriin.

---

## Yleisiä virhekäsityksiä viikolla 4

Vähintään kaksi oppituntia kohden, kullekin `Korjaus:`-rivi. O11:n (*tehokas = nopea*) ja O12:n (*palaute on kritiikkiä*) ovat yleisimmät; ennakoi molemmat oppitunnin ensimmäisten kymmenen minuutin aikana.

### Oppitunnin 10 virhekäsitykset

**Virhekäsitys:** *"Jos on useampi kuin yksi pätevä ratkaisu, sillä ei ole väliä, minkä valitsen."*
**Korjaus:** Sillä on väliä heti, kun sinulla on nimetty kriteeri. Ilman kriteeriä *"ei ole väliä"* on rehellinen. Kriteerin kanssa — sano vaikka *selkeys ensikertalaiselle tekijälle* — voit perustella valinnan. Tämä viikko on juuri liike *ei kriteeriä → kriteeri*.

**Virhekäsitys:** *"Jos ratkaisuni eroaa opettajan ratkaisusta, omani on varmaan väärin."*
**Korjaus:** Niin kauan kuin ratkaisu saavuttaa tavoitteen ja on selkeästi kirjoitettu, se on **pätevä**. Opettajan ratkaisu on yksi vaihtoehto useiden joukossa. Kerää O10:n lämmittelyssä taululle 2–3 opiskelijoiden vaihtoehtoa *"tee kuppi teetä"*:n tekemiseen tämän osoittamiseksi.

### Oppitunnin 11 virhekäsitykset

**Virhekäsitys:** *"Tehokas = nopea."*
**Korjaus:** Tällä kurssilla *tehokas* tarkoittaa **ei hukattuja vaiheita**. Nopea mutta virhealtis ratkaisu voi silti olla tehokkuudeltaan huono, koska uudelleentyö syö ajan, jonka nopeus säästi. Arkikuva on *"pitkä reitti on joskus nopeampi, koska sitä ei tarvitse tehdä uudelleen"*.

**Virhekäsitys:** *"Hyvä ratkaisu voittaa joka kriteerillä."*
**Korjaus:** Oikeat ratkaisut **kompromisoivat**. Neljä kriteeriä voivat vetää eri suuntiin. *"Resepti A voittaa selkeydessä, Resepti B voi voittaa tehokkuudessa, oikea valinta riippuu tekijästä"* on täydellinen O11-vastaus.

**Bonus-virhekäsitys (esiintyy usein O11:n lopussa):** *"Nuo neljä ovat ainoat olemassa olevat kriteerit."*
**Korjaus:** Laajemmassa maailmassa on monia kriteerejä — kustannus, saavutettavuus, tietoturva. Tällä kurssilla työskentelemme neljällä, koska ne riittävät tottumuksen harjoitteluun.

### Oppitunnin 12 virhekäsitykset

**Virhekäsitys:** *"Palaute on kritiikkiä."*
**Korjaus:** Palaute, joka **nimeää kriteerin**, on informaatiota; ilman kriteeriä se on makua. Protokolla pakottaa kriteerin. *"En vain pitänyt vaiheesta 3"* ei ole palautetta; *"vaihe 3 on epäselvä, koska sana **tiedosto** ei kerro, mistä tiedostosta on kyse"* on.

**Virhekäsitys:** *"Minun pitää toimia jokaisen palautteen mukaan."*
**Korjaus:** Sinun pitää **harkita** jokainen ja kyetä sanomaan, **mihin kriteeriin se viittaa**. Voit perustellusti hylätä palautteen, jos kriteeri ei päde tässä — se itsessään on kriteerillä nimetty vastaus.

---

## Oppitunti 10 — 90 minuutin suunnitelma

**Aihe.** Sama ongelma, useita ratkaisuja.

**Tämän oppitunnin ydinviesti.** Ongelma ei ole sama asia kuin sen ratkaisu; yhden ongelman voi ratkaista monella tavalla, ja sen huomaaminen on hyvin valitsemisen alku.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: kirjoita *"tee kuppi teetä"* taululle. Kerää 2–3 opiskelijoiden vaihtoehtoa. Alleviivaa, mikä on sama ja mikä eri. Lue viikon 4 ydinviesti ääneen ja kirjoita se taulun yläosaan. | Koko luokka |
| 0:10–0:25 | Opettajan input: sano ydinviesti; piirrä *ongelma vs. ratkaisu* kahteen sarakkeeseen; esitä Resepti A ja Resepti B rinnakkain; esitä kaksi varmuuskopiotapaa ICT-vastineena. Arki ennen ICT:tä. | Luento |
| 0:25–0:55 | **ITSENÄINEN TYÖ (30 min):** jokainen opiskelija valitsee yhden tutun arkitehtävän ja kirjoittaa siihen **kaksi pätevää vaihtoehtoista algoritmia** (5–8 vaihetta kumpaankin). Ei vielä kriteerejä — huomaa vain monimuotoisuus. Kynät käteen, ei laitteita. | Itsenäinen |
| 0:55–1:15 | Tuntien pariaktiviteetti: **Aktiviteetti B — "Vaihteluetsintä"** tiedostosta `tuntitehtavat.md`. Parit vaihtavat kahden algoritmin pareja ja tunnistavat **vähintään kaksi tapaa**, joilla parin kaksi ratkaisua eroavat. Roolit vaihtuvat. | Pari |
| 1:15–1:28 | Koko luokan purku: kerää taululle 4–5 *erotapojen lajia* (vaiheiden järjestys; mikä jätetään implisiittiseksi; missä käyttäjän pitää valita; miten ratkaisu kohtelee asioiden menemistä pieleen). Tämä on **O11:n kriteerien siemen**. **Älä** vielä nimeä niitä. | Koko luokka |
| 1:28–1:30 | Yhden rivin esikatsaus oppitunnista 11: *"Huomenna annamme näille eroille nimet."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90:stä).** Täyttää 30–50 %:n säännön.

**Mitä sanot luennolla ääneen.** "Sama tavoite — juotava kuppi teetä — kaksi reseptiä, molemmat toimivat. Ne eroavat **järjestyksessä** (keitä ensin vs. pussi ensin) ja siinä, mitä **jätetään käyttäjälle** (laske kolme minuuttia vs. arvioi väri). Kumpikaan ei ole väärin. Yhdellä ongelmalla voi olla monta pätevää ratkaisua. **Pätevyys** tällä kurssilla tarkoittaa: saavuttaa tavoitteen, sananmukainen tulkitsija voi suorittaa. Mitään *paremmasta*. *Parempi* on seuraavan oppitunnin sana."

**Materiaalit.** Taulu ja tussi; kaksi teereseptiä ja kaksi varmuuskopiotapaa kirjoitettuina tai projisoituina ennen tuntia; paperia itsenäiseen lohkoon. O10:ssä ei käytetä täydentävää kalvosettiä.

**Kalvovinkit — pääkalvosetti `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **1** *(otsikko)* ruudulla opiskelijoiden saapuessa; vaihda kalvoon **2** *(Viikon ydinviesti)* sanasta-sanaan-aloitukseen. Sitten taululle teereseptien vaihtoehtoja varten.
- **Luento (0:10–0:25):** kalvot **3 → 6**: *Missä viikko 4 sijaitsee · Ongelma ei ole sama asia kuin sen ratkaisu · Kaksi tapaa tehdä teetä · Kaksi tapaa varmuuskopioida projektikansio*. Viivy kalvolla 4 — O10:n saranakohta.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **4** ruudulle hiljaisena kehystysmuistutuksena.
- **Aktiviteetti B — Vaihteluetsintä (0:55–1:15):** ei kalvoja; keskustelu tapahtuu parien välillä.
- **Purku (1:15–1:28):** kalvo **7** *(Mikä on sama, mikä eri?)* keräyspohjana; kirjoita luokan *erotapojen lajit* taululle sen viereen.
- **Päätös (1:28–1:30):** ei kalvoja; yksi suullinen rivi esikatselemaan O11:tä.

---

## Oppitunti 11 — 90 minuutin suunnitelma

**Aihe.** Ratkaisujen arviointikriteerit — selkeys, tehokkuus, toistettavuus, virhealttius.

**Tämän oppitunnin ydinviesti.** Kriteeri on nimetty mittapuu — nimeä se, ja *parempi* lakkaa olemasta tunne ja alkaa olla vertailu.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: kertaa *kaksi pätevää ratkaisua* yhdellä opiskelijan tuottamalla parilla O10:stä. Kysy: *"Mikä eilen löytämämme erotapojen laji oli hyödyllisin?"* Kerää yksi vastaus taululle. | Koko luokka |
| 0:10–0:35 | Opettajan input — viikon pisin luentolohko. Sano *maku → kriteeri* -liike. Esittele neljä kriteeriä lukitussa järjestyksessä 2–4 lauseen määritelmällä kustakin ja yhden rivin arki + yhden rivin ICT-esimerkki. Projisoi **täydentävä kalvosetti `kalvot-o11-kriteerien-lapikaynti.md`** läpityöstettyyn esimerkkiin kahdesta teereseptistä. Palaa pääkalvosettiin varmuuskopiotapaesimerkkiä varten. Katkaise 25 minuutin lohko yhdellä opiskelijan ääneen kertomalla esimerkillä puolivälissä. | Luento |
| 0:35–1:05 | **ITSENÄINEN TYÖ (30 min):** jokainen opiskelija ottaa omat O10:n kaksi vaihtoehtoista algoritmiaan ja soveltaa kaikkia neljää kriteeriä neljärivisessä taulukossa. **Ei pyydetä valitsemaan voittajaa.** Yksi lyhyt lause solua kohden. Kynät käteen. | Itsenäinen |
| 1:05–1:22 | Pariaktiviteetti: opiskelijat vaihtavat kriteeritaulukoita ja tarkistavat — *Nimeisikö pari kriteerin joka rivillä? Viittasiko hän tiettyyn vaiheeseen?* Kukin pari kirjoittaa takaisin yhden tai kaksi parannusehdotusta. | Pari |
| 1:22–1:28 | Koko luokan purku: kerää 3–4 paikkaa, joissa kriteerit **vetivät eri suuntiin** (kompromissit). Kirjoita kukin muotoon *"Ratkaisu X voittaa selkeydessä; ratkaisu Y voittaa tehokkuudessa."* Vastusta voittajan kruunaamista. | Koko luokka |
| 1:28–1:30 | Yhden rivin esikatsaus oppitunnista 12: *"Huomenna käytämme näitä neljää kriteeriä toistemme oikeisiin viikon 2 ja 3 tuotoksiin."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90:stä).** Täyttää 30–50 %:n säännön.

**Mitä sanot luennolla ääneen.** "Eilen löysimme eroja. Tänään annamme niille nimet. **Neljä** nimeä — selkeys, tehokkuus, toistettavuus, virhealttius — tässä järjestyksessä. **Selkeys:** sananmukainen tulkitsija voi lukea sen kerran ja tietää, mitä tehdä. **Tehokkuus:** tavoite saavutetaan ilman hukattuja vaiheita. *Tehokas ei ole sama kuin nopea — nopea mutta virhealtis ratkaisu hukkaa uudelleentyöhön enemmän aikaa kuin se säästi.* **Toistettavuus:** sama syöte, sama tulos joka kerta. *'Hieman vettä'* rikkoo toistettavuuden. **Virhealttius:** vaikea tehdä väärää asiaa sen mukaan toimiessa." Käy sitten Resepti A vs. Resepti B läpi kukin kriteeri vuorollaan. Päätä kompromissilauseeseen: *"Resepti A voittaa selkeydessä, Resepti B voi voittaa tehokkuudessa — oikea valinta riippuu siitä, onko tekijä tehnyt tätä ennen."*

**Materiaalit.** Taulu ja tussi; kaksi teereseptiä ja kaksi varmuuskopiotapaa O10:stä yhä näkyvissä; paperia ja viivain kriteeritaulukoihin. Täydentävä kalvosetti `kalvot-o11-kriteerien-lapikaynti.md` projisoidaan läpityöstettyä esimerkkiä varten.

**Kalvovinkit — pääkalvosetti `kalvot.md` + täydentävä kalvosetti `kalvot-o11-kriteerien-lapikaynti.md`.**

- **Lämmittely (0:00–0:10):** pääkalvosetin kalvo **7** *(Mikä on sama, mikä eri?)* O10:n siirtymänä. Sitten taululle opiskelijan tuottamaa esimerkkiä varten.
- **Luento (0:10–0:35):** pääkalvosetin kalvot **8 → 9** *(Mausta kriteeriin · Neljä kriteeriä)* avaavaa kehystystä varten. Kalvosta 9 eteenpäin vaihda **täydentävän kalvosetin `kalvot-o11-kriteerien-lapikaynti.md` kalvoihin (kalvot 1 → 6)** läpityöstettyä esimerkkiä varten Resepti A vs. Resepti B. Sitten takaisin pääkalvosetin kalvoihin **10 → 12** *(Selkeys kahdessa teereseptissä · Tehokkuus kahdessa varmuuskopiotavassa · Toistettavuus ja virhealttius)* ICT-vastinetta varten. Päätä pääkalvosetin kalvolle **13** *(Kompromissit)*.
- **Itsenäinen työ (0:35–1:05):** jätä pääkalvosetin kalvo **9** *(Neljä kriteeriä)* ruudulle hiljaisena muistutuksena neljästä nimestä ja lukitusta järjestyksestä.
- **Pariaktiviteetti (1:05–1:22):** ei kalvoja; keskustelut kriteeritaulukoista.
- **Purku (1:22–1:28):** kalvo **13** *(Kompromissit)* keräyspohjana; kompromissilauseet menevät taululle.
- **Päätös (1:28–1:30):** ei kalvoja; yksi suullinen rivi esikatselemaan O12:ta.

---

## Oppitunti 12 — 90 minuutin suunnitelma

**Aihe.** Oman ratkaisun parantaminen vertaispalautteen avulla. Pakollinen tuntiaktiviteetti (vertaisarviointiprotokolla) asuu tällä oppitunnilla.

**Tämän oppitunnin ydinviesti.** Palaute, joka nimeää kriteerin, on palautetta, jonka mukaan voi toimia; palaute, joka ei, on makua valeasussa.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: kirjoita kolmivaiheinen protokolla taululle isoin kirjaimin — **kriteerit → palaute → revisio**. Muistuta opiskelijoita ottamaan esiin viikon 2 ositus tai viikon 3 vuokaavio. Unohtaneille jaa varatuotospari `opiskelijatehtavat.md`:stä. | Koko luokka |
| 0:10–0:22 | Opettajan input: lyhyet läpikäynnit aiheista *Palaute, jota joku voi todella käyttää* (nimeä kriteeri; yksi konkreettinen kohta; kritisoi tuotosta, älä ihmistä) ja *Palautteen vastaanottaminen, kun et ole samaa mieltä* (harkitse jokainen; voit hylätä, jos kriteeri ei päde). Kaksitoista minuuttia. Älä pitkitä. | Luento |
| 0:22–0:52 | Tunnin opettajavetoinen aktiviteetti: **PAKOLLINEN Aktiviteetti A — "Vertaisarviointi neljällä kriteerillä"** tiedostosta `tuntitehtavat.md`. Hiljainen lukeminen → kriteerikierros → valitse kaksi → vaihto ilman puolustamista -kyselytuokio. Opettaja kiertää ja valvoo *makua → kriteeri* -liikettä reaaliajassa. Yksinäiset opiskelijat pariutuvat opettajan kanssa. | Pari |
| 0:52–1:22 | **ITSENÄINEN TYÖ (30 min):** jokainen opiskelija korjaa omaa viikon 2 / viikon 3 tuotostaan **yhden** kahdesta parin palautteesta perusteella ja kirjoittaa 3–5 lauseen muutosmuistion. Viiden sanan muutos voi olla täsmälleen pointti. Kynät käteen. | Itsenäinen |
| 1:22–1:28 | Koko luokan purku: kolme vapaaehtoista jakavat, mikä muuttui ja mikä kriteeri ohjasi muutosta. Kuuntele kriteerin nimeä — *"selkeys vaiheessa 3"*, *"virhealttius vinoneliössä"*. Silta AT2:een. | Koko luokka |
| 1:28–1:30 | Yhden rivin esikatsaus viikosta 5 (*if / then / else*) ja AT2-muistutus: *"AT2 osuu viikon 5 lopulle / viikolle 6, ja se pyytää täsmälleen tätä silmukkaa omaan työhösi."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90:stä).** Täyttää 30–50 %:n säännön.

**Mitä sanot luennolla ääneen.** "Oma työ on vaikeinta lukea selvästi — muistat, mitä **tarkoitit**, joten et voi nähdä, mitä **kirjoitit**. Neljä kriteeriä ovat tapa lukea se **jonkun toisen silmin**. Tänään silmät ovat oikeat: parisi. Kolme vaihetta. Lue ensin hiljaa — ei selittämistä. Kirjoita yksi lause kriteeriä kohden lukitussa järjestyksessä. Valitse kaksi hyödyllisintä. Anna ne pois. **Vain selventäviä kysymyksiä, ei puolustamista.** Sitten sinulla on jotain, mihin tarttua. Korjaat yhden asian — et kaikkea — ja kirjoitat kolmesta viiteen lausetta nimeten, mikä muuttui ja miksi. *Miksi* nimeää kriteerin. Tämä on se silmukka, jota AT2 pyytää sinua ajamaan omaan työhösi kahden viikon kuluttua."

**Materiaalit.** Taulu ja tussi; kolmivaiheinen protokolla esikirjoitettuna taululle ennen kuin opiskelijat saapuvat; **varatuotospari tulostettuna opettajan pöydällä** (vähintään 4 kopiota); paperia kriteerilauseille ja muutosmuistiolle. O12:ssä ei käytetä täydentävää kalvosettiä.

**Kalvovinkit — pääkalvosetti `kalvot.md`.**

- **Lämmittely (0:00–0:10):** kalvo **14** *(Vertaisarviointiprotokolla)* hiljaisena muistutuksena; taulu kantaa tilan version isoin kirjaimin.
- **Luento (0:10–0:22):** kalvo **15** *(Palaute, jota joku voi käyttää)* kolmen säännön esitykseen; pysy kalvolla 15 koko kaksitoista minuuttia.
- **Aktiviteetti A — Vertaisarviointi neljällä kriteerillä (0:22–0:52):** jätä kalvo **14** ruudulle hiljaisena protokollamuistutuksena. Ei muita kalvoja — parikeskustelu on oppitunti.
- **Itsenäinen työ (0:52–1:22):** jätä kalvo **14** päälle taustaksi; taulu kantaa tilan muistutuksen.
- **Purku (1:22–1:28):** kalvo **16** *(Viikon tehtävät)* kehystyksenä — vapaaehtoisten muutosmuistiot näyttävät must-do-minimum-tehtävän lennossa.
- **Päätös (1:28–1:30):** kalvo **17** *(Mitä seuraavaksi: Viikko 5)* yhden rivin esikatseluun ja AT2-muistutukseen, ja päätä kalvolle **18** *(Kertaus — viikon ydinviesti)*.

---

## Fasilitointivinkit

- **Valvo *maku → kriteeri* -liikettä.** Jokainen *"pidän tästä vain enemmän"* palautetaan lempeästi muotoon *"millä kriteerillä?"*. Jokainen *"oikea vastaus on…"* saa *"…millä kriteerillä?"*. Viikon yksittäinen tärkein fasilitointiliike.
- **Vastusta voittajan kruunaamista.** Molemmat teereseptit toimivat. Molemmat varmuuskopiotavat toimivat. Pointti on *miten ne eroavat*. Jos opiskelija vaatii *"mutta A on vain parempi"*, kysy *"parempi millä kriteerillä, ja mille tekijälle?"*.
- **Ei numeerista pisteytystä. Koskaan.** *"4/5 selkeydessä"* ei ole sallittu. *"Selkeämpi vaiheessa 5"* on. Kriteerit ovat **kuvailevia linssejä**, eivät arvostelurubriikki. Jos opiskelijat tarttuvat numeroihin, vaihda sanoiksi.
- **O11:ssä luentolohko on poikkeuksellisen pitkä (25 min).** Katkaise se yhdellä opiskelijan ääneen kertomalla esimerkillä puolivälissä — pyydä opiskelijaa lukemaan O10:n *kaksi pätevää ratkaisuaan* ja vie luokka läpi, miten *selkeys* soveltuu kunkin vaiheeseen 3.
- **O12:ssa parit, jotka jumittuvat *"minulla ei ole palautetta"* -tilaan, herätetään kriteerilistalla.** *"Käy läpi selkeys, tehokkuus, toistettavuus, virhealttius järjestyksessä. Yksi lause kriteeriä kohden."*
- **Parityön epäonnistumistila.** Pariuta yksinäinen opiskelija **opettajan** kanssa, ei toisen yksinäisen kanssa. Jos parityö on sinä päivänä perustavanlaatuisesti mahdotonta, vaihda tehtävä 4.2 suunnitelmasta (*"Kaksi teereseptiä, neljä kriteeriä"*) must-do-minimumin korvikkeeksi.
- **Varatuotospari pöydällä ennen O12:ta.** Vähintään 4 kopiota. Anna yksi jokaiselle tyhjäkätiselle opiskelijalle 0:00–0:10, ei 0:22.
- **Puolivälin pulssitarkistus — nosta esiin, mutta älä päästä raiteilta.** O12 on luonnollinen hetki kysyä *"mikä viikoilta 1–3 tuntuu yhä epävarmalta?"*. Merkitse muistilappuun; **älä** avaa keskustelua O12:ssa. Viikon 4 on päätyttävä vertaisarviointi- ja revisiointitottumukseen, ei viikkojen 1–3 kertaukseen.

---

## Vastauksia opiskelijoiden yleisiin kysymyksiin

- *"Mitä jos kaksi ratkaisuani ovat periaatteessa samanlaisia?"* — Sitten ne eivät ole oikeasti kaksi ratkaisua. Vaadi eroja vaiheiden järjestyksessä, siinä mitä jätetään implisiittiseksi, tai siinä kenen pitää valita. Niiden on erottava **jossakin, mitä sananmukainen tulkitsija huomaisi**.

- *"Mikä kriteeri on tärkein?"* — Yksikään abstraktilla tasolla. Tärkein kriteeri riippuu **tilanteesta**. Aivan uudelle ICT-harjoittelijalle selkeys on yleensä ratkaiseva. Help desk -makrolle, joka laukeaa tuhat kertaa päivässä, tehokkuus voi olla. **Kompromissin nimeäminen on vastaus**, ei mestarin valinta.

- *"Onko vertailuun oikeaa vastausta?"* — On oikea vastaus **heti kun nimeät kriteerin**. *"Kumpi on selkeämpi vaiheessa 3?"* on oikea vastaus. *"Kumpi on parempi resepti?"* ilman kriteeriä ei — se on makua.

- *"Mitä jos parin palaute on väärä?"* — Sano, mihin kriteeriin se viittaa, ja sano, **miksi se ei mielestäsi päde tässä**. Se on vastaus. *"Toimi jokaisen palautteen mukaan"* ei ole tavoite; *"harkitse jokainen ja nimeä kriteeri, jota vasten punnitsit sen"* on.

- *"Tarvitsenko mihinkään näistä tietokonetta?"* — En. Viikko 4 on paperia, taulua ja keskustelua. Tuomasi tuotokset ovat ne, jotka piirsit viikoilla 2 ja 3. Laitteita ei tarvita.

- *"Voinko käyttää ChatGPT:tä vertailuun?"* — Vain sparrauskumppanina SYVENTÄVISSÄ tehtävissä. PAKOLLINEN työ on **oma tuotoksesi** ja **oikean parin palaute**. LLM ei voi ajaa oikean parin kanssa käytävää edestakaista keskustelua.

- *"Mitä jos minulta jäi viikko 2 tai 3 väliin?"* — Käytä `opiskelijatehtavat.md`:n lopussa olevaa varatuotosparia. Valitse yksi; kerro parillesi, että käytät varatuotosta. Varatuotokset ovat tahallisesti karkeita — arvioija löytää niistä kriteerillä nimettyjä heikkouksia alle viidessä minuutissa.

---

## Formatiiviset arviointivinkit

Viikolla 4 ei ole **summatiivista hetkeä**. Alla olevat tarkistukset ovat formatiivisia — ne tekevät ymmärtämisen näkyväksi, jotta virhekäsityksiä voidaan korjata ennen kuin AT2 alkaa viikolla 5. Käytä yhtä tai kahta oppituntia kohden; älä käytä kaikkia.

### Oppituntikohtaiset epämuodolliset tarkistukset

- **O10:n exit ticket (2 min).** *"Kaksi pätevää ratkaisua samaan ongelmaan voivat erota [X]:ssä ja [Y]:ssä."* Jos yli kolmannes kirjoittaa pelkästään *"järjestys"*, kertaa *"mitä jätetään käyttäjälle"* ja *"miten kohtelee asioiden pieleen menemistä"* O11:n alussa.
- **O10/O11:n taululla äänestäminen.** Kolme lausetta: (a) *"Jos kaksi ratkaisua saavuttavat tavoitteen, vain yksi on oikea."* (b) *"Jos kaksi ratkaisua saavuttavat tavoitteen, molemmat ovat päteviä."* (c) *"Lyhyempi on parempi."* Vahva (a)- tai (c)-ääni tarkoittaa, että pätevyys-vs-kriteeri-liike ei ole iskenyt.
- **O11:n nimeä-neljä (2 min).** Jokainen opiskelija kirjoittaa neljä kriteerinimeä muistista, järjestyksessä. Jos yli kolmannes unohtaa yhden (yleensä virhealttiuden tai toistettavuuden), kertaa O12:n alussa — sama lukittu järjestys.
- **O11:n minuutin paperi.** *"Kuvaile yksi kompromissi, jonka löysit tänään."* Kuuntele kriteerinimiä heidän kirjoituksissaan.
- **O12:n parien raportointi.** Kaksi paria raportoivat yhden antamansa palautteen. Kuuntele kriteerinimeä ja tiettyä vaihetta. Jos kriteeri puuttuu, kysy *"millä kriteerillä?"* luokan edessä — mallinna liike ääneen.
- **O12:n exit ticket.** *"Mikä kriteeri ohjasi revisiotasi tänään, ja mitä muutit?"* Epämääräiset vastaukset (*"tein siitä selkeämmän"*) merkitsevät saman aukon kuin puuttuva *selkeys vaiheessa X*.

### Puolivälin pulssitarkistus (valinnainen, sopii O12:n päätökseen vain jos aikaa on)

Muistilappujen kerääminen aivan O12:n lopussa. Jokainen opiskelija kirjoittaa joko *"Yksi asia viikoilta 1–3, joka tuntuu yhä epävarmalta"* tai *"Yksi asia, jossa nyt tunnen olevani vahva"*. Lue kolme kummastakin ääneen. Merkitse epävarmat viikon 5/6 kertausta varten — **älä** avaa keskustelua O12:ssa.

### Mitä kuuntelet viikon yli

Kolme lausetta, jotka merkitsevät aitoa ymmärtämistä viikon 4 loppuun mennessä:

- *"Molemmat ratkaisut saavuttavat tavoitteen — ne eroavat …"* (eikä *"tämä on oikea"*).
- *"Ratkaisu A voittaa selkeydessä; ratkaisu B voittaa tehokkuudessa — se riippuu tekijästä."* (eikä *"A on parempi"*).
- *"Muutin vaihetta 3 selkeyden vuoksi — pari huomautti, että …"* (eikä *"tein siitä paremman"*).

Jos nuo kolme lausetta ilmestyvät opiskelijoiden puheeseen oppitunnin 12 loppuun mennessä, viikko 4 on tehnyt työnsä ja viikko 5 voi rakentaa luokan päälle, joka osaa lukea omaa työtään ja korjata sitä.
