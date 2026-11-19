# Oppitunti 21 — Iän rajoitus -tarkistus, kolmasti

Läpikäyntisetti O21:lle. Sama algoritmi pseudokoodissa, sitten JavaScriptissä, sitten C#:ssa. Yksi muunnos per kalvo.

---

## Viikon 6 pseudokoodi, jonka jo tunnemme

```pseudo
READ age
IF age >= 18 THEN
  WRITE "Pääset sisään."
ELSE
  WRITE "Olen pahoillani, et ole tarpeeksi vanha."
ENDIF
```

Ystävä osaa noudattaa tätä. Tietokone ei — pseudokoodi ei kuulu sen sanalistaan.

---

## Vaihe 1 — JavaScript, rivi riviltä

```javascript
let age = 16;
if (age >= 18) {
  console.log("Pääset sisään.");
} else {
  console.log("Olen pahoillani, et ole tarpeeksi vanha.");
}
```

`READ age` → `let age = 16;` (kovakoodaamme nyt).
`IF … THEN` → `if (…) {`.
`WRITE` → `console.log`.
`ENDIF` → `}`.

---

## Vaihe 2 — C#, rivi riviltä

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

`READ age` → `int age = 16;`.
`IF … THEN` → `if (…) {`.
`WRITE` → `Console.WriteLine`.
`ENDIF` → `}`.

---

## Mikä on samaa kaikissa kolmessa?

- Rakenne: *testi, then-lohko, else-lohko*.
- Vertailu `>=`.
- Kaksi viestiä.
- Rivien järjestys ylhäältä alas.

Ajattelu ei muutu siirryttäessä pseudokoodista JS:ään ja C#:aan.

---

## Mikä on erilaista?

- Oikea koodi tarvitsee todellisen arvon: `let age = 16` tai `int age = 16` `READ age`:n sijaan.
- Tulostusfunktio: `console.log(...)` vs `Console.WriteLine(...)`.
- Tyyppisana C#:ssa (`int`) — JavaScript päättelee tyypin.
- Aaltosulkeet `{ }` korvaavat `THEN … ELSE … ENDIF`:n.

Nämä ovat **syntaksia**. Erot ovat paikallisia. Ajattelu on jaettua.

---

## Ennusta — sitten aja

Ennen Run-painikkeen klikkaamista ennusta tuloste arvolla `age = 16`. Kirjoita se ylös. Sitten aja.

```text
Olen pahoillani, et ole tarpeeksi vanha.
```

Vaihda nyt `age` arvoon `19`. Ennusta uudelleen. Aja uudelleen. Tulosteen tulisi vaihtaa haaraa.

Jos molemmat ennustukset vastasivat todellisuutta, olet juuri käsiajanut koodia samalla tavalla kuin käsiajoit pseudokoodia viikolla 6.

---

## Luovutus AT3:lle

AT3 (viikko 8) pyytää sinua ottamaan **yhden** palan omaa viikon 6 pseudokoodiasi, jossa on `IF/ELSE`, ja muuttamaan sen ajettavaksi ohjelmaksi JavaScriptissä tai C#:ssa.

Näiden kalvojen läpikäynti on täsmälleen se muoto, jota AT3 odottaa.

Tallenna tämän päivän koodi — se on ensi viikon palautuksen siemen.
