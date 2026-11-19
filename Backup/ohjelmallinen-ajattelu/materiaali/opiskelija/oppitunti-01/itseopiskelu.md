# Tietokoneelle puhuminen — mitä se oikeasti kuulee?

## Johdanto

Pyydät kaveriltasi: "Hae mun laturi keittiön pöydältä." Kaveri kävelee keittiöön, näkee pöydällä kolme laturia, poimii väärän ja tuo sen sinulle. Huokaiset ja selität, kumpi se oli. Kaveri kuunteli kyllä; ohje vain ei ollut tarpeeksi täsmällinen. Kuvittele nyt sama tilanne tietokoneen kanssa — paitsi että tietokone ei voi huokaista eikä arvata. Se vain tekee sen, mitä kirjoitit.

Tästä kysymyksestä koko kurssi pyörii: **Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?** Kuulostaa yksinkertaiselta. Ei ole. Suurin osa ohjelmoinnin, selkeän tiketin kirjoittamisen ja jopa hyvien ohjeiden antamisen vaikeudesta tulee yhdestä asiasta: tietokone lukee sen, mitä kirjoitit, ei sitä, mitä tarkoitit.

Tämän oppitunnin jälkeen pystyt määrittelemään ohjelmallisen ajattelun omin sanoin. Pystyt selittämään, mitä tarkoittaa että tietokone "ottaa sinut sananmukaisesti". Pystyt antamaan arkiesimerkin ja ICT-esimerkin tilanteesta, jossa ohje menee pieleen monitulkintaisuuden takia, ja näet että vika on ohjeessa, ei koneessa.

## Mitä ohjelmallinen ajattelu on?

Ohjelmallinen ajattelu on tapa ajatella ongelmia siten, että tietokone — tai kuka tahansa, joka noudattaa ohjeita sananmukaisesti — voi ratkaista ne. Se on se ajattelu, joka tapahtuu *ennen* ohjelmointia. Se on se osa, jonka teet ennen kuin kosket koodiin. Kun leipuri kirjoittaa reseptin niin, että aloittelija voi noudattaa sitä kysymättä mitään, leipuri tekee ohjelmallista ajattelua. Kun help desk -työntekijä kirjoittaa selkeän tiketin niin, että toisella aikavyöhykkeellä oleva kollega voi korjata ongelman ilman palaveria, sekin on ohjelmallista ajattelua.

Alaa tutkivat ihmiset puhuvat usein ohjelmallisen ajattelun neljästä "pilarista": ositus, mallien tunnistaminen, abstraktio ja algoritmit. Jokainen näistä saa myöhemmin oman oppituntinsa kurssilla, joten älä yritä opetella niitä ulkoa nyt. Oppitunnilla 1 vain yksi ajatus on tärkeä: tietokone tekee sen, mitä ohjeesi todella sanoo.

> **Pysähdy hetkeksi:** Mieti jotain ohjetta, jonka annoit tänään — kaverille, sisarukselle, opettajalle, chat-botille. Tekikö toinen tarkalleen sen, mitä tarkoitit? Jos ei, oliko ongelma hänen päässään vai sinun sanoissasi?

## Tietokone ottaa sinut sananmukaisesti

Kuvittele, että sanot pikkuveljellesi: "Tee mulle voileipä. Laita juusto kahden leipäpalan väliin." Hän tuo takaisin kaksi leipäpalaa, jotka makaavat juustopalan päällä. Hänen näkökulmastaan juusto on palojen välissä: yksi pala on juuston yllä, yksi alla. Sinä tarkoitit juuston sisälle, voileipätyyliin. Hän luki sanat juuri niin kuin ne olivat kirjoitettu.

Tai kuvittele, että annat vierailijalle reittiohjeet kaupunginkirjastoon. Sanot: "Käänny vasemmalle ison puun kohdalla." Sillä kadulla on kolme isoa puuta. Vierailija pysähtyy ensimmäisen kohdalla, kääntyy vasemmalle ja päätyy parkkipaikalle. Reittiohjeet eivät olleet tahallaan väärät. Ne olivat vain avoimet useammalle kuin yhdelle tulkinnalle.

Tietokone käyttäytyy aivan kuin tuo pikkuveli ja tuo vierailija — joka kerta, poikkeuksetta. Se ei voi valita "ilmeistä" tulkintaa, koska se ei tiedä, mikä tulkinta on sinulle ilmeinen. Se lukee ohjeen ja tekee sen asian.

Sama kuvio nousee esiin heti kun alat käyttää ICT-työkaluja. Kirjoitat hakukenttään `pyhton tutorial`, koska sinulla on kiire. Hakukone etsii sivuja, joissa esiintyy `pyhton`, löytää tuskin mitään hyödyllistä ja palauttaa ohuet hakutulokset — ehkä jopa kohteliaan "Tarkoititko: python tutorial?" -kysymyksen. Haku ei epäonnistunut; se teki tarkalleen sen, mitä pyysit. Kirjoitusvirhe oli sinun ohjeessasi.

