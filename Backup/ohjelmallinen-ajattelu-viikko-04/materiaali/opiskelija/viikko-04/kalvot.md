# Viikko 4 — Ratkaisujen vertailu

Ohjelmallinen ajattelu

Ammatillinen ICT-kurssi 1. vuosi

---

## Viikon ydinviesti

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Tämä on koko viikon muistettava lause.

---

## Missä viikko 4 sijaitsee

- Viikot 1–3 — algoritmit (V1), ositus + AT1 (V2), vuokaaviot ja abstraktio (V3)
- **Viikko 4 — kurssin puolivälin reflektio: vertaile ja korjaa, mitä olet jo rakentanut**
- Viikot 5–8 — logiikkarakenteet (V5), pseudokoodi + AT2 (V6), JavaScript (V7), silmukat + AT3 (V8)

Tällä viikolla ei tule uutta ohjelmallisen ajattelun primitiiviä. Raaka-aineena on oma viikon 2 ja viikon 3 työsi.

---

## Ongelma ei ole sama asia kuin sen ratkaisu

**Ongelma** on tavoite: *"tee juotava kuppi teetä"*, *"pidä palautettavissa oleva varmuuskopio projektikansiosta"*.

**Ratkaisu** on yksi tapa saavuttaa tuo tavoite — vaiheet, jotka kirjoitat ylös.

Yksi ongelma. Monta mahdollista ratkaisua, kaikki päteviä.

---

## Kaksi tapaa tehdä teetä

| Vaihe | Resepti A (keitä ensin) | Resepti B (hauduta ensin) |
|------|------------------------|--------------------------|
| 1 | Täytä vedenkeitin 250 ml:lla vettä | Laita yksi teepussi kuppiin |
| 2 | Keitä vesi | Täytä vedenkeitin 250 ml:lla vettä |
| 3 | Laita yksi teepussi kuppiin | Keitä vesi |
| 4 | Kaada keitetty vesi pussin päälle | Kaada keitetty vesi pussin päälle |
| 5 | Odota 3 minuuttia, poista pussi | Odota, kunnes väri näyttää oikealta, poista pussi |

Molemmat tuottavat juotavan kupin teetä. Ne eroavat *järjestyksessä* ja siinä, mitä jätetään käyttäjälle.

---

## Kaksi tapaa varmuuskopioida projektikansio

| Vaihe | Tapa A (USB-kopio) | Tapa B (zip + sähköposti) |
|------|----------------------|--------------------------|
| 1 | Kytke USB-tikku läppäriin | Klikkaa projektikansiota hiiren oikealla |
| 2 | Avaa projektikansio | Valitse *"Pakkaa .zip-tiedostoon"* |
| 3 | Valitse kaikki tiedostot, paina Ctrl+C | Odota, että zip-tiedosto ilmestyy |
| 4 | Avaa USB-tikku | Avaa koulun sähköposti |
| 5 | Paina Ctrl+V, odota kopioinnin valmistumista | Liitä zip ja lähetä itsellesi |
| 6 | Irrota USB-tikku turvallisesti | Tallenna sähköposti *Varmuuskopiot*-kansioon |

Molemmat tuottavat palautettavissa olevan varmuuskopion. Ne eroavat siinä, *missä kopio sijaitsee* ja *mikä voi mennä pieleen*.

---

## Mikä on sama, mikä eri?

- **Sama** — molemmat saavuttavat tavoitteen, molemmat ovat päteviä.
- **Eri** — *vaiheiden järjestys* muuttuu (keitä ensin vs. hauduta ensin).
- **Eri** — mitä *jää käyttäjälle* (laske kolme minuuttia vs. arvioi väri).
- **Eri** — mikä voi *mennä pieleen* (pussin unohtaminen vs. tikun irrottamatta jättäminen).

Tuo viimeinen lista on kriteerien alku.

---

## Mausta kriteeriin

*"Pidän vain Reseptistä A enemmän."* — makua.

*"Resepti A on selkeämpi vaiheessa 5, koska *3 minuuttia* kertoo tekijälle täsmälleen, milloin pysähtyä."* — kriteerillä nimetty.

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Kriteeri on nimetty mittapuu — nimeä se, ja *parempi* lakkaa olemasta tunne ja alkaa olla vertailu.

---

## Neljä kriteeriä

Tässä lukitussa järjestyksessä ensimmäisellä mainintakerralla: **selkeys · tehokkuus · toistettavuus · virhealttius**.

- **Selkeys** — sananmukainen tulkitsija voi lukea sen kerran ja tietää, mitä tehdä.
- **Tehokkuus** — saavuttaa tavoitteen ilman hukattuja vaiheita.
- **Toistettavuus** — sama syöte, sama tulos joka kerta.
- **Virhealttius** — vaikea tehdä väärää asiaa sen mukaan toimiessa.

Neljä kriteeriä. Samat neljä nimeä kaikkialla.

---

## Selkeys kahdessa teereseptissä

Resepti A — *"Odota 3 minuuttia, poista pussi."* Luku. Sananmukainen tulkitsija pysähtyy oikeaan aikaan.

Resepti B — *"Odota, kunnes väri näyttää oikealta, poista pussi."* Tekijän on tiedettävä, miltä *oikea väri* näyttää. Se on yksi lisäolettama, joka jätetään sanomatta.

