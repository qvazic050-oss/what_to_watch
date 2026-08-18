"""Пакет приложения для работы с мнениями о фильмах."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from settings import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from opinions_app import cli_commands  # noqa: E402
from opinions_app import error_handlers  # noqa: E402
from opinions_app import models  # noqa: E402
from opinions_app import views  # noqa: E402
