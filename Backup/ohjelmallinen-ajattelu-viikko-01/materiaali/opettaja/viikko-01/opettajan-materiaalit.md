# Viikko 1 — Opettajan materiaalit

Tämä dokumentti kattaa kaikki viikon 1 kolme oppituntia (L1, L2, L3) yhdessä paikassa. Se rakentuu saman keskeisen kysymyksen ympärille kuin opiskelijatkin näkevät: **"Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?"** Viikko 1 asettaa käsitteellisen perustan koko 8 viikon kurssille. Tällä viikolla ei esitellä koodia, vuokaavioita tai pseudokoodia; kolme oppituntia muodostavat yhden kaaren — oppitunti 1 nimeää ongelman (sananmukainen tulkinta, monitulkintaisuus), oppitunti 2 nimeää työkalun joka ratkaisee sen (algoritmi), ja oppitunti 3 koettelee työkalua jahtaamalla ja poistamalla monitulkintaisuutta.

Ristiviittaukset: oppitunneilla 1 ja 3 käytettävät tuntiaktiviteetit on kuvattu yksityiskohtaisesti samassa kansiossa olevassa tiedostossa `tuntitehtavat.md`. Ristiviittaukset näkyvät alla olevissa oppituntikohtaisissa suunnitelmissa.

---

## Viikon 1 oppimistavoitteet (Bloomiin mapattuna)

Viikko 1 pysyy **Muistamisen** ja **Ymmärtämisen** sisällä, sallien **kevyttä Soveltamista** oppitunneilla 2 ja 3 (lyhyen arkisen algoritmin kirjoittaminen; epätäsmällisen ohjeen uudelleenkirjoittaminen). Viikon 1 tavoitteissa kielletyt verbit ovat *luo, rakenna, suunnittele, kehitä, arvioi, tuomitse, analysoi, pilko, abstrahoi, debuggaa*. Nämä palaavat myöhemmillä viikoilla.

### Oppitunti 1 — Ihmiset, tietokoneet ja ohjeiden tulkitseminen

- **Muistaminen:** opiskelija osaa **määritellä** ohjelmallisen ajattelun omin sanoin.
- **Ymmärtäminen:** opiskelija osaa **selittää**, että tietokone seuraa ohjeita sananmukaisesti.
- **Ymmärtäminen:** opiskelija osaa **antaa** yhden arkisen esimerkin ja yhden ICT-esimerkin "tietokoneelle puhumisesta".
- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, että monitulkintaisuus on ohjeen ominaisuus, ei tietokoneen.

### Oppitunti 2 — Algoritmit arkielämässä

- **Muistaminen:** opiskelija osaa **määritellä** *algoritmin* omin sanoin.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa** algoritmeja arjen tilanteissa (resepti, reitti, aamurutiini).
- **Ymmärtäminen:** opiskelija osaa **kuvata** algoritmin neljä osaa — tavoite, syöte, vaiheet, tuloste.
- **Ymmärtäminen:** opiskelija osaa **vertailla** kahta algoritmia samaan tavoitteeseen pintapuolisesti (kumpi on lyhyempi, kumpi on helpompi seurata).
- **Kevyt Soveltaminen:** opiskelija osaa **kirjoittaa** 5–10 vaiheen arkisen algoritmin selkeällä suomella.

### Oppitunti 3 — Täsmälliset ja epätäsmälliset ohjeet

- **Ymmärtäminen:** opiskelija osaa **tunnistaa** monitulkintaiset sanat lyhyestä ohjeesta.
- **Ymmärtäminen:** opiskelija osaa **selittää**, miksi testaaminen paljastaa viat nopeammin kuin uudelleenlukeminen.
- **Kevyt Soveltaminen:** opiskelija osaa **kirjoittaa uudelleen** epätäsmällisen ohjeen siten, että sananmukainen tulkitsija voi suorittaa sen.
- **Kevyt Soveltaminen:** opiskelija osaa **testata** ohjeen toimimalla "sananmukaisena tietokoneena".

Kurssin korkeampia Bloom-tasoja — *Analysointi* (viikko 4), *Luominen* (lopullinen arvioitava tehtävä, viikko 8) — ei tarkoituksellisesti ole tämän viikon laajuudessa.

