from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app) 
from app.models.products import Products
with app.app_context():
    db.create_all()
from app.view.reso_products import Index
api.add_resource(Index, '/')
@app.route("/")
def Index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")