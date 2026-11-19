# Sanasto

## Viikon 6 sanasto

Alla olevat termit kattavat oppitunnit 16, 17 ja 18. Määritelmät ovat lyhyitä tarkoituksella — lue itseopiskelu nähdäksesi esimerkit kontekstissa. Yksi termi lopussa (*console*) on viikon 7 esikatselu, ja se on merkitty sellaiseksi.

### Pseudokoodi

Tiukempi, sääntösidonnaisempi tapa kirjoittaa prosessikuvauksia paperille. Se käyttää pientä jaettua avainsanajoukkoa (`SET`, `IF`, `WHILE` ja niin edelleen), mutta on edelleen tarkoitettu ihmisten luettavaksi, ei tietokoneen ajettavaksi. Pseudokoodi on silta arkikielen ja oikean koodin välillä: tarpeeksi täsmällistä, että tietokone osaisi tarvittaessa noudattaa sitä, mutta tarpeeksi luettavaa jaettavaksi henkilölle, joka ei osaa ohjelmoida.

### Avainsana

Yksi pienistä kiinteistä sanoista, joita pseudokoodi käyttää merkitsemään rakennetta: `SET`, `READ`, `WRITE`, `IF`, `ELSE`, `ENDIF`, `WHILE`, `ENDWHILE`, `FOR`, `ENDFOR`. Avainsanat näyttävät aina samalta (ISOIN KIRJAIMIN tällä kurssilla), jotta silmä löytää ne nopeasti. Kaikki, mikä ei ole avainsana, on omaa englantiasi: muuttujan nimi, arvo, viesti.

### Muuttuja

Nimetty säilö yhdelle arvolle, joka voi muuttua pseudokoodin suorituksen aikana. *"Tee post-it-lappu purkkiin, jossa lukee `passwordLength`; lapulla oleva numero voi muuttua, mutta lappu pysyy."* Tänään muuttuja saattaa pitää lukua, huomenna kyllä/ei-arvoa, ylihuomenna lyhyttä merkkijonoa.

### Arvo

Muuttujassa annetulla hetkellä tallennettu varsinainen sisältö — luku (`7`), kyllä/ei (`YES`) tai lyhyt teksti (`"hunter2"`). Muuttuja on etiketöity laatikko; arvo on se, mitä laatikon sisällä on juuri nyt.

### Sijoitus

Toimenpide, jolla arvo laitetaan muuttujaan. Tällä kurssilla se kirjoitetaan aina `SET variableName TO value`, esimerkiksi `SET passwordLength TO 7`. Sijoituksen jälkeen muuttuja pitää uutta arvoa ja unohtaa vanhan.

### Syöte

Mitä pseudokoodi ottaa vastaan ulkoa — yleensä luku, merkkijono tai kyllä/ei, jonka käyttäjä kirjoittaa. Pseudokoodissa se näkyy muodossa `READ variableName`. Ennen kuin syöte saapuu, muuttujalla ei ole vielä hyödyllistä arvoa.

### Käsittely

Mitä pseudokoodi tekee keskellä, syötteen lukemisen ja tulosteen kirjoittamisen välillä. Käsittelyssä säännöt elävät: ehto, joka päättää, mikä haara otetaan, toisto, joka tekee jotain jokaiselle alkiolle, sijoitus, joka yhdistää arvoja.

### Tuloste

Mitä pseudokoodi lähettää takaisin ulkomaailmaan — yleensä lyhyt viesti, luku tai kyllä/ei. Pseudokoodissa se näkyy muodossa `WRITE expression`. Tuloste on se, mitä käyttäjä todella näkee.

### Ehto

Testi, joka päättää, mihin haaraan pseudokoodi siirtyy seuraavaksi. *(Kerrataan viikolta 5.)* Pseudokoodissa se kirjoitetaan muodossa `IF test THEN … ELSE … ENDIF`. `IF` ja `ENDIF` merkitsevät, mistä testi alkaa ja minne se päättyy, jotta lukija näkee haarat yhdellä silmäyksellä.