---

## Viikon 1 yleisiä virhekäsityksiä

Vähintään kaksi virhekäsitystä per oppitunti esiintyy täällä. Ennakoi listan ensimmäinen (*tietokone on tyhmä*) heti oppitunnin 1 alussa — se on yleisin ja vahingollisin, jos se jätetään.

### Oppitunnin 1 virhekäsitykset

**Virhekäsitys:** "Tietokone on tyhmä."
**Korjaus:** Tietokone on **sananmukainen**, ei tyhmä. Sananmukaisella tulkitsijalla ei ole mielipidettä siitä, onko ohje järkevä; se tekee täsmälleen mitä sanat sallivat. Vaadi sanaa *sananmukainen* heti ensimmäisestä minuutista ja korjaa lempeästi *tyhmä/typerä* aina kun se ilmestyy opiskelijan puheeseen. Koko kurssi nojaa tähän uudelleenkehystämiseen — opiskelijat, jotka pitävät "tyhmä" -sanan sanavarastossaan, jatkavat olettamista, että koneen olisi pitänyt tietää mitä he tarkoittivat.

**Virhekäsitys:** "Ohjelmallinen ajattelu on vain ohjelmointia."
**Korjaus:** Ohjelmallinen ajattelu on ohjelmoinnin **takana oleva ajattelu** — ongelman ottaminen, sen nimeäminen mikä on kiinteää ja mikä vaihtelee, ja ratkaisun ilmaiseminen selkeinä vaiheina. Ohjelmointi on yksi paikka, jossa ohjelmallista ajattelua käytetään, ei ainoa. Resepti, help desk -käsikirjoitus ja paloharjoituksen toimintaohje ovat kaikki ohjelmallisen ajattelun muotoja. Ohjelmointi saapuu kunnolla viikolla 7.

### Oppitunnin 2 virhekäsitykset

**Virhekäsitys:** "Algoritmit ovat vain tietojenkäsittelytieteilijöille."
**Korjaus:** Jokainen resepti on algoritmi. Jokainen joukko bussiohjeita on algoritmi. Jokainen aamurutiini on algoritmi. Sana *algoritmi* nimeää jotakin, mitä opiskelijat jo tekevät — oppitunti antaa heille nimen taidolle, joka heillä jo on, ei opeta täysin uutta taitoa.

**Virhekäsitys:** "Algoritmin täytyy olla pitkä laskettavaksi."
**Korjaus:** Kolme selkeää vaihetta voi olla kelvollinen algoritmi, jos ne saavuttavat tavoitteen ilman monitulkintaisuutta. Pituus ei ole kriteeri; **selkeys ja tavoitteen saavuttaminen** ovat. Käänteisesti, 30-vaiheinen ohje täynnä epämääräisiä sanoja on huono algoritmi.

### Oppitunnin 3 virhekäsitykset

**Virhekäsitys:** "Epätäsmällinen tarkoittaa vain lyhyttä."
**Korjaus:** Pitkä ohje voi silti olla epätäsmällinen. Lyhyt ohje voi olla täydellisen täsmällinen. Epätäsmällisyys on **siitä, onko sananmukaisella tulkitsijalla useampi kuin yksi perusteltavissa oleva tapa toimia**, ei siitä kuinka monta sanaa on.

**Virhekäsitys:** "Jos ohje kuulostaa oikealta kun sen luen, se on oikein."
**Korjaus:** Oman ohjeen takaisin lukeminen itselleen harvoin paljastaa monitulkintaisuutta, koska tiedät jo mitä tarkoitit. **Vain testaaminen sananmukaisella tulkitsijalla (luokkakaveri, sisarus tai sinä itse lukemassa sitä 24 tunnin kuluttua) paljastaa aukot.** Tästä syystä oppitunnin 3 keskeinen aktiviteetti on toimia sananmukaisena tietokoneena.

