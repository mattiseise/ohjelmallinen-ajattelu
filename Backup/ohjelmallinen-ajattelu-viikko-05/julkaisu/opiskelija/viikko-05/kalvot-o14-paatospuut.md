# Päätöspuut — yksi puu päästä päähän

Oppituntiin 14 liittyvä lisäkalvosarja.

Käy yksi arkinen päätöspuu rauhassa läpi, ja katso sitten sama muoto ICT-ympäristössä.

---

## Arkinen sääntö

*"Pitäisikö minun ottaa sateenvarjo tänään?"*

Sääntö yhdellä suullisella lauseella:

> Jos juuri nyt sataa, kyllä.
> Jos juuri nyt ei sada, mutta ennuste lupaa sadetta, kyllä.
> Muutoin ei.

---

## Piirrä puu — haarat ja testit

```
            Sataako nyt?
              /          \
            kyllä           ei
            /                \
       ota sateenvarjo    Lupaako ennuste
                             sadetta?
                          /         \
                        kyllä          ei
                        /              \
                  ota sateenvarjo   jätä kotiin
```

Juurikysymys huipulle. Kaksi testiä, kolme lehteä. Jokainen testi on jotain, jonka pystyt oikeasti tarkistamaan.

---

## Ilmaise sääntö rentona if … then …

- **if** *sataa juuri nyt*, **then** *ota sateenvarjo*
- **else if** *ennuste lupaa sadetta*, **then** *ota sateenvarjo*
- **else** *jätä kotiin*

Sama sääntö, kirjoitettuna englanninkielisenä lyhennemerkintänä. Ei koodia — vain asettelu, joka helpottaa testin ja toiminnan näkemistä.

---

## ICT-peilikuva — pitäisikö tämä kirjautumisyritys estää?

Sääntö yhdellä suullisella lauseella:

> Jos salasana on väärä ja se on jo neljäs yritys viiden minuutin sisällä, estä tili.
> Jos salasana on väärä mutta yrityksiä on ollut alle 4, pyydä käyttäjää yrittämään uudelleen.
> Jos salasana on oikea, kirjaudu sisään.

---

## Sama puu, eri ympäristö

```
              Onko salasana oikea?
                /              \
              kyllä              ei
              /                    \
          kirjaudu sisään   Onko käyttäjä yrittänyt
                            4+ kertaa 5 min sisällä?
                              /          \
                            kyllä           ei
                            /                \
                       estä tili       pyydä yrittämään uudelleen
```

Kolme haaraa. Kaksi testiä. Sama muoto kuin sateenvarjopuulla — eri testit, eri lehdet.

---

## Testin nimeäminen rehellisesti

Päätöspuun laatu on sen haarojen testien laatu.

- Rehellinen: *"Sataako nyt?"*, *"Onko yrityksiä ollut 4+ viiden minuutin sisällä?"*
- Ei vielä rehellinen: *"Sataako jossain vaiheessa?"*, *"Onko käyttäjä epäilyttävä?"*

Jos testi on epämääräinen, tulkitsijan on arvattava — ja puu lakkaa olemasta hyödyllinen.

Vie kotiin: kun piirrät puun tällä viikolla, hio jokaista haaraa, kunnes testi on jotain, mitä sananmukainen tulkitsija pystyy tarkistamaan.
