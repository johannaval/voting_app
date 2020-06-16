## Voting_app

Sovellus tarjoaa mahdollisuuden luoda äänestyksiä sekä osallistumaan itse muiden äänestyksiin. Äänestyksen tekijä saa itse määritellä, näkyykö äänestyksen tulokset muille. 
Sovelluksessa on myös mahdollisuus anonyymeille äänestyksille, jotka eivät vaadi kirjautumista. Äänestyksen tekijä pääsee näkemään äänestyksen kaikki tulokset, sekä sen, miten äänestysaktiviteetti on ajan suhteen jakautunut.

Testitunnukset:

    
    (admin käyttäjä):
    käyttäjänimi: admin
    salasana: testaaja
    
    käyttäjänimi: tero
    salasana: testaaja

    
[Sovellus (Heroku)](https://tsoha-voting-app.herokuapp.com/)

[User storyt:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/user_stories.md)

[Tietokantakaavio ja schema:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/Tietokantakaavio%26Schema.md)

[Jatkokehitys:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/Jatkokehitys.md)

[Käyttöohje:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/K%C3%A4ytt%C3%B6ohje.md)

[Rajoitteet/Heikkoudet](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/SovelluksenRajoitteet.md)

[Omat kokemukset](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/OmatKokemukset.md)


## Asennusohje:

### Paikallinen asennus:

Lataa sovellus koneellesi painamalla tämän repositorion vihreätä nappia, jossa lukee "Clone or download".
<br>

Paina "Download ZIP"
<br>

Luo uusi kansio tiedostoihisi, ja siirrä sekä pura lataamasi ZIP sinne.
<br>

Siirry ZIP:in luomaan kansioon 
<br>

Asenna Python-virtuaaliympäristö samaan hakemistoon, missä sovellus on, komennolla:
``` python -m venv venv ```
<br>

Virtuaaliympäristön saa käyttöön:
``` source venv/bin/activate ```
<br>


Asenna tarvittavat riippuvuudet:

``` pip install -r requirements.txt ```


Käynnistä ohjelma:

``` python run.py ```


Ja nyt ohjelmaa voi käyttää osoitteessa http://localhost:5000/ sekä http://127.0.0.1:5000/

### Herokuun asennus:

Paikallisen asennuksen jälkeen voi asentaa sovelluksen myös Herokuun.
Luo Githubiin repositorio
Saat mahdollisuuden projektin versiointiin sekä .git-nimisen kansion luomalla projektikansiolle git-versionhallinnan:

``` git init ``` 
<br>

Lisää GitHubissa oleva repositorio kansion paikallisen versionhallinnan etäpisteeksi. Löydät projektin nimen GitHubista, joka on muotoa: https://github.com/käyttäjätunnus/projektin-nimi.git. Syötä nyt komento:

```git remote add origin github-projektin osoite ``` 

<br>

Lisää tiedostot GitHubiin:

``` git add .``` (huomaa piste!)
``` git push -u origin master```

<br>

Jäädytetään projektin tämän hetkiset riippuvuudet, jotta Heroku tietää mitä riippuvuuksia tulee asentaa.  

```pip freeze > requirements.txt ```

<br>

Poista requirements.txt tiedostosta rivi: pkg-resources==0.0.0 (esim tekstieditorilla)
<br>

Luo sovellukselle paikka Herokuun. Jotta paikan luominen onnistuu, ei saman nimistä sovellusta Herokussa saa olla.
Kokeile eri vaihtoehtoja, tai aja pelkkä "heroku create", jolloin Heroku valitsee projektille satunnaisen nimen.
Valitsemallasi nimellä paikan luominen onnistuu komennolla: 

```heroku create sovelluksen_nimi ```  
<br>

Lisää paikalliseen versionhallintaan tieto Herokusta.

```git remote add heroku https://git.heroku.com/sovelluksen_nimi.git```
<br>

Lähetetään sovellus Herokuun komennoilla:

```git add .``` Huom taas piste!
```git commit -m "Initial commit"```
```git push heroku master```

<br>

Löydät sovelluksen nyt osoitteesta: https://sovelluksen_nimi.herokuapp.com/. Jossa sovelluksen_nimi on sille antamasi nimi.
<br>

Sovellus kannattaa päivittää GitHubiin, sillä  siihen on tullut päivityksiä: 

```git push origin master```
<br>


