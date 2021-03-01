import os
from flask import Flask, render_template
from flask_migrate import Migrate, Manager, MigrateCommand
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from secret import secret_key, mysql_db, mysql_url, mysql_user, \
    mysql_password, mysql_port
from flask_session import Session

db = SQLAlchemy()
recaptcha = ReCaptcha()


def page_not_found(e):
    return render_template('page404.html'), 404


def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.secret_key = secret_key
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config["SESSION_FILE_DIR"] = os.path.join(app.root_path, "session")
    app.config['SESSION_KEY_PREFIX'] = 'session:'
    app.config.update(dict(
        RECAPTCHA_ENABLED=True,
        RECAPTCHA_USE_SSL=False,
        RECAPTCHA_SITE_KEY="6LcboUwaAAAAAB6iZ_936CmHdULkXqAHJU_216Kg",
        RECAPTCHA_SECRET_KEY="6LcboUwaAAAAAMLIuutVczc2VIT7jGACNE5v8Lta",
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

    app.config.from_object(__name__)
    Session(app)

    return app
