from pathlib import Path

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from settings import Config

BASE_DIR = Path(__file__).parent

app = Flask(__name__, instance_path=BASE_DIR / "instance")
app.config.from_object(Config)
app.config["JSON_AS_ASCII"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, cli_commands, error_handlers, views
