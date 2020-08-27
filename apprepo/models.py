from .import db

class User(db.Model):
    __tablename__='user'

    id = db.Column(
        db.Integer,
        primary_key=True,
        unique=True
        )
    username = db.Column(
        db.String(100)
        )
    department=db.Column(
        db.String(100)
        )

    def __repr__(self):
        return 'Username: {}'.format(self.username)