# AT2 — arvioitava tehtävä: Pseudokoodi ja jäljitys omasta prosessista

## Tavoite

Tehtävässä 6.1 kirjoitit pseudokoodin prosessista, jonka kätesi jo osaavat, ja kävit sen paperilla läpi kahdesti. AT2 pyytää samaa työtä, eikä mitään uutta tarvitse opetella. Pseudokoodisi kelpaa sellaisenaan. Tehtävän 6.1 jäljitykset olivat kuitenkin harjoitus: AT2:n kaksi taulukkoa teet uudelleen käsin luokassa oppitunnilla 18, koska ne ovat testi. AT2 on kurssin toinen arvioitava tehtävä, ja se kokoaa viikon 6: pseudokoodin, jäljityksen ja selityksen yleiskielellä. Tehtävä näyttää, osaatko kirjoittaa pienen prosessin kurssin avainsanoilla niin, että kirjaimellinen suorittaja voi seurata sitä, ja osaatko itse olla se suorittaja jäljitystaulukon avulla. Oikeaa ohjelmointikieltä ei käytetä; paperi ja kynä riittävät, ja jäljityksessä ne ovat vaatimus.

## Mitä palautat ja milloin

Palautat kolme osaa, jotka voi palauttaa yhtenä nippuna.

1. Pseudokoodi, 10–20 riviä, kurssin avainsanoilla (SET, READ, WRITE, IF/ELSE/ENDIF, WHILE/ENDWHILE, FOR/ENDFOR). Mukana on vähintään yksi ehto ja vähintään yksi toisto, ja lohkot on sisennetty. Prosessi on oma arkiprosessisi, ei oppikirjaesimerkki.
2. Kaksi käsin tehtyä jäljitystaulukkoa: yksi normaalilla syötteellä ja yksi hankalalla syötteellä. Taulukossa on yksi sarake jokaiselle muuttujalle, yksi sarake tulosteelle ja yksi rivi jokaiselle suoritetulle riville. Palautat taulukot paperilla tai valokuvana paperista; molemmat kelpaavat.
3. Reflektio, 5 virkettä yleiskielellä, jossa on yksi rivinumero: rivi, jolla toteutunut tuloste erosi odotetusta ensimmäisen kerran, tai rivi, jolla hankala syöte käsiteltiin oikein.

Palautus on noin oppitunnilla 18. Vaiheet 1–3 teet ennen oppituntia 18, jäljitykset teet oppitunnin 18 itsenäisessä jaksossa, ja nippu luovutetaan tunnin lopussa opettajan ilmoittamalla tavalla.

## Vaiheet

1. Ota esiin tehtävän 6.1 pseudokoodisi ennen oppituntia 18. Vaiheet 1–3 ovat kotityötä, jotta tunnin 30 minuutin itsenäinen jakso riittää kahteen jäljitykseen. Jos et tehnyt tehtävää 6.1, kirjoita uusi pseudokoodi samoilla säännöillä prosessista, jota teet lähes joka päivä, esimerkiksi puhelimen lataamisesta yön yli.
2. Tarkista pseudokoodi tehtävän 6.1 vaiheen 3 silmin. Avainsanat ovat isoilla kirjaimilla, lohkojen sisältö on sisennetty ja jokainen muuttuja on nimetty niin, että nimi kertoo sisällön. Nimi `teekuppienMaara` kertoo lukijalle, mitä lasketaan; nimi `x` ei kerro. Numeroi rivit marginaaliin, koska reflektiossa viittaat rivinumeroon.
3. Valitse hankala syöte omasta prosessistasi. Se on poikkeustilanne, jonka prosessi voi oikeasti kohdata: akku on jo 100 prosentissa, repussa ei ole yhtään kirjaa, teepurkki on tyhjä. Kirjoita hankala syöte valmiiksi pseudokoodin alle, niin tunnilla jäljitys alkaa heti.
4. Jäljitä pseudokoodi käsin kahdesti oppitunnin 18 itsenäisessä jaksossa, ensin normaalilla ja sitten hankalalla syötteellä. Etene rivi riviltä ja kirjoita jokaiselle suoritetulle riville oma rivi taulukkoon. Älä ohita WHILE-ehdon uudelleentarkistusta silmukan lopussa: jos ehto tarkistetaan viisi kertaa, taulukossa on viisi riviä sitä varten.
5. Vertaa hankalan syötteen jäljitystä siihen, mitä halusit prosessin tekevän. Jos ne eroavat, ympyröi ensimmäinen rivi, jolla ero syntyi, ja nimeä bugi tehtävän 6.2 neljällä tyypillä: off-by-one-virhe, väärä vertailu, puuttuva alustaminen tai väärä haara. Korjaa pseudokoodi ja merkitse korjattu rivi näkyviin. Jos ehdit, jäljitä korjattu versio uudella taulukolla; se ei ole pakollista, mutta nostaa arviota. Jos hankala syöte toimi oikein, kirjoita ylös rivinumero, jolla poikkeustilanne käsiteltiin, ja perustele jäljityksellä, miksi se riitti.
6. Kirjoita reflektio, 5 virkettä yleiskielellä. Kerro, mitä pseudokoodisi tekee, mikä oli pseudokoodilla vaikeampaa tai helpompaa kuin tavallisella kielellä, ja mitä jäljitys paljasti sellaista, mitä pelkkä lukeminen ei paljastanut. Yksi virke sisältää rivinumeron vaiheesta 5. Jos käytit LLM:ää tehtävän 6.4 tapaan, kerro, missä kohtaa oma ja LLM:n jäljitys erosivat ja kumpi oli oikeassa, kun jäljitit uudelleen.
7. Luovuta nippu tunnin lopussa. Reflektion saat kirjoittaa itsenäisen jakson jälkeen ennen luovutusta. Tarkista, että reflektion rivinumero löytyy palautetusta pseudokoodista.

