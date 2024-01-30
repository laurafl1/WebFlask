import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app import db
from app.data.videojuego_dao import VideojuegoDao

rutas_juegos = Blueprint("routes", __name__)

@rutas_juegos.route("/")
def index():
    return render_template('index.html')

@rutas_juegos.route("/Formulario")
def formulario():
    return render_template('formulario.html')

@rutas_juegos.route('/personajes')
def personajes():
    nombre1=random.randint(1,100)
    nombre2=random.randint(1,100)

    return render_template('personajes.html')

@rutas_juegos.route('/verVideojuegos')
def verVideojuegos():
    videojuego_dao = VideojuegoDao()

    videojuegos = videojuego_dao.select_all(db)

    return render_template('videojuegos.html',aleatorio=videojuegos)

@rutas_juegos.route('/addVideojuego', methods=['POST'])
def addVideojuego():
    videojuego_dao = VideojuegoDao()

    nombre = request.form['nombre']
    año_lanzamiento = request.form['año_lanzamiento']
    plataforma = request.form['plataforma']
    genero = request.form['genero']
    desarrolladores = request.form['desarrolladores']

    if (nombre == "" or año_lanzamiento == "" or plataforma == "" or genero == "" or desarrolladores == "" ):
        return redirect(url_for('routes.verVideojuegos'))
    videojuego_dao.insert(db,nombre,año_lanzamiento,plataforma,genero,desarrolladores)

    return redirect(url_for('routes.verVideojuegos'))

@rutas_juegos.route('/delVideojuego', methods=['POST'])
def delVideojuego():
    videojuego_dao = VideojuegoDao()

    id = request.form['id']
    videojuego_dao.delete(db,id)

    return redirect(url_for('routes.verVideojuegos'))

@rutas_juegos.route('/updateVideojuego', methods=['POST'])
def updateVideojuego():
    videojuego_dao = VideojuegoDao()

    id = request.form['id']
    nombre = request.form['nombre']
    año_lanzamiento = request.form['año_lanzamiento']
    plataforma = request.form['plataforma']
    genero = request.form['genero']
    desarrolladores = request.form['desarrolladores']

    if (año_lanzamiento == ""):
        videojuego_dao.updateVideojuego(db,id,nombre)
    else:
        videojuego_dao.update(db,id,nombre,año_lanzamiento,plataforma,genero,desarrolladores)
    
    return redirect(url_for('routes.verVideojuegos'))