from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from wtforms.validators import EqualTo
  
class CreateNewForm(FlaskForm):
    createNewName = StringField("Nimi: ", [validators.Length(min=3, max=30, message='Nimessä pitää olla 3-30 merkkiä!')])
    createNewUsername = StringField("Käyttäjänimi: ", [validators.Length(min=3, max=20, message='Käyttäjänimessä pitää olla 3-20 merkkiä!')])
    createNewPassword = PasswordField("Salasana: ", [validators.Length(min=3, max=20, message='Salasanassa pitää olla 3-20 merkkiä!'), EqualTo('createNewPassword_again', message='Hups! tarkista että salasanat ovat samat')])
    createNewPassword_again = PasswordField("Salasana uudestaan: ")


    class Meta:
        csrf = False


class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi: ")
    password = PasswordField("Salasana: ")
  
    class Meta:
        csrf = False

