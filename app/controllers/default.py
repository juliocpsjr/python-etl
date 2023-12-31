import json
from flask import jsonify, render_template, flash, redirect, request, url_for
from app import app, db, lm
from app.models.tables import User, Skap
from app.models.forms import SkapForm, LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
import numpy as np
import pandas as pd
import sys
sys.setrecursionlimit(4500)
import requests


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

#Route Index
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/select/<user>')
def select(user):
    i = Skap.query.filter_by(username={user}).all()
    result_dict = [u.__dict__ for u in i]
    df = pd.DataFrame(result_dict)
    df = df.drop("_sa_instance_state",axis=1)
    print(df)
    return "Ok"

@app.route('/select_all')
def select_all():
    i = Skap.query.all()
    result_dict = [u.__dict__ for u in i]
    df = pd.DataFrame(result_dict)
    df = df.drop("_sa_instance_state",axis=1)
    print(df)
    return "Ok"

@app.route('/update')
def update():
    i = User.query.filter_by(username="julio").first()
    i.name="Julio R."
    db.session.add(i)
    db.session.commit()
    print(i.name)
    return "Ok"

#Route Delete User
@app.route('/delete/user')
def delete_user():
    i = User.query.filter_by(username="JulioC").first()
    db.session.delete(i)
    db.session.commit()
    return "Ok"

#Route Delete Skap
@app.route('/delete/skap/<user>')
def delete_skap(user):
    i = Skap.query.filter_by(username="%s" % (user)).first()
    db.session.delete(i)
    db.session.commit()
    return "Ok"

#Route Create User
@app.route('/create/user')
def create_users():
    i = User("JulioC","1234","Julio","teste@teste.com.br","Automacao","Eng")
    db.create_all()
    db.session.add(i)
    db.session.commit()
    return "User created"

#Route Create Skap
@app.route('/create/skap')
def create_skap():
    j = Skap("Teste",9991,"Eng","ADM",1,1,1,1,100.0)
    db.create_all()
    db.session.add(j)
    db.session.commit()
    return "SKAP created"


