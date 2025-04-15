from flask import Blueprint, render_template, request, redirect, url_for
from models.jugador import Jugador
from utils.db import db

jugadores = Blueprint('jugadores', __name__)

@jugadores.route('/')
def dasboard():
    jugadores = Jugador.query.all()
    return render_template('index.html', jugadores=jugadores)

@jugadores.route('/new', methods=['POST'])
def añadir_jugador():
    nombre=request.form['nombre']
    email=request.form['email']
    puntuacion=request.form['puntuacion']

    nuevo_jugador = Jugador(nombre, email, puntuacion)

    db.session.add(nuevo_jugador)
    db.session.commit()

    return redirect(url_for('jugadores.dasboard'))

@jugadores.route('/update/<id>', methods = ['POST', 'GET'])
def actualizar(id):
    jugador = Jugador.query.get(id)
    if request.method == 'POST':
        jugador.nombre = request.form["nombre"]
        jugador.email = request.form["email"]
        jugador.puntuacion = request.form["puntuacion"]

        db.session.commit()
        return redirect(url_for("jugadores.dasboard"))
    return render_template('actualizar.html', jugador = jugador)

@jugadores.route('/delete/<id>')
def borrar(id):
    jugador = Jugador.query.get(id)

    db.session.delete(jugador)
    db.session.commit()

    return redirect(url_for('jugadores.dasboard'))