### Toisto

Saman pseudokoodilohkon tekeminen useammin kuin kerran, pysäytysehdolla. *(Kerrataan viikolta 5.)* Pseudokoodissa se kirjoitetaan muodossa `WHILE test DO … ENDWHILE` tai `FOR each item IN list DO … ENDFOR`. Kuten viikolla 5, jokainen toisto tarvitsee rehellisen pysäytyksen.

### Lohko

`IF`:n, `WHILE`:n tai `FOR`:n runko — kaikki avaavan avainsanan ja sen vastaavan `ENDIF`:n, `ENDWHILE`:n tai `ENDFOR`:n välissä. Lohko sisennetään kahdella välilyönnillä tällä kurssilla, jotta silmä näkee, mistä rakenteen sisäpuoli alkaa ja päättyy.

### Käsiajo

Pseudokoodipätkän läpikäyminen käsin, rivi riviltä, paperilla, esittäen tietokonetta. Käsiajo on sinä, joka näyttelet sananmukaista robottia omalle pseudokoodillesi (sama sananmukainen robotti -idea viikolta 1, sovellettuna omaan tekstiisi). Käsiajo paperilla löytää bugeja, joita uudelleenlukeminen ei.

### Jäljityskaavio

Pieni taulukko, jonka piirrät pseudokoodisi viereen sen aikana kun käsiajat sitä. Siinä on yleensä yksi sarake per muuttuja ja sarake tulosteelle. Jokainen taulukon rivi on yksi suoritettu pseudokoodirivi. Jäljityskaavio pakottaa kirjoittamaan jokaisen askeleen alas sen sijaan, että teeskentelet pitäväsi kaiken päässä.

### Bugi

Paikka pseudokoodissasi, jossa todellinen tuloste ei täsmää odotettuun tulosteeseen. Bugi on pieni, täsmällinen vika — yksi väärä rivi, yksi väärä testi, yksi puuttuva sijoitus — ei epämääräinen "se ei toimi". Bugin nimeäminen on puolet sen korjaamisesta.

### Odotettu tuloste

Mitä sinä, kirjoittaja, halusit pseudokoodin kirjoittavan annetulla syötteellä. Ennen kuin käsiajat, kirjoita odotettu tuloste sivun reunaan. *Ennen* — ei jälkeen; muuten se lakkaa olemasta tarkistus.

### Todellinen tuloste

Mitä käsiajo todella tuotti samalle syötteelle, rivi riviltä. Kun *todellinen tuloste* täsmää *odotettuun tulosteeseen* sekä normaalilla syötteellä että hankalalla, voit kutsua pseudokoodia valmiiksi. Kun ne ovat eri mieltä, sinulla on bugi etsittävänä.

### Rajatapaus

*(Kerrataan viikolta 1.)* Syöte, joka istuu sen rajalla, mitä pseudokoodi odottaa: tyhjä merkkijono, luku nolla, negatiivinen luku, lista, jossa ei ole alkioita, salasana, joka on täsmälleen 8 merkkiä pitkä, kun sääntö sanoo "vähintään 8". Rajatapaukset ovat paikkoja, joissa useimmat bugit piileskelevät; jäljityskaavio on se, mikä löytää ne.

### Console *(katse eteenpäin — viikko 7, jossa pseudokoodi kohtaa oikean kielen)*

Viikolla 7 pseudokoodisi sanat `READ` ja `WRITE` alkavat laskeutua oikeaan paikkaan ruudulla nimeltä *console*: pienelle tekstialueelle, jossa ohjelma pyytää syötettä ja tulostaa sen tulosteensa. Sinun ei tarvitse vielä osata käyttää konsolia — tämä termi on tässä, jotta sana ei ole uusi ensi viikolla.
