from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config
from pathlib import Path

BASE_DIR = Path(__file__).parent

app = Flask(__name__, instance_path=BASE_DIR / "instance")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import cli_commands, error_handlers, views