Molemmat saavuttavat tavoitteen. Resepti A on **selkeämpi vaiheessa 5**, koska se nimeää konkreettisen ajan.

---

## Tehokkuus kahdessa varmuuskopiotavassa

Tapa A (USB-kopio) kopioi jokaisen tiedoston yksi kerrallaan. Jos kansiossa on 500 pientä tiedostoa, kopiointi kestää kauemmin kuin pelkän datan perusteella voisi olettaa.

Tapa B (zip + sähköposti) pakkaa kansion ensin yhdeksi tiedostoksi ja siirtää yhden tiedoston kerran.

Molemmat saavuttavat tavoitteen. Tapa B on **tehokkaampi monien pienien tiedostojen kansiossa** — vähemmän hukattuja vaiheita siirrossa.

---

## Toistettavuus ja virhealttius — pikaesimerkkejä

**Toistettavuus.** Resepti A käyttää aina 200 ml:aa ja kolme minuuttia — sama juoma maanantaina ja perjantaina. *"Hieman vettä, maistele"* antaa eri juoman joka kerta.

**Virhealttius.** Tapa A kirjoittaa edellisen USB-varmuuskopion päälle, jos et nimeä kansiota uudelleen; yksi lipsahdus ja eilisen kopio on poissa. Tapa B säilyttää sähköpostipäivätyn kopion jokaisesta varmuuskopiosta — vaikeampi hukata vahingossa.

---

## Kompromissit — kun kriteerit vetävät eri suuntiin

Resepti A voittaa **selkeydessä** (kolme minuuttia on täsmällinen).

Resepti B voi voittaa **tehokkuudessa** (se keittää vain kerran ja käyttää väriä lopettamisvihjeenä, jonka kokenut teejuomari lukee yhdellä silmäyksellä).

"Paras" valinta riippuu tekijästä. **Kompromissin nimeäminen on analyysi.** Sinun ei tarvitse kruunata voittajaa.

---

## Vertaisarviointiprotokolla

Kolme vaihetta. Tässä lukitussa järjestyksessä.

1. **Kriteerit** — lue parin tuotos hiljaa. Kirjoita yksi lause kriteeriä kohden (selkeys, tehokkuus, toistettavuus, virhealttius).
2. **Palaute** — valitse **kaksi hyödyllisintä** lausetta. Kumpikin nimeää kriteerin ja tietyn vaiheen.
3. **Revisio** — tekijä muuttaa sitten yhden tai kaksi tiettyä asiaa alkuperäisessä toimiakseen palautteen mukaan ja kirjoittaa 3–5 lauseen muutosmuistion.

Ei arvosanoja. Ei numeroita. Ei "parasta".

---

## Palaute, jota joku voi käyttää

Kolme lyhyttä sääntöä.

- **Nimeä kriteeri.** *"Tämä on epäselvää"* → *"Tämä on epäselvää vaiheessa 3, koska sana *tiedosto* ei kerro, mistä tiedostosta on kyse."*
- **Yksi konkreettinen kohta.** *"Kokonaisuus on liian pitkä"* → *"Vaiheet 4 ja 5 toistavat vaihetta 2."*
- **Kritisoi tuotosta, älä ihmistä.**

Ehdotus on valinnainen mutta tervetullut — *"ehkä yhdistä vaiheet 4 ja 5"*.

---

## Viikon tehtävät

- **Tehtävä 4.1 — PAKOLLINEN (must-do minimum)** — Vertaisarviointi neljällä kriteerillä, omaan viikon 2 tai 3 tuotokseen.
- **Tehtävä 4.3 — SYVENTÄVÄ** — Varmuuskopiotavat, kriteeri kerrallaan (ammatillinen).
- **Tehtävä 4.4 — SYVENTÄVÄ** — Help desk -makro: pitkä vs. lyhyt (ammatillinen, valinnainen LLM-sparrausvaihe).
- **Tehtävä 4.5 — SYVENTÄVÄ** — Uuden käyttäjän perehdytys: tili-ensin vs. kierros-ensin (ammatillinen).

Pidä vertaispalautemuistiinpanosi ja revisiosi tallessa — ne syöttävät **AT2:ta viikon 5 lopussa / viikolla 6**.

---

## Mitä seuraavaksi: Viikko 5 — logiikkarakenteet

Viikko 5 muuttaa O7:n vinoneliön muodolliseksi **ehdoksi** *if / then / else*:llä ja esittelee **silmukat** — *tee, katso, muuta, tee uudelleen*.

Vertaisarviointi- ja revisiointitottumus, jota tällä viikolla harjoittelit, on **täsmälleen** se, mitä AT2 pyytää sinua tekemään — pidä muistiinpanosi tallessa.

---

## Kertaus — viikon ydinviesti vielä kerran

> **Samaan ongelmaan voi olla useampi kuin yksi pätevä ratkaisu. Niiden välillä valitseminen ei ole makuasia — vaan kysymys nimetyistä kriteereistä.**

Neljä kriteeriä: **selkeys · tehokkuus · toistettavuus · virhealttius**. Samat neljä nimeä. Sama lukittu järjestys. Kuvaile, älä arvostele.
