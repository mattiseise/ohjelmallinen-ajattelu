# Viikko 8 — Puhujamuistiinpanot (paadiat)

## Dia 1 — Viikko 8: Silmukka sulkeutuu

Avaa kurssin viimeinen viikko juhlavalla mutta rauhallisella tavalla. Sano: "Tervetuloa kurssin viimeiselle viikolle. Otsikko on tarkoituksellinen — silmukka sulkeutuu kahdessa merkityksessä." Toinen: opetellaan silmukkarakenne koodissa. Toinen: kurssin kaari sulkeutuu, kun pseudokoodi muuttuu toimivaksi ohjelmaksi. Kerro, että AT3 on viikon huipennus ja palautetaan oppitunnilla 24. Älä rakenna turhaa jännitystä — AT3 on pieni tehtävä, joka rakentuu jo tehtyyn työhön. Noin 1 min.

## Dia 2 — Mitä tällä viikolla tapahtuu

Käy viikon kolme oppituntia läpi: 22 silmukat koodissa rinnakkain, 23 rakentamispäivä (käännä viikon 6 pseudokoodisi), 24 testaa-korjaa-esitä-AT3. Lue myös pidempi lainaus dialta ääneen: "Kurssi sulkee silmukan: otat itse viikolla 6 kirjoittamasi pseudokoodin, käännät sen JavaScriptiksi tai C#:ksi, suoritat sen, löydät yhden bugin, korjaat sen ja selität, miten se toimii. Ohjelmointi ei ole enää mystistä." Painota viimeistä lausetta. Sano: "Tämä on kurssin lupaus. Tällä viikolla todistamme sen." Noin 2 min.

## Dia 3 — Silmukat — muoto (JS ja C# rinnakkain)

Esittele for-silmukka rinnakkain. JavaScript: for (let i = 1; i <= 5; i++) { console.log(i); }. C#: for (int i = 1; i <= 5; i++) { Console.WriteLine(i); }. Painota: sulkujen sisältö on identtinen (paitsi let vs. int). Lue molemmat. Vinkki: molemmat tulostavat luvut 1, 2, 3, 4 ja 5. Kysy: "Mikä on pienin muutos JavaScriptin ja C#:n välillä tässä?" Vastaus: let vs. int ja console.log vs. Console.WriteLine. Loppu on sama. Tämä on viikon perusrakenne. Noin 2,5 min.

## Dia 4 — Laskuri, ehto, runko, päivitys

Käy for-silmukan neljä osaa läpi. Laskuri i, alkaa arvosta 1. Ehto i <= 5, tarkistetaan ennen jokaista toistoa. Runko on aaltosulkeiden sisältö, suoritetaan kerran per toisto. Päivitys i++, muuttaa laskuria toistojen välissä. Lue ääneen: "Laskuri alkaa yhdestä; niin kauan kuin se on 5 tai alle, tulosta laskuri ja lisää yksi." Tämä on hyvä mantra. Ajattele näin -ohje on tärkeä: silmukka on toisto, jossa pysäytysehto on kirjoitettu näkyviin. Tämä on viikon 5 oppi (pysäytysehto on turvavyö) koodina. Noin 2,5 min.

## Dia 5 — while-silmukka (JS ja C# rinnakkain)

Esittele while-silmukka rinnakkain. JavaScript: let count = 0; while (count < 3) { console.log("Hei"); count = count + 1; }. C# vastaava. Painota ero for-silmukkaan: while testaa ehdon ennen jokaista kierrosta, mutta laskurin pitää muuttua rungossa, ei automaattisesti. Sano: "while on yleisempi — käytetään, kun et tiedä etukäteen, kuinka monta kertaa silmukka toistuu." Esimerkki: lue tiedoston rivit, kunnes loppu. Vinkki: while tarkistaa ehdon ennen jokaista kierrosta. Tämä on tärkeä ero for-silmukkaan, joka usein tietää listan koon etukäteen. Noin 2,5 min.

