from flask import Blueprint, request, jsonify, session
from flask_cors import CORS

data_api = Blueprint('data_api', 'data_api', url_prefix='/data')

CORS(data_api) # enable CORS

@data_api.route('/hello', methods=['GET'])
def hello():
    r = {
        "message": "Hello from DataController!"
    }
    return jsonify(r)

