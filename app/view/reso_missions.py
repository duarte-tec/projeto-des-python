from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missions import Missions
from datetime import date

argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('date', type=str)
argumentos.add_argument('destination', type=str)
argumentos.add_argument('state', type=str)
argumentos.add_argument('tripulation', type=str)
argumentos.add_argument('charge', type=str)
argumentos.add_argument('duration', type=str)
argumentos.add_argument('cost', type=float)
argumentos.add_argument('status', type=str)


argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos_update.add_argument('date', type=str)
argumentos_update.add_argument('destination', type=str)
argumentos_update.add_argument('state', type=str)
argumentos_update.add_argument('tripulation', type=str)
argumentos_update.add_argument('charge', type=str)
argumentos_update.add_argument('duration', type=str)
argumentos_update.add_argument('cost', type=float)
argumentos_update.add_argument('status', type=str)

argumento_deletar = reqparse.RequestParser()
argumento_deletar.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class MissionsCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Missions.save_missions(self, datas['name'], datas['date'], datas['destination'], datas['state'], datas['tripulation'], datas['charge'], datas['duration'], datas['cost'], datas['status'])
            return {"message": 'Mission created successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

      
class MissionsUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Missions.update_missions(self, datas['id'], datas['name'], datas['date'], datas['destination'], datas['state'], datas['tripulation'], datas['charge'], datas['duration'], datas['cost'], datas['status'])
            return {"message": 'Mission updated successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        
class MissionsDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_update.parse_args()
            Missions.delete_missions(self, datas['id'])
            return {"message": 'Mission deleted successfully!'}, 200  
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
