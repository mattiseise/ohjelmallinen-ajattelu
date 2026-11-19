# Kolme liikettä: sekvenssi, ehto, toisto

## Johdanto

Heräät. Tarkistat puhelimesi. Jos kello on yli 7:30, jätät aamupalan väliin; muuten syöt. Sitten kävelet kouluun. Matkalla tarkistat jokaisen liikennevalon: jos se on punainen, pysähdyt; jos vihreä, jatkat eteenpäin. Toistat tätä jokaisella suojatiellä, kunnes olet portilla.

Tuo lyhyt kappale kuvaa todellista aamua. Se käyttää samoja kolmea liikettä, joita jokainen koskaan kirjoitettu ohjelma käyttää. Kävit läpi *vaiheita järjestyksessä* (heräät, sitten tarkistat puhelimen, sitten kävelet kouluun). Teit *päätöksiä* (yli 7:30 vai ei? punainen vai vihreä?). Ja *toistit* saman tarkistuksen yhä uudestaan, jokaisella suojatiellä, kunnes näit lopetuksen (saavuit portille).

Näillä kolmella liikkeellä on lyhyet, selkeät nimet: **sekvenssi**, **ehto** ja **toisto**.

> **Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto.** Kun osaat nimetä nämä arkisissa tehtävissä, sinulla on jokaisen ohjelman luuranko.

Tämä on viikon keskeinen viesti. Viikko 1 sanoi, että tietokone on sananmukainen tulkitsija, ei nokkela. Viikot 2 ja 3 sanoivat, että isot ongelmat voidaan pilkkoa ja kuvata prosesseina. Viikko 4 sanoi, että "oikein" voi tarkoittaa useampaa kuin yhtä asiaa. Viikko 5 antaa nimen niille kolmelle rakenteelliselle liikkeelle, jotka ovat jokaisen kuvatun prosessin sisällä — niin että ensi viikolla, kun alat kirjoittaa jotain lähempänä koodia (nimeltään *pseudokoodi*), liikkeet ovat jo tuttuja.

Tämä viikko pysyy selkokielessä. Koodia ei vielä ole. Kirjoitat ehtoja muodossa `if … then … else …` ja toistoja muodossa `for each …` tai `repeat until …`, mutta nämä ilmaukset ovat selkokielistä lyhennemerkintää, eivät ohjelmointikieltä. Ajattelu on tällä viikolla tärkeintä.

**AT2-yhteys.** AT2 palautetaan viikon 5 lopussa / viikon 6 aikana. Se pyytää sinua kuvaamaan valitsemasi prosessin luonnollisella kielellä siten, että kaikki kolme rakennuspalikkaa näkyvät. Must-do minimum -tehtävä tiedostossa `opiskelijatehtavat.md` on juuri tämä tuotos pienemmässä mittakaavassa. Säilytä muistiinpanot jokaiselta oppitunnilta — ne ovat AT2:n raaka-ainetta.

---

## Oppitunti 13 — Sekvenssi: ohjelma etenee vaihe vaiheelta

### Mitä sekvenssi tarkoittaa

**Sekvenssi** on yksinkertaisin kolmesta rakennuspalikasta: *yhden vaiheen tekeminen toisensa perään, kiinteässä järjestyksessä, ellei ohje toisin sano.* Tuo viimeinen kohta on tärkeä. Sekvenssi on **oletusarvo**. Kun mitään ehtoa ei ole kirjoitettu eikä mitään toistoa ole kirjoitettu, sananmukainen tulkitsija vain käy vaiheet läpi ylhäältä alas ja tekee jokaisen täsmälleen kerran.

Jos sekvenssi kuulostaa liian itsestäänselvältä ollakseen "rakennuspalikka", se on hyödyllinen varoitusmerkki. Suurin osa todellisista kuvattujen prosessien virheistä — epäonnistuvat reseptit, vialliset käyttöönotot, aamurutiinit, jotka jättävät sinut juoksemaan bussille — johtuu yhdestä vaihdetusta tai yhdestä puuttuvasta vaiheesta. Sekvenssi on oletusarvo, ja oletusarvossa asiat menevät rikki.

