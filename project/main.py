from flask import Flask, render_template, request, flash, session, redirect, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def root():
    return render_template('index.html')


@main.route('/user')
def user_page():
    if 'username' in session:
        pass
    else:
        return redirect('/login')
    return render_template('user.html')


