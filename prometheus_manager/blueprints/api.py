from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/')
def index():
    return jsonify({'apiVersions': ['v1']})
