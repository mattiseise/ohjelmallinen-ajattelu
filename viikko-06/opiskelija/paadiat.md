# Viikko 6 — Ajattelusta koodiin

Ohjelmallinen ajattelu

Ammatillisen tieto- ja viestintätekniikan ensimmäisen vuoden kurssi

---

## Keskeinen kysymys

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

Tällä viikolla vastaamme siihen yhdellä uudella sanalla: **pseudokoodi**.

---

## Tällä viikolla — pseudokoodi, muuttujat, kuivaharjoittelu

- Oppitunti 16 — **pseudokoodi**: tiukempi tapa kirjoittaa sitä, mitä jo kirjoitat.
- Oppitunti 17 — **muuttujat** ja syöte → käsittely → tuloste -runko.
- Oppitunti 18 — käsin läpikäynti eli **kuivaharjoittelu** jäljitystaulukolla.

**AT2 palautetaan noin oppitunnilla 18.** Alla oleva työ on sen raaka-ainetta.

Vinkki: pseudokoodi ei ole oikea ohjelmointikieli, mutta se pakottaa ajattelemaan kuin ohjelmoija.

---

## Mitä pseudokoodi on?

Pseudokoodi on silta arki-englannin ja oikean koodin välillä: tarpeeksi täsmällistä, jotta
tietokone voisi seurata sitä, jos sen olisi pakko, mutta tarpeeksi luettavaa, jotta sen voi jakaa
myös ei-ohjelmoijalle.
Yhä paperilla. Yhä englanninkielisillä avainsanoilla. Vain muutama yhteinen sana ja kiinteä
muoto.

### Ajattele näin: pseudokoodi kertoo algoritmin ennen kuin päätät lopullisen ohjelmointikielen. ---

## Pieni joukko avainsanoja

• `SET name TO value` - arvon asettaminen muuttujaan
• `READ name` - syöte
• `WRITE expression` - tuloste
• `IF test THEN … ELSE … ENDIF` - ehto
• `WHILE test DO … ENDWHILE` - toisto, jossa testi tarkistetaan ensin
• `FOR each item IN list DO … ENDFOR` - toisto tunnetun listan yli
• Nämä ovat kaikki avainsanat, joita tarvitset tällä viikolla.

### Vinkki: avainsanat pidetään tässä englanniksi, jotta yhteys oikeaan koodiin näkyy. ---

## Englanti vs. pseudokoodi - teen tekeminen

Englanti: Täytä vedenkeitin. Kytke se päälle. Odota, kunnes se naksahtaa pois. Laita pussi
mukiin. Kaada vesi. Jos käytät sokeria, lisää yksi lusikallinen.
Pseudokoodi:

```pseudocode
READ takesSugar
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
wait
ENDWHILE
SET bagInMug TO YES
WRITE "kaada kuuma vesi"
IF takesSugar = YES THEN
WRITE "lisää yksi lusikallinen sokeria"
ENDIF
```

### Vinkki: pseudokoodi on pidempi, mutta arvaaminen vähenee. ---

## Järjestys, ehto, toisto - tavataan taas

• Pseudokoodi on vain viikon 5 kolme rakennuspalikkaa yhteisillä sanoilla:
• *järjestys* - rivit ylhäältä alas
• *ehto* - `IF … THEN … ELSE … ENDIF`
• *toisto* - `WHILE … ENDWHILE` tai `FOR … ENDFOR`
• Ajattelu on sama. Muoto vain tiukentuu.

### Ajattele näin: uusi ulkoasu, vanha logiikka. ---

## Syöte → käsittely → tuloste

• Useimmat pseudokoodit noudattavat samaa runkoa:
• Syöte - `READ` lukee jotakin ulkopuolelta.
• Käsittely - päättele, laske, toista.
• Tuloste - `WRITE` kirjoittaa vastauksen ulos.
• Esimerkki: kysy numero, kaksinkertaista se, kirjoita tulos.

### Vinkki: jos koodi tuntuu sekavalta, etsi ensin nämä kolme osaa. ---

## Mikä on muuttuja?

Muuttuja on nimetty säiliö yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen
aikana.
Kuvittele tarra purkin kyljessä. Tarran nimi pysyy samana. Tarrassa oleva numero voi
muuttua.

```pseudocode
SET passwordLength TO 7
SET passwordLength TO 8
```

### Esimerkki: muuttujan nimi voi olla `score`, mutta sen arvo voi vaihtua pelin aikana. ---

## Hyvä muuttujan nimi

Huono: `SET x TO 7`
Hyvä: `SET passwordLength TO 7`
Molemmat tekevät tietokoneelle saman asian. Toinen kertoo seuraavalle lukijalle - tai tulevalle
sinulle - mitä luku 7 tarkoittaa.

### Vinkki: jos muuttujan nimi vastaa kysymykseen "mikä tämä arvo on?", nimi on yleensä

parempi. ---

## Ammatillinen esimerkki - salasanan vahvuus

