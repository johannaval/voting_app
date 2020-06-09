from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.votings.models import Voting, UserVoted, Vote, Option
from application.votings.forms import VotingForm
from application.votings.forms import VoteForm
from datetime import datetime

@app.route("/votings", methods=["GET"])
def votings_index():

    votingsToVoteNow =[]
    votingsToVoteLater=[]

    if not current_user.is_authenticated:

       votingsToVoteNow = Voting.getAnonymousVotingsThatCanbeVotedNow()
       votingsToVoteLater = Voting.getAnonymousVotingsThatCanbeVotedLater()


    return render_template("votings/list.html", votingsToVoteNow=votingsToVoteNow, votingsToVoteLater = votingsToVoteLater)


@app.route("/votings/new/")
@login_required
def votings_form():

    return render_template("votings/new.html", form=VotingForm())


@app.route("/votings/vote/<voting_id>", methods=["POST"])
def votings_vote(voting_id):

    data = Option.query.filter(Option.voting_id == voting_id).all()
    result = []

    v = Voting.query.get(voting_id)

    teksti = []

    creator = v.account_id
    current = 999

    current_time = datetime.now()
    isOn = False
    
    if (v.starting_time < current_time):
        isOn = True

    if current_user.is_authenticated:
        current = current_user.id

    user_has_voted = UserVoted.has_voted(current, voting_id)

    if not isOn:
       time = v.starting_time

    else:
        time = v.ending_time

    separated_time=[]
    separated_time.append(time.strftime("%m"))
    separated_time.append(time.strftime("%d"))
    separated_time.append(time.strftime("%Y"))
    separated_time.append(time.strftime("%H"))
    separated_time.append(time.strftime("%M"))
    separated_time.append(time.strftime("%S"))


    return render_template("votings/vote.html", voting=v, data=data, creator=creator, current=current, user_has_voted=user_has_voted, form=VoteForm(), isOn = isOn, separated_time = separated_time)


@app.route("/votings/<voting_id>/show", methods=["GET"])
def votings_show_this(voting_id):

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id == voting_id).all()


    result = []
    teksti = []
    list = []

    if v.show_result == 2:
        teksti.append("Kolme eniten ääniä saanutta vaihtoehtoa: : ")
        list = Vote.return_top_3_votes_in_vote(voting_id)

    elif v.show_result == 1:
        teksti.append("")

    elif v.show_result == 3:
        teksti.append("Kaikki äänet: ")
        list = Vote.return_top_3_votes_in_vote(voting_id)

    for l in list:
        l.replace("'", "")
        l.replace(" ", "   ")

    creator = v.account_id

    current = 999

    if current_user.is_authenticated:
        current = current_user.id


    name = Voting.query.get(voting_id)
    tekija = Voting.query.get(voting_id).account_id

    user_has_voted = UserVoted.has_voted(current, voting_id)

    return render_template("votings/showVotingResults.html", voting=v, data=data, creator=creator, current=current, list=list, teksti=teksti, user_has_voted=user_has_voted, form=VoteForm())


@app.route("/votings/vote/<voting_id>/", methods=["GET", "POST"])
def votings_vote_this(voting_id):

    v_id = voting_id

    form = VoteForm(request.form)

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id == v_id).all()

    time = v.starting_time
    formatted_time = time.strftime("%m %d, %Y %H:%M:%S")
    separated_time=[]
    formatted_time = "06 20,2020 20:06:46"
    separated_time.append(time.strftime("%m"))
    separated_time.append(time.strftime("%d"))
    separated_time.append(time.strftime("%Y"))
    separated_time.append(time.strftime("%H"))
    separated_time.append(time.strftime("%M"))
    separated_time.append(time.strftime("%S"))

    print (separated_time[0])
    print (separated_time[1])
    print (separated_time[2])
    print (separated_time[3])
    print (separated_time[4])
    print (separated_time[5])


   
    print (formatted_time)

    if not form.validate():
        return render_template("votings/vote.html", voting=v, data=data, form=form, formatted_time = formatted_time, separated_time=separated_time)

    if current_user.is_authenticated:
        user = current_user
        user_vote = UserVoted(voting_id)
        user_vote.voting_id = voting_id
        user_vote.user_id = current_user.id
        db.session.add(user_vote)
        db.session.commit()

    uv = form.answer.data
    index = int(uv)-1
    op = data[index]

    new_vote = Vote(voting_id)
    new_vote.voting_id = int(voting_id)+3

    # mikä ihmeen 3

    new_vote.option_id = op.option_id

    db.session.add(new_vote)
    db.session.commit()



    if not current_user.is_authenticated:
        return redirect(url_for("votings_index"))

    return redirect(url_for("votings_notVoted"))


