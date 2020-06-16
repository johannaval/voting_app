### Tietokantakaavio: 


<img src="https://github.com/johannaval/voting_app/blob/master/dokumentaatio/Screenshot%20from%202020-06-16%2013-24-12.png" width="950" height="500">

Kaaviota selkeyttämään pienet kuvaukset jokaista taulua kohti:

Voting
- Taulu, joka kuvaa yhtä äänestystä

Vote
- Taulu, joka kuvaa yhtä annettua ääntä
- Käyttäjä voi äänestää vain kerran per äänestys, ellei se oli anonyymi-äänestys
- Ei tallenna ikinä tarkkaa tietoa, mitä käyttäjä on äänestänyt, vain tiedon missä äänestyksessä hän on äänestänyt
- Tallentaa myös anonyyminä annetut äänet

User_Voted
- Taulu, joka kuvaa äänestykset, missä käyttäjä on äänestänyt, ellei käyttäjä ole anonyymi

Option
- Taulu, joka kuvaa äänestyksen vaihtoehdon (Niitä on 3-6 per äänestys)

Account
- Taulu, joka kuvaa käyttäjän tietoja


### SQL-schema:

```
CREATE TABLE option (
	option_id INTEGER NOT NULL, 
	voting_id INTEGER, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(144), 
	PRIMARY KEY (option_id)
);
CREATE TABLE user_voted (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	voting_id INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE vote (
	vote_id INTEGER NOT NULL, 
	voting_id INTEGER, 
	option_id INTEGER, 
	time DATETIME, 
	PRIMARY KEY (vote_id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	is_admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
);
CREATE TABLE voting (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	description VARCHAR(144), 
	account_id INTEGER NOT NULL, 
	starting_time DATETIME, 
	ending_time DATETIME, 
	show_result INTEGER, 
	anonymous INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
```
