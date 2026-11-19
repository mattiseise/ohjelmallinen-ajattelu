# Viikko 7 — Oppitunti 21 lisämateriaali — Puhujamuistiinpanot

## Dia 1 — Viikko 7: Oppitunti 21 lisämateriaali

Avaa lyhyellä saatteella: "Tämä on lisämateriaali oppitunnille 21. Käymme yhden esimerkin — ikärajatarkistuksen — läpi kolmena versiona: pseudokoodi, JavaScript ja C#." Tarkoitus on hidas, askel kerrallaan etenevä siirtymä viikon 6 muodosta viikon 7 muotoon. Tämä dia on lyhyt — siirry nopeasti varsinaiseen sisältöön. Sano, että materiaali kannattaa katsoa tunnilla, mutta opiskelija voi myös palata siihen myöhemmin AT3:n yhteydessä. Noin 20 sek.

## Dia 2 — Oppitunti 21 — Ikärajatarkistus kolme kertaa

Esittele dian rakenne. Sama algoritmi kolmena versiona, yksi muunnos per dia. Pseudokoodi → JavaScript → C#. Tämä on tärkeä pedagoginen valinta: yhden esimerkin näkeminen kolmessa muodossa kerrallaan rakentaa intuitiota siitä, mikä on ajattelu (sama) ja mikä on syntaksi (eri). Sano: "Älkää opetelko ulkoa eri muotoja. Etsikää sama rakenne kaikista kolmesta." Tämä on tehokkain tapa oppia. Noin 1 min.

## Dia 3 — Viikon 6 pseudokoodi, jonka jo tunnemme

Käy pseudokoodi läpi rivi riviltä. READ age lukee iän. IF age >= 18 THEN tarkistaa ehdon. WRITE "Pääset sisään." tulostaa onnistuneen viestin. ELSE-haarassa WRITE-rivi tulostaa hylkäyksen. ENDIF sulkee rakenteen. Painota, että tämä rakenne on tuttu viikolta 6: testi, then-lohko, else-lohko. Vinkki kalvolla on tärkeä: rakenne on aina sama. Tämä on muoto, johon palaamme aina, kun katsomme if/else-rakennetta. Sano: "Tunnistakaa tämä muoto. Se toistuu tuhansia kertoja koodissa, jota luette myöhemmin." Noin 1,5 min.

## Dia 4 — Vaihe 1 — JavaScript rivi riviltä

Käy JavaScript-koodi läpi. let age = 16 luo muuttujan ja antaa sille arvon. if (age >= 18) { aloittaa if-lohkon. console.log("Pääset sisään."); on then-haaran tuloste. } else { aloittaa else-haaran. console.log("Valitettavasti..."); on else-haaran tuloste. } sulkee lohkon. Käy vastinparit pseudokoodista JavaScriptiin: READ age → let age = 16, IF...THEN → if(...){, WRITE → console.log, ENDIF → }. Sano: "Vasen sarake on pseudokoodi, oikea on JavaScript. Sama ajatus, eri muoto." Ajattele näin -ohje on hyödyllinen: let age = 16 korvaa pseudokoodin READ age, koska annamme testiarvon suoraan. Tämä on pieni mutta tärkeä huomio. Noin 2,5 min.

## Dia 5 — Vaihe 2 — C# rivi riviltä

Käy C#-koodi läpi. int age = 16; — kokonaisluku, joka saa arvon 16. if (age >= 18) — testi. Aaltosulje { aloittaa lohkon. Console.WriteLine("Pääset sisään."); tulostaa. } else { aloittaa else-lohkon. Vastinparit pseudokoodista C#:aan: READ age → int age = 16, IF...THEN → if(...){, WRITE → Console.WriteLine, ENDIF → }. Painota: ainoa ero JavaScriptiin on tyyppisana int ja tulostuskomennon nimi. Vinkki: C#:ssa int kertoo, että age on kokonaisluku. Tämä on C#:n tapa: tyyppi näkyy etukäteen. Sano: "Jos tämä tuntuu monimutkaisemmalta kuin JavaScript, ette ole väärässä — C# on hieman tarkempi. Mutta tarkkuus on myös etu, koska virheet näkyvät aikaisemmin." Noin 2,5 min.

## Dia 6 — Mikä on samaa kaikissa kolmessa?

Tämä on dia, jossa pedagoginen pointti kiteytyy. Käy lista läpi: rakenne (testi, then-lohko, else-lohko), vertailu >=, kaksi viestiä, rivien järjestys ylhäältä alas. Ajattelu ei muutu, kun siirryt pseudokoodista JavaScriptiin ja C#:aan. Sano: "Kun löydätte saman rakenteen, syntaksi tuntuu vähemmän vieraalta." Tämä on kurssin keskeinen oppimismenetelmä. Kysy: "Mikä on tärkein samanlaisuus?" Hyvä vastaus: rakenne — testi ja kaksi haaraa. Tämä rakenne on if/else koko ohjelmoinnin maailmassa. Noin 2 min.

## Dia 7 — Mikä on erilaista?

Käy erot läpi. Oikea koodi tarvitsee todellisen arvon: let age = 16 tai int age = 16, ei READ age. Tulostusfunktio: console.log vs. Console.WriteLine. C#:n tyyppisana int. Aaltosulkeet { } korvaavat THEN ja ENDIF. Painota: nämä ovat syntaksia. Erot ovat paikallisia. Ajattelu on yhteinen. Ajattele näin -ohje on hyödyllinen: älä opettele kaikkea uutena, etsi vastineet. Sano: "Jos joskus opettelette kolmannen kielen, etsikää samalla tavalla vastineet. Se on nopein tie." Tämä on ammattilaisen tapa oppia uusia kieliä. Noin 2 min.

## Dia 8 — Ennusta — suorita sitten

Tämä dia opettaa työtavan. Ennen kuin painat Run, ennusta tuloste arvolle age = 16. Kirjoita ylös. Suorita. Vertaa. Tuloste on "Valitettavasti et ole vielä tarpeeksi vanha." Vaihda age arvoksi 19. Ennusta uudelleen — nyt tuloste on "Pääset sisään." Suorita ja vertaa. Jos molemmat ennusteet täsmäsivät, olet juuri kuivaharjoitellut koodia. Sano: "Tämä on sama kuivaharjoittelu kuin viime viikolla. Vain muoto on uusi." Kysy: "Mitä tapahtuu, jos vaihdat arvoksi 18?" Vastaus: pääset sisään, koska >= 18 sisältää tasan 18. Tämä on hyvä reunaehto-keskustelu. Noin 2,5 min.

## Dia 9 — Siirtymä AT3:een

Tämä dia kytkee oppitunnin AT3:een. AT3 (viikko 8) pyytää ottamaan yhden viikon 6 pseudokoodisi, jossa on IF/ELSE, ja muuttamaan sen toimivaksi ohjelmaksi JavaScriptillä tai C#:lla. Näiden diojen läpikäynti on täsmälleen se muoto, jota AT3 odottaa. Painota: tallenna tämän päivän koodi. Se on ensi viikon palautuksen siemen. Vinkki: pieni toimiva esimerkki on parempi lähtökohta kuin iso keskeneräinen. Sano: "Älkää valitko viiden sivun pseudokoodia AT3:een. Valitkaa pieni, jossa on yksi ehto. Se riittää hyväksyttyyn." Tämä rauhoittaa stressaantuneita opiskelijoita. Noin 2 min.
