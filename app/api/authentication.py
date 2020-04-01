
from flask_jwt_extended import create_access_token

from flask import jsonify, request
from . import api


@api.route('/auth', methods=["POST"])
def get_jwt():
    pass
