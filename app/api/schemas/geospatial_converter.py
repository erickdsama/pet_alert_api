from geoalchemy2 import Geography, WKTElement
from marshmallow import fields, ValidationError
from marshmallow_sqlalchemy import ModelConverter

from app import db
from app.utils.geo_functions import geodesic_point_buffer


class GeoConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({
        Geography: fields.Str
    })


class GeoPoint(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        lat = db.session.scalar(value.ST_Y())
        lon = db.session.scalar(value.ST_X())
        geo_radius = geodesic_point_buffer(lat, lon, 0.5)

        if value is None:
            return {
                "lat": 0,
                "lon": 0
            }
        return geo_radius

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return WKTElement('Point({} {})'.format(value.get("lon"), value.get("lat")), srid=4326)

        except ValueError as error:
            raise ValidationError("Error formating") from error
