# Viikko 7 — Opettajan materiaalit

Tämä dokumentti kattaa kaikki viikon 7 kolme oppituntia (O19, O20, O21) yhdessä paikassa. Se on rakennettu saman keskeisen viestin ympärille, jonka opiskelijat näkevät: **"Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone osaa noudattaa niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain se syntaksi, jolla se kirjoitetaan."** Viikko 7 on silta koodiin. Kuuden viikon pseudokoodi, sekvenssi-ehto-toisto, pilkkominen ja käsiajo kohtaavat oikean syntaksin ensimmäistä kertaa — ja kahdella kielellä, JavaScriptillä ja C#:lla, rinta rinnan, ei toinen toisensa perään.

**AT3 julkaistaan viikon 8 lopussa**, ei tällä viikolla. Viikon 7 tehtävä on tehdä AT3:n aloittamisesta tylsää: opiskelija, joka on tällä viikolla kirjoittanut kolme toimivaa riviä valitsemallaan kielellä, avaa AT3:n toimeksiannon ensi viikolla ja tunnistaa muodon välittömästi. Jokainen tehtävä tiedostoissa `student-tasks-js.md` ja `student-tasks-csharp.md` kantaa AT3-muistutuksen tästä syystä.

Oikeaa IDE:tä ei käytetä. Ei `node`:a, ei `npm`:ää, ei `dotnet new`:tä, ei Visual Studiota, ei VS Codea, ei JetBrains Rider:iä. JavaScript ajetaan selaimen DevTools-konsolissa. C# ajetaan **.NET Fiddlessä** (`dotnetfiddle.net`) — sharplab.io ja C#-yhteensopiva Replit ovat hyväksyttäviä vaihtoehtoja. Automaattisia testaus- tai debugger-frameworkkeja ei käytetä missään. Taso on *kokeile, aja, katso mitä tapahtuu, lue tuloste*.

Ristiviittaukset: täydennyssetti `slides-l21-age-check.md` käytetään O21:n luentosegmentin aikana. Pakollinen tuntiaktiviteetti *Konsolirelay* on kuvattu tiedostossa `in-class-tasks.md` ja kuuluu O20:n 55–75 min slottiin.

---

## Viikon 7 oppimistavoitteet (kuvattuna Bloomiin)

Viikko 7 pysyy **Ymmärtämisen** ja **Soveltamisen** sisällä. Kielletyt verbit viikon 7 tavoitteissa: *analysoi, arvioi, suunnittele, luo, rakenna, debuggaa, refaktoroi, optimoi*. AT3 viikolla 8 on se paikka, johon Luomisen sävyinen työ laskeutuu.

### Oppitunti 19 — Miksi ohjelmointikieliä tarvitaan (kieliriippumaton)

