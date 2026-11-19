# Ohjelmallinen ajattelu — viikko 2

Ensimmäisen vuoden kurssi ammatillisille ICT-opiskelijoille (noin 15–17-vuotiaita, ei aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, joista kullakin on 3 oppituntia á 90 minuuttia per viikko. Tämä julkaisu sisältää **viikon 2** paketin — kolme oppituntia ryhmiteltynä yhden teeman alle.

Koko kurssi kääntyy yhden keskeisen kysymyksen ympärillä:

> **Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?**

## Viikon 2 teema

**Ongelman pilkkominen**

> Iso ongelma muuttuu hallittavaksi ongelmaksi, kun nimeät päätehtävän, sen osatehtävät ja järjestyksen, jossa ne on tehtävä.

## Tällä viikolla käsiteltävät oppitunnit

- **Oppitunti 04**: Ongelman pilkkominen: päätehtävä, osatehtävät ja tavoite
- **Oppitunti 05**: Vaiheiden järjestys ja riippuvuudet
- **Oppitunti 06**: ICT-tehtävän pilkkominen (AT1 palautetaan)

## Arvioinnin liityntäkohta

AT1 (pilkota arkielämän tai ICT-tehtävä vaiheisiin) palautetaan oppitunnin 6 lopussa.

## Tila

**Tämä julkaisu sisältää vain viikon 2**. Muut viikot asuvat omissa julkaisuissaan polussa `material-pipeline/output/computational-thinking-en-week-XX/release/`. Katso täysi 8 viikon tiekartta alta.

## Viikon kanoninen lohkorakenne

```
student/week-02/
  overview.md          # yhden sivun viikkokatsaus: teema, must-do minimum vs. syventävä
  self-study.md        # opiskelijalle suunnattu itseopiskeluteksti kaikista kolmesta oppitunnista
  student-tasks.md     # 1–2 MANDATORY + 2–3 DEEPENING tehtävää
  vocabulary.md        # 10–18 termiä englanninkielisillä määritelmillä
  slides.md            # ~10–20 Markdown-kalvoa eroteltuna `---`-rivein
teacher/week-02/
  teacher-materials.md # oppimistavoitteet, virhekäsitykset, kolme 90 min:n oppituntisuunnitelmaa, formatiivinen arviointi
  in-class-tasks.md    # vähintään yksi MANDATORY opettajajohtoinen luokkahuoneaktiviteetti
```

Jos `teacher-materials.md`:n luentojakso tarvitsee syvempää materiaalia kuin pääkalvodek tarjoaa, täydentävä dek `slides-l<n>-<topic>.md` toimitetaan `student/week-02/`-kansiossa. Oppitunnin Slide cues -alaosio nimeää täydentävän dekin.

## Viikon 2 tiedostot

| Viikko | Tila | Tiedostot |
|---|---|---|
| 02 — Ongelman pilkkominen | **rakennettu** | [yleiskatsaus](opiskelija/viikko-02/yleiskatsaus.md) · [itseopiskelu](opiskelija/viikko-02/itseopiskelu.md) · [opiskelijatehtävät](opiskelija/viikko-02/opiskelijatehtavat.md) · [sanasto](opiskelija/viikko-02/sanasto.md) · [kalvot](opiskelija/viikko-02/kalvot.md) · [opettajan materiaalit](opettaja/viikko-02/opettajan-materiaalit.md) · [tuntitehtävät](opettaja/viikko-02/tuntitehtavat.md) |

## Täysi 8 viikon tiekartta

### Viikko 1 — Ohjelmallinen ajattelu

| O# | Aihe | Tila |
|----|------|--------|
| 01 | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkinta | **rakennettu** |
| 02 | Algoritmit arkielämässä: vaihe vaiheelta annetut ohjeet ilman koodia | **rakennettu** |
| 03 | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen | **rakennettu** |

### Viikko 2 — Ongelman pilkkominen

| O# | Aihe | Tila |
|----|------|--------|
| [04](opiskelija/viikko-02/itseopiskelu.md) | Ongelman pilkkominen: päätehtävä, osatehtävät ja tavoite | **rakennettu** |
| [05](opiskelija/viikko-02/itseopiskelu.md) | Vaiheiden järjestys ja riippuvuudet | **rakennettu** |
| [06](opiskelija/viikko-02/itseopiskelu.md) | ICT-tehtävän pilkkominen (AT1 palautetaan) | **rakennettu** |

### Viikko 3 — Prosessin kuvaaminen

| O# | Aihe | Tila |
|----|------|--------|
| 07 | Prosessin kuvaaminen: lista, vaihe vaiheelta -rakenne, yksinkertainen vuokaavio | suunniteltu |
| 08 | Abstraktio | suunniteltu |
| 09 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | suunniteltu |

### Viikko 4 — Ratkaisujen vertailu

| O# | Aihe | Tila |
|----|------|--------|
| 10 | Sama ongelma, useita ratkaisuja | suunniteltu |
| 11 | Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virhealttius | suunniteltu |
| 12 | Oman ratkaisun parantaminen ja vertaispalaute | suunniteltu |

### Viikko 5 — Logiikan rakenteet

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
| 18 | Pseudokoodin testaaminen: käsiajo (AT2 palautetaan) | suunniteltu |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 1)

| O# | Aihe | Tila |
|----|------|--------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript ja C# | suunniteltu |
| 20 | Ensimmäiset käskyt: console.log / Console.WriteLine, arvot, muuttujat | suunniteltu |
| 21 | Ehdot koodissa: if, else, vertailut | suunniteltu |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 2)

| O# | Aihe | Tila |
|----|------|--------|
| 22 | Silmukat koodissa: yksinkertainen for- tai while-rakenne | suunniteltu |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:iin (AT3-rakennuspäivä) | suunniteltu |
| 24 | Testaaminen, aloittelijatason debuggaus, 2 minuutin esitys (AT3 palautetaan) | suunniteltu |

## Lähde

- Viikon lukittu suunnitelma: `../01-suunnitelma.md`
- Viikon alkuperäinen toimeksianto: `../00-toimeksianto.md`
- Kurssin toimeksianto ja alkuperäinen 24 oppitunnin suunnitelma: `../../computational-thinking-en-week-01/00-brief.md` ja `../../computational-thinking-en-week-01/01-suunnitelma.md`

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaaliputken läpi.
