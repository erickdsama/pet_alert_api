from marshmallow import fields
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema

from app import db
from app.api.schemas.pet_schema import PetSchema
from app.api.schemas.geospatial_converter import GeoConverter, GeoPoint
from app.models import Alert


class AlertSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Alert
        model_converter = GeoConverter
        sqla_session = db.session
        load_instance = True
        include_fk = True

    id = auto_field()
    lost_point = GeoPoint()
    pet = fields.Nested(PetSchema)


