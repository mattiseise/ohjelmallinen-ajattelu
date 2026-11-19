# Toimeksianto — Ohjelmallisen ajattelun kurssi, viikko 7 (englanti)

## Viikon 7 teema
**Ohjelmointikielet käytännössä (JavaScript & C#, osa 1)**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O19**: Miksi ohjelmointikieliä tarvitaan? Syntaksi, käskyt ja JavaScriptin rooli
- **O20**: Ensimmäiset käskyt: console.log / Console.WriteLine, arvot, muuttujat, yksinkertaiset laskut
- **O21**: Ehdot koodissa: if, else, vertailut

## Viikon keskeinen viesti
Ohjelmointikieli on tapa tehdä ohjeista niin täsmällisiä, että tietokone osaa noudattaa niitä ilman arvailua. Ajattelu on sitä, mitä olemme tehneet koko kurssin ajan; kieli on vain se syntaksi, jolla se kirjoitetaan.

## Bloom-katto
Ymmärtäminen + Soveltaminen (suorita ensimmäiset käskyt, kirjoita pieni if/else; ei debugger-frameworkkeja).

## Ammatillinen kulma
Esimerkkejä joihin Rasmuksen kannattaa nojata: arvon kirjaaminen selaimen konsoliin; kahden luvun vertailu (iän tarkistus, salasanan pituuden tarkistus); ystävällisen tervehdyksen tulostaminen.

## Arvioinnin kosketuspiste
Pohja AT3:lle (käännä oma pseudokoodi pieneksi ohjelmaksi). AT3:n toimeksianto julkaistaan viikolla 8.

## Lisäsäännöt tälle viikolle

- **Kaksikielisyysvaatimus.** Oppitunti 19 on kieliriippumaton — selitä *mikä* ohjelmointikieli on ja *mitä* syntaksi tarkoittaa, ennen kuin sidot sen mihinkään tiettyyn kieleen. Oppitunnit 20 ja 21 esittelevät konkreettisen syntaksin **sekä JavaScriptillä että C#:lla** rinta rinnan.
- Jaa tehtävätiedostot: tuota `student-tasks-js.md` ja `student-tasks-csharp.md` `student-tasks.md`:n lisäksi (tai sen sijaan). Käytä lyhyttä `student-tasks.md`:tä indeksinä, joka osoittaa kahteen kielikohtaiseen tiedostoon, TAI ohita `student-tasks.md` ja käytä kahta kielikohtaista tiedostoa suoraan — Sune päättää.
- Selainkonsoli (JavaScript) ja yksinkertainen .NET-interaktiivinen / online-C#-ympäristö ovat ainoat suoritusalustat. Ei IDE-asennusta selaimen/online-työkalujen lisäksi.
- Ei automaattista testausta tai debugger-frameworkkeja. Ohjelmointitehtävän taso on "kokeile, aja, katso mitä tapahtuu".

## Tuotoskieli
**Englanti.** Börje (suomenkielinen viimeistely) ohitetaan tällä ajolla.

## Tuotoksen laajuus (tällä ajolla)
- Sune tuottaa viikon 7 suunnitelman lukituilla hyväksymiskriteereillä, Rasmuksen briiffin ja eteenpäin katsovat stubit.
- Rasmus rakentaa **vain viikon 7**.
- Linnea + Wilhelm auditoivat viikon 7.
- Alfred paketoi viikon 7 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** putkessa tällä kierroksella. Markdown-julkaisu on toimitettava.

## Kanoninen lohkorakenne per viikko (lukittu)
```
student/week-07/
├── overview.md         # viikon teema + must-do-minimi vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria joka kattaa kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 PAKOLLISTA + 2–3 🟣 SYVENTÄVÄÄ tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---' erottimet
teacher/week-07/
├── teacher-materials.md  # 3 × 90 min fasilitointi, oppituntikohtaisilla kalvovinkeillä
└── in-class-tasks.md     # ≥1 PAKOLLINEN opettajavetoinen tuntiharjoitus
```

Lisäksi vain silloin kun luentosegmentti aidosti tarvitsee syvempää materiaalia, ylimääräinen `student/week-07/slides-l<n>-<aihe>.md`-tiedosto (4–8 kalvoa). Rasmus päättää luentosegmenttikohtaisesti.

## Kovat säännöt kaikille viikoille
- **Englanti läpi**, kaikki 7 tiedostoa.
- **"AI-resilient"-merkki on sisäinen** — ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuutta, ei merkkiä.
- **"Jos teet tämän yksin"** -alaluku (`### Jos teet tämän yksin`) on pakollinen jokaisessa tehtävässä, joka olettaa paria / seuraajaa / testaajaa, ja siihen tulee konkreettinen vaihtoehto (24 h tauko, video itsestä, eri laite, luokan chat).
- **"Must-do-minimi"** on sanamuoto PAKOLLISILLE tehtäville overview.md:ssä ja student-tasks.md:ssä (ei "pakollinen minimi").
- **Kalvovinkit** vaaditaan jokaiseen 90 min oppituntisuunnitelmaan `teacher-materials.md`:n sisällä.
- **30–50 % itsenäisen työn** lohko vaaditaan jokaiseen 90 min oppituntisuunnitelmaan.
- **Ei kalvotiedostoja `slides.md`:n (+ valinnaisen `slides-l<n>-*.md`:n) lisäksi.** Ei PowerPointia, ei jest/mocha/vitest/pytest-viittauksia missään.
- **AT1-muistutus** jokaisen tehtävän `### Pidä muistiinpanot`-lohkossa (paitsi jos viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitse relevantti AT).
- **Tiedostojen välinen yhtenäisyys**: tehtävänumerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; tuntiaktiviteetit joihin viitataan `teacher-materials.md`:ssä on olemassa `in-class-tasks.md`:ssä.

## Kurssitason konteksti
Yllä oleva toimeksianto on viiva 8-viikkoisen kurssin **viikolle 7**. Koko kurssin toimeksianto ja lukittu 24 oppitunnin tiekartta löytyy:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssin toimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8 viikon tiekartta)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyyliviittauksena)

## Kultainen näyte (suomi, tyylin/syvyyden/määrän viittaus)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason määrä on ~3× yhden kultaisen näytteen oppitunnin. Viikon 1 julkaisu yllä olevassa polussa on myös viittaus päästä päähän englanninkieliselle viikolle.
