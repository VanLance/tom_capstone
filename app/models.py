from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe

from app import db, login

# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password =db.Column(db.String(50), nullable=False)

    
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(50), nullable=False)
    instructions =db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Recipe'{self.title}'"