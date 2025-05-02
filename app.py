from flask import Flask
from routes.jugadores import jugadores
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/jugadoresdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(jugadores)
