# AT3 — arvioitava tehtävä: Pseudokoodista toimivaksi ohjelmaksi

## Tavoite

Viikolla 6 kirjoitit pseudokoodin omasta arkiprosessistasi ja jäljitit sen paperilla. Nyt kurssi sulkee silmukan: sama pseudokoodi käännetään toimivaksi ohjelmaksi, ajetaan kahdella lähtöarvolla, yksi bugi korjataan ja koko juttu selitetään ääneen kahdessa minuutissa. AT3 on kurssin viimeinen arvioitava tehtävä. Valitset itse kielen, JavaScriptin tai C#:n; kummankin polku on tällä sivulla. Suullisen osan neljä tarkistusta ovat hyväksytyn (S) kynnys; arviointi erottelee lisäksi tasot S-, S ja S+.

## Mitä palautat ja milloin

### Kirjallinen osa (oppitunnin 23 lopussa)

Palautat viisi asiaa.

1. Lähdekoodi tiedostona (`at3.js` tai `at3.cs`) tai palautukseen liitettynä tekstinä, 10–25 riviä.
2. Se pseudokoodi, josta käännös tehtiin: AT2:n tai tehtävän 6.1 pseudokoodisi, tai varamallista itse kirjoittamasi pseudokoodi (ks. vaihe 1). Opettaja vertaa käännöstä siihen.
3. Kuvakaappaus omasta ympäristöstäsi, jossa näkyvät molemmat ajot eri lähtöarvoilla.
4. Kaksi yhden rivin merkintää: "Virheilmoitus: …" sanasta sanaan (tai hiljaisen bugin kohdalla "Tuli: … / Piti tulla: …") ja "Ennuste ennen ajoa 1: …".
5. Pohdinta, 3–5 virkettä, jossa on kolme asiaa: mitä ohjelma tekee, mitä muuttujaa muutit ajojen välillä ja vastasiko tuloste ennustetta, sekä minkä bugin löysit ja minkä rivin korjasit. Halutessasi lisäät yhden virkkeen, joka nostaa arviota (ks. vaihe 6); se ei kuulu 3–5 virkkeen rajaan.

### Suullinen osa (oppitunnilla 24)

Pidät 2 minuutin esityksen, jossa on neljä kohtaa, noin 30 sekuntia kukin.

1. Mitä ohjelma tekee: yksi tai kaksi virkettä yleiskielellä.
2. Miten se tekee sen: muuttujat, if/else ja silmukka, jos sellainen on mukana.
3. Mikä meni pieleen: yksi bugi nimeltä, esimerkiksi "kirjoitin `scre` enkä `score`".
4. Miten korjasit sen: se yksi rivi, jota muutit.

Käytä puhelimen ajastinta niin, että se näkyy luokalle. Alle ajan on ok; yli ajan ei. Dioja tai ulkoa opeteltua käsikirjoitusta ei tarvita: esityksessä arvioidaan ymmärrystä, ei esiintymistä.

Opettaja tarkistaa neljä asiaa: ohjelma toimii tai epäonnistunut yritys on dokumentoitu virheilmoituksineen; osaat nimetä yleiskielellä, mitä ohjelma tekee; kuvaat yhden bugi–korjaus-parin; pidit 2 minuutin esityksen. Nämä neljä ovat hyväksytyn (S) kynnys. Lopuksi luokka nimeää yhden asian, jonka huomasi. Opettaja heijastaa saman ohjeen (`lisamateriaali-l24-esitysrubriikki.md`) esitysten välissä.

## Vaiheet

