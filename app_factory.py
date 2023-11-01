from flask import Flask
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite",
    )
    db.init_app(app)
    return app