### Sekvenssi arkisissa prosesseissa

Tässä on pieni algoritmi, jonka osaat jo: teemukin valmistus.

1. Täytä vedenkeitin vedellä.
2. Kytke keitin päälle.
3. Laita teepussi mukiin.
4. Odota, että vesi kiehuu.
5. Kaada kiehuva vesi mukiin.
6. Anna teepussin hautua kolme minuuttia.
7. Poista teepussi.
8. Lisää maitoa, jos haluat.

Tämä on sekvenssi: kahdeksan numeroitua vaihetta, kukin selkeä toiminta, kiinteässä järjestyksessä. Sananmukainen tulkitsija, jolla ei ole kokemusta teen valmistuksesta, voisi silti päätyä juotavaan kuppiin, jos hän seuraisi tätä täsmälleen.

Kokeile nyt ajatuskoetta. Vaihda vaiheet 4 ja 5 — *kaada kiehuva vesi mukiin*, sitten *odota, että vesi kiehuu*. Mitä tapahtuu? Tulkitsija kaataa kylmää vettä mukiin ja jää katsomaan jo tyhjää keitintä, jossa ei ole mitään kiehutettavaa. Ohje ei ole enää teeresepti; se on sekava liikkeiden joukko. Pointti: **se järjestys, jonka kirjoitit, on se järjestys, jonka tulkitsija saa**. Sekvenssi ei takaa, että prosessi toimii — se takaa sen, että tulkitsija ei hiljaa järjestele vaiheitasi uudelleen.

Jotkin sekvenssin vaiheet voidaan vaihtaa rikkomatta mitään. Voit harjata hampaat ennen pukeutumista tai sen jälkeen — kummassakin järjestyksessä päädyt samaan aamukuntoiseen sinuun. Toisia vaiheita ei voi vaihtaa. Et voi kaataa teetä ennen kuin keität veden; et voi syödä kakkua ennen kuin paistat sen. Sanomme, että niillä vaiheilla, joita ei voi vaihtaa, on **riippuvuus**: myöhempi vaihe tarvitsee aiemman vaiheen tuloksen voidakseen suorittua.

Sinun ei tarvitse tällä viikolla analysoida riippuvuuksia muodollisesti. Riittää, että *huomaat* ne ja kirjoitat sekvenssisi järjestyksessä, joka kunnioittaa tunnistamiasi riippuvuuksia.

### Sekvenssi ICT-kontekstissa — käyttöönottolista

Tässä sekvenssi ammatillisen ICT:n maailmasta: yksinkertaistettu *käyttöönottolista* — vaiheet, joita pieni tiimi voisi seurata viedäkseen uuden version verkkosivustaan käyttäjille.

1. Yhdistä uusi haara pääkehitysharaan.
2. Aja build.
3. Aja smoke-testit.
4. Vie staging-ympäristöön.
5. Ilmoita tiimille chatissa.
6. Odota toisen henkilön hyväksyntä.
7. Vie tuotantoon.
8. Tarkkaile dashboardia kymmenen minuuttia.

Tämä on samaa muotoa kuin teeresepti: numeroitu lista selkeitä toimintoja kiinteässä järjestyksessä. Useita vaiheita ei voi järjestää uudelleen rikkomatta prosessia. Et voi ajaa buildia ennen mergeä — ei ole mitään uutta rakennettavaa. Et voi viedä tuotantoon ennen hyväksyntää — sehän on hyväksynnän *tarkoitus*. Käyttöönottolista on sekvenssi, jota pitävät koossa sen riippuvuudet.

