# Wilhelm — audit, kierros 1 (AT1–AT3)

Auditoitu: `materiaali/student/lesson-06|18|24/assessment.md`, `materiaali/teacher/lesson-06|18|24/rubric.md`, `course.draft.json`
Vasten: `01-suunnitelma.md` (H1–H9, H14–H15, Rajaukset), `00-brief.md`, `course.schema.json`, lähdetehtävät viikko-02/06/08, `lisamateriaali-l24-esitysrubriikki.md`, proosasäännöstö `golden-sample-teaching.md`, Linnean r1/r2.
Rajattu ajo: teacher-materials-otsikkokontrakti, Mermaid, self-study/vocabulary/teacher-materials -vaatimukset eivät koske tätä ajoa (suunnitelman Rajaukset).
Päivä: 2026-11-04

## Päätös

**approved**

## Blocking-löydökset

Ei löydöksiä. Kaikki mekaaniset tarkistukset (a)–(f) läpäisty komentoajoina, ks. Tarkistettu evidenssi.

## Non-blocking-parannukset

1. `student/lesson-24/assessment.md`, `## Mihin viikon tehtäviin tämä nojaa` (rivi 46): H5 listaa AT3:lle myös "esitysohje L24". Osio nimeää 8.1-JS/CS, 8.2, 8.3, 8.4, 8.5 ja AT2/6.1, mutta ei `lisamateriaali-l24-esitysrubriikki.md`:tä. Tiedosto on viitattu kahdesti muualla (rivi 21 ja Arviointikohteet), joten viittaus on olemassa; yksi virke osioon riittää. Alfred.
2. Termi "isku": `student/lesson-24/assessment.md` ja `teacher/lesson-24/rubric.md` puhuvat "neljästä iskusta" (suunnitelman sanavalinta), mutta viitattu `lisamateriaali-l24-esitysrubriikki.md` ja tehtävä 8.1 sanovat "4 kohtaa" / "neljä osaa". Opiskelija ei löydä sanaa "isku" viitatusta tiedostosta. Yhtenäistäminen Alfredille tai Börjelle; sisältö on sama.
3. `course.draft.json` lesson-24 `tasks`: id:t `8.2`, `8.3`, `8.4`, `8.5` ovat suunnitelman H5:n mukaiset, mutta lähdetiedostojen otsikoissa id:t ovat `8.2-JS`/`8.2-CS` jne. Resolvoituvat yksikäsitteisesti (kummassakin kielitiedostossa sama numero), joten ei blocking; Alfred päättää täyteen manifestiin yhdistäessä, pidetäänkö kieliagnostinen id.
4. `student/lesson-18/assessment.md` rivi 5: Tavoite-kappaleen toinen virke on 35 sanaa ja kolme sivulausetta (”AT2 pyytää samaa työtä … koska ne ovat testi”). Sisältö on oikein ja Linnean K3-korjaus; Börje voi jakaa kahdeksi.
5. `teacher/lesson-06/rubric.md` rivi 13: taulukon jälkeinen virke "kysymysliite puuttuu → täydennettäväksi" on Linnean huomion B mukainen ja hyvä, mutta H3 ei mainitse taulukon jälkeistä riviä AT1:lle (AT3:lle mainitsee). Hyväksyn, koska se täsmentää K4:n ES-rajaa; kirjaan näkyviin.
6. Lähdetiedostot (ei tämän ajon tuotos): viikko-02 tehtävät 2.4 ja 2.5, viikko-06 6.4 ja viikko-08 8.4-JS kantavat labelin "SYVENTÄVÄ" ilman 🟣-merkkiä; manifestin `class`-arvot (DEEPENING) ovat silti oikein. Orkestraattorille tiedoksi legacy-korjausajoa varten.

## Tarkistettu evidenssi

