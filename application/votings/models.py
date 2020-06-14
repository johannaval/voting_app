from application import db
from application.models import Base
from datetime import datetime
from sqlalchemy.sql import text
import datetime
from datetime import datetime
import os




class Voting(Base):
    date_created = db.Column(db.DateTime, default=db.func.LOCALTIMESTAMP())
    date_modified = db.Column(db.DateTime, default=db.func.LOCALTIMESTAMP(), onupdate=db.func.LOCALTIMESTAMP())
    description = db.Column(db.String(144), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)
    starting_time = db.Column(db.DateTime)
    ending_time = db.Column(db.DateTime)
    show_result = db.Column(db.Integer)
    anonymous = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.done = False

    @staticmethod
    def is_voting_name_unique(name):

        stmt = text("SELECT Voting.name FROM Voting "
                    "WHERE Voting.name =:name").params(name=name)

        result = db.engine.execute(stmt).first()

        if (result == None):
            return True
        else:
            return False

    @staticmethod
    def is_options_different(list):

        if len(list) > len(set(list)):
            return False

        else:
            return True

    @staticmethod
    def get_anonymous_votings_that_can_be_voted_now():

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time <= :currentTime "
                    "and ending_time > :currentTime "
                    "and anonymous = 2 "
                    "GROUP BY id").params(currentTime = currentTime)

        res = db.engine.execute(stmt)
        listAll = []

        for row in res:
            listAll.append(row)

        return listAll


    @staticmethod
    def get_anonymous_votings_that_can_be_voted_later():

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time > :currentTime "
                    "and anonymous = 2 "
                    "GROUP BY id").params(currentTime = currentTime)

        res = db.engine.execute(stmt)
        listAll = []

        for row in res:
            listAll.append(row)

        return listAll



    @staticmethod
    def get_votings_that_can_be_voted_now(user_id):

        voted = text(
            "SELECT * FROM User_Voted WHERE user_id = :user_id GROUP BY voting_id, id, user_id").params(user_id=user_id)

        res2 = db.engine.execute(voted)
        response2 = []

        for row in res2:
            response2.append(row)
        
        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE account_id != :user_id "
                    "and starting_time <= :currentTime "
                    "and ending_time > :currentTime "
                    "GROUP BY id").params(user_id=user_id, currentTime = currentTime)

        res = db.engine.execute(stmt)
        cleanedList = []

        response = []

        for row in res:
            response.append(row)
            cleanedList.append(row)

        len1 = len(response)
        len2 = len(response2)

        newIndex = 0

        for j in range(len1):
            for i in range(len2):
                newIndex = newIndex + 1
                if(response[j].id == response2[i].voting_id):
                    cleanedList.remove(response[j])
                    newIndex = newIndex - 1

        return cleanedList

    @staticmethod
    def get_votings_that_can_be_voted_later(user_id):

        voted = text(
            "SELECT * FROM User_Voted WHERE user_id = :user_id GROUP BY voting_id, id, user_id").params(user_id=user_id)

        res2 = db.engine.execute(voted)
        response2 = []

        for row in res2:
            response2.append(row)

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE account_id != :user_id "
                    "and starting_time > :currentTime "
                    "GROUP BY id").params(user_id=user_id, currentTime = currentTime)

        res = db.engine.execute(stmt)
        cleanedList = []

        response = []

        for row in res:
            response.append(row)
            cleanedList.append(row)

        len1 = len(response)
        len2 = len(response2)

        newIndex = 0

        for j in range(len1):
            for i in range(len2):
                newIndex = newIndex + 1
                if(response[j].id == response2[i].voting_id):
                    cleanedList.remove(response[j])
                    newIndex = newIndex - 1

        return cleanedList
 
    @staticmethod
    def get_own_waiting_votings(user_id):

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time > :currentTime "
                    "and account_id = :user_id "
                    "GROUP BY id").params(currentTime = currentTime, user_id=user_id)

        res = db.engine.execute(stmt)
        listAll = []

        for row in res:
            listAll.append(row)

        return listAll


    @staticmethod
    def get_own_started_votings(user_id):

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time < :currentTime "
                    "and ending_time > :currentTime "
                    "and account_id = :user_id "
                    "GROUP BY id").params(currentTime = currentTime, user_id=user_id)

        res = db.engine.execute(stmt)
        listAll = []

        for row in res:
            listAll.append(row)

        return listAll

    @staticmethod
    def get_own_ended_votings(user_id):

        currentTime = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE ending_time < :currentTime "
                    "and account_id = :user_id "
                    "GROUP BY id").params(currentTime = currentTime, user_id=user_id)

        res = db.engine.execute(stmt)
        listAll = []

        for row in res:
            listAll.append(row)

        return listAll