- **Ymmärtäminen:** opiskelija osaa **määritellä** *ohjelmointikielen*, *syntaksin*, *käskyn*, *tulkin* ja *kääntäjän* epämuodollisesti omin sanoin.
- **Ymmärtäminen:** opiskelija osaa **selittää**, miksi ohjelmointikieltä tarvitaan, kun pseudokoodi on jo täsmällistä — eli että oikea tietokone ei osaa lukea englanninkielistä pseudokoodia.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, että sama algoritmi voidaan kirjoittaa eri kielillä ja silti se tarkoittaa samaa.
- **Ymmärtäminen:** opiskelija osaa **nimetä** kaksi todellista ohjelmointikieltä (JavaScript, C#) ja yhden paikan, jossa kumpaakin tyypillisesti käytetään (JS = selain; C# = .NET, Unity).

### Oppitunti 20 — Ensimmäiset käskyt: tuloste, arvot, muuttujat (kaksikielinen)

- **Soveltaminen:** opiskelija osaa **suorittaa** ensimmäisen ohjelman, joka tulostaa tekstiä konsoliin — `console.log("…")` JavaScriptissä tai `Console.WriteLine("…")` C#:ssa.
- **Soveltaminen:** opiskelija osaa **esitellä** muuttujan ja **antaa** sille arvon — `let` JS:ssä, tyypitetyt esittelyt (`int`, `string`) C#:ssa.
- **Soveltaminen:** opiskelija osaa **tulostaa** muuttujan arvon, mukaan lukien yhdistämällä `+`:lla.
- **Soveltaminen:** opiskelija osaa **suorittaa** yksinkertaisen aritmeettisen laskutoimituksen (vuosia täysi-ikäisyyteen, kokonaishinta) ja tulostaa tuloksen.
- **Ymmärtäminen:** opiskelija osaa **tunnistaa**, että *ajattelu* — lue arvo, laske, tulosta — on sama molemmilla kielillä.

### Oppitunti 21 — Ehdot koodissa: if, else, vertailut (kaksikielinen)

- **Soveltaminen:** opiskelija osaa **kirjoittaa** vertailulausekkeen (`age >= 18`) molemmilla kielillä ja **tunnistaa**, että vertailuoperaattorit ovat olennaisesti identtiset.
- **Soveltaminen:** opiskelija osaa **kirjoittaa** ensimmäisen `if/else`-lohkon, joka tulostaa toisen kahdesta viestistä muuttujan arvon mukaan.
- **Soveltaminen:** opiskelija osaa **kuvata** palan viikon 6 pseudokoodia (`IF age >= 18 THEN … ELSE …`) koodiksi valitsemallaan kielellä.
- **Soveltaminen:** opiskelija osaa **ennustaa** pienen `if/else`-ohjelman tulosteen ennen ajamista, sitten ajaa ja tarkistaa — viikon 6 käsiajo nyt koodissa.

---

## Yleisiä virhekäsityksiä viikolla 7

Vähintään kaksi virhekäsitystä per oppitunti. Kaksi koskettaa suoraan JS-vs-C#-valintaa, koska viikon 7 opiskelijat päättävät, minkä kielen ottavat AT3:een, ja useita huhuja kiertää.

### Oppitunnin 19 virhekäsitykset

**Virhekäsitys:** *"Pseudokoodi riittää jo — miksi tarvitsemme koodia?"*
**Korjaus:** Pseudokoodi on tarkoitettu ihmisseuraajalle, joka osaa englantia. Tietokone lukee vain pientä sanalistaa, jonka se rakennettiin tuntemaan, eikä pseudokoodi kuulu tuohon listaan. Koodi ei ole "enemmän ajattelua kuin pseudokoodi"; se on sama ajattelu kirjoitettuna sanalistaan, jonka tietokone oikeasti hyväksyy.

**Virhekäsitys:** *"On olemassa yksi 'oikea' tai 'todellinen' ohjelmointikieli ja muut ovat leluja."*
**Korjaus:** Tuhansia ohjelmointikieliä on olemassa. JavaScript ja C# ovat kaksi monista. Ajattelu — sekvenssi, ehto, toisto, muuttujat, syöte, käsittely, tuloste — siirtyy niiden kaikkien yli. Kieli on pinta; ajattelu on pohja.

### Oppitunnin 20 virhekäsitykset

**Virhekäsitys:** *"C# on JavaScriptiä vaikeampi"* (tai päinvastoin — *"JavaScript ei ole oikea kieli, koska se ajetaan selaimessa"*).
**Korjaus:** Kumpikaan väite ei ole totta. C# pyytää nimeämään tyypin (`int`, `string`) siellä, missä JavaScript päättelee sen arvosta; tämä on yksi ylimääräinen sana per esittely, ei eri ajattelutapa. JavaScript ajaa samanlaisia päätöksiä kuin C# — se vain sattuu ajamaan ne selaimessa. Ajattelu siirtyy molempiin suuntiin.

**Virhekäsitys:** *"`console.log` ja `Console.WriteLine` tekevät eri asioita."*
**Korjaus:** Ne tekevät saman asian — tulostavat yhden rivin konsoliin. Sanat eroavat. Työ on identtinen. Niiden näyttäminen rinta rinnan jokaisella O20-kalvolla on vastalääke.

### Oppitunnin 21 virhekäsitykset

**Virhekäsitys:** *"`=` tarkoittaa 'on yhtä suuri kuin'."*
**Korjaus:** `=` on **sijoitus**-operaattori — se laittaa arvon muuttujaan. **Vertailu**-operaattori on `==` (ja JavaScriptissä myös `===`). Tämä kompastuttaa opiskelijoita, jotka ovat nähneet `=`:n vain matematiikan tunnilla. Lue `let age = 16;` ääneen muodossa *"age ottaa arvon 16"*, ei *"age on yhtä suuri kuin 16"*.

**Virhekäsitys:** *"`if` on väärin ilman `else`:tä."*
**Korjaus:** `else` on valinnainen. `if (condition) { … }` yksinään on kelvollista molemmilla kielillä. Monet oikeat ohjelmat käyttävät yksinäisiä `if`:ejä, kun "else"-tapauksessa ei ole mitään tehtävää.

---

## Oppitunti 19 — 90 min suunnitelma

**Aihe.** Miksi ohjelmointikielet ovat olemassa. Syntaksi, käskyt, tulkit ja kääntäjät. Kieliriippumaton — ei toimivaa koodia opiskelijoilta tällä oppitunnilla.

**Tämän oppitunnin keskeinen viesti (yksi lause).** Pseudokoodi on tarpeeksi täsmällistä ihmiselle noudatettavaksi; ohjelmointikieli on tarpeeksi täsmällistä sananmukaiselle tietokoneelle noudatettavaksi — sama ajattelu, tiukemmat sanat.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: laita yksi pala viime viikon pseudokoodia taululle (iän rajoitus -tarkistus on ihanteellinen). Kysy luokalta: *"Voisiko tietokone ajaa tämän täsmälleen niin kuin kirjoitettu?"* Kerää kolme vastausta. Päädy "ei, koska sanat eivät kuulu minkään tietokoneen sanalistaan." | Koko luokka |
| 0:10–0:30 | Opettajan syöte: määrittele *ohjelmointikieli*, *syntaksi*, *käsky*, *tulkki*, *kääntäjä* epämuodollisesti. Nimeä JS ja C#, nimeä yksi tyypillinen käyttötarkoitus kummallekin. Näytä vain yksi side-by-side `Hello`-teaserkalvo — ei live-koodausta luokalta vielä. | Luento |
| 0:30–1:00 | **Itsenäinen työ** (30 min): opiskelijat lukevat `self-study.md`:n O19-osion ja kirjoittavat 4–6 lausetta muistiinpanoihinsa vastauksena: *"Miksi ohjelmointikielen pitää olla olemassa, kun pseudokoodi on jo täsmällistä?"* | Itsenäinen |
| 1:00–1:20 | Pariaktiviteetti: parit vaihtavat vastaukset, löytävät yhden paikan, jossa ovat eri mieltä, merkitsevät sen. Koko luokan debrief poimii kaksi eri mielisyyttä taululta. | Pari |
| 1:20–1:28 | O20:n ennakko: näytä side-by-side `Hello`-kalvo vielä kerran ja kerro luokalle *"seuraavalla oppitunnilla kirjoitat nämä rivit itse."* Kahden minuutin kädennosto: kuka uskoo valitsevansa JS:n, kuka C#:n, kenelle ei vielä mitään ideaa. Kaikki vastaukset ovat ok. | Koko luokka |
| 1:28–1:30 | Lopetus. | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** O19 ei käytä mitään aktiviteettia tiedostosta `in-class-tasks.md` — pakollinen *Konsolirelay* kuuluu O20:een.

**Kalvovinkit — pääsetti `slides.md`.**

- **Lämmittely (0:00–0:10):** kalvo **2** (*Keskeinen kysymys vielä kerran*) ruudulla, kun taulu kantaa elävää "voisiko tietokone ajaa tämän?" -keskustelua.
- **Luento (0:10–0:30):** pääsetin kalvot **3 → 6**: *Mitä tämä viikko harjoittaa* · *Miksi ohjelmointikieli?* · *Mitä syntaksi on?* · *Kaksi kieltä, jotka kohtaamme*. Viivyttele kalvolla 5; syntaksin määritelmä on O19:n keskipiste.
- **Itsenäinen työ (0:30–1:00):** jätä kalvo **4** (*Miksi ohjelmointikieli?*) ruudulle hiljaisena kehotteena kirjoittamiselle.
- **Pariaktiviteetti (1:00–1:20):** ei kalvoja; työ paperilla.
- **O20:n ennakko (1:20–1:28):** kalvo **7** (*Hello, console — rinta rinnan*) näytettynä lyhyesti vain teaserina.

---

## Oppitunti 20 — 90 min suunnitelma

**Aihe.** Ensimmäiset käskyt molemmilla kielillä rinta rinnan: tuloste, arvot, muuttujat, ensimmäinen laskutoimitus. **Kaksikielinen** — molemmat kielet ajavat huoneessa yhtaikaa.

**Tämän oppitunnin keskeinen viesti (yksi lause).** Ohjelma on sananmukaisten käskyjen sarja; "tulosta arvo konsoliin" on yksinkertaisin tällainen käsky kummallakin kielellä.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: live-demo. Avaa selainkonsoli ruudun toiselle puoliskolle ja `dotnetfiddle.net` toiselle. Tulosta `"Hello, class"` kummassakin. Kaksi riviä, kaksi kotia, yksi työ. | Koko luokka |
| 0:10–0:25 | Opettajan syöte: muuttujat, sijoitus, tuloste. Opettaja kirjoittaa yhden esimerkin JS:ssä, sitten saman esimerkin C#:ssa, taululle ruutujen viereen. Tee rinnakkaisuudesta väistämätön. | Luento |
| 0:25–0:55 | **Itsenäinen työ** (30 min): jokainen opiskelija tekee PAKOLLISEN tehtävän valitsemallaan kielellä (`Ensimmäinen konsoliohjelmasi (JS)` tai `Ensimmäinen konsoliohjelmasi (C#)`). Kuvakaappaukset muistiinpanotiedostoon lopuksi. | Itsenäinen |
| 0:55–1:15 | **PAKOLLINEN opettajavetoinen aktiviteetti — *Konsolirelay*** (aktiviteetti A tiedostossa `in-class-tasks.md`, ~20 min). Kuusi pientä katkelmaa (3 JS, 3 C#), näytetty yksi kerrallaan projektorilla. Jokainen opiskelija kirjoittaa ennustuksen; opettaja ajaa katkelman livenä; luokka vertailee. Kielisekoittunut suunnitelmallisesti — jopa JS-opiskelija näkee C#-katkelmat, ja päinvastoin. | Koko luokka |
| 1:15–1:25 | Koko luokan debrief: kerää yksi yllätys per kieli "näimme"-taululle. Yhdistä eksplisiittisesti O19:n "ajattelu on siirrettävää, syntaksi on sopimus" -ideaan. | Koko luokka |
| 1:25–1:30 | Lopetus + O21:n ennakko: *"Seuraavalla oppitunnilla sama side-by-side-temppu sille `if/else`:lle, jota olet kirjoittanut pseudokoodissa kaksi viikkoa."* | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** 55–75 min slotti on **aktiviteetti A — *Konsolirelay*** tiedostosta `in-class-tasks.md`. Valmistele kuusi katkelmaa etukäteen (tiedosto antaa oletusjoukon). Aktiviteetti B tiedostosta `in-class-tasks.md` on valinnainen ja kuuluu O21:een.

**Kalvovinkit — pääsetti `slides.md`.**

- **Lämmittely (0:00–0:10):** kalvot **7** (*Hello, console — rinta rinnan*), **8** (*Selainkonsolin avaaminen*) ja **9** (*Online-C#-ympäristön avaaminen*) järjestyksessä, kun live-demo pyörii ruuduilla.
- **Luento (0:10–0:25):** pääsetin kalvot **10** (*Muuttujat — rinta rinnan*) ja **11** (*Ensimmäinen laskutoimitus — rinta rinnan*). Käy jokainen rivi taululla kalvon vieressä.
- **Itsenäinen työ (0:25–0:55):** jätä kalvo **11** ruudulle hiljaiseksi viitteeksi vuosia-täysi-ikäisyyteen-esimerkille.
- **Tuntiaktiviteetti (0:55–1:15):** kalvo **12** (*Ennusta ennen ajamista*) ruudulla relayn aikana. Itse katkelmat asuvat live-editorissa, eivät kalvolla.
- **Debrief (1:15–1:25):** ei kalvoja; käytä "näimme"-taulua.
- **Lopetus (1:25–1:30):** ei kalvoja.

---

## Oppitunti 21 — 90 min suunnitelma

**Aihe.** Ehdot koodissa: `if`, `else`, vertailut, molemmilla kielillä rinta rinnan. Luovutus AT3:lle.

**Tämän oppitunnin keskeinen viesti (yksi lause).** `if/else` on sama päätös, jota olet kirjoittanut pseudokoodissa kaksi viikkoa — vain välimerkit ovat erilaiset.

| Aika | Aktiviteetti | Muoto |
|---|---|---|
| 0:00–0:10 | Lämmittely: laita viikon 6 iän rajoitus -pseudokoodi taululle. Kysy: *"Miltä tämä näyttäisi koodina?"* Ota kolme arvausta; älä korjaa vielä. | Koko luokka |
| 0:10–0:30 | Opettajan syöte: vertailuoperaattorit taululla (`==`, `!=`, `>=`, `<=`, `>`, `<`); `if/else`-lohkorakenne. Aja täydennyssetti `slides-l21-age-check.md` kokonaisuudessaan — kuusi lyhyttä kalvoa, jotka kuljettavat iän rajoitus -esimerkin pseudokoodista → JS:ksi → C#:ksi. | Luento |
| 0:30–1:00 | **Itsenäinen työ** (30 min): jokainen opiskelija tekee *Ensimmäinen if/else* -syventävän tehtävän valitsemallaan kielellä (`Ensimmäinen if/else (JS)` tai `Ensimmäinen if/else (C#)`). Ennusta, aja, ota kuvakaappaus molemmista ajoista. | Itsenäinen |
| 1:00–1:20 | Pariaktiviteetti — *Käännä naapurisi* (aktiviteetti B tiedostossa `in-class-tasks.md`, ~20 min). Pariuta JS-opiskelija C#-opiskelijan kanssa. Jokainen kääntää toisen `if/else`:n omalle kielelleen käsin, ei LLM:ää. Vertaa alkuperäiseen. | Pari |
| 1:20–1:28 | Luovutus AT3:lle: *"AT3 julkaistaan viikon 8 lopussa. Se pyytää ottamaan yhden palan omaa viikon 6 pseudokoodiasi ja muuttamaan sen ajettavaksi ohjelmaksi sillä kielellä, jonka valitsit tällä viikolla. Tehtävä, jonka juuri teit, on kenraaliharjoitus."* | Koko luokka |
| 1:28–1:30 | Lopetus: huoltotyöt; muistuta opiskelijoita tallentamaan kaiken. | Koko luokka |

**Itsenäisen työn lohko: 30 minuuttia (33 % 90 minuutista).** Täyttää 30–50 %:n säännön.

**Ristiviittaukset.** 60–80 min slotti on **aktiviteetti B — *Käännä naapurisi*** tiedostosta `in-class-tasks.md`. Täydennyssetti `slides-l21-age-check.md` käytetään luentosegmentin aikana.

**Kalvovinkit — pääsetti `slides.md` (ja täydennyssetti `slides-l21-age-check.md`).**

- **Lämmittely (0:00–0:10):** kalvo **12** (*Ennusta ennen ajamista*) ruudulla, kun taulu kantaa viikon 6 pseudokoodia.
- **Luento (0:10–0:30):** pääsetin kalvo **13** (*Vertailuoperaattorit*) operaattoritaulukolle, sitten **vaihda täydennyssettiin `slides-l21-age-check.md` ja aja se päästä päähän** (6 lyhyttä kalvoa). Palaa pääsetin kalvolle **14** (*Ensimmäinen if/else — rinta rinnan*) lopetukseen.
- **Itsenäinen työ (0:30–1:00):** jätä pääsetin kalvo **14** ruudulle hiljaiseksi viitteeksi.
- **Pariaktiviteetti (1:00–1:20):** ei kalvoja; parit työskentelevät paperilla ja ruudulla.
- **AT3-luovutus (1:20–1:28):** pääsetin kalvo **17** (*Kielen valinta AT3:lle*) rauhalliselle ennakolle.
- **Lopetus (1:28–1:30):** kalvo **18** (*Yhteenveto — keskeinen kysymys vielä kerran*), jotta luokka lähtee sananmukaisella keskeisellä kysymyksellä.

---

## Fasilitointivinkit

### Työkalut — sano se ääneen kerran per oppitunti

**IDE-asennusta ei vaadita.** Opiskelijat käyttävät **selaimen DevTools-konsolia** JavaScriptille ja **online-C#-ympäristöä** (.NET Fiddle oletuksena; sharplab.io tai C#-yhteensopiva Replit ovat hyväksyttäviä vaihtoehtoja) C#:lle. Älä asenna Node.js:ää, .NET SDK:ta, Visual Studiota tai VS Codea tälle viikolle. Jos opiskelija ilmestyy paikallisen asennuksen kanssa jo, se on ok — mutta luokka pyörii selaimilla, ja demojen tulee käyttää selaimia, jotta jokainen opiskelija voi seurata.

### Kielisekoittuneen luokkahuoneen hallinta

- **Anna opiskelijoiden valita.** Älä työnnä yhtä kieltä. O19:n loppukädennosto on kysely, ei lajitteluhattu. Opiskelijat voivat vaihtaa O21:een asti ja sen aikana.
- **Pariuta JS-opiskelijat C#-opiskelijoiden kanssa** O21:n pariaktiviteettiin (*Käännä naapurisi*). Käännös on koko pointti; samankieliset parit kaipaavat oppitunnin.
- **Projisoi side-by-side-kalvot jokaiselle käsitteelle.** Älä koskaan projisoi yhden kielen kalvoa käsitteelle, jolla on side-by-side-vastine. Visuaalinen rinnakkaisuus tekee puolet työstä.
- **Kun opiskelija sanoo "C# on vaikeampi" (tai "JS ei ole oikea"),** ohjaa yhdellä lauseella: *"Ne ovat eri pintoja saman ajattelun päällä — näytä missä oikeasti jäit jumiin."* Virhekäsitys melkein aina piilottaa konkreettisen sekaannuksen (puuttuva puolipiste, puuttuva sulkeva lainausmerkki), joka on yhden korjauksen päässä.

### Virheilmoitusten ääneenlukeminen

Kun *Konsolirelay* tuottaa odottamattoman tulosteen tai virheen, **lue virheilmoitus ääneen sana sanalta** ennen kuin sanot mitään muuta. Tämän mallintaminen luokan edessä on viikon 7 paras yksittäinen tapasiirto: opiskelijat, jotka näkevät opettajan lukevan virheilmoituksen ääneen, oppivat, että viesti ei ole satunnaista melua; se on kieli, joka osoittaa riville.

---

## Vastauksia yleisiin opiskelijan kysymyksiin

- *"Minkä kielen valitsisin?"* — Valitse se, joka näyttää vähemmän pelottavalta, kun luet side-by-side-kalvoja. Väärää valintaa ei ole. Voit vaihtaa milloin tahansa ennen AT3:n eräpäivää, mutta on helpompi vaihtaa aikaisemmin kuin myöhemmin.
- *"Onko toinen kielistä toista vaikeampi?"* — Ei. Ne ovat eri pintoja. C# pyytää yhden ylimääräisen sanan (tyypin, esim. `int`) jokaisessa esittelyssä. JavaScript päättelee tyypin arvosta. Kumpikaan ei ole vaikeampi; ne ovat erilaisia.
- *"Riippuuko AT3:n arvosanani siitä, minkä kielen valitsen?"* — Ei. AT3 arvioi ajattelua — tekikö ohjelmasi sen työn, jonka pseudokoodisi kuvasi, ja osaatko puhua siitä rivi riviltä. Kieli on valintasi eikä muuta arviointia.
- *"Tarvitsenko asentaa mitään?"* — Ei. JavaScript ajetaan selaimesi DevTools-konsolissa (`Ctrl+Shift+J` / `Cmd+Opt+J`). C# ajetaan **.NET Fiddlessä** osoitteessa `dotnetfiddle.net`, ilman tiliä.
- *"Voinko käyttää ChatGPT:tä (tai muuta LLM:ää) kirjoittamaan koodini?"* — Voit käyttää LLM:ää **tarkistamaan** kirjoittamasi koodin — vertaamaan vastaustasi toiseen vastaukseen. Et voi palauttaa AT3-koodia, jota et ymmärrä rivi riviltä; AT3 sisältää lyhyen läpikäynnin omasta ohjelmastasi, ja opiskelija, joka ei osaa lukea omaa koodiaan ääneen, ei ole tehnyt tehtävää.
- *"Entä jos virheilmoitus on englannilla, jota en ymmärrä?"* — Lue ensin rivinumero, katso sitä riviä ja jätä loput viestistä huomiotta, kunnes olet lukenut oman koodisi. Puolet kaikista virheilmoituksista osoittavat suoraan puuttuvaan lainausmerkkiin tai puolipisteeseen, joka näkyy paljaalla silmällä sillä rivillä, jonka ne nimeävät.
- *"Onko pseudokoodi kuollut nyt kun meillä on oikea koodi?"* — Ei. Pseudokoodi on yhä ensiluonnos. Oikea koodi on lopullinen luonnos tietokoneelle. AT3 pyytää molempia: viikolla 6 kirjoittamasi pseudokoodin ja siitä tällä viikolla rakentamasi koodin.

---

## Formatiivisen arvioinnin vinkit

Viikko 7 päättyy viikkoa ennen AT3:n laskeutumista. Formatiivisten tarkistusten rooli on tehdä luottamuksesta näkyvää *ennen* kuin AT3 alkaa.

### Oppituntikohtaiset epämuodolliset tarkistukset

- **Oppitunti 19 — exit-tiketti (3 min, tunnin loppu).** Jokainen opiskelija kirjoittaa yhden lauseen: *"Ohjelmointikieltä tarvitaan, ei pelkkää pseudokoodia, koska…"* Selaa nopeasti matkalla O20:een. Jos monet lauseet eivät mainitse sanaa *tietokone*, palaa "sananmukainen tulkitsija" -kehystykseen O20:n alussa.
- **Oppitunti 20 — live-näyttöjen näyttäminen.** Itsenäisen työn lopussa pyydä opiskelijoita nostamaan kannettavansa, jotta huone näkee kunkin konsolin / .NET Fiddlen. Yksi vilkaisu kertoo, mitkä opiskelijat ovat ajaneet jotakin ja mitkä eivät. Älä siirry eteenpäin ennen kuin jokaisella ruudulla on tulostetta.
- **Oppitunti 20 — yhden rivin exit-tiketti.** *"Kirjoita yksi rivi koodia, kummalla tahansa kielellä, joka tulostaa nimesi."* Lue neljä satunnaista ääneen. Huoneessa olevien `console.log`:ien ja `Console.WriteLine`:ien sekoitus on terveellinen ja näyttää, että kaksikielinen kehys on iskenyt sisään.
- **Oppitunti 21 — pariraportti.** Pariaktiviteetin lopussa jokainen pari antaa yhden havainnon: *"Mikä oli sama molemmilla kielillä? Mikä oli erilainen?"* Kuvio huoneen yli kertoo, onko viesti "ajattelu on siirrettävää, syntaksi on sopimus" sisäistetty.
- **Oppitunti 21 — AT3-valmiuden yhden minuutin paperi.** *"Yhdellä lauseella, minkä viikon 6 pseudokoodikappaleen muutat koodiksi AT3:lle?"* Vastaus kertoo viikkoa ennen AT3:n laskeutumista, kuka on jo valinnut materiaalinsa ja kuka tarvitsee tönäisyn.

### Mitä kuuntelet läpi viikon

O21:n loppuun mennessä kolme lausetta merkitsevät aitoa ymmärrystä:

- *"`console.log` ja `Console.WriteLine` tekevät saman asian"* — sanottuna ilman kehotetta opiskelijalta, joka selittää omaa koodiaan.
- *"Ennustin `X`:n, konsoli sanoi `Y`, joten bugi on rivillä `N`"* — viikon 6 käsiajo nyt sovellettuna koodiin.
- *"Teen AT3:n `<kielellä>` koska…"* — ja *koska*-osa viittaa luettavuuteen, ei huhuun vaikeudesta.

Jos nuo lauseet ilmestyvät opiskelijapuheessa O21:n loppuun mennessä, AT3 laskeutuu ilman korjaustoimia ensi viikolla. *Konsolirelay* O20:ssa on keskeinen diagnostiikka — luokka, joka ennustaa kuudesta katkelmasta useimmat oikein, on luokka, joka on valmis AT3:lle.
