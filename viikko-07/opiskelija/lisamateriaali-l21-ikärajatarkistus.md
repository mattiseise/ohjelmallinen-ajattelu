# Viikko 7 — Oppitunti 21 lisämateriaali

---

## Oppitunti 21 - Ikärajatarkistus kolme kertaa

Ohjelmallinen ajattelu
Läpikäyntidiasto oppitunnille 21. Sama algoritmi pseudokoodina, sitten JavaScriptinä, sitten C#:na. Yksi muunnos per dia.

---

## Viikon 6 pseudokoodi, jonka jo tunnemme

```pseudocode
READ age
IF age >= 18 THEN
WRITE "Pääset sisään."
ELSE
WRITE "Valitettavasti et ole vielä tarpeeksi vanha."
ENDIF
```

### Vinkki: rakenne on testi → then-lohko → else-lohko. ---

## Vaihe 1 - JavaScript rivi riviltä

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
} else {
  console.log("Valitettavasti et ole vielä tarpeeksi vanha.");
}
```

Vastinparit pseudokoodista JavaScriptiin:

- `READ age` → `let age = 16;` (kovakoodattu testiarvo toistaiseksi).
- `IF … THEN` → `if (…) {`.
- `WRITE` → `console.log`.
- `ENDIF` → `}`.

### Ajattele näin: `let age = 16` korvaa pseudokoodin `READ age` tässä esimerkissä, koska annamme testiarvon suoraan. ---

## Vaihe 2 - C# rivi riviltä

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("Pääset sisään.");
}
else
{
    Console.WriteLine("Valitettavasti et ole vielä tarpeeksi vanha.");
}
```

Vastinparit pseudokoodista C#:aan:

- `READ age` → `int age = 16;`.
- `IF … THEN` → `if (…) {`.
- `WRITE` → `Console.WriteLine`.
- `ENDIF` → `}`.

### Vinkki: C#:ssa `int` kertoo, että `age` on kokonaisluku. ---

## Mikä on samaa kaikissa kolmessa?

• Rakenne: *testi, then-lohko, else-lohko*.
• Vertailu `>=`.
• Kaksi viestiä.
• Rivien järjestys ylhäältä alas.
• Ajattelu ei muutu, kun siirryt pseudokoodista JavaScriptiin ja C#:aan.

### Vinkki: kun löydät saman rakenteen, syntaksi tuntuu vähemmän vieraalta. ---

## Mikä on erilaista?

• Oikea koodi tarvitsee todellisen arvon: `let age = 16` tai `int age = 16` sen sijaan, että lukisi
`READ age`.
• Tulostusfunktio: `console.log(...)` vs. `Console.WriteLine(...)`.
• C#:n tyyppisana (`int`) - JavaScript päättelee tyypin itse.
• Aaltosulkeet `{ }` korvaavat `THEN … ELSE … ENDIF` -rakenteen.
• Nämä ovat syntaksia. Erot ovat paikallisia. Ajattelu on yhteinen.

### Ajattele näin: älä opettele kaikkea uutena, vaan etsi vastineet. ---

## Ennusta - suorita sitten

Ennen kuin painat Run, ennusta tuloste arvolle `age = 16`. Kirjoita se ylös. Suorita sitten.

```
Valitettavasti et ole vielä tarpeeksi vanha.
```

Vaihda nyt `age` arvoksi `19`. Ennusta uudelleen. Suorita uudelleen. Tulosteen pitäisi vaihtaa
haaraa.
Jos molemmat ennusteet vastasivat todellisuutta, olet juuri kuivaharjoitellut koodia samalla
tavalla kuin pseudokoodia viikolla 6. ---

## Siirtymä AT3:een

AT3 (viikko 8) pyytää sinua ottamaan yhden oman viikon 6 pseudokoodin pätkän, jossa on
`IF/ELSE`, ja muuttamaan sen toimivaksi ohjelmaksi JavaScriptillä tai C#:lla.
Näiden diojen läpikäynti on täsmälleen se muoto, jota AT3 odottaa.
Tallenna tämän päivän koodi - se on ensi viikon palautuksen siemen.

### Vinkki: pieni toimiva esimerkki on parempi lähtökohta kuin iso keskeneräinen.
