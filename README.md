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

##

Ensin tarvitset:

- Pythonin version  3.5. (Tai uudemman) [Linkki](https://www.python.org/downloads/)

- Pythonin pip:in, jonka avulla saat ladattua apukirjastoja. Tämä asentuu oletuksena linkin takaa löytyvistä Python-versioista.

- Pythonin venv-kirjaston. Tämä yleensä asentuu yllä mainitun Python-ympäristön mukana.

- PostgreSQL-tietokannanhallintajärjestelmän [Linkki](https://www.postgresql.org/). Tämän lisäksi voit myös ladata pgAdmin:in. [Linkki](https://www.pgadmin.org/)

- GIT:in, eli välineet git-repositorioiden käsittelyyn. [Linkki](https://git-scm.com/downloads)

- Jos haluat ladata sovelluksen Herokuun, tarvitset tunnukset sinne [Linkki](https://www.heroku.com) sekä työvälineet sen käyttöön. [Linkki](https://devcenter.heroku.com/articles/heroku-cli)

- Jos haluat tarkastella tai muokata koodia, esimerkiksi Visual Studio Code on hyvä vaihtoehto [Linkki](https://code.visualstudio.com/) 

- Github-käyttäjätunnuksen [Linkki](https://github.com/)




### Paikallinen asennus:

- Lataa sovellus koneellesi painamalla tämän repositorion vihreätä nappia, jossa lukee "Clone or download".

- Paina "Download ZIP"

- Luo uusi kansio tiedostoihisi, ja siirrä sekä pura lataamasi ZIP sinne.

- Siirry ZIP:in luomaan kansioon 

- Asenna Python-virtuaaliympäristö samaan hakemistoon, missä sovellus on, komennolla:
- ``` python -m venv venv ```

- Virtuaaliympäristön saa käyttöön:
- ``` source venv/bin/activate ```

- Asenna tarvittavat riippuvuudet:
- ``` pip install -r requirements.txt ```


- Käynnistä ohjelma:
- ``` python run.py ```

- Ja nyt ohjelmaa voi käyttää osoitteessa http://localhost:5000/ sekä http://127.0.0.1:5000/
<br>
<br>

### Herokuun asennus:

- Paikallisen asennuksen jälkeen voi asentaa sovelluksen myös Herokuun.

- Luo Githubiin repositorio

- Saat mahdollisuuden projektin versiointiin sekä .git-nimisen kansion luomalla projektikansiolle git-versionhallinnan:

- ``` git init ``` 

- Lisää GitHubissa oleva repositorio kansion paikallisen versionhallinnan etäpisteeksi. Löydät projektin nimen GitHubista, joka on muotoa: https://github.com/käyttäjätunnus/projektin-nimi.git. Syötä nyt komento:

- ```git remote add origin github-projektin osoite ``` 

- Lisää tiedostot GitHubiin:

- ``` git add .``` (huomaa piste!)
- ``` git push -u origin master```


- Jäädytetään projektin tämän hetkiset riippuvuudet, jotta Heroku tietää mitä riippuvuuksia tulee asentaa.  

- ```pip freeze > requirements.txt ```


- Poista requirements.txt tiedostosta rivi: pkg-resources==0.0.0 (esim tekstieditorilla)

- Luo sovellukselle paikka Herokuun. Jotta paikan luominen onnistuu, ei saman nimistä sovellusta Herokussa saa olla.
Kokeile eri vaihtoehtoja, tai aja pelkkä "heroku create", jolloin Heroku valitsee projektille satunnaisen nimen.
Valitsemallasi nimellä paikan luominen onnistuu komennolla: 

- ```heroku create sovelluksen_nimi ```  

- Lisää paikalliseen versionhallintaan tieto Herokusta.

- ```git remote add heroku https://git.heroku.com/sovelluksen_nimi.git```

- Lähetetään sovellus Herokuun komennoilla:

- ```git add .``` Huom taas piste!
- ```git commit -m "Initial commit"```
- ```git push heroku master```


- Löydät sovelluksen nyt osoitteesta: https://sovelluksen_nimi.herokuapp.com/. Jossa sovelluksen_nimi on sille antamasi nimi.

- Sovellus kannattaa päivittää GitHubiin, sillä  siihen on tullut päivityksiä: 

- ```git push origin master```


