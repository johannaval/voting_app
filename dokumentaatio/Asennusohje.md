

## Asennusohje:

## Ensin tarvitset:

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

- Paina "Download ZIP" tai jos haluat kloonata projektin itselleni, kopioi HTTPS linkki

- Luo uusi kansio tiedostoihisi.

- Jos käytät ZIP:piä, siirrä sekä pura lataamasi ZIP tähän uuteen kansioon.

- Jos taas haluat kloonata projektin, siirry komentokentän kautta uuteen kansioon ja kirjoita komento:
- ``` git clone https://github.com/johannaval/voting_app.git``` 

- Pääset projektikansioon
- ``` cd tsoha``` 

- Asenna Python-virtuaaliympäristö samaan hakemistoon, missä sovellus on, komennolla:
- ``` python3 -m venv venv ```

- Virtuaaliympäristön saa käyttöön: (Komentojen eteen ilmestyy (venv))
- ``` source venv/bin/activate ```

- Asenna tarvittavat riippuvuudet:
- ``` pip install -r requirements.txt ```


- Käynnistä ohjelma:
- ``` python run.py ```

- Ja nyt ohjelmaa voi käyttää osoitteessa http://localhost:5000/ sekä http://127.0.0.1:5000/

- Huomaa, että jos haluat käynnistää sovelluksen myöhemmin uudelleen, sinun pitää ensin käynnistää virtuaaliympäristössä aiemmin mainitulla koodilla:
- ``` source venv/bin/activate.``` 

- Ohjelman suorituksen saa lopetettua näppäimillä Ctrl + C.
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

- Sovelluksen latautumisessa Herokuun voi mennä pieni hetki. Kun se avautuu, voit kirjautua sisään READ.ME:ssä mainituilla tunnuksilla tai luoda kokonaan omat.


