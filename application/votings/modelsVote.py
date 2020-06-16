from application import db
from datetime import datetime
from sqlalchemy.sql import text
import datetime
from datetime import datetime
import os



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

            time_to = time_to - 6

            if(time_to==-1):
                time_to=23
            if(time_to==-2):
                time_to=22
            if(time_to==-3):
                time_to=21
            if(time_to==-4):
                time_to = 20
            if (time_to==-5):
                time_to=19
            if(time_to==-6):
                time_to=18
           


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

