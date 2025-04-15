from utils.db import db

class Jugador(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100))
    puntuacion = db.Column(db.String(100))


    def __init__(self, nombre, email, puntuacion):
        self.nombre = nombre
        self.email = email
        self.puntuacion = puntuacion