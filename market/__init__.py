from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
from market.models import Item