## Dia 6 — Kun silmukka pyörii ikuisesti

Tämä on tärkeä turvallisuusopetus. Jos laskuri ei muutu, ehto ei muutu, silmukka jatkaa ikuisesti. Selaimen konsolissa sivu jumittuu — selain varoittaa skriptin hitaudesta. .NET Fiddle aikakatkeaa muutamassa sekunnissa. Korjaus: varmista, että jokin rungon sisällä muuttaa arvoa, jota ehto testaa. Esimerkki: jos count = count + 1 puuttuu, count < 3 pysyy totena ikuisesti. Sano: "Tämä on viikon 5 turvavyö-opetus koodina. Pysäytysehdon pitää oikeasti pysäyttää." Kysy luokalta: "Mitä tapahtuu, jos koneella pyörii ikuinen silmukka?" Vastauksia: CPU 100 %, kone hidastuu, tuuletin lähtee käyntiin. Noin 2 min.

## Dia 7 — Omasta pseudokoodista omaksi ohjelmaksi

Tämä on oppitunnin 23 esittely. Rakentamispäivä. Mitään uutta ei tule. Valitset yhden osan viikon 6 pseudokoodistasi (6–20 riviä). Käännät rivi riviltä taulukon avulla. Suoritat. Tallennat tiedoston. Painota: ajattelu oli tehty jo viikolla 6. Tällä viikolla työ on enimmäkseen muodon vaihtamista. Tämä on rauhoittava viesti — opiskelija ei aloita tyhjästä. Tee näin -ohje on tärkeä: käännä ensin vain pieni toimiva osa. Laajenna sen jälkeen. Sano: "Tämä on yleinen ohjelmointitapa — aloita pienestä, laajenna." Tämä on viisas käytäntö myös ammattityössä. Noin 2 min.

## Dia 8 — Käännöstaulukko

Tämä on viikon ehkä hyödyllisin yksittäinen dia. Käy käännöstaulukko läpi. Pseudokoodi → JavaScript → C#. WRITE → console.log → Console.WriteLine. SET x TO 5 → let x = 5 → int x = 5. IF x >= 18 THEN → if (x >= 18) {...} → samoin C#:ssa. REPEAT N TIMES → for-silmukka. WHILE test DO → while (test) {...}. Painota: tämä taulukko on AT3:n tukipyörä. Vinkki: älä käännä ajatusta uudelleen alusta. Etsi vastaava muoto. Sano: "Pitäkää tämä dia auki, kun teette AT3:a. Se on huijauslehti, jota kannattaa käyttää." Noin 2,5 min.

## Dia 9 — Silmukka + if/else — salasanatarkistus (JS ja C# rinnakkain)

Käy esimerkki läpi. JavaScript: lista salasanoja, for-silmukka käy läpi, if tarkistaa pituuden, tulostaa "tarpeeksi pitkä" tai "liian lyhyt". C# vastaava. Painota: tämä yhdistää viikon 5 kaikki kolme rakennetta (järjestys, ehto, toisto) yhdessä koodinpätkässä. Sano: "Tämä on kompleksisin koodi, jonka olette nähnyt kurssilla. Käykää se läpi rivi riviltä." Lue läpi rauhallisesti. Kysy: "Mikä tulosteet tulisivat?" Vastauksia: "hi" → liian lyhyt, "correcthorse" → tarpeeksi pitkä, "12345678" → tarpeeksi pitkä (tasan 8). Vinkki: rakenne on sama, vain pintasanat eroavat. Noin 3 min.

## Dia 10 — Tallenna, suorita, katso tuloste

