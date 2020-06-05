from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"
  
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)


    votings = db.relationship("Voting", backref='account', lazy=True)


    def __init__(self, name, username, password, is_admin):
        self.name = name
        self.username = username
        self.password = password
        self.is_admin = is_admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if (self.is_admin == True):
            return "ADMIN"
        else:
            return "ANY"
