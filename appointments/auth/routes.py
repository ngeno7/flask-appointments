from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user, login_required, logout_user
from passlib.hash import pbkdf2_sha256
auth = Blueprint('auth', __name__)
from ..users.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       username = request.form.get('username')
       password = request.form.get('password')
       user = User.query.filter_by(username=username).first()

       if user and pbkdf2_sha256.verify(password, user.password):
           login_user(user)

           return redirect('/')

    return render_template('auth/login.html')

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('auth.login'))

    return redirect(url_for('auth.login'))