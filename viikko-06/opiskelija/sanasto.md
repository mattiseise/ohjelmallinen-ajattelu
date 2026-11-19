# Viikko 6 — Ajattelusta koodiin

## Viikon 6 sanasto

Alla olevat termit liittyvät oppitunteihin 16, 17 ja 18. Määritelmät ovat tarkoituksella lyhyitä —
katso esimerkit itseopiskelumateriaalista. Lopun termi (konsoli) on ennakkokatsaus viikkoon
7.

### Pseudokoodi

Tiukempi, sääntöihin sidotumpi tapa kirjoittaa prosessikuvauksia paperille. Se käyttää pientä
joukkoa yhteisiä avainsanoja ( , , ja niin edelleen), mutta se on edelleen `SET IF WHILE`
tarkoitettu ihmisten luettavaksi, ei tietokoneen suoritettavaksi. Pseudokoodi on silta tavallisen
kielen ja oikean koodin välillä: tarpeeksi täsmällinen, jotta tietokone voisi periaatteessa seurata
sitä, mutta tarpeeksi luettava, jotta myös ei-ohjelmoija voi ymmärtää sen.

### Avainsana

Yksi niistä pienistä, kiinteistä sanoista, joilla pseudokoodi merkitsee rakennetta: , , `SET READ`
, , , , , , , . Avainsanat näyttävät aina

```pseudocode
WRITE IF ELSE ENDIF WHILE ENDWHILE FOR ENDFOR
```

samoilta (tällä kurssilla SUURAAKKOSIN), jotta silmä löytää ne nopeasti. Kaikki mikä ei ole
avainsana on omaa kieltäsi: muuttujan nimi, arvo tai viesti.

### Muuttuja

Nimetty säiliö yhdelle arvolle, joka voi vaihtua pseudokoodin aikana. Ajattele purkkia, jonka
kyljessä on lappu ; purkin sisällä oleva luku voi vaihtua, mutta nimi pysyy. `passwordLength`
Tänä hetkenä muuttuja voi sisältää luvun, seuraavaksi kyllä/ei-arvon ja myöhemmin lyhyen
tekstin.

### Arvo

Se konkreettinen sisältö, joka muuttujassa on tietyllä hetkellä — luku ( ), kyllä/ei-arvo ( ) `7 YES`
tai lyhyt tekstinpätkä ( ). Muuttuja on nimetty laatikko; arvo on se, mitä laatikon `"hunter2"`
sisällä juuri nyt on.

### Sijoitus

Toiminto, jossa arvo laitetaan muuttujaan. Tällä kurssilla se kirjoitetaan aina muodossa `SET`
, esimerkiksi . Sijoituksen jälkeen

```pseudocode
variableName TO value SET passwordLength TO 7
```

muuttujassa on uusi arvo ja vanha unohtuu.

### Syöte

Se, mitä pseudokoodi saa ulkopuolelta — tavallisesti luku, merkkijono tai kyllä/ei-arvo, jonka
käyttäjä kirjoittaa. Pseudokoodissa tämä näkyy muodossa . Ennen kuin `READ variableName`
syöte saapuu, muuttujalla ei vielä ole hyödyllistä arvoa.

### Käsittely

Se, mitä pseudokoodi tekee keskellä, syötteen lukemisen ja tuotoksen kirjoittamisen välillä.
Käsittely on kohta, jossa säännöt elävät: ehto päättää haaran, toisto käy läpi listaa, sijoitus
yhdistää arvoja.

### Tuotos

Se, mitä pseudokoodi lähettää takaisin ulkomaailmaan — tavallisesti lyhyt viesti, luku tai
kyllä/ei-arvo. Pseudokoodissa tämä näkyy muodossa . Tuotos on se, minkä `WRITE expression`
käyttäjä oikeasti näkee.

### Ehto

