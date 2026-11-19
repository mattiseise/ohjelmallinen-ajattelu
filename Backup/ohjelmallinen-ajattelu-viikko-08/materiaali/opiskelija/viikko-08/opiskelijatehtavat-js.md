# Viikko 8 — Opiskelijatehtävät (JavaScript)

## Yleiskatsaus viikon tehtäviin

Tällä viikolla on **kaksi 🟢 PAKOLLISTA** ja **kolme 🟣 SYVENTÄVÄÄ** JavaScript-tehtävää. Pakolliset tehtävät ovat sinun **must-do minimum** — viimeistele molemmat läpäistäksesi AT3:n. Syventävät tehtävät ovat valinnaisia; valitse yksi tai kaksi, jos sinulla on aikaa.

**AT3 on tämän viikon keskeinen tuotos.** Tehtävä 8.1-JS *on* AT3-briiffaus. Palautat lähdekoodin, kuvakaappauksen ja lyhyen reflektion O23:n lopussa ja pidät **2 minuutin** suullisen esityksen O24:llä. Tehtävä 8.2-JS on pieni silmukan lämmittely ennen kuin käännät oman pseudokoodisi.

JS pyörii selaimesi DevTools-konsolissa (`Cmd + Opt + J` Macilla, `Ctrl + Shift + J` Win/Linuxilla). "Testaaminen" tarkoittaa ajamista kahdella eri arvolla; "virheenkorjaus" tarkoittaa konsolin virheen lukemista ja yhden rivin muuttamista.

---

## 🟢 PAKOLLINEN — Tehtävä 8.1-JS — AT3-briiffaus: käännä viikon 6 pseudokoodisi JavaScriptiin

**Tavoite.** Käännä yksi pala omaa viikon 6 pseudokoodiasi pieneksi, toimivaksi JavaScript-ohjelmaksi (noin 10–25 riviä), aja se selaimen konsolissa kahdella eri alkuarvolla, löydä ja korjaa yksi bugi ja valmistele **2 minuutin** suullinen esitys. Tämä on **AT3**.

**Tämä on viikon 8 must-do minimum.** Ilman tätä tehtävää ei ole AT3:a.

### Vaiheet

1. **Valitse yksi pala viikon 6 pseudokoodistasi** (6–20 riviä). Jos et löydä yhtä, käytä varamallia ja mukauta arvot: ikätarkistus; salasanan pituuden tarkistus; pisteet palautteeksi; yksinkertainen laskuri (1–5); tervehdys nimellä kolme kertaa.
2. **Käännä se rivi riviltä JavaScriptiin** käyttäen `self-study.md`:n käännöstaulukkoa. Käytä kovakoodattuja muuttuja-arvoja ylhäällä (ei `prompt()`:a tarvita). Esimerkki:

   ```js
   let password = "hi";
   if (password.length >= 8) {
     console.log("strong enough");
   } else {
     console.log("too short");
   }
   ```

