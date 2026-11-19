# Työstetty esimerkki — teen keittäminen

Kävely englannista pseudokoodiin, päästä päähän.

Sama pohja, jota viikko 1 käytti pikanuudeleille, nyt pseudokoodissa.

---

## Englanniksi

You fill the kettle and switch it on. You wait until it clicks. You put a tea bag in your mug and pour the hot water. You leave the bag in for three minutes. If you take sugar, you add one spoon and stir.

Viisi lausetta. Tarpeeksi selvää ihmiskaverille. Tietokone kompastuisi edelleen kohtiin *"wait until it clicks"* (kuinka kauan?) ja *"if you take sugar"* (mistä se tietää?).

---

## Pseudokoodina — runko

```text
READ takesSugar
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour hot water"
WRITE "wait three minutes"
IF takesSugar = YES THEN
  WRITE "add one spoon of sugar"
  WRITE "stir"
ENDIF
WRITE "tea is ready"
```

Kaksitoista riviä. Viikon 5 `IF` ja `WHILE` näkyvät yhdellä silmäyksellä.

---

## Osien nimeäminen

```text
READ takesSugar             <-- SYÖTE
SET kettleOn TO YES         <-- KÄSITTELY alkaa
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour hot water"      <-- TULOSTE
WRITE "wait three minutes"  <-- TULOSTE
IF takesSugar = YES THEN
  WRITE "add one spoon of sugar"  <-- TULOSTE
  WRITE "stir"                    <-- TULOSTE
ENDIF
WRITE "tea is ready"        <-- TULOSTE
```

Yksi syöte. Yksi käsittelylohko keskellä. Useita tulosteita lopussa. Tämä on jo O17:n runko.

---

## Mikä täsmentyi

Englanti jätti nämä epämääräisiksi — pseudokoodi täsmensi:

- *"the kettle"* → nimetty tila `kettleHasNotClicked`, jonka voimme oikeasti tarkistaa.
- *"if you take sugar"* → nimetty muuttuja `takesSugar`, jolla selvä `YES` / `NO` -arvo.
- *"three minutes"* → eksplisiittinen `WRITE`-rivi, ei sivuhuomautus.

Pseudokoodi on pidempää kuin englanti. Se on kauppa: enemmän rivejä, vähemmän arvailua.

---

## Pohja skaalautuu

Sama muoto toimii hyvin erilaisille tehtäville:

- **Help-deskin tikettien priorisointi** — `READ ticketText`, `IF` se sisältää sanan "password" THEN ohjaa tasolle 1, `ELSE IF` "outage" THEN tasolle 2, `ELSE` tasolle 3.
- **Salasanan vahvuuden tarkistus** — `READ password`, laske pituus, `IF` pituus on vähintään 8 JA siinä on numero THEN vahva, `ELSE` heikko.
- **Päivittäinen varmuuskopiointirutiini** — `FOR each folder IN backupList DO` kopioi se, `ENDFOR`. Tulosta lista siitä, mitä kopioitiin.

Sama runko: syöte ylhäällä, käsittely keskellä, tuloste lopussa.
