from flask import Blueprint, render_template, request, redirect, url_for

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/login')
def iniciar_sesion():
    return render_template('login.html',)

@usuarios.route('/register')
def registro():
    return render_template('registro.html',)