Tai käsket ohjelmaa avaamaan tiedoston `report-final.docx`, ja ohjelma sanoo *tiedostoa ei löydy*. Tuijotat näyttöä varmana siitä, että tiedosto on siellä. Se onkin — mutta se on kansiossa, johon muistat siirtäneesi sen viime viikolla. Antamasi polku on väärä. Ohjelma ei valehtele. Se katsoi tarkalleen sinne, mihin osoitit, eikä siellä ollut tiedostoa.

> **Pysähdy hetkeksi:** Kun sovellus tekee "väärän asian", onko se rikki vai noudattiko se ohjettasi täsmälleen? Miten erottaisit nuo kaksi toisistaan?

## Monitulkintaisuus asuu ohjeessa, ei tietokoneessa

Moni sanoo, kun sovellus käyttäytyy ärsyttävällä tavalla: "tämä tietokone on niin tyhmä" tai "tällä vehkeellä ei oo mitään käsitystä siitä mitä mä haluan". Se on normaali reaktio. Se on myös väärä kuva siitä, mitä todella tapahtuu.

Tietokone ei ole tyhmä. Tietokone on *sananmukainen tulkitsija*. Ne ovat eri asioita. Tyhmä kuuntelija ei ymmärrä edes selkeää ohjetta. Sananmukainen tulkitsija ymmärtää ohjeen sanasta sanaan ja tekee tarkalleen sen, mitä sanat sanovat. Jos sanat voivat tarkoittaa kahta asiaa, sananmukainen tulkitsija valitsee toisen niistä — etkä aina pääse valitsemaan kummasta.

Tämä on oppitunnin käsitteellinen käännekohta, ja sen sanominen kannattaa hitaasti: kun tietokone "tekee väärän asian", bugi on lähes aina *ohjeessa*, ei *tulkitsijassa*. Monitulkintaisuus on ohjeen ominaisuus samalla tavalla kuin paino on reppusi ominaisuus. Reppu ei ole laiska siksi että se on raskas; se on raskas siksi mitä siihen laitoit.

Tämä uudelleenmuotoilu on tärkeä, koska se muuttaa sen, mitä teet seuraavaksi. Jos ajattelet että tietokone on tyhmä, ainoa siirto on valittaa. Jos hyväksyt, että ohje oli monitulkintainen, sinulla on uusi tehtävä: löytää se monitulkintainen kohta ja kirjoittaa se uudelleen. Tämä toinen siirto on se, mitä ICT-ammattilainen tekee päivisin — joskus koodissa, joskus tiketeissä, joskus viesteissä muille ihmisille.

## Miksi tämä on tärkeää ICT-ammattilaiselle

ICT-työssä kirjoitat ohjeita koko päivän, myös silloin kun et kirjoita koodia. Kirjoitat tikettejä kollegoille. Kirjoitat päivitysmuistioita loppukäyttäjille. Kirjoitat hakuja, kun debuggaat. Kirjoitat pieniä skriptejä, jotka automatisoivat tehtäviä. Jokainen niistä on ohje, jota joku — ihminen tai kone — noudattaa niin sananmukaisesti, että jokin menee pieleen, jos et ollut huolellinen.

Taito kirjoittaa ohje, jota ei voi lukea väärin, ei ole näyttävä, mutta se on taito, joka erottaa turhautuneen juniorin rauhallisesta seniorista. Senioritason ICT-ammattilaiset eivät kirjoita taikakoodia; he kirjoittavat ohjeita, joihin ei jää arvailun varaa. Mitä aikaisemmin alat harjoitella tätä, sitä halvemmaksi se tulee. Tämän kurssin loppuun mennessä olet harjoitellut sitä arkikielellä, prosessikuvauksissa, pseudokoodissa ja lopulta JavaScriptissä. Ajattelu on samaa joka kerroksessa.

## Yhteenveto

Tämä oppitunti pohjusti kysymyksen, jonka ympärille koko kurssi on rakennettu: *Miten puhun tietokoneelle niin, että se ymmärtää mitä haluan sen tekevän?* Näit, että tietokone lukee ohjeita sananmukaisesti — kuten sisarus, joka tekee "voileivän" niin että leipä on ulkopuolella, tai hakukone, joka palauttaa mitään hyödyllistä haulle `pyhton tutorial`. Näit myös oppitunnin tärkeimmän uudelleenmuotoilun: kun jokin menee pieleen, monitulkintaisuus on lähes aina ohjeessa, ei tietokoneessa. Se on hyvä uutinen, koska ohjeet ovat jotain mitä voit kirjoittaa uudelleen.

Seuraavalla oppitunnilla tutustut sanaan *algoritmi*. Algoritmi on vain selkeä sarja sananmukaisia vaiheita, jotka saavat työn tehdyksi — ja olet jo kirjoitellut niitä tänään kutsumatta niitä siksi.
