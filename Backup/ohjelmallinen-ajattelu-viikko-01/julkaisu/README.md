# Ohjelmallinen ajattelu

Ensimmäisen vuoden kurssi ammatillisen ICT:n opiskelijoille (noin 15–17-vuotiaat, ei aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, ja viikossa on 3 oppituntia á 90 minuuttia — yhteensä 24 oppituntia. Se alkaa arkisista ohjeista, joita teini-ikäinen jo päivittäin antaa, etenee vähitellen osituksen, abstraktion, sekvenssin, ehdon ja toiston kautta, ja vasta kahdella viimeisellä viikolla kääntää ajattelun pieneksi selainpohjaiseksi JavaScript-ohjelmaksi. Ohjelmointia kohdellaan viimeisenä kerroksena; ajattelu on se mitä kurssi oikeasti harjoittelee.

Koko kurssi pyörii yhden keskeisen kysymyksen ympärillä:

> **Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?**

## Tila

Tämä julkaisu sisältää vain **viikon 1** (oppitunnit 1–3). Täysi 24 oppitunnin suunnitelma on lukittuna projektin juuressa tiedostossa `01-suunnitelma.md`; viikot 2–8 tuotetaan myöhemmissä pipeline-ajoissa. Alla oleva kansioasettelu on jo lopullisessa muodossaan, joten jokainen tuleva viikko voidaan pudottaa kansioon `student/week-XX/` ja `teacher/week-XX/` muuta uudelleenjärjestämättä.

## Kanoninen viikkokohtainen lohkorakenne

Jokainen kurssin viikko toimitetaan seitsemänä Markdown-tiedostona kahdessa kansiossa. Tiedostonimet ovat tarkkoja, pienaakkosin ja kebab-case-muodossa:

```
student/week-XX/
  overview.md          # yhden sivun viikkokatsaus: teema, can-do-lauseet, ydin vs. syventäminen
  self-study.md        # opiskelijalle suunnattu itseopiskeluteksti kaikille kolmelle oppitunnille
  student-tasks.md     # 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ tehtävää
  vocabulary.md        # 10–18 termiä englanninkielisin määritelmin, mukaan lukien yksi eteenpäin katsova esikatselutermi
  slides.md            # ~10–20 Markdown-slideä erotettuna `---`-merkillä; orkestraattori muuntaa PPTX:ksi
teacher/week-XX/
  teacher-materials.md # oppimistavoitteet, virhekäsitykset, kolme 90-min oppituntisuunnitelmaa, formatiivinen arviointi
  in-class-tasks.md    # vähintään yksi PAKOLLINEN opettajavetoinen luokkatehtävä, sekä vapaaehtoisia lisiä
```

Kalvot toimitetaan vain Markdownina (`slides.md`); PPTX-muunnos tapahtuu tämän julkaisun jälkeen.

## Viikkohakemisto

| Viikko | Tila | Tiedostot |
|---|---|---|
| 01 — Ohjelmallinen ajattelu | **rakennettu** | [yleiskatsaus](student/week-01/overview.md) · [itseopiskelu](student/week-01/self-study.md) · [opiskelijatehtävät](student/week-01/student-tasks.md) · [sanasto](student/week-01/vocabulary.md) · [kalvot](student/week-01/slides.md) · [opettajan-materiaalit](teacher/week-01/teacher-materials.md) · [tuntitehtävät](teacher/week-01/in-class-tasks.md) |

## Täysi 8 viikon suunnitelma

Kurssi on ryhmitelty viikoittain. Vain viikko 1 on rakennettu tässä julkaisussa; loput ovat **suunniteltuja** ja tuotetaan myöhemmissä pipeline-ajoissa. Kolme arvioitavaa tehtävää (AT1 viikon 2 lopussa, AT2 noin viikolla 6, AT3 viikolla 8) on jokainen ankkuroitu opiskelijan omaan kontekstiin, omaan tuotokseen ja lyhyeen suulliseen tai nauhoitettuun osuuteen.

### Viikko 1 — Ohjelmallinen ajattelu

| L# | Aihe | Tila |
|----|------|------|
| [01](student/week-01/self-study.md) | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen | **rakennettu** |
| [02](student/week-01/self-study.md) | Algoritmit arkielämässä: vaiheittaiset ohjeet ilman koodia | **rakennettu** |
| [03](student/week-01/self-study.md) | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen | **rakennettu** |

### Viikko 2 — Ongelman pilkkominen

| L# | Aihe | Tila |
|----|------|------|
| 04 | Ongelman pilkkominen: päätehtävä, alitehtävät ja tavoite | suunniteltu |
| 05 | Vaiheiden järjestys ja riippuvuudet | suunniteltu |
| 06 | ICT-tehtävän pilkkominen (AT1 palautetaan) | suunniteltu |

### Viikko 3 — Prosessin kuvaaminen

| L# | Aihe | Tila |
|----|------|------|
| 07 | Prosessin kuvaaminen: lista, vaiheittainen rakenne ja yksinkertainen vuokaavio | suunniteltu |
| 08 | Abstraktio | suunniteltu |
| 09 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | suunniteltu |

### Viikko 4 — Ratkaisujen vertailu

| L# | Aihe | Tila |
|----|------|------|
| 10 | Sama ongelma, useita ratkaisuja | suunniteltu |
| 11 | Ratkaisujen arviointikriteerit | suunniteltu |
| 12 | Oman ratkaisun parantaminen ja vertaispalaute | suunniteltu |

### Viikko 5 — Logiikkarakenteet

| L# | Aihe | Tila |
|----|------|------|
| 13 | Sekvenssi | suunniteltu |
| 14 | Ehdot: if-then-else -ajattelu | suunniteltu |
| 15 | Toisto | suunniteltu |

### Viikko 6 — Ajattelusta koodiin

| L# | Aihe | Tila |
|----|------|------|
| 16 | Pseudokoodi | suunniteltu |
| 17 | Syöte, käsittely, tuloste ja muuttujan idea | suunniteltu |
| 18 | Pseudokoodin testaaminen: käsiajo (AT2 palautetaan) | suunniteltu |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript, osa 1)

| L# | Aihe | Tila |
|----|------|------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript | suunniteltu |
| 20 | Ensimmäiset JavaScript-käskyt: console.log, arvot, muuttujat | suunniteltu |
| 21 | Ehdot JavaScriptissä: if, else, vertailut | suunniteltu |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript, osa 2)

| L# | Aihe | Tila |
|----|------|------|
| 22 | Silmukat JavaScriptissä: for tai while | suunniteltu |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin | suunniteltu |
| 24 | Testaus, debuggaus, esitys (AT3 palautetaan ja esitetään) | suunniteltu |

## Lähde totuudelle

- `../01-suunnitelma.md` — lukittu viikon 1 suunnitelma ja kurssikonteksti, jota Sune käytti tämän ajon rajaamiseen: viikon 1 viikkokohtainen erittely (L1–L3-tavoitteet, sanasto, ydinminimi vs. syventäminen), eteenpäin katsovat luonnokset viikoille 2–8, laajuusrajat ja 29 hyväksymiskriteeriä, jotka jokaisen viikkopaketin on täytettävä.
- `../00-brief.md` — alkuperäinen toimeksianto, josta suunnitelma johdettiin.

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaalipipelinen kautta.
