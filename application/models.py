from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
