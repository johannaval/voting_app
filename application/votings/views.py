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

       votingsToVoteNow = Voting.get_anonymous_votings_that_can_be_voted_now()
       votingsToVoteLater = Voting.get_anonymous_votings_that_can_be_voted_later()


    return render_template("votings/list.html", votingsToVoteNow=votingsToVoteNow, votingsToVoteLater = votingsToVoteLater)


@app.route("/votings/new/")
@login_required
def votings_form():

    return render_template("votings/new.html", form=VotingForm())


@app.route("/votings/vote/<voting_id>/", methods=["GET", "POST"])
def votings_vote(voting_id):

    data = Option.query.filter(Option.voting_id == voting_id).all()
    result = []

    v = Voting.query.get(voting_id)

    teksti = []

    creator = v.account_id
    current = 999

    currentTime = datetime.now()
    isOn = False
    
    if (v.starting_time < currentTime):
        isOn = True

    if current_user.is_authenticated:
        current = current_user.id

    userHasVoted = UserVoted.has_voted(current, voting_id)

    if not isOn:
       time = v.starting_time

    else:
        time = v.ending_time

    separatedTime=[]
    separatedTime.append(time.strftime("%m"))
    separatedTime.append(time.strftime("%d"))
    separatedTime.append(time.strftime("%Y"))
    separatedTime.append(time.strftime("%H"))
    separatedTime.append(time.strftime("%M"))
    separatedTime.append(time.strftime("%S"))

    form = VoteForm(request.form)

    if not form.validate():

            if (v.starting_time < currentTime):
               isOn = True

            error = ""
            return render_template("votings/vote.html", voting=v, data=data, form=form, separated_time=separatedTime, user_has_voted=userHasVoted, isOn = isOn, error=error, current = current, creator = creator)


    if request.method=="POST":

        if not form.validate():
           error = "Valitsethan vaihtoehdon tääl!"
           return render_template("votings/vote.html", voting=v, data=data, form=form, separated_time=separatedTime, user_has_voted=userHasVoted, isOn = isOn, error=error, current = current, creator = creator)

        if current_user.is_authenticated:
           user = current_user
           userVote = UserVoted(voting_id)
           userVote.voting_id = voting_id
           userVote.user_id = current_user.id
           db.session.add(userVote)
           db.session.commit()

           voted=""
           voted = form.answer.data
           index = int(voted)-1
           op = data[index]

           newVote = Vote(voting_id)
           newVote.voting_id = int(voting_id)

           newVote.option_id = op.option_id

           db.session.add(newVote)
           db.session.commit()


        if not current_user.is_authenticated:
            return redirect(url_for("votings_index"))

        else:
            return redirect(url_for("votings_notVoted"))


@app.route("/votings/<voting_id>/show", methods=["GET"])
@login_required
def votings_show_this(voting_id):

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id == voting_id).all()


    result = []
    text = []
    list = []

    if v.show_result == 2:
        text.append("Kolme eniten ääniä saanutta vaihtoehtoa: : ")
        list = Vote.return_top_3_votes_in_voting(voting_id)

    elif v.show_result == 1:
        text.append("")

    elif v.show_result == 3:
        text.append("Kaikki äänet: ")
        list = Vote.return_top_3_votes_in_voting(voting_id)

    for l in list:
        l.replace("'", "")
        l.replace(" ", "   ")

    creator = v.account_id
    current = 999

    if current_user.is_authenticated:
        current = current_user.id

    name = Voting.query.get(voting_id)
    userHasVoted = UserVoted.has_voted(current, voting_id)

    countByHour = []

    countByHour.append(Vote.get_votes_in_time(voting_id, "00", "01"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "01", "02"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "02", "03"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "03", "04"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "04", "05"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "05", "06"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "06", "07"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "07", "08"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "08", "09"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "09", "10"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "10", "11"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "11", "12"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "12", "13"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "13", "14"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "14", "15"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "15", "16"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "16", "17"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "17", "18"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "18", "19"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "19", "20"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "20", "21"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "21", "22"))    
    countByHour.append(Vote.get_votes_in_time(voting_id, "22", "23"))
    countByHour.append(Vote.get_votes_in_time(voting_id, "23", "00"))

    return render_template("votings/showVotingResults.html", voting=v, data=data, creator=creator, current=current, list=list, teksti=text, user_has_voted=userHasVoted, form=VoteForm(), time_count=countByHour)



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

    if(Voting.is_options_different(list) == False):
        error = "Jokainen vaihtoehto pitää olla eri!"
        return render_template("votings/new.html", form=form, error=error)

    if Voting.is_voting_name_unique(name) == False:
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


    current = current_user.id
    creator = v.account_id

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

       if(Voting.is_options_different(list) == False):
          error = "Jokainen vaihtoehto pitää olla eri!"
          return render_template("votings/edit.html", form=form, error=error, voting=v, options = options, current = current, creator = creator)

       if Voting.is_voting_name_unique(name) == False and Voting.query.get(voting_id).name != request.form.get("name"):
          error = "Tällä nimellä on jo äänestys!"
          return render_template("votings/edit.html", form=form, error=error, voting = v, options = options, current = current, creator = creator)

       if not form.validate():
          return render_template("votings/edit.html", form=form, error= error, voting= v, options= options, current = current, creator = creator)
    

       if not form.validate() or form.starting_time.data >= form.ending_time.data:

           v = Voting(form.name.data)

           timeError=""

           if(form.starting_time.data >= form.ending_time.data):
               timeError = "Ops! Valitsethan äänestyksen päättymisajaksi myöhemmän ajan kuin alkamisaika!"

           return render_template("votings/edit.html", form=form, error= error, timeError=timeError, voting=v, options = options, current = current, creator = creator)


    if request.method == "POST" and form.validate():

        newName = request.form.get("name")
        v.name = newName
        v.date_modified = datetime.now()

        v.show_result = form.results.data
        v.anonymous = form.anonymous.data

        v.starting_time = form.starting_time.data
        v.ending_time = form.ending_time.data
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

        return render_template("votings/edit.html", voting=v, options=options, form=form, current = current, creator = creator)


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

    waitingVotings = Voting.get_own_waiting_votings(user_id)
    startedVotings = Voting.get_own_started_votings(user_id)
    endedVotings = Voting.get_own_ended_votings(user_id)

    return render_template("votings/ownVotings.html", waitingVotings = waitingVotings, startedVotings = startedVotings, endedVotings = endedVotings)

@app.route("/votings/created_by/<user_id>")
@login_required
def votings_show_votings_by_id(user_id):

    votings = Voting.query.filter(Voting.account_id == user_id).all()

    waitingVotings = Voting.get_own_waiting_votings(user_id)
    startedVotings = Voting.get_own_started_votings(user_id)
    endedVotings = Voting.get_own_ended_votings(user_id)

    creator = user_id
    current = current_user.id


    return render_template("votings/ownVotings.html", creator = creator, current = current, waitingVotings = waitingVotings, startedVotings = startedVotings, endedVotings = endedVotings)


@app.route("/votings/notVoted")
@login_required
def votings_notVoted():

    user_id = current_user.id
    votingsToVoteNow = Voting.get_votings_that_can_be_voted_now(user_id)
    votingsToVoteLater = Voting.get_votings_that_can_be_voted_later(user_id)


    return render_template("votings/votingsToVote.html", votingsNow=votingsToVoteNow, votingsLater=votingsToVoteLater)


@app.route("/votings/voted")
@login_required
def votings_voted():

    user_id = current_user.id
    votings = UserVoted.get_voted_votings(user_id)

    return render_template("votings/votedVotings.html", votings=votings)




 








