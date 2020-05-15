from application import app, db
from flask import redirect, render_template, request, url_for
from application.votings.models import Voting

@app.route("/votings", methods=["GET"])
def votings_index():
    return render_template("votings/list.html", votings = Voting.query.all())

@app.route("/votings/new/")
def votings_form():
    return render_template("votings/new.html")

@app.route("/votings/<voting_id>/", methods=["POST"])
def votings_set_done(voting_id):

    v = Voting.query.get(voting_id)
    v.done = True
    db.session().commit()
  
    return redirect(url_for("votings_index"))

@app.route("/votings/", methods=["POST"])
def votings_create():
    v = Voting(request.form.get("name"))

    db.session().add(v)
    db.session().commit()
  
    return redirect(url_for("votings_index"))
