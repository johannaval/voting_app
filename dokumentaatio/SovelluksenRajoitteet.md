## Rajoitteet/heikkoudet

Sovellukseen sain tehtyä kaikki ominaisuudet, joita alusta alkaen halusinkin. Tietenkin vielä lisäominaisuuksia olisi saanut, 
esimerkiksi äänestyksen lopullista äänimäärää olisi voinut havainnollistaa jonkun graafisen diagrammin avulla, joka olisi ollut
äänestyksen tekijälle mukava ominaisuus.

Yhtenä rajoitteena pidän lisävaihtoehtojen antamista automaattisen kolmen vaihtoehdon jälkeen. En halunnut koodata vaihtoehtojen
määrää automaattisesti johonkin lukuun, vaan halusin antaa myös käyttäjän päättää, mikäli hän haluaa enemmän vaihtoehtoja.
Tämä ominaisuus toimii, mutta scriptin ja html kielten kanssa minulla on vielä vaikeuksia. Nyt tähän lisävaihtoehtojen antamiseen käytän scriptiä, jossa
hyödynnän innerHTML metodeja. Kuten kirjoitinkin jo itse sovellukseen kyseiseen kohtaan, kannattaa käyttäjän ensin
valita oikea määrä vaihtoehtoja, ja vasta sen jälkeen täyttää kohdat tiedoilla. Jos täyttää ensin tiedot tähän lisävaihtoehtoon,
ja vasta sitten haluaakin uuden vaihtoehdon, ei aiempi teksti jää talteen, vaan se on kirjoitettava uudestaan.
Jos käyttäjä painaa "Lisää", eikä kaikki kohdat validoitu, "piiloituu" lisävaihtoehdot ja ne pitää klikata uudelleen auki jos muutoksia haluaa niihin vielä tehdä. Tätä kuitenkin
koitin helpottaa, ja muuttaa "uusi vaihtoehto"-napin värin punaiseksi ja lisätä kuvaavan viestin siihen, mikäli virhe on sattunut näissä lisävaihtoehtojen validoinnissa, jotta käyttäjä osaa klikata ne auki ja korjata kohdan.

Toisena heikkoutena näen datetimepickerin asetukset, sillä kalenterin päivät alkavat sunnuntaista, toisin kuin meillä Suomessa, jossa kalenterin viikot katsotaan alkavan aina maanantaista. Tätäkään ominaisuutta en saanut muokattua, vaikka yritin.

