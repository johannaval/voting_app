## Voting_app

Sovellus tarjoaa mahdollisuuden luoda äänestyksiä sekä osallistumaan itse muiden äänestyksiin. Äänestyksen tekijä saa itse määritellä, näkyykö äänestyksen tulokset muille. 
Sovelluksessa on myös mahdollisuus anonyymeille äänestyksille, jotka eivät vaadi kirjautumista.

Testitunnukset:

    
    (admin käyttäjä):
    käyttäjänimi: admin
    salasana: testaaja
    
    käyttäjänimi: tero
    salasana: testaaja

    
[Sovellus (Heroku)](https://tsoha-voting-app.herokuapp.com/)

[User storyt:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/user_stories.md)

[Tietokantakaavio:](https://github.com/johannaval/voting_app/blob/master/dokumentaatio/Screenshot%20from%202020-05-13%2016-03-35.png)


Asennusohje:

- Asenna Python-virtuaaliympäristö samaan hakemistoon, missä sovellus on, komennolla:

´´´ python -m venv venv ´´´


- Virtuaaliympäristön saa käyttöön:

´´´ source venv/bin/activate ´´´


- Asenna tarvittavat riippuvuudet:

´´´ pip install -r requirements.txt ´´´


- Käynnistä ohjelma:

´´´ python run.py ´´´


Ja nyt ohjelmaa voi käyttää osoitteessa http://localhost:5000/ sekä http://127.0.0.1:5000/




Käyttöohje:

- Jos et halua kirjautua tai tehdä tunnusta, pääset selaamaan äänestyksiä, jotka eivät vaadi tunnusta painamalla "Aloitetaan!"-napista, joka löytyy heti kun avaat ohjelman. 
- Painamalla "Äänestä" pääset näkemään äänestyksen vaihtoehdot. Valitse sinulle sopivin vaihtoehto ja ruksita sitä vastaava numero. Sen jälkeen voit painaa "Äänestä", jolloin valintasi tallennetaan. 


 - Jos taas haluat kirjautua sisään tai rekisteröidä käyttäjän, valitse oikeasta yläreunassa haluamasi toiminta. 
 - Pääset lisäämään uuden äänestyksen kohdasta "Lisää uusi äänestys" ja täyttämällä tarvittavat tiedot. Sen jälkeen voit painaa napista "Lisää", jolloin äänestyksesi julkaistaan.
 - "Äänestykset"-valikon kautta pääset tutkimaan omia äänestyksiäsi, äänestyksiä joissa et vielä ole äänestänyt, ja äänestyksiä, joissa olet jo äänestänyt.
 - Omia äänestyksiä voit "Omat äänestykset" -kohdassa muokata, poistaa ja tarkastella sen tuloksia.
 - "Äänestykset, missä et ole vielä äänestänyt" -kohdassa näet käynnissä olevat äänestykset joissa voit myös äänestää, sekä odottavat äänestykset, jotka eivät vielä ole alkaneet.
 - "Tarkastele äänestämiesi äänestysten tuloksia" -kohdassa pääset näkemään niiden äänestysten tuloksia, joissa olet jo äänestänyt. Tulokset näkyvät sen mukaan, mitä äänestyksen tekijä on halunnut jakaa.
 - Pääset kirjautumaan ulos oikeassa yläreunassa olevan "Kirjaudu ulos" -napin kautta

