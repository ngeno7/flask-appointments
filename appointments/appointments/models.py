from sqlalchemy import func
from ..db import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, default=0, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="cascade"))
