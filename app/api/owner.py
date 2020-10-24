from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from app.api.schemas import OwnerSchema
from app.models import Owner

owner_schema = OwnerSchema()  # type: SQLAlchemyAutoSchema


class OwnerResource(Resource):

    def get(self):
        pets = Owner.query.all()
        list_pets = owner_schema.dump(pets, many=True)
        return jsonify(list_pets)

    def post(self):
        data = request.get_json()
        try:
            pet_model = owner_schema.load(data, instance=Owner(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        db.session.add(pet_model)
        db.session.commit()
        return owner_schema.dump(pet_model)