3. **Avaa selaimen DevTools-konsoli**, liitä ohjelma, paina Enter, lue tuloste.
4. **Aja se kahdella eri alkuarvolla.** Vaihda yhtä muuttujaa ylhäällä ja aja kumpikin versio. Ota **kuvakaappaus**, jossa molemmat tulosteet näkyvät.
5. **Löydä ja korjaa yksi bugi.** Jos ohjelmasi pyöri ensimmäisellä yrityksellä, **laukaise** bugi tarkoituksella: kirjoita yhden muuttujan nimi tarkoituksella väärin tai poista yksi `;`. Aja, lue virheilmoitus, korjaa se takaisin. Nimeä bugi selkeällä suomella ("minulla oli `passwrd` `password`:n sijaan").
6. **Tallenna lähdekoodi** nimellä `at3.js` (tai liitä aidattuna ```js-lohkona palautusmuistiinpanoihisi).
7. **Kirjoita 3–5 lauseen reflektio**, jossa nimeät, mitä ohjelma tekee, sen yhden bugin, jonka löysit, ja sen yhden korjauksen, jonka teit.
8. **Valmistele 2 minuutin suullinen esityksesi** O24:lle. Neljä kohtaa, ~30 sekuntia kukin: **mitä** ohjelma tekee → **miten** se toimii (muuttujat, `if/else`, silmukka?) → **mikä** meni vikaan → **miten** korjasit sen. Harjoittele puhelimen ajastimella.

### Jos teet tämän yksin

O24:n esitys olettaa yleisön. Jos et pysty esittämään livenä — sairaus, hybridiosallistuminen — nauhoita **2 minuutin** video esittäen kameralle, *tai* julkaise ohjelma plus 3 lauseen tiivistelmä luokan chatissa. Neljä kohtaa ovat samat.

### Säilytä muistiinpanosi

Tämä **on** **AT3**. Tuo neljä artefaktia O24:lle: lähdekooditiedosto (`at3.js`), kuvakaappaus kahdesta ajosta, 3–5 lauseen reflektio, jossa nimeät bugin ja korjauksen, ja itsesi valmiina pitämään **2 minuutin** suullisen esityksen.

AT3 **palautetaan O23:n lopussa** ja **esitetään O24:llä**. Hyväksytty / ei-vielä-hyväksytty neljän tarkistuksen perusteella: ohjelma pyörii (tai epäonnistunut yrityksesi on dokumentoitu), osaat nimetä, mitä se tekee, yksi bugi-ja-korjaus-pari on kuvattu, **2 minuutin** esitys on pidetty.

---

## 🟢 PAKOLLINEN — Tehtävä 8.2-JS — Silmukan lämmittely: laske 1:stä 5:een JavaScriptillä

**Tavoite.** Kirjoita kolme lyhyttä `for`-silmukkaa JavaScriptillä — laske ylös, laske alas, tervehdi nimellä — jotta silmukkakuvio on sormissasi ennen AT3:a.

**Tämä on osa viikon 8 must-do minimumia.**

### Vaiheet

1. **Avaa selaimen konsoli.** Liitä ja aja:

   ```js
   for (let i = 1; i <= 5; i++) {
     console.log(i);
   }
   ```

   Odotettu tuloste: 1, 2, 3, 4, 5, yksi per rivi.
2. **Muokkaa se tulostamaan 5:stä alas 1:een.** Vaihda `i = 1` → `i = 5`, `i <= 5` → `i >= 1`, `i++` → `i--`. Aja.
3. **Muokkaa se tulostamaan "Hello, NAME" kolme kertaa.** Korvaa nimesi lainausmerkkien sisään:

   ```js
   for (let i = 0; i < 3; i++) {
     console.log("Hello, <oma nimesi>");
   }
   ```

4. **Tallenna kaikki kolme pätkää yhteen tiedostoon** (`loop-warmup.js`) yhden rivin kommentilla kunkin yläpuolella.

### Säilytä muistiinpanosi

Nämä kolme kuviota ovat täsmälleen ne silmukkamuodot, joita saatat tarvita **AT3**-ohjelmassasi. Säilytä `loop-warmup.js` samassa kansiossa kuin AT3-tiedostosi.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.3-JS — Yhdistä silmukka + if/else JavaScriptissä

**Tavoite.** Kirjoita pieni JS-ohjelma, joka silmukoi 5 salasanan listan läpi ja tulostaa "long enough" tai "too short" jokaiselle.

### Vaiheet

1. **Selaimen konsolissa**, liitä ja aja:

   ```js
   let passwords = ["hi", "correcthorse", "12345", "battery", "longpassword"];
   for (let i = 0; i < passwords.length; i++) {
     if (passwords[i].length >= 8) {
       console.log("long enough");
     } else {
       console.log("too short");
     }
   }
   ```

2. **Ennusta tuloste ennen Enter:n painamista.** Viisi riviä, yksi per salasana.
3. **Vertaa ennustusta todellisuuteen.** Jos jokin rivi yllätti sinut, etsi salasana, josta se tuli, ja selitä miksi.
4. **Kirjoita 3 lauseen reflektio** siitä, mitä ohjelma tekee ja yhdestä asiasta, jonka lisäisit seuraavaksi.

### Säilytä muistiinpanosi

Jos **AT3**-ohjelmasi käyttää `if/else`:ä ja olet valmis aikaisin, liitä tämä pätkä luonnollisena laajennuksena. Säilytä se AT3-kansiossa.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.4-JS — Lue oikea virheilmoitus ja korjaa se (JS)

**Tavoite.** Lue kolme oikeaa JavaScript-virheilmoitusta ja sovella yhtä pientä korjausta kuhunkin, jotta ensimmäinen yllätysvirhe AT3:ssa ei pysäytä sinua.

### Vaiheet

1. **Liitä kukin alla oleva pätkä selaimen konsoliin, yksi kerrallaan.** Jokaisessa on täsmälleen yksi virhe.

   ```js
   // Pätkä A
   let score = 75;
   if (scre >= 50) {
     console.log("you passed");
   }
   ```

   ```js
   // Pätkä B
   let age = 17;
   if (age = 18) {
     console.log("adult");
   }
   ```

   ```js
   // Pätkä C
   for (let i = 0; i < 3; i++) {
     console.log("Hello");
   
   ```

2. **Jokaisesta pätkästä**, kopioi täsmällinen virheilmoitus (Pätkä B tulostaa odottamattoman tulosteen — hiljainen bugi, ei virhe). Nimeä rivi ja korjaus selkeällä suomella. Sovella korjaus ja aja uudelleen.
3. **Valinnainen LLM-sparraus-vaihe.** Liitä yksi virheilmoitus plus pätkä LLM:ään tällä kehotteella:

   ```text
   Selitä, mitä tämä JavaScript-virhe tarkoittaa kertomatta, miten korjata se.
   Haluan löytää korjauksen itse.
   <liitä virheilmoitus + pätkä tähän>
   ```

   Jos LLM antaa korjauksen joka tapauksessa, **hylkää** vastaus ja kirjoita korjaus omin sanoin. Älä liitä LLM:n tulostetta sanatarkasti muistiinpanoihisi.

### Säilytä muistiinpanosi

Pieni kirjasto JS-virheitä nyt kirjoitettuna nopeuttaa sinua O24:n **AT3**-hetkellä, kun joudut lukemaan oikean virheilmoituksen ja soveltamaan yhtä pientä korjausta.

---

## 🟣 SYVENTÄVÄ — Tehtävä 8.5-JS — Vertaile C#-luokkakaveriin

**Tavoite.** Lue luokkakaverin C#-ohjelma ja kirjoita 3–5 lausetta eroista ja yhdestä asiasta, joka on sama.

### Vaiheet

1. **Etsi luokkakaveri**, joka käytti C#:ia AT3:lle. Näyttäkää toisillenne ohjelmanne.
2. **Lue hänen ohjelmansa rivi riviltä.** Tunnista jokaisen C#-rivin JS-vastine.
3. **Kirjoita 3–5 lausetta** eroista (puolipisteet, `Console.WriteLine` vs. `console.log`, `int` / `string` vs. `let`, isot metodien nimet C#:ssa) ja **yhdestä asiasta, joka on sama** (silmukkarakenne, `if/else`, tavoite).

### Jos teet tämän yksin

Jos C#-luokkakaveria ei ole saatavilla, lue C#-versio yhdestä `self-study.md`:n työn ääressä olevista esimerkeistä (Ohjelmat A–E) ja kirjoita samat 3–5 lausetta verraten sitä saman sivun JS-versioon.

### Säilytä muistiinpanosi

Liitä 3–5 lausetta **AT3**-kansioosi. Ne eivät ole osa läpäisytarkistusta, mutta ne terävöittävät O24-esitystäsi: opiskelija, joka osaa nimetä yhden asian *toisesta* kielestä, ymmärtää oman valintansa paremmin.
