from application import db
from sqlalchemy.sql import text


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
        cleaned_list = []

        response = []

        for row in res:
            response.append(row)

        len1 = len(response)
        len2 = len(response2)

        for j in range(len1):
            for i in range(len2):
                if(response[j].id == response2[i].voting_id):
                    cleaned_list.append(response[j])

        return cleaned_list

    @staticmethod
    def has_voted(u_id, v_id):

        stmt = text("SELECT user_id FROM User_Voted "
                    "WHERE user_id = :u_id AND voting_id = :v_id").params(u_id=u_id, v_id=v_id)

        result = db.engine.execute(stmt).first()

        if (result == None):
            return False
        else:
            return True




