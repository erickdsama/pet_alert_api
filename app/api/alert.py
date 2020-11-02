import decimal
import flask


from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import func
from marshmallow import ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from app.api.schemas.alert_schema import AlertSchema
from app.models import Alert

alert_schema = AlertSchema()  # type: SQLAlchemyAutoSchema




class AlertResource(Resource):
    def post(self):
        data = request.get_json()
        try:
            pet_model = alert_schema.load(data, instance=Alert(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        db.session.add(pet_model)
        db.session.commit()
        return alert_schema.dump(pet_model)


class AlertsResource(Resource):

    def get(self, lat, lon):
        alerts = Alert.query.filter(
            func.ST_Distance(
                Alert.lost_point, 'POINT({} {})'.format(lon, lat)
            ) < 100)
        list_pets = alert_schema.dump(alerts, many=True)
        return jsonify(list_pets)

    def post(self):
        data = request.get_json()
        try:
            pet_model = alert_schema.load(data, instance=Alert(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        db.session.add(pet_model)
        db.session.commit()
        return alert_schema.dump(pet_model)
