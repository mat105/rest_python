
ojeos = {
}

class Ojeo:
    CODIGO = 0

    def dame_todos():
        return ojeos

    def guardar_bd(self):
        ojeos[self.codigo] = self
        
    def cargar_bd(self):
        return ojeos.get(self.codigo, None)

    def __init__(self, codigo, jugador, fecha, comentarios):
        self.comentarios = comentarios
        self.fecha = fecha
        self.codigo = Ojeo.CODIGO
        self.jugador = jugador