**Virhekäsitys (bonus, esiintyy usein oppitunnilla 1 tai 3):** "Jos lisään 'kiitos' tai 'ystävällisesti', tietokone on mukavampi."
**Korjaus:** Sananmukaisella tulkitsijalla ei ole kohteliaisuuskanavaa. *Kiitos* ja *ystävällisesti* eivät ole sen enempää tai vähempää informatiivisia kuin niiden ympärillä olevat verbit; ne eivät lisää tai vähennä sananmukaista merkitystä. Tämä on myös hyvä hetki huomauttaa, että ihmisten kohteliaisuuskäytännöt eivät siirry sananmukaiseen ohjeiden noudattamiseen.

---

## Oppitunti 1 — 90 minuutin suunnitelma

**Aihe.** Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen.

**Tämän oppitunnin keskeinen viesti (yhdellä virkkeellä).** Tietokone on ohjeiden sananmukainen tulkitsija, joten ohjeen laatu — ei koneen näppäryys — ratkaisee lopputuloksen.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: 5 minuutin "Sananmukainen tulkitsija livenä" -demo (yksi lappu, esim. *"Tuo minulle tuoli"*), sitten esittele keskeinen kysymys taululla. | Opettajan demo + koko luokka |
| 0:10–0:25 | Opettajan input: määrittele ohjelmallinen ajattelu omin sanoin ensin, sitten tarjoa lyhyt kurssin laajuinen määritelmä. Kehystä neljä klassista pilaria nimeltä (ositus, mallien tunnistaminen, abstraktio, algoritmit) ja kerro opiskelijoille, että jokainen saa oman tulevan viikkonsa. | Luento |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija laatii 6–10 vaiheen ohjeen henkilökohtaiselle tehtävälle, jota hän todella tekee. **Ei tulkitsijaa vielä** — tämä on tehtävän 1.1 kirjoitusvaihe. | Itsenäinen |
| 0:55–1:15 | Pariaktiviteetti: opiskelijat vaihtavat luonnoksia ja lukevat toistensa *sananmukaisesti*. Vastaanottaja alleviivaa jokaisen vaiheen, joka on avoin useammalle kuin yhdelle tulkinnalle. Kirjoittaja katsoo ja pidättäytyy selittämästä. | Pari |
| 1:15–1:25 | Koko luokan purku: rakenna "Arki vs. ICT" -taulu. Kerää 3–4 arkista esimerkkiä sananmukaisesta väärinluennasta (sisarus + voileipä, monitulkintaiset reittiohjeet, autocorrect) ja 3–4 ICT-esimerkkiä (kirjoitusvirhe hakukyselyssä, tiedostopolku puuttuvalla kauttaviivalla). | Koko luokka |
| 1:25–1:30 | Sulkeva reflektiokehote taululla, sekä yhden rivin esikatselu oppitunnille 2. | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** Aloituslämmittely käyttää yhtä lappua tiedoston `tuntitehtavat.md` aktiviteetista A. Täysi aktiviteetti A on varattu oppitunnille 3.

**Mitä sanot ääneen lämmittelyssä.** "Hetken kuluttua yksi teistä näyttelee tietokonetta viiden minuutin ajan. Tietokone tekee vain sen, mitä sanat sanovat — ei sen enempää eikä vähempää. Yleisön tehtävä on huomata hetki, jolloin sana osoittautuu tarkoittavan useampaa kuin yhtä asiaa." Pidä demo. Vastusta kiusausta purkaa pitkään; yksi virke ("huomatkaa, että monitulkintaisuus oli ohjeessa, ei vapaaehtoisessa") riittää — täysi purku on oppitunnilla 3.

**Slidevihjeet — päädekki `slides.md`.**

