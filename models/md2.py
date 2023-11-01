from .base import db


class User2(db.Model):
    __tablename__ = 'users2'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), unique=True)