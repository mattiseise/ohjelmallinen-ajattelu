# Linnea — pedagoginen audit, kierros 1 (AT1–AT3)

Auditoitu: `materiaali/student/lesson-06|18|24/assessment.md`, `materiaali/teacher/lesson-06|18|24/rubric.md`
Vertailutaso: golden sample lesson-01, viikkotehtävät 2.1–2.5, 6.1–6.4, 8.1–8.5 (JS/CS), L24-esitysohje.
Päivä: 2026-11-04

## Päätös

**korjattava**

Yksikään kolmesta arvioitavasta tehtävästä ei ole AI:lla läpi juostava: jokaisessa on vähintään yksi rakenteellinen ankkuri (oma todellinen tehtävä + luokassa tehty parikatselmointi; käsin luokassa tehty jäljitys; oma pseudokoodi ketjutettuna AT2:een + live-esitys). Punainen lanka pitää, osatehtäväviittaukset ovat oikein. Yksi blocking-löydös: AT3-rubriikin K1-sarake on sisäisesti ristiriitainen varamallipolulla, eli juuri heikoimman opiskelijan polulla. Lisäksi joukko korjattavia kohtia, joista tärkeimmät ovat AT1 K3:n S-taso (ei mittaa O6.3:a kokonaan), AT2:n kolmannen jäljityksen asema ja AT3:n pohdinnan kuorma.

---

## Löydökset luokiteltuina

### BLOCKING

**B1 — `teacher/lesson-24/rubric.md`, rivi K1 "Käännös omasta pseudokoodista", solut ES / S- / S.**
Rasmuksen oma tulkinta S--solussa ("Varamallilla tehty käännös, jossa arvot on vain vaihdettu, sijoittuu tähän") on hengeltään perusteltu — pelkkä arvojen vaihto ei osoita yhtään kääntämisosaamista (O24.1), joten se ei voi olla S. Mutta sellaisenaan sarake ei toimi varamallipolulla:
- Tehtävä 8.1 (JS ja CS, vaihe 1) ohjeistaa varamallista täsmälleen "muokkaa arvot". Opiskelija, joka noudattaa viikkotehtävän ohjetta sanatarkasti, saa AT3:ssa S-. Rubriikki rankaisee viikkotehtävän määräämästä toiminnasta, eikä assessment.md kerro, mitä varamalliopiskelijan pitää tehdä enemmän päästäkseen S:ään.
- S-solu vaatii, että ohjelma "vastaa palautettua omaa viikon 6 pseudokoodia rivi riviltä". Varamalliopiskelijalla ei ole omaa pseudokoodia, joten hän ei voi täyttää S-solun sanamuotoa — vaikka orkestraattori päätti, että varamalli sallii S:n.
- ES-solu: "lähdepseudokoodia ei ole palautettu, eikä ohjelmaa voi verrata mihinkään" → varamalliopiskelija on ES:n sanamuodon mukaan hylätty. Sama palautus on siis ES:n, S-:n ja S:n solujen mukaan kolmella eri tasolla.
- S--solu niputtaa kaksi eri puutetta ("rakenne on eri" ja "arvot vain vaihdettu"), jotka ovat eri osaamisen puutteita.

Vaadittu korjaus: määrittele varamallipolku yhdessä paikassa ja kirjoita se sekä opiskelijalle (`student/lesson-24/assessment.md`, vaihe 1 ja "Mihin viikon tehtäviin tämä nojaa") että rubriikin K1-soluihin. Ehdotus, joka tekee O24.1:n mitattavaksi myös varamallilla: varamalliopiskelija kirjoittaa ensin varamallin kurssin pseudokoodina (avainsanat, 6–12 riviä) ja palauttaa sen "lähdepseudokoodina"; käännös verrataan siihen. Silloin ES = ei lähdepseudokoodia (omaa tai varamallista kirjoitettua), S- = pseudokoodi ja ohjelma eivät vastaa toisiaan TAI varamallista on vain vaihdettu arvot ilman pseudokoodivaihetta, S = vastaa rivi riviltä (varamalli jää tähän), S+ = oma pseudokoodi + nimetty vastaamattomuuskohta. Jos orkestraattori ei halua lisätä vaihetta, vaihtoehto on hyväksyä Rasmuksen tulkinta mutta kirjoittaa ES- ja S-solut niin, etteivät ne sulje varamallia pois, ja sanoa assessment.md:ssä suoraan: "varamalli + pelkkä arvojen vaihto = S-; S vaatii, että muutat myös yhtä rakennetta (ehto tai silmukka) ja kerrot pohdinnassa mitä".

