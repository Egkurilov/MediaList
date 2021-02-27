import json
from flask import render_template, request, session, redirect, Blueprint
from project.models import FilmList, User_backlog
from project.utils import AlchemyEncoder

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
        .filter(FilmList.nameRu.ilike('%' + request.args.get('q') + '%')).limit(5).all()

    print(json.dumps(query, cls=AlchemyEncoder))
    return ""


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
