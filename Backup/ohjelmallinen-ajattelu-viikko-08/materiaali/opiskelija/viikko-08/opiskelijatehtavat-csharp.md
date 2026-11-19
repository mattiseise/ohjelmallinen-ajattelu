# Viikko 8 — Opiskelijatehtävät (C#)

## Yleiskatsaus viikon tehtäviin

Tällä viikolla on **kaksi 🟢 PAKOLLISTA** ja **kolme 🟣 SYVENTÄVÄÄ** C#-tehtävää. Pakolliset tehtävät ovat sinun **must-do minimum** — viimeistele molemmat läpäistäksesi AT3:n. Syventävät tehtävät ovat valinnaisia; valitse yksi tai kaksi, jos sinulla on aikaa.

**AT3 on tämän viikon keskeinen tuotos.** Tehtävä 8.1-CS *on* AT3-briiffaus. Palautat lähdekoodin, kuvakaappauksen ja lyhyen reflektion O23:n lopussa ja pidät **2 minuutin** suullisen esityksen O24:llä. Tehtävä 8.2-CS on pieni silmukan lämmittely ennen kuin käännät oman pseudokoodisi.

C# pyörii **.NET Fiddlessä** (`dotnetfiddle.net`); ei asennusta. "Testaaminen" tarkoittaa ajamista kahdella eri arvolla; "virheenkorjaus" tarkoittaa kääntäjän viestin lukemista ja yhden rivin muuttamista.

---

## 🟢 PAKOLLINEN — Tehtävä 8.1-CS — AT3-briiffaus: käännä viikon 6 pseudokoodisi C#:iin

**Tavoite.** Käännä yksi pala omaa viikon 6 pseudokoodiasi pieneksi, toimivaksi C#-ohjelmaksi (noin 10–25 riviä), aja se .NET Fiddlessä kahdella eri alkuarvolla, löydä ja korjaa yksi bugi ja valmistele **2 minuutin** suullinen esitys. Tämä on **AT3**.

**Tämä on viikon 8 must-do minimum.** Ilman tätä tehtävää ei ole AT3:a.

### Vaiheet

1. **Valitse yksi pala viikon 6 pseudokoodistasi** (6–20 riviä). Jos et löydä yhtä, käytä varamallia ja mukauta arvot: ikätarkistus; salasanan pituuden tarkistus; pisteet palautteeksi; yksinkertainen laskuri (1–5); tervehdys nimellä kolme kertaa.
2. **Käännä se rivi riviltä C#:iin** käyttäen `self-study.md`:n käännöstaulukkoa. Käytä kovakoodattuja muuttuja-arvoja ylhäällä (ei `Console.ReadLine()`:ä tarvita). Esimerkki:

   ```csharp
   string password = "hi";
   if (password.Length >= 8) {
       Console.WriteLine("strong enough");
   } else {
       Console.WriteLine("too short");
   }
   ```

