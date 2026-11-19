# Oppitunti 7 — Vuokaavion läpikäynti

Yhden arjen vuokaavion muoto-kerrallaan -rakentaminen.

Käytä vain, jos luokka tarvitsee hitaan rakentamisen; ohita, jos live-piirros taululla toimii hyvin.

---

## Kalvo 1 — Alku

```
( Alku )
```

Jokainen vuokaavio alkaa täsmälleen yhdellä Alku-soikiolla. Se kertoo, mistä prosessi avautuu.

Tämän päivän esimerkissä prosessi on *"päätä, otatko sateenvarjon mukaan tänä aamuna"*.

---

## Kalvo 2 — Ensimmäinen vaihe

```
( Alku )
   |
   v
[ Tarkista sääennuste ]
```

Yksi suorakulmio. Yksi toiminto. *"Tarkista sääennuste"* on yksi vaihe, jonka tulkitsija tekee.

Huomaa, ettei siinä sanota, *miten* ennuste tarkistetaan — tuo yksityiskohta on piilotettuna laatikon sisällä.

---

## Kalvo 3 — Päätös

```
( Alku )
   |
   v
[ Tarkista sääennuste ]
   |
   v
< Onko sadetodennäköisyys > 50 % ? >
   /                            \
  Kyllä                          Ei
```

Vinoneliö sisältää yhden kyllä/ei-kysymyksen. Siitä lähtee kaksi nuolta — yksi kumpaakin vastausta varten. Jokaisella nuolella on oma lyhyt merkintänsä.

Tämä on se hetki, jolloin tasainen lista ei pärjää — prosessi haarautuu.

---

## Kalvo 4 — Molemmat haarat

```
< Onko sadetodennäköisyys > 50 % ? >
   /                            \
  Kyllä                          Ei
   |                              |
   v                              v
[ Ota sateenvarjo ]      [ Jätä sateenvarjo ovelle ]
```

Jokainen haara kantaa omat suorakulmionsa. Kyllä-polku tekee yhden asian; Ei-polku tekee toisen. Molemmat haarat ovat rehellisiä siitä, mitä tulkitsija oikeasti tekee kummassakin tapauksessa.

---

## Kalvo 5 — Vuokaavion sulkeminen

```
( Alku )
   |
   v
[ Tarkista sääennuste ]
   |
   v
< Onko sadetodennäköisyys > 50 % ? >
   /                            \
  Kyllä                          Ei
   |                              |
   v                              v
[ Ota sateenvarjo ]      [ Jätä sateenvarjo ovelle ]
   \                              /
    \                            /
     v                          v
        ( Lähde kotoa )
```

Molemmat polut yhtyvät Loppu-soikioon. Jokaisen polun vuokaavion läpi on päädyttävä Loppu-soikioon.

Yhteensä kahdeksan muotoa. Yksi Alku, yksi Loppu, kolme suorakulmiota, yksi vinoneliö. Koko sateenvarjoprosessi yhdellä sivulla.

---

## Kalvo 6 — Sama muoto, ICT-esimerkki

Samat viisi muotoa; eri konteksti.

- Alku → *"Lue tiketin teksti"* → *"Pääseekö käyttäjä nyt kirjautumaan?"*
  - Kyllä → *"Sulje tiketti"* → Loppu (Suljettu)
  - Ei → *"Pyydä käyttäjältä kuvakaappaus"* → Loppu (Odota vastausta)

Vuokaavion neljä muotoa kantavat ICT-prosessia yhtä siististi kuin sateenvarjoprosessia. Sama kuvan sanasto; uusi yleisö.
