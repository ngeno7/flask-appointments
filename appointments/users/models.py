from ..db import db
from ..conf import login_manager
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           default=datetime.datetime.utcnow)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
