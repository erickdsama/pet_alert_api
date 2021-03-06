import sqlalchemy
from flask import request, jsonify
from flask_restful import Resource, reqparse
from marshmallow import ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from app.api.schemas import OwnerSchema
from app.models import Owner

owner_schema = OwnerSchema()  # type: SQLAlchemyAutoSchema


class OwnerResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, action='append', help='Rate cannot be converted')
        args = parser.parse_args()
        list_ids = []
        if "id" in args:
            list_ids = args.get("id", [])
        pets = Owner.query.filter(Owner.id.in_(list_ids)).all()
        list_pets = owner_schema.dump(pets, many=True)
        return jsonify(list_pets)

    def post(self):
        data = request.get_json()
        try:
            owner_model = owner_schema.load(data, instance=Owner(), partial=True)
        except ValidationError as e:
            return jsonify(e.messages)
        try:
            db.session.add(owner_model)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
            print("errdsadsadsaor", data.get("email"))
            try:
                owner_model = Owner.query.filter(Owner.email == data.get("email")).first()
            except Exception as e:
                print("ERRROR", e)

        return owner_schema.dump(owner_model)
