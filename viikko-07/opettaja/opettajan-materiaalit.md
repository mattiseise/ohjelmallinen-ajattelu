# Viikko 7 — Opettajan materiaalit

Tämä dokumentti kattaa viikon 7 kaikki kolme oppituntia (L19, L20, L21) samassa paikassa. Viikko rakentuu saman
ydinviestin ympärille, jonka opiskelijat näkevät:
“Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone voi seurata niitä arvaamatta. Ajattelu
on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain syntaksi, johon se kirjoitetaan.”
Viikko 7 on silta koodiin. Kuusi viikkoa pseudokoodia, järjestys–ehto–toistoa, pilkkomista ja kuivaharjoittelua
kohtaavat oikean syntaksin ensimmäistä kertaa — ja kahdessa kielessä, JavaScriptissä ja C#:ssa, rinnakkain, ei
peräkkäin. AT3 julkaistaan viikon 8 lopussa, ei tällä viikolla. Viikon 7 tehtävä on tehdä AT3:n aloittamisesta tylsää:
opiskelija, joka on kirjoittanut tällä viikolla kolme toimivaa riviä valitsemallaan kielellä, avaa AT3-ohjeen ensi viikolla
ja tunnistaa muodon heti.
Jokainen tehtävä tiedostoissa student-tasks-js.md ja student-tasks-csharp.md sisältää tästä syystä AT3-
muistutuksen. Varsinaista IDEä ei käytetä. Ei node-komentoa, ei npm:ää, ei dotnet new -komentoa, ei Visual
Studiota, VS Codea eikä JetBrains Rideria. JavaScript ajetaan selaimen DevTools-konsolissa. C# ajetaan .NET
Fiddlessä (dotnetfiddle.net); sharplab.io ja C#-tuettu Replit ovat hyväksyttäviä vaihtoehtoja. Automaattisia
testaus- tai debuggauskehyksiä ei käytetä. Taso on: kokeile, aja, katso mitä tapahtuu, lue tuloste.
Ristiinviittaukset: lisäpakkaa slides-l21-age-check.md käytetään L21:n opetusosuudessa. Pakollinen tuntitehtävä
Console relay kuvataan tiedostossa in-class-tasks.md, ja se kuuluu L20:n 55–75 minuutin jaksoon.
Vinkki opettajalle: Pidä JS ja C# koko ajan rinnakkain. Tarkoitus ei ole opettaa kahta erillistä kurssia, vaan näyttää,
että sama ajattelu kirjoitetaan kahdella eri pinnalla.

## Viikon 7 oppimistavoitteet (Bloom-taksonomian mukaan)

Viikko 7 pysyy tasoilla Ymmärtäminen ja Soveltaminen. Viikon 7 tavoitteissa vältettävät verbit ovat analysoida,
arvioida, suunnitella, luoda, rakentaa, debugata, refaktoroida, optimoida. AT3 viikolla 8 on se kohta, jossa luomista
muistuttava työ tulee mukaan.

### Oppitunti 19 — Miksi ohjelmointikieliä tarvitaan (kieliriippumaton)

