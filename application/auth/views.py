from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import bcrypt, app, db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import CreateNewForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    usernameError = ""
    passwordError = ""

    user = User.query.filter_by(
        username=form.username.data).first()

    if (user == None):

        usernameError = "Kyseisellä nimellä ei ole käyttäjää!"
        return render_template("auth/loginform.html", form=form, usernameError=usernameError, passwordError = passwordError)

    else:

        password = form.password.data
        pw = user.password

        if (bcrypt.check_password_hash(pw, password)):

            login_user(user)
            return redirect(url_for("index"))

        else :
            
            passwordError = "Salasana väärin!"
    
    return render_template("auth/loginform.html", form=form, usernameError = usernameError, passwordError=passwordError)



@app.route("/auth/create", methods=["GET", "POST"])
def auth_create():

    if request.method == "GET":
        return render_template("auth/createnewform.html", form=CreateNewForm())

    form = CreateNewForm(request.form)

    user = User.query.filter(
        User.username == form.createNewUsername.data).first()
    if user:
        return render_template("/auth/createnewform.html", form=form, error="Käyttäjänimi on jo varattu!")

    if not form.validate():
        return render_template("/auth/createnewform.html", form=form)

    users = User.query.all()
    user_count = len(users)

    is_admin = False

    if user_count == 0:
        is_admin = True

    password = form.createNewPassword.data
    pw_hash = bcrypt.generate_password_hash(password)

    user = User(form.createNewName.data, form.createNewUsername.data, pw_hash, is_admin)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/list_all")
def auth_listall():

    data = User.query.all()

    return render_template("/auth/listall.html", data=data)


@app.route("/auth/edit/<user_id>", methods=["POST", "GET"])
def auth_edit(user_id):

    form = CreateNewForm(request.form)
    user = User.query.get(user_id)

    data = []

    oldName = user.query.get(user_id).name
    data.append(oldName)
    oldUsername = user.query.get(user_id).username
    data.append(oldUsername)
    oldPassword = user.query.get(user_id).password
    data.append(oldPassword)

    if request.method == "POST" and form.validate():

        newName = request.form.get("createNewName")
        user.name = newName
        newUserName = request.form.get("createNewUsername")
        user.username = newUserName
        newPassword = request.form.get("createNewPassword")
        user.password = newPassword

        db.session.commit()

        return redirect(url_for("auth_listall"))

    else:

        return render_template("auth/editUser.html", user=user, data=data, form=form)


@app.route("/votings/del/<user_id>", methods=["POST", "GET"])
def auth_delete(user_id):

    user = User.query.get(user_id)
    db.session.delete(user)
    db.session().commit()

    return redirect(url_for("auth_listall"))
