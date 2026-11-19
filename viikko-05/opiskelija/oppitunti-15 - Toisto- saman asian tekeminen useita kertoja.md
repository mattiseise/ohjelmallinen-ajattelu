# Oppitunti 15 — Toisto: saman asian tekeminen useita kertoja

### Mitä toisto tarkoittaa?

Toisto tarkoittaa saman vaiheen tai saman vaiheryhmän tekemistä useammin kuin kerran
niin, että mukana on pysäytysehto, joka kertoo suorittajalle, milloin pitää lopettaa. Teknologian
arkikielessä tästä puhutaan usein myös silmukkana (loop), mutta tällä kurssilla käytämme
enimmäkseen sanaa toisto.
Järjestys on suora viiva. Ehto on haara. Toisto on ympyrä, jolla on myös rehellinen uloskäynti.
Jos uloskäynti puuttuu, suorittaja kiertää ikuisesti — syntyy karkaava toisto. Palaamme
siihen aivan kohta.

### Arkisia toistoja, joita käytät jo

Teet näitä koko ajan, aivan kuten ehtoja, yleensä nimeämättä niitä.
• “Merkitse jokainen nimi läsnäolevaksi tai poissaolevaksi.” Teet saman pienen toiminnon
jokaiselle nimelle ja lopetat, kun lista loppuu.
• “Lisää sokeria ja sekoita, kunnes maku on oikea.” Teet saman toiminnon uudelleen ja
lopetat, kun testi “maku on oikea” palautuu todeksi.
• “Niin kauan kuin vedenkeitin on yhä kuuma, älä keitä sitä uudelleen.” Tarkistat ehdon
ennen jokaista kierrosta; niin kauan kuin se on tosi, jatkat.

### Kolme toiston perusmuotoa

Kolme arkista muotoa riittää melkein jokaiseen toistoon, jonka kirjoitat tavallisella kielellä.
• Jokaiselle — jokaiselle listan kohteelle tee …
Käytä silloin, kun lista on tiedossa etukäteen. Pysäytysehto on listan loppuminen.
Esimerkki: jokaiselle nimelle luettelossa merkitse läsnä tai poissa.
• Toista kunnes — tee … kunnes pysäytysehto on tosi
Käytä silloin, kun lopettaminen riippuu siitä, mitä toiston aikana tapahtuu.
Esimerkki: sekoita kunnes sokeri liukenee.
• Niin kauan kuin ( ) — niin kauan kuin ehto on tosi, tee … `while`
Käytä silloin, kun testi tarkistetaan ennen jokaista kierrosta.
Esimerkki: niin kauan kuin vedenkeitin on kuuma, älä keitä sitä uudelleen.
Sinun ei tarvitse opetella näitä kuin sanalistaa. Ne ovat kolme rytmiä, joista valitset
tilanteeseen sopivan. Kaikissa tärkeintä on sama:

pysäytyksen täytyy olla todellinen, ja suorittajan täytyy pystyä havaitsemaan se.

### Pysäytysehto on turvavyö

Vertaa kahta lausetta:
• “Jokaiselle viikonlopun kuvalle puhelimessa päätä, säilytätkö sen.”
Rehellinen pysäytys: viikonlopun kuvien lista on rajallinen, joten kuvat loppuvat.
• “Työskentele sen parissa, kunnes ymmärrät.”
Ei rehellinen pysäytys. Ymmärtäminen ei ole havaittava testi. Suorittaja saattaa jatkaa
loputtomiin — tai luovuttaa satunnaisesti.
Jokainen toisto tarvitsee lopun, jonka suorittaja voi havaita. “Kunnes saapuneet-kansio on
tyhjä” on havaittava. “Kunnes paikka vapautuu” on havaittava. “Kunnes tunnet olevasi valmis”
ei ole — ellei sitä muuteta tarkistettavaksi muodoksi, esimerkiksi “kunnes pystyt selittämään
asian luokkakaverille yhdellä lauseella” tai “kunnes vastaat kolmeen harjoituskysymykseen
peräkkäin oikein”.
Kun toistolla ei ole rehellistä pysäytystä, sinulla on karkaava toisto. Korjaus on lähes aina
sama: lisää turvapysäytys tavallisella kielellä.
Esimerkiksi:
“Toista, kunnes sivu latautuu — tai lopeta 30 sekunnin jälkeen ja yritä myöhemmin uudelleen.”
Turvapysäytys on toiston turvavyö.
Pysähdy hetkeksi: Nimeä yksi asia, jonka teit tänään ja joka oli toisto. Mikä oli
pysäytysehto? Oliko se oikeasti havaittava, vai lopetitko vain siksi, että “tuntui
valmiilta”?
Pysähdy hetkeksi: Kuvittele “toista kunnes …” -muoto, jossa loppua ei voi oikeasti
havaita. Kirjoita se ylös. Lisää sitten turvapysäytys, joka pelastaisi sen. Mitä jouduit
muuttamaan?

### Laskurit — kun pysäytys on määrä

Joskus pysäytys on pelkkä lukumäärä. “Tee kaksikymmentä punnerrusta.” “Toista kertosäe
kolme kertaa.” Teet sisäisen vaiheen, pidät kirjaa siitä, montako kertaa olet tehnyt sen, ja
lopetat, kun saavutat luvun.
Laskuri on tavallaan erityistapaus muodosta jokaiselle:
“tee 20 punnerrusta” = “jokaiselle luvulle 1:stä 20:een tee yksi punnerrus.”
Et tarvitse tähän mitään erityistä syntaksia. Riittää, että määrä on rehellinen.
“Toista, kunnes olet tehnyt tarpeeksi” ei ole laskuri.
“Toista 20 kertaa” on.

### Kaikki kolme yhdessä — oikea prosessi

Suurin osa todellisista prosesseista näyttää tältä: järjestys, jonka sisällä on ehto, jonka sisällä on
toisto — tai toisto, jonka sisällä on ehto, jonka sisällä on pieni järjestys. Juuri kolmen
rakennuspalikan erikseen nimeäminen tekee kuvauksesta luettavan.
Ajattele saapuneet-kansion läpikäyntiä:
1. Avaa sähköposti.
2. Käy viestit läpi järjestyksessä.
3. Jos viesti vaatii vastauksen, niin vastaa tai merkitse se tehtäväksi.
4. Jos viesti on vain tiedoksi, niin arkistoi se.
5. Toista tämä jokaiselle viestille, kunnes saapuneet-kansio on tyhjä.
Ilman rakennuspalikoiden nimiä tämä olisi vain kappale, joka sanoo “käy sähköpostit läpi”.
Nimien kanssa siitä tulee prosessi, jonka kirjaimellinen suorittaja pystyy seuraamaan.
Ajattele näin: hyvä toisto ei kerro vain mitä tehdään uudelleen, vaan myös mistä tiedetään,
että ollaan valmiita.