3. **Avaa .NET Fiddle**, valitse **Console**, liitä `Main`-metodiin, paina **Run**.
4. **Aja se kahdella eri alkuarvolla.** Vaihda yhtä muuttujaa ylhäällä ja aja kumpikin versio. Ota **kuvakaappaus**, jossa molemmat tulosteet näkyvät.
5. **Löydä ja korjaa yksi bugi.** Jos ohjelmasi pyöri ensimmäisellä yrityksellä, **laukaise** bugi tarkoituksella: kirjoita yhden muuttujan nimi tarkoituksella väärin tai poista yksi `;`. Paina Run, lue kääntäjän tai ajonaikainen viesti, korjaa se takaisin. Nimeä bugi selkeällä suomella ("minulla oli `passwrd` `password`:n sijaan; kääntäjä sanoi CS0103").
6. **Tallenna lähdekoodi** nimellä `at3.cs` (tai liitä aidattuna ```csharp-lohkona palautusmuistiinpanoihisi).
7. **Kirjoita 3–5 lauseen reflektio**, jossa nimeät, mitä ohjelma tekee, sen yhden bugin, jonka löysit, ja sen yhden korjauksen, jonka teit.
8. **Valmistele 2 minuutin suullinen esityksesi** O24:lle. Neljä kohtaa, ~30 sekuntia kukin: **mitä** ohjelma tekee → **miten** se toimii (muuttujat, `if/else`, silmukka?) → **mikä** meni vikaan → **miten** korjasit sen. Harjoittele puhelimen ajastimella.

### Jos teet tämän yksin

O24:n esitys olettaa yleisön. Jos et pysty esittämään livenä — sairaus, hybridiosallistuminen — nauhoita **2 minuutin** video esittäen kameralle, *tai* julkaise ohjelma plus 3 lauseen tiivistelmä luokan chatissa. Neljä kohtaa ovat samat.

### Säilytä muistiinpanosi

Tämä **on** **AT3**. Tuo neljä artefaktia O24:lle: lähdekooditiedosto (`at3.cs`), kuvakaappaus kahdesta ajosta, 3–5 lauseen reflektio, jossa nimeät bugin ja korjauksen, ja itsesi valmiina pitämään **2 minuutin** suullisen esityksen.

AT3 **palautetaan O23:n lopussa** ja **esitetään O24:llä**. Hyväksytty / ei-vielä-hyväksytty neljän tarkistuksen perusteella: ohjelma pyörii (tai epäonnistunut yrityksesi on dokumentoitu), osaat nimetä, mitä se tekee, yksi bugi-ja-korjaus-pari on kuvattu, **2 minuutin** esitys on pidetty.

---

## 🟢 PAKOLLINEN — Tehtävä 8.2-CS — Silmukan lämmittely: laske 1:stä 5:een C#:lla

**Tavoite.** Kirjoita kolme lyhyttä `for`-silmukkaa C#:lla, jotta silmukkakuvio on sormissasi ennen AT3:a.

**Tämä on osa viikon 8 must-do minimumia.**

### Vaiheet

1. **Avaa .NET Fiddle**, valitse **Console**, liitä `Main`-metodiin ja paina **Run**:

   ```csharp
   for (int i = 1; i <= 5; i++) {
       Console.WriteLine(i);
   }
   ```

   Odotettu tuloste: 1, 2, 3, 4, 5, yksi per rivi.
2. **Muokkaa se tulostamaan 5:stä alas 1:een.** Vaihda `i = 1` → `i = 5`, `i <= 5` → `i >= 1`, `i++` → `i--`. Paina **Run**.
3. **Muokkaa se tulostamaan "Hello, NAME" kolme kertaa.** Korvaa nimesi lainausmerkkien sisään:

   ```csharp
   for (int i = 0; i < 3; i++) {
       Console.WriteLine("Hello, <oma nimesi>");
   }
   ```

4. **Tallenna kaikki kolme pätkää yhteen tiedostoon** (`loop-warmup.cs`) yhden rivin kommentilla kunkin yläpuolella.

### Säilytä muistiinpanosi

Nämä kolme kuviota ovat täsmälleen ne silmukkamuodot, joita saatat tarvita **AT3**-ohjelmassasi. Säilytä `loop-warmup.cs` samassa kansiossa kuin AT3-tiedostosi.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.3-CS — Yhdistä silmukka + if/else C#:ssa

**Tavoite.** Kirjoita pieni C#-ohjelma, joka silmukoi 5 salasanan listan läpi ja tulostaa "long enough" tai "too short" jokaiselle.

**Huomio taulukosta.** `string[]` on lista merkkijonoja. `passwords[0]` käsittelee sen yhtä alkiota; `passwords.Length` on alkioiden lukumäärä.

### Vaiheet

1. **.NET Fiddlessä**, `Main`:in sisällä, liitä ja aja:

   ```csharp
   string[] passwords = { "hi", "correcthorse", "12345", "battery", "longpassword" };
   for (int i = 0; i < passwords.Length; i++) {
       if (passwords[i].Length >= 8) {
           Console.WriteLine("long enough");
       } else {
           Console.WriteLine("too short");
       }
   }
   ```

2. **Ennusta tuloste ennen Run:n painamista.** Viisi riviä, yksi per salasana.
3. **Vertaa ennustusta todellisuuteen.** Jos jokin rivi yllätti sinut, etsi salasana, josta se tuli, ja selitä miksi.
4. **Kirjoita 3 lauseen reflektio** siitä, mitä ohjelma tekee ja yhdestä asiasta, jonka lisäisit seuraavaksi.

### Säilytä muistiinpanosi

Jos **AT3**-ohjelmasi käyttää `if/else`:ä ja olet valmis aikaisin, liitä tämä pätkä laajennuksena. Säilytä se AT3-kansiossa.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.4-CS — Lue oikea virheilmoitus ja korjaa se (C#)

**Tavoite.** Lue kolme oikeaa C#-kääntäjän tai ajonaikaista viestiä ja sovella yhtä pientä korjausta kuhunkin, jotta ensimmäinen yllätysvirhe AT3:ssa ei pysäytä sinua.

### Vaiheet

1. **Liitä kukin alla oleva pätkä .NET Fiddlen `Main`-metodiin, yksi kerrallaan.** Jokaisessa on täsmälleen yksi virhe.

   ```csharp
   // Pätkä A
   int score = 75;
   if (scre >= 50) {
       Console.WriteLine("you passed");
   }
   ```

   ```csharp
   // Pätkä B
   int age = 17
   if (age >= 18) {
       Console.WriteLine("adult");
   }
   ```

   ```csharp
   // Pätkä C
   for (int i = 0; i < 3; i++) {
       Console.WriteLine("Hello");
   
   ```

2. **Jokaisesta pätkästä**, kopioi täsmällinen kääntäjän viesti (alkaa `error CS…`). Nimeä rivi ja korjaus selkeällä suomella. Sovella korjaus ja aja uudelleen.
3. **Valinnainen LLM-sparraus-vaihe.** Liitä yksi virheilmoitus plus pätkä LLM:ään tällä kehotteella:

   ```text
   Selitä, mitä tämä C#-kääntäjän virhe tarkoittaa kertomatta, miten korjata se.
   Haluan löytää korjauksen itse.
   <liitä virheilmoitus + pätkä tähän>
   ```

   Jos LLM antaa korjauksen joka tapauksessa, **hylkää** vastaus ja kirjoita korjaus omin sanoin. Älä liitä LLM:n tulostetta sanatarkasti muistiinpanoihisi.

### Säilytä muistiinpanosi

Pieni kirjasto C#-virhekoodeja (CS0103, CS1002, …) nyt kirjoitettuna nopeuttaa sinua O24:n **AT3**-hetkellä, kun joudut lukemaan oikean kääntäjän viestin ja soveltamaan yhtä pientä korjausta.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.5-CS — Vertaile JS-luokkakaveriin

**Tavoite.** Lue luokkakaverin JavaScript-ohjelma ja kirjoita 3–5 lausetta eroista ja yhdestä asiasta, joka on sama.

### Vaiheet

1. **Etsi luokkakaveri**, joka käytti JavaScriptiä AT3:lle. Näyttäkää toisillenne ohjelmanne.
2. **Lue hänen ohjelmansa rivi riviltä.** Tunnista jokaisen JS-rivin C#-vastine.
3. **Kirjoita 3–5 lausetta** eroista (puolipisteet kaikkialla C#:ssa vs. valinnaiset JS:ssä, `Console.WriteLine` vs. `console.log`, `int` / `string` vs. `let`, isot metodien nimet C#:ssa) ja **yhdestä asiasta, joka on sama** (silmukkarakenne, `if/else`, tavoite).

### Jos teet tämän yksin

Jos JS-luokkakaveria ei ole saatavilla, lue JavaScript-versio yhdestä `self-study.md`:n työn ääressä olevista esimerkeistä (Ohjelmat A–E) ja kirjoita samat 3–5 lausetta verraten sitä saman sivun C#-versioon.

### Säilytä muistiinpanosi

Liitä 3–5 lausetta **AT3**-kansioosi. Ne eivät ole osa läpäisytarkistusta, mutta ne terävöittävät O24-esitystäsi: opiskelija, joka osaa nimetä yhden asian *toisesta* kielestä, ymmärtää oman valintansa paremmin.
