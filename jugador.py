
personas = {
    0:Jugador("Cebolla", "Independiente", "Volante", 10000000),
    1:Jugador("Messi", "Barcelona", "Delantero", 80000000),
    2:Jugador("Robben", "Bayern Munich", "Delantero", 30312424)
    }


class Jugador:
    CODIGO = 0

    def __str__(self):
        return "Nombre: {}      Club: {}        Posicion: {}        Costo: {}".format( self.nombre, self.club, self.posicion, self.costo )
        
    def __repr__(self):
        return "Nombre: {}      Club: {}".format(self.nombre, self.club)

    def dame_todos():
        return personas

    def guardar_bd(self):
        personas[self.codigo] = self
        
    def cargar_bd(self):
        return personas.get(self.codigo, None)

    def agregar_ojeo(self, ojo):
        self.ojeos.append(ojo)

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.ojeos = []
        self.codigo = codigo