@app.route("/votings/", methods=["POST", "GET"])
@login_required
def votings_create():

    if request.method == "GET":
        return render_template("votings/new.html", form=VotingForm())

    form = VotingForm(request.form)
    error = ""

    name = form.name.data

    list = []
    list.append(form.option1.data)
    list.append(form.option2.data)
    list.append(form.option3.data)

    if(Voting.isOptionsDifferent(list) == False):
        error = "Jokainen vaihtoehto pitää olla eri!"
        return render_template("votings/new.html", form=form, error=error)

    if Voting.isVotingNameUnique(name) == False:
        error = "Tällä nimellä on jo äänestys!"
        return render_template("votings/new.html", form=form, error=error)

    if not form.validate() or form.starting_time.data >= form.ending_time.data:

        v = Voting(form.name.data)

        timeError=""

        if(form.starting_time.data >= form.ending_time.data):
            timeError = "Ops! Valitsethan äänestyksen päättymisajaksi myöhemmän ajan kuin alkamisaika!"

        return render_template("votings/new.html", form=form, error= error, timeError=timeError)

    v = Voting(form.name.data)
    v.done = False
    v.description = form.nameDescription.data
    v.account_id = current_user.id
    v.show_result = form.results.data
    v.anonymous = form.anonymous.data

    v.starting_time = form.starting_time.data
    v.ending_time = form.ending_time.data


    db.session().add(v)
    db.session().commit()

    o1 = Option(form.option1.data)
    o1.name = form.option1.data
    o1.description = form.option1Description.data
    o1.voting_id = v.id
    db.session().add(o1)

    o2 = Option(form.option2.data)
    o2.name = form.option2.data
    o2.description = form.option2Description.data
    o2.voting_id = v.id
    db.session().add(o2)

    o3 = Option(form.option3.data)
    o3.name = form.option3.data
    o3.description = form.option3Description.data
    o3.voting_id = v.id
    db.session().add(o3)

    db.session().commit()

    return redirect(url_for("votings_index"))


@app.route("/votings/<voting_id>/edit", methods=["GET", "POST"])
@login_required
def votings_edit(voting_id):

    form = VotingForm(formdata=request.form)
    v = Voting.query.get(voting_id)

    error = ""

    name = form.name.data

    list = []
    list.append(form.option1.data)
    list.append(form.option2.data)
    list.append(form.option3.data)

    options = Option.query.filter(Option.voting_id == voting_id).all()

    o1 = options[0]
    o2 = options[1]
    o3 = options[2]

    if request.method=="POST":

       if(Voting.isOptionsDifferent(list) == False):
          error = "Jokainen vaihtoehto pitää olla eri!"
          return render_template("votings/edit.html", form=form, error=error, voting=v, options = options)

       if Voting.isVotingNameUnique(name) == False and Voting.query.get(voting_id).name != request.form.get("name"):
          error = "Tällä nimellä on jo äänestys!"
          return render_template("votings/edit.html", form=form, error=error, voting = v, options = options)

       if not form.validate():
          return render_template("votings/edit.html", form=form, error= error, voting= v, options= options)
    

    if request.method == "POST" and form.validate():

        newName = request.form.get("name")
        v.name = newName
        v.date_modified = default = db.func.current_timestamp()
        v.show_result = form.results.data
        v.anonymous = form.anonymous.data
        db.session.commit()

        newOption1 = request.form.get("option1")
        o1.name = newOption1
        o1.description = request.form.get('option1Description')
        db.session.commit()

        newOption2 = request.form.get("option2")
        o2.name = newOption2
        o2.description = request.form.get('option2Description')
        db.session.commit()

        newOption3 = request.form.get("option3")
        o3.name = newOption3
        o3.description = request.form.get('option3Description')
        db.session.commit()

        return redirect(url_for("votings_index"))

    else:

        return render_template("votings/edit.html", voting=v, options=options, form=form)


@app.route("/votings/<voting_id>/del", methods=["POST", "GET"])
@login_required
def votings_delete(voting_id):

    v = Voting.query.get(voting_id)
    db.session.delete(v)
    db.session().commit()

    return redirect(url_for("votings_index"))


@app.route("/votings/all")
@login_required
def votings_listAllVotings():

    votings = Voting.query.all()

    return render_template("votings/listAllVotings.html", votings=votings)


@app.route("/votings/own")
@login_required
def votings_own():

    user_id = current_user.id

    votings = Voting.query.filter(Voting.account_id == user_id).all()

    return render_template("votings/ownVotings.html", votings=votings)


@app.route("/votings/notVoted")
@login_required
def votings_notVoted():

    user_id = current_user.id
    votingsToVoteNow = Voting.getVotingsThatCanbeVotedNow(user_id)
    votingsToVoteLater = Voting.getVotingsThatCanbeVotedLater(user_id)


    return render_template("votings/votingsToVote.html", votingsNow=votingsToVoteNow, votingsLater=votingsToVoteLater)


@app.route("/votings/voted")
@login_required
def votings_voted():

    user_id = current_user.id
    votings = UserVoted.getVotedVotings(user_id)

    return render_template("votings/votedVotings.html", votings=votings)





