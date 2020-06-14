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


## Asennusohje:

- Asenna Python-virtuaaliympäristö samaan hakemistoon, missä sovellus on, komennolla:

``` python -m venv venv ```


- Virtuaaliympäristön saa käyttöön:

``` source venv/bin/activate ```


- Asenna tarvittavat riippuvuudet:

``` pip install -r requirements.txt ```


- Käynnistä ohjelma:

``` python run.py ```


Ja nyt ohjelmaa voi käyttää osoitteessa http://localhost:5000/ sekä http://127.0.0.1:5000/

