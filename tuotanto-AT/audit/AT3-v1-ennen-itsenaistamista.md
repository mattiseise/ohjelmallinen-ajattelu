# AT3 — arvioitava tehtävä: Pseudokoodista toimivaksi ohjelmaksi

## Tavoite

Viikolla 6 kirjoitit pseudokoodin omasta arkiprosessistasi ja jäljitit sen paperilla. Nyt kurssi sulkee silmukan: sama pseudokoodi käännetään toimivaksi ohjelmaksi, ajetaan kahdella lähtöarvolla, yksi bugi korjataan ja koko juttu selitetään ääneen kahdessa minuutissa. AT3 on kurssin viimeinen arvioitava tehtävä. Valitset itse kielen, JavaScriptin tai C#:n, ja kielikohtainen ohje on tehtävässä 8.1-JS tai 8.1-CS. Tehtävän 8.1 neljä tarkistusta ovat hyväksytyn (S) kynnys; arviointi erottelee lisäksi tasot S-, S ja S+.

## Mitä palautat ja milloin

### Kirjallinen osa (oppitunnin 23 lopussa)

Palautat viisi asiaa.

1. Lähdekoodi tiedostona (`at3.js` tai `at3.cs`) tai palautusmuistiinpanojen koodilohkona, 10–25 riviä.
2. Se pseudokoodi, josta käännös tehtiin: AT2:n tai tehtävän 6.1 pseudokoodisi, tai varamallista itse kirjoittamasi pseudokoodi (ks. vaihe 1). Opettaja vertaa käännöstä siihen.
3. Kuvakaappaus omasta ympäristöstäsi, jossa näkyvät molemmat ajot eri lähtöarvoilla.
4. Kaksi yhden rivin merkintää: "Virheilmoitus: …" sanasta sanaan (tai hiljaisen bugin kohdalla "Tuli: … / Piti tulla: …") ja "Ennuste ennen ajoa 1: …".
5. Pohdinta, 3–5 virkettä, jossa on kolme asiaa: mitä ohjelma tekee, mitä muuttujaa muutit ajojen välillä ja vastasiko tuloste ennustetta, sekä minkä bugin löysit ja minkä rivin korjasit. Halutessasi lisäät yhden virkkeen, joka nostaa arviota (ks. vaihe 6); se ei kuulu 3–5 virkkeen rajaan.

### Suullinen osa (oppitunnilla 24)

Pidät 2 minuutin esityksen neljällä kohdalla: mitä ohjelma tekee, miten se toimii, mikä meni pieleen, miten korjasit sen. Ohje, ajoitus ja tarkistukset ovat tiedostossa `lisamateriaali-l24-esitysrubriikki.md`. Lopuksi luokka nimeää yhden asian, jonka huomasi.

## Vaiheet

1. Valitse pseudokoodi. Ota AT2:n tai tehtävän 6.1 pseudokoodistasi pala, josta syntyy 10–25 riviä ohjelmaa. Jos omaa pseudokoodia ei ole, saat käyttää tehtävän 8.1 varamallia, mutta kirjoita se ensin kurssin pseudokoodina viikon 6 avainsanoilla (6–12 riviä) ja palauta se lähdepseudokoodina. Varamalli, josta on vaihdettu vain arvot ilman tätä pseudokoodivaihetta, jää tässä arviointikohteessa tasolle S-, eikä S+ ole tässä kohteessa varamallilla mahdollinen.
2. Käännä pseudokoodi rivi riviltä oman polkusi ohjeen mukaan. Säilytä muuttujanimesi: jos pseudokoodissa oli `akunProsentti`, se on ohjelmassakin `akunProsentti`. Jos huomaat kohdan, jossa pseudokoodi ja kieli eivät vastaa suoraan toisiaan, esimerkiksi "toista 3 kertaa" muuttuu laskurisilmukaksi, kirjoita se muistiin lisävirkettä varten.
3. Aja ohjelma ensimmäisellä lähtöarvolla ja lue tuloste. Kirjoita ennen ajoa yhden rivin ennuste ("Ennuste ennen ajoa 1: liian lyhyt") ja vertaa sitä toteutuneeseen.
4. Muuta yhtä muuttujaa ohjelman alussa ja aja uudelleen. Vahvin toinen lähtöarvo on rajatapaus kuten AT2:n hankala syöte: akku 0 prosentissa, tyhjä salasana, laskuri joka alkaa viidestä. Ota kuvakaappaus, jossa molemmat tulosteet näkyvät.
5. Etsi ja korjaa yksi bugi. Jos ohjelma toimi heti, aiheuta bugi tahallaan tehtävän 8.1 tapaan. Kopioi virheilmoitus sanasta sanaan omaksi rivikseen; jos bugi oli hiljainen eli ohjelma tulosti väärin kaatumatta (tehtävän 8.4 pätkä B), kirjaa rivinä, mitä tuli ja mitä piti tulla. Merkitse korjattu rivi.
6. Kirjoita pohdinta, 3–5 virkettä, kohdan "Kirjallinen osa" kolmella asialla. Vapaaehtoinen lisävirke: vaiheessa 2 muistiin kirjoittamasi kohta, jossa pseudokoodi ja kieli eivät vastanneet toisiaan, tai kumpi oli vaikeampi löytää, virheilmoituksen antanut bugi vai hiljainen bugi. Hiljaisen bugin kokemukseksi kelpaa tehtävän 8.4 pätkä B, vaikka omassa ohjelmassasi oli vain yksi bugi.
7. Harjoittele esitys ajastimella niin, että neljä kohtaa mahtuvat kahteen minuuttiin, ja varaudu jatkokysymykseen "mitä tapahtuisi, jos lähtöarvo olisi …".
8. Palauta kirjallinen osa oppitunnin 23 lopussa ja pidä esitys oppitunnilla 24.

