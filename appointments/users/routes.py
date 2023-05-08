from flask import Blueprint, render_template, request, redirect, url_for
from passlib.hash import pbkdf2_sha256

users = Blueprint('users', __name__, template_folder='templates')
from .models import User
from ..db import db

@users.route('/users', methods=['GET', 'POST'])
def index():
    user = User()
    if request.form.get('id'):
        user = User.query.filter_by(id=request.form.get('id')).first()
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.username = request.form.get('username')
        user.password = pbkdf2_sha256.hash(request.form.get('password'))
        user.active = True
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.index'))

    return render_template("users/index.html", title='Users', users=user.query.all())
