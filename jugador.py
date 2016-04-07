from ojeo import Ojeo

class Jugador:
    CODIGO = 0
    
    personas = {
    }

    def crear_ejemplos():
        j1 = Jugador(0,"Cebolla", "Independiente", "Volante", 10000000)
        #j1.agregar_ojeo( Ojeo(0, j1, "2016/01/01", "Buen jugador") )
        j1.guardar_bd()
        j1 = Jugador(1,"Messi", "Barcelona", "Delantero", 80000000)
        j1.guardar_bd()
        j1 = Jugador(2,"Robben", "Bayern Munich", "Delantero", 30312424)
        j1.guardar_bd()

    def ultimo_codigo():
        if Jugador.personas:
            return max( Jugador.personas.keys() )
        return 0

    def dame_ojeos(self):
        return Ojeo.dame_todos_json_jugador(self.codigo)

    def dame_todos():
        return Jugador.personas
        
    def transformar_json(self):
        return { 'Nombre' : self.nombre, 'Club' : self.club, 'Posicion' : self.posicion, 'Costo' : self.costo }
        
    def dame_todos_json():
        js = {}
        for k, v in Jugador.personas.items():
            js[str(k)] = v.transformar_json()
        return js
            
    def guardar_bd(self):
        Jugador.personas[self.codigo] = self
        
    def cargar_bd(self):
        return Jugador.personas.get(self.codigo, None)

    def agregar_ojeo(self, ojo):
        #self.ojeos.append(ojo)
        ojo.guardar_bd()

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.codigo = codigo
        