from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.get('/api')
def index():
    return jsonify({'apiVersions': ['v1']})
