# Ohjelmallinen ajattelu

Ammatillisten ICT-opiskelijoiden ensimmäisen vuoden kurssi (noin 15–17-vuotiaille, ilman aiempaa ohjelmointikokemusta). Kurssi kestää 8 viikkoa, joiden aikana on 3 oppituntia per viikko, kukin 90 minuuttia — yhteensä 24 oppituntia. Se alkaa arkisista ohjeista, joita teini-ikäinen jo joka päivä antaa, etenee vähitellen osituksen, abstraktion, sekvenssin, ehdon ja toiston kautta ja kääntää tämän ajattelun vasta kahden viimeisen viikon aikana pieneksi selainpohjaiseksi JavaScript-ohjelmaksi. Ohjelmointia käsitellään viimeisenä kerroksena; ajattelu on se, mitä kurssi todella treenaa.

Koko kurssi pyörii yhden keskeisen kysymyksen ympärillä:

> **Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?**

## Tila

**Tämä julkaisu sisältää vain oppitunnin 1.** Koko 24 oppitunnin suunnitelma on lukittu tiedostoon `01-suunnitelma.md` projektin juuressa, ja oppitunnit 2–24 tuotetaan myöhemmissä pipeline-ajoissa. Kansiorakenne alla on jo lopullisessa muodossaan, joten jokainen tuleva oppitunti voidaan pudottaa kansioihin `student/lesson-XX/` ja `teacher/lesson-XX/` ilman muun rakenteen muuttamista.

## Kanoninen lohkorakenne per oppitunti

Jokainen kurssin oppitunti toimitetaan neljänä Markdown-tiedostona kahdessa kansiossa. Tiedostonimet ovat tarkalleen pienillä kirjaimilla, kebab-case-muodossa:

```
student/lesson-XX/
  self-study.md        # opiskelijoille suunnattu itseopiskeluteksti (800–1400 sanaa)
  student-tasks.md     # 1–2 tehtävää, vähintään yksi tekoälykestävä (400–900 sanaa)
  vocabulary.md        # 6–10 termiä, vähintään yksi eteenpäin katsova esimakutermi
teacher/lesson-XX/
  teacher-materials.md # tavoitteet, virhekäsitykset, 90 min suunnitelma, arviointi (800–1400 sanaa)
```

Viides tiedosto — `teacher/lesson-XX/teacher-led-tasks.md` — on **valinnainen** ja lisätään vain silloin, kun oppitunti aidosti tarvitsee erillisen opettajavetoisen ryhmäaktiviteetin. Oppitunti 1 ei tarvitse.

## Oppituntien hakemisto

| Oppitunti | Otsikko | Tiedostot |
|---|---|---|
| 01 | Tietokoneelle puhuminen — mitä se oikeasti kuulee? | [itseopiskelu](opiskelija/oppitunti-01/itseopiskelu.md) · [opiskelijatehtävät](opiskelija/oppitunti-01/opiskelijatehtavat.md) · [sanasto](opiskelija/oppitunti-01/sanasto.md) · [opettajan-materiaalit](opettaja/oppitunti-01/opettajan-materiaalit.md) |

## Koko 24 oppitunnin etenemissuunnitelma

Kurssi on ryhmitelty viikoittain. Vain oppitunti 01 on rakennettu tähän julkaisuun; loput ovat **suunniteltuja** ja tuotetaan myöhemmissä pipeline-ajoissa. Kolme arvioitavaa tehtävää (AT1 viikolla 2/3, AT2 noin viikoilla 5/6, AT3 viikolla 8) on kaikki suunniteltu tekoälykestäviksi: jokainen vaatii opiskelijan oman kontekstin, oman tuotoksen ja lyhyen suullisen tai tallennetun osuuden.

### Viikko 1 — Ohjelmallinen ajattelu

| O# | Aihe | Tila |
|----|------|--------|
| [01](opiskelija/oppitunti-01/itseopiskelu.md) | Mitä ohjelmallinen ajattelu tarkoittaa? Ihmiset, tietokoneet ja ohjeiden tulkitseminen | **rakennettu** |
| 02 | Algoritmit arkielämässä: vaihe vaiheelta annetut ohjeet ilman koodia | suunniteltu |
| 03 | Täsmälliset ja epätäsmälliset ohjeet: ohjeiden testaaminen ja parantaminen | suunniteltu |

### Viikko 2 — Ongelman pilkkominen

| O# | Aihe | Tila |
|----|------|--------|
| 04 | Ongelman pilkkominen: päätehtävä, alitehtävät ja tavoite | suunniteltu |
| 05 | Vaiheiden järjestys ja riippuvuudet | suunniteltu |
| 06 | ICT-tehtävän pilkkominen (AT1 palautettu) | suunniteltu |

### Viikko 3 — Prosessin kuvaaminen

| O# | Aihe | Tila |
|----|------|--------|
| 07 | Prosessin kuvaaminen: lista, vaiheittainen rakenne ja yksinkertainen vuokaavio | suunniteltu |
| 08 | Abstraktio | suunniteltu |
| 09 | Uudelleenkäytettävät ohjeet ja funktion idea ilman koodia | suunniteltu |

### Viikko 4 — Ratkaisujen vertailu

| O# | Aihe | Tila |
|----|------|--------|
| 10 | Sama ongelma, useita ratkaisuja | suunniteltu |
| 11 | Ratkaisujen arviointikriteerit | suunniteltu |
| 12 | Oman ratkaisun parantaminen ja vertaispalautteen hyödyntäminen | suunniteltu |

### Viikko 5 — Logiikkarakenteet

| O# | Aihe | Tila |
|----|------|--------|
| 13 | Sekvenssi | suunniteltu |
| 14 | Ehdot: if-then-else -ajattelu | suunniteltu |
| 15 | Toisto | suunniteltu |

### Viikko 6 — Ajattelusta koodiin

| O# | Aihe | Tila |
|----|------|--------|
| 16 | Pseudokoodi | suunniteltu |
| 17 | Syöte, käsittely, tuloste ja muuttujan idea | suunniteltu |
| 18 | Pseudokoodin testaaminen: käsiajo (AT2 palautettu) | suunniteltu |

### Viikko 7 — Ohjelmointikielet käytännössä (JavaScript, osa 1)

| O# | Aihe | Tila |
|----|------|--------|
| 19 | Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt, JavaScript | suunniteltu |
| 20 | Ensimmäiset JavaScript-käskyt: console.log, arvot, muuttujat | suunniteltu |
| 21 | Ehdot JavaScriptissä: if, else, vertailut | suunniteltu |

### Viikko 8 — Ohjelmointikielet käytännössä (JavaScript, osa 2)

| O# | Aihe | Tila |
|----|------|--------|
| 22 | Silmukat JavaScriptissä: for tai while | suunniteltu |
| 23 | Pieni käytännön tehtävä: pseudokoodista JavaScriptiin | suunniteltu |
| 24 | Testaus, virheiden korjaaminen, esitys (AT3 palautettu ja esitetty) | suunniteltu |

## Lähde, johon nojataan

- `../01-suunnitelma.md` — lukittu kurssisuunnitelma: koko 24 oppitunnin taulukko, oppimistavoitteet Bloomin tasoittain, arvioinnin rakenne, laajuusrajat ja 17 hyväksymiskriteeriä, jotka jokaisen oppitunnin tulee täyttää.
- `../00-toimeksianto.md` — alkuperäinen toimeksianto, josta suunnitelma on johdettu.

Jos jokin tässä julkaisussa on ristiriidassa suunnitelman kanssa, suunnitelma voittaa. Lähetä korjaukset takaisin materiaalipipelinen kautta.
