from app.data.modelo.videojuego import Videojuego

class VideojuegoDao:

    def select_all(self,db) -> list[Videojuego]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM videojuegos')
        videojuegos_en_db = cursor.fetchall()
        videojuegos : list[Videojuego]= list()
        for videojuego_en_db in videojuegos_en_db:
            videojuegos.append(Videojuego(videojuego_en_db[0], videojuego_en_db[1], videojuego_en_db[2], videojuego_en_db[3], videojuego_en_db[4], videojuego_en_db[5]))
        
        cursor.close()
        return videojuegos
    def select_uno(self,db,nombre) -> Videojuego:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM videojuegos WHERE nombre =%s',[nombre])
        videojuegos_en_db = cursor.fetchall()
        if (videojuegos_en_db == []):
            return None
        videojuego_en_db = videojuegos_en_db[0]
        videojuego  = Videojuego(videojuego_en_db[0], videojuego_en_db[1], videojuego_en_db[2],videojuego_en_db[3], videojuego_en_db[4], videojuego_en_db[5])
        cursor.close()
        return equipo
    
    def insert(self,db,nombre,año_lanzamiento,plataforma,genero,desarrolladores):
        cursor = db.cursor()
        sql = ("INSERT INTO videojuegos (nombre,año_lanzamiento,plataforma,genero,desarrolladores) VALUES (%s,%s)")
        data = (nombre,año_lanzamiento,plataforma,genero,desarrolladores)
        cursor.execute(sql,data)
        db.commit()
    
    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("DELETE FROM videojuegos WHERE id = %s")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
    
    def update(self,db,id,nombre,año_lanzamiento,plataforma,genero,desarrolladores):
        cursor = db.cursor()
        sql = ("UPDATE videojuegos SET nombre = %s, año_lanzamiento = %s, plataforma = %s, genero = %s, desarrolladores = %s WHERE id = %s")
        data = [nombre,año_lanzamiento,plataforma,genero,desarrolladores,id]
        cursor.execute(sql, data)
        db.commit()
    
    def updateNombre(self,db,id,nombre):
        cursor = db.cursor()
        sql = ("UPDATE videojuegos SET nombre = %s WHERE id = %s")
        data = [nombre,id]
        cursor.execute(sql, data)
        db.commit()