Huomaa, miten arkinen ja ICT elävät tässä rinnakkain. *Keitä vesi → kaada vesi* on samaa muotoa kuin *aja build → aja smoke-testit*. Arkinen versio tuli ensin, koska se oli tutumpi; ICT-versio on sama idea eri ympäristössä. Näin loppuviikko etenee: arkinen esimerkki ensin, sitten ammatillinen peilikuva.

### Riippumattomuus vs. riippuvuus — pehmeä johdatus

Vielä kaksi pientä esimerkkiä eron tuntemiseen.

- **Kaksi vaihetta, jotka eivät riipu toisistaan.** "Harjaa hampaat" ja "pue kengät" voivat tapahtua kummassakin järjestyksessä aamurutiinissa. Niiden välillä ei ole riippuvuutta.
- **Kaksi vaihetta, jotka riippuvat.** "Avaa tiedosto" ja "tallenna tiedosto" riippuvat toisistaan. Et voi tallentaa sitä, mitä et ole avannut.

Sinun ei tarvitse piirtää riippuvuuskaaviota. Tällä viikolla harjoituksena on vain *kirjoittaa se järjestys, jonka tarkoitat*, ja olla itsesi kanssa rehellinen silloin, kun vaiheen on tultava ennen toista, koska se valmistelee jotain, mitä myöhempi vaihe tarvitsee.

> **Pysähdy hetkeksi:** Kirjoita ylös kolmen vaiheen arkiprosessi, jossa järjestys voidaan vaihtaa, ja toinen kolmen vaiheen prosessi, jossa sitä ei voi vaihtaa. Millä yhdellä sanalla kuvailisit eron näiden kahden välillä?

---

## Oppitunti 14 — Ehdot: if-then-else -ajattelu ja päätöspuut

### Mikä ehto on

**Ehto** on testi, joka päättää, mikä vaihe tapahtuu seuraavaksi. Se on se prosessin hetki, jolloin polku jakautuu.

Sekvenssi itsessään on suora viiva: tee A, sitten B, sitten C. Ehto lisää haaran: tee A, sitten **jos X on tosi** tee B, **muuten** tee C. Tulkitsijan näkökulmasta ehto on se hetki, jolloin hän pysähtyy, tarkistaa testin ja valitsee haaran.

### Arkiset ehdot, joita käytät jo

Käytät ehtoja joka päivä, yleensä nimeämättä niitä.

- *"Jos sataa, mene bussilla; muuten kävele."* — kaksihaarainen ehto (`if … then … else …`).
- *"Jos saat läksyt valmiiksi ennen päivällistä, voit pelata."* — yksihaarainen ehto (`if … then …`). Jos läksyt eivät ole valmiina ennen päivällistä, sääntö ei sano mitään ylimääräistä; tulkitsija ei tee mitään ylimääräistä.
- *"Jos maito haisee, heitä se pois."* — toinen yksihaarainen ehto. Jos maito haisee hyvältä, et tee asialle mitään; jätät sen rauhaan.

Ero *if … then …* (ei `else`) ja *if … then … else …* (jossa on `else`) välillä on pieni mutta todellinen. Ilman `else`-haaraa tulkitsijalla on vain yksi ylimääräinen asia, jonka hän saattaa tehdä — "then" — ja jos testi epäonnistuu, hän vain jatkaa eteenpäin. `else`-haaran kanssa tulkitsija tekee aina jommankumman; `else` nimeää vaihtoehdon.

### Ehdon kirjoittaminen luonnollisella kielellä

Voit kirjoittaa ehdot samassa rennossa muodossa läpi loppuviikon. Muodot näyttävät englannilta vähäisellä asettelulla:

> **if** *sataa*, **then** *mene bussilla*, **else** *kävele*.

> **if** *maito haisee*, **then** *heitä se pois*.

Nämä eivät ole koodia. Ne ovat englanninkielistä lyhennemerkintää. Sanat *if*, *then* ja *else* tekevät samaa työtä kuin välimerkit — ne helpottavat näkemään, missä testi loppuu ja toiminta alkaa. Pidä ne pienikirjaimisina tai kursivoituna; älä vielä muuta niitä ohjelmointikieleksi tiukkoine sääntöineen (se on viikon 6 asia).

