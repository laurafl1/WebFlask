import random
from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.lenguajes_dao import LenguajesDao
from app.data.videojuego_dao import VideojuegoDao
from app.data.modelo.videojuego import Videojuego



rutas_lenguajes = Blueprint("routes_lenguajes", __name__)


@rutas_lenguajes.route('/verLenguajes', methods=['POST', 'GET'])
def verLenguajes():
    lenguajes = list()
    nombreVideojuego = ""
    videojuego_dao = VideojuegoDao()
    videojuegos = videojuego_dao.select_all(db)

    if (request.method == 'POST'):
        id_videojuego = request.form['id_videojuego']
        lenguajes_dao = LenguajesDao()
        lenguajes = lenguajes_dao.select_all(db,id_videojuego)
        for videojuego in videojuegos:
            if (videojuego.id == str(videojuego.id)):
                nombreVideojuego = videojuego.nombre

    print(nombreVideojuego)

    return render_template('lenguajes.html', lenguajes=lenguajes,videojuegos=videojuegos,nombreVideojuego=nombreVideojuego)

@rutas_lenguajes.route('/delLenguaje', methods=['POST'])
def delVideojuego():
    id = request.form['id']
    videojuego_dao = VideojuegoDao()
    videojuego_dao.delete(db,id)

    return redirect(url_for('routes.VerVideojuegos'))