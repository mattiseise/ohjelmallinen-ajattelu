# Ohjelmallinen ajattelu — viikko 3

Ensimmäisen vuoden kurssi ammatillisille ICT-opiskelijoille (noin 15–17-vuotiaita, ei aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, 3 oppituntia á 90 minuuttia viikossa. Tämä julkaisu sisältää **viikon 3** paketin — kolme oppituntia yhden teeman alla.

Koko kurssi pyörii yhden keskeisen kysymyksen ympärillä:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

## Viikon 3 teema

**Prosessin kuvaaminen**

> Kun osaat pilkkoa ongelman, seuraava taito on kuvata prosessi niin, että joku muu voi suorittaa sen — ja päättää, mitkä yksityiskohdat ovat tärkeitä ja mitkä voidaan turvallisesti piilottaa.

## Tämän viikon oppitunnit

- **Oppitunti 07**: Prosessin kuvaaminen: lista, vaiheittainen rakenne, yksinkertainen vuokaavio
- **Oppitunti 08**: Abstraktio
- **Oppitunti 09**: Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia

## Arvioinnin kosketuspiste

Tällä viikolla ei palauteta arvioitavaa tehtävää. Viikko 3 rakentaa sanastoa AT2:ta varten viikoilla 5–6.

## Tila

**Tämä julkaisu sisältää vain viikon 3**. Muut viikot ovat omissa julkaisuissaan polun `material-pipeline/output/computational-thinking-en-week-XX/release/` alla. Katso täysi 8 viikon tiekartta alta.

## Kanoninen lohkorakenne per viikko

```
opiskelija/viikko-03/
  yleiskatsaus.md         # yhden sivun viikkokatsaus: teema, must-do-minimi vs. syventävä
  itseopiskelu.md         # opiskelijalle suunnattu itseopiskeluteksti, kattaa kaikki kolme oppituntia
  opiskelijatehtavat.md   # 1–2 PAKOLLISTA + 2–3 SYVENTÄVÄÄ tehtävää
  sanasto.md              # 10–18 termiä englanninkielisin määritelmin
  kalvot.md               # ~10–20 Markdown-kalvoa erotettuna `---`-rivein
opettaja/viikko-03/
  opettajan-materiaalit.md  # oppimistavoitteet, virhekäsitykset, kolme 90 min oppituntisuunnitelmaa, formatiivinen arviointi
  tuntitehtavat.md          # vähintään yksi PAKOLLINEN opettajavetoinen tuntiaktiviteetti
```

Jos jokin luento-osio tiedostossa `opettajan-materiaalit.md` tarvitsee syvempää materiaalia kuin pääkalvosetti tarjoaa, lisäsetti `kalvot-o<n>-<aihe>.md` toimitetaan polussa `opiskelija/viikko-03/`. Oppitunnin kalvovihjeet-alaosio nimeää lisäsetin.

## Viikon 3 tiedostot

| Viikko | Tila | Tiedostot |
|---|---|---|
| 03 — Prosessin kuvaaminen | **rakennettu** | [yleiskatsaus](opiskelija/viikko-03/yleiskatsaus.md) · [itseopiskelu](opiskelija/viikko-03/itseopiskelu.md) · [opiskelijatehtavat](opiskelija/viikko-03/opiskelijatehtavat.md) · [sanasto](opiskelija/viikko-03/sanasto.md) · [kalvot](opiskelija/viikko-03/kalvot.md) · [opettajan-materiaalit](opettaja/viikko-03/opettajan-materiaalit.md) · [tuntitehtavat](opettaja/viikko-03/tuntitehtavat.md) |

## Täysi 8 viikon tiekartta

### Viikko 1 — Ohjelmallinen ajattelu

| O# | Aihe | Tila |
|----|------|------|
| 01 | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkinta | **rakennettu** |
| 02 | Algoritmit arkielämässä: vaiheittaiset ohjeet ilman koodia | **rakennettu** |
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
| [07](opiskelija/viikko-03/itseopiskelu.md) | Prosessin kuvaaminen: lista, vaiheittainen rakenne, yksinkertainen vuokaavio | **rakennettu** |
| [08](opiskelija/viikko-03/itseopiskelu.md) | Abstraktio | **rakennettu** |
| [09](opiskelija/viikko-03/itseopiskelu.md) | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | **rakennettu** |

### Viikko 4 — Ratkaisujen vertaileminen

| O# | Aihe | Tila |
|----|------|------|
| 10 | Sama ongelma, useita ratkaisuja | suunniteltu |
| 11 | Ratkaisujen arviointikriteerit: selkeys, tehokkuus, toistettavuus, virhealttius | suunniteltu |
| 12 | Oman ratkaisun parantaminen ja vertaispalautteen käyttäminen | suunniteltu |

### Viikko 5 — Logiikkarakenteet

| O# | Aihe | Tila |
|----|------|------|
| 13 | Sekvenssi: ohjelma etenee vaihe vaiheelta | suunniteltu |
| 14 | Ehdot: if-then-else -ajattelu ja päätöspuut | suunniteltu |
| 15 | Toisto: saman asian tekeminen monta kertaa | suunniteltu |

### Viikko 6 — Ajattelusta koodiin

| O# | Aihe | Tila |
|----|------|------|
| 16 | Pseudokoodi: luonnollisesta kielestä täsmällisempään muotoon | suunniteltu |
| 17 | Syöte, käsittely, tuloste ja muuttujan idea | suunniteltu |
| 18 | Pseudokoodin testaaminen: käsiajo (AT2 palautetaan) | suunniteltu |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 1)

| O# | Aihe | Tila |
|----|------|------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript ja C# | suunniteltu |
| 20 | Ensimmäiset käskyt: console.log / Console.WriteLine, arvot, muuttujat | suunniteltu |
| 21 | Ehdot koodissa: if, else, vertailut | suunniteltu |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript & C#, osa 2)

| O# | Aihe | Tila |
|----|------|------|
| 22 | Silmukat koodissa: yksinkertainen for- tai while-rakenne | suunniteltu |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin tai C#:iin (AT3-rakennuspäivä) | suunniteltu |
| 24 | Testaaminen, aloittelijatason debuggaus, 2 minuutin esitys (AT3 palautetaan) | suunniteltu |

## Totuuden lähde

- Viikon lukittu suunnitelma: `../01-suunnitelma.md`
- Viikon alkuperäinen toimeksianto: `../00-toimeksianto.md`
- Kurssin toimeksianto ja alkuperäinen 24 oppitunnin suunnitelma: `../../computational-thinking-en-week-01/00-brief.md` ja `../../computational-thinking-en-week-01/01-suunnitelma.md`

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaalipipelinin kautta.
