import json
from flask import render_template, request, session, redirect, Blueprint
from werkzeug.security import generate_password_hash

from project.models import FilmList, User_backlog, User
from project.utils import AlchemyEncoder
from . import db
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
    query = FilmList.query.join(User_backlog, FilmList.id == User_backlog.content_id) \
        .filter(User_backlog.user_id == session['id'], User_backlog.type == 'film')
    return render_template('user.html', film_list=query)


@main.route('/ajax/search', methods=['POST'])
def search():
    query = FilmList.query \
        .filter(FilmList.nameRu.ilike('%' + request.args.get('q') + '%')).limit(10).all()
    return json.dumps(query, cls=AlchemyEncoder)


@main.route('/search/film', methods=['POST'])
def add():
    film_id = 5
    # query = User_backlog.query(User_backlog.id, User_backlog.user_id) \
    #     .filter(User_backlog.id == film_id, User_backlog.user_id == session['id'])
    query = FilmList.query \
        .filter(FilmList.nameRu.ilike('%' + request.args.get('q') + '%')).paginate(10, 10, False)

    return render_template('user.html', film_list=query)
    for q in query:
        print(q)
        return "q"


@main.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.form.get('submit') is not None:
        email = request.form.get('email')
        passwd = request.form.get('password')
        username = request.form.get('username')
        if len(passwd) < 6:
            error = "Вы не прошли проверку длину пароля"
            return render_template('profile.html', error=error,
                                   email=email, username=username)
        User.query.filter(User.id == session['id']) \
            .update({'email': email, 'name': username, 'password': generate_password_hash(passwd, method='sha256')})
        db.session.commit()

    query = User.query.filter(User.id == session['id']).limit(1).all()
    return render_template('profile.html', user=query)
