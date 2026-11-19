# Viikko 7 — Tuntitehtävät

## Yleiskatsaus

Tämä tiedosto sisältää viikon 7 **tunnilla tehtävät, opettajavetoiset** aktiviteetit. Ne ajetaan tunnilla, eivät kotitehtävänä, eikä niitä voi korvata LLM:llä tai työlomakkeella. Molemmat aktiviteetit on suunniteltu toimimaan **kielisekoittuneessa huoneessa** — osa opiskelijoista JavaScriptillä, osa C#:lla, samanaikaisesti. Tämä on pointti, ei ongelma.

- **Aktiviteetti A — *Konsolirelay*** on **PAKOLLINEN**. Se kuuluu **oppitunnin 20 55–75 min slottiin**. Jokainen opiskelija huoneessa — sekä JS- että C#-opiskelija — näkee ja ennustaa molempien kielten katkelmat, ja vertailu on oppitunti.
- **Aktiviteetti B — *Käännä naapurisi*** on **VALINNAINEN**. Se sopii **oppitunnin 21 60–80 min pariaktiviteettislottiin**.

---

## Aktiviteetti A — *Konsolirelay* PAKOLLINEN

**Tavoite.** Luokka ennustaa kuuden pienen katkelman — kolme JavaScriptiä, kolme C#:a — tulosteen ennen kuin opettaja ajaa kunkin livenä. Opiskelijat näkevät — eivät kertomalla — että *ajattelu* on sama molemmilla kielillä ja syntaksi on ainoa, mikä muuttuu. Viikon 7 vastalääke virhekäsitykselle "C# on JS:ää vaikeampi".

**Ryhmäkoko.** Koko luokka. Jokainen opiskelija kirjoittaa oman ennustuksensa; opettaja ajaa kunkin katkelman projektorilla.

**Aika.** 20 min (oppitunti 20, **55–75 min slotti**). Älä lainaa sitä edeltävästä 30 min itsenäisestä lohkosta.

**Opettajan valmistelu.**

