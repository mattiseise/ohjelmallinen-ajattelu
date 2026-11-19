# Viikko 6 — Oppitunti 16 lisämateriaali

---

## Malliesimerkki - teen tekeminen

Kulku englannista pseudokoodiin alusta loppuun.
Sama malli, jota viikko 1 käytti pikanuudeleihin, mutta nyt pseudokoodina.

---

## Englanniksi

Täytät vedenkeittimen ja kytket sen päälle. Odotat, kunnes se naksahtaa pois. Laitat teepussin
mukiin ja kaadat kuuman veden. Jätät pussin hautumaan kolmeksi minuutiksi. Jos käytät
sokeria, lisäät yhden lusikallisen ja sekoitat.
Viisi virkettä. Tarpeeksi selkeää ihmisystävälle. Tietokone kuitenkin kompastuisi vielä kohtiin
"odota, kunnes se naksahtaa" (kuinka kauan?) ja "jos käytät sokeria" (mistä se tietää?).

### Vinkki: pseudokoodi tekee piilossa olevat kysymykset näkyviksi. ---

## Pseudokoodina - runko

```pseudocode
READ takesSugar
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
wait
ENDWHILE
SET bagInMug TO YES
WRITE "kaada kuuma vesi"
WRITE "odota kolme minuuttia"
IF takesSugar = YES THEN
WRITE "lisää yksi lusikallinen sokeria"
WRITE "sekoita"
ENDIF
WRITE "tee on valmis"
```

Kaksitoista riviä. Viikon 5 `IF` ja `WHILE` näkyvät yhdellä silmäyksellä.

### Vinkki: sisennys näyttää, mitkä rivit kuuluvat IF- tai WHILE-lohkoon. ---

## Osien nimeäminen

```pseudocode
READ takesSugar <-- SYÖTE
SET kettleOn TO YES <-- KÄSITTELY alkaa
WHILE kettleHasNotClicked DO
wait
ENDWHILE
SET bagInMug TO YES
WRITE "kaada kuuma vesi" <-- TULOSTE
WRITE "odota kolme minuuttia" <-- TULOSTE
IF takesSugar = YES THEN
WRITE "lisää yksi lusikallinen sokeria" <-- TULOSTE
WRITE "sekoita" <-- TULOSTE
ENDIF
WRITE "tee on valmis" <-- TULOSTE
```

Yksi syöte. Yksi käsittelylohko keskellä. Useita tulosteita lopussa. Tämä on jo oppitunnin 17
runko. ---

## Mikä tarkentui?

• Englanti jätti nämä epämääräisiksi - pseudokoodi kiinnitti ne:
• *"vedenkeitin"* → nimetty tila `kettleHasNotClicked`, jonka voimme oikeasti tarkistaa.
• *"jos käytät sokeria"* → nimetty muuttuja `takesSugar`, jolla on selkeä `YES` / `NO` -arvo.
• *"kolme minuuttia"* → erillinen `WRITE`-rivi, ei sivuhuomautus.
• Pseudokoodi on pidempi kuin englanti. Se on kompromissi: enemmän rivejä, vähemmän
arvaamista.

### Ajattele näin: pituus kasvaa, mutta epäselvyys vähenee. ---

## Malli skaalautuu

• Sama muoto toimii hyvin erilaisissa tehtävissä:
• Help desk -tikettien lajittelu - `READ ticketText`, `IF` se sisältää sanan "password" THEN ohjaa
tasolle 1, `ELSE IF` "outage" THEN tasolle 2, `ELSE` tasolle 3.
• Salasanan vahvuustarkistus - `READ password`, laske pituus, `IF` pituus on vähintään 8 AND
siinä on numero THEN vahva, `ELSE` heikko.
• Päivittäinen varmuuskopio - `FOR each folder IN backupList DO` kopioi se, `ENDFOR`. Tulosta
lista kopioiduista kansioista.
• Sama runko: syöte ylhäällä, käsittely keskellä, tuloste lopussa.

### Vinkki: kun runko on sama, opittu siirtyy uuteen tilanteeseen.
