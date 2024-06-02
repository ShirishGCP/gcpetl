from flask import request, jsonify, Flask
from src.app.module_custodian.services.module_custodian_service_function import custodian_service_function
from src.app.module_access.services.module_access_service_function import access_service_function
from src.app.module_common.services.module_common_service_function import common_service_function
from urllib.parse import quote

def register_routes(app):
    @app.route('/custodian/endpoint1', methods=['GET'])
    def module_custodian_endpoint1():
        param = request.args.get('param')
        result = custodian_service_function(quote(param))
        return jsonify({"result": result})

    @app.route('/access/endpoint1', methods=['POST'])
    def module_access_endpoint1():
        data = request.json
        if 'param' not in data:
            return jsonify({"error": "Missing 'param' in request"}), 400
        
        param = data['param']
        result = access_service_function(param)
        result = quote(result)
        return jsonify({"result": result})

    @app.route('/common/endpoint', methods=['GET'])
    def module_common_endpoint():
        param = request.args.get('param')
        result = common_service_function(param)
        result = quote(result)
        return jsonify({"result": result})
