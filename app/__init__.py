import decimal

from flask import json
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DECIMAL

from config import config

mail = Mail()
db = SQLAlchemy()
moment = Moment()
jwt_manager = JWTManager()
ma = Marshmallow()



class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        print(type(obj))
        if isinstance(obj, decimal.Decimal):
            # Convert decimal instances to strings.
            return float(str(obj))
        return super(MyJSONEncoder, self).default(obj)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config['default'].init_app(app)

    app.json_encoder = MyJSONEncoder
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    jwt_manager.init_app(app)
    from .api import api_bp

    app.register_blueprint(api_bp)
    return app
