# Viikko 5 — Kolme liikettä: sekvenssi, ehto, toisto

Ohjelmallinen ajattelu

Ensimmäisen vuoden ammatillinen ICT-kurssi

---

## Keskeinen viesti

**Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto.**

Kun osaat nimetä nämä arkisissa tehtävissä, sinulla on jokaisen ohjelman luuranko.

---

## Mitä tämä viikko harjoittaa

- Oppitunti 13 — **sekvenssi**: asioiden tekeminen järjestyksessä
- Oppitunti 14 — **ehdot**: seuraavan vaiheen päättäminen
- Oppitunti 15 — **toisto**: saman asian tekeminen uudelleen, lopetuksella

Vain selkokieltä. Ei vielä koodia.

---

## Sekvenssi — oletusarvoinen liike

Sekvenssi on yhden vaiheen tekemistä toisensa perään, kiinteässä järjestyksessä.

Teeresepti:

1. Täytä keitin.
2. Kytke se päälle.
3. Laita teepussi mukiin.
4. Kaada kiehuva vesi.

---

## Kun järjestys merkitsee

Vaihda vaiheet 2 ja 4:

1. Täytä keitin.
2. *Kaada kiehuva vesi.*
3. Laita teepussi mukiin.
4. *Kytke keitin päälle.*

Sananmukainen tulkitsija kaataa kylmää vettä ja katsoo tyhjää keitintä. Se järjestys, jonka kirjoitat, on se järjestys, jonka saat.

---

## Sekvenssi työssä — käyttöönottolista

1. Yhdistä uusi haara.
2. Aja build.
3. Aja smoke-testit.
4. Vie staging-ympäristöön.
5. Hanki hyväksyntä.
6. Vie tuotantoon.

Sama muoto kuin teereseptillä. Useita vaiheita ei voi järjestää uudelleen rikkomatta prosessia.

---

## Ehto — testi, joka jakaa polun

Ehto on testi, joka päättää, mikä vaihe tapahtuu seuraavaksi.

*"Jos sataa, mene bussilla; muuten kävele."*

Ehto on se hetki, jolloin polku haarautuu.

---

## if … then … else …

Arki: *jos sataa, niin mene bussilla, muuten kävele.*

ICT-peilikuva: *jos salasana on lyhyempi kuin 8 merkkiä, niin hylkää, muuten hyväksy.*

Sama muoto. Eri ympäristö.

---

## Päätöspuu — jakautumisen piirtäminen

```
        Sataako?
        /        \
      kyllä       ei
      /            \
mene bussilla   kävele
```

Kynä ja paperi riittää. Piirtäminen pakottaa rehelliseen testiin jokaisessa haarassa.

---

## Ehto työssä — salasanan tarkistus

- **if** lyhyempi kuin 8 merkkiä, **then** hylkää
- **if** ei numeroa, **then** hylkää
- **if** ei isoa kirjainta, **then** hylkää
- **muutoin** hyväksy

Ehtoketju, joka päättyy kahteen lopputulokseen.

---

## Toisto — tekeminen uudelleen, lopetuksella

Toisto on saman vaiheen tekemistä useammin kuin kerran, lopetusehdon kanssa, jonka tulkitsija näkee.

Arki: *jokaiselle nimelle luettelossa, merkitse läsnä tai poissa.*

---

## Toiston kolme muotoa

- **for each** — lista on tiedossa etukäteen.
- **repeat until** — lopetus riippuu siitä, mitä tapahtuu.
- **while** — testi tarkistetaan ennen jokaista toistoa.

Kaikki kolme tarvitsevat rehellisen, havaittavan lopetuksen.

---

## Toisto työssä — sähköpostien läpikäynti

> **for each** lukematon viesti sähköpostissa:
> &nbsp;&nbsp;&nbsp;&nbsp;**if** henkilöltä, merkitse vastattavaksi;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** uutiskirje, arkistoi;
> &nbsp;&nbsp;&nbsp;&nbsp;**else if** roskaposti, poista.
> Toista, kunnes sähköposti on tyhjä.

Kaikki kolme rakennuspalikkaa yhdessä prosessissa.

---

## Lopetusehto on turvavyö

Rehellinen lopetus: *"kunnes sähköposti on tyhjä"*, *"kunnes ajastin osuu 30 sekuntiin"*.

Ei lopetus: *"kunnes tuntuu valmiilta"*, *"kunnes ymmärrät"*.

Karanneella toistolla ei ole rehellistä lopetusta. Korjaus on turvalopetus selkokielellä.

---

## Kolme liikettä yhdessä prosessissa

Useimmat todelliset prosessit ovat kudelmaa:

- pieni **sekvenssi** sisällä
- **ehto**, joka valitsee mitä tehdä
- **toisto**, joka tekee sen joka kohteelle

Kolmen nimeäminen on se, mikä tekee kuvauksesta luettavan.

---

## Must-do minimum vs. syventävä

**Must-do minimum**
- Nimeä kolme rakennuspalikkaa arkisessa prosessissa.
- Yhdistä kaikki kolme yhdeksi lyhyeksi prosessikuvaukseksi.

**Syventävä**
- Yhdistetyt ehdot (AND, OR).
- Turvalopetukset karanneille toistoille.
- Ammatilliset ympäristöt: salasanasääntö, tikettien reititys, sähköpostien läpikäynti.
- LLM-sparrailu strukturoidulla kehotteella.

---

## Tämän viikon tehtävät

- Tehtävä 5.1 — Kolme liikettä yhdessä prosessissa (PAKOLLINEN, AT2-syöttö)
- Tehtävä 5.3 — Päätöspuu todellisesta säännöstä (SYVENTÄVÄ)
- Tehtävä 5.4 — Lopetusehto on turvavyö (SYVENTÄVÄ)
- Tehtävä 5.5 — Ammatillinen näkökulma, valinnainen LLM-sparrailu (SYVENTÄVÄ)

Säilytä muistiinpanot — AT2 palautetaan viikon 5 lopussa / viikon 6 aikana.

---

## Mitä seuraavaksi: viikko 6 — pseudokoodi

Tällä viikolla kirjoittamiisi luonnollisen kielen kuvauksiin lisätään muutama pieni konventio: yksinkertaisia muuttujia, kevyt sisennys, käsiajotaulukko.

Ajattelu pysyy samana. Muoto vain tiivistyy.

---

## Yhteenveto — keskeinen viesti vielä kerran

**Lähes mikä tahansa prosessi voidaan kuvata kolmella rakennuspalikalla: sekvenssi, ehto ja toisto.**

Kun osaat nimetä nämä arkisissa tehtävissä, sinulla on jokaisen ohjelman luuranko.
