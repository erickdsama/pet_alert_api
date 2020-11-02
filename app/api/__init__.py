from flask import Blueprint
from flask_restful import Api

from app.api.alert import AlertResource, AlertsResource

api_bp = Blueprint('api', __name__)
api_rest = Api(api_bp)

from app.api.pet import PetResource
from app.api.owner import OwnerResource

api_rest.add_resource(PetResource, '/pet/')
api_rest.add_resource(OwnerResource, '/owner/')
api_rest.add_resource(AlertResource, '/alert/')
api_rest.add_resource(AlertsResource, '/alert/<string:lon>/<string:lat>/')


