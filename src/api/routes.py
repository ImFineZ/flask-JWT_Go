"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

api = Blueprint('api', __name__)


@api.route('/token', methods=['POST'])
def create_token():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    if email != "test" or password != "test":
        print(email,password)
        return jsonify({"msg":"Wrong email or password"}), 401

    acces_token = create_access_token(identity=email)
    return jsonify(acces_token=acces_token)



@api.route('/hello', methods=['GET'])
def get_hello():

    dictionary = {
        "msg": "Hello World"
    }
    return jsonify(dictionary)