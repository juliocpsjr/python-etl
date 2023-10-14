from app import db, lm
from flask_login import UserMixin
import json
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String,unique=True)
    email = db.Column(db.String, unique=True)
    cargo = db.Column(db.String)
    area = db.Column(db.String)
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    @lm.user_loader
    def get_id(self):
        return str(self.id)


    def __init__(self, username, password, name, email,cargo,area):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.cargo = cargo
        self.area = area
    
    def __repr__(self):
        return f'{self.username},{self.cargo}' 
    # basta criar uma representação em formato de dicionário para pegar todas as informações que precisar


class Skap(db.Model):
    __tablename__ = "skap"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True)
    number_id = db.Column(db.Integer,unique=True) 
    area = db.Column(db.String)
    turno = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    
    resultado = db.Column(db.Integer)

    def __init__(self, username, number_id, area, turno,q1,q2,q3,q4,resultado):
        self.username = username
        self.number_id = number_id
        self.area = area
        self.turno = turno
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.resultado = resultado
        
    def __str__(self):
        return f'{self.username},{self.number_id},{self.area},{self.turno},{self.q1},{self.q2},{self.q3},{self.q4},{self.resultado}'