### KORJATTAVA

**K1 — `teacher/lesson-06/rubric.md`, rivi K3 "Järjestys ja riippuvuudet", S-solu.**
O6.3 sanoo: "nimetä vähintään yhden riippuvuuden **sekä tunnistaa, mitkä osatehtävät ovat järjestyksen suhteen vapaita**". S-solu mittaa vain riippuvuuden; vapaan osatehtävän tunnistus on vasta S+:ssa. Kriteeri ei siis mittaa tavoitetta kokonaan S-tasolla, vaikka assessment.md:n vaihe 4 vaatii sen kaikilta ("Merkitse myös, mitkä osatehtävät voisi tehdä kummassa tahansa järjestyksessä"). Korjaus: S = yksi perusteltu riippuvuus **ja** vähintään yksi osatehtävä merkitty vapaaksi (tai perustelu, miksi mikään ei ole vapaa); S+ = vähintään kaksi perusteltua riippuvuutta ja vapaan osatehtävän perustelu — pilkkominen ei ole tarkistuslista. S+ pysyy laadullisesti eri tasona, ei vain määränä.

**K2 — `student/lesson-18/assessment.md`, vaihe 5 ↔ `teacher/lesson-18/rubric.md` K4 S+.**
Vaihe 5 käskee: "Korjaa pseudokoodi ja jäljitä korjattu versio uudella taulukolla" — pakollisena vaiheena. Rubriikissa korjatun version uudelleenjäljitys on S+-elementti. Opiskelija lukee, että L18:n 30 minuutin itsenäisessä jaksossa pitää tehdä kolme täyttä jäljitystä (10–20 riviä × silmukan kierrokset) + reflektio. Se ei ole realistista 15–18-vuotiaalle 30 minuutissa, ja ristiriita rubriikin kanssa hämärtää, mikä on kynnys. Korjaus: vaihe 5 muotoon "Korjaa pseudokoodi ja merkitse korjattu rivi. Jos ehdit, jäljitä korjattu versio uudella taulukolla — se nostaa arviota." Arviointikohteet-listaan ei tarvitse lisätä tasokuvausta.

**K3 — `student/lesson-18/assessment.md`, "Tavoite" ja "Mihin viikon tehtäviin tämä nojaa" ↔ "Mitä palautat ja milloin" + vaihe 4.**
Tavoite-kappale sanoo, että 6.1:n työ "on täsmälleen se työ, jota AT2 pyytää", ja viittausosio sanoo, että 6.1:n "kaksi jäljitystä … ovat AT2:n raaka-aine lähes sellaisenaan". Vaihe 4 ja palautusosio kuitenkin vaativat, että jäljitykset tehdään L18:n itsenäisessä jaksossa (tämä on AT2:n AI-resilienssin ydin, H10 AT2 b, ja se on oikein). Opiskelija ei tiedä, kelpaako kotona tehty 6.1-taulukko. Korjaus: sano yhdessä virkkeessä, että 6.1:n jäljitykset ovat harjoitus ja AT2:n taulukot tehdään uudelleen luokassa L18:lla — "se on testi". Samalla kerro, että vaiheet 1–3 (pseudokoodin tarkistus, rivinumerointi, hankalan syötteen valinta) tehdään **ennen** oppituntia 18, jotta 30 minuuttia riittää kahteen jäljitykseen.

**K4 — `student/lesson-24/assessment.md`, "Kirjallinen osa" kohta 4 + vaiheet 2, 3, 6 ↔ rubriikki K1–K3 S+.**
Pohdinnan pituus on 3–5 virkettä, mutta siihen pitää mahtua: mitä ohjelma tekee, mitä muuttujaa muutettiin, mikä bugi, miten korjattiin, virheilmoitus sanasta sanaan — ja S+-tasolle lisäksi vastaamattomuuskohta pseudokoodin ja kielen välillä (vaihe 2), ennuste vs. toteutunut (vaihe 3) ja syntaksi- vs. hiljainen bugi -vertailu (vaihe 6). Kahdeksan asiaa viidessä virkkeessä ei ole 15–18-vuotiaalle realistinen, ja se johtaa siihen, että S+-havainnot jäävät pois tilan puutteen takia. Legacy 8.1 vaati pohdinnalta kolme asiaa. Korjaus: joko (a) pohdinta 5–8 virkettä, tai (b) pidä 3–5 virkettä ydinasioille ja siirrä virheilmoitus, ennuste ja vastaamattomuuskohta omiksi yhden rivin merkinnöikseen palautuksen listaan ("Virheilmoitus: …", "Ennuste ennen ajoa 1: …"). Vaihtoehto (b) on myös opettajalle helpompi tarkistaa.

