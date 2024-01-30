class Videojuego:
    def __init__(self, id:int, nombre:str, año_lanzamiento:int, plataforma:str, genero:str, desarrolladores:str):
        self.id = id
        self.nombre = nombre
        self.año_lanzamiento = año_lanzamiento
        self.plataforma = plataforma
        self.genero = genero
        self.desarrolladores = desarrolladores