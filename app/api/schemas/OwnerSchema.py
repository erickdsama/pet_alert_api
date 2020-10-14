from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema

from app import db
from app.models import Owner


class OwnerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Owner
        sqla_session = db.session
        load_instance = True

    id = auto_field()
