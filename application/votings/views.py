from flask import render_template, request, redirect, url_for
from flask_login import current_user
from application import app, db, login_required
from application.votings.modelsOption import Option
from application.votings.modelsUserVoted import UserVoted
from application.votings.modelsVote import Vote
from application.votings.modelsVoting import Voting
from application.votings.forms import VotingForm
from application.votings.forms import VoteForm
from datetime import datetime



@app.route("/votings", methods=["GET"])
def votings_index():

    votings_to_vote_now =[]
    votings_to_vote_later=[]

    if not current_user.is_authenticated:

       votings_to_vote_now = Voting.get_anonymous_votings_that_can_be_voted_now()
       votings_to_vote_later = Voting.get_anonymous_votings_that_can_be_voted_later()
    
    top_votings = []
    top_votings = Voting.get_top_3_votings_that_are_on()

    sum_of_this_user_has_voted  = 0
    
    if current_user.is_authenticated:
        user_id = current_user.id
        sum_of_this_user_has_voted = Voting.how_many_times_this_user_has_voted(current_user.id)

    sum_of_voted_votings = Voting.how_many_times_users_have_voted()

    get_most_voted_option = Voting.get_most_voted_options()
    if (len(get_most_voted_option)>0):
        most_voted = get_most_voted_option[0]
    else:
        most_voted = ""


    return render_template("votings/list.html", votingsToVoteNow=votings_to_vote_now, votingsToVoteLater = votings_to_vote_later, top_votings=top_votings, 
    sum_of_this_user_has_voted = sum_of_this_user_has_voted, whole_sum =sum_of_voted_votings, most_voted=most_voted)




@app.route("/votings/new/")
@login_required
def votings_form():

    return render_template("votings/new.html", form=VotingForm())





@app.route("/votings/vote/<voting_id>/", methods=["GET", "POST"])
def votings_vote(voting_id):

    data = Option.query.filter(Option.voting_id == voting_id).all()
    result = []
    v = Voting.query.get(voting_id)

    creator = v.account_id
    current = 999

    current_time = datetime.now()
    is_on = False
    
    if (v.starting_time < current_time):
        is_on = True

    if current_user.is_authenticated:
        current = current_user.id

    user_has_voted = UserVoted.has_voted(current, voting_id)

    if not is_on:
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

    form = VoteForm(request.form)

    selected = None
    if (len(data)==3):
        selected = form.answer.data
    if (len(data)==4):
        selected = form.answer4.data
    if (len(data)==5):
        selected = form.answer5.data
    if (len(data)==6):
        selected = form.answer6.data
    

    if selected == None:

            if (v.starting_time < current_time):
               is_on = True

            error = ""
            return render_template("votings/vote.html", voting=v, data=data, form=form, separated_time=separated_time, user_has_voted=user_has_voted, isOn = is_on, error=error, current = current, creator = creator)


    if request.method=="POST":


        if selected == None:
           error = "Oops! Valitsethan vaihtoehdon!"
           return render_template("votings/vote.html", voting=v, data=data, form=form, separated_time=separated_time, user_has_voted=user_has_voted, isOn = is_on, error=error, current = current, creator = creator)

        if current_user.is_authenticated:
           user = current_user
           user_vote = UserVoted(voting_id)
           user_vote.voting_id = voting_id
           user_vote.user_id = current_user.id
           db.session.add(user_vote)
           db.session.commit()

        voted=""
        voted = selected
        index = int(voted)-1
        op = data[index]

        new_vote = Vote(voting_id)
        new_vote.voting_id = int(voting_id)

        new_vote.option_id = op.option_id

        db.session.add(new_vote)
        db.session.commit()


        if not current_user.is_authenticated:
            return redirect(url_for("votings_index"))

        else:
            return redirect(url_for("votings_not_voted"))


@app.route("/votings/show/<voting_id>", methods=["GET"])
@login_required
def votings_show_this(voting_id):

    v = Voting.query.get(voting_id)
    data = Option.query.filter(Option.voting_id == voting_id).all()

    result = []
    text = []
    list = []

    if v.show_result == 2 and v.account_id != current_user.id:
        text.append("Kolme eniten ääniä saanutta vaihtoehtoa: ")
        list = Vote.return_top_3_votes_in_voting(voting_id)

    elif v.show_result == 1 and v.account_id != current_user.id:
        text.append("")

    elif v.show_result == 3 or v.account_id == current_user.id:
        text.append("Kaikki äänet: ")
        list = Vote.return_votes_in_voting(voting_id)

  
    creator = v.account_id
    current = 999

    if current_user.is_authenticated:
        current = current_user.id

    name = Voting.query.get(voting_id)
    user_has_voted = UserVoted.has_voted(current, voting_id)

    count_by_hour = []

    i = 0
    for i in range(24):
        count_by_hour.append(Vote.get_votes_in_time(voting_id, i))


    return render_template("votings/showVotingResults.html", voting=v, data=data, creator=creator, current=current, list=list, text=text, user_has_voted=user_has_voted, form=VoteForm(), time_count=count_by_hour)




