from app import db
from datetime import datetime

class Missions(db.Model):
    __tablename__ = 'missions'
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date = db.Column(db.Date)
    destination = db.Column(db.String)
    state = db.Column(db.String)
    tripulation = db.Column(db.String)
    charge = db.Column(db.String)
    duration = db.Column(db.Interval)
    cost = db.Column(db.Integer)
    status = db.Column(db.String)
    
    def __init__(self,name,date,destination,state,tripulation,charge,duration,cost,status):
        self.name = name
        self.date = date
        self.destination = destination
        self.state = state
        self.tripulation = tripulation
        self.charge = charge
        self.duration = duration
        self.cost = cost
        self.status = status
             
        
    def save_missions(self,name,date,destination,state,tripulation,charge,duration,cost,status):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            add_banco = Missions(name, date_obj, destination, state, tripulation, charge, duration, cost, status)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as e:
            print(e)
    
    def update_missions(self,id,name,date,destination,state,tripulation,charge,duration,cost,status):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            db.session.query(Missions).filter(Missions.id==id).update({"name":name,"date": date_obj, "destination": destination, "state": state, "tripulation": tripulation, "charge":charge, "duration": duration, "cost": cost, "status": status})
            db.session.commit()
        except Exception as e:
            print(e)

    def delete_missions(self, id):
        try:
            db.session.query(Missions).filter(Missions.id==id).delete()
            db.session.commit()
        except Exception as e:
            print(e)
        