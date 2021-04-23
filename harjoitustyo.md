---
layout: default
title: Harjoitustyöohje / JODA 2021
year: 2021
---

**Ohje viimeistellään ensimmäisten luentoviikkojen aikana.** Ilmoita epäjohdonmukaisuuksista Jukalle, vaikka Slack-kanavalla.

Johdanto datatieteeseen -harjoitustyössä käydään läpi datatiedeprojektin keskeiset vaiheet. Voit valita aiheen ja datalähteen vapaasti.
Saat pisteitä julkaisemalla Slackissa kuvauksen [harjoitustyön eri vaiheiden](https://jodatut.github.io/2021/harjoitustyo/) toteutuksesta.
Eräs vaihtoehto on Airbnb-aineiston analyysi datatieteen menetelmin.
Voit vaikkapa toteuttaa hintaennustimen [esimerkkianalyysiä](https://github.com/InfoTUNI/joda2021/blob/master/koodiesimerkit/airnbn/python_scikit_airbnb.ipynb) soveltamalla.

## Vaiheet ja pisteet

| Vaihe  | 1 piste  | 2 pistettä   | 3 pistettä  |
|--------|---|---|---|
| Kehitysympäristö   | [CSC Notebooks](https://www.csc.fi/web/blog/post/-/blogs/notebooks-enemman-aikaa-opetuksen-ytimelle) | Anaconda omalla koneella | Oma pilviympäristö |
| Datan kerääminen   | Valmis datasetti         | Datasettien yhdistely | Oma datasetti |   
| Datan jalostaminen | Siistiä lähtödataa       | Siivoaminen ja piirteiden erottaminen | Web DAD |   
| Datan kuvaileminen | Standardikuvaajat        | Monipuolinen visuaalinen raportti | Vuorovaikutteinen Web-kojelauta |   
| Koneoppiminen      | Lineaarinen regressio    | Monimuuttujaregressio | Hybriditoteutus |   
| Toimeenpano        | Staattinen raportti      | Vuorovaikutteinen raportti  | Ohjaava analytiikka |  

**Kehitysympäristö**
Perusta kehitysympäristö projektiasi varten.
CSC Notebooks -palvelun käyttäminen mahdollistaa Jupyterin opettelun.
Google Colabin hyödyntäminen on suoraviivaisin vaihtoehto. Vaihtoehtoisesti voit asentaa koneellesi Anacondan tai pelkän Jupyterin.
Voit myös rakentaa oman pilvipalvelupohjaisen analytiikkaympäristösi.
Esimerkiksi [Google Cloud Platform](https://cloud.google.com/) viimeksi mainittuun kategoriaan.

**Datan kerääminen**
Suoraviivaisinta on lähteä liikkeelle valmiista datasta.
Ehdotamme [Inside Airbnb](http://insideairbnb.com/) -datasetin käyttöä.
Analytiikkavälineet tarjoavat myös puhdasta esimerkkidataa, katso vaikkapa
[Kagglen tarjonta](https://www.kaggle.com/datasets).
Datasettien yhdistely tuo mukanaan lisähaastetta.
Voit myös kerätä oman datasetin Web-ryöminnän, ruudunraavinnan tai API-ohjelmoinnin keinoin.

**Datan jalostaminen**
Analyysi edellyttää aina datan jalostamista ja siivoamista.
Piirteiden erottaminen on keskeisessä roolissa tätä vaihetta.
Siistissä datassa piirteet ovat pääosin valmiina,
mutta usein niiden erottaminen edellyttää lisätyötä.
[Web DAD](https://www.datasciencecentral.com/profiles/blogs/data-scientist-versus-data-engineer)
viittaa tässä itse kerätyn datan jalostamiseen analyysiä varten.

**Datan kuvaileminen**
Datan kartoittava (eksploratiivinen) ja kuvaileva (deskriptiivinen) analyysi on välttämätöntä analytiikkaprojektin laadun takaamiseksi.
Toteuta minimissään joukko datan ominaisuuksia kuvaavia visualisointeja.
Pandas tarjoaa kätevät apuvälineet aikajanoista pistekaaviomatriiseihin.
Halutessasi voit hyödyntää Web-ohjelmointiosaamistasi ja
toteuttaa monipuolisen visuaalisen raportin tai
vuorovaikutteisen Web-kojelaudan esimerkiksi [Streamlitillä](https://streamlit.io/).

**Koneoppiminen**
Kahden muuttujan välistä suhdetta tarkasteleva lineaarinen regressio on
yksinkertaisin koneoppimismenetelmä.
Voit vaikkapa etsiä Airbnb-asunnon hintaa parhaiten selittävät muuttujat.
Monimuuttujaregressio mahdollistaa esimerkiksi
[Airbnb-asunnon hinnan ennustamisen](https://github.com/InfoTUNI/joda2021/blob/master/koodiesimerkit/airnbn/python_scikit_airbnb.ipynb).
Käytännön sovellukset ovat tyypillisesti useita eri menetelmiä yhdisteleviä hybridejä.

**Toimeenpano**
Datatiedeprojekti tähtää toimenpiteisiin.
Voit esimerkiksi ehdottaa liiketoimintaan liittyviä toimenpiteitä
(kuvitteelliselle tai todelliselle) kohdehenkilölle.
Miten Airbnb-asuntojen sijaintia voisi hyödyntää kahvilaketjun toimipisteiden valinnassa?
Miten Airbnb-asunnosta olisi mahdollista saada nykyistä parempi päivähinta?
Staattinen raportti voi olla tekstiä ja kuvia yhdistelevä tuotos.
Vuorovaikutteisen raportin avulla käyttäjä voi myös itse perehtyä tekemääsi analyysiin.
Suosittelujärjestelmä tai Airbnb-asunnon hinnan arviointi käyttäjän syöttämien ominaisuuksien perusteella määrittelevä sovellus (vrt. [blok.ai](https://blok.ai/asunnon-hinta-arvio/)) ovat esimerkkejä ohjaavasta analytiikasta.

<a name="tasmennys-vuorovaikutteisuus"></a> **Täsmennys 23.4.2021** Datan kuvaileminen -vaiheen kohta Vuorovaikutteinen Web-kojelauta ja Toimeenpano-vaiheen Vuorovaikutteinen raportti edellyttävät molemmat *loppukäyttäjälle* tarkoitetun “sovelluksen” kehittämistä. Esimerkiksi [Streamlit.io](https://streamlit.io/) tarjoaa varsin näppärät välineet moisen sovelluksen toteuttamiseen.
Jupyter Notebook -pohjainen ratkaisu on ok, jos se on mietitty kokonaisuudessaan loppukäyttäjän sovellukseksi. Sovelluksessa syöte annetaan  lomakekomponenteilla ja visualisoinnit on toteutettu  vuorovaikutteisena esimerkiksi D3.js- tai vastaavalla kirjastolla, joka mahdollistavat esimerkiksi aineiston järjestämisen ja suodattamisen. Vrt. [Analyzing Your Goodreads Reading Habits](https://share.streamlit.io/tylerjrichards/streamlit_goodreads_app/books.py) tai [DC.js](https://dc-js.github.io/dc.js/).

## Pisteiden kerääminen

Pisteiden kerääminen tapahtuu julkaisemalla kunkin vaiheen kuvaus
toteutuskerran Slackissä **torstaihin 29.4 kello 17 mennessä**.
Pisteet myönnetään täysimääräisenä kun minimivaatimukset täyttyvät ja
palautus on tehty annetun aikataulun puitteissa.

Aihepiiriin jo ennen toteutuskerran alkua perehtyneitä suorittajia kannustetaan toteuttamaan etenkin **ensimmäiset vaiheet annettua aikataulua rivakammin** ja siten jakamaan osaamistaan muille.
Erityisen informatiiviset palautukset huomioidaan kokonaissuoritusta arvosteltaessa.

Yhden vaiheen kuvaus sisältää seuraavat pääkohdat:

1. tiivis kuvaus toteutuksesta,
1. muutamia otteita toteutuksesta (ohjelmakoodista, asetustiedostoista, ...),
1. listaus (siis lista linkkejä) ohjeista tai esimerkiksi verkkolähteistä jotka olivat erityisesti hyödyksi tehtävää tehdessä ja
1. listaus vähintään kolmesta asiasta, jotka olivat valitulla teknologialla joko erityisen helppoja tai vastaavasti hankaloittivat työtäsi merkittävästi.

Kun viesti on valmis, julkaise se Slackissä.
Halutessasi voit kirjoittaa kuvauksen esimerkiksi dillinger.io-palvelulla ja liittää sen Slackiin-viestiin PDF-muodossa.
Löydät Slackistä erillisen kanavan kullekin eri vaiheelle.
Lisää Slack-viestiin sopivat hashtagit (esimerkiksi #jupyter #scikitlearn #pandas) kuvaamaan toteutuksessa käyttämiäsi teknologioita.  

## Yhteistyö on sallittua

Harjoitustyön tekeminen yhteistyössä on sallittua.
Halutessanne voitte myös toteuttaa yhdessä esimerkiksi datan keräämiseen tai
jalostamiseen tarvittavia komponentteja.
Jokainen kuitenkin palauttaa omat kuvauksensa.
Yhteistyötä tehdesssänne käyttäkää komponenttien jakamiseen versionhallintajärjestelmää.
Harjoitustyöt eivät saa olla identtisiä.

## Loppuraportti

Harjoitustyön palautus tapahtuu lähettämällä oheisen mallin mukainen viesti
Moodlen palautusautomaatilla **perjantaihin 14.5. kello 17 mennessä**.

<blockquote>
  <p>
    Nimi: James Station<br />
    Opiskelijanumero: H654321<br />
    Sähköposti: <a href="mailto:jstat@trolleywatch.org">jstat@trolleywatch.org</a>
  </p>
  <p>Harjoitustyöni aihe: Julkisen liikenteen vaikutus Airbnb-asunnon hintaan</p>
  <p>Harjoitustyö löytyy kokonaisuudessaan oheisesta zip-paketista (jodatuni2021-H654321.zip).</p>

<p>Oppimispäiväkirjani löytyy osoitteesta:
<a href="http://blog.fi/jamesstation/jodatuni2021">http://blog.fi/jamesstation/jodatuni2021</a>.</p>

</blockquote>

Palautettavan zip-paketin (jodatuni2021-opiskelijanumero.zip) tulee sisältää hakemisto nimeltä jodatuni2021-H654321 (korvaa lukusarja H654321 omalla opiskelijanumerollasi), jonka sisältä löytyvät työhösi liittyvät koodi- ja asetustiedostot.
Liitä mukaan tiivis käyttöönotto-ohje.

<!--
Merkitse lisäksi harjoitustyön eri ominaisuuksien raportoiduista toteutuksista keräämäsi pisteet
[Google-laskentataulukkoon](https://docs.google.com/spreadsheets/d/1xKYYAjyzkk5rTL3KuSMs2Srdp-wLgHzPc-QXXGRtaVw/edit?usp=sharing ) (ei edellytä sisäänkirjautumista).
-->
**Merkitse pisteet ainoastaan siinä tapauksessa, että olet julkaissut kuvauksen määräaikaan mennessä.**