1. Valitse pseudokoodi. Ota AT2:n tai tehtävän 6.1 pseudokoodistasi pala, josta syntyy 10–25 riviä ohjelmaa. Jos omaa pseudokoodia ei ole, saat käyttää tehtävän 8.1 varamallia (ikärajan tarkistus; salasanan pituustarkistus; pisteistä palautteeksi; yksinkertainen laskuri 1–5; tervehdys nimellä kolme kertaa), mutta kirjoita se ensin kurssin pseudokoodina avainsanoilla SET, READ, WRITE, IF/ELSE/ENDIF, WHILE/ENDWHILE ja FOR/ENDFOR (6–12 riviä) ja palauta se lähdepseudokoodina. Varamalli, josta on vaihdettu vain arvot ilman tätä pseudokoodivaihetta, jää tässä arviointikohteessa tasolle S-, eikä S+ ole tässä kohteessa varamallilla mahdollinen.
2. Käännä pseudokoodi rivi riviltä oman polkusi ohjeen mukaan. Säilytä muuttujanimesi: jos pseudokoodissa oli `akunProsentti`, se on ohjelmassakin `akunProsentti`. Jos huomaat kohdan, jossa pseudokoodi ja kieli eivät vastaa suoraan toisiaan, esimerkiksi "toista 3 kertaa" muuttuu laskurisilmukaksi, kirjoita se muistiin lisävirkettä varten.
3. Aja ohjelma ensimmäisellä lähtöarvolla ja lue tuloste. Kirjoita ennen ajoa yhden rivin ennuste ("Ennuste ennen ajoa 1: liian lyhyt") ja vertaa sitä toteutuneeseen.
4. Muuta yhtä muuttujaa ohjelman alussa ja aja uudelleen. Vahvin toinen lähtöarvo on rajatapaus kuten AT2:n hankala syöte: akku 0 prosentissa, tyhjä salasana, laskuri joka alkaa viidestä. Ota kuvakaappaus, jossa molemmat tulosteet näkyvät.
5. Etsi ja korjaa yksi bugi. Jos ohjelma toimi heti, aiheuta bugi tahallaan polkusi vaiheen 5 tapaan. Kopioi virheilmoitus sanasta sanaan omaksi rivikseen; jos bugi oli hiljainen eli ohjelma tulosti väärin kaatumatta, kirjaa rivinä, mitä tuli ja mitä piti tulla. Merkitse korjattu rivi.
6. Kirjoita pohdinta, 3–5 virkettä, kohdan "Kirjallinen osa" kolmella asialla. Vapaaehtoinen lisävirke: vaiheessa 2 muistiin kirjoittamasi kohta, jossa pseudokoodi ja kieli eivät vastanneet toisiaan, tai kumpi oli vaikeampi löytää, virheilmoituksen antanut bugi vai hiljainen bugi. Hiljaisen bugin kokemukseksi kelpaa tehtävän 8.4 pätkä B (`if (ika = 18)` yhdellä yhtäsuuruusmerkillä).
7. Harjoittele esitys ajastimella niin, että neljä kohtaa mahtuvat kahteen minuuttiin, ja varaudu jatkokysymykseen "mitä tapahtuisi, jos lähtöarvo olisi …".
8. Palauta kirjallinen osa oppitunnin 23 lopussa ja pidä esitys oppitunnilla 24.

Vaiheet 2–5 tehdään valitsemallasi kielellä; alla on kummankin kielen polku. Tehtävät 8.1-JS ja 8.1-CS ovat sama ohje laajempana, mutta tämä sivu riittää.

### JavaScript-polku

1. Avaa selaimen DevTools-konsoli: Macilla `Cmd + Opt + J`, Windowsissa ja Linuxissa `Ctrl + Shift + J`. Mitään ei tarvitse asentaa.
2. Käännä pseudokoodi rivi riviltä tällä taulukolla. READ-rivit korvataan kovakoodatulla arvolla ohjelman alussa, esimerkiksi `let salasana = "hei";`; `prompt()`-komentoa ei tarvita.

| Pseudokoodi | JavaScript |
|---|---|
| `SET nimi TO arvo` (ensimmäinen kerta) | `let nimi = arvo;` |
| `SET nimi TO uusi arvo` (muuttuja jo luotu) | `nimi = uusi arvo;` |
| `READ nimi` | `let nimi = "kovakoodattu arvo";` ohjelman alussa |
| `WRITE "teksti"` | `console.log("teksti");` |
| `IF ehto THEN … ELSE … ENDIF` | `if (ehto) { … } else { … }` |
| `WHILE ehto DO … ENDWHILE` | `while (ehto) { … }` |
| `FOR each … / toista N kertaa` | `for (let i = 0; i < N; i++) { … }` |

Kirjoita `let` vain muuttujan ensimmäiselle riville; jos määrittelet saman nimen uudelleen, konsoli antaa virheen "has already been declared".

3. Liitä koko ohjelma konsoliin, paina Enter ja lue tuloste. Ennuste kirjoitetaan ennen Enteriä (vaihe 3).
4. Toinen ajo: muuta yhtä muuttujaa ohjelman alussa, liitä ja aja uudelleen. Kuvakaappaus molemmista tulosteista (vaihe 4).
5. Bugi: kirjoita yhden muuttujan nimi väärin tai poista yksi `;`. Konsoli antaa virheilmoituksen, esimerkiksi `ReferenceError: salasna is not defined`. Kopioi se sanasta sanaan, korjaa rivi ja aja uudelleen (vaihe 5).
6. Tallenna lähdekoodi nimellä `at3.js` tai liitä se palautukseen koodilohkona, jonka kielimerkintä on `js`.

### C#-polku