class Option(db.Model):
    option_id = db.Column(db.Integer, primary_key=True)
    voting_id = db.Column(db.Integer)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def count_options_from_voting(voting_id):

        stmt = text("SELECT * FROM Option "
                    "WHERE voting_id = :voting_id "
                    "GROUP BY option_id").params(voting_id=voting_id)

        res = db.engine.execute(stmt)
        response = []
        i = 0

        for row in res:    
            i = i + 1

        return i






 

class UserVoted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    voting_id = db.Column(db.Integer)

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def get_voted_votings(user_id):
        voted = text(
            "SELECT * FROM User_Voted WHERE user_id = :user_id GROUP BY voting_id, id, user_id").params(user_id=user_id)

        res2 = db.engine.execute(voted)
        response2 = []

        for row in res2:
            response2.append(row)

        stmt = text("SELECT * FROM VOTING "
                    "WHERE account_id != :user_id "
                    "GROUP BY id").params(user_id=user_id)

        res = db.engine.execute(stmt)
        cleanedList = []

        response = []

        for row in res:
            response.append(row)

        len1 = len(response)
        len2 = len(response2)

        for j in range(len1):
            for i in range(len2):
                if(response[j].id == response2[i].voting_id):
                    cleanedList.append(response[j])

        return cleanedList

    @staticmethod
    def has_voted(u_id, v_id):

        stmt = text("SELECT user_id FROM User_Voted "
                    "WHERE user_id = :u_id AND voting_id = :v_id").params(u_id=u_id, v_id=v_id)

        result = db.engine.execute(stmt).first()

        if (result == None):
            return False
        else:
            return True







class Vote(db.Model):
    vote_id = db.Column(db.Integer, primary_key=True)
    voting_id = db.Column(db.Integer)
    option_id = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=db.func.LOCALTIMESTAMP())



    def __init__(self, voting_id):
        self.voting_id = voting_id

    @staticmethod
    def return_votes_in_voting(id, count):

        if (count == "3"):

            stmt = text("SELECT Option.name, COUNT(Vote.option_id) FROM Option "
                        "LEFT JOIN Vote ON Vote.option_id = Option.option_id "
                        "WHERE Option.voting_id = :id "
                        "GROUP BY option.name "
                        "ORDER BY count(Vote.option_id) DESC LIMIT 3").params(id=id)
        else:
            stmt = text("SELECT Option.name, COUNT(Vote.option_id) FROM Option "
                        "LEFT JOIN Vote ON Vote.option_id = Option.option_id "
                        "WHERE Option.voting_id = :id "
                        "GROUP BY option.name "
                        "ORDER BY count(Vote.option_id) DESC").params(id=id)

        res = db.engine.execute(stmt)
        response = []
        line = ""

        for row in res:
            response.append(row)
            print(row)

        return response


    @staticmethod
    def get_votes_in_time(voting_id, time_to):

        
        if os.environ.get("HEROKU"):

            time_to = time_to + 3
           
            stmt = text("SELECT * FROM VOTE "
                       "WHERE extract(hour from time) = :time_to "
                       "AND voting_id = :voting_id "
                       "GROUP BY vote_id").params(voting_id=voting_id, time_to = time_to)

        else:

            time_to = str(time_to)

            stmt = text("SELECT * FROM Vote "
                    "WHERE strftime('%H', time) = :time_to "
                    "AND voting_id = :voting_id "
                    "GROUP BY vote_id").params(voting_id=voting_id, time_to = time_to)

        res = db.engine.execute(stmt)
        response = []
        i = 0

        for row in res:    
            i = i + 1

        return i


