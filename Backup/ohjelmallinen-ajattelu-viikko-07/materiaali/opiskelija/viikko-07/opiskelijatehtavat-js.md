# Viikko 7 — Opiskelijatehtävät (JavaScript)

## Yleiskatsaus tämän viikon JavaScript-tehtäviin

Tällä viikolla on **neljä tehtävää JavaScript-makuna**. Vihreäpiste-tehtävä (🟢 PAKOLLINEN) on **must-do-minimi** — tee se pysyäksesi luokan tahdissa. Kolme violettipiste-tehtävää (🟣 SYVENTÄVÄ) ovat valinnaisia laajennuksia; valitse yksi tai kaksi, jos sinulla on aikaa.

Kaikki, mitä kirjoitat tällä viikolla, on raaka-ainetta **AT3:lle, joka saapuu viikon 8 lopussa**. AT3 pyytää kääntämään palan omaa viikon 6 pseudokoodiasi pieneksi ohjelmaksi sillä kielellä, jonka valitset tällä viikolla. Tallenna koodisi.

IDE-asennusta ei vaadita. JavaScript ajetaan selaimesi DevTools-konsolissa. Testiframeworkkia ei ole tällä viikolla; ajat koodin, luet tulosteen, vertaat sitä siihen, mitä ennustit.

### Miten avaat JavaScript-konsolin

- **Mac**: `Cmd + Opt + J` missä tahansa selaimessa.
- **Windows / Linux**: `Ctrl + Shift + J` missä tahansa selaimessa.
- **Tai**: hiiren oikea klikkaus missä tahansa sivulla, valitse **Tarkasta**, klikkaa sitten **Konsoli**-välilehteä.

Liimaa rivi, paina Enter, lue mitä ilmestyy.

---

## 🟢 PAKOLLINEN — Ensimmäinen konsoliohjelmasi (JS)

**Tavoite:** Aja ensimmäinen JavaScript-ohjelma selaimesi konsolissa, joka tulostaa tervehdyksen, esittelee muuttujan ja tekee pienen laskutoimituksen. Tämä on viikon 7 must-do-minimi JavaScript-polulla.

Kuvakaappaus, jonka tallennat tämän tehtävän lopussa, on täsmälleen sen kaltainen artefakti, jota AT3 käyttää uudelleen ensi viikolla.

### Vaiheet

1. **Avaa konsoli** missä tahansa selaimessa (resepti yllä).
2. **Tulosta tervehdys oikealla nimelläsi.** Kirjoita alla oleva rivi käyttäen **omaa nimeäsi** lainausmerkeissä ja paina sitten Enter:

   ```javascript
   console.log("Hei, <oma nimesi>");
   ```

   Jos mitään ei ilmesty, tarkista lainausmerkit ja piste `console.log`:ssa.
3. **Esittele muuttuja iällesi ja tulosta se.** Vaihda `<oma ikäsi>` omaksi numeroksesi:

   ```javascript
   let age = <oma ikäsi>;
   console.log(age);
   ```

4. **Laske vuosia täysi-ikäisyyteen ja tulosta se.** Samassa konsoli-istunnossa:

   ```javascript
   let yearsToAdulthood = 18 - age;
   console.log(yearsToAdulthood);
   ```

   Jos olet jo 18 tai vanhempi, luku on nolla tai negatiivinen — se on oikein.
5. **Ota kuvakaappaus** konsolista, joka näyttää kaikki kolme tulostetta järjestyksessä. Liimaa se viikko 7:n muistiinpanotiedostoosi.
6. **Kirjoita 2–3 lauseen reflektio.** Yksi asia, joka yllätti sinut; yksi asia, joka toimi täsmälleen kuten ennustit.

### Pidä muistiinpanot

Pidä kuvakaappaus, kolme riviä koodia ja reflektiosi yhdessä kansiossa. **AT3 saapuu viikon 8 lopussa** ja pyytää pientä ohjelmaa tällä täsmälleen muodolla — muuttuja, laskutoimitus, tuloste. Tämän koodin uudelleenkäyttöä AT3:ssa kannustetaan.

---

## 🟣 SYVENTÄVÄ — Ensimmäinen if/else (JS)

**Tavoite:** Kirjoita 6-rivinen JavaScript-ohjelma, joka käyttää `if/else`-rakennetta tulostaakseen toisen kahdesta viestistä muuttujan arvon mukaan. O21-itseopiskelun ohjelma omissa käsissäsi.

### Vaiheet

1. **Liimaa konsoliin** alla oleva ohjelma:

   ```javascript
   let age = 16;
   if (age >= 18) {
     console.log("Pääset sisään.");
   } else {
     console.log("Olen pahoillani, et ole tarpeeksi vanha.");
   }
   ```

2. **Ennusta ennen ajamista.** Kun `age = 16`, mitä odotat konsolin tulostavan? Kirjoita se ylös **ennen** Enter-painikkeen painamista.
3. **Aja se.** Vertaa ennustusta todellisuuteen.
4. **Vaihda iäksi 19 ja aja uudelleen.** Ennusta ensin uudelleen. Tulosteen tulisi vaihtaa haaraa.
5. **Ota kuvakaappaus molemmista ajoista.** Tallenna ne ennustusmuistiinpanojesi viereen.

### Jos teet tämän yksin

Tämä tehtävä ei oleta paria. Jos haluat toiset silmäparit, käytä **24 tunnin taukoa**: ennusta tuloste tänään, aja ohjelma huomenna ilman, että luet ennustuksesi uudelleen.

### Pidä muistiinpanot

Pidä ohjelma, molemmat ennustukset, molemmat kuvakaappaukset. **AT3 saapuu viikon 8 lopussa** ja pyytää pientä `if/else`-ohjelmaa tällä täsmälleen muodolla. Tämä tehtävä on AT3:n kenraaliharjoitus.

---

## 🟣 SYVENTÄVÄ — Käännä viikon 6 pseudokoodisi (JS)

**Tavoite:** Ota yksi pala omaa viikon 6 pseudokoodiasi, jossa on `IF/ELSE`, ja muuta se pieneksi JavaScript-ohjelmaksi, joka ajaa konsolissa.

Tämä on tiedoston AT3-muotoisin tehtävä. Sen tekeminen nyt tarkoittaa, että AT3 on puoliksi kirjoitettu ennen julkaisua.

### Vaiheet

1. **Valitse yksi pala viikon 6 pseudokoodiasi**, jossa on `IF` (tai `IF/ELSE`). Itse kirjoittamasi on paras.
2. **Kopioi pseudokoodi** muistiinpanotiedostoosi.
3. **Käännä se JavaScriptiksi rivi riviltä**:
   - `READ <jokin>` → `let <jokin> = <valitsemasi arvo>;` toistaiseksi.
   - `IF … THEN` → `if (…) {`.
   - `ELSE` → `} else {`.
   - `WRITE "…"` → `console.log("…");`.
   - `ENDIF` → `}`.
4. **Liimaa JavaScript konsoliin** ja aja se. Lue mahdolliset virheilmoitukset — tulkki yleensä osoittaa suoraan riville.
5. **Tallenna pseudokoodi ja JavaScript rinta rinnan** muistiinpanoissasi. Tämä on täsmälleen se artefakti, jota AT3 pyytää.

### Pidä muistiinpanot

Pidä pseudokoodi ja JS rinta rinnan. **AT3 saapuu viikon 8 lopussa** ja käyttää tätä artefaktia suoraan uudelleen.

---

## 🟣 SYVENTÄVÄ — Riko se tarkoituksella (JS)

**Tavoite:** Tuo tarkoituksella yksi virhe kerrallaan toimivaan ohjelmaasi ensimmäisestä if/else-tehtävästä ja lue täsmällinen virheilmoitus, jonka JavaScript-moottori tulostaa.

Pointti on lukea **oikeita** virheilmoituksia, jotta ensimmäinen yllätysvirhe AT3:ssa ei pysäytä sinua.

### Vaiheet

1. **Aloita toimivasta `if/else`-ohjelmasta** *Ensimmäinen if/else (JS)* -tehtävästä. Varmista, että se yhä ajaa puhtaasti.
2. **Riko se kolmella tavalla, yksi kerrallaan**, ja kopioi täsmällinen virheilmoitus, jonka konsoli tulostaa:
   - **Unohda lainausmerkki.** Muuta `"Pääset sisään."` muotoon `"Pääset sisään.` (ei sulkevaa lainausmerkkiä).
   - **Unohda sulkeva aaltosulje.** Poista viimeinen `}`.
   - **Kirjoita tulostusfunktio väärin.** Muuta `console.log` muotoon `consle.log`.
3. **Korjaa kukin** ennen seuraavan esittelyä.
4. **Reflektio (2–3 lausetta):** mikä virheilmoitus oli selkein? Mikä oli sekava? Osoittiko jokin niistä väärälle riville?

### Jos teet tämän yksin

Tämä tehtävä ei oleta paria — konsoli on sparrauskumppanisi. Jos haluat toisen mielipiteen, lähetä yksi virheilmoitus luokan chattiin: *"Onko kukaan muu nähnyt tätä JS:ssä?"*

### Pidä muistiinpanot

Pidä kolme rikkinäistä riviäsi ja kolme täsmällistä virheilmoitusta. **AT3 saapuu viikon 8 lopussa** ja sisältää vähintään yhden virheilmoituksen, jota et ole ennen nähnyt — pieni JS-virheiden kirjasto kirjoitettuna nyt nopeuttaa sinut tuon hetken läpi.