@app.route("/votings/", methods=["POST", "GET"])
@login_required
def votings_create():


    form = VotingForm(request.form)

    if request.method == "GET":
        return render_template("votings/new.html", form=VotingForm())

    form = VotingForm(request.form)
    error = ""

    name = form.name.data

    list = []
    list.append(form.option1.data)
    list.append(form.option2.data)
    list.append(form.option3.data)

    if (len(form.option4.data)>0):
        list.append(form.option4.data)

    if (len(form.option5.data)>0):
        list.append(form.option5.data)

    if (len(form.option6.data)>0):
        list.append(form.option6.data)



    if(Voting.is_options_different(list) == False):
        error = "Jokainen vaihtoehto pitää olla eri!"
        return render_template("votings/new.html", form=form, error=error)

    if Voting.is_voting_name_unique(name) == False:
        error = "Tällä nimellä on jo äänestys!"
        return render_template("votings/new.html", form=form, error=error)


    if not form.validate() or form.starting_time.data >= form.ending_time.data:

        v = Voting(form.name.data)

        timeError= ""

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

    if (len(form.option4.data)>0):
        o4 = Option(form.option4.data)
        o4.name = form.option4.data
        o4.description = form.option4Description.data
        o4.voting_id = v.id
        db.session().add(o4)

    if (len(form.option5.data)>0):
        o5 = Option(form.option5.data)
        o5.name = form.option5.data
        o5.description = form.option5Description.data
        o5.voting_id = v.id
        db.session().add(o5)

    if (len(form.option6.data)>0):
        o6 = Option(form.option6.data)
        o6.name = form.option6.data
        o6.description = form.option6Description.data
        o6.voting_id = v.id
        db.session().add(o6)


    db.session().commit()

    return redirect(url_for("votings_index"))


@app.route("/votings/edit/<voting_id>", methods=["GET", "POST"])
@login_required
def votings_edit(voting_id):

    v = Voting.query.get(voting_id)

    if not current_user.is_admin:
        if v.account_id != current_user.id:
           return redirect(url_for("votings_index"))


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

    if (len(form.option4.data)>0):
        list.append(form.option4.data)

    if (len(form.option5.data)>0):
        list.append(form.option5.data)

    if (len(form.option6.data)>0):
        list.append(form.option6.data)


    options = Option.query.filter(Option.voting_id == voting_id).all()

    o1 = options[0]
    o2 = options[1]
    o3 = options[2]

    timeError=""


    if request.method=="POST":
       error = ""

       if ((len(form.option5.data)!=0 and len(form.option4.data)==0) or (len(form.option6.data)!=0 and len(form.option4.data)==0) or
       (len(form.option6.data)!=0 and len(form.option5.data)==0)):
            error = "Täytäthän kysymyskentät järjestyksessä!"
            return render_template("votings/edit.html", form=form, error=error, voting=v, options = options, current = current, creator = creator)


       if(Voting.is_options_different(list) == False):
            error = "Jokainen vaihtoehto pitää olla eri!"
            return render_template("votings/edit.html", form=form, error=error, voting=v, options = options, current = current, creator = creator)

       if Voting.is_voting_name_unique(name) == False and Voting.query.get(voting_id).name != request.form.get("name"):
            error = "Tällä nimellä on jo äänestys!"
            return render_template("votings/edit.html", form=form, error=error, voting = v, options = options, current = current, creator = creator)

       if not form.validate():
            return render_template("votings/edit.html", form=form, error= error, voting= v, options= options, current = current, creator = creator)
    
     
       if not form.validate() or form.starting_time.data >= form.ending_time.data or error=="Jokainen vaihtoehto pitää olla eri!":

           timeError=""

           if(form.starting_time.data >= form.ending_time.data):
               timeError = "Ops! Valitsethan äänestyksen päättymisajaksi myöhemmän ajan kuin alkamisaika!"

           return render_template("votings/edit.html", form=form, error= error, timeError=timeError, voting=v, options = options, current = current, creator = creator)


    if request.method == "POST" and form.validate():

        new_name = request.form.get("name")
        v.name = new_name
        v.date_modified = datetime.now()

        v.show_result = form.results.data
        v.anonymous = form.anonymous.data

        v.starting_time = form.starting_time.data
        v.ending_time = form.ending_time.data
        db.session.commit()

        new_option_1 = request.form.get("option1")
        o1.name = new_option_1
        o1.description = request.form.get('option1Description')
        db.session.commit()

        new_option_2 = request.form.get("option2")
        o2.name = new_option_2
        o2.description = request.form.get('option2Description')
        db.session.commit()

        new_option_3 = request.form.get("option3")
        o3.name = new_option_3
        o3.description = request.form.get('option3Description')
        db.session.commit()

        if (len(form.option4.data)>0):
            if (Option.count_options_from_voting(voting_id)>3):
                o4 = options[3]
                new_option_4 = request.form.get("option4")
                o4.name = new_option_4
                o4.description = request.form.get('option4Description')
            else:
                o4 = Option(form.option4.data)
                o4.name = form.option4.data
                o4.description = form.option4Description.data
                o4.voting_id = v.id
                db.session().add(o4)
               
            db.session.commit()

        if (len(form.option4.data)==0 and Option.count_options_from_voting(voting_id)>3):

                opt = options[3]
                db.session.delete(opt)
                db.session().commit()


        if (len(form.option5.data)>0):
            if (Option.count_options_from_voting(voting_id)>4):
                o5 = options[4]
                new_option_5 = request.form.get("option5")
                o5.name = new_option_5
                o5.description = request.form.get('option5Description')
            else:
                o5 = Option(form.option5.data)
                o5.name = form.option5.data
                o5.description = form.option5Description.data
                o5.voting_id = v.id
                db.session().add(o5)
               
            db.session.commit()

        if (len(form.option5.data)==0 and Option.count_options_from_voting(voting_id)>4):

                opt = options[4]
                db.session.delete(opt)
                db.session().commit()



        if (len(form.option6.data)>0):
            if  (Option.count_options_from_voting(voting_id)>5):
                o6 = options[5]
                new_option_6 = request.form.get("option6")
                o6.name = new_option_6
                o6.description = request.form.get('option6Description')
            else:
                o6 = Option(form.option6.data)
                o6.name = form.option6.data
                o6.description = form.option6Description.data
                o6.voting_id = v.id
                db.session().add(o6)
               
            db.session.commit()

        if (len(form.option6.data)==0 and Option.count_options_from_voting(voting_id)>5):

                opt = options[5]
                db.session.delete(opt)
                db.session().commit()

        if (v.account_id != current_user.id and current_user.is_admin):
           return redirect(url_for("votings_list_all_votings"))

        else:
            return redirect(url_for("votings_own"))

    else:

        return render_template("votings/edit.html", voting=v, options=options, form=form, current = current, creator = creator, timeError = timeError)



