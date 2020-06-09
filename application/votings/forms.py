from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, RadioField, DateTimeField, BooleanField
from datetime import datetime
from application.votings.models import Voting
from wtforms.validators import InputRequired

class VotingForm(FlaskForm):
    name = StringField("Kysymys:", [validators.Length(min=3, max=50, message='Kysymyksessä pitää olla 3-50 merkkiä!')])
    nameDescription = StringField("Kuvaus: (vapaaehtoinen)")
    option1 = StringField("vaihtoehto 1:", [validators.Length(min=1, max=30, message='Vaihtoehdossa pitää olla 1-30 merkkiä!')])
    option1Description = StringField("Kuvaus: (vapaaehtoinen)")
    option2 = StringField("vaihtoehto 2:", [validators.Length(min=1, max=30, message='Vaihtoehdossa pitää olla 1-30 merkkiä!')])
    option2Description = StringField("Kuvaus: (vapaaehtoinen)")
    option3 = StringField("vaihtoehto 3:", [validators.Length(min=1, max=30, message='Vaihtoehdossa pitää olla 1-30 merkkiä!')])
    option3Description = StringField("Kuvaus: (vapaaehtoinen)")

    starting_time = DateTimeField("Aloitusaika:", [validators.InputRequired(message='Valitsethan aloituspäivän ja ajan!')])
    ending_time = DateTimeField("Lopetusaika:", [validators.InputRequired(message='Valitsethan lopetuspäivän ja ajan!')])

    results = RadioField('Mitä tuloksia haluat, että muut näkevät?', choices = [('1','Ei mitään'),('2','Vain kärjen'),('3','Kaikki äänet')], validators=[InputRequired()])
    anonymous = RadioField('Äänestys vain kirjautuneille käyttäjille? ', choices = [('1','Kyllä'),('2','Ei')], validators=[InputRequired()])
    
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

