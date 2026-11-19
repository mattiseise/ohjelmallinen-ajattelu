# Ohjelmallinen ajattelu — Viikko 4

1. vuoden kurssi ammatillisille ICT-opiskelijoille (noin 15–17-vuotiaat, ei aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, 3 oppituntia per viikko 90 minuuttia kerrallaan. Tämä julkaisu sisältää **viikon 4** paketin — kolme oppituntia yhden teeman alla.

Koko kurssi pyörii yhden ydinkysymyksen ympärillä:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

## Viikon 4 teema

**Ratkaisujen vertailu**

> Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.

## Tällä viikolla käsiteltävät oppitunnit

- **Oppitunti 10**: Sama ongelma, useita ratkaisuja
- **Oppitunti 11**: Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virhealttius
- **Oppitunti 12**: Oman ratkaisun parantaminen ja vertaispalaute

## Arviointikosketuspiste

Tällä viikolla ei palauteta arvioitavaa tehtävää. Viikko 4 on kurssin puolivälin reflektiopiste ja syöttää AT2:ta ja AT3:a.

## Tila

**Tämä julkaisu sisältää vain viikon 4**. Muut viikot asuvat omissa julkaisuissaan polun `material-pipeline/output/computational-thinking-en-week-XX/release/` alla. Katso täysi 8-viikon roadmap alta.

## Kanoninen lohkorakenne viikkoa kohden

```
student/week-04/
  overview.md          # yhden sivun viikon yleiskatsaus: teema, must-do minimum vs. syventävä
  self-study.md        # opiskelijalle suunnattu itseopiskeluteksti, joka kattaa kaikki kolme oppituntia
  student-tasks.md     # 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ tehtävää
  vocabulary.md        # 10–18 termiä suomenkielisin määritelmin
  slides.md            # ~10–20 Markdown-kalvoa erotettuna `---`-merkein
teacher/week-04/
  teacher-materials.md # oppimistavoitteet, virhekäsitykset, kolme 90 min:n oppituntisuunnitelmaa, formatiivinen arviointi
  in-class-tasks.md    # vähintään yksi PAKOLLINEN opettajavetoinen tuntiaktiviteetti
```

Jos jokin luentosegmentti `opettajan-materiaalit.md`:ssä tarvitsee syvempää materiaalia kuin pääkalvosetti tarjoaa, täydentävä kalvosetti `kalvot-o<n>-<aihe>.md` toimitetaan polkuun `student/week-04/`. Oppitunnin Kalvovinkit-alajakso nimeää täydennyksen.

## Viikon 4 tiedostot

| Viikko | Tila | Tiedostot |
|---|---|---|
| 04 — Ratkaisujen vertailu | **rakennettu** | [yleiskatsaus](opiskelija/viikko-04/yleiskatsaus.md) · [itseopiskelu](opiskelija/viikko-04/itseopiskelu.md) · [opiskelijatehtavat](opiskelija/viikko-04/opiskelijatehtavat.md) · [sanasto](opiskelija/viikko-04/sanasto.md) · [kalvot](opiskelija/viikko-04/kalvot.md) · [opettajan-materiaalit](opettaja/viikko-04/opettajan-materiaalit.md) · [tuntitehtavat](opettaja/viikko-04/tuntitehtavat.md) |

## Täysi 8-viikon roadmap

### Viikko 1 — Ohjelmallinen ajattelu

| O# | Aihe | Tila |
|----|------|--------|
| 01 | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkinta | **rakennettu** |
| 02 | Algoritmit arkielämässä: vaihe vaiheelta -ohjeet ilman koodia | **rakennettu** |
| 03 | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen | **rakennettu** |

### Viikko 2 — Ongelman pilkkominen

| O# | Aihe | Tila |
|----|------|--------|
| 04 | Ongelman pilkkominen: päätehtävä, alitehtävät ja tavoite | **rakennettu** |
| 05 | Vaiheiden järjestys ja riippuvuudet | **rakennettu** |
| 06 | ICT-tehtävän pilkkominen (AT1 palautettu) | **rakennettu** |

### Viikko 3 — Prosessin kuvaaminen

| O# | Aihe | Tila |
|----|------|--------|
| 07 | Prosessin kuvaaminen: lista, vaihe vaiheelta -rakenne, yksinkertainen vuokaavio | **rakennettu** |
| 08 | Abstraktio | **rakennettu** |
| 09 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | **rakennettu** |

### Viikko 4 — Ratkaisujen vertailu

| O# | Aihe | Tila |
|----|------|--------|
| [10](opiskelija/viikko-04/itseopiskelu.md) | Sama ongelma, useita ratkaisuja | **rakennettu** |
| [11](opiskelija/viikko-04/itseopiskelu.md) | Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virhealttius | **rakennettu** |
| [12](opiskelija/viikko-04/itseopiskelu.md) | Oman ratkaisun parantaminen ja vertaispalaute | **rakennettu** |

### Viikko 5 — Logiikkarakenteet

| O# | Aihe | Tila |
|----|------|--------|
| 13 | Sekvenssi: ohjelma etenee vaihe vaiheelta | suunniteltu |
| 14 | Ehdot: if-then-else -ajattelu ja päätöspuut | suunniteltu |
| 15 | Toisto: saman asian tekeminen monta kertaa | suunniteltu |

### Viikko 6 — Ajattelusta koodiin

| O# | Aihe | Tila |
|----|------|--------|
| 16 | Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon | suunniteltu |
| 17 | Syöte, käsittely, tuloste ja muuttujan idea | suunniteltu |
| 18 | Pseudokoodin testaaminen: käsiajo (AT2 palautettu) | suunniteltu |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 1)

| O# | Aihe | Tila |
|----|------|--------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, komennot, JavaScript ja C# | suunniteltu |
| 20 | Ensimmäiset käskyt: console.log / Console.WriteLine, arvot, muuttujat | suunniteltu |
| 21 | Ehdot koodissa: if, else, vertailut | suunniteltu |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 2)

| O# | Aihe | Tila |
|----|------|--------|
| 22 | Silmukat koodissa: yksinkertainen for- tai while-rakenne | suunniteltu |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:iin (AT3:n rakennuspäivä) | suunniteltu |
| 24 | Testaaminen, alkeistason debuggaus, 2 minuutin esitys (AT3 palautettu) | suunniteltu |

## Totuuden lähde

- Viikon lukittu suunnitelma: `../01-suunnitelma.md`
- Viikon alkuperäinen toimeksianto: `../00-toimeksianto.md`
- Kurssin toimeksianto ja alkuperäinen 24 oppitunnin suunnitelma: `../../computational-thinking-en-week-01/00-brief.md` ja `../../computational-thinking-en-week-01/01-suunnitelma.md`

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaaliputken kautta.
