# Viikko 8 — Silmukan sulkeminen

Ohjelmallinen ajattelu

1. vuoden ammatillisen ICT:n kurssi

Viimeinen viikko. Silmukat, ensimmäinen oikea ohjelmasi ja 2 minuutin esitys.

---

## Mitä tällä viikolla laskeutuu

- Oppitunti 22 — **silmukat koodissa**: `for` ja `while`, rinnakkain JavaScriptissä ja C#:ssa
- Oppitunti 23 — **rakennuspäivä**: käännä viikon 6 pseudokoodisi pieneksi toimivaksi ohjelmaksi
- Oppitunti 24 — **testaa, korjaa yksi bugi, esitä**: AT3 palautetaan ja esitetään luokassa

> *Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen JavaScriptiksi tai C#:ksi, ajat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi on lakannut olemasta mystinen asia.*

---

## Silmukat — muoto (JS ja C# rinnakkain)

#### JavaScript

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

#### C#

```csharp
for (int i = 1; i <= 5; i++) {
    Console.WriteLine(i);
}
```

Molemmat tulostavat 1, 2, 3, 4, 5. Sama työ — eri pintasanat.

---

## Laskuri, ehto, runko, päivitys

`for`-silmukalla on neljä nimettyä osaa:

- **Laskuri** — `i`, alkaa 1:stä
- **Ehto** — `i <= 5`, tarkistetaan ennen jokaista toistoa
- **Runko** — aaltosulkeinen lohko, pyörii kerran per toisto
- **Päivitys** — `i++`, muuttaa laskuria toistojen välissä

Lue ääneen: *"Laskuri 1:stä, kun 5 tai alle, tulosta laskuri, lisää yksi."*

---

## `while`-silmukka (JS ja C# rinnakkain)

#### JavaScript

```js
let count = 0;
while (count < 3) {
  console.log("Hello");
  count = count + 1;
}
```

#### C#

```csharp
int count = 0;
while (count < 3) {
    Console.WriteLine("Hello");
    count = count + 1;
}
```

Molemmat tulostavat `Hello` kolme kertaa. Käytä `while`:ä, kun "kunnes" on luonnollisempi kuin "toista N kertaa".

---

## Kun silmukka pyörii ikuisesti

Jos laskuri ei koskaan muutu, ehto ei koskaan muutu epätodeksi ja runko jatkaa pyörimistä.

- Selaimen konsoli — sivu jumiutuu; selain varoittaa, että skripti on hidas.
- .NET Fiddle — ajo katkeaa aikakatkaisun vuoksi muutaman sekunnin kuluttua.

**Korjaus**: varmista, että jokin rungon sisällä muuttaa arvoa, jota ehto testaa.

---

## Pseudokoodistasi ohjelmaksi

Oppitunti 23 on rakennuspäivä. Mitään uutta ei laskeudu.

Valitset yhden palan **viikon 6 pseudokoodistasi** (6–20 riviä). Käännät sen rivi riviltä taulukon avulla. Ajat sen. Tallennat tiedoston.

Ajattelu oli jo tehty viikolla 6. Tämän viikon työ on enimmäkseen korvaamista.

---

## Käännöstaulukko

| Pseudokoodi            | JavaScript                          | C#                                      |
|------------------------|-------------------------------------|-----------------------------------------|
| `WRITE "Hello"`        | `console.log("Hello");`             | `Console.WriteLine("Hello");`           |
| `SET x TO 5`           | `let x = 5;`                        | `int x = 5;`                            |
| `IF x >= 18 THEN …`    | `if (x >= 18) { … }`                | `if (x >= 18) { … }`                    |
| `REPEAT N TIMES`       | `for (let i = 0; i < N; i++) { … }` | `for (int i = 0; i < N; i++) { … }`     |
| `INCREASE x BY 1`      | `x = x + 1;`                        | `x = x + 1;`                            |

Tämä riittää kaikkeen, mitä kirjoitit viikolla 6.

---

## Silmukka + if/else — salasanan tarkistus (JS ja C# rinnakkain)

#### JavaScript

```js
let passwords = ["hi", "correcthorse", "12345678"];
for (let i = 0; i < 3; i++) {
  if (passwords[i].length >= 8) {
    console.log("long enough");
  } else {
    console.log("too short");
  }
}
```

#### C#

```csharp
string[] passwords = { "hi", "correcthorse", "12345678" };
for (int i = 0; i < 3; i++) {
    if (passwords[i].Length >= 8) {
        Console.WriteLine("long enough");
    } else {
        Console.WriteLine("too short");
    }
}
```

Rakenne (silmukka, ehto, haara) on identtinen. Pintasanat eroavat.

---

## Tallenna, aja, näe tuloste

**JavaScript** — selaimen DevTools-konsolissa:

- `Cmd + Opt + J` (Mac) tai `Ctrl + Shift + J` (Win/Linux)
- Liitä, paina Enter, lue tuloste
- Tallenna koodi `.js`-tiedostona

