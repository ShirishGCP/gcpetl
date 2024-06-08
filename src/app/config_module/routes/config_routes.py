from flask import Blueprint, request, jsonify
from urllib.parse import quote
config_routes = Blueprint('config_routes', __name__)

from app.config_module.service.config_reader import config_reader

@config_routes.route('/', methods=['GET'])
def get_config():
    return jsonify(config_reader.get_config())


@config_routes.route('/<group>', methods=['GET'])
def get_group_config(group):
    group_config = config_reader.get_group_config(group)
    if group_config:
        return jsonify(group_config)
    else:
        return jsonify({"error": "Group not found"}), 404
