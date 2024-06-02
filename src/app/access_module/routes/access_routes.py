from flask import Blueprint, request, jsonify
from urllib.parse import quote
access_routes = Blueprint('access_routes', __name__)

from app.access_module.service.module_access_service_function import access_service_function

@access_routes.route('/endpoint1', methods=['GET'])
def module_access_endpoint1():
    param = request.args.get('param')
    result = access_service_function(quote(param))
    return jsonify({"result": result})
