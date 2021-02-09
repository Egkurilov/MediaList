from flask import Flask, render_template
from flask_migrate import Migrate, Manager, MigrateCommand

from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy

from secret import RECAPTCHA_SECRET_KEY, RECAPTCHA_SITE_KEY, secret_key, mysql_db, mysql_url, mysql_user, \
    mysql_password, mysql_port

db = SQLAlchemy()
recaptcha = ReCaptcha()


def page_not_found(e):
    return render_template('page404.html'), 404


def create_app():
    app = Flask(__name__)

    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.secret_key = secret_key

    app.config.update(dict(
        RECAPTCHA_ENABLED=True,
        RECAPTCHA_USE_SSL=False,
        RECAPTCHA_SITE_KEY=RECAPTCHA_SITE_KEY,
        RECAPTCHA_SECRET_KEY=RECAPTCHA_SECRET_KEY,
    ))

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{mysql_user}:{mysql_password}@{mysql_url}:{mysql_port}/{mysql_db}' \
                                            '?charset=utf8'.format(mysql_db=mysql_db, mysql_url=mysql_url,
                                                                   mysql_port=mysql_port, mysql_user=mysql_user,
                                                                   mysql_password=mysql_password)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_error_handler(404, page_not_found)
    recaptcha.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
