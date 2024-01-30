from app.data.modelo.lenguaje import Lenguaje
from app.data.modelo.videojuego import Videojuego
class LenguajesDao:

    def select_all(self,db, id_videojuego) -> list[Lenguaje]:
        cursor = db.cursor()
        cursor.execute (""" SELECT l.*,v.nombre FROM lenguajes j inner join videojuegos v on l.id_videojuego = v.id WHERE l.id_videojuego = %s """,[id_videojuego])
        lenguajes_en_db = cursor.fetchall()
        lenguajes : list[Lenguaje]= list()
        for lenguajes_en_db in lenguajes_en_db:
            lenguajes.append(Lenguaje(lenguaje_en_db[0], lenguaje_en_db[1], lenguaje_en_db[2]))
        
        cursor.close()
        return lenguajes

    def select_uno(self,db,nombre) -> Videojuego:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM videojuegos WHERE nombre = %s', [nombre])
        videojuegos_en_db = cursor.fetchall()
        if (videojuegos_en_db == []):
            return None
        videojuegos_en_db = videojuegos_en_db[0]
        videojuego = Videojuego(videojuego_en_db[0], videojuego_en_db[1], videojuego_en_db[2], videojuego_en_db[3], videojuego_en_db[4], videojuego_en_db[5])
        cursor.close()
        return videojuego

    def insert (self,db,nombre,año_lanzamiento,plataforma,genero,desarrolladores):
        cursor = db.cursor()
        sql = ("INSERT INTO videojuegos (nombre,año_lanzamiento,plataforma,genero,desarrolladores) values (%s,%s)")
        data = (nombre,año_lanzamiento,plataforma,genero,desarrolladores)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("DELETE FROM videojuegos WHERE id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
    
    def update(self,db,id,nombre,año_lanzamiento,plataforma,genero,desarrolladores):
        cursor = db.cursor()
        sql = ("UPDATE videojuegos SET nombre = %s, año_lanzamiento = %s, plataforma = %s, genero = %s, desarrolladores = %s, where id = %s")
        data = [nombre,año_lanzamiento,plataforma,genero,desarrolladores,id]
        cursor.execute(sql,data)
        db.commit()

    def updateNombre(self,db,id,nombre):
        cursor = db.cursor()
        sql = ("UPDATE videojuegos SET nombre = %s WHERE id = %s")
        data = [nombre,id]
        cursor.execute(sql,data)
        db.commit()