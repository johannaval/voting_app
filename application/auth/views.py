from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import bcrypt, app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import CreateNewForm
from flask_login import current_user
from application.votings.modelsVoting import Voting




@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    username_error = ""
    password_error = ""

    user = User.query.filter_by(
        username=form.username.data).first()

    if (user == None):

        username_error = "Kyseisellä nimellä ei ole käyttäjää!"
        return render_template("auth/loginform.html", form=form, usernameError=username_error, passwordError = password_error)

    else:

        password = form.password.data
        pw = user.password


        if (bcrypt.check_password_hash(pw, password)):

            login_user(user)
            return redirect(url_for("votings_index"))

        else :
            
            password_error = "Salasana väärin!"
    
    return render_template("auth/loginform.html", form=form, usernameError = username_error, passwordError=password_error)



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
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(form.createNewName.data, form.createNewUsername.data, pw_hash, is_admin)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("votings_index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))




@app.route("/auth/list_all")
@login_required
def auth_listall():

    if not current_user.is_admin:
        return redirect(url_for("votings_index"))

    data = User.query.all()
    return render_template("/auth/listall.html", data=data)




@app.route("/auth/edit/<user_id>", methods=["POST", "GET"])
@login_required
def auth_edit(user_id):

    if not current_user.is_admin:
        return redirect(url_for("votings_index"))

    form = CreateNewForm(request.form)
    user = User.query.get(user_id)

    data = []

    old_name = user.query.get(user_id).name
    data.append(old_name)
    old_username = user.query.get(user_id).username
    data.append(old_username)
    old_password = user.query.get(user_id).password
    data.append(old_password)

    u = User.query.filter(
        User.username == request.form.get("createNewUsername")).first()

    this = User.query.get(user_id)

    if u != None and u.username != this.username:
        return render_template("auth/editUser.html", user=this, data=data, form=form, error = "Käyttäjänimi on jo käytössä!")


    if request.method == "POST" and form.validate():

        new_name = request.form.get("createNewName")
        user.name = new_name
        new_username = request.form.get("createNewUsername")
        user.username = new_username
        new_password = request.form.get("createNewPassword")

        pw_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        user.password = pw_hash

        db.session.commit()

        return redirect(url_for("auth_listall"))

    else:

        return render_template("auth/editUser.html", user=user, data=data, form=form)




@app.route("/votings/del/<user_id>", methods=["POST", "GET"])
@login_required
def auth_delete(user_id):

    if not current_user.is_admin:
        return redirect(url_for("votings_index"))

    user = User.query.get(user_id)
    users_votings = Voting.get_all_votings_by_user_id(user.id)

    for uv in users_votings:
        v = Voting.query.get(uv)
        db.session.delete(v)
        db.session().commit()
        

    db.session.delete(user)
    db.session().commit()

    return redirect(url_for("auth_listall"))
