from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app
from application import  db
from application.votings.models import Voting, Option
from application.votings.forms import VotingForm
from application.votings.forms import VoteForm


@app.route("/votings", methods=["GET"])
def votings_index():

    return render_template("votings/list.html", votings = Voting.query.all())



@app.route("/votings/new/")
@login_required
def votings_form():

    return render_template("votings/new.html", form = VotingForm())



@app.route("/votings/<voting_id>/vote", methods=["POST","GET"])
@login_required
def votings_vote(voting_id):

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id==voting_id).all()

    return render_template("votings/vote.html", voting = v, data=data, form = VoteForm())


@app.route("/votings/<voting_id>/vote/this", methods=["GET", "POST"])
@login_required
def votings_vote_this(voting_id):

    form = VoteForm(request.form)

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id==voting_id).all()

    if not form.validate():
       return render_template("votings/vote.html", voting = v, data = data, form = form)

    votings_set_done(voting_id)

    return redirect(url_for("votings_index"))


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

    o1 = Option(form.option1.data)
    o1.name = form.option1.data
    o1.voting_id = v.id
    db.session().add(o1)

    o2 = Option(form.option2.data)
    o2.name = form.option2.data
    o2.voting_id = v.id
    db.session().add(o2)

    o3 = Option(form.option3.data)
    o3.name = form.option3.data
    o3.voting_id = v.id
    db.session().add(o3)
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
def votings_edit(voting_id):
    
    form = VotingForm(formdata=request.form)
    v = Voting.query.get(voting_id)

    options = Option.query.filter(Option.voting_id==voting_id).all()

    o1 = options[0]
    o2 = options[1]
    o3 = options[2]

    if request.method == 'POST' and form.validate():

            newName = request.form.get("name")
            v.name = newName
            v.date_modified = default=db.func.current_timestamp()
            db.session.commit()
  
            
            newOption1 = request.form.get("option1")
            o1.name = newOption1
            db.session.commit()

            newOption2 = request.form.get("option2")
            o2.name = newOption2
            db.session.commit()

            newOption3 = request.form.get("option3")
            o3.name = newOption3
            db.session.commit()
           

            return redirect(url_for("votings_index"))
    
    if request.method == 'POST' and form.validate() == False:
     return render_template("votings/edit.html", voting=v, options=options, form=form)

    else:
     return render_template("votings/edit.html", voting=v, options = options, form=form)

    
@app.route("/votings/<voting_id>/delete", methods=["POST"])
@login_required
def votings_delete(voting_id):

    v = Voting.query.get(voting_id)
    db.session.delete(v)
    db.session().commit()   

    return redirect(url_for("votings_index"))

