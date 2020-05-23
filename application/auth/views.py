from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import CreateNewForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Tarkista käyttäjänimi ja salasana!")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/create", methods = ["GET", "POST"])
def auth_create():

    if request.method == "GET":
        return render_template("auth/createnewform.html", form=CreateNewForm())

    form = CreateNewForm(request.form)

    user = User.query.filter(User.username==form.createNewUsername.data).first()
    if user:
        return render_template("/auth/createnewform.html", form = form, error = "Käyttäjänimi on jo varattu!")


    if not form.validate():
        return render_template("/auth/createnewform.html", form = form,
                                error = "Käyttäjän luominen ei onnistunut")

    user = User(form.createNewName.data, form.createNewUsername.data, form.createNewPassword.data)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    