- **Lämmittely (0:00–0:10):** ei slidejä. Sananmukaisen tulkitsijan demo on livenä; ruudulla oleva slide kilpailisi sen kanssa.
- **Luento (0:10–0:25):** päädekin slidet **4 → 7**: *Mitä ohjelmallinen ajattelu on?* · *Tietokone ottaa sinut sananmukaisesti* · *"Tee voileipä" — mikä voi mennä pieleen?* · *Monitulkintaisuus on ohjeessa, ei tietokoneessa*. Kävele noin 3–4 min per slide. Pysähdy slidellä 7 tarpeeksi pitkään, jotta uudelleenkehystäminen laskeutuu.
- **Itsenäinen työ (0:25–0:55):** ei slidejä ruudulla. Opiskelijat tarvitsevat hiljaista kirjoitusaikaa ja puhtaan taulun.
- **Pariaktiviteetti (0:55–1:15):** jätä slide **7** ruudulle hiljaisena muistutuksena siitä, että monitulkintaisuus on ohjeessa, ei tulkitsijassa.
- **Purku (1:15–1:25):** slide **5** on hyödyllinen, jos opiskelijoilla on vaikeuksia keksiä arki vs. ICT -esimerkkejä; muutoin rakenna kaksipalstainen taulu tuoreesti.
- **Sulkeminen (1:25–1:30):** ei slidejä. Päätä taululle.

Viikon 1 päädekki riittää oppitunnin 1 luento-osuudelle. Täydentävää dekkiä ei tarvita.

**Materiaalit.** Taulu ja tussi; yksi monitulkintainen ohje lapulla; tulostettu lista neljästä pilarista nimineen (jakomateriaali valinnainen). Teknologiaa ei tarvita tällä oppitunnilla.

---

## Oppitunti 2 — 90 minuutin suunnitelma

**Aihe.** Algoritmit arkielämässä: vaiheittaiset ohjeet ilman koodia.

**Tämän oppitunnin keskeinen viesti (yhdellä virkkeellä).** Algoritmi on arkinen nimi selkeälle sananmukaisten vaiheiden sarjalle, ja sellaisen kirjoittaminen on taito, jota kuka tahansa voi harjoitella ilman koodia.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: pyydä luokkaa huutamaan kolme algoritmia arjesta. Kerää ne taululle. Todennäköisiä vastauksia: resepti, bussireitti, hampaiden harjaus. Vastusta "vääräin" vastausten korjaamista; kaikki järkevä kelpaa. | Koko luokka |
| 0:10–0:25 | Opettajan input: määrittele *algoritmi*, nimeä neljä osaa — **tavoite, syöte, vaiheet, tuloste** — ja kävele yksi taulun esimerkki neljän osan kautta livenä. | Luento |
| 0:25–1:00 | **Itsenäinen työ** (35 min): jokainen opiskelija kirjoittaa oman aamurutiininsa algoritmin (tai jos hän mieluummin, toisen tutun arkisen algoritmin) 7–12 numeroidussa vaiheessa. He nimeävät tavoitteen, syötteen, vaiheet ja tulosteen erikseen sivun yläosaan. | Itsenäinen |
| 1:00–1:20 | Pariaktiviteetti: opiskelijat vaihtavat algoritmeja. Lukija **ennustaa tulosteen** pelkistä vaiheista — kysymättä kirjoittajalta. Sitten he vertaavat ennustetta tarkoitukseen ja puhuvat siitä, mitkä vaiheet olivat tarpeeksi tarkkoja paljastaakseen tavoitteen. (Tämä on aktiviteetti B tiedostosta `tuntitehtavat.md` lyhennetyssä muodossa; käytä täyttä versiota, jos aikaa riittää.) | Pari |
| 1:20–1:28 | Koko luokan purku: kerää yksi löydös kolmelta parilta. Minkä tyyppinen vaihe oli tarpeeksi tarkka tehdäkseen tavoitteen ilmiselväksi? Minkä tyyppinen vaihe oli liian epämääräinen auttaakseen? | Koko luokka |
| 1:28–1:30 | Kahden virkkeen esikatselu oppitunnille 3. | Koko luokka |

