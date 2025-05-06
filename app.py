from flask import Flask
from routes.jugadores import jugadores
from routes.usuarios import usuarios
from utils.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jugadores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(jugadores)

app.register_blueprint(usuarios)