Hyvällä ehdolla on kolme rehellistä osaa:

1. **Testi, jonka tulkitsija pystyy oikeasti tarkistamaan.** *"Sataako nyt?"* — kyllä tai ei. *"Onko salasana lyhyempi kuin 8 merkkiä?"* — kyllä tai ei.
2. **then-haara** — mitä tehdä, kun testi on tosi.
3. **else-haara** *(valinnainen)* — mitä tehdä, kun testi on epätosi. Jos et kirjoita else-haaraa, sanot "ei mitään ylimääräistä muutoin"; varmista, että se oli juuri se, mitä tarkoitit.

### Päätöspuut — jakautumisen piirtäminen

**Päätöspuu** on yksinkertaisesti kuva ehdosta. Se laittaa testin huipulle ja piirtää haarat alaspäin.

Säännölle "jos sataa, bussi; muuten kävele":

```
        Sataako?
        /        \
      kyllä       ei
      /            \
mene bussilla   kävele
```

Tämä on kaksihaarainen puu. Voit myös tehdä kolmihaaraisen lisäämällä `else if`:

```
                 Sataako?
                 /        \
               kyllä        ei
               /              \
       mene bussilla     Oletko myöhässä?
                                /        \
                              kyllä        ei
                              /              \
                           juokse          kävele
```

Et tarvitse mitään erityisohjelmistoa päätöspuun piirtämiseen. Kynä ja muistivihon kulma riittää. Päätöspuun hyöty ei ole piirtämisessä — se on siinä keskustelussa, johon se sinut pakottaa itsesi kanssa. Kun joudut laittamaan testin jokaiseen haaraan, huomaat ne haarat, joissa et ole ollut rehellinen sen suhteen, mikä testi oikeasti on.

### Ehdot ICT-kontekstissa — salasanan tarkistus

Kuvittele rekisteröitymislomake verkkosivulla. Kun klikkaat *luo tili*, järjestelmä tarkistaa salasanasi sääntöjoukkoa vasten. Tässä yksinkertaistettu versio säännöistä selkokielellä:

- **if** salasana on lyhyempi kuin 8 merkkiä, **then** hylkää se.
- **if** salasanassa ei ole numeroa, **then** hylkää se.
- **if** salasanassa ei ole isoa kirjainta, **then** hylkää se.
- **muutoin** hyväksy se.

Tämä on ketju kolmesta ehdosta ja yksi else-haara — yhteensä neljä haaraa, jotka päättyvät kahteen mahdolliseen lopputulokseen (hylkää, hyväksy). Voit piirtää sen päätöspuuna, jossa kukin testi vuorollaan on uuden solmun huipulla:

```
                Onko se lyhyempi kuin 8 merkkiä?
                 /                       \
               kyllä                       ei
               /                            \
            hylkää             Puuttuuko numero?
                                   /                  \
                                 kyllä                  ei
                                  /                     \
                               hylkää       Puuttuuko iso kirjain?
                                                  /                  \
                                                kyllä                  ei
                                                 /                     \
                                              hylkää                hyväksy
```

Huomaa, että tämä on samaa muotoa kuin "jos sataa, bussi; muuten jos olet myöhässä, juokse; muuten kävele." Ympäristö on eri — salasanat säätilan sijaan — mutta *muoto* on sama: testien ketju, jossa jokainen reitittää joko lopulliseen vaiheeseen tai uuteen testiin. **Sama muoto, eri ympäristö.** Tämä on oppi.

### Yhdistetyt ehdot — AND, OR *(syventävää lukemistoa, valinnainen)*

Joskus yhdessä ehdossa on enemmän kuin yksi testi sisällään. Käytät näitä joka päivä, selkokielellä:

