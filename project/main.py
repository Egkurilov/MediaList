import json
from flask import render_template, request, session, redirect, Blueprint
from project.models import FilmList
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
    query = FilmList.query \
        .filter(FilmList.nameRu.ilike('%Паук%')).limit(10)
    return render_template('user.html', film_list=query)


@main.route('/ajax/search', methods=['POST'])
def search():
    query = FilmList.query \
        .filter(FilmList.nameRu.ilike('%' + request.args.get('q') + '%')).limit(5).all()

    print(json.dumps(query, cls=AlchemyEncoder))
    return ""