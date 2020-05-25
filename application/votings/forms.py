from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, RadioField, DateTimeField, BooleanField
from datetime import datetime

class VotingForm(FlaskForm):
    name = StringField("Kysymys:", [validators.Length(min=3)])
    nameDescription = StringField("Kuvaus: (vapaaehtoinen)")
    option1 = StringField("vaihtoehto 1:")
    option1Description = StringField("Kuvaus: (vapaaehtoinen)")
    option2 = StringField("vaihtoehto 2:")
    option2Description = StringField("Kuvaus: (vapaaehtoinen)")
    option3 = StringField("vaihtoehto 3:")
    option3Description = StringField("Kuvaus: (vapaaehtoinen)")
    starting_time = DateTimeField("Aloitusaika:")
    ending_time = DateTimeField("Lopetusaika:")
    results = RadioField('Mitä tuloksia haluat, että muut näkevät?', choices = [('1','Ei mitään'),('2','Vain kärjen'),('3','Kaikki äänet')])
    anonymous = RadioField('Äänestys vain kirjautuneille käyttäjille? ', choices = [('1','Kyllä'),('2','Ei')])
    
    class Meta:
        csrf = False

class VoteForm(FlaskForm):
    name = StringField("Kysymys:")
    option1 = StringField("1. ")
    option2 = StringField("2. ")
    option3 = StringField("3. ")
    answer = RadioField('Mitä äänestät?', choices = [('1','1'),('2','2'),('3','3')])

    class Meta:
        csrf = False

