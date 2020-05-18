from flask_wtf import FlaskForm
from wtforms import StringField, validators

class VotingForm(FlaskForm):
    name = StringField("Question:", [validators.Length(min=3)])
    option1 = StringField("Option 1")
    option2 = StringField("Option 2")
    option3 = StringField("Option 3")

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    name = StringField("Question:", [validators.Length(min=3)])
    option1 = StringField("Option 1")
    option2 = StringField("Option 2")
    option3 = StringField("Option 3")

    class Meta:
        csrf = False

