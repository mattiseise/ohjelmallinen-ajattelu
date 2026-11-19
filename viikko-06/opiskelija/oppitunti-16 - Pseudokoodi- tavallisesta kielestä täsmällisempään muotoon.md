# Oppitunti 16 — Pseudokoodi: tavallisesta kielestä täsmällisempään muotoon

### Tavallisesta kielestä pseudokoodiin

Tässä on tuttu prosessi tavallisella kielellä. Teet kupin teetä, ja tänään saatat ottaa sokeria tai
olla ottamatta.
Täytät vedenkeittimen ja laitat sen päälle. Odotat, että se naksahtaa. Laitat teepussin
mukiin ja kaadat kuuman veden. Annetaan hautua kolme minuuttia. Jos käytät
sokeria, lisäät yhden lusikallisen ja sekoitat. Sitten tee on valmis.
Lue tämä kerran ääneen. Ihmisystäväsi ymmärtää sen. Tietokone ei ymmärrä — “odota, että se
naksahtaa” (kuinka kauan? miten tietokone huomaa naksahduksen?) ja “jos käytät sokeria”
(mistä se tietää?) ovat molemmat kohteliaita aukkoja, jotka toimivat vain siksi, että lukija on
ihminen.
Sama prosessi pseudokoodina:

```pseudocode
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

Kun laitat nämä vierekkäin, mikä muuttuu? Tavallinen kieli on lyhyempää ja ystävällisempää.
Pseudokoodi on pidempää, mutta jokainen rivi kertoo yhden asian, jonka suorittajan pitää
tehdä, ja jokainen tavallisen kielen kohtelias aukko (naksahdus, sokeri) on nyt nimetty
kysymys ( , ), johon on selkeä vastaus. `kettleHasNotClicked takesSugar`
Pseudokoodi erottaa myös toisistaan sen, mitä käyttäjältä kysytään ( ) ja sen, mitä `READ`
käyttäjälle näytetään ( ). Tavallinen kieli sulautti nämä yhteen. Huomaa myös, että `WRITE`
viikon 5 tutut rakenteet ja ovat yhä mukana: niille on vain annettu yhteinen muoto `IF WHILE`
ja lopetusavainsanat ( , ), jotta lukija näkee yhdellä vilkaisulla, mistä lohko `ENDIF ENDWHILE`
alkaa ja mihin se päättyy.
Pseudokoodi ei ole uusi kieli, joka pitäisi opetella ulkoa. Se on samaa asiaa, jota kirjoitit jo
viikolla 5, mutta muutamalla yhteisesti sovitulla sanalla ja vakiomuodolla, jotta vieras lukija
lukee sen samalla tavalla kuin sinä.

### Pieni joukko avainsanoja

Tällä kurssilla käytetään pientä, kiinteää pseudokoodin avainsanajoukkoa. Kaikki nämä
ajatukset tulivat jo vastaan tavallisella kielellä viikolla 5. Avainsanat kirjoitetaan aina
SUURAAKKOSIN, jotta ne erottuvat nopeasti. Kaikki muu — muuttujien nimet, arvot ja viestit
— on omaa kieltäsi. `SET passwordLength TO 7`
Sijoitus. Laita arvo nimettyyn säiliöön . Tämän rivin jälkeen `7 passwordLength`
on .

```
passwordLength 7
READ password
```

Syöte. Ota käyttäjän kirjoittama arvo ja laita se nimettyyn säiliöön .

```
password
WRITE "your password is strong"
```

Tuotos. Näytä tämä viesti käyttäjälle.

```pseudocode
IF length >= 8 THEN
WRITE "long enough"
ELSE
WRITE "too short"
ENDIF
```

Ehto. Jos testi on tosi, suorita ensimmäinen lohko. Muuten suorita toinen lohko. kertoo, `ENDIF`
mihin ehtorakenne päättyy.

```pseudocode
WHILE inboxIsNotEmpty DO
WRITE "process one message"
ENDWHILE
```

Toisto, jossa testi tarkistetaan ennen jokaista kierrosta. Heti kun testi ei enää ole tosi,
toisto loppuu.

```pseudocode
FOR each folder IN backupList DO
WRITE "back up the folder"
ENDFOR
```

Toisto valmiiksi tunnetun listan yli. Suorittaja tekee sisällä olevan vaiheen kerran jokaista
listan kohtaa varten.
Näitä muotoja on kuusi. Käsittele tätä kohtaa ikään kuin muistikorttina — palaat siihen
oppitunneilla 17 ja 18.

### Järjestys, ehto, toisto — vanhat tutut uudessa muodossa

Katso yllä olevaa teepseudokoodia uudestaan. Rivirakenne, joka etenee vain ylhäältä alas ( `SET`
, sitten , sitten -rivit), on järjestystä. Lohko,

```pseudocode
kettleOn TO YES SET bagInMug TO YES WRITE
```

joka alkaa , on ehto. Lohko, joka alkaa

```
IF takesSugar = YES THEN WHILE
```

, on toisto. Täsmälleen samat kolme rakennuspalikkaa kuin viikolla `kettleHasNotClicked DO`
5.
Pseudokoodi ei tuo mukaan neljättä suurta liikettä. Se vain antaa näille kolmelle yhteisen
kirjallisen muodon.

### Miksi pseudokoodi on luotettavampi jakaa kuin tavallinen proosateksti?

Jos sinä ja parisi kirjoittaisitte saman teekuvauksen tavallisella kielellä, kaksi ystävällistä
lukijaa voisi päätyä hieman eri käsitykseen siitä, mitä sokerivaiheessa tarkalleen tapahtuu.
Pseudokoodi sulkee näitä aukkoja. “Jos käytät sokeria” muuttuu muotoon “onko muuttujan
arvo juuri nyt ?” Tämän voi lukea vain yhdellä tavalla. `takesSugar YES`
Pseudokoodin tarkoitus ei ole tehdä kirjoittamisesta helpompaa — usein se tekee siitä
vaikeampaa. Sen tarkoitus on tehdä väärinlukemisesta vaikeampaa. Kun annat sen vieraalle
lukijalle, vieras saa näkyviin juuri sen prosessin, jonka tarkoitit.
Pysähdy hetkeksi: Valitse yksi lyhyt prosessi, jonka teet joka aamu (puhelimen
lataaminen, hampaiden pesu, bussisovelluksen tarkistaminen). Missä kohdassa
tavallinen kielesi olisi liian kohteliasta — missä se jättäisi aukon, johon
kirjaimellinen suorittaja kompastuisi? Nimeä yksi tällainen aukko kirjallisesti ennen
kuin jatkat.
Pysähdy hetkeksi: Yllä oleva teepseudokoodi on 12 riviä pitkä. Jos poistaisit siitä
- ja -rivit, olisiko merkitys yhä selvä? Miksi luulet, että kurssi `ENDIF ENDWHILE`
käyttää niitä silti?
