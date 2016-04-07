
class Ojeo:
    CODIGO = 0
    
    ojeos = {
    }
    
    
    def ultimo_codigo():
        if(Ojeo.ojeos):
            return max(Ojeo.ojeos.keys())
        return 0

    def dame_todos():
        return Ojeo.ojeos
        
    def eliminar_ojeos_jugador(jid):
        for k, v in Ojeo.ojeos:
            if v.jugador.codigo == jid:
                #del Ojeo.ojeos[k]
                self.eliminar_bd()

        
    def dame_todos_json_jugador(jid):
        ret = {}
        for k, v in Ojeo.ojeos.items():
            if v.jugador.codigo == jid:
                ret[str(k)] = v.transformar_json()
        return ret
            
        
    def transformar_json(self):
        return { 'Jugador' : self.jugador.transformar_json(), 'Fecha' : self.fecha, 'Comentarios' : self.comentarios }
        
    def dame_todos_json():
        js={}
        for k, v in Ojeo.ojeos.items():
            js[str(k)] = v.transformar_json()
        return js

    def guardar_bd(self):
        Ojeo.ojeos[self.codigo] = self
        
    def cargar_bd(self):
        return Ojeo.ojeos.get(self.codigo, None)
        
    def eliminar_bd(self):
        del Ojeo.ojeos[self.codigo]

    def __init__(self, codigo, jugador=None, fecha="", comentarios=""):
        self.comentarios = comentarios
        self.fecha = fecha
        self.codigo = Ojeo.CODIGO
        self.jugador = jugador