# Brief — Ohjelmallinen ajattelu: arvioitavat tehtävät AT1, AT2, AT3

**Tilaaja:** Matti Seise, Business College Helsinki
**Päivä:** 2026-11-04
**Kieli:** fi

## Tilanne

Kurssi "Ohjelmallinen ajattelu" (8 viikkoa, 24 oppituntia, ammatillinen toinen aste, 15–18-vuotiaat, ICT-ala) on jo tuotettu tällä putkella viikkotasolla (legacy-muoto `viikko-XX/opiskelija/opiskelijatehtavat.md`). Kurssin toimeksianto ja suunnitelma lukitsevat kolme arvioitavaa tehtävää (AT1–AT3), mutta **AT1:tä ja AT2:ta ei ole koskaan kirjoitettu omiksi tehtäviksi** – niistä on olemassa vain yksi dia kummastakin (`paadiat.md`). AT3 on olemassa viikon 8 tehtävänä 8.1-JS / 8.1-CS, mutta siltä puuttuu rubriikki ja kieliagnostinen koontiohje.

## Tehtävä tälle ajolle

Tuota **vain** arvioitavat tehtävät ja niiden rubriikit – ei uutta viikkomateriaalia, ei itseopiskelua, ei sanastoa. Kolme assessment-oppituntia:

| AT | Oppitunti | Palautus | Sisältö (lukittu toimeksiannossa) |
|----|-----------|----------|-----------------------------------|
| AT1 | L6 (viikko 2) | L6:n lopussa / L7:n alussa | Arkisen tai ICT-tehtävän pilkkominen: päätehtävä + tavoite, 4–8 osatehtävää osatavoitteineen, järjestys jossa vähintään yksi riippuvuus nimetty, 3–5 virkkeen reflektio. Artefakti voi olla taulukko, kaavio tai tekstirakenne. |
| AT2 | L18 (viikko 6) | noin L18 | Pseudokoodi pienestä itse valitusta tehtävästä, jossa vähintään yksi ehto ja yksi toisto; jäljitystaulukko normaalilla ja yhdellä hankalalla syötteellä; 5 virkkeen reflektio. Ei oikeaa ohjelmointikieltä. |
| AT3 | L23–L24 (viikko 8) | palautus L23:n lopussa, 2 min suullinen esitys L24:ssä | Oman viikon 6 pseudokoodin kääntäminen toimivaksi ohjelmaksi (JS tai C#, 10–25 riviä), ajo kahdella lähtöarvolla, yhden bugin korjaus, lähdekoodi + kuvakaappaus + lyhyt pohdinta + esitys. Tehtävä 8.1 on jo kirjoitettu; tähän tarvitaan kieliagnostinen koontiohje (assessment.md) ja rubriikki. |

Tuotokset per AT:
- `student/lesson-XX/assessment.md` – opiskelijalle: tavoite, mitä palautetaan, vaiheet, mihin viikon tehtäviin tämä nojaa (osatehtävät nimettynä), "Jos teet tämän yksin", arviointikohteet ilman tasokuvauksia.
- `teacher/lesson-XX/rubric.md` – ES / S- / S / S+ -grid, 3–5 kriteeriä, pohja `templates/rubric-template.md`.

Muoto ja sävy: sama kuin viikon 8 tehtävä 8.1 (`lahde/viikko-08/opiskelija/opiskelijatehtavat-js.md`) ja golden sample. Osatehtävät = olemassa olevat viikon tehtävät (2.1–2.5, 6.1–6.4, 8.1–8.5); AT viittaa niihin id:llä, ei kirjoita niitä uudelleen.

## Lähteet (lahde/)

- `Backup/ohjelmallinen-ajattelu/00-toimeksianto.md` – lukitut arvioitavat osat
- `Backup/ohjelmallinen-ajattelu/01-suunnitelma.md` – oppituntitaulukko, tavoitteet L4–L6, L13–L18, L19–L24
- `viikko-02/opiskelija/opiskelijatehtavat.md` + `paadiat.md` + `opettaja/opettajan-materiaalit.md`
- `viikko-06/opiskelija/opiskelijatehtavat.md` + `paadiat.md` + `opettaja/opettajan-materiaalit.md`
- `viikko-08/opiskelija/opiskelijatehtavat-js.md`, `-csharp.md`, `lisamateriaali-l24-esitysrubriikki.md`, `opettaja/opettajan-materiaalit.md`

## Rajaukset

- Älä muuta olemassa olevia viikkotehtäviä. Jos niissä on ristiriita (esim. viikon 6 diat numeroivat tehtävät 6.1, 6.3, 6.4, 6.5 mutta tehtävätiedosto 6.1–6.4), kirjaa poikkeama, viittaa tehtävätiedoston numerointiin.
- AT2:n palautus: noin L18 (diojen mukaan), ei "viikon 5 lopussa".
- AT3: kieliagnostinen; JS- ja C#-polut viittaavat tehtäviin 8.1-JS ja 8.1-CS. Esitysrubriikki L24 on jo olemassa (`lisamateriaali-l24-esitysrubriikki.md`) – AT3-rubriikki ei toista sitä vaan viittaa siihen esitys-kriteerissä.
- Ei YAML-front-matteria. Ei sanaa "AI-resilientti" opiskelijatiedostoissa.
- Kielletyt termit: ei tilaajan nimiä materiaalissa (ei "Business College Helsinki" opiskelijatiedostoissa).
- Opiskelijalle näkyvä tehtäväluokka: AT on arvioitava – ei 🟢/🟣-merkkiä, vaan otsikko "AT1 — arvioitava tehtävä".
