from application import db
from application.models import Base
from datetime import datetime

class Voting(Base):
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    description = db.Column(db.String(144), nullable=True)
    done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    starting_time = db.Column(db.DateTime)
    ending_time = db.Column(db.DateTime())
    show_result = db.Column(db.Integer)
    anonymous = db.Column(db.Boolean)

    def __init__(self, name):
        self.name = name
        self.done = False


class Option(db.Model):
    option_id = db.Column(db.Integer, primary_key=True)
    voting_id = db.Column(db.Integer)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(144), nullable=True)
   
    def __init__(self, name):
        self.name = name


class User_Voted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    voting_id = db.Column(db.Integer)

    def __init__(self, user_id):
        self.user_id = user_id