- *"Jos sinulla on bussikortti **ja** siinä on rahaa, voit mennä bussilla."* — kaksi testiä yhdistetty AND-sanalla. Kummankin on oltava tosi.
- *"Jos sataa **tai** tuulee kovaa, mene bussilla."* — kaksi testiä yhdistetty OR-sanalla. Joko toisen olla tosi riittää.

Yhdistettyjä ehtoja on aivan hyvä käyttää selkokielellä. Et tarvitse mitään symboleja (et näe `∧` tai `||` missään tämän kurssin aikana tänä vuonna). Sanat *ja* ja *tai* tekevät täsmälleen sen työn, jonka ne tekevät tavallisissa lauseissa. Jos yhdistetty ehto alkaa tuntua ahtaalta — sano vaikka *"jos A ja B tai C ja ei D"* — se on merkki siitä, että se kannattaa kirjoittaa uudelleen pieneksi puuksi useilla lyhyemmillä testeillä, yksi per haara.

> **Pysähdy hetkeksi:** Kirjoita ylös yksi sääntö, jota joku perheessäsi käyttää kanssasi ja joka on muotoa *if … then … else …*. Mikä on testi? Voisiko testi epäonnistua rehellisyydessä — voisivatko kaksi sen lukijaa olla eri mieltä siitä, onko se tosi?

> **Pysähdy hetkeksi:** Katso jonkin verkkosivun rekisteröitymislomaketta (mikä tahansa — suoratoistopalvelu, koulun portaali, peli). Pystytkö nimeämään kolme eri ehtoa, joita lomake tarkistaa ennen kuin sallii lähetyksen? Et tarvitse koodia näkyviin; voit lukea ne virheilmoituksista.

---

## Oppitunti 15 — Toisto: saman asian tekeminen monta kertaa

### Mitä toisto tarkoittaa

**Toisto** on saman vaiheen tai saman vaihejoukon tekemistä useammin kuin kerran, lopetusehdon kanssa, joka kertoo tulkitsijalle, milloin pysähtyä. Toistoa kutsutaan arkisessa tekniikkapuheessa myös *silmukaksi* — molemmat sanat tarkoittavat samaa asiaa tällä kurssilla; käytämme enimmäkseen sanaa *toisto*.

Sekvenssi on suora viiva. Ehto on haara. Toisto on ympyrä, jossa *on myös* rehellinen ulospääsy. Jos ulospääsy puuttuu, tulkitsija kiertää ikuisesti — *karannut toisto*. Tästä lisää alla.

### Arkiset toistot, joita käytät jo

Teet näitä koko ajan, aivan kuten ehtoja, antamatta niille nimeä.

- *"Merkitse jokainen nimi luettelosta läsnä tai poissa."* Teet saman pienen toiminnon — kirjoitat L tai P nimen viereen — kerran jokaista listalla olevaa nimeä kohti, ja pysähdyt, kun lista loppuu.
- *"Lisää sokeria ja sekoita, kunnes maistuu hyvältä."* Teet saman toiminnon — lisää hyppysellinen, sekoita, maista — ja pysähdyt, kun testi "maistuu hyvältä" lopulta palauttaa toden.
- *"Niin kauan kuin keitin on vielä kuuma, älä keitä uudelleen."* Tarkistat ehdon *ennen* kuin toimit; niin kauan kuin se on tosi, jatkat (tai tässä tapauksessa jatkat *olemista* keittämättä).

### Toiston kolme muotoa

On kolme pientä, rentoa muotoa, jotka kattavat melkein jokaisen toiston, jonka koskaan kirjoitat selkokielellä:

