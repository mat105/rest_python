
class Ojeo:
    CODIGO = 0
    
    ojeos = {
    }
    

    def dame_todos():
        return Ojeo.ojeos
        
    def ojeo_json(self):
        return { 'Jugador' : self.juga_json(), 'Fecha' : self.fecha, 'Comentarios' : self.comentarios }
        
    def dame_todos_json():
        js={}
        for k, v in Ojeo.ojeos.items():
            js[k] = v.ojeo_json()
        return js

    def guardar_bd(self):
        Ojeo.ojeos[self.codigo] = self
        
    def cargar_bd(self):
        return Ojeo.ojeos.get(self.codigo, None)

    def __init__(self, codigo, jugador=None, fecha="", comentarios=""):
        self.comentarios = [comentarios]
        self.fecha = fecha
        self.codigo = Ojeo.CODIGO
        self.jugador = jugador