1. Avaa `dotnetfiddle.net` selaimessa ja valitse Console-tila. Mitään ei tarvitse asentaa; ohjelma kirjoitetaan `Main`-metodin sisään.
2. Käännä pseudokoodi rivi riviltä tällä taulukolla. READ-rivit korvataan kovakoodatulla arvolla ohjelman alussa, esimerkiksi `string salasana = "hei";`; `Console.ReadLine()`-komentoa ei tarvita. C# vaatii muuttujalle tyypin: `int` luvulle, `string` tekstille.

| Pseudokoodi | C# |
|---|---|
| `SET nimi TO arvo` (ensimmäinen kerta) | `int nimi = arvo;` tai `string nimi = "arvo";` |
| `SET nimi TO uusi arvo` (muuttuja jo luotu) | `nimi = uusi arvo;` |
| `READ nimi` | `int nimi = 5;` tai `string nimi = "arvo";` ohjelman alussa |
| `WRITE "teksti"` | `Console.WriteLine("teksti");` |
| `IF ehto THEN … ELSE … ENDIF` | `if (ehto) { … } else { … }` |
| `WHILE ehto DO … ENDWHILE` | `while (ehto) { … }` |
| `FOR each … / toista N kertaa` | `for (int i = 0; i < N; i++) { … }` |

Kirjoita tyyppi (`int`, `string`) vain muuttujan ensimmäiselle riville; jos määrittelet saman nimen uudelleen, kääntäjä antaa virheen CS0128 tai CS0136.

3. Liitä koodi `Main`-metodiin, paina Run ja lue tuloste alla olevasta ruudusta. Ennuste kirjoitetaan ennen Runia (vaihe 3).
4. Toinen ajo: muuta yhtä muuttujaa ohjelman alussa ja paina Run uudelleen. Kuvakaappaus molemmista tulosteista (vaihe 4).
5. Bugi: kirjoita yhden muuttujan nimi väärin tai poista yksi `;`. Kääntäjä antaa virheilmoituksen, esimerkiksi `CS0103: The name 'salasna' does not exist in the current context`. Kopioi se sanasta sanaan, korjaa rivi ja paina Run uudelleen (vaihe 5).
6. Tallenna lähdekoodi nimellä `at3.cs` tai liitä se palautukseen koodilohkona, jonka kielimerkintä on `csharp`.

💡 Vinkki: Jos ohjelma ei lähde toimimaan ollenkaan, se ei ole hylkäys. Liitä koodi, virheilmoitus sanasta sanaan ja kaksi virkettä siitä, mitä kokeilit: dokumentoitu epäonnistuminen täyttää suullisen osan ensimmäisen tarkistuksen.

## Mihin viikon tehtäviin tämä nojaa

Tämä sivu riittää AT3:n tekemiseen; viikon 8 tehtävät ovat taustaa, joka helpottaa työtä. Tehtävät 8.1-JS ja 8.1-CS ovat sama ohje laajempana, koodiesimerkkeineen. Tehtävä 8.2 antaa kolme silmukkamallia AT3-ohjelman toistoon. Tehtävä 8.4 opetti lukemaan virheilmoituksen ja erottamaan hiljaisen bugin kaatumisesta. Tehtävät 8.3 ja 8.5 ovat valinnaisia; 8.5:n kielivertailu terävöittää esitystä. Lähdepseudokoodi on AT2:n tai tehtävän 6.1 pseudokoodisi; jos sitä ei ole, vaiheen 1 varamalli kurssin pseudokoodiksi kirjoitettuna kelpaa ja rajaa ensimmäisen arviointikohteen tasolle S.

## Jos teet tämän yksin

Esitys olettaa yleisön. Jos et voi esittää livenä, tallenna 2 minuutin video, jossa esittelet ohjelman kameralle, tai lähetä ohjelma ja 3 virkkeen tiivistelmä luokan chattiin. Neljä kohtaa ovat samat kuin livenä. Pyydä chatissa yhtä luokkakaveria nimeämään yksi asia, jonka hän huomasi: se on vertaishavaintosi.

## Arviointikohteet

- **Käännös omasta pseudokoodista** — arvioija katsoo, vastaako 10–25 rivin ohjelma palautettua pseudokoodiasi rivi riviltä ja toimiiko se tai onko epäonnistunut yritys dokumentoitu.
- **Testaus kahdella lähtöarvolla** — arvioija katsoo, näyttääkö kuvakaappaus kaksi ajoa eri lähtöarvoilla ja nimeääkö pohdinta muutetun muuttujan.
- **Bugi ja korjaus** — arvioija katsoo, onko yksi bugi nimetty yleiskielellä, virheilmoitus lainattu sanasta sanaan ja korjattu rivi näytetty.
- **Suullinen esitys** — arvioija katsoo, pidettiinkö 2 minuutin esitys neljällä kohdalla suullisen osan ohjeen mukaan.