- **For each** — *jokaiselle listan kohteelle tee …*. Käytä, kun lista on **tiedossa etukäteen**. Lista on lopetusehto: pysähdyt, kun lista loppuu. Esimerkki: *jokaiselle nimelle luettelossa, merkitse läsnä tai poissa*.
- **Repeat until** — *tee … kunnes lopetusehto on tosi*. Käytä, kun lopetus riippuu **siitä mitä tapahtuu** toiston aikana. Esimerkki: *jatka sekoittamista, kunnes sokeri liukenee*.
- **While** — *niin kauan kuin ehto on tosi, jatka tekemistä …*. Käytä, kun testi **tarkistetaan ennen jokaista toistokierrosta**. Esimerkki: *niin kauan kuin keitin on vielä kuuma, älä keitä sitä uudelleen*.

Sinun ei tarvitse opetella näiden muotojen eroa ulkoa kuten sanaston sanaa. Ne ovat kolme rytmiä, ja sinä valitset tilanteeseen sopivan. Kaikissa kolmessa olennaista on: **lopetus on todellinen, ja tulkitsija näkee sen.**

### Toisto ICT-kontekstissa — sähköpostien läpikäynti

Tässä sama idea ammatillisessa ympäristössä. Avaat sähköpostilaatikkosi päivän alussa. Näet 47 lukematonta viestiä. Käyt ne läpi:

> **for each** lukematon viesti sähköpostissa:
> &nbsp;&nbsp;&nbsp;&nbsp;**if** se on henkilöltä, **then** merkitse vastattavaksi;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** se on uutiskirje, **then** arkistoi;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** se on roskapostia, **then** poista.
> Toista, kunnes sähköposti on tyhjä.

Pysähdy ja huomaa jotain: tuo yksi prosessi käyttää **kaikkia kolmea rakennuspalikkaa**.

- 1–2 vaihetta, jotka teet viestiä kohti (merkitse / arkistoi / poista) ovat pieni **sekvenssi**.
- "Onko se henkilöltä / uutiskirje / roskapostia" -valinta on **ehto** (kolmella haaralla).
- "Jokaiselle lukemattomalle viestille … kunnes sähköposti on tyhjä" -kehys on **toisto**.

Useimmat todelliset prosessit näyttävät tällaisilta — sekvenssi käärittynä ehtoon, käärittynä toistoon, tai toisto, joka sisältää ehdon, joka sisältää pienen sekvenssin. Kolmen palikan nimeäminen erikseen on se, mikä tekee kuvauksesta luettavan. Ilman nimiä sähköpostien läpikäynti on vain kappale, joka sanoo "käy sähköpostit läpi." Nimien kanssa se on prosessi, jonka sananmukainen tulkitsija voisi suorittaa.

### Lopetusehto on turvavyö

Vertaa näitä kahta lausetta:

- *"Jokaiselle viikonloppuvalokuvalle puhelimellani, päätä säilytätkö sen."* — Rehellinen lopetus: viikonloppuvalokuvien lista on äärellinen, joten tulkitsija lopulta loppuu valokuvat.
- *"Jatka työskentelyä, kunnes ymmärrät."* — Ei rehellinen lopetus. Ei ole havaittavissa olevaa testiä "ymmärtämiselle". Tulkitsija (sinä) saatat pyöriä ikuisesti tai — todennäköisemmin — luovutat sattumanvaraisesti ja tunnet syyllisyyttä siitä.

Jokainen toisto tarvitsee lopetuksen, jonka tulkitsija näkee. *"Kunnes sähköposti on tyhjä"* on havaittavissa. *"Kunnes paikka on vapaa"* on havaittavissa. *"Kunnes tuntuu valmiilta"* ei ole — ellei sitä muunneta tarkistettavaksi (*"kunnes pystyt selittämään sen luokkatoverille yhdellä lauseella"*, *"kunnes olet vastannut kolmeen harjoituskysymykseen oikein peräkkäin"*).

Kun toistossa ei ole rehellistä lopetusta, sinulla on **karannut toisto**. Korjaus on lähes aina sama: lisää turvalopetus selkokielellä. *"Toista, kunnes sivu latautuu — tai pysähdy 30 sekunnin jälkeen ja yritä myöhemmin uudelleen."* Turvalopetus on turvavyö.

