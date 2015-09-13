import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash,jsonify

#create app
app = Flask(__name__)
app.config.from_object(__name__)

#load default conf and override config from an env var
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY = 'dev key',
    USERNAME = 'admin',
    PASSWORD = 'admin'
))


# def connect_db():
#     """connect to the specific db"""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv



# def get_db():
#     """opens a new db connection if there is none yet for the cyrrent app"""
#     if not hasattr(g, 'sqlite_db'):
#         g.sqlite_db = connect_db()
#         return g.sqlite_db

# @app.teardown_appcontext
# def close_db(error):
#     """closes the db again at the end of the request."""
# if hasattr(g, 'sqlite_db'):
#     g.sqlite_db.close()

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


# @app.route('/')
# def show_entries():
#     db=get_db()
#     cur = db.execute('select title, text from entries order by id desc')
#     entries = cur.fetchall()
#     print entries
#     return render_template('show_entries.html', entries=entries)

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
    result = {}
    if username != app.config['USERNAME']:
        msg = 'Invalid username'
    elif pwd != app.config['PASSWORD']:
        msg = 'Invalid password'
    else:
        msg = "Succesfully logged in"
        
    return jsonify({"result":msg})
     



if __name__== '__main__':
    app.run()
