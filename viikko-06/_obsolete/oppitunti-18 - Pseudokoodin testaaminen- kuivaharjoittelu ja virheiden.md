# Oppitunti 18 - Pseudokoodin testaaminen: kuivaharjoittelu ja virheiden

## löytäminen

### Mitä kuivaharjoittelu on?

Kuivaharjoittelu tarkoittaa sitä, että käyt läpi pseudokoodin käsin, rivi riviltä, paperilla ja
kuvittelet olevasi tietokone. Et saa hypätä eteenpäin tai arvata puuttuvia kohtia. Juuri tämä
kurinalaisuus paljastaa virheet.

### Seurantataulukko

Seurantataulukko on pieni ruudukko, jonka piirrät pseudokoodin viereen. Yksi sarake
jokaista muuttujaa varten, yksi tuotosta varten ja yksi rivi jokaista suoritettua riviä varten.
SET total TO 0
SET counter TO 1
WHILE counter <= 3 DO
SET total TO total + counter
SET counter TO counter + 1
ENDWHILE
WRITE total
Odotettu tuotos: .
6
Rivi counter total Tuotos
1 — 0
2 1 0
3 1 0 (testi: 1 <= 3,
kyllä)
4 1 1
5 2 1
3 2 1 (testi: 2 <= 3,
kyllä)
4 2 3
5 3 3
3 3 3 (testi: 3 <= 3,
kyllä)
4 3 6
Rivi counter total Tuotos
5 4 6
3 4 6 (testi: 4 <= 3, ei)
7 4 6 6
Todellinen tuotos on , joten pseudokoodi toimii tällä syötteellä.
6

### Virheen löytäminen

Kun muutat ehtorivin muotoon , kolmas kierros jää tekemättä ja
WHILE counter < 3 DO
todellinen tuotos muuttuu arvoksi . Tästä näet, että kyseessä on off-by-one-virhe — ehto on
3
yhden vertailun verran pielessä.

### Reunatapaukset paperilla

Paras jäljitettävä syöte ei aina ole helppo tapaus. Reunatapaukset, kuten tyhjä syöte, arvo ,
0
negatiivinen luku tai täsmälleen raja-arvon mittainen salasana, paljastavat virheitä hyvin
tehokkaasti.

### AT2:sta

AT2 pyytää juuri tätä: lyhyt pseudokoodi, kuivaharjoittelu yhdellä tavallisella ja yhdellä
hankalalla syötteellä sekä lyhyt pohdinta siitä, mitä jäljitys näytti.
Pysähdy hetkeksi: Mikä on ensimmäinen kohta, jossa odotettu ja todellinen tuotos
eroavat toisistaan? Aloita virheen etsintä siitä.

## Yhteenveto ja mitä seuraavaksi

Viikko 6 antoi viikkojen 1–5 ajattelulle yhteisen muodon: pseudokoodin. Tapasit avainsanat,
muuttujan, syöte → käsittely → tuotos -rungon sekä kuivaharjoittelun seurantataulukon avulla.
Ensi viikolla sama ajattelu siirtyy oikeaan ohjelmointikieleen. Ajattelu pysyy, kirjoitustapa
muuttuu.