> **Pysähdy hetkeksi:** Nimeä yksi asia, jonka teit tänään ja joka oli toisto. Mikä oli lopetusehto? Oliko lopetusehto jotain, jonka pystyit oikeasti havaitsemaan, vai pysähdyitkö, koska "tuntui valmiilta"?

> **Pysähdy hetkeksi:** Kuvittele *"toista, kunnes …"* ilman lopetusta, jonka pystyt oikeasti havaitsemaan. Kirjoita se ylös. Kirjoita sitten turvalopetus, joka sen pelastaisi. Mitä jouduit muuttamaan?

### Laskurit — kun lopetus on luku

Joskus lopetus on vain luku. *"Tee kaksikymmentä punnerrusta."* *"Toista kertosäe kolme kertaa."* Teet sisävaiheen, pidät kirjaa siitä, montako kertaa olet sen tehnyt, ja pysähdyt, kun saavutat luvun.

Laskuri on eräänlainen `for each` numeroista 1:stä N:ään. *"Tee kaksikymmentä punnerrusta"* on samaa muotoa kuin *"jokaiselle numerolle 1:stä 20:een, tee yksi punnerrus."* Et tarvitse mitään erityissyntaksia tähän; tarvitset vain rehellisen luvun. *"Toista, kunnes olet tehnyt tarpeeksi"* ei ole laskuri; *"toista 20 kertaa"* on.

---

## Yhteenveto ja mitä seuraavaksi

Tämä viikko nimesi ne kolme rakenteellista liikettä, joista lähes jokainen kuvattu prosessi koostuu:

- **Sekvenssi** — tee A, sitten B, sitten C, järjestyksessä, oletuksena.
- **Ehto** — tässä kohdassa, testaa jotain, ja valitse haara.
- **Toisto** — tee tämä uudelleen, lopetuksella, jonka tulkitsija näkee.

> **Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto.** Kun osaat nimetä nämä arkisissa tehtävissä, sinulla on jokaisen ohjelman luuranko.

Kohtasit jokaisen palikan ensin arkisessa ympäristössä — teeresepti, "jos sataa, mene bussilla", luettelon merkitseminen — ja sitten ammatillisessa peilikuvassa — käyttöönottolista, salasanasääntö, sähköpostien läpikäynti. Arkinen versio tuli ensin tarkoituksella. ICT-versio on sama idea eri vaatteissa.

**AT2-yhteys — uudelleen.** AT2 palautetaan viikon 5 lopussa / viikon 6 aikana. Se pyytää sinua kuvaamaan valitsemasi prosessin luonnollisella kielellä siten, että kaikki kolme rakennuspalikkaa näkyvät. Tämän viikon must-do minimum -tehtävä on sama tuotos pienemmässä mittakaavassa: valitse prosessi, jota oikeasti teet, kirjoita 3–6 vaiheen sekvenssirunko, lisää vähintään yksi ehto (puun kanssa), lisää vähintään yksi toisto (oikealla lopetuksella). Säilytä muistiinpanosi — se työ, jonka teet tällä viikolla, on AT2-tuotos miniatyyrissä.

**Mitä seuraavaksi: viikko 6 — pseudokoodi ja käsiajo.** Ensi viikolla tiivistämme nämä luonnollisen kielen kuvaukset hieman lähemmäs koodia — mutta vielä paperilla. Sitä kutsutaan **pseudokoodiksi**: muutama lisäkonventio (pienet muuttujat, yksinkertainen sisennys, käsiajotaulukko), jotka muuttavat tällä viikolla kirjoittamasi löyhän selkokielen sellaiseksi, että aloitteleva ohjelmoija voisi lukea sen rivi riviltä. Se ajattelu, jota harjoittelit tällä viikolla — kolmen rakennuspalikan nimeäminen — on juuri sitä, mikä tekee pseudokoodista luettavaa. Itse koodi tulee vasta viikolla 7.
