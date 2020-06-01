from application import db
from application.models import Base
from datetime import datetime
from sqlalchemy.sql import text


class Voting(Base):
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
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
    def isVotingNameUnique(name):

        stmt = text("SELECT Voting.name FROM Voting "
                    "WHERE Voting.name =:name").params(name=name)

        result = db.engine.execute(stmt).first()

        if (result == None):
            return True
        else:
            return False

    @staticmethod
    def isOptionsDifferent(list):

        print(list[0])
        print(list[1])
        print(list[2])

        if (list[0] == list[1] or list[0] == list[2] or list[1] == list[2]):
            return False
        else:
            return True


class Option(db.Model):
    option_id = db.Column(db.Integer, primary_key=True)
    voting_id = db.Column(db.Integer)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)

    def __init__(self, name):
        self.name = name


class UserVoted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    voting_id = db.Column(db.Integer)

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def getVotedVotings(user_id):

        stmt = text("SELECT name FROM Voting "
                    "LEFT JOIN User_Voted ON User_Voted.voting_id = Voting.id "
                    "WHERE User_Voted.user_id =:user_id "
                    "GROUP BY Voting.name").params(user_id=user_id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response

    @staticmethod
    def has_voted(u_id, v_id):

        stmt = text("SELECT user_id FROM User_Voted "
                    "WHERE user_id = :u_id AND voting_id = :v_id").params(u_id=u_id, v_id=v_id)

        result = db.engine.execute(stmt).first()

        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print (result)

        if (result == None):
            return False
        else:
            return True


class Vote(db.Model):
    vote_id = db.Column(db.Integer, primary_key=True)
    voting_id = db.Column(db.Integer)
    option_id = db.Column(db.Integer)
    time = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, voting_id):
        self.voting_id = voting_id

    @staticmethod
    def return_top_3_votes_in_vote(id):

        stmt = text("SELECT Option.name, COUNT(Vote.option_id) FROM Option "
                    "LEFT JOIN Vote ON Vote.option_id = Option.option_id "
                    "WHERE Option.voting_id = :id "
                    "GROUP BY option.name "
                    "ORDER BY count(Vote.option_id) DESC").params(id=id)

        res = db.engine.execute(stmt)
        response = []
        line = ""

        for row in res:
            line = row[0], row[1]
            result = " ".join(str(x) for x in line)
            response.append(result)

        return response
