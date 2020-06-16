from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, RadioField, DateTimeField, BooleanField, SubmitField
from datetime import datetime
from application.votings.modelsVoting import Voting
from wtforms.validators import InputRequired

class VotingForm(FlaskForm):
    name = StringField("Kysymys:", [validators.Length(min=3, max=100, message='Kysymyksessä pitää olla 3-100 merkkiä!')])
    nameDescription = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option1 = StringField("vaihtoehto 1:", [validators.Length(min=1, max=50, message='Vaihtoehdossa pitää olla 1-50 merkkiä!')])
    option1Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option2 = StringField("vaihtoehto 2:", [validators.Length(min=1, max=50, message='Vaihtoehdossa pitää olla 1-50 merkkiä!')])
    option2Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option3 = StringField("vaihtoehto 3:", [validators.Length(min=1, max=50, message='Vaihtoehdossa pitää olla 1-50 merkkiä!')])
    option3Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option4 = StringField("vaihtoehto 4:", [validators.Length(max=50, message='Vaihtoehdossa ei saa olla yli 50 merkkiä!')])
    option4Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option5 = StringField("vaihtoehto 5:", [validators.Length(max=50, message='Vaihtoehdossa ei saa olla yli 50 merkkiä!')])
    option5Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
    option6 = StringField("vaihtoehto 6:", [validators.Length(max=59, message='Vaihtoehdossa ei saa olla yli 50 merkkiä!')])
    option6Description = StringField("Kuvaus: (vapaaehtoinen)", [validators.Length(max=70, message='Kuvauksessa ei voi olla yli 70 merkkiä!')])
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
    answer4 = RadioField('Mitä äänestät?', choices = [('1','1'),('2','2'),('3','3'),('4','4')])
    answer5 = RadioField('Mitä äänestät?', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    answer6 = RadioField('Mitä äänestät?', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')])

    class Meta:
        csrf = False