```pseudocode
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

### Ajattele näin: `length` ja `hasDigit` ovat väliarvoja. Ne auttavat ehtoa pysymään luettavana. ---

## Mitä kuivaharjoittelu tarkoittaa?

Kuivaharjoittelu tarkoittaa, että kävelet pseudokoodin läpi käsin, rivi riviltä, ja teeskentelet
olevasi tietokone.
Se on viikon 1 "kirjaimellinen robotti" - mutta nyt robotti olet sinä, paperilla, lukemassa omaa
tekstiäsi.

### Vinkki: älä oikaise. Kirjoita arvot ylös juuri siinä kohdassa, jossa ne muuttuvat. ---

## Jäljitystaulukko

Pieni taulukko pseudokoodin vieressä. Yksi sarake jokaiselle muuttujalle sekä tulostesarake.
Yksi rivi jokaiselle suoritetulle riville.

```
Rivi | counter | total | Tuloste
-----|---------|-------|--------
1 | 1 | 0 |
2 | 1 | 1 |
3 | 2 | 1 |
4 | 2 | 3 |
```

Vinkki: taulukko tekee näkymättömistä muuttujista näkyviä.

---

## Bugin löytäminen — toteutunut vs. odotettu tuloste

Odotettu tuloste syötteelle `5`: kirjoita `15`.

Jäljitys sanoo, että toteutunut tuloste on `10`.

Katso riviä, jossa arvot alkavat erota. Bugi asuu siellä.

Korjaa se yksi rivi. Jäljitä uudelleen. Odotettu ja toteutunut vastaavat nyt toisiaan.

Ajattele näin: et arvaa korjausta, vaan etsit ensimmäisen eron.

---

## AT2 - palautus noin oppitunnilla 18

• Mitä pyydetään: lyhyt pseudokoodin pätkä pienestä itse valitsemastasi tehtävästä sekä
jäljitystaulukko.
• Mitä tuot: pseudokoodi, jäljitystaulukko (normaali syöte + yksi hankala syöte) ja 5 virkkeen
reflektio.
• Mitä EI tuoda: mitään oikeaa ohjelmointikieltä. Vain pseudokoodia.

### Tee näin: valitse tehtävä, jossa on ainakin yksi ehto ja yksi toisto. ---

## Viikon 6 sanasto yhdellä silmäyksellä

• pseudokoodi, avainsana, muuttuja, arvo, arvon asettaminen
• syöte, käsittely, tuloste
• ehto, toisto, lohko
• kuivaharjoittelu, jäljitystaulukko, bugi, odotettu tuloste, toteutunut tuloste
• Ennakkoon: *konsoli* (viikko 7).

### Vinkki: "lohko" tarkoittaa yhteen kuuluvaa rivijoukkoa, esimerkiksi IF-rakenteen sisällä. ---

## Pakollinen vähimmäistaso vs. syventäminen

• Pakollinen vähimmäistaso
• Kirjoita 10-20 riviä pseudokoodia tutusta prosessista, jossa on yksi ehto ja yksi toisto.
• Kuivaharjoittele se jäljitystaulukolla yhdelle normaalille ja yhdelle hankalalle syötteelle.
• Syventäminen
• Etsi ja nimeä bugin tyyppi rikkinäisestä katkelmasta.
• Jäljitä luokkakaverin pseudokoodi ja verratkaa.
• Käytä LLM:ää sparrauskumppanina omaa jäljitystäsi vastaan. ---

## Tämän viikon tehtävät

• Tehtävä 6.1 - Kirjoita pseudokoodi tutulle prosessille (PAKOLLINEN, AT2:n selkäranka).
• Tehtävä 6.3 - Etsi bugi (SYVENTÄVÄ).
• Tehtävä 6.4 - Jäljitä luokkakaverin pseudokoodi (SYVENTÄVÄ).
• Tehtävä 6.5 - LLM-sparraus kuivaharjoitteluasi vastaan (SYVENTÄVÄ).
• Säilytä pseudokoodisi ja jäljitystaulukkosi - AT2 palautetaan noin oppitunnilla 18 tällä viikolla.

### Tee näin: ota mukaan myös hankala syöte, ei vain helppoa testitapausta. ---

## Seuraavaksi - Viikko 7: ensimmäinen oikea koodi

Ensi viikolla sama pseudokoodin muoto muuttuu pieneksi ohjelmaksi oikealla kielellä, jota
suoritat selaimessa.
Tällä viikolla opituilla avainsanoilla on siellä suorat vastineet. Ajattelu ei muutu.

Vinkki: älä pelkää syntaksia. Opit vain kirjoittamaan saman ajatuksen tarkemmalla kielellä.

---

## Kertaus — keskeinen kysymys, vielä kerran

Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?

**Pseudokoodi on silta arki-englannin ja oikean koodin välillä.** Tällä viikolla rakensit sillan. Ensi viikolla kävelet sen yli.