**K5 — `student/lesson-06/assessment.md`, vaihe 1 + "Jos teet tämän yksin".**
AT1 olettaa, että opiskelijalla on tehtävästä 2.1, 2.2 tai 2.4 valmis pilkkominen. Opiskelija, joka ei tehnyt viikon 2 tehtäviä (poissaolo), aloittaa L6:n 30 minuutissa tyhjästä, eikä tiedosto sano, mitä hän tekee. AT2 hoitaa saman tilanteen ("Jos et tehnyt tehtävää 6.1 …, kirjoita uusi"). Korjaus: lisää vaiheeseen 1 virke "Jos sinulla ei ole yhtään viikon 2 pilkkomista, valitse nyt yksi tämän viikon todellinen tehtäväsi ja tee vaiheet 2–4 tehtävän 2.1 säännöillä; osatehtäviä riittää neljä."

**K6 — `student/lesson-06/assessment.md`, "Mitä palautat ja milloin" + `teacher/lesson-06/rubric.md` K4.**
AI-resilienssi on AT1:ssä riittävä, mutta ohuin kolmesta: artefakti (päätehtävä, tavoite, osatehtävät, riippuvuus) on kokonaisuudessaan kotona LLM:llä tuotettavissa arkisella polulla, ja rubriikin K4 nojaa reflektion omaan ilmoitukseen siitä, mitä pari kysyi. Luokassa tehty parikatselmointi on todellinen ankkuri, mutta siitä ei jää palautukseen jälkeä. Korjaus: lisää palautettaviin viides osa, joka on jo viikkotehtävässä 2.2 (vaihe 4): "Parisi (tai yksin-vaihtoehdon) kolme tarkentavaa kysymystä sanasta sanaan, osatehtävän numerolla." Reflektion muutos sidotaan yhteen näistä kysymyksistä. Rubriikin K4 S-solu: "muutos vastaa yhtä palautetuista kysymyksistä". Tämä ei lisää kuormaa (kysymykset kirjoitetaan jo muistiin vaiheessa 5) ja tekee S-tason havainnoitavaksi.

### HUOMIO

**H1 — `student/lesson-18/assessment.md`, "Jos teet tämän yksin".** Vaihtoehto "jäljitä kerran puhelimen muistiinpanoihin ja seuraavana päivänä paperille" on ristiriidassa sen kanssa, että AT2:n taulukot tehdään L18:lla luokassa. Tarkoitus on selvästi korvata 6.3:n ulkopuolinen lukija ennen L18:aa; sano se ("ennen oppituntia 18, harjoituksena").

**H2 — `teacher/lesson-18/rubric.md`, K5 S+.** Vaatii "havainnon ulkopuolisesta lukijasta (tehtävä 6.3)" tai LLM-erimielisyydestä (6.4). Molemmat ovat syventäviä tehtäviä, mikä on S+:lle hyväksyttävää. Kirjoita kuitenkin näkyviin, että yksin-vaihtoehdon "päivän vanha minä" (24 h tauko) kelpaa ulkopuoliseksi lukijaksi, kuten tehtävä 6.1 lupaa. Muuten yksin tekevä ei voi saavuttaa S+:aa K5:ssä.

**H3 — `teacher/lesson-24/rubric.md`, K3 S+.** "Erottaa syntaksivirheen ja hiljaisen logiikkavirheen ja kertoo, kumpi oli vaikeampi löytää" edellyttää, että opiskelijalla sattui olemaan molemmat bugit. Brief vaatii yhden bugin. Sano solussa, että toinen tapaus saa olla tehtävän 8.4 pätkä B -kokemus, jolloin S+ ei riipu tuurista.

