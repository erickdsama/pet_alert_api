from marshmallow import fields, ValidationError
from marshmallow_sqlalchemy import ModelConverter
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema
from sqlalchemy import DECIMAL


from app import db
from app.api.schemas.owner_schema import OwnerSchema
from app.models import Pet


# class DecimalConverter(ModelConverter):
#     SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
#     SQLA_TYPE_MAPPING.update({
#         DECIMAL: fields.Decimal
#     })

class PetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        sqla_session = db.session
        load_instance = True

    id = auto_field()
    owner = fields.Nested(OwnerSchema)

