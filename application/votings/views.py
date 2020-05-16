from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app
from application import  db
from application.votings.models import Voting
from application.votings.forms import VotingForm

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