**H4 — `teacher/lesson-24/rubric.md`, K2 ES.** "Kuvakaappaus … toisen opiskelijan ympäristöstä" ei ole luotettavasti havainnoitava: kaksi DevTools-konsolia näyttävät samalta. Ei korjausvaatimus — K4:n live-esitys ja jatkokysymys ovat todellinen tarkistus — mutta älä luota tähän soluun yksin.

**H5 — `student/lesson-24/assessment.md`, palautusajoitus ↔ legacy L24-tuntisuunnitelma.** Kirjallinen osa (sis. kuvakaappaus kahdesta ajosta ja bugi–korjaus) palautetaan L23:n lopussa, mutta legacy-tuntisuunnitelman L24 itsenäinen jakso 0:25–0:55 on "testausta ja korjausta". Jos testaus tapahtuu vasta L24:llä, kuvakaappaus ei voi olla valmis L23:lla. Brief lukitsee ajoituksen, joten tämä on orkestraattorin asia: joko L24:n jakso on esityksen harjoittelua, tai kuvakaappauksen ja bugin saa täydentää L24:n alkuun asti. Ei Rasmuksen korjattava.

**H6 — `student/lesson-06/assessment.md` 💡 Vinkki ja `student/lesson-18/assessment.md` 💡 Vinkki.** Kumpikin toistaa viikkotehtävän vinkin lähes sanasta sanaan (2.3: "jos jokainen alitehtävä riippuu edellisestä…"; 6.2: "noin puolet ajasta bugi on jäljityksessä"). Ei uudelleenopetusta käsitteen tasolla, mutta lyhyempi viittaus ("muista tehtävän 2.3 vinkki: …") pitäisi punaisen langan siistimpänä.

**H7 — `student/lesson-06/assessment.md`, vaihe 6 + rubriikki K4 S+.** Reflektio on 3–5 virkettä, mutta siihen pyydetään: vaikein osatavoite, muutos numerolla, (jos LLM) hyväksytty haaste, hylätty haaste perusteluineen, (S+) epäselvyyden paikka. Sano "3–5 virkettä; LLM-virkkeet tulevat lisäksi", niin pituusrajaa ei rikota S+-yrityksessä.

**H8 — `teacher/lesson-18/rubric.md`, K3.** Rubriikki tunnistaa konegeneroidun taulukon ulkonäöstä. Todellinen tae on, että taulukot tehdään L18:n itsenäisessä jaksossa opettajan nähden; sano se S-solussa yhdellä sivulauseella ("tehty oppitunnin 18 itsenäisessä jaksossa"), jotta rubriikki ja assessment.md nojaavat samaan ankkuriin.

**H9 — `teacher/lesson-18/rubric.md`, K1 S.** Esimerkkilistassa "teen keitto" — kielivirhe, Börjen asia, kirjaan vain näkyviin.

---

## Pedagogiset löydökset

- Mikään AT ei ole copy-paste-LLM → submit. AT2 on kolmesta vahvin (käsin luokassa tehty jäljitys + rivinumerosidonta), AT3 toiseksi vahvin (ketju AT2 → oma pseudokoodi → ohjelma → live-puhe), AT1 ohuin arkisella polulla (ks. K6).
- AT:t eivät opeta uutta; ne kokoavat. Vaiheet ovat golden samplen tasolla: numeroituja, konkreettinen esimerkki ennen termiä, oma konteksti pakollinen. Sisällön määrä ei ole golden samplea ohuempi (773–798 sanaa / tiedosto).
- Kuorma: AT1 L6:n 30 minuutissa realistinen, jos viikon 2 tehtävät on tehty (K5 hoitaa poikkeuksen). AT2 L18:n 30 minuutissa realistinen vain, jos vaiheet 1–3 on tehty ennen tuntia ja kolmas jäljitys on valinnainen (K2, K3). AT3:n pohdinta on ylikuormitettu (K4).
- Rasmuksen tulkinta AT3 K1 S-:stä: perusteltu periaatteena, mutta ristiriidassa tehtävän 8.1 oman ohjeen ("muokkaa arvot") ja saman sarakkeen ES/S-solujen kanssa → B1.

## Punainen lanka

