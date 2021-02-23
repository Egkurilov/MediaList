import re

from flask import Flask, render_template, request, flash, session, redirect, app, Blueprint

from werkzeug.security import generate_password_hash, check_password_hash
from . import recaptcha
from . import db
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    email = request.form.get('email')
    passwd = request.form.get('password')

    if 'username' in session:
        return redirect('/user')

    if email is not None and passwd is not None:
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, passwd):
            session['username'] = email
            session['id'] = user.id
            return redirect('/user')
        else:
            error = "Что то пошло не так"
            return render_template('auth/login.html', error=error)
    return render_template('auth/login.html')


@auth.route('/register', methods=['POST', 'GET'])
def registration():
    if request.form.get('submit') is not None:
        email = request.form.get('email')
        passwd = request.form.get('password')
        username = request.form.get('username')

        if recaptcha.verify() is False:
            error = "Вы не прошли проверку recaptcha"
            return render_template('auth/registration.html', error=error,
                                   email=email, username=username)

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            error = "Вы не прошли проверку на email"
            return render_template('auth/registration.html', error=error,
                                   email=email, username=username)
        if len(passwd) < 6:
            error = "Вы не прошли проверку длину пароля"
            return render_template('auth/registration.html', error=error,
                                   email=email, username=username)

        user = User.query.filter_by(email=email).first()
        if user:
            return redirect('/login')

        new_user = User(email=email, name=username, password=generate_password_hash(passwd, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        session['username'] = email
        return redirect('/login')

    return render_template('auth/registration.html')