• Ymmärtäminen: opiskelija osaa määritellä epämuodollisesti omin sanoin sanat ohjelmointikieli, syntaksi,
komento, tulkki ja kääntäjä.
• Ymmärtäminen: opiskelija osaa selittää, miksi ohjelmointikieltä tarvitaan, vaikka pseudokoodi on jo
täsmällistä — oikea tietokone ei pysty lukemaan englanninkielisillä avainsanoilla kirjoitettua pseudokoodia.
• Ymmärtäminen: opiskelija osaa tunnistaa, että sama algoritmi voidaan kirjoittaa eri kielillä ja se voi silti
tarkoittaa samaa asiaa.
• Ymmärtäminen: opiskelija osaa nimetä kaksi todellista ohjelmointikieltä (JavaScript, C#) ja yhden
tyypillisen käyttöpaikan kummallekin (JS = selain; C# = .NET, Unity).

### Oppitunti 20 — Ensimmäiset komennot: tulostus, arvot, muuttujat (kaksi kieltä)

• Soveltaminen: opiskelija osaa ajaa ensimmäisen ohjelman, joka tulostaa tekstiä konsoliin:
JavaScriptissä tai C#:ssa.

```javascript
console.log("…") Console.WriteLine("…")
```

• Soveltaminen: opiskelija osaa määritellä muuttujan ja antaa sille arvon: let JS:ssä, tyypitetyt määrittelyt
(int, string) C#:ssa.
• Soveltaminen: opiskelija osaa tulostaa muuttujan arvon, myös yhdistämällä tekstiä ja arvoja +-merkillä.
• Soveltaminen: opiskelija osaa tehdä yksinkertaisen laskun (vuodet täysi-ikäisyyteen, kokonaishinta) ja
tulostaa tuloksen.
• Ymmärtäminen: opiskelija osaa tunnistaa, että ajattelu — lue arvo, laske, tulosta — on sama molemmissa
kielissä.

### Oppitunti 21 — Ehdot koodissa: if, else ja vertailut (kaksi kieltä)

• Soveltaminen: opiskelija osaa kirjoittaa vertailulausekkeen (age >= 18) molemmilla kielillä ja tunnistaa,
että vertailuoperaattorit ovat käytännössä samat.
• Soveltaminen: opiskelija osaa kirjoittaa ensimmäisen -lohkon, joka tulostaa yhden kahdesta `if/else`
viestistä muuttujan mukaan.
• Soveltaminen: opiskelija osaa liittää viikon 6 pseudokoodin (IF age >= 18 THEN … ELSE …)
valitsemansa kielen koodiin.
• Soveltaminen: opiskelija osaa ennustaa pienen if/else-ohjelman tulosteen ennen ajamista, ajaa sen ja
tarkistaa — viikon 6 kuivaharjoittelu, nyt koodissa.

## Viikon 7 yleiset väärinkäsitykset

Alla on vähintään kaksi väärinkäsitystä per oppitunti. Kaksi niistä koskee suoraan JS-vs.-C#-valintaa, koska viikon 7
opiskelijat päättävät, kumman kielen vievät AT3:een, ja luokassa liikkuu helposti huhuja.

### Oppitunnin 19 väärinkäsitykset

Väärinkäsitys: “Pseudokoodi riittää jo — miksi tarvitsemme koodia?”
Korjaus: Pseudokoodi on ihmiselle, joka lukee englanninkielisiä ohjeita. Tietokone lukee vain sen pienen sanalistan,
jonka se on rakennettu tuntemaan, eikä pseudokoodi ole sillä listalla. Koodi ei ole “enemmän ajattelua kuin
pseudokoodi”; se on sama ajattelu kirjoitettuna sanalistalla, jonka tietokone todella hyväksyy.
Väärinkäsitys: “On yksi ‘oikea’ tai ‘aito’ ohjelmointikieli ja muut ovat leluja.”
Korjaus: Ohjelmointikieliä on tuhansia. JavaScript ja C# ovat kaksi monista. Ajattelu — järjestys, ehto, toisto,
muuttujat, syöte, käsittely, tuotos — siirtyy kaikkiin niihin. Kieli on pinta; ajattelu on lattia.

### Oppitunnin 20 väärinkäsitykset

Väärinkäsitys: “C# on vaikeampi kuin JavaScript” tai päinvastoin “JavaScript ei ole oikea kieli, koska se toimii
selaimessa”.
Korjaus: Kumpikaan ei pidä paikkaansa. C# pyytää nimeämään tyypin (int, string), kun JavaScript päättelee sen
arvosta. Se on yksi lisäsana per muuttujan määrittely, ei erilainen ajattelutapa. JavaScript tekee samoja päätöksiä
kuin C# — se vain sattuu toimimaan selaimessa. Ajattelu siirtyy molempiin suuntiin.
Väärinkäsitys: “console.log ja Console.WriteLine tekevät eri asioita.”
Korjaus: Ne tekevät saman asian: tulostavat yhden rivin konsoliin. Sanat eroavat. Tehtävä on sama. Niiden
näyttäminen rinnakkain jokaisella L20-dialla on paras vastalääke.

### Oppitunnin 21 väärinkäsitykset

Väärinkäsitys: “= tarkoittaa ‘on yhtä suuri kuin’.”
Korjaus: = on sijoitusoperaattori — se laittaa arvon muuttujaan. Vertailuoperaattori on == (ja JavaScriptissä
myös ===). Tämä kompastuttaa opiskelijoita, jotka ovat nähneet =-merkin vain matematiikassa. Lue let age = 16;
ääneen muodossa “age saa arvon 16”, ei “age on yhtä suuri kuin 16”.
Väärinkäsitys: “if on väärin ilman else-osaa.”
Korjaus: else on valinnainen. if (condition) { … } yksinään on kelvollinen molemmissa kielissä. Monissa oikeissa
ohjelmissa käytetään yksinäisiä if-lauseita, kun “muuten”-tapauksessa ei tarvitse tehdä mitään.

## Oppitunti 19 — 90 minuutin suunnitelma

Aihe. Miksi ohjelmointikieliä on olemassa. Syntaksi, komennot, tulkit ja kääntäjät. Kieliriippumaton — opiskelijat eivät
vielä kirjoita toimivaa koodia tällä tunnilla.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Pseudokoodi on riittävän täsmällistä ihmiselle; ohjelmointikieli on
riittävän täsmällistä kirjaimelliselle tietokoneelle — sama ajattelu, tiukemmat sanat.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: laita taululle yksi pala viime Koko ryhmä
viikon pseudokoodia, mieluiten ikärajan
tarkistus. Kysy ryhmältä: “Voisiko
tietokone ajaa tämän täsmälleen näin
kirjoitettuna?” Kerää kolme vastausta.
Päädy vastaukseen “ei, koska sanat
eivät ole minkään tietokoneen
sanalistalla”.
0:10–0:30 Opettajan osuus: määrittele Opetuspuhe
epämuodollisesti ohjelmointikieli,
syntaksi, komento, tulkki ja kääntäjä.
Nimeä JS ja C#, kerro yksi tyypillinen
käyttöpaikka kummallekin. Näytä yksi
rinnakkainen Hello-teaser-dia — ei vielä
livekoodausta opiskelijoilta.
0:30–1:00 Itsenäinen työ (30 min): opiskelijat Itsenäinen
lukevat self-study.md-tiedoston L19-
osan ja kirjoittavat muistiinpanoihinsa 4–
6 virkettä vastauksena: “Miksi
ohjelmointikieltä tarvitaan, kun
pseudokoodi on jo täsmällistä?”
1:00–1:20 Parityö: parit vaihtavat vastauksia, Pari
löytävät yhden kohdan, josta ovat eri
mieltä, ja merkitsevät sen. Koko ryhmän
purku nostaa taululta kaksi
Aika Toiminta Muoto
erimielisyyttä.
1:20–1:28 Ennakko L20:stä: näytä rinnakkainen Koko ryhmä
Hello-dia vielä kerran ja sano ryhmälle:
“seuraavalla tunnilla kirjoitatte nämä rivit
itse.” Kahden minuutin käsiäänestys:
kuka arvelee valitsevansa JS:n, kuka
C#:n, kuka ei vielä tiedä. Kaikki
vastaukset ovat ok.
1:28–1:30 Lopetus. Koko ryhmä
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. L19 ei käytä tehtävää tiedostosta ; pakollinen Console relay kuuluu L20:een. `in-class-tasks.md`
Diavihjeet — pääpakka . `slides.md`
• Lämmittely (0:00–0:10): dia 2 (Ydinkysymys vielä kerran) näkyviin samalla, kun taulu kantaa keskustelua
“voisiko tietokone ajaa tämän?”.
• Opettajan osuus (0:10–0:30): pääpakan diat 3 → 6: Mitä tämä viikko harjoittaa · Miksi ohjelmointikieli? ·
Mitä syntaksi on? · Kaksi kieltä, jotka tapaamme. Viivy diassa 5; syntaksin määritelmä on L19:n
käännekohta.
• Itsenäinen työ (0:30–1:00): jätä dia 4 (Miksi ohjelmointikieli?) näkyviin hiljaiseksi kirjoituskehotteeksi.
• Parityö (1:00–1:20): ei dioja; työ paperilla.
• L20-ennakko (1:20–1:28): dia 7 (Hello, console — rinnakkain) näytetään lyhyesti vain teaserina.

## Oppitunti 20 — 90 minuutin suunnitelma

Aihe. Ensimmäiset komennot molemmissa kielissä rinnakkain: tulostus, arvot, muuttujat, ensimmäinen lasku. Kaksi
kieltä — molemmat kielet ajetaan luokassa samaan aikaan.
Tämän oppitunnin ydinviesti yhdellä virkkeellä. Ohjelma on kirjaimellisten komentojen järjestys; “tulosta arvo
konsoliin” on kummassakin kielessä yksinkertaisin tällainen komento.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: live-demo. Avaa Koko ryhmä
selainkonsoli näytön toiselle puolikkaalle
ja dotnetfiddle.net toiselle. Tulosta
kummassakin "Hello, class". Kaksi riviä,
kaksi kotia, yksi tehtävä.
0:10–0:25 Opettajan osuus: muuttujat, sijoitus, Opetuspuhe
tulostus. Opettaja kirjoittaa yhden
esimerkin JS:llä ja sitten saman
esimerkin C#:lla taululle näyttöjen
viereen. Tee rinnakkaisuus
väistämättömäksi.
0:25–0:55 Itsenäinen työ (30 min): jokainen Itsenäinen
opiskelija tekee PAKOLLISEN tehtävän
valitsemallaan kielellä (Your first
console program (JS) tai Your first
console program (C#)).
Kuvakaappaukset
muistiinpanotiedostoon lopuksi.
0:55–1:15 PAKOLLINEN opettajajohtoinen Koko ryhmä
tehtävä — Console relay (tehtävä A
tiedostossa in-class-tasks.md, noin 20
min). Kuusi pientä koodipätkää (3 JS, 3
C#), yksi kerrallaan projektorilla.
Jokainen opiskelija kirjoittaa ennusteen;
opettaja ajaa pätkän livenä; ryhmä
vertaa. Kielisekoitus on tarkoituksellinen
— myös JS-opiskelija näkee C#-pätkät
ja päinvastoin.
1:15–1:25 Koko ryhmän purku: kerää yksi yllätys Koko ryhmä
per kieli taululle otsikon “näimme” alle.
Aika Toiminta Muoto
Kytke selvästi L19:n ajatukseen:
“ajattelu on siirrettävää, syntaksi on
sopimus.”
1:25–1:30 Lopetus + L21-ennakko: “Seuraavalla Koko ryhmä
tunnilla sama rinnakkainen temppu
if/else-rakenteelle, jota olette
kirjoittaneet pseudokoodina kaksi
viikkoa.”
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 55–75 minuutin jakso on Tehtävä A — Console relay tiedostosta in-class-tasks.md.
Valmistele kuusi pätkää etukäteen; tiedosto antaa oletussetin. Tehtävä B tiedostosta in-class-tasks.md on
valinnainen ja kuuluu L21:een.
Vinkki opiskelijalle: Kun näet console.log ja Console.WriteLine, lue molemmat mielessä “tulosta rivi konsoliin”.
Silloin erot ovat kirjoitusasua, eivät uutta ajattelua.
Diavihjeet — pääpakka slides.md.
• Lämmittely (0:00–0:10): diat 7 (Hello, console — rinnakkain), 8 (Selainkonsolin avaaminen) ja 9 (Online C#
-ympäristön avaaminen) järjestyksessä samalla, kun live-demo pyörii näytöillä.
• Opettajan osuus (0:10–0:25): pääpakan diat 10 (Muuttujat — rinnakkain) ja 11 (Ensimmäinen lasku —
rinnakkain). Käy jokainen rivi taululla dian vieressä.
• Itsenäinen työ (0:25–0:55): jätä dia 11 näkyviin hiljaiseksi viitteeksi vuosia täysi-ikäisyyteen -esimerkille.
• Tuntitehtävä (0:55–1:15): dia 12 (Ennusta ennen kuin ajat) näkyviin releen aikana. Pätkät itse elävät live-
editorissa, eivät diassa.
• Purku (1:15–1:25): ei dioja; käytä “näimme”-taulua.
• Lopetus (1:25–1:30): ei dioja.

## Oppitunti 21 — 90 minuutin suunnitelma

Aihe. Ehdot koodissa: , , vertailut, molemmissa kielissä rinnakkain. Siirto AT3:een. `if else`
Tämän oppitunnin ydinviesti yhdellä virkkeellä. on sama päätös, jota olet kirjoittanut pseudokoodina `if/else`
kaksi viikkoa — vain välimerkit ovat erilaisia.
Aika Toiminta Muoto
0:00–0:10 Lämmittely: laita taululle viikon 6 ikäraja- Koko ryhmä
pseudokoodi. Kysy: “Miltä tämä näyttäisi
koodina?” Ota kolme arvausta; älä vielä
korjaa.
0:10–0:30 Opettajan osuus: vertailuoperaattorit Opetuspuhe
taululle (==, !=, >=, <=, >, <); if/else-
lohkon rakenne. Käytä lisäpakka slides-
l21-age-check.md kokonaan — kuusi
lyhyttä diaa kuljettaa ikärajaesimerkin
pseudokoodista → JS:ään → C#:aan.
0:30–1:00 Itsenäinen työ (30 min): jokainen Itsenäinen
opiskelija tekee First if/else -syventävän
tehtävän valitsemallaan kielellä (First
if/else (JS) tai First if/else (C#)).
Ennusta, aja, ota kuvakaappaus
molemmista ajoista.
1:00–1:20 Parityö — Translate-your-neighbour Pari
(tehtävä B tiedostossa in-class-
tasks.md, noin 20 min). Parita JS-
opiskelija C#-opiskelijan kanssa.
Jokainen kääntää parin if/else-
rakenteen omaan kieleensä käsin, ei
LLM:llä. Verratkaa alkuperäiseen.
1:20–1:28 Siirto AT3:een: “AT3 julkaistaan viikon 8 Koko ryhmä
lopussa. Siinä pyydetään ottamaan yksi
Aika Toiminta Muoto
pala omaa viikon 6 pseudokoodia ja
muuttamaan se toimivaksi ohjelmaksi
kielellä, jonka valitsit tällä viikolla. Juuri
tekemäsi tehtävä on kenraaliharjoitus.”
1:28–1:30 Lopetus: käytännön asiat; muistuta Koko ryhmä
opiskelijoita tallentamaan kaikki.
Itsenäisen työn jakso: 30 minuuttia (33 % 90 minuutista). Täyttää 30–50 % -säännön.
Ristiinviittaukset. 60–80 minuutin jakso on Tehtävä B — Translate-your-neighbour tiedostosta in-class-
tasks.md. Lisäpakkaa slides-l21-age-check.md käytetään opetusosuudessa.
Diavihjeet — pääpakka slides.md ja lisäpakka slides-l21-age-check.md.
• Lämmittely (0:00–0:10): dia 12 (Ennusta ennen kuin ajat) näkyviin samalla, kun taulu kantaa viikon 6
pseudokoodin.
• Opettajan osuus (0:10–0:30): pääpakan dia 13 (Vertailuoperaattorit) operaattoritaulukkoon, sitten vaihda
lisäpakkaan slides-l21-age-check.md ja käytä se alusta loppuun (6 lyhyttä diaa). Palaa pääpakan
diaan 14 (Ensimmäinen if/else — rinnakkain) sulkemista varten.
• Itsenäinen työ (0:30–1:00): jätä pääpakan dia 14 näkyviin hiljaiseksi viitteeksi.
• Parityö (1:00–1:20): ei dioja; parit työskentelevät paperilla ja näytöillä.
• AT3-siirto (1:20–1:28): pääpakan dia 17 (Kielen valitseminen AT3:een) rauhalliseen ennakkoon.
• Lopetus (1:28–1:30): dia 18 (Kertaus — ydinkysymys vielä kerran) niin, että ryhmä lähtee sanasta sanaan
-ydinkysymyksen kanssa.

## Fasilitointivinkit

### Työkalut — sano ääneen kerran per oppitunti

IDE-asennusta ei tarvita. Opiskelijat käyttävät selaimen DevTools-konsolia JavaScriptille ja online C#
-ympäristöä (oletuksena .NET Fiddle; sharplab.io tai C#-tuettu Replit ovat hyväksyttäviä vaihtoehtoja) C#:lle. Älä
asenna Node.js:ää, .NET SDK:ta, Visual Studiota tai VS Codea tätä viikkoa varten. Jos opiskelijalla on paikallinen
asennus valmiina, se on ok — mutta luokka toimii selaimilla, ja demojen pitää käyttää selaimia, jotta jokainen voi
seurata.

### Kielisekoitteisen luokan ohjaaminen

• Anna opiskelijoiden valita. Älä työnnä ketään yhteen kieleen. L19:n lopun käsiäänestys on kysely, ei
lajitteluhattu. Opiskelija saa vaihtaa L21:een saakka ja sen aikana.
• Parita JS-opiskelijat C#-opiskelijoiden kanssa L21:n parityössä (Translate-your-neighbour). Kääntäminen
on koko pointti; saman kielen parit menettävät oppitunnin.
• Projisoi rinnakkaiset diat jokaiselle käsitteelle. Älä koskaan näytä yhden kielen diaa käsitteestä, jolle on
rinnakkainen versio. Visuaalinen rinnakkaisuus tekee puolet työstä.
• Kun opiskelija sanoo “C# on vaikeampi” tai “JS ei ole oikea”, ohjaa yhdellä virkkeellä: “Ne ovat eri
pintoja saman ajattelun päällä — näytä missä oikeasti jäit jumiin.” Väärinkäsityksen takaa löytyy melkein
aina konkreettinen sekaannus (puuttuva puolipiste, puuttuva lainausmerkki), joka on yhden korjauksen
päässä.

### Virheilmoitusten lukeminen ääneen

Kun Console relay tuottaa odottamattoman tuloksen tai virheen, lue virheilmoitus ääneen sanasta sanaan ennen
kuin sanot mitään muuta. Tämän mallintaminen luokan edessä on viikon 7 paras tavan siirto: opiskelijat, jotka
näkevät opettajan lukevan virheilmoituksen ääneen, oppivat, ettei viesti ole satunnaista kohinaa; se on kieli, joka
osoittaa riville.

## Vastauksia yleisiin opiskelijakysymyksiin

• “Minkä kielen valitsen?” — Valitse se, joka näyttää vähemmän pelottavalta, kun luet rinnakkaisia dioja. Ei ole
väärää valintaa. Voit vaihtaa milloin tahansa ennen AT3:n palautusta, mutta aikaisemmin vaihtaminen on
helpompaa kuin myöhemmin.
• “Onko toinen kieli vaikeampi?” — Ei. Ne ovat eri pintoja. C# pyytää yhden lisäsanan (tyypin, esimerkiksi int)
jokaisessa määrittelyssä. JavaScript päättelee tyypin arvosta. Kumpikaan ei ole vaikeampi; ne ovat erilaisia.
• “Riippuuko AT3-arvosanani siitä, minkä kielen valitsen?” — Ei. AT3 arvioi ajattelua: tekeekö ohjelma sen
työn, jonka pseudokoodi kuvasi, ja pystytkö puhumaan siitä rivi riviltä. Kieli on sinun valintasi eikä muuta
arviointia.
• “Tarvitsenko asennuksia?” — Et. JavaScript toimii selaimen DevTools-konsolissa (Ctrl+Shift+J /
Cmd+Opt+J). C# toimii .NET Fiddlessä osoitteessa dotnetfiddle.net ilman tiliä.
• “Saanko käyttää ChatGPT:tä tai muuta LLM:ää koodin kirjoittamiseen?” — Voit käyttää LLM:ää
tarkistamaan kirjoittamaasi koodia — vertaamaan vastaustasi toiseen vastaukseen. Et voi palauttaa AT3-
koodia, jota et ymmärrä rivi riviltä. AT3 sisältää lyhyen oman ohjelman läpikäynnin, ja opiskelija, joka ei
pysty lukemaan omaa koodiaan ääneen, ei ole tehnyt tehtävää.
• “Mitä jos virheilmoitus on englantia, jota en ymmärrä?” — Lue ensin rivinumero, katso sitä riviä ja jätä muu
viesti hetkeksi huomiotta, kunnes olet lukenut oman koodisi. Puolet virheilmoituksista osoittaa suoraan
puuttuvaan lainausmerkkiin tai puolipisteeseen rivillä, jonka viesti nimeää.
• “Onko pseudokoodi nyt kuollut, kun meillä on oikeaa koodia?” — Ei. Pseudokoodi on edelleen ensimmäinen
luonnos. Oikea koodi on lopullinen luonnos tietokoneelle. AT3 pyytää molemmat: viikon 6 pseudokoodin ja
siitä tällä viikolla rakennettavan koodin.

## Formatiivisen arvioinnin vinkit

Viikko 7 päättyy viikkoa ennen AT3:n tuloa. Formatiivisten tarkistusten tehtävä on tehdä varmuus näkyväksi ennen
AT3:n alkamista.

### Oppituntikohtaiset epämuodolliset tarkistukset

• Oppitunti 19 — poistumislappu (3 min tunnin lopussa). Jokainen opiskelija kirjoittaa yhden virkkeen:
“Ohjelmointikieltä tarvitaan, ei pelkkää pseudokoodia, koska…” Silmäile matkalla L20:een. Jos moni virke ei
mainitse sanaa tietokone, palaa “kirjaimellinen tulkki” -kehykseen L20:n alussa.
• Oppitunti 20 — live-näyttökatsaus. Itsenäisen työn lopussa pyydä opiskelijoita nostamaan läppäreitä niin,
että huone näkee jokaisen konsolin / .NET Fiddlen. Yhdellä vilkaisulla näet, kuka on ajanut jotakin ja kuka ei.
Älä jatka ennen kuin jokaisella näytöllä on tulostetta.
• Oppitunti 20 — yhden rivin poistumislappu. “Kirjoita yksi koodirivi jommallakummalla kielellä, joka
tulostaa nimesi.” Lue neljä satunnaisesti ääneen. Huoneen sekoitus console.log- ja Console.WriteLine-
rivejä on terve merkki siitä, että kahden kielen kehys on asettunut.
• Oppitunti 21 — parien raportointi. Parityön lopussa jokainen pari antaa yhden havainnon: “Mikä oli samaa
molemmissa kielissä? Mikä oli erilaista?” Huoneen malli kertoo, onko viesti “ajattelu siirtyy, syntaksi on
sopimus” sisäistetty.
• Oppitunti 21 — AT3-valmiuden yhden minuutin paperi. “Minkä viikon 6 pseudokoodin aiot muuttaa
koodiksi AT3:ssa?” Vastaus kertoo viikkoa ennen AT3:a, kuka on jo valinnut materiaalin ja kuka tarvitsee
tönäisyä.

### Mitä kuuntelet koko viikon ajan

L21:n loppuun mennessä kolme ilmausta merkitsee aitoa ymmärrystä:
• “console.log ja Console.WriteLine tekevät saman asian” — opiskelijan sanomana ilman kehotusta
hänen omasta koodistaan.
• “Ennustin X, konsoli sanoi Y, joten bugi on rivillä N” — viikon 6 kuivaharjoittelu siirtyneenä koodiin.
• *“Teen AT3:n kielellä __, koska…“* — ja koska viittaa luettavuuteen, ei huhuun vaikeudesta.
Jos nämä ilmaukset näkyvät opiskelijoiden puheessa L21:n loppuun mennessä, AT3 tulee ensi viikolla ilman
korjaavaa kertausta. L20:n Console relay on viikon keskeinen diagnostiikka: ryhmä, joka ennustaa suurimman osan
kuudesta pätkästä oikein, on valmis AT3:een.
