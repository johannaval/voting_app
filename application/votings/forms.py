from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class VotingForm(FlaskForm):
    name = StringField("Kysymys:", [validators.Length(min=3)])
    option1 = StringField("vaihtoehto 1:")
    option2 = StringField("vaihtoehto 2:")
    option3 = StringField("vaihtoehto 3:")

    class Meta:
        csrf = False

class VoteForm(FlaskForm):
    name = StringField("Kysymys:")
    option1 = StringField("1. ")
    option2 = StringField("2. ")
    option3 = StringField("3. ")
    answer = IntegerField("Mitä äänestät? (numero)", [validators.NumberRange(min=1, max=3)])

    class Meta:
        csrf = False

