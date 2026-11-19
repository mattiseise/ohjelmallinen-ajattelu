# Ohjelmallinen ajattelu — viikko 6

Ensimmäisen vuoden kurssi ammatillisille ICT-opiskelijoille (noin 15–17-vuotiaille, ei aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, 3 oppituntia 90 minuuttia per viikko. Tämä julkaisu sisältää **viikon 6** paketin — kolme oppituntia yhden teeman alla.

Koko kurssi pyörii yhden keskeisen kysymyksen ympärillä:

> **How do I speak to a computer so that it understands what I want it to do?**

## Viikon 6 teema

**Ajattelusta koodiin**

> Pseudokoodi on silta arkikielen ja oikean koodin välillä. Se on tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida.

## Tämän viikon oppitunnit

- **Oppitunti 16**: Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon
- **Oppitunti 17**: Syöte, käsittely, tuloste ja muuttujan idea
- **Oppitunti 18**: Pseudokoodin testaaminen: käsiajo (AT2 palautetaan tämän oppitunnin tienoilla)

## Arvioinnin kosketuspiste

AT2 palautetaan oppitunnin 18 tienoilla.

## Tila

**Tämä julkaisu sisältää vain viikon 6**. Muut viikot ovat omissa julkaisuissaan polussa `material-pipeline/output/computational-thinking-en-week-XX/release/`. Katso täysi 8 viikon tiekartta alta.

## Kanoninen lohkorakenne per viikko

```
opiskelija/viikko-06/
  yleiskatsaus.md      # yhden sivun viikkokatsaus: teema, must-do-minimi vs. syventävä
  itseopiskelu.md      # opiskelijalle suunnattu itseopiskeluteksti, kattaa kaikki kolme oppituntia
  opiskelijatehtavat.md # 1–2 PAKOLLINEN + 2–3 SYVENTÄVÄ -tehtävää
  sanasto.md           # 10–18 termiä englanninkielisillä määritelmillä
  kalvot.md            # ~10–20 Markdown-kalvoa erotettu `---`-merkeillä
opettaja/viikko-06/
  opettajan-materiaalit.md # oppimistavoitteet, virhekäsitykset, kolme 90 min oppituntisuunnitelmaa, formatiivinen arviointi
  tuntitehtavat.md     # vähintään yksi PAKOLLINEN opettajan vetämä luokkahuoneaktiviteetti
```

Jos jokin luento-osio tiedostossa `opettajan-materiaalit.md` tarvitsee syvällisempää materiaalia kuin päälakvosarja tarjoaa, toimitetaan täydentävä kalvosarja `kalvot-o<n>-<aihe>.md` kansiossa `opiskelija/viikko-06/`. Oppitunnin Slide cues -alaosio nimeää täydennyksen.

## Viikon 6 tiedostot

| Viikko | Tila | Tiedostot |
|---|---|---|
| 06 — Ajattelusta koodiin | **rakennettu** | [yleiskatsaus](opiskelija/viikko-06/yleiskatsaus.md) · [itseopiskelu](opiskelija/viikko-06/itseopiskelu.md) · [opiskelijatehtavat](opiskelija/viikko-06/opiskelijatehtavat.md) · [sanasto](opiskelija/viikko-06/sanasto.md) · [kalvot](opiskelija/viikko-06/kalvot.md) · [opettajan-materiaalit](opettaja/viikko-06/opettajan-materiaalit.md) · [tuntitehtavat](opettaja/viikko-06/tuntitehtavat.md) |

## Täysi 8 viikon tiekartta

### Viikko 1 — Ohjelmallinen ajattelu

| O# | Aihe | Tila |
|----|------|------|
| 01 | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkinta | **rakennettu** |
| 02 | Algoritmit arkielämässä: vaihe vaiheelta -ohjeet ilman koodia | **rakennettu** |
| 03 | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen | **rakennettu** |

### Viikko 2 — Ongelman pilkkominen

| O# | Aihe | Tila |
|----|------|------|
| 04 | Ongelman pilkkominen: päätehtävä, osatehtävät ja tavoite | **rakennettu** |
| 05 | Vaiheiden järjestys ja riippuvuudet | **rakennettu** |
| 06 | ICT-tehtävän pilkkominen (AT1 palautetaan) | **rakennettu** |

### Viikko 3 — Prosessin kuvaaminen

| O# | Aihe | Tila |
|----|------|------|
| 07 | Prosessin kuvaaminen: lista, vaihe vaiheelta -rakenne, yksinkertainen vuokaavio | **rakennettu** |
| 08 | Abstraktio | **rakennettu** |
| 09 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | **rakennettu** |

### Viikko 4 — Ratkaisujen vertailu

| O# | Aihe | Tila |
|----|------|------|
| 10 | Sama ongelma, useita ratkaisuja | **rakennettu** |
| 11 | Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virheherkkyys | **rakennettu** |
| 12 | Oman ratkaisun parantaminen ja vertaispalautteen käyttö | **rakennettu** |

### Viikko 5 — Logiikkarakenteet

| O# | Aihe | Tila |
|----|------|------|
| 13 | Sekvenssi: ohjelma etenee vaihe vaiheelta | **rakennettu** |
| 14 | Ehdot: if-then-else -ajattelu ja päätöspuut | **rakennettu** |
| 15 | Toisto: saman asian tekeminen monta kertaa | **rakennettu** |

### Viikko 6 — Ajattelusta koodiin

| O# | Aihe | Tila |
|----|------|------|
| [16](opiskelija/viikko-06/itseopiskelu.md) | Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon | **rakennettu** |
| [17](opiskelija/viikko-06/itseopiskelu.md) | Syöte, käsittely, tuloste ja muuttujan idea | **rakennettu** |
| [18](opiskelija/viikko-06/itseopiskelu.md) | Pseudokoodin testaaminen: käsiajo (AT2 palautetaan) | **rakennettu** |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 1)

| O# | Aihe | Tila |
|----|------|------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript ja C# | suunnitteilla |
| 20 | Ensimmäiset käskyt: console.log / Console.WriteLine, arvot, muuttujat | suunnitteilla |
| 21 | Ehdot koodissa: if, else, vertailut | suunnitteilla |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 2)

| O# | Aihe | Tila |
|----|------|------|
| 22 | Silmukat koodissa: yksinkertainen for- tai while-rakenne | suunnitteilla |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:aan (AT3-rakennuspäivä) | suunnitteilla |
| 24 | Testaaminen, alkeisdebuggaus, 2 minuutin esitys (AT3 palautetaan) | suunnitteilla |

## Lähdetiedot

- Viikon lukittu suunnitelma: `../01-suunnitelma.md`
- Viikon alkuperäinen toimeksianto: `../00-toimeksianto.md`
- Kurssin toimeksianto ja alkuperäinen 24 oppitunnin suunnitelma: `../../computational-thinking-en-week-01/00-brief.md` ja `../../computational-thinking-en-week-01/01-suunnitelma.md`

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaaliputken läpi.