1. **Avaa molemmat ympäristöt rinta rinnan** projektorille ennen tuntia: selaimen DevTools-konsoli (mikä tahansa selain) toiselle puoliskolle, `dotnetfiddle.net` toiselle. Pidä C#:n `Main`-luuranko jo näkyvissä Fiddlessä.
2. **Valmistele kuusi katkelmaa** etukäteen — joko kopioituna muistiinpanotiedostoon tai numeroituihin kortteihin. Suositeltu oletusjoukko (kolme JS, kolme C#, tässä järjestyksessä):

   ```javascript
   // Katkelma 1 (JS)
   let x = 5;
   let y = 3;
   console.log(x + y);
   ```

   ```javascript
   // Katkelma 2 (JS)
   let name = "Lyra";
   console.log("Hei, " + name);
   ```

   ```javascript
   // Katkelma 3 (JS)
   let age = 17;
   if (age >= 18) console.log("aikuinen");
   else console.log("alaikäinen");
   ```

   ```csharp
   // Katkelma 4 (C#)
   int x = 5;
   int y = 3;
   Console.WriteLine(x + y);
   ```

   ```csharp
   // Katkelma 5 (C#)
   string name = "Lyra";
   Console.WriteLine("Hei, " + name);
   ```

   ```csharp
   // Katkelma 6 (C#)
   int age = 17;
   if (age >= 18) Console.WriteLine("aikuinen");
   else Console.WriteLine("alaikäinen");
   ```

   Pariutus on tarkoituksellinen: katkelma 1 ↔ 4, 2 ↔ 5, 3 ↔ 6. Sama työ, eri pinta.
3. **Päätä katkelmajärjestys.** Vuorottele (1, 4, 2, 5, 3, 6) vahvimman side-by-side-tuntuman saamiseksi, tai blokkaa (1, 2, 3, sitten 4, 5, 6), jos luokkasi tarvitsee ensin JS-vain/C#-vain-kehyksen. Vuorottelu on oletussuositus.
4. **Pidä taulu valmiina** kaksisarakkeisella tallyllä: **Ennustettu oikein | Tulostuksen yllättämä**. Ruksit relayn aikana kertovat reaaliaikaisesti, lukeeko luokka koodia vai arvaileeko.

**Vaihe vaiheelta fasilitointi.**

1. **Aseta säännöt (2 min).** *"Näytän kuusi pientä katkelmaa, yksi kerrallaan. Kolme on JavaScriptiä, kolme C#:a. Jokaisesta katkelmasta kirjoitat — paperille tai chattiin — täsmälleen sen, mitä luulet konsolin tulostavan, **ennen** kuin painan Run. Sitten ajan sen. Sitten katsomme eroa, jos sellainen on. Pointti ei ole olla oikeassa; pointti on lukea koodia rivi riviltä."*
2. **Näytä katkelma 1 ruudulla (2 min).** Lue se ääneen kerran. Anna opiskelijoille 30 sekuntia. Aja se. Lue tuloste ääneen. Kysy yhdeltä opiskelijalta: *"Mitä ennustit?"* Ruksaa oikea sarake taululle.
3. **Toista katkelmille 2–6 (~15 min yhteensä)**, vuorotellen JS:n ja C#:n välillä (1, 4, 2, 5, 3, 6 on oletusjärjestys). Kullekin katkelmalle:
   - 20 sekuntia ennustaa hiljaisuudessa,
   - aja livenä,
   - lue tuloste ääneen,
   - yksi opiskelija vapaaehtoinen kertomaan, mitä kirjoitti, huone vertailee, ruksaa taulu.
4. **Vie vertailu maaliin lopussa (1 min).** Osoita taulua. *"Ajattelu oli identtinen katkelmille 1 ja 4. 2 ja 5. 3 ja 6. Asia, joka muuttui joka kerta, oli vain sanat. Tämä on se, mitä 'syntaksi on sopimus, ajattelu on se asia' tarkoittaa."*

**Debrief-kysymykset** (käytä 1–2 näistä O20:n 1:15–1:25-debriefissä, ei relay-aktiviteetin sisällä).

- Mikä pari (1↔4, 2↔5 vai 3↔6) tuntui "ilmiselvästi samalta"?
- Ennustiko joku katkelman oikein *toisella* kielellä?
- Mikä yksi C#-sana sinun täytyi etsiä? Mikä yksi JS-sana?

**Miksi tämä vaatii luokkahuoneen.** Live-ennusta-sitten-aja-rytmi ja välitön vertaisvertailu ovat koko pointti. Ei voida tehdä kotitehtävänä.

**Ristiviittaus.** Tämä on **oppitunnin 20 55–75 min slotti** tiedostossa `teacher-materials.md`. "Näimme"-taulu rakennettuna tässä slotissa taitetaan sitten takaisin 1:15–1:25-debriefiin.

---

## Aktiviteetti B — *Käännä naapurisi* VALINNAINEN

**Tavoite.** JS-opiskelija ja C#-opiskelija kääntävät toistensa `if/else`-koodin omalle kielelleen käsin, ei LLM:ää. Opiskelijat löytävät, että käännös on enimmäkseen sana sanalta ja jäljelle jäävät erot ovat pieniä.

**Ryhmäkoko.** Parit — **yksi JS-opiskelija yhden C#-opiskelijan kanssa**. (Parittomat luvut: yksi kolmen ryhmä kahdella samaa kieltä.)

**Aika.** 20 min (oppitunti 21, **60–80 min pariaktiviteettislotti**).

**Opettajan valmistelu.**

1. **Tauluohje** käännöksen säännöillä.
2. **Paperia ja kynä per opiskelija.** Ei kannettavia itse käännöksen aikana.
3. **Varakäyttöinen `if/else`-katkelma** siltä varalta, että opiskelijalla ei ole vielä omaa tehtäväkoodiaan (mikä tahansa iän rajoitus -`if/else` itseopiskelusta toimii).

**Vaihe vaiheelta fasilitointi.**

1. **Pariuta kielten yli (2 min).** Jokaisessa parissa on yksi JS-opiskelija ja yksi C#-opiskelija.
2. **Vaihda `if/else`-koodi (1 min).** Jokainen opiskelija antaa toiselle toimivan koodinsa *Ensimmäinen if/else* -tehtävästä. Ei suullisia vihjeitä.
3. **Käännä käsin (8 min).** Jokainen opiskelija kirjoittaa — paperille, ei kannettavalle — *toisen* opiskelijan koodin **omalla** kielellään. Mikäli sana sanalta -käännös epäonnistuu, ympyröi rivi.
4. **Aja käännökset (5 min).** Salli nyt kannettavat. Jokainen opiskelija liimaa ja testaa käännöksensä omassa ympäristössään.
5. **Paljasta ja keskustele (2 min).** Parit vertaavat, mitä kukin ympyröi. Mitkä rivit kääntyivät puhtaasti?
6. **Koko luokan debrief (2 min).** Kysy kahdelta parilta: *"Mikä yksi sana muuttui eniten? Mikä yksi ei muuttunut lainkaan?"* Odotettu kuvio: `let` ↔ `int`/`string`, `console.log` ↔ `Console.WriteLine`. `if`, `else`, `>=`, `{`, `}` eivät muuttuneet.

**Debrief-kysymykset.**

- Mitkä rivit käänsit empimättä?
- Mitkä rivit saivat sinut pysähtymään ja miettimään?

**Miksi tämä vaatii luokkahuoneen.** Kielten välinen pariutus on olemassa vain huoneessa. Live-käännös käsin on se, mitä LLM ei voi korvata.

**Ristiviittaus.** Tämä on **oppitunnin 21 60–80 min slotti** tiedostossa `teacher-materials.md`. Jos opettajan on pudotettava yksi aktiviteetti tällä viikolla, pudota aktiviteetti B — **aktiviteetti A kantaa viikon 7 keskeisen viestin** ja on AT3-valmiuden diagnostiikka.
