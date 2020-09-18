from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#from marshmallow import post_load, Schema, fields
#import regras as regras_negocio

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)
 

from .routes import cartao
app.register_blueprint(cartao)

db.create_all()

