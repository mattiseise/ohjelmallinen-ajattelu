# Viikko 6 — Ajattelusta koodiin

Ohjelmallinen ajattelu

Ammatillinen ICT-kurssi, 1. vuosi

---

## Keskeinen kysymys

How do I speak to a computer so that it understands what I want it to do?

Tällä viikolla vastaamme siihen yhdellä uudella sanalla: **pseudokoodi**.

---

## Tällä viikolla — pseudokoodi, muuttujat, käsiajo

- Oppitunti 16 — **pseudokoodi**: tiiviimpi tapa kirjoittaa sitä, mitä jo kirjoitat.
- Oppitunti 17 — **muuttujat** ja syöte → käsittely → tuloste -runko.
- Oppitunti 18 — **käsiajo** paperilla jäljityskaavion avulla.

**AT2 palautetaan oppitunnin 18 tienoilla.** Alla oleva työ on sen raaka-aine.

---

## Mikä pseudokoodi on?

**Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer.**

Edelleen paperilla. Edelleen englanniksi. Vain muutamilla jaetuilla sanoilla ja kiinteällä muodolla.

---

## Pieni avainsanojen joukko

- `SET name TO value` — sijoitus
- `READ name` — syöte
- `WRITE expression` — tuloste
- `IF test THEN … ELSE … ENDIF` — ehto
- `WHILE test DO … ENDWHILE` — toisto, jossa testi ensin
- `FOR each item IN list DO … ENDFOR` — toisto tunnetun listan yli

Nämä ovat kaikki avainsanat, joita tarvitset tällä viikolla.

---

## Englanti vs. pseudokoodi — teen keittäminen

**Englanti:** Fill the kettle. Switch it on. Wait until it clicks. Put the bag in the mug. Pour the water. If you take sugar, add one spoon.

**Pseudokoodi:**

```text
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour water"
IF takesSugar THEN
  WRITE "add one spoon"
ENDIF
```

---

## Sekvenssi, ehto, toisto — tervehdys uudestaan

Pseudokoodi on vain viikon 5 kolme rakennuspalikkaa jaetuilla sanoilla:

- *sekvenssi* — rivit ylhäältä alas.
- *ehto* — `IF … THEN … ELSE … ENDIF`.
- *toisto* — `WHILE … ENDWHILE` tai `FOR … ENDFOR`.

Ajattelu on sama. Muoto vain tiukentuu.

---

## Syöte → käsittely → tuloste

Useimmat pseudokoodit noudattavat samaa runkoa:

- **Syöte** — `READ` jotain ulkopuolelta.
- **Käsittely** — päätä, laske, toista.
- **Tuloste** — `WRITE` vastaus takaisin.

Esimerkki: pyydä luku, tuplaa se, kirjoita tulos.

---

## Mikä muuttuja on?

**Muuttuja** on nimetty säilö yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen aikana.

Kuvittele post-it-lappu purkin päällä. Etiketti pysyy samana. Lapulla oleva numero voi muuttua.

```text
SET passwordLength TO 7
SET passwordLength TO 8
```

Nyt purkki pitää sisällään 8.

---

## Hyvä muuttujan nimi

Huono: `SET x TO 7`

Hyvä: `SET passwordLength TO 7`

Molemmat tekevät saman asian tietokoneelle. Toinen kertoo seuraavalle lukijalle (tai tulevalle sinulle), mitä 7 tarkoittaa.

---

## Ammatillinen esimerkki — salasanan vahvuus

```text
READ password
SET length TO numberOfCharactersIn(password)
SET hasDigit TO doesPasswordContainADigit(password)
IF length >= 8 AND hasDigit = YES THEN
  SET isStrong TO YES
ELSE
  SET isStrong TO NO
ENDIF
WRITE isStrong
```

Syöte → käsittely → tuloste. Yksi muuttuja per idea.

---

## Mikä käsiajo on?

