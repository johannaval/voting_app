from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app
from application import  db
from application.votings.models import Voting
from application.votings.forms import VotingForm
from application.votings.forms import EditForm

@app.route("/votings", methods=["GET"])
def votings_index():
    return render_template("votings/list.html", votings = Voting.query.all())

@app.route("/votings/new/")
@login_required
def votings_form():
    return render_template("votings/new.html", form = VotingForm())

@app.route("/votings/", methods=["POST"])
@login_required
def votings_create():

    form = VotingForm(request.form)

    if not form.validate():
       return render_template("votings/new.html", form = form)

    v = Voting(form.name.data)
    v.done = False
    v.account_id = current_user.id
  
    db.session().add(v)
    db.session().commit()

    return redirect(url_for("votings_index"))

@app.route("/votings/<voting_id>/", methods=["POST"])
@login_required
def votings_set_done(voting_id):

    t = Voting.query.get(voting_id)
    t.done = True

    db.session().commit()
  
    return redirect(url_for("votings_index"))


@app.route("/votings/edit/<voting_id>/", methods=["GET", "POST"])
@login_required
def votings_ed(voting_id):
    
    form = EditForm(formdata=request.form)
    v = Voting.query.get(voting_id)

    if request.method == 'POST' and form.validate():

            newName = request.form.get("name")
            v.name = newName
            db.session.commit()
            return redirect(url_for("votings_index"))
    
    if request.method == 'POST' and form.validate() == False:
     return render_template("votings/edit.html", voting=v, form=form)

    else:
     return render_template("votings/edit.html", voting=v, form=form)


@app.route("/votings/edit/", methods=["POST"])
@login_required
def votings_edit(voting_id):

    form = VotingForm(request.form)
    name = VotingForm(form.name.data)
    id = Voting.query.filter_by(name = votings.name).first()

    return redirect(url_for("votings_index"))
    
@app.route("/votings/<voting_id>/delete", methods=["POST"])
@login_required
def votings_delete(voting_id):

    v = Voting.query.get(voting_id)
    db.session.delete(v)
    db.session().commit()   

    return redirect(url_for("votings_index"))

