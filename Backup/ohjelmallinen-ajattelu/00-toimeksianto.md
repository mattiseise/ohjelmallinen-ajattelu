# Toimeksianto — Ohjelmallisen ajattelun kurssi (englanniksi)

## Työnimi
Computational Thinking

## Tarkoitus
Antaa aloitteleville ammatillisille ICT-opiskelijoille (~15-vuotiaille) käsitteellinen ymmärrys siitä, miten ohjelmointi toimii, ennen kuin he opiskelevat varsinaista ohjelmointikieltä syvällisesti. Kurssin ydinkysymys on: *Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?*

## Kohderyhmä
- Ammatillisen ICT-koulutuksen 1. vuoden opiskelijat, ikä noin 15–17 v.
- Aiempaa ohjelmointiosaamista ei oleteta; perus-ICT-taidot riittävät
- Mukana voi olla opiskelijoita, jotka tarvitsevat tukea, joiden koulumotivaatio on heikko tai joilla on vaikeuksia abstraktien käsitteiden kanssa
- Ammatillinen toinen aste — käytännön merkityksellisyys on kriittistä

## Tuotoksen kieli
**Englanti** — koko kurssi englanniksi. Börje (suomenkielinen kielenhuoltoportti) ohitetaan tällä ajolla.

## Kurssin kesto
8 viikkoa × 3 oppituntia viikossa × 90 min = yhteensä 24 oppituntia.

## Tämän ajon testilaajuus
- **Sune**: lukitse koko 24 oppitunnin suunnitelma + hyväksymiskriteerit + Rasmuksen ohjeistus oppituntia 1 varten.
- **Rasmus**: rakenna **vain viikko 1 / oppitunti 1** ("Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen") täydellä kanonisella 4-lohkon rakenteella.
- **Linnea / Wilhelm**: auditoi vain oppitunti 1.
- **Alfred**: paketoi yksittäinen oppitunti Netlify-yhteensopivaksi julkaisuksi, jossa kurssitason README osoittaa täydelliseen suunnitelmaan.

## Kanoninen lohkorakenne per oppitunti (lukittu)
```
student/lesson-XX/
├── self-study.md
├── student-tasks.md
└── vocabulary.md
teacher/lesson-XX/
└── teacher-materials.md
```
**Ei kalvoja.** Jos jokin toimeksiannossa viittaa kalvoihin, kohtele niitä laajuuden ulkopuolisina.

## Kurssin yleiset tavoitteet
- Ymmärtää ohjelmallinen ajattelu, algoritmi ja abstraktio.
- Pilkkoa ongelma pienempiin osiin.
- Kuvata prosessi loogisessa järjestyksessä.
- Tunnistaa sekvenssi, ehto ja toisto.
- Ymmärtää pseudokoodi.
- Siirtyä luonnollisesta kielestä muodollisiin ohjeisiin.
- Saada ensimmäinen tutustuminen JavaScriptiin käytännön esimerkkien kautta (vain viikot 7–8).

## Pedagogiset periaatteet
- Erittäin käytännönläheinen, ammatillisesti realistinen.
- Arkiesimerkit ensin, ICT-esimerkit toiseksi.
- Ohjelmoinnin käsitteitä harjoitellaan ilman koodia ennen koodia.
- Virheet käsitellään luonnollisina; paljon konkreettisia harjoituksia.
- Käsitteisiin palataan useissa muodoissa (arki → prosessi → pseudokoodi → JavaScript).
- Tuki vähän motivoituneille / heikon abstraktiokyvyn opiskelijoille: pohjat, mallivastaukset, strukturoidut vaihtoehdot.

## Viikkokohtaiset teemat (toimeksiannosta)
1. Ohjelmallinen ajattelu
2. Ongelman pilkkominen
3. Prosessin kuvaaminen
4. Ratkaisujen vertailu
5. Logiikkarakenteet
6. Ajattelusta koodiin
7–8. Ohjelmointikielet käytännössä: JavaScript

## Oppituntikohtaiset aiheet (toimeksianto-PDF:stä, lukitut)
| Vk | O# | Aihe |
|----|----|----|
| 1 | 1 | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen |
| 1 | 2 | Algoritmit arkielämässä: vaihe vaiheelta annetut ohjeet ilman koodia |
| 1 | 3 | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen |
| 2 | 4 | Ongelman pilkkominen: päätehtävä, alitehtävät ja tavoite |
| 2 | 5 | Vaiheiden järjestys ja riippuvuudet |
| 2 | 6 | ICT-tehtävän pilkkominen |
| 3 | 7 | Prosessin kuvaaminen: lista, vaiheittainen rakenne ja yksinkertainen vuokaavio |
| 3 | 8 | Abstraktio |
| 3 | 9 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia |
| 4 | 10 | Sama ongelma, useita ratkaisuja |
| 4 | 11 | Ratkaisujen arviointikriteerit |
| 4 | 12 | Oman ratkaisun parantaminen ja vertaispalautteen hyödyntäminen |
| 5 | 13 | Sekvenssi |
| 5 | 14 | Ehdot: if-then-else -ajattelu |
| 5 | 15 | Toisto |
| 6 | 16 | Pseudokoodi |
| 6 | 17 | Syöte, käsittely, tuloste ja muuttujan idea |
| 6 | 18 | Pseudokoodin testaaminen: käsiajo |
| 7 | 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript |
| 7 | 20 | Ensimmäiset JavaScript-käskyt: console.log, arvot, muuttujat |
| 7 | 21 | Ehdot JavaScriptissä: if, else, vertailut |
| 8 | 22 | Silmukat JavaScriptissä: for tai while |
| 8 | 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin |
| 8 | 24 | Testaus, virheiden korjaaminen, esitys |

## Arvioitavat osat (lukitut)
- **AT1** — Viikon 2 lopussa / viikon 3 alussa — arkisen tai ICT-tehtävän pilkkominen vaiheisiin.
- **AT2** — Viikon 5 lopussa / viikon 6 aikana — prosessikuvaus, jossa on sekvenssi, ehto ja toisto.
- **AT3** — Viikko 8 — pieni JavaScript-ratkaisu pseudokoodista.

## Työkalut (sallitut)
Selain + konsoli, tekstieditori, paperia, valinnainen vuokaaviotyökalu, valinnainen Scratch/Blockly. Ei monimutkaisia asennuksia.

## Kultainen näyte (tyyli, rakenne, sisällön määrä — sama kaikille porteille)
`/Users/agent/ai-perusteet-md/` — Tekoälyn perusteet (Business College Helsinki, 27 oppituntia, suomeksi, julkaistu Netlifyssä GitHubin kautta).
- Tyylin/rakenteen/määrän viite kullekin oppitunnille: `/Users/agent/ai-perusteet-md/student/lesson-01/` ja `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`.
- Viite on tarkoitettu **tyyliä, syvyyttä ja sisällön määrää** varten — älä kopioi sisältöä. Tuotoksen kieli on englanti; viite on suomeksi.
