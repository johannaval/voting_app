## User stories:

- Admin-käyttäjänä haluan poistaa epäsopivia äänestyksiä

```
DELETE FROM voting WHERE voting.id = ?
```
<br>
<br>
<br>

- Admin-käyttäjänä haluan muokata epäsopivia äänestyksiä

```
SELECT Voting.name FROM Voting WHERE Voting.name =?
UPDATE voting SET name=?, date_modified=?, starting_time=?, ending_time=?, 
show_result=?, anonymous=? WHERE voting.id = ?

SELECT option.option_id AS option_option_id, option.voting_id AS option_voting_id 
FROM option WHERE option.option_id = ?
UPDATE option SET name=?, description=? WHERE option.option_id = ?
-> viimeisin select-lause tulee x*vaihtoehtojen määrän verran
```
<br>
<br>
<br>

- Admin-käyttäjän haluan mahdollisuuden poistaa käyttäjiä

```
DELETE FROM account WHERE account.id = ?
```
<br>
<br>
<br>

- Admin-käyttäjän haluan mahdollisuuden muokata käyttäjän tietoja

```
SELECT account.id AS account_id, account.name AS account_name, account.username 
AS account_username, account.password AS account_password, account.is_admin AS account_is_admin 
FROM account 
WHERE account.id = ?
UPDATE account SET name=?, username=?, password=? WHERE account.id = ?

```
<br>
<br>
<br>

- Käyttäjänä haluan luoda tunnukset

```
INSERT INTO account (name, username, password, is_admin) VALUES (?, ?, ?, ?)
```
<br>
<br>
<br>

- Käyttäjänä haluan kirjautua sisään tunnuksillani

```
SELECT account.id AS account_id, account.name AS account_name, account.username 
AS account_username, account.password AS account_password, account.is_admin AS account_is_admin 
FROM account 
WHERE account.username = ?
```
<br>
<br>
<br>

- Käyttäjänä haluan lisätä omia äänestyksiä

```
INSERT INTO voting (name, date_created, date_modified, description, account_id, starting_time, 
ending_time, show_result, anonymous) VALUES (?, DATETIME(CURRENT_TIMESTAMP, "localtime"), 
DATETIME(CURRENT_TIMESTAMP, "localtime"), ?, ?, ?, ?, ?, ?)
```
<br>
<br>
<br>

- Käyttäjänä haluan nähdä äänestykseni tulokset

```
SELECT option.option_id AS option_option_id, option.voting_id AS option_voting_id, 
option.name AS option_name, option.description AS option_description 
FROM option 
WHERE option.voting_id = ?
SELECT Option.name, COUNT(Vote.option_id) FROM Option LEFT JOIN Vote ON Vote.option_id = 
Option.option_id WHERE Option.voting_id = ? GROUP BY option.name ORDER BY count(Vote.option_id) DESC
```
<br>
<br>
<br>


- Käyttäjän haluan äänestää muiden äänestyksissä

```
INSERT INTO user_voted (user_id, voting_id) VALUES (?, ?)
INSERT INTO vote (voting_id, option_id, time) VALUES (?, ?, 
DATETIME(CURRENT_TIMESTAMP, "localtime"))
```
<br>
<br>
<br>

- Käyttäjänä haluan luoda äänestyksen myös anonyymeille käyttäjille

```
INSERT INTO voting (name, date_created, date_modified, description, account_id, 
starting_time, ending_time, show_result, anonymous) VALUES (?, DATETIME(CURRENT_TIMESTAMP, 
"localtime"), DATETIME(CURRENT_TIMESTAMP, "localtime"), ?, ?, ?, ?, ?, ?)
```
<br>
<br>
<br>

- Anonyyminä käyttäjänä haluan mahdollisuuden osallistua äänestyksiin ilman rekisteröitymistä

```
INSERT INTO vote (voting_id, option_id, time) VALUES (?, ?, DATETIME(CURRENT_TIMESTAMP, "localtime"))
```
<br>
<br>
<br>


- Käyttäjänä haluan pystyä muokkaamaan äänestystäni ennen kuin se on alkanut

```
SELECT Voting.name FROM Voting WHERE Voting.name =?
UPDATE voting SET name=?, date_modified=?, starting_time=?, ending_time=?, show_result=?, 
anonymous=? WHERE voting.id = ?

SELECT option.option_id AS option_option_id, option.voting_id AS option_voting_id 
FROM option WHERE option.option_id = ?
UPDATE option SET name=?, description=? WHERE option.option_id = ?
-> viimeisin select-lause tulee x*vaihtoehtojen määrän verran
```
<br>
<br>
<br>

- Käyttäjänä haluan mahdollisuuden poistaa äänestykseni
```
DELETE FROM voting WHERE voting.id = ?
```
<br>
<br>
<br>

Lisäksi:
- Käyttäjänä haluan, ettei tarkat äänestystietoni tallennu minnekkään. 
Tähän ei tarvita SQL-kyselyä, vaan ominaisuus on rakennettu tietokantaan


