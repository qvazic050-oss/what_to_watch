"""Пакет приложения для работы с мнениями о фильмах."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import SECRET_KEY, SQLALCHEMY_DATABASE_URI


app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from opinions_app import cli_commands  # noqa: E402
from opinions_app import error_handlers  # noqa: E402
from opinions_app import models  # noqa: E402
from opinions_app import views  # noqa: E402
