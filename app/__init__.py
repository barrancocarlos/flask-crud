from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
db = SQLAlchemy(app)

from app import models

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