**Käsiajo** on pseudokoodin läpikäymistä käsin, rivi riviltä, esittäen tietokonetta.

Se on viikon 1 "sananmukainen robotti" — mutta nyt robotti olet sinä, paperilla, lukemassa omaa tekstiäsi.

---

## Jäljityskaavio

Pieni taulukko pseudokoodisi vieressä. Yksi sarake per muuttuja, plus tulostesarake. Yksi rivi per suoritettu rivi.

| Rivi | counter | total | Tuloste |
|------|---------|-------|---------|
| 1    | 1       | 0     |         |
| 2    | 1       | 1     |         |
| 3    | 2       | 1     |         |
| 4    | 2       | 3     |         |
| 5    | 3       | 3     | 3       |

Taulukko pakottaa kirjoittamaan jokaisen askeleen alas.

---

## Bugin löytäminen — todellinen vs. odotettu tuloste

Odotettu tuloste syötteelle `5`: kirjoita `15`.

Jäljitys sanoo, että todellinen tuloste on `10`.

Katso riviä, jossa arvot poikkeavat. Bugi asuu siellä.

Korjaa se yksi rivi. Jäljitä uudelleen. Odotettu ja todellinen täsmäävät nyt.

---

## AT2 — palautetaan oppitunnin 18 tienoilla

- **Mitä se pyytää:** lyhyt pseudokoodi pienestä valitsemastasi tehtävästä, plus jäljityskaavio.
- **Mitä tuoda:** pseudokoodi, jäljityskaavio (normaali syöte + yksi hankala syöte), 5 lauseen reflektio.
- **Mitä EI tuoda:** mitään oikeaa ohjelmointikieltä. Vain pseudokoodia.

---

## Viikon 6 sanasto yhdellä silmäyksellä

- pseudokoodi, avainsana, muuttuja, arvo, sijoitus
- syöte, käsittely, tuloste
- ehto, toisto, lohko
- käsiajo, jäljityskaavio, bugi, odotettu tuloste, todellinen tuloste

Katse eteenpäin: *console* (viikko 7).

---

## Must-do-minimi vs. syventävä

**Must-do-minimi**

- Kirjoita 10–20 riviä pseudokoodia tutusta prosessista, jossa yksi ehto ja yksi toisto.
- Käsiaja se jäljityskaaviolla yhdelle normaalille ja yhdelle hankalalle syötteelle.

**Syventävä**

- Löydä ja nimeä bugin tyyppi rikotusta katkelmasta.
- Jäljitä luokkakaverin pseudokoodi ja vertaa.
- Käytä LLM:ää harjoituskumppanina omaa jäljitystäsi vastaan.

---

## Tämän viikon tehtävät

- Tehtävä 6.1 — Pseudokoodaa tuttu prosessi (PAKOLLINEN, AT2:n selkäranka)
- Tehtävä 6.3 — Etsi bugi (SYVENTÄVÄ)
- Tehtävä 6.4 — Jäljitä luokkakaverin pseudokoodi (SYVENTÄVÄ)
- Tehtävä 6.5 — LLM-sparraus omaa käsiajoasi vastaan (SYVENTÄVÄ)

Säilytä pseudokoodisi ja jäljityskaaviosi — **AT2 palautetaan tämän viikon oppitunnin 18 tienoilla.**

---

## Mitä tulee seuraavaksi — viikko 7: ensimmäinen oikea koodi

Ensi viikolla sama pseudokoodimuoto muuttuu pieneksi ohjelmaksi oikealla kielellä, jonka ajat selaimessa.

Tämän viikon avainsanoilla on suorat parit siellä. Ajattelu ei muutu.

---

## Kertaus — keskeinen kysymys vielä kerran

How do I speak to a computer so that it understands what I want it to do?

**Pseudokoodi on silta arkikielen ja oikean koodin välillä.** Tällä viikolla rakensit sillan. Ensi viikolla kävelet sen yli.
