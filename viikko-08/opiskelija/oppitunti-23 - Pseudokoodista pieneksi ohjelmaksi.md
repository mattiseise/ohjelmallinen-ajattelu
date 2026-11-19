# Oppitunti 23 — Pseudokoodista pieneksi ohjelmaksi

Rakennuspäivä. Mitään täysin uutta käsitettä ei enää tule. Käännät yhden oman viikon 6
pseudokoodinpätkäsi JavaScriptiksi tai C#:ksi rivi riviltä. Ajattelu on jo tehty. Työ on
enimmäkseen korvaamista: tämä pseudokoodirivi muuttuu tällaiseksi ohjelmakoodiksi.

### Valitse yksi viikon 6 pseudokoodinpätkä

Avaa viikon 6 muistiinpanosi. Valitse yksi pätkä — esimerkiksi ikärajatarkistus, salasanan
pituustarkistus, pistemäärästä palautteeseen -ratkaisu, laskuri tai tervehdys. Hyvä pituus on 6–
20 riviä. Jos suosikkipätkäsi on suurempi, ota siitä vain yksi selkeä osa, joka tekee yhden
tunnistettavan työn alusta loppuun.
Jos et löydä viikon 6 pseudokoodiasi tai hukutit sivun, voit käyttää yhtä näistä varapohjista ja
muokata arvoja itsellesi sopiviksi:
• Ikärajatarkistus. Aseta ikä. Jos ikä on vähintään 18, tulosta allowed, muuten not
allowed.
• Salasanan pituustarkistus. Aseta salasana. Jos se on vähintään 8 merkkiä pitkä,
tulosta strong enough, muuten too short.
• Pistemäärä palautteeksi. Aseta pistemäärä. Jos se on vähintään 80, tulosta great
work; jos vähintään 50, tulosta you passed; muuten try again.
• Yksinkertainen laskuri. Tulosta luvut 1–5 -silmukalla. `for`
• Nimellä tervehtiminen. Aseta nimi ja tulosta Hello, NAME kolme kertaa - `for`
silmukalla.

### Käännöstaulukko

Useimmilla pseudokoodiriveillä on selkeä vastine JavaScriptissä ja C#:ssa. Tämä pieni taulukko
tekee oppitunnista 23 lähes mekaanisen.
Pseudokoodin muoto JavaScript C#

```javascript
WRITE "Hello" console.log("Hello"); Console.WriteLine("Hello");
SET x TO 5 let x = 5; int x = 5;
SET name TO "Aino" let name = "Aino"; string name = "Aino";
IF x >= 18 THEN … ELSE … if (x >= 18) { … } else { … } if (x >= 18) { … } else { … }
REPEAT N TIMES for (let i = 0; i < N; i++) { … } for (int i = 0; i < N; i++) { … }
WHILE x < 3 DO … while (x < 3) { … } while (x < 3) { … }
```

tai tai

```
INCREASE x BY 1 x = x + 1; x++; x = x + 1; x++;
```

tai

```
IF x EQUALS 5 THEN … if (x === 5) { … } == if (x == 5) { … }
```

Tämä riittää kaiken viikon 6 pseudokoodin kääntämiseen. Rakenne oli jo olemassa. Taulukko
antaa sille vain oikeat pintasanat valitussa kielessä.

### Kaksi valmista esimerkkiä rinnakkain

Ikärajatarkistus. Viikon 6 pseudokoodi: aseta iäksi 17; jos ikä on vähintään 18, tulosta
allowed, muuten not allowed.
JavaScript

```javascript
let age = 17;
if (age >= 18) {
console.log("allowed");
} else {
console.log("not allowed");
}
```

C

```csharp
int age = 17;
if (age >= 18) {
Console.WriteLine("allowed");
} else {
Console.WriteLine("not allowed");
}
```

Molemmat tulostavat . Jos vaihdat arvon arvoksi , molemmat tulostavat `not allowed 17 19`
. `allowed`
Nimellä tervehtiminen (silmukka + muuttuja). Viikon 6 pseudokoodi: toista 3 kertaa —
tulosta Hello, name.
C

```csharp
string name = "Aino";
for (int i = 0; i < 3; i++) {
Console.WriteLine("Hello, " + name);
}
```

JavaScript

```javascript
let name = "Aino";
for (let i = 0; i < 3; i++) {
console.log("Hello, " + name);
}
```

Molemmat tulostavat kolme kertaa. yhdistää tekstin ja muuttujan arvon yhdeksi `Hello, Aino +`
tekstiksi. Tätä kutsutaan konkatenaatioksi.
Pieni tärkeä huomio virheitä ajatellen: merkkijonon pituus kirjoitetaan JavaScriptissä
(pieni ) mutta C#:ssa (iso ). Tämä on juuri sellainen yhden `name.length l name.Length L`
merkin ero, josta saatetaan saada virheilmoitus oppitunnilla 24.

### Tallenna, aja, katso tulos

JavaScript selaimen konsolissa: avaa mikä tahansa verkkosivu, paina (Mac) `Cmd + Opt + J`
tai (Windows/Linux), liitä koodisi, paina Enter ja katso tuloste. Tallenna sama `Ctrl + Shift + J`
koodi -tiedostoksi. Se on lähdekoodisi AT3:a varten. `.js`
C# verkossa: avaa , valitse Console, liitä koodisi -metodin sisään, paina `dotnetfiddle.net Main`
Run ja katso tuloste. Tallenna sama koodi -tiedostoksi. Se on lähdekoodisi AT3:a varten. `.cs`
Ota kuvakaappaus ajosta niin, että tuloste näkyy. Se on yksi AT3:n palautettavista osista.
Pysähdy hetkeksi: Katso ohjelmaasi ja lue se kerran rivi riviltä ääneen tavallisella
suomella. Jos osaat sanoa jokaisen rivin työn ilman käännöstaulukkoa, olet jo lähellä
sitä, että pystyt esittämään ohjelman kahdessa minuutissa.

### Kun ruutu jää tyhjäksi

Jos ajat ohjelman eikä mitään tapahdu, tarkista ensin tylsät syyt:
• painoitko oikeasti Run tai Enter?
• liititkö koko ohjelman vai vain osan siitä?
• onko tulostusrivillä kirjoitusvirhe? ( ei ole sama kuin , `console.Log console.log`
ei ole sama kuin ) `Console.Writeline Console.WriteLine`
• pysähtyikö ohjelma jo aiemmin virheilmoitukseen?
Jos mikään näistä ei auta, lisää ohjelman alkuun rivi tai

```javascript
console.log("got here");
```

. Jos tämä tulostuu, ohjelma ainakin käynnistyy ja ongelma on

```csharp
Console.WriteLine("got here");
```

alempana.
Pysähdy hetkeksi: Aseta viikon 6 pseudokoodisi ja valmis ohjelmakoodisi
vierekkäin. Ympyröi kohdat, jotka ovat kirjaimellisesti samoja: muuttujien nimet,
luvut, , vertailut. Jäljelle jäävä osa on syntaksia. Ympyröidyt kohdat ovat sitä `if`
ajattelua, jota olet harjoitellut viikosta 1 asti.