Ei uudelleenopetusta ilman viittausta. Osatehtäväviittaukset (2.1–2.5, 6.1–6.4 tiedostonumeroinnilla, 8.1-JS/CS, 8.2–8.5, L24-esitysohje) ovat id:ltään ja sisällöltään oikein: 2.2:n kolme kysymystä ja "osatehtävässä / osatavoitteessa / yhteydessä" -kysymys, 6.2:n neljä bugityyppiä, 6.3:n "vaikein rivi", 8.4:n pätkä B, 8.1:n vaiheet 2–6 ja neljä tarkistusta täsmäävät lähteisiin. Alitehtävä/osatehtävä-termiero on selitetty AT1:ssä. Kaksi lähes sanatarkkaa vinkkitoistoa (H6).

## Rubriikkien validius

- AT1: K1–K4 ↔ O6.1–O6.4 yksi yhteen. S+ erottuu laadullisesti K1, K2, K4:ssä. K3:n S-taso ei mittaa O6.3:n vapaa-osatehtävä-osaa (K1-korjaus). ES/S- havainnoitavia.
- AT2: K1–K5 ↔ O18.1–O18.5 yksi yhteen; viisi kriteeriä perusteltu. S+ laadullisesti eri taso kaikissa viidessä. S+ K5:n saavutettavuus yksin tekevälle tarkennettava (H2). ES/S- havainnoitavia; K3 ES:n "konegeneroitu" nojaa luokassa tekemiseen (H8).
- AT3: K1–K4 ↔ O24.1–O24.4 yksi yhteen. K2 ja K4 erottelevat aidosti. K3 S+ riippuu toisen bugin sattumisesta (H3). K1 on varamallipolulla sisäisesti ristiriitainen (B1). H14-virke taulukon jälkeen on paikallaan.

## Korjausvaatimukset Rasmukselle

1. `teacher/lesson-24/rubric.md` K1 ES/S-/S + `student/lesson-24/assessment.md` vaihe 1 ja viittausosio: määrittele varamallipolku niin, että sama palautus osuu yhteen soluun ja O24.1 on mitattavissa (B1).
2. `teacher/lesson-06/rubric.md` K3 S ja S+: vapaa osatehtävä S-tasolle, kaksi riippuvuutta + perustelu S+:aan (K1).
3. `student/lesson-18/assessment.md` vaihe 5: korjatun version uudelleenjäljitys valinnaiseksi/arvoa nostavaksi (K2); Tavoite + viittausosio + vaiheet 1–3: 6.1:n taulukot ovat harjoitus, AT2:n taulukot tehdään L18:lla, vaiheet 1–3 ennen tuntia (K3).
4. `student/lesson-24/assessment.md` Kirjallinen osa kohta 4 + vaihe 6: pohdinnan kuorma — 5–8 virkettä tai erilliset yhden rivin merkinnät (K4).
5. `student/lesson-06/assessment.md` vaihe 1: polku opiskelijalle, jolla ei ole viikon 2 pilkkomista (K5); "Mitä palautat": parin kolme kysymystä palautukseen + rubriikin K4 S sidotaan niihin (K6).
6. Huomiot H1–H3, H6–H8 harkinnan mukaan samalla kierroksella; H5 ja H9 eivät ole Rasmuksen.

## AI-resilienssin tila

Arvioitavat (ehdoton kynnys):
- **AT1 — riittävä, ohuin.** Ankkurit: oma todellinen tehtävä (2.4-polulla opettajan tarkistettavat valikkonimet), luokassa tehty parikatselmointi, muutos osatehtävän numerolla. Heikkous: arkisella polulla artefakti on kotona generoitavissa ja parikatselmoinnista ei jää jälkeä palautukseen → K6 vahvistaa.
- **AT2 — vahva.** Käsin luokassa tehdyt taulukot, oma hankala syöte, rivinumero sidottu palautettuun pseudokoodiin. Pseudokoodi voi olla LLM:n, mutta jäljitys osoittaa oman suorituskyvyn.
- **AT3 — vahva.** Oma pseudokoodi verrataan AT2:een, oma ympäristö, oma virheilmoitus, live-puhe + vertaishavainto + jatkokysymys. S-tasolla ulkoa opeteltu esitys läpäisee; S+ erottelee ymmärryksen puheesta. Varamallipolku on heikoin ja juuri siinä rubriikki ei toimi (B1).

Harjoitustehtäviä ei tässä ajossa auditoitu (eivät kuulu laajuuteen).

## Seuraava

palauta Rasmukselle korjattavaksi
