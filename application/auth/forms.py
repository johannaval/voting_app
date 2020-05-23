from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, StringField, ValidationError
from application.auth.models import User
  
class CreateNewForm(FlaskForm):
    createNewName = StringField("Nimi: ", [validators.Length(min=3, max=30, message="Nimessä pitää olla 3-30 merkkiä!")])
    createNewUsername = StringField("Käyttäjänimi: ", [validators.Length(min=3, max=20, message="Käyttäjänimessä pitää olla 3-20 merkkiä!")])
    createNewPassword = PasswordField("Salasana: ", [validators.Length(min=3, max=20, message="Salasanassa pitää olla 3-20 merkkiä!")])

    def validate_username(self, username):
  
       user = User.query.filter_by(username=createNewName.data).first()
   #    if user:
    #      raise ValidationError('That username is taken. Please choose another.')

    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi: ")
    password = PasswordField("Salasana: ")
  
    class Meta:
        csrf = False
