from flask import jsonify, request
from flask_restful import Resource, reqparse
from app.models.expedicoes import Expedicoes
from datetime import date

argumentos = reqparse.RequestParser()
argumentos.add_argument('nome', type = str)
argumentos.add_argument('data', type=str)
argumentos.add_argument('destino', type = str)
argumentos.add_argument('estado', type = str)
argumentos.add_argument('tripulacao', type = str)
argumentos.add_argument('carga', type = str)
argumentos.add_argument('duracao', type = str)
argumentos.add_argument('custo', type = float)
argumentos.add_argument('status', type = str)

argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type = int)
argumentos_update.add_argument('nome', type = str)
argumentos_update.add_argument('data', type=str)
argumentos_update.add_argument('destino', type = str)
argumentos_update.add_argument('estado', type = str)
argumentos_update.add_argument('tripulacao', type = str)
argumentos_update.add_argument('carga', type = str)
argumentos_update.add_argument('duracao', type = str)
argumentos_update.add_argument('custo', type = float)
argumentos_update.add_argument('status', type = str)

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type = int)

args = reqparse.RequestParser()
args.add_argument('id', type = int)

argumentos_buscar = reqparse.RequestParser()
argumentos_buscar.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify("Bem vindo à aplicação Flask")

class ExpedicaoCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Expedicoes.save_expedicoes(self, datas['nome'], datas['data'], datas['destino'], datas['estado'], datas['tripulacao'], datas['carga'], datas['duracao'], datas['custo'], datas['status'])
            return {"message": 'Expedição criada com sucesso!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class ExpedicaoUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Expedicoes.update_expedicoes(self, datas['id'], datas['nome'], datas['data'], datas['destino'], datas['estado'], datas['tripulacao'], datas['carga'], datas['duracao'], datas['custo'], datas['status'])
            return {"message": 'Expedição atualizada com sucesso!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500
        

class ExpedicaoDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            expedicao_id = datas['id']
            expedicao = Expedicoes.query.get(expedicao_id)
            if expedicao:
                Expedicoes.delete_expedicoes(self, expedicao_id)
                return {"message": 'Expedição deletada com sucesso!'}, 200
            else:
                return {"message": 'O ID fornecido não existe.'}, 404

        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500


class ExpedicaoList(Resource):
    def get(self):
        try:
            datas = argumentos_buscar.parse_args()
            expedicao_id = datas.get('id')
            print(f'ID inserido : {expedicao_id}')
            
            # Se um ID foi fornecido, retornar os detalhes da expedição correspondente
            if expedicao_id is not None:
                expedicao = Expedicoes.query.get(expedicao_id)
                print(f'Expedição encontrada: {expedicao}')
                if expedicao:
                    expedicao_list = {'id': expedicao.id,'nome': expedicao.nome, 'data': expedicao.data.isoformat(),'destino': expedicao.destino,'estado': expedicao.estado, 'tripulacao': expedicao.tripulacao,'carga': expedicao.carga,'duracao': expedicao.duracao.isoformat(),'custo': expedicao.custo, 'status': expedicao.status}
                    return expedicao_list
                else:
                    return {'status': 404, 'msg': 'Expedição não encontrada'}, 404
            
            # Se nenhum ID foi fornecido, retornar a lista completa de expedições
            else:
                expedicoes = Expedicoes.query.order_by(Expedicoes.data.desc()).all()
                expedicoes_list = [{'id': expedicao.id,'nome': expedicao.nome, 'data': expedicao.data.isoformat(),'destino': expedicao.destino,'estado': expedicao.estado, 'tripulacao': expedicao.tripulacao,'carga': expedicao.carga,'duracao': expedicao.duracao.isoformat(),'custo': expedicao.custo, 'status': expedicao.status} for expedicao in expedicoes]
                return expedicoes_list

        except Exception as e:
            return {'status': 500, 'msg': f'Erro ao processar a requisição: {e}'}, 500