💡 Vinkki: Muista tehtävän 6.2 vinkki: kun tulosteet eroavat, jäljitä ensin uudelleen puhtaalle sivulle ennen kuin kosket pseudokoodiin. Jos bugi olikin jäljityksessä, sekin on arvokas havainto reflektioon.

## Mihin viikon tehtäviin tämä nojaa

Tehtävä 6.1 on täysimittainen AT2-harjoitus: siinä tekemäsi pseudokoodi on AT2:n pseudokoodi, ja sen kaksi jäljitystä ovat harjoitus, jonka toistat luokassa oppitunnilla 18 arvioitavana versiona. Tehtävä 6.2 opetti nimeämään bugin neljällä tyypillä ja jäljittämään korjatun version; sama liike on AT2:n vaihe 5. Tehtävä 6.3 antoi sinulle ulkopuolisen lukijan, jonka havainto vaikeimmasta rivistä sopii reflektioon. Tehtävä 6.4 on valinnainen LLM-sparraus; jos teit sen, erimielisyys LLM:n kanssa ja sen ratkaisu kuuluvat reflektioosi.

## Jos teet tämän yksin

Perussuoritus ei tarvitse paria, koska kaksi jäljitystäsi ovat testi. Jos haluat tehtävän 6.3 ulkopuolisen lukijan tilalle toisen silmäparin, tee se ennen oppituntia 18 harjoituksena: kirjoita pseudokoodi tänään ja jäljitä se huomenna lukematta omaa pohdintaasi, tai jäljitä kerran puhelimen muistiinpanoihin ja seuraavana päivänä paperille. Päivän vanha sinä kelpaa ulkopuoliseksi lukijaksi reflektiossa. Arvioitavat taulukot teet silti käsin luokassa.

## Arviointikohteet

- **Pseudokoodin rakenne** — arvioija katsoo, onko pseudokoodissa 10–20 riviä, kurssin avainsanat, vähintään yksi ehto ja yksi toisto, ja onko prosessi oma arkiprosessisi.
- **Muuttujien nimeäminen** — arvioija katsoo, kertooko jokaisen muuttujan nimi, mitä arvoa se sisältää.
- **Jäljitystaulukot** — arvioija katsoo, onko kaksi käsin tehtyä taulukkoa, normaali ja hankala syöte, sarake per muuttuja ja rivi per suoritettu rivi.
- **Bugin paikantaminen ja korjaus** — arvioija katsoo, nimeätkö rivinumeron, bugityypin ja korjauksen, tai perusteletko jäljityksellä, että hankala syöte toimi.
- **Reflektio yleiskielellä** — arvioija katsoo, kertooko viisi virkettä, mitä pseudokoodi tekee ja mitä jäljitys paljasti.
