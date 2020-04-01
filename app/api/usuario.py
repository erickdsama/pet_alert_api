import sqlalchemy
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app import db
from flask import request, jsonify, json, Response
from . import api


@api.route('/user', methods=["POST"])
def add_user():
    pass


@api.route('/user/<int:id>', methods=["DELETE"])
@jwt_required
def delete_user(id):
    pass


@api.route('/user/confirm/<string:uuid>', methods=["GET"])
def confirm_user(uuid):
    pass


@api.route('/user/<int:id>', methods=["PATCH"])
@jwt_required
def edit_user(id):
    pass


@api.route('/user/<int:id>', methods=["GET"])
@jwt_required
def get_user(id):
    pass


@api.route('/users', methods=["GET"])
@jwt_required
def get_users():
    pass