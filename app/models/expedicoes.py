from app import db
from datetime import datetime

class Expedicoes(db.Model):
    __tablename__ = 'Expedicoes'
    __table_args__ = {'sqlite_autoincrement': True}
   
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = False)
    data = db.Column(db.Date, nullable = False)
    destino = db.Column(db.String, nullable = False)
    estado = db.Column(db.String, nullable = False)
    tripulacao = db.Column(db.String, nullable = False)
    carga = db.Column(db.String, nullable = False)
    duracao = db.Column(db.Date, nullable = False)
    custo = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String, nullable = False)
   
    def list_id(self, expedicao_id):
            try:
                expedicoes = db.session.query(Expedicoes).filter(Expedicoes.id == expedicao_id).all()
                expedicoes_dict = [{'id': expedicao.id, 'nome': expedicao.nome, 'data': expedicao.data.isoformat(), 'destino': expedicao.destino, 'estado': expedicao.estado,'tripulacao': expedicao.tripulacao, 'carga': expedicao.carga, 'duracao': expedicao.duracao.isoformat(), 'custo': expedicao.custo, 'status': expedicao.status} for expedicao in expedicoes]
                return expedicoes_dict
            except Exception as e:
                print(e)

    def __init__(self, nome, data, destino, estado, tripulacao, carga, duracao, custo, status):
        self.nome = nome
        self.data = data
        self.destino = destino
        self.estado = estado
        self.tripulacao = tripulacao
        self.carga = carga
        self.duracao = duracao
        self.custo = custo
        self.status = status

    def save_expedicoes(self, nome, data, destino, estado, tripulacao, carga, duracao, custo, status):
        try:
            date_obj = datetime.strptime(data, "%Y-%m-%d").date()
            date_duracao = datetime.strptime(duracao, "%Y-%m-%d").date()
            add_banco = Expedicoes(nome, date_obj, destino, estado, tripulacao, carga, date_duracao, custo, status)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:  
            print(e)
   
    def update_expedicoes(self, id, nome, data, destino, estado, tripulacao, carga, duracao, custo, status):
        try:
            date_obj = datetime.strptime(data, "%Y-%m-%d").date()
            date_duracao = datetime.strptime(duracao, "%Y-%m-%d").date()
            db.session.query(Expedicoes).filter(Expedicoes.id==id).update({"nome":nome, "data": date_obj, "destino": destino, "estado": estado, "tripulacao": tripulacao, "carga":carga, "duracao": date_duracao, "custo": custo, "status": status})
            db.session.commit()
        except Exception as e:
            print(e)

    def delete_expedicoes(self, id):
        try:
            db.session.query(Expedicoes).filter(Expedicoes.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)

    @classmethod
    def list_expedicoes(cls):
            try:
                expedicoes = db.session.query(cls).order_by(cls.data.desc()).all()
                expedicoes_list = [{'id': expedicao.id,'nome': expedicao.nome, 'data': expedicao.data.isoformat(),'destino': expedicao.destino,'estado': expedicao.estado, 'tripulacao': expedicao.tripulacao,'carga': expedicao.carga,'duracao': expedicao.duracao.isoformat(),'custo': expedicao.custo, 'status': expedicao.status} for expedicao in expedicoes]
                return expedicoes_list
            except Exception as e:
                print(e)
                return []