import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash,jsonify

#create app
app = Flask(__name__)
app.config.from_object(__name__)

from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(10))
    email = db.Column(db.String(120), unique=True)
    

    def __init__(self, username,password,email):
        self.username = username
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % self.username

def init_db():
    db.create_all()

def clear_data():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print 'Clear table %s' % table
        db.session.execute(table.delete())
    db.session.commit()


@app.route('/filename/', methods=['GET'])
def filename():
    #name = request.args.get('name')
    current_dir =os.path.realpath(__file__)
    path = os.path.dirname(current_dir)
    tree = dict(name=path, children=[])
    try: 
        lst = os.listdir(path)
    except OSError:
        pass 
    else:
        tree['children'] = lst
       
    return jsonify(tree)

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.args.get('username')
    pwd = request.args.get('password')
    registered_user = User.query.filter(username=username,password=pwd).first()
    result = {}
    if registered_user is None:
        msg = 'Username or Password is invalid'
    else:
        msg = 'User authenticate successfully'    
        
    return jsonify({"result":msg})

@app.route('/users', methods=['GET'])
def get_users():
    if request.args.get('city')
        users = User.query.filter(city=request.args.get('city'))
    else:
        users = User.query.all()

    return jsonify(users)

@app.route('/status', methods=['GET'])
def get_status(): 
    return jsonify({})
    
@app.route('/insert',methods=['POST'])     
def insert_entries():
    username = request.args.get('username')
    pwd = request.args.get('password')
    email = request.args.get('email')
    me = User(username, pwd,email)
    db.session.add(me)
    try:
        db.session.commit()
    except Exception,e:
        print e    
        



if __name__== '__main__':
    app.run()
