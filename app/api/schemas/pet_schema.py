from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema

from app import db
from app.models import Pet


class PetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        sqla_session = db.session
        load_instance = True

    id = auto_field()