**(a) Manifesti ja polut** — `python3 -I` + `jsonschema.validate(course.draft.json, course.schema.json)` → VALID. Pakolliset kentät `id, title, type, objectives, concepts, builds_on, tasks` kaikilla kolmella lessonilla. `rubric`-polut `teacher/lesson-06|18|24/rubric.md` resolvoituvat materiaali-kansiossa (os.path.exists → True ×3); `student/lesson-XX/assessment.md` olemassa ×3; moduulien `lessons`-id:t löytyvät `lessons`-listasta ×3. `find materiaali -type f` → täsmälleen kuusi tiedostoa (H1).

**(b) H1/H2-otsikot** — H2-lista jokaisessa assessment.md:ssä merkki merkiltä `['## Tavoite','## Mitä palautat ja milloin','## Vaiheet','## Mihin viikon tehtäviin tämä nojaa','## Jos teet tämän yksin','## Arviointikohteet']` → True ×3, ei muita H2:ia. H1 regex `^# AT[123] — arvioitava tehtävä: ` (pitkä viiva) → True ×3; `grep '^# AT[123] - '` → 0 osumaa. H3:t vain lesson-24:ssä ja vain sallituissa osioissa (`### Kirjallinen osa (oppitunnin 23 lopussa)`, `### Suullinen osa (oppitunnilla 24)`, `### JavaScript-polku`, `### C#-polku`).

**(c) Kriteerit ja rubriikki** — assessment.md:n `- **…**`-nimet ↔ rubric.md:n ensimmäinen sarake: lesson-06 4/4, lesson-18 5/5, lesson-24 4/4, sama järjestys, sanasta sanaan (list-equality True). Nimet täsmäävät suunnitelman K-taulukoihin. Otsikkorivi `| Arviointikohteet | ES | S- | S | S+ |` ×3; rivimäärät 4/5/4 (3–5); Asteikko-loppurivi sanasta sanaan ×3; `**Arvioitava tehtävä:**` ja `**Mittaa tavoitteita:** O6.1–O6.4 / O18.1–O18.5 / O24.1–O24.4` ×3; rubriikin H1 = manifestin lesson-title ×3; ei `<!--`-kommentteja eikä `<placeholder>`-jäänteitä. Solujen virkemäärät 1–3 (H7), ei "hyvä/erinomainen"-sanastoa.

**(d) Kielletyt termit** — grep (case-insensitive) kaikista kuudesta tiedostosta manifestin 13 `forbidden_terms` + `AI resilient`, `AI-resilien`, `AI resilien`, `tekoälyresilien`, `resilien`, `resisten`, `Hyväksytty / ei vielä hyväksytty` → 0 osumaa. `🟢|🟣|PAKOLLINEN|SYVENTÄVÄ` → 0 osumaa kaikissa tiedostoissa (H9).

**(e) Tehtävä-id-ristiviittaukset** — assessment.md:ssä mainitut id:t: lesson-06 {2.1, 2.2, 2.3, 2.4, 2.5}; lesson-18 {6.1, 6.2, 6.3, 6.4}; lesson-24 {8.1-JS, 8.1-CS, 8.1, 8.2, 8.3, 8.4, 8.5, 6.1}. Kaikki löytyvät `grep '^## .*\b2\.[0-9]'` ym. -ajoilla lähdeotsikoista: viikko-02 rivit 17/53/94/131/179; viikko-06 rivit 22/82/145/185; viikko-08 JS rivit 17/73/120/152/198 ja CS 19/79/127/161/206. Manifestin `tasks[].id` (pl. AT-rivi) ⊆ assessment.md:n viittaukset ×3 (orkestraattorin päätös 2). Sisältöviittaukset tarkistettu lähteistä: 2.2 kolme tarkentavaa kysymystä + "alitehtävässä/alatavoitteessa/yhteydessä" (viikko-02 r. 66, 73), 2.3 tarkistuslista-vinkki (r. 121), 2.4 valikkopolut (r. 134), 6.1 vaihe 3 muuttujanimet + "päivän vanha sinä" (viikko-06 r. 29, 46–47), 6.2 neljä bugityyppiä (r. 122–123) ja puhtaalle sivulle -vinkki (r. 136), jäljitystaulukon muoto (r. 53), 8.1 varamalli/vaiheet 2–6/yksin-vaihtoehto/neljä tarkistusta/L23–L24 (JS r. 17–72), 8.4 pätkä B (JS r. 168), esitysrubriikin 4 kohtaa, 2 min, neljä tarkistusta, "Nimeä yksi asia, jonka huomasit" (lisamateriaali r. 12–17, 33–38, 51).

