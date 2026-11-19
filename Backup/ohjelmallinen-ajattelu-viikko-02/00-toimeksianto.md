# Toimeksianto — Ohjelmallinen ajattelu -kurssi, viikko 2 (englanniksi)

## Viikon 2 teema
**Ongelman pilkkominen**

## Oppitunnit (lukittu kurssisuunnitelmasta)
- **O4**: Ongelman pilkkominen: päätehtävä, osatehtävät ja tavoite
- **O5**: Vaiheiden järjestys ja riippuvuudet
- **O6**: ICT-tehtävän pilkkominen (AT1 palautetaan O6:n lopussa / O7:n alussa)

## Viikon keskeinen viesti
Iso ongelma muuttuu hallittavaksi ongelmaksi, kun nimeät päätehtävän, sen osatehtävät ja järjestyksen, jossa ne on tehtävä.

## Bloom-kattorajat
Muistaminen + Ymmärtäminen hallitsevia; Soveltaminen sallittua (opiskelijat pilkkovat oikeita tehtäviä).

## Ammatillinen näkökulma
Esimerkkejä, joihin Rasmuksen kannattaa nojata: käyttäjätilin luominen, tiedoston jakaminen, uuden kollegan perehdyttäminen, käynnistysongelman vianetsintä, tukitiketin täyttäminen.

## Arvioinnin liityntäkohta
AT1 (pilkota arkielämän tai ICT-tehtävä vaiheisiin) palautetaan oppitunnin 6 lopussa. Tämän viikon tehtävät syöttävät suoraan AT1:een.

## Tulostekieli
**Englanti.** Börje (suomenkielinen kielenhuolto) ohitetaan tällä kierroksella.

## Tulostuksen laajuus (tämä kierros)
- Sune tuottaa viikon 2 suunnitelman lukittuine hyväksymiskriteereineen, Rasmuksen briiffeineen ja eteenpäin katsovine luonnoksineen.
- Rasmus rakentaa **vain viikon 2**.
- Linnea + Wilhelm auditoivat viikon 2.
- Alfred paketoi viikon 2 julkaisun pelkkänä Markdownina.
- **Ei PDF:ää, ei PPTX-renderöintiä** putkessa tällä kierroksella. Markdown-julkaisu on toimitettava tuote.

## Viikon kanoninen lohkorakenne (lukittu)
```
student/week-02/
├── overview.md         # viikon teema + must-do minimum vs. syventävä (200–400 sanaa)
├── self-study.md       # teoria kattaen kaikki 3 oppituntia (~2400–4000 sanaa)
├── student-tasks.md    # 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING -tehtävää
├── vocabulary.md       # 10–18 termiä
└── slides.md           # ~10–20 Markdown-kalvoa, '---'-erottimet
teacher/week-02/
├── teacher-materials.md  # 3 × 90 min fasilitointia, oppituntikohtaisilla Slide cues -osioilla
└── in-class-tasks.md     # ≥1 MANDATORY opettajajohtoinen tuntitehtävä
```

Lisäksi vain silloin kun luentojakso oikeasti tarvitsee syvempää aineistoa, lisätiedosto `student/week-02/slides-l<n>-<topic>.md` (4–8 kalvoa). Rasmus päättää luentojaksokohtaisesti.

## Kovat säännöt kaikille viikoille
- **Englanti kauttaaltaan**, kaikki 7 tiedostoa.
- **"AI-resilient"-leima on sisäinen** — ei saa esiintyä missään oppijalle näkyvässä tiedostossa. Linnea auditoi ominaisuuden, ei leimaa.
- **"If you are doing this alone"** -alaosio (`### If you are doing this alone`) vaaditaan jokaiseen tehtävään, joka olettaa pariin / seuraajaan / testaajaan, konkreettisella vaihtoehdolla (24h:n tauko, video itsestä, eri laite, luokkachat).
- **"Must-do minimum"** on sanamuoto MANDATORY-tehtäville overview.md:ssä ja student-tasks.md:ssä (ei "mandatory minimum").
- **Slide cues** vaaditaan jokaiseen 90 min:n oppituntisuunnitelmaan `teacher-materials.md`:n sisällä.
- **30–50 % itsenäistä työskentelyä** -lohko vaaditaan jokaisessa 90 min:n oppituntisuunnitelmassa.
- **Ei muita kalvotiedostoja kuin `slides.md` (+ valinnainen `slides-l<n>-*.md`).** Ei PowerPointia, ei jest/mocha/vitest/pytest-viittauksia mihinkään.
- **AT1-muistutus** jokaisen tehtävän `### Keep your notes` -lohkossa (paitsi jos tämän viikon tehtävät syöttävät AT2:ta tai AT3:a — silloin mainitse kyseinen AT).
- **Tiedostojen välinen johdonmukaisuus**: tehtävänumerointi `slides.md`:ssä vastaa `student-tasks.md`:tä; tuntitehtävät, joihin viitataan `teacher-materials.md`:ssä, löytyvät `in-class-tasks.md`:stä.

## Kurssitason konteksti
Yllä oleva toimeksianto on viipale 8-viikkoisen kurssin **viikosta 2**. Koko kurssin toimeksianto ja lukittu 24 oppitunnin tiekartta löytyy:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (kurssin toimeksianto)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (lukittu 24 oppitunnin suunnitelma + 8-viikon tiekartta)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (viikko 1 — rakennettu, käytä kurssin sisäisenä tyylin referenssinä)

## Golden sample (suomeksi, tyylin/syvyyden/laajuuden referenssi)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

Viikkotason laajuus on ~3× yksittäinen golden sample -oppitunti. Viikon 1 julkaisu yllä olevassa polussa toimii myös referenssinä koko englanninkieliselle viikolle.