### JavaScript-polku

Kielikohtaiset vaiheet, käännöstaulukko ja ympäristö (selaimen DevTools-konsoli) ovat tehtävässä 8.1-JS. Seuraa sen vaiheita 2–6 ja palaa tähän sivuun pohdinnan ja esityksen kohdalla.

### C#-polku

Kielikohtaiset vaiheet, käännöstaulukko ja ympäristö (.NET Fiddle, Console-tila) ovat tehtävässä 8.1-CS. Seuraa sen vaiheita 2–6 samalla tavalla.

💡 Vinkki: Jos ohjelma ei lähde toimimaan ollenkaan, se ei ole hylkäys. Liitä koodi, virheilmoitus sanasta sanaan ja kaksi virkettä siitä, mitä kokeilit: dokumentoitu epäonnistuminen täyttää tehtävän 8.1 ensimmäisen tarkistuksen.

## Mihin viikon tehtäviin tämä nojaa

Tehtävät 8.1-JS ja 8.1-CS ovat AT3:n kielikohtaiset ohjeet: valitset toisen, ja sen vaiheet tuottavat lähdekoodin, kuvakaappauksen ja bugi–korjaus-parin. Tehtävä 8.2 on silmukkalämmittely, josta saat kolme silmukkamallia AT3-ohjelman toistoa varten. Tehtävä 8.4 opetti lukemaan virheilmoituksen ja erottamaan hiljaisen bugin kaatumisesta; se nopeuttaa vaihetta 5. Tehtävät 8.3 ja 8.5 ovat valinnaisia; 8.5:n kielivertailu terävöittää esitystä, vaikka se ei kuulu AT3:een. AT2 tai tehtävä 6.1 on lähdepseudokoodi, johon opettaja vertaa käännöstäsi; tehtävän 8.1 varamalli kelpaa vain kurssin pseudokoodiksi kirjoitettuna (vaihe 1) ja rajaa ensimmäisen arviointikohteen tasolle S. Oppitunnin 24 esitysohje `lisamateriaali-l24-esitysrubriikki.md` on suullisen osan kriteeri: sen neljä kohtaa, 2 minuutin ajoitus ja neljä tarkistusta ovat se, mitä esityksestä katsotaan.

## Jos teet tämän yksin

Oppitunnin 24 esitys olettaa yleisön. Jos et voi esittää livenä esimerkiksi sairauden takia, tallenna 2 minuutin video, jossa esittelet ohjelman kameralle, tai lähetä ohjelma ja 3 virkkeen tiivistelmä luokan chattiin. Neljä kohtaa ovat samat kuin livenä. Pyydä chatissa yhtä luokkakaveria nimeämään yksi asia, jonka hän huomasi: se on vertaishavaintosi.

## Arviointikohteet

- **Käännös omasta pseudokoodista** — arvioija katsoo, vastaako 10–25 rivin ohjelma palautettua pseudokoodiasi rivi riviltä ja toimiiko se tai onko epäonnistunut yritys dokumentoitu.
- **Testaus kahdella lähtöarvolla** — arvioija katsoo, näyttääkö kuvakaappaus kaksi ajoa eri lähtöarvoilla ja nimeääkö pohdinta muutetun muuttujan.
- **Bugi ja korjaus** — arvioija katsoo, onko yksi bugi nimetty yleiskielellä, virheilmoitus lainattu sanasta sanaan ja korjattu rivi näytetty.
- **Suullinen esitys** — arvioija katsoo, pidettiinkö 2 minuutin esitys neljällä kohdalla esitysohjeen mukaan.
