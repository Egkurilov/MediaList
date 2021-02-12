from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class FilmList(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_id = db.Column(db.String(250), nullable=False, server_default="")
    nameRu = db.Column(db.String(250), nullable=False, default="")
    nameEn = db.Column(db.String(250), nullable=False)
    kinopoiskUrl = db.Column(db.String(250), nullable=False)
    posterUrl = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    filmLength = db.Column(db.String(250), nullable=False)
    countries = db.Column(db.String(250), nullable=False)
    genres = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
