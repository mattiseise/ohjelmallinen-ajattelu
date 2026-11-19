# Viikko 6 — Oppitunti 16 lisämateriaali — Puhujamuistiinpanot

## Dia 1 — Viikko 6: Oppitunti 16 lisämateriaali

Avaa lyhyellä saatteella: "Tämä on lisämateriaali oppitunnille 16. Käymme yhden pseudokoodi-esimerkin läpi alusta loppuun, sama, johon paadiat viittasivat." Tarkoitus on hidas, yksityiskohtainen läpikäynti. Tämä on materiaali, jonka opiskelija voi katsoa myös itsenäisesti, jos pääkalvot tuntuivat vauhdikkailta. Sano, että viikolla 1 sama prosessi (teen tekeminen) käytiin läpi luonnollisella kielellä ja viikolla 3 vuokaaviona. Nyt sama prosessi saa pseudokoodimuodon. Toisto on tarkoituksellinen — kun esimerkki on tuttu, voitte keskittyä uuteen muotoon. Noin 30 sek.

## Dia 2 — Malliesimerkki — teen tekeminen

Esittele dian rakenne: kulku englannista pseudokoodiin alusta loppuun. Sano: "Käytämme samaa esimerkkiä kuin viikolla 1, koska sisältö on tuttu. Uutta on muoto." Tämä on pedagoginen valinta — kun aihe on tuttu, kognitiivinen kuorma vähenee ja oppija voi keskittyä uuteen muotoon. Kysy: "Muistatteko viikon 1 pikanuudeliesimerkin?" Useimmat muistavat. Tämä on sama idea: tutusta tehtävästä rakennetaan tarkempi kuvaus. Noin 1 min.

## Dia 3 — Englanniksi

Lue englanninkielinen kuvaus ääneen rauhallisesti. Viisi virkettä, selkeää arkikieltä. Painota, että ihmiselle tämä on hyvin riittävää. Mutta tietokoneelle kaksi kohtaa kompastuu: "odota, kunnes se naksahtaa" (kuinka kauan, miten tarkistetaan?) ja "jos käytät sokeria" (mistä tietokone tietää?). Tämä on tärkeä huomio — luonnollinen kieli kätkee oletuksia, joita ihminen täydentää automaattisesti. Sano: "Tietokone ei täydennä. Se kysyy aina: mistä tämän tiedon saa?" Vinkki: pseudokoodi tekee piilossa olevat kysymykset näkyviksi. Noin 1,5 min.

## Dia 4 — Pseudokoodina — runko

Käy pseudokoodi rivi riviltä. READ takesSugar — kysytään ulkopuolelta, käyttääkö sokeria. SET kettleOn TO YES — asetetaan muuttuja. WHILE kettleHasNotClicked DO ... ENDWHILE — toistetaan odotusta. SET bagInMug TO YES — asetetaan toinen muuttuja. WRITE-rivit antavat tulosteita. IF takesSugar = YES THEN ... ENDIF — sokerilisäys ehdollisena. Painota sisennyksen merkitystä: rivit IF:n ja ENDIF:n välissä kuuluvat IF-lohkoon. Lue rivit ääneen siten, että ehto ja toisto erottuvat. Kaksitoista riviä yhteensä. Sano: "Tämä on enemmän tekstiä kuin englanniksi, mutta se on yksiselitteistä." Noin 2,5 min.

## Dia 5 — Osien nimeäminen

Käy sama pseudokoodi uudelleen, mutta nyt nuolet osoittavat roolit: SYÖTE, KÄSITTELY, TULOSTE. READ takesSugar on syöte (yksi). SET-rivit ja WHILE ovat käsittelyä. WRITE-rivit ovat tulosteita (useita). Painota: tämä on sama syöte–käsittely–tuloste -runko, joka esiintyy melkein kaikessa koodissa. Sano: "Tämä runko on niin yleinen, että voitte etsiä sitä jokaisesta ohjelmasta, jonka koskaan luette." Kysy: "Kuinka monta syötettä? Kuinka monta tulostetta?" Vastaus: yksi syöte, viisi tulostetta. Tämä on tyypillinen suhde: vähän syötteitä, paljon tulostetta. Noin 2 min.

## Dia 6 — Mikä tarkentui?

Tämä on dian ydin — vertailu englannin ja pseudokoodin välillä. Käy bullettilista läpi. "Vedenkeitin" → kettleHasNotClicked — nyt tila on nimetty ja tarkistettavissa. "Jos käytät sokeria" → takesSugar muuttuja YES/NO. "Kolme minuuttia" → erillinen WRITE-rivi, ei sivuhuomautus. Sano: "Pseudokoodi on pidempi, mutta jokainen oletus on näkyvissä. Tämä on kompromissi — enemmän rivejä, vähemmän arvaamista." Tämä on hyvä periaate kaikessa koodaamisessa. Kysy: "Onko tämä mielestänne hyvä vaihto?" Useimmat sanovat kyllä, kun esimerkki on konkreettinen. Noin 2 min.

## Dia 7 — Malli skaalautuu

Lopeta osoittamalla, että sama runko toimii hyvin erilaisissa tehtävissä. Help desk -tikettien lajittelu: READ ticketText, IF "password" → taso 1, ELSE IF "outage" → taso 2, ELSE → taso 3. Salasanan vahvuus: READ password, laske pituus, IF pituus >= 8 AND on numero → vahva. Päivittäinen varmuuskopio: FOR each folder IN backupList DO kopioi, ENDFOR. Sano: "Sama runko, eri sisältö. Jos opitte tämän muodon, voitte kirjoittaa pseudokoodia melkein mistä tahansa työtehtävästä." Tämä on viikon ydinlupaus. Vinkki: kun runko on sama, opittu siirtyy uuteen tilanteeseen. Kannustaa opiskelijaa kokeilemaan AT2:ssa työelämälähtöistä tehtävää. Noin 2,5 min.