@app.route("/votings/delete/<voting_id>", methods=["POST", "GET"])
@login_required
def votings_delete(voting_id):

    v = Voting.query.get(voting_id)

    if not current_user.is_admin:
        if v.account_id != current_user.id:
           return redirect(url_for("votings_index"))

    db.session.delete(v)
    db.session().commit()


    if (v.account_id != current_user.id and current_user.is_admin):
        return redirect(url_for("votings_list_all_votings"))

    else:
        return redirect(url_for("votings_own"))



@app.route("/votings/all")
@login_required
def votings_list_all_votings():

    if not current_user.is_admin:
        return redirect(url_for("votings_index"))

    per_one_page = 5
    page = 1

    page = request.args.get('page', 1, type=int)
    votings = Voting.query.paginate(page, per_one_page, False)

    next_page = None
    previous_page = None

    if votings.has_next:
        next_page = url_for('votings_list_all_votings', page=votings.next_num) \
  
    if votings.has_prev:
         previous_page = url_for('votings_list_all_votings', page=votings.prev_num) \


    return render_template("votings/listAllVotings.html", votings=votings, next_url = next_page, prev_url=previous_page)




@app.route("/votings/own")
@login_required
def votings_own():


    user_id = current_user.id
    votings = Voting.query.filter(Voting.account_id == user_id).all()

    waiting_votings = Voting.get_own_waiting_votings(user_id)
    started_votings = Voting.get_own_started_votings(user_id)
    ended_votings = Voting.get_own_ended_votings(user_id)

    return render_template("votings/ownVotings.html", waitingVotings = waiting_votings, startedVotings = started_votings, endedVotings = ended_votings)



@app.route("/votings/created_by/<user_id>")
@login_required
def votings_show_votings_by_id(user_id):


    if not current_user.is_admin:
        return redirect(url_for("votings_index"))


    votings = Voting.query.filter(Voting.account_id == user_id).all()

    waiting_votings = Voting.get_own_waiting_votings(user_id)
    started_votings = Voting.get_own_started_votings(user_id)
    ended_votings = Voting.get_own_ended_votings(user_id)

    creator = user_id
    current = current_user.id


    return render_template("votings/ownVotings.html", creator = creator, current = current, waitingVotings = waiting_votings, startedVotings = started_votings, endedVotings = ended_votings)



@app.route("/votings/not_voted")
@login_required
def votings_not_voted():

    user_id = current_user.id
    votings_to_vote_now = Voting.get_votings_that_can_be_voted_now(user_id)
    votings_to_vote_later = Voting.get_votings_that_can_be_voted_later(user_id)


    return render_template("votings/votingsToVote.html", votingsNow=votings_to_vote_now, votingsLater=votings_to_vote_later)




@app.route("/votings/voted")
@login_required
def votings_voted():

    user_id = current_user.id
    votings = UserVoted.get_voted_votings(user_id)

    return render_template("votings/votedVotings.html", votings=votings)




@app.route("/voting_search/")
@login_required
def votings_search():

    query = request.args['search']

    voting = Voting.query.filter(Voting.name == query).first()
    user_id = current_user.id

    if (voting == None):
        return redirect(redirect_url())


    if (voting.account_id == user_id or UserVoted.has_voted(user_id, voting.id)):
        return redirect(url_for("votings_show_this", voting_id = voting.id))


    return redirect(url_for("votings_vote", voting_id = voting.id))




def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

