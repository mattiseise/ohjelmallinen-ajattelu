# Sanasto

## Viikon 2 sanasto

Alla olevat termit kattavat oppitunnit 4, 5 ja 6. Määritelmät ovat tarkoituksella lyhyitä — itseopiskeluteksti sisältää esimerkit kontekstissa. Yksi termi lopussa (*abstraktio*) on viikon 3 ennakkokatsaus, ja se on merkitty sellaiseksi. *Ositus* esiteltiin viikolla 1; tällä viikolla se saa täyden määritelmän.

### Ositus
Liike, jossa otetaan tehtävä, joka on liian iso yhdelle tasaiselle vaihelistalle, ja pilkotaan se **päätehtäväksi**, jolla on **tavoite**, ja pieneksi joukoksi **osatehtäviä**, joilla kullakin on oma osatavoite. Ositus on suunnitteluliike — varsinaisten vaiheiden täytyy yhä olla olemassa pintaa syvemmällä, vain hallittavan kokoisina. *"Tee aamiainen neljälle hengelle"* pilkkoutuu osiin: *päätä menu*, *tarkista jääkaappi*, *valmista lämmin ruoka*, *valmista kylmä ruoka*, *kata pöytä*, *kutsu kaikki pöytään*.

### Päätehtävä
Ylätason tehtävä, jonka olet aikeissa suorittaa. Päätehtävällä on yksi **tavoite** — lyhyt lause, joka kertoo, miltä lopputilan tulisi näyttää. *"Tee aamiainen neljälle hengelle klo 8:30 mennessä"* on päätehtävä; sen tavoite on *"kaikki syövät aamiaista klo 8:30 mennessä."*

### Osatehtävä
Pienempi tehtävä, joka asuu päätehtävän alla. Osatehtävä on riittävän pieni, että pystyt kirjoittamaan sille puhtaan pikku algoritmin (yhden lyhyen sananmukaisen vaihesekvenssin), ja sillä on oma **osatavoite**. *"Valmista lämmin ruoka"* on tehtävän *"tee aamiainen neljälle hengelle"* osatehtävä.

### Osatavoite
Yhden tietyn osatehtävän tavoite, kirjoitettuna yhdellä lauseella. Osatavoite ei ole sama kuin päätehtävän tavoite — se on kapeampi ja tarkempi. Osatehtävän *"valmista lämmin ruoka"* osatavoite voisi olla *"munakokkeli ja paahtoleipä ovat lämpiminä tarjoiluvadilla."*

### Tavoite (kertaus)
Mitä tehtävä yrittää saavuttaa — lopputila. Tutustuit *tavoitteeseen* viikolla 1 algoritmin yhteydessä; tällä viikolla se koskee sekä päätehtävää että erikseen jokaista osatehtävää. Hyvä nyrkkisääntö: jos et pysty kirjoittamaan tavoitetta yhdellä lyhyellä lauseella, tehtävä on edelleen liian iso tai liian epämääräinen.

### Riippuvuus
Yhteys kahden osatehtävän välillä, jossa toinen tarvitsee toisen **tulosteen** ennen kuin se voi alkaa. *"Kaada vesi kuppiin"* riippuu osatehtävästä *"keitä vesi"*, koska keittämisen tuloste (kuuma vesi) on kaatamisen syöte. Riippuvuudet naulaavat jotkut osatehtävät kiinteään järjestykseen; ne osatehtävät, joilla ei ole keskinäistä riippuvuutta, ovat järjestykseltään vapaita.

### Järjestys (osatehtävien)
Sekvenssi, jossa osatehtävät tosiasiassa suoritetaan. Järjestys ei ole vapaa — riippuvuudet rajoittavat sitä. Kaksi osatehtävää, joilla ei ole keskinäistä riippuvuutta, voivat tulla kummassa järjestyksessä tahansa, mutta järkevä oletusjärjestys auttaa silti sananmukaista tulkitsijaa.

### Sekvenssi (kertaus)
Lista asioita järjestyksessä. Viikolla 1 kirjoitit algoritmeja vaihesekvenssinä; viikolla 2 kirjoitat sekvenssin **osatehtäviä**, joissa kukin osatehtävä on itse pieni vaihesekvenssi.

### Edellytys
Ehto, jonka on oltava tosi ennen kuin voit aloittaa osatehtävän. Edellytys on lähellä riippuvuutta, mutta ei identtinen: riippuvuus on yhteys kahden osatehtävän välillä, kun taas edellytys on maailman tila ("kannettava on otettu pakkauksesta ja kytketty päälle"), jonka on pidettävä ennen kuin osatehtävä voi alkaa. Monet edellytykset täyttyvät toisen osatehtävän tulosteesta, ja silloin nämä kaksi ideaa menevät päällekkäin.

### Rinnakkainen (vain epämuodollinen merkitys)
Kaksi osatehtävää ovat *rinnakkaisia*, kun niillä ei ole keskinäistä riippuvuutta ja ne voisivat tapahtua samaan aikaan — esimerkiksi kaksi ihmistä tekisi ne yhtä aikaa, tai yksi ihminen vaihtaa niiden välillä. Tällä kurssilla *rinnakkainen* käytetään vain arkikielen merkityksessä; tekninen samanaikaisuuden idea **ei** esitellä tällä viikolla.

### Ylätehtävä
Toinen nimi päätehtävälle, kun haluat korostaa hierarkiaa: ylätehtävä sijaitsee osatehtäviensä yläpuolella. *"Perehdytä uusi kollega"* on ylätehtävä osatehtäville *"tilaa kannettava", "aseta sähköposti", "esittele tiimille."*

### Hierarkia
Osituksen epämuodollinen muoto: yksi päätehtävä ylimpänä, osatehtävät alla. Jos osatehtävä on itse riittävän iso, voit pilkkoa *senkin* pienemmiksi osatehtäviksi, ja hierarkia menee tasoa syvemmälle. Viikko 2 pysyy yhdessä tai enintään kahdessa tasossa syvällä.

### Sananmukainen tulkitsija (kertaus)
Viikon 1 idea, edelleen voimassa: jokainen osatehtävä, yksinään, täytyy pystyä kirjoittamaan selvänä sananmukaisten vaiheiden sekvenssinä, jonka sananmukainen tulkitsija voi suorittaa. Ositus ei poista sananmukaisen tulkitsijan ajatusmallia; se pinoutuu sen päälle.

### AT1
Kurssin ensimmäinen arvioitava tehtävä. Se palautetaan oppitunnin 6 lopussa. AT1 pyytää sinua pilkkomaan yhden tehtävän (arkielämästä tai ICT:hen liittyvä) päätehtäväksi, jolla on tavoite, 4–8 osatehtäväksi, joilla on osatavoitteet, ja järjestykseen, jossa vähintään yksi riippuvuus on nostettu esiin. Muistiinpanot, jotka pidät tämän viikon tehtävistä, ovat raaka-aineesi.

### Abstraktio *(katsaus eteenpäin — viikon 3 keskeinen aihe)*
Liike, jossa piilotetaan yksityiskohdat, joita et tarvitse, ja säilytetään vain se mikä on olennaista. Viikko 3 esittelee sen muodollisesti; toistaiseksi huomaa, että kun sanot *"valmista lämmin ruoka"* osatehtävänä, abstrahoit jo — et vielä sano, *mitä* lämmintä ruokaa, *millä* pannulla, *missä* lämpötilassa. Tämä piilottaminen tekee osatehtävän nimestä käyttökelpoisen suunnittelutasolla.