Testi, joka päättää, mihin haaraan pseudokoodi seuraavaksi menee. (Viikolta 5 tuttu käsite.)
Pseudokoodissa ehto kirjoitetaan muodossa . ja `IF test THEN … ELSE … ENDIF IF ENDIF`
merkitsevät, mistä ehto alkaa ja mihin se loppuu, jotta lukija näkee haarat nopeasti.

### Toisto

Saman pseudokoodilohkon tekeminen useamman kuin kerran lopetusehdon kanssa. (Viikolta 5
tuttu käsite.) Pseudokoodissa toisto kirjoitetaan muodossa tai `WHILE test DO … ENDWHILE`
. Kuten viikolla 5, jokainen toisto tarvitsee rehellisen `FOR each item IN list DO … ENDFOR`
lopetuksen.

### Lohko

-, - tai -rakenteen runko — kaikki se, mikä on avaavan avainsanan ja sitä `IF WHILE FOR`
vastaavan -, - tai -rivin välissä. Tällä kurssilla lohko sisennetään `ENDIF ENDWHILE ENDFOR`
kahdella välilyönnillä, jotta silmä näkee missä rakenne alkaa ja mihin se päättyy.

### Kuivaharjoittelu

Pseudokoodin läpikäyminen käsin, rivi riviltä, paperilla, ikään kuin olisit tietokone.
Kuivaharjoittelu on sitä, että esität itse omaa kirjaimellista robottiasi (sama idea kuin viikolla 1,
nyt omalle tekstille sovellettuna). Paperilla tehty kuivaharjoittelu löytää virheitä, joita pelkkä
uudelleenlukeminen ei löydä.

### Seurantataulukko

Pieni taulukko, jonka piirrät pseudokoodin viereen kuivaharjoittelun aikana. Tavallisesti siinä
on yksi sarake jokaista muuttujaa varten sekä yksi sarake tuotokselle. Jokainen taulukon rivi
vastaa yhtä suoritettua pseudokoodiriviä. Seurantataulukko pakottaa kirjaamaan jokaisen
askeleen ylös sen sijaan, että yrittäisit pitää kaiken päässäsi.

### Virhe

Kohta pseudokoodissa, jossa todellinen tuotos ei vastaa odotettua tuotosta. Virhe on pieni,
täsmällinen vika — yksi väärä rivi, yksi väärä testi, yksi puuttuva sijoitus — ei epämääräinen
tunne siitä, että “tämä ei toimi”. Virheen nimeäminen on puolet sen korjaamisesta.

### Odotettu tuotos

Se, minkä sinä kirjoittajana halusit pseudokoodin tuottavan annetulla syötteellä. Ennen
kuivaharjoittelua kirjoitat odotetun tuotoksen paperin reunaan. Ennen, ei jälkeen — muuten
se ei enää toimi tarkistuksena.

### Todellinen tuotos

Se, mitä kuivaharjoittelu oikeasti tuotti samalla syötteellä, rivi riviltä. Kun todellinen tuotos
vastaa odotettua tuotosta sekä tavallisella että hankalalla syötteellä, voit sanoa pseudokoodin
olevan valmis. Kun ne eroavat, sinulla on virhe löydettävänä.

### Reunatapaus (uudelleen viikolta 1)

Syöte, joka sijaitsee pseudokoodin odotusten rajalla: tyhjä merkkijono, luku nolla, negatiivinen
luku, lista ilman rivejä tai salasana, joka on täsmälleen 8 merkkiä pitkä silloin kun sääntö
sanoo “vähintään 8”. Reunatapauksissa suurin osa virheistä piilee; juuri seurantataulukko
auttaa nappaamaan ne.

### Konsoli (ennakkokatsaus — viikko 7, jossa pseudokoodi kohtaa oikean kielen)

Viikolla 7 pseudokoodin sanat ja saapuvat oikeaan paikkaan ruudulla, jota `READ WRITE`
kutsutaan konsoliksi: pieneksi tekstialueeksi, jossa ohjelma kysyy syötettä ja tulostaa
tuotoksensa. Sinun ei tarvitse vielä osata käyttää konsolia — termi on mukana siksi, ettei sana
ole uusi ensi viikolla.