**(f) Hygienia** — `startswith('---')` → False ×6 (ei YAML). ```` ``` ````-määrä 0 ×6 (ei koodilohkoja, H7). Taulukkorivien pipe-määrä 6 jokaisella rivillä ×3 (5 solua, renderöityy). Numeroidut listat jatkuvia: lesson-06 1–5 ja 1–7 (Linnean r2-korjaus 2 todettu tehdyksi), lesson-18 1–3 ja 1–7, lesson-24 1–5 ja 1–8. grep englanninkieliset jäänteet (`in this guide|for example|you should|note:|TODO|TBD|placeholder`) → 0. Absoluuttiset polut (`/home/`, `/Users/`, `~/`) → 0; viittaus `lisamateriaali-l24-esitysrubriikki.md` suhteellisena (H15). Sanamäärät (kirjaimelliset sanat) 785 / 794 / 789 (H7: 450–800). Tyhjät lupaukset: jokainen "ks. vaihe N" / "kohta Kirjallinen osa" -viittaus osoittaa olemassa olevaan vaiheeseen; ei viittauksia tiedostoihin, joita ei ole.

**H6 ajoitus** — AT1 r. 19 "oppitunnin 6 lopussa (noin 75 minuutin kohdalla) tai viimeistään oppitunnin 7 alussa"; AT2 r. 15 "noin oppitunnilla 18"; AT3 r. 9/19/32 "oppitunnin 23 lopussa" + "oppitunnilla 24". Täsmäävät.

**H14** — `student/lesson-24/assessment.md` r. 5 "Tehtävän 8.1 neljä tarkistusta ovat hyväksytyn (S) kynnys…"; `teacher/lesson-24/rubric.md` r. 13 "neljä tarkistusta täyttyvät = vähintään S". Täsmää.

**Linnean r2 korjaukset todettu**: (1) rubric-24 K1 ES = "ei mitään pseudokoodia eikä varamallia", S- = "varamalli sellaisenaan, vain arvot vaihdettu" → yksi solu per tapaus; assessment-24 vaihe 1 "jää tässä arviointikohteessa tasolle S-". (2) lesson-06 vaiheiden numerointi 1–7 ehjä. Huomiot A (lesson-18 vaihe 7), B (rubric-06 r. 13) ja C (lesson-24 kohta 5 "ei kuulu 3–5 virkkeen rajaan") tehty.

**Proosapistokoe säännöstöä vasten** — Kaikki kolme `## Tavoite`-osiota avautuvat opiskelijan omalla tilanteella ("Olet viikon 2 aikana pilkkonut…", "Tehtävässä 6.1 kirjoitit…", "Viikolla 6 kirjoitit…"), eivät määritelmällä. Sinuttelu läpi; esimerkki ennen termiä (AT1 vaihe 2 salasanan nollaus, AT2 vaihe 3 akku 100 %, AT3 vaihe 4 akku 0 %). Yli 35 sanan virkkeitä 0 (skripti), yksi 35-sanainen (non-blocking 4). Bullet-osuus: listat vain palautettavissa, vaiheissa ja arviointikohteissa — säännöstön sallimat kohdat. Rubriikkien solut havainnoitavia ("X riippuu Y:stä, koska …", rivinumero, virheilmoitus sanasta sanaan), ES/S- kuvattu puutteena eikä adjektiivilla.

## Seuraava

jatka Alfredille
