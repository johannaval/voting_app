from application import db
from application.models import Base
from datetime import datetime
from sqlalchemy.sql import text
import datetime
from datetime import datetime



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

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time <= :current_time "
                    "and ending_time > :current_time "
                    "and anonymous = 2 "
                    "GROUP BY id").params(current_time = current_time)

        res = db.engine.execute(stmt)
        list_all = []

        for row in res:
            list_all.append(row)

        return list_all


    @staticmethod
    def get_anonymous_votings_that_can_be_voted_later():

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time > :current_time "
                    "and anonymous = 2 "
                    "GROUP BY id").params(current_time = current_time)

        res = db.engine.execute(stmt)
        list_all = []

        for row in res:
            list_all.append(row)

        return list_all



    @staticmethod
    def get_votings_that_can_be_voted_now(user_id):

        voted = text(
            "SELECT * FROM User_Voted WHERE user_id = :user_id GROUP BY voting_id, id, user_id").params(user_id=user_id)

        res2 = db.engine.execute(voted)
        response2 = []

        for row in res2:
            response2.append(row)
        
        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE account_id != :user_id "
                    "and starting_time <= :current_time "
                    "and ending_time > :current_time "
                    "GROUP BY id").params(user_id=user_id, current_time = current_time)

        res = db.engine.execute(stmt)
        cleaned_list = []

        response = []

        for row in res:
            response.append(row)
            cleaned_list.append(row)

        len1 = len(response)
        len2 = len(response2)

        new_index = 0

        for j in range(len1):
            for i in range(len2):
                new_index = new_index + 1
                if(response[j].id == response2[i].voting_id):
                    cleaned_list.remove(response[j])
                    new_index = new_index - 1

        return cleaned_list

    @staticmethod
    def get_votings_that_can_be_voted_later(user_id):

        voted = text(
            "SELECT * FROM User_Voted WHERE user_id = :user_id GROUP BY voting_id, id, user_id").params(user_id=user_id)

        res2 = db.engine.execute(voted)
        response2 = []

        for row in res2:
            response2.append(row)

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE account_id != :user_id "
                    "and starting_time > :current_time "
                    "GROUP BY id").params(user_id=user_id, current_time = current_time)

        res = db.engine.execute(stmt)
        cleaned_list = []

        response = []

        for row in res:
            response.append(row)
            cleaned_list.append(row)

        len1 = len(response)
        len2 = len(response2)

        new_index = 0

        for j in range(len1):
            for i in range(len2):
                new_index = new_index + 1
                if(response[j].id == response2[i].voting_id):
                    cleaned_list.remove(response[j])
                    new_index = new_index - 1

        return cleaned_list
 
    @staticmethod
    def get_own_waiting_votings(user_id):

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time > :current_time "
                    "and account_id = :user_id "
                    "GROUP BY id").params(current_time = current_time, user_id=user_id)

        res = db.engine.execute(stmt)
        list_all = []

        for row in res:
            list_all.append(row)

        return list_all


    @staticmethod
    def get_own_started_votings(user_id):

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE starting_time < :current_time "
                    "and ending_time > :current_time "
                    "and account_id = :user_id "
                    "GROUP BY id").params(current_time = current_time, user_id=user_id)

        res = db.engine.execute(stmt)
        list_all = []

        for row in res:
            list_all.append(row)

        return list_all

    @staticmethod
    def get_own_ended_votings(user_id):

        current_time = datetime.now()

        stmt = text("SELECT * FROM VOTING "
                    "WHERE ending_time < :current_time "
                    "and account_id = :user_id "
                    "GROUP BY id").params(current_time = current_time, user_id=user_id)

        res = db.engine.execute(stmt)
        list_all = []

        for row in res:
            list_all.append(row)

        return list_all
