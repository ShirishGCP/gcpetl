from flask import Flask, request, jsonify
from app.custodian_module.routes.custodian_routes import custodian_routes
from app.access_module.routes.access_routes import access_routes
from app.config_module.routes.config_routes import config_routes

app = Flask(__name__)
app.register_blueprint(custodian_routes, url_prefix='/custodian')
app.register_blueprint(access_routes, url_prefix='/access')
app.register_blueprint(config_routes, url_prefix='/config')

if __name__ == '__main__':
    app.run(debug=True)    


  

