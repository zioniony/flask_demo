from .base import db


class User1(db.Model):
    __tablename__ = 'users1'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(50), unique=True)