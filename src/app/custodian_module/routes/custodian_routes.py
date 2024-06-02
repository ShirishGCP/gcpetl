from flask import Blueprint, request, jsonify
from urllib.parse import quote  
custodian_routes = Blueprint('custodian_routes', __name__)

from app.custodian_module.service.module_custodian_service_function import custodian_service_function

@custodian_routes.route('/endpoint1', methods=['GET'])
def module_custodian_endpoint1():
    param = request.args.get('param')
    result = custodian_service_function(quote(param))
    return jsonify({"result": result})
