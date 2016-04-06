from ojeo import Ojeo

class Jugador:
    CODIGO = 0
    
    personas = {
    }

    def crear_ejemplos():
        j1 = Jugador(0,"Cebolla", "Independiente", "Volante", 10000000)
        j1.guardar_bd()
        j1 = Jugador(1,"Messi", "Barcelona", "Delantero", 80000000)
        j1.guardar_bd()
        j1 = Jugador(2,"Robben", "Bayern Munich", "Delantero", 30312424)
        j1.guardar_bd()

    def dame_todos():
        return Jugador.personas
        
    def juga_json(self):
        return { 'Nombre' : self.nombre, 'Club' : self.club, 'Posicion' : self.posicion, 'Costo' : self.costo }
        
    def dame_todos_json():
        js = {}
        for k, v in Jugador.personas.items():
            js[str(k)] = v.juga_json()
        return js
            
    def guardar_bd(self):
        Jugador.personas[self.codigo] = self
        
    def cargar_bd(self):
        return Jugador.personas.get(self.codigo, None)

    def agregar_ojeo(self, ojo):
        self.ojeos.append(ojo)

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.ojeos = []
        self.codigo = codigo
        