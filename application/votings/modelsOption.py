from application import db
from sqlalchemy.sql import text



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

