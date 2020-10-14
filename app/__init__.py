from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config

mail = Mail()
db = SQLAlchemy()
moment = Moment()
jwt_manager = JWTManager()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config['default'].init_app(app)

    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    jwt_manager.init_app(app)
    from .api import api_bp

    app.register_blueprint(api_bp)
    return app
