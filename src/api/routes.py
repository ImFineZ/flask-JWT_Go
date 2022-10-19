"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

api = Blueprint('api', __name__)



@api.route('/hello', methods=['GET'])
@jwt_required
def get_hello():

    dictionary = {
        "msg": "Hello World"
    }
    return jsonify(dictionary)