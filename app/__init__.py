from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crud.db"
db = SQLAlchemy(app)

from app.models.missions import Missions
with app.app_context():
    db.create_all()
    
from app.view.reso_missions import Index, MissionsCreate, MissionsUpdate, MissionsDelete
api.add_resource(Index, '/')
api.add_resource(MissionsCreate, '/criar')
api.add_resource(MissionsUpdate, '/atualizar')
api.add_resource(MissionsDelete, '/deletar')