# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 1 (englanti)

## Työnimi
Ohjelmallinen ajattelu (Computational Thinking)

## Tarkoitus
Antaa aloitteleville ammatillisille ICT-opiskelijoille (~15-vuotiaat) käsitteellinen ymmärrys siitä, miten ohjelmointi toimii, ennen kuin he opiskelevat varsinaista ohjelmointikieltä syvällisemmin. Keskeinen kysymys: *Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?*

## Kohderyhmä
- Ensimmäisen vuoden ammatillisen ICT:n opiskelijat, ikä noin 15–17.
- Aiempaa ohjelmointiosaamista ei oleteta; vain ICT-perustaidot.
- Joukossa voi olla opiskelijoita, joilla on tuen tarpeita, alhainen koulumotivaatio tai vaikeuksia abstraktien käsitteiden kanssa.

## Tuotoskieli
**Englanti.** Börje (suomenkielinen kielenhuolto) jätetään pois tällä ajolla.

## Kurssin kesto
8 viikkoa × 3 oppituntia × 90 min = 24 oppituntia.

## Testilaajuus (tämä ajo)
- **Sune**: tuottaa viikon 1 suunnitelman (kattaa oppitunnit L1–L3 yhtenä viikkopakettina) sekä eteenpäin katsovat luonnokset viikoille 2–8.
- **Rasmus**: rakentaa **täyden viikon 1 paketin** uudessa kanonisessa week-XX -rakenteessa.
- **Linnea/Wilhelm**: auditoivat viikon 1.
- **Alfred**: paketoi viikon 1 julkaisun kalvoineen.

## Kanoninen viikkokohtainen lohkorakenne (lukittu)
```
student/week-XX/
├── overview.md         # viikon teema + ydinminimi vs. syventäminen
├── self-study.md       # 3 oppituntia teoriaa yhdessä dokumentissa
├── student-tasks.md    # 1–2 🟢 SUOSITELTUA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # viikon sanasto
└── slides.md           # viikon Markdown-kalvosarja (---)
teacher/week-XX/
├── teacher-materials.md  # 3 × 90 min fasilitointi
└── in-class-tasks.md     # ≥1 pakollinen opettajavetoinen tuntitehtävä
```

## Viikko 1 — Ohjelmallinen ajattelu (lukitut oppituntien aiheet)
- **L1**: Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen.
- **L2**: Algoritmit arkielämässä: vaiheittaiset ohjeet ilman koodia.
- **L3**: Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen.

## Viikon 1 erityispiirteet
- **Bloom-katto**: vain Muistaminen + Ymmärtäminen. Soveltaminen saa esiintyä kevyesti L2:ssa (ensimmäisten algoritmien kirjoittaminen luonnollisella kielellä) ja L3:ssa (testaaminen ja uudelleenkirjoittaminen), mutta ei tavoitteiden hallitsevana verbinä.
- **Keskeinen kysymys** tulee esiintyä sanatarkasti jossakin kohdassa self-study.md:tä sekä kalvosarjassa.
- **Konkreettiset esimerkit**: arki ennen ICT:tä, aina.
- **30–50 %:n sääntö**: tiedostossa teacher-materials.md jokaisen 90 minuutin oppituntisuunnitelman tulee varata 30–50 % itsenäiseen opiskelutyöhön tunnilla (ei pelkkä luento + ryhmätyö).

## Tehtävät (tämä viikko)
- **SUOSITELTU (1–2)**: pakollinen minimi, AI-kestävä, jokainen ankkuroitu opiskelijan omaan kontekstiin tai tuottaa havaittavia tuotoksia.
- **SYVENTÄVÄ (2–3)**: vapaaehtoinen laajennus. Voi nojata LLM:ään sparrauskumppanina jäsentyneillä kehotteilla, voi syventyä rajatapauksiin tai ammatillisiin näkökulmiin. Edelleen AI-kestävä.

## Kalvot
Tuota `slides.md` käyttäen `---` -merkintää kalvojen erottimena. Jokainen kalvo: selkeä H1/H2-otsikko sekä minimaalinen tukisisältö (3–5 lyhyttä bulletia tai 1–2 lyhyttä virkettä). Tavoittele noin 10–20 kalvoa koko viikolle. Kalvot ovat tuntikäyttöön; ne eivät korvaa itseopiskelua.

## Ulkopuolella
- Ei automaattisia testaus-/debuggauskehyksiä (jest, mocha, vitest).
- Ei suoraa PowerPoint-luontia — Rasmus kirjoittaa `slides.md` (Markdown); orkestraattori muuntaa PPTX:ksi.
- Ei IDE-asennusta, ei Node.js-asennusta.
- Ei alustakohtaisia itsenäisiä harjoituksia (ne tuottaa eri tiimi).
- Ei syvällistä tietojenkäsittelytieteen teoriaa.

## Kielirekisteri
- Itseopiskelu + opiskelijatehtävät: CEFR ~B1.
- Opettajan materiaalit + tuntitehtävät: CEFR ~B2.
- Kalvot: B1, erittäin lyhyet virkkeet.

## Kultainen näyte (kaikkien porttien rakennetta, syvyyttä ja sisältövolyymia varten)
`/Users/agent/ai-perusteet-md/` — Tekoälyn perusteet, Business College Helsinki, julkaistu Netlifyyn.
- Viikkotason volyymi on noin **3×** yksittäinen kultanäyteoppitunti (koska yksi viikon 1 self-study kattaa kolmen oppitunnin sisällön).
- Vertailu koskee vain tyyliä/syvyyttä/volyymia — älä kopioi sisältöä. Tuotoskieli on englanti; vertailuaineisto on suomeksi.

## Aiemman oppitunnin 1 testiajon tila
Aiempi pipeline-ajo tuotti oppituntikohtaisen oppitunnin 1 tuotoksen polkuun:
`/Users/agent/material-pipeline/output/computational-thinking-en/release/`
Tämä viikon 1 ajo **korvaa** kyseisen lähestymistavan uudella viikkokohtaisella jaottelulla. Aiempi tuotos säilytetään vain historiallisena tallenteena, eikä se ole osa tätä julkaisua.
