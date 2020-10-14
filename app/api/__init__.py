from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__)
api_rest = Api(api_bp)

from app.api.pet import PetResource
from app.api.owner import OwnerResource

api_rest.add_resource(PetResource, '/pet/')
api_rest.add_resource(OwnerResource, '/owner/')


