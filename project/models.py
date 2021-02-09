from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return '<User %r>' % self.name


class FilmList(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_id = db.Column(db.String(250), nullable=False)
    nameRu = db.Column(db.String(250), nullable=False)
    nameEn = db.Column(db.String(250), nullable=False)
    kinopoiskUrl = db.Column(db.String(250), nullable=False)
    posterUrl = db.Column(db.String(250), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    filmLength = db.Column(db.String(250), nullable=False)
    countries = db.Column(db.String(250), nullable=False)
    genres = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<BASE_FILM %r>' % self.nameEn
