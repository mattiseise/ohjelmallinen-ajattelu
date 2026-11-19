# Viikko 7 — Opiskelijatehtävät (C#)

## Yleiskatsaus tämän viikon C#-tehtäviin

Tällä viikolla on **neljä tehtävää C#-makuna**. Vihreäpiste-tehtävä (🟢 PAKOLLINEN) on **must-do-minimi** — tee se pysyäksesi luokan tahdissa. Kolme violettipiste-tehtävää (🟣 SYVENTÄVÄ) ovat valinnaisia laajennuksia; valitse yksi tai kaksi, jos sinulla on aikaa.

Kaikki, mitä kirjoitat tällä viikolla, on raaka-ainetta **AT3:lle, joka saapuu viikon 8 lopussa**. AT3 pyytää kääntämään palan omaa viikon 6 pseudokoodiasi pieneksi ohjelmaksi sillä kielellä, jonka valitset tällä viikolla. Tallenna koodisi.

IDE-asennusta ei vaadita. Ei `dotnet new`:tä, ei Visual Studiota, ei .NET SDK -asennusta. C# ajetaan tällä viikolla pienessä online-ympäristössä samassa selaimessa, jossa luet tätä. Testiframeworkkia ei ole tällä viikolla; ajat koodin, luet tulosteen, vertaat sitä siihen, mitä ennustit.

### Miten avaat online-C#-ympäristön