Käy käytännön ohjeet läpi. JavaScript: selaimen DevTools-konsoli (Cmd+Opt+J / Ctrl+Shift+J), liitä, paina Enter, lue tuloste. Tallenna .js-tiedostona. C#: dotnetfiddle.net, Console-tila, liitä Main-metodiin, paina Run. Tallenna .cs-tiedostona. Ota kuvakaappaus ajosta. Tee näin -ohje on tärkeä: nimeä tiedosto niin, että tunnistat version, esimerkiksi at3-v1.js. Painota: kuvakaappaus on AT3:n vaatimus. Se todistaa, että ohjelma todella pyöri. Sano: "Tallentakaa ja kuvakaappaakaa heti, kun ohjelma toimii. Älkää luottako siihen, että se toimii ensi viikolla." Noin 2 min.

## Dia 11 — Oikean virheilmoituksen lukeminen (JavaScript)

Käy virheilmoitus läpi. Uncaught ReferenceError: scre is not defined at <anonymous>:3:15. Yleiskielellä: "En tiedä, mikä scre on." Selitä, että ylempänä määriteltiin score, mutta myöhemmin kirjoitettiin scre — o puuttuu. Korjaus: etsi scre, kirjoita puuttuva o, suorita uudelleen. Vinkki: virheilmoituksen rivinumero on ensimmäinen paikka katsoa. Sano: "Virheilmoitus näyttää pelottavalta, mutta se on itse asiassa apuviesti. Se kertoo missä ja mikä on vialla." Kysy: "Mikä numero 3 tarkoittaa rivissä '<anonymous>:3:15'?" Vastaus: rivin numero. 15 on sarake. Tämä on debuggauksen perustaito. Noin 2,5 min.

## Dia 12 — Oikean virheilmoituksen lukeminen (C#)

Sama bugi C#:ssa. error CS0103: The name 'scre' does not exist in the current context. Sama korjaus: lisää puuttuva o. C# ei suostu kääntymään ennen kuin korjaat. Mainitse toinen yleinen virhe: CS1002: ; expected — puolipiste puuttuu. Vinkki: C# on tarkka puolipisteistä. Jos näet CS1002, katso rivin loppua. Sano: "C#:n virheilmoitukset ovat hieman teknisempiä kuin JavaScriptin, mutta saman tarkoituksen ne palvelevat: kerroaan, mikä on vialla." Sama bugi, sama korjaus eri kielissä. Tämä on hyvä esimerkki kielten yhteneväisyydestä. Noin 2 min.

## Dia 13 — Yksi pieni korjaus, yksi uusi ajo

Tämä dia määrittelee debuggauksen tällä kurssilla. Ei debugger-työkalua, ei rivi-kerrallaan-suoritusta, ei testauskehystä. Vain: lue viesti → etsi rivi → muuta yksi pieni asia → suorita uudelleen. Painota: tämä on AT3:n yksi pakollinen kohta. Jokaisen pitää tehdä vähintään yksi bugi-korjaus-pari. Ajattele näin -ohje on tärkeä: hyvä korjaus on pieni ja testattava. Älä muokkaa viittä riviä yhtä aikaa — silloin et tiedä mikä korjasi. Sano: "Tämä on ammattimaisin tapa korjata bugeja: pieniä muutoksia, testaa jokainen erikseen." Noin 2 min.

## Dia 14 — Kahden minuutin esityksesi

Esittele AT3:n esitysosa. Neljä kohtaa, noin 30 sekuntia kukin. Mitä ohjelma tekee yleiskielellä. Miten se tekee sen (muuttujat, if/else, silmukka). Mikä meni pieleen — yksi bugi nimeltä. Miten korjasit sen — se yksi rivi. Ajoita puhelimella. Kaksi minuuttia on lyhyt — tähtää mieluummin alle kuin yli. Painota: tämä ei ole pitkä puhe. Lyhyt ja konkreettinen riittää. Vinkki: harjoittele kerran ääneen. Sano: "Kun puhutte ääneen ensimmäisen kerran, huomaatte mitkä kohdat tarvitsevat vielä työtä." Lisämateriaali oppitunnilla 24 syventää tämän. Noin 2 min.

## Dia 15 — Pakollinen vähimmäistaso vs. syventäminen