**Itsenäisen työn lohko: 35 minuuttia (39 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** Aikaväli 60–80 minuuttia käyttää aktiviteettia B tiedostosta `tuntitehtavat.md` (Algoritmiviesti).

**Mitä sanot ääneen luennossa.** "Algoritmilla on neljä osaa. Tavoite on se, mitä haluat lopussa. Syöte on se, mitä sinulla on oltava ennen kuin voit aloittaa. Vaiheet ovat se, mitä teet, järjestyksessä. Tuloste on se, mitä sinulla on, kun vaiheet on tehty. Jos jokin näistä puuttuu, algoritmi on epätäydellinen." Sitten kävele taulun esimerkkien kautta yksi (esim. pikanuudeleiden valmistus): tavoite — kulhollinen kuumia nuudeleita; syöte — vedenkeitin, vesi, paketti, kulho, haarukka; vaiheet — listattu; tuloste — kulhollinen kuumia nuudeleita syötäväksi. Vältä houkutusta lisätä viidettä osaa (esim. esiedellytyksiä, jälkiedellytyksiä). Neljä riittää viikolle 1.

**Slidevihjeet — päädekki `slides.md` + täydentävä dekki.**

- **Lämmittely (0:00–0:10):** ei slidejä. Kerää arkisia algoritmeja taululle livenä.
- **Luento (0:10–0:25):** päädekin slidet **8 → 10**: *Algoritmi — nimi sille mitä jo teet* · *Algoritmin osat (tavoite · syöte · vaiheet · tuloste)* · *Kaksi algoritmia, yksi tavoite*. Kävele hitaasti slidellä 9 — neljän osan on tarttuvat.
  - **Täydentävä dekki saatavilla:** `kalvot-o2-algoritmin-lapikaynti.md` (6 lyhyttä slidea) ottaa neljä osaa ja kävelee ne yhden konkreettisen esimerkin läpi (pikanuudeleiden valmistus). **Aja tämä heti sliden 9 jälkeen, jos luokkasi tarvitsee neljä osaa näytettynä todellisella, täydellisellä esimerkillä ennen kuin he alkavat kirjoittaa omia.** Ohita se, jos live-kävely taululla riittää.
- **Itsenäinen työ (0:25–1:00):** jätä slide **9** ruudulle hiljaiseksi mallipohjaksi (tavoite · syöte · vaiheet · tuloste). Muutoin ei slidejä.
- **Pariaktiviteetti (1:00–1:20):** ei slidejä; parit työskentelevät paperilla.
- **Purku (1:20–1:28):** ei slidejä. Pysy taululla.
- **Sulkeminen (1:28–1:30):** ei slidejä.

**Materiaalit.** Taulu ja tussi. Paperia ja kyniä. Teknologiaa ei tarvita.

---

## Oppitunti 3 — 90 minuutin suunnitelma

**Aihe.** Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen.

**Tämän oppitunnin keskeinen viesti (yhdellä virkkeellä).** Ohjeet eivät ole valmiit kun ne kuulostavat oikealta; ne ovat valmiit kun sananmukainen tulkitsija voi suorittaa ne kysymättä.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: kaksi lyhyttä monitulkintaista ohjetta taululla (esim. *"Tallenna tiedosto tavalliseen paikkaan"* ja *"Vastaa hänelle siitä"*). Luokka nimeää mikä on monitulkintaista ja ehdottaa uudelleenkirjoitusta. Kevyt tempo. | Koko luokka |
| 0:10–0:25 | Opettajan input: määrittele *täsmällinen* ja *epätäsmällinen* selkeällä suomella. Kävele neljän yleisen monitulkintaisuusmallin läpi — epämääräiset substantiivit ("tiedosto"), deiktiset sanat ("tässä", "tuolla", "hän"), suhteellinen aika ("myöhemmin", "pian"), epämääräinen määrä ("vähän", "jonkin verran"). Yksi esimerkki per malli. | Luento |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija ottaa oppitunnilta 2 aamurutiininsa algoritmin ja kirjoittaa sen uudelleen poistaakseen monitulkintaisuuden. Hän ympyröi jokaisen vaihtamansa sanan ja kirjoittaa yhden rivin syyn sen viereen. | Itsenäinen |
| 0:55–1:20 | Tuntiaktiviteetti opettajan johdolla: **Aktiviteetti A — "Sananmukainen tulkitsija livenä"** tiedostosta `tuntitehtavat.md`. Vapaaehtoinen näyttelee sananmukaista tietokonetta kolmen valmistellun lapun ajan; luokka purkaa jokaisen; uudelleenkirjoitukset menevät taululle; jokainen opiskelija osallistuu yhdellä monitulkintaisella tarralappuohjeella sulkemisminuuttiin. | Koko luokka |
| 1:20–1:28 | Koko luokan purku: mikä neljästä monitulkintaisuusmallista esiintyi useimmin live-harjoituksessa? Liitä lyhyesti takaisin L1:n ajatukseen siitä, että monitulkintaisuus on ohjeessa, ei tulkitsijassa. | Koko luokka |
| 1:28–1:30 | Esikatselu viikolle 2 — ositus — yhdellä rivillä: *"Ensi viikolla käsittelemme ongelmia, jotka ovat liian suuria yhdelle algoritmille."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** Aikaväli 55–80 minuuttia on aktiviteetin A täysi versio tiedostosta `tuntitehtavat.md`. Lue tuo tiedosto ennen tätä oppituntia — siinä luetellaan tarkat lapulle valmistettavat ohjeet ja tarkat purkuliikkeet.

**Mitä sanot ääneen luennossa.** "On olemassa neljä sanatyyppiä, jotka lähes aina aiheuttavat monitulkintaisuutta. Ensimmäinen on epämääräinen substantiivi — 'tiedosto', 'nappi', 'paikka'. Mikä tiedosto? Toinen on sana, joka osoittaa johonkin, jota lukija ei näe — 'tässä', 'tuolla', 'tämä', 'hän'. Sormella osoittaminen ilman sormea ei toimi kirjoituksessa. Kolmas on suhteellinen aika — 'myöhemmin', 'pian', 'lounaan jälkeen'. Pian milloin? Neljäs on epämääräinen määrä — 'vähän', 'jonkin verran', 'tarpeeksi'. Nämä neljä eivät ole ainoita monitulkintaisuuden lähteitä, mutta ne saavat kiinni suurimman osan siitä mitä käytännössä näet." Kirjoita neljä mallia taululle ja pidä ne näkyvissä loppuoppitunnin ajan.

**Slidevihjeet — päädekki `slides.md`.**

- **Lämmittely (0:00–0:10):** ei slidejä; monitulkintaiset ohjeet menevät taululle, jotta luokka voi joukkoistaa uudelleenkirjoitukset.
- **Luento (0:10–0:25):** päädekin slidet **11 → 14**: *Täsmälliset vs. epätäsmälliset ohjeet* · *Monitulkintaisuuden jahtaaminen — neljä mallia* · *Testaaminen sananmukaisena robottina* · *Rajatapaukset (lempeä esittely)*. Slide 12 kantaa neljä mallia; kopioi ne myös taululle, jotta ne pysyvät näkyvinä sen jälkeen kun olet edennyt dekissä.
- **Itsenäinen työ (0:25–0:55):** jätä slide **12** ruudulle ruudulla näkyvänä viittauksena samalla kun opiskelijat jahtaavat monitulkintaisuutta omasta oppitunnin 2 algoritmistaan.
- **Tuntiaktiviteetti (0:55–1:20):** ei slidejä. Sananmukaisen tulkitsijan demo elää huoneessa, ei seinällä.
- **Purku (1:20–1:28):** ei slidejä; puhu neljän mallin läpi taulun live-näytön valossa.
- **Sulkeminen (1:28–1:30):** slide **18** *(Mitä seuraavaksi: viikko 2 — ositus)* yhden rivin esikatseluna, sitten slide **19** *(Kertaus — keskeinen kysymys)* lähettämään opiskelijat ulos ovesta oikealla linjalla.

Viikon 1 päädekki riittää oppitunnin 3 luento-osuudelle. Täydentävää dekkiä ei tarvita.

**Materiaalit.** Kolme valmisteltua monitulkintaisten ohjeiden lappua aktiviteetille A. Taulu ja tussi. Tarralappuja (yksi pakkaus per rivi). Paperia ja kyniä.

---

## Fasilitointivinkkejä

### Ennen mitä tahansa kolmesta tunnista

- **Testaa keskeinen kysymys ensin itseesi.** Lue se ääneen kerran, hitaasti. Jos et osaa sanoa sitä ulkomuistista kun kävelet luokkaan, opiskelijatkaan eivät imeydy siihen. Sanatarkka muoto — *"Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?"* — esiintyy kalvosarjassa kahdesti; peilaa se puheessasi.
- **Esikirjoita taulun asettelu.** Oppituntia 1 varten luonnostele "Arki vs. ICT" -kaksisarakeruudukko muistiinpanoihisi. Oppituntia 2 varten luonnostele algoritmin neljä osaa. Oppituntia 3 varten luonnostele neljä monitulkintaisuusmallia. Niiden piirtäminen taululle livenä on ok; livenä ajatteleminen on riskialtista.
- **Lue `tuntitehtavat.md` läpi ennen oppituntia 1.** Aktiviteetti A esiintyy kahdesti viikon aikana ja vaatii valmistellut laput. Jos opetatte yhdessä, antakaa aktiviteetti A nimenomaisesti yhdelle — se toimii paremmin, kun yksi ihminen omistaa sen.

### Tunnin aikana

- **Johda arkiesimerkillä. Aina.** Toimeksianto on tiukka: arkiesimerkki ennen ICT-esimerkkiä. Jos opiskelija tarjoaa ensin ICT-esimerkin, hyväksy se mutta paritta se arkiesimerkin kanssa ennen kuin etenet.
- **Vaadi sanaa *sananmukainen*.** Joka kerta kun opiskelija sanoo *tietokone on tyhmä*, vaihda sana lempeästi: "Sananmukainen — tietokone on sananmukainen. Tyhmä on silloin kun olisit pitänyt tietää paremmin. Tietokoneella ei koskaan ollut mahdollisuutta tietää." Kaksi tai kolme korjausta oppitunnilla 1 yleensä riittää loppuviikolle.
- **Pidä hiljaisuus sen jälkeen kun olet antanut lapun vapaaehtoiselle.** Uudet opettajat taipuvat selittämään vapaaehtoisen tekemisiä. Älä tee niin. Hiljaisuus on oppitunti.
- **Käytä taulua uudelleenkirjoituksiin, ei slidejä.** Slidet asettavat kysymyksen; uudelleenkirjoitusten on tapahduttava taululla, jotta luokka näkee live-siirtymän monitulkintaisesta täsmälliseen.
- **Tarkkaile kelloa 30–50 %:n säännön vuoksi.** Itsenäinen työ on se osa, jota paineen alla opettajat ensimmäiseksi leikkaavat. Suojaa sitä. Yllä olevat aikataulut jättävät 30–35 minuuttia per oppitunti; älä leikkaa 27:n alle.

---

## Vastauksia yleisiin opiskelijoiden kysymyksiin

- *"Onko Google algoritmi?"* — Kyllä, Google-hakua toteuttavat algoritmit (monet, mukaan lukien nykyaikaiset koneoppimispohjaiset). Viikolla 1 opiskelijan tarvitsema vastaus on: *kyllä, algoritmi arkisessa mielessä — vaiheiden sarja, joka ottaa syötteen (hakukyselysi) ja tuottaa tulosteen (tuloslista)*. Syvempi yksityiskohta kuuluu myöhemmille viikoille.
- *"Miksi autocorrect ei ymmärrä minua?"* — Koska autocorrect on myös sananmukainen omalla tavallaan: se noudattaa sääntöjä siitä, mitkä kirjainsekvenssit näyttävät miltäkin sanoilta, eikä sillä ole aavistustakaan mitä tarkoitit. Käytä tätä siltana ajatukseen "monitulkintaisuus on ohjeessa, ei tietokoneessa".
- *"Onko tämä arvioitavassa tehtävässä?"* — Viikolla 1 ei ole arvioitavaa tehtävää. AT1 tulee viikon 2 lopussa. Tämän viikon muistiinpanot ovat AT1:n raaka-ainetta; se on rehellinen vastaus.
- *"Tarvitsenko tietokoneen tämän kotitehtävän tekemiseen?"* — Et. Tehtävät 1.1 ja 1.4 voi tehdä paperilla, kynällä ja halukkaalla tulkitsijalla. Tehtävät 1.2 ja 1.3 vaativat vain paperia. Ainoa "tietokone", jonka viikko 1 tarvitsee, on luokkahuoneen sisällä oleva sananmukainen.
- *"Voinko käyttää ChatGPT:tä?"* — Kyllä, tehtävän 1.2 kuvaamalla tavalla — sparrauskumppanina, joka tönäisee ajatteluasi. Et saa liittää sen tulostetta ja palauttaa sitä. Tehtävää 1.1 erityisesti ei voi väärentää LLM:llä, koska se vaatii todellisen tulkitsijan ja havaittavan tuotoksen.

---

## Vinkkejä formatiiviseen arviointiin

Viikolla 1 ei ole **summatiivista arviointia**. Formatiivisten tarkistusten rooli on tehdä opiskelijan ymmärtämisestä näkyvää aikaisin, jotta virhekäsityksiä voidaan korjata ennen kuin viikon 2 ositus rakennetaan päälle. Käytä yhtä tai kahta seuraavista per oppitunti; älä yritä käyttää kaikkia.

### Oppituntikohtaisia epämuodollisia tarkistuksia

- **Oppitunti 1 — exit ticket (3 min, tunnin lopussa).** Jokainen opiskelija kirjoittaa yhden virkkeen vastatakseen: *"Mitä omin sanoin tarkoittaa, että tietokone on sananmukainen?"* Kerää tiketit, selaa ne matkalla oppitunnille 2 ja aloita oppitunti 2 lukemalla ääneen kaksi anonyymiä vahvaa vastausta. Vääriä vastauksia ei korjata julkisesti; sen sijaan yllä oleva virhekäsityslista kertoo, mitä palata oppitunnin 2 lämmittelyssä.
- **Oppitunti 1 — taulukysely.** Näytä kolme väittämää: (a) *"Tietokone on tyhmä."* (b) *"Tietokone on sananmukainen."* (c) *"Riippuu."* Pyydä jokaista opiskelijaa nostamaan käsi yhden puolesta. Käsien kuvio kertoo, laskeutuiko keskeinen uudelleenkehystäminen; vahva (a) tai (c) -ääni tarkoittaa, että asiaa on käsiteltävä uudelleen ennen etenemistä.
- **Oppitunti 2 — pariraportointi (2 min, pariaktiviteetin jälkeen).** Pyydä kahta paria nimeämään yksi osa toistensa algoritmista, joka oli selkeä, ja yksi joka oli epämääräinen. Kuuntele, käyttävätkö opiskelijat sanoja *tavoite, syöte, vaiheet, tuloste* — se on onnistumisen signaali.
- **Oppitunti 2 — yhden minuutin paperi.** Tunnin lopussa: *"Kirjoita yksi tänään käyttämäsi algoritmi, jota et pitänyt algoritmina ennen tätä oppituntia."* Lue kolme oppitunnin 3 alussa lämmittelyksi.
- **Oppitunti 3 — tarralappujen keräys.** Aktiviteetti A päättyy jo tarralappuihin; pidä ne. Opiskelijoiden kirjoittamien monitulkintaisten ohjeiden kuvio on itsessään arvio siitä, kuinka hyvin he tunnistavat monitulkintaisuutta omasta kielestään.
- **Oppitunti 3 — exit ticket.** *"Nimeä se monitulkintaisuusmalli, jonka huomaat helpoimmin, ja se, jonka huomaat vaikeimmin."* Käytä vastauksia viikon 2 lämmittelyesimerkkien valintaan.

### Mitä kuuntelet koko viikon ajan

Kaksi lausetta, jotka osoittavat aitoa ymmärrystä viikon 1 päätteeksi, ovat:

- *"Ohje on monitulkintainen"* (sen sijaan että *tietokone on väärässä*).
- *"Anna minun testata se sananmukaisella tulkitsijalla"* (sen sijaan että *anna minun lukea se uudelleen*).

Jos nämä kaksi lausetta esiintyvät opiskelijoiden puheessa oppituntiin 3 mennessä, viikko 1 on tehnyt tehtävänsä, ja viikko 2 (ositus) voi rakentua sen päälle ilman uudelleenharjoittelua.