- **Oletus — .NET Fiddle.** Mene osoitteeseen `dotnetfiddle.net` millä tahansa selaimella. Ei tiliä tarvita. Valitse **Console** yläosasta. Liimaa koodirivisi `Main`-metodin aaltosulkeiden sisään ja paina sitten **Run**. Tuloste ilmestyy alempaan laatikkoon.
- **Vaihtoehto — sharplab.io.** Sama idea, hieman erilainen asettelu — myös selainpohjainen, ei tiliä.
- **Vaihtoehto — Replit (C#-yhteensopiva pohja).** Selainpohjainen, valinnainen kirjautuminen.

Valitse yksi ja pidä siitä kiinni viikon ajan.

---

## 🟢 PAKOLLINEN — Ensimmäinen konsoliohjelmasi (C#)

**Tavoite:** Aja ensimmäinen C#-ohjelma online-ympäristössä, joka tulostaa tervehdyksen, esittelee muuttujan ja tekee pienen laskutoimituksen. Tämä on viikon 7 must-do-minimi C#-polulla.

Kuvakaappaus, jonka tallennat tämän tehtävän lopussa, on täsmälleen sen kaltainen artefakti, jota AT3 käyttää uudelleen ensi viikolla.

### Vaiheet

1. **Avaa .NET Fiddle** osoitteessa `dotnetfiddle.net`. Valitse **Console** yläosasta. Sinun pitäisi nähdä pieni pohja `Main`-metodilla.
2. **Tulosta tervehdys oikealla nimelläsi.** Kirjoita `Main`:n sisään alla oleva rivi käyttäen **omaa nimeäsi** lainausmerkeissä:

   ```csharp
   Console.WriteLine("Hei, <oma nimesi>");
   ```

   Paina **Run**. Jos punainen virhe ilmestyy, tarkista puolipiste ja isot kirjaimet `Console.WriteLine`:ssa.
3. **Esittele muuttuja iällesi ja tulosta se.** Lisää kaksi riviä, vaihtaen `<oma ikäsi>` omaksi numeroksesi:

   ```csharp
   int age = <oma ikäsi>;
   Console.WriteLine(age);
   ```

4. **Laske vuosia täysi-ikäisyyteen ja tulosta se.** Kaksi riviä lisää:

   ```csharp
   int yearsToAdulthood = 18 - age;
   Console.WriteLine(yearsToAdulthood);
   ```

   Jos olet jo 18 tai vanhempi, luku on nolla tai negatiivinen — se on oikein.
5. **Ota kuvakaappaus** tulostelaatikosta, joka näyttää kaikki kolme riviä järjestyksessä. Liimaa se viikko 7:n muistiinpanotiedostoosi.
6. **Kirjoita 2–3 lauseen reflektio.** Yksi asia, joka yllätti sinut C#:ssa (esim. että täytyi nimetä tyyppi `int` etukäteen); yksi asia, joka toimi täsmälleen kuten ennustit.

### Pidä muistiinpanot

Pidä kuvakaappaus, koodirivit ja reflektiosi yhdessä kansiossa. **AT3 saapuu viikon 8 lopussa** ja pyytää pientä ohjelmaa tällä täsmälleen muodolla — muuttuja, laskutoimitus, tuloste. Tämän koodin uudelleenkäyttöä AT3:ssa kannustetaan.

---

## 🟣 SYVENTÄVÄ — Ensimmäinen if/else (C#)

**Tavoite:** Kirjoita 6-rivinen C#-ohjelma, joka käyttää `if/else`-rakennetta tulostaakseen toisen kahdesta viestistä muuttujan arvon mukaan. O21-itseopiskelun ohjelma omissa käsissäsi.

### Vaiheet

1. **.NET Fiddlessä** liimaa `Main`-metodin sisään alla oleva ohjelma:

   ```csharp
   int age = 16;
   if (age >= 18)
   {
       Console.WriteLine("Pääset sisään.");
   }
   else
   {
       Console.WriteLine("Olen pahoillani, et ole tarpeeksi vanha.");
   }
   ```

2. **Ennusta ennen ajamista.** Kun `age = 16`, mitä odotat tulostelaatikon tulostavan? Kirjoita se ylös **ennen** **Run**-painikkeen painamista.
3. **Aja se.** Vertaa ennustusta todellisuuteen.
4. **Vaihda iäksi 19 ja aja uudelleen.** Ennusta ensin uudelleen. Tulosteen tulisi vaihtaa haaraa.
5. **Ota kuvakaappaus molemmista ajoista.** Tallenna ne ennustusmuistiinpanojesi viereen.

### Jos teet tämän yksin

Tämä tehtävä ei oleta paria. Jos haluat toiset silmäparit, käytä **24 tunnin taukoa**: ennusta tuloste tänään, aja ohjelma huomenna ilman, että luet ennustuksesi uudelleen.

### Pidä muistiinpanot

Pidä ohjelma, molemmat ennustukset, molemmat kuvakaappaukset. **AT3 saapuu viikon 8 lopussa** ja pyytää pientä `if/else`-ohjelmaa tällä täsmälleen muodolla. Tämä tehtävä on AT3:n kenraaliharjoitus.

---

## 🟣 SYVENTÄVÄ — Käännä viikon 6 pseudokoodisi (C#)

**Tavoite:** Ota yksi pala omaa viikon 6 pseudokoodiasi, jossa on `IF/ELSE`, ja muuta se pieneksi C#-ohjelmaksi, joka ajaa .NET Fiddlessä.

Tämä on tiedoston AT3-muotoisin tehtävä. Sen tekeminen nyt tarkoittaa, että AT3 on puoliksi kirjoitettu ennen julkaisua.

### Vaiheet

1. **Valitse yksi pala viikon 6 pseudokoodiasi**, jossa on `IF` (tai `IF/ELSE`). Itse kirjoittamasi on paras.
2. **Kopioi pseudokoodi** muistiinpanotiedostoosi.
3. **Käännä se C#:ksi rivi riviltä**:
   - `READ <jokin>` → `int <jokin> = <valitsemasi arvo>;` (tai `string`, jos arvo on tekstiä) toistaiseksi.
   - `IF … THEN` → `if (…) {`.
   - `ELSE` → `} else {`.
   - `WRITE "…"` → `Console.WriteLine("…");`.
   - `ENDIF` → `}`.
4. **Liimaa C#-koodi `Main`-metodiin** ja paina **Run**. Lue mahdollinen punainen virheilmoitus — kääntäjä yleensä osoittaa suoraan riville ja kertoo, mistä sanasta se ei pitänyt.
5. **Tallenna pseudokoodi ja C# rinta rinnan** muistiinpanoissasi. Tämä on täsmälleen se artefakti, jota AT3 pyytää.

### Pidä muistiinpanot

Pidä pseudokoodi ja C# rinta rinnan. **AT3 saapuu viikon 8 lopussa** ja käyttää tätä artefaktia suoraan uudelleen.

---

## 🟣 SYVENTÄVÄ — Riko se tarkoituksella (C#)

**Tavoite:** Tuo tarkoituksella yksi virhe kerrallaan toimivaan ohjelmaasi ensimmäisestä if/else-tehtävästä ja lue täsmällinen kääntäjän viesti, jonka C# tulostaa.

Pointti on lukea **oikeita** kääntäjän viestejä, jotta ensimmäinen yllätysvirhe AT3:ssa ei pysäytä sinua. C# on tässä JavaScriptiä tiukempi: monet ongelmat ilmestyvät *käännösvirheinä* ennen kuin ohjelma edes yrittää ajaa, mikä on itse asiassa ystävällistä.

### Vaiheet

1. **Aloita toimivasta `if/else`-ohjelmasta** *Ensimmäinen if/else (C#)* -tehtävästä. Varmista, että se yhä ajaa puhtaasti.
2. **Riko se kolmella tavalla, yksi kerrallaan**, ja kopioi täsmällinen kääntäjän viesti:
   - **Unohda puolipiste.** Poista `;` `int age = 16` -rivin lopusta. (Tämä on klassinen C#-käännösvirhe, jota JavaScript ei olisi havainnut.)
   - **Mismatchaa aaltosulje.** Poista `if`-haaran sulkeva `}`.
   - **Kirjoita tulostusfunktio väärin.** Muuta `Console.WriteLine` muotoon `Console.WriteLin`.
3. **Korjaa kukin** ennen seuraavan esittelyä.
4. **Reflektio (2–3 lausetta):** mikä viesti oli selkein? Mikä oli sekava? Osoittiko jokin niistä väärälle riville?

### Jos teet tämän yksin

Tämä tehtävä ei oleta paria — kääntäjä on sparrauskumppanisi. Jos haluat toisen mielipiteen, lähetä yksi virheilmoitus luokan chattiin: *"Onko kukaan muu nähnyt tätä C#:ssa?"*

### Pidä muistiinpanot

Pidä kolme rikkinäistä riviäsi ja kolme täsmällistä kääntäjän viestiä. **AT3 saapuu viikon 8 lopussa** ja sisältää vähintään yhden virheilmoituksen, jota et ole ennen nähnyt — pieni C#-virheiden kirjasto kirjoitettuna nyt nopeuttaa sinut tuon hetken läpi.