Käy taso-erottelu läpi. Pakollinen vähimmäistaso jokaiselle: pieni ohjelma käännetty omasta viikon 6 pseudokoodista, kaksi ajoa, kaksi tulostetta, yksi löydetty ja korjattu bugi, kahden minuutin suullinen esitys. Syventäminen (valinnainen): silmukka + if/else, vertaa luokkakaverin toiseen kieleen, lisää syöte (prompt() tai Console.ReadLine()). Sano selvästi: vähimmäistaso riittää hyväksyttyyn. Syventäminen on niille, jotka haluavat enemmän. Tämä on oikeudenmukaisuusasia — opiskelijat tietävät, mitä vaaditaan minimissään. Noin 2 min.

## Dia 16 — Tämän viikon tehtävät (katso oman kielesi tehtävätiedosto)

Käy tehtävät läpi. 8.1 pakollinen — AT3-ohje, käännä viikon 6 pseudokoodisi (oman kielen tehtävätiedosto). 8.2 pakollinen — silmukkalämmittely, laske 1–5. 8.3 syventävä — silmukka + if/else. 8.4 syventävä — lue oikea virheilmoitus ja korjaa. 8.5 syventävä — vertaa luokkakaverin kanssa toisella kielellä. Tee näin: kirjaa jokaisesta ajosta syöte ja tuloste. Tämä on AT3:n raaka-aine. Sano: "Älkää tehkö ajoja ilman muistiinpanoja. Joka ajo kannattaa kirjata, niin reflektion kirjoittaminen on helpompaa." Noin 2 min.

## Dia 17 — Miten AT3 arvioidaan

Tärkeä dia: AT3:n palautus ja arviointi. Hyväksytty / täydennettävä neljän tarkistuksen perusteella: ohjelma toimii tai yritys on dokumentoitu virheilmoituksen kanssa, osaat nimetä yleiskielellä mitä ohjelma tekee, yksi bugi-korjaus-pari dokumentoitu reflektiossa, kahden minuutin esitys pidettiin oppitunnilla 24. Ei numeroarvosanaa. Ei muuta rubriikkia. Sano selvästi: "Ette saa numeroa. Joko AT3 on hyväksytty tai täydennetään. Jos jokin puuttuu, tiedätte täsmälleen mitä." Tämä rauhoittaa kilpailutyyppisiä opiskelijoita ja antaa kaikille selkeän tavoitteen. AT3 palautustila on auki viikon loppuun saakka. Noin 2,5 min.

## Dia 18 — Silmukka sulkeutuu — viikko 1 vielä kerran

Tämä on emotionaalinen dia. Kurssi alkoi yhdellä kysymyksellä: "Miten puhun tietokoneelle niin, että se ymmärtää, mitä haluan sen tekevän?" Painota: olet vastannut siihen. Et teoriassa — toimiva ohjelma kädessäsi. Ohjelmointi ei ole enää mystistä. Lue ääneen rauhallisesti. Anna hetki hiljaisuutta. Sano: "Tästä alkaa varsinainen harjoittelu, ei loppu. Olette nyt valmiit oppimaan lisää, koska perusta on kunnossa." Tämä on tärkeä viesti: kurssi ei ole loppu, vaan portti. Noin 2 min.

## Dia 19 — Kiitos, ja mitä seuraavaksi?

Päätös. Sano: "Tämä oli ohjelmallinen ajattelu — perusta sen ohjelmoinnin alla, jota teette lopuissa opinnoissanne." Painota AT3-lähdetiedostojen säilyttämistä. "Lukekaa se uudelleen kuuden kuukauden päästä. Se näyttää pieneltä. Se on tarkoituskin — te kirjoititte sen." Tämä on hyvä metafora kasvusta. Kiitä luokkaa ajasta ja työstä. Tervetuloa keskeisen kysymyksen toiselle puolelle. Anna lyhyt hiljaisuus. Jos sopii ilmapiiriin, voit kysyä: "Mikä yksi asia tämän kurssin aikana yllätti?" Päätä rauhallisesti ja juhlavasti. Noin 2 min.
