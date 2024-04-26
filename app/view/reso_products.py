from flask_restful import Resource, reqparse
from app.models.products import Products
from flask import jsonify
class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")