**C#** — online-.NET-ajurissa:

- Avaa `dotnetfiddle.net`, valitse **Console**
- Liitä `Main`-metodiin, paina **Run**
- Tallenna koodi `.cs`-tiedostona

Ota kuvakaappaus ajosta.

---

## Oikean virheilmoituksen lukeminen (JavaScript)

```text
Uncaught ReferenceError: scre is not defined
    at <anonymous>:3:15
```

Selkeällä suomella: *"En tiedä, mikä `scre` on."*

Syy: jossain ylempänä määrittelit `score`-muuttujan, sitten myöhemmin kirjoitit `scre` (puuttuva `o`).

Korjaus: etsi `scre`, kirjoita puuttuva `o`, aja uudelleen.

---

## Oikean virheilmoituksen lukeminen (C#)

```text
error CS0103: The name 'scre' does not exist in the current context
```

Sama bugi, sama korjaus. C# kieltäytyy kääntämästä, kunnes korjaat kirjoitusasun.

Toinen yleinen C#-virhe:

```text
error CS1002: ; expected
```

Puuttuva puolipiste. Viesti nimeää rivin. Lisää `;`, aja uudelleen.

---

## Yksi pieni korjaus, yksi uusi ajo

Tätä "virheenkorjaus" tarkoittaa tällä kurssilla.

- Ei debuggerityökalua.
- Ei pysäytä-ohjelma-rivi-riviltä -työkalua.
- Ei testauskehystä.

**Lue viesti → etsi rivi → muuta yksi pieni asia → aja uudelleen.**

Teet tämän vähintään kerran AT3:ta varten.

---

## 2 minuutin esityksesi

Neljä kohtaa, noin 30 sekuntia kukin:

1. **Mitä** ohjelma tekee (selkeällä suomella).
2. **Miten** se tekee sen (muuttujat, `if/else`, silmukka).
3. **Mikä meni vikaan** (se yksi bugi, nimeltä).
4. **Miten korjasit sen** (se yksi rivi, jonka muutit).

Ajasta puhelimella. Kaksi minuuttia on lyhyt — pyri alittamaan, ei ylittämään.

---

## Must-do minimum vs. syventävä

**Must-do minimum** — jokainen opiskelija lähtee viikolta 8 mukanaan:

- Pieni ohjelma, käännetty omasta viikon 6 pseudokoodistaan
- Kaksi ajoa, kaksi tulostetta, yksi bugi löydetty ja korjattu
- 2 minuutin suullinen esitys luokassa

**Syventävä (valinnainen):**

- Yhdistä silmukka `if/elseen`
- Vertaa ohjelmaasi luokkakaverin toisen kielen versioon
- Lisää syöte funktiosta `prompt()` tai `Console.ReadLine()`

---

## Tämän viikon tehtävät (katso oman kielesi tehtävätiedostosta)

- **Tehtävä 8.1** *(PAKOLLINEN)* — AT3-briiffaus: käännä viikon 6 pseudokoodisi (tiedostossa `student-tasks-js.md` tai `student-tasks-csharp.md`)
- **Tehtävä 8.2** *(PAKOLLINEN)* — Silmukan lämmittely: laske 1:stä 5:een
- **Tehtävä 8.3** *(SYVENTÄVÄ)* — Silmukka + if/else salasanan tarkistus
- **Tehtävä 8.4** *(SYVENTÄVÄ)* — Lue oikea virheilmoitus ja korjaa se
- **Tehtävä 8.5** *(SYVENTÄVÄ)* — Vertaile luokkakaveriin, joka käyttää toista kieltä

---

## Miten AT3 arvioidaan

Hyväksytty / ei-vielä-hyväksytty neljän tarkistuksen perusteella:

- Ohjelma **pyörii** (tai on dokumentoitu yritys virheineen).
- Osaat **nimetä** selkeällä suomella, mitä ohjelma tekee.
- Yksi **bugi-ja-korjaus-pari** on dokumentoitu reflektiossasi.
- **2 minuutin** esitys on pidetty oppitunnilla 24.

Ei numeroarvosanaa. Ei muuta matriisia kuin tämä tarkistuslista.

---

## Silmukan sulkeminen — viikko 1, vielä kerran

Kurssi avautui yhdellä kysymyksellä:

> **Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?**

Olet vastannut siihen. Ei teoriassa — toimivan ohjelman kanssa kädessäsi.

Ohjelmointi on lakannut olemasta mystinen asia.

---

## Kiitos ja mitä seuraavaksi

Tämä oli Ohjelmallinen ajattelu — perusta, jonka päällä teet ohjelmointia loppuopintojesi ajan.

Säilytä AT3-lähdetiedostosi. Lue se uudelleen puolen vuoden kuluttua. Se näyttää pieneltä. Se on pointti — sinä kirjoitit sen.

Tervetuloa keskeisen kysymyksen toiselle puolelle.
