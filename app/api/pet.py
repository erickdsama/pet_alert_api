from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from app.api.schemas.pet_schema import PetSchema
from app.models import Pet

pet_schema = PetSchema()  # type: SQLAlchemyAutoSchema


class PetResource(Resource):

    def get(self):
        pets = Pet.query.all()
        list_pets = pet_schema.dump(pets, many=True)
        return jsonify(list_pets)

    def post(self):
        data = request.get_json()
        try:
            pet_model = pet_schema.load(data, instance=Pet(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        db.session.add(pet_model)
        db.session.commit()
        return pet_schema.dump(pet_model)
