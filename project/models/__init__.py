from flask.ext.sqlalchemy import SQLAlchemy
from project import app

db = SQLAlchemy()
db.init_app(app)