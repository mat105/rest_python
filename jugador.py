from ojeo import Ojeo

import dbacceso

class Jugador:
    CODIGO = 0
    
    personas = {
    }

    def crear_ejemplos():
        #dbacceso.insert_db('delete from jugador')
        j1 = Jugador(0,"Cebolla", "Independiente", "Volante", 10000000)
        #j1.agregar_ojeo( Ojeo(0, j1, "2016/01/01", "Buen jugador") )
        j1.guardar_bd()
        j1 = Jugador(1,"Messi", "Barcelona", "Delantero", 80000000)
        j1.guardar_bd()
        j1 = Jugador(2,"Robben", "Bayern Munich", "Delantero", 30312424)
        j1.guardar_bd()

    def ultimo_codigo():
        #if Jugador.personas:
            #return max( Jugador.personas.keys() )
        codn = dbacceso.query_db('select max(codigo) as codigo from jugador', one=True)

        return codn['codigo'] if codn else 0

    def dame_ojeos(self):
        return Ojeo.dame_todos_json_jugador(self.codigo)

    def dame_todos():
        return dbacceso.query_db( 'select * from jugador' )
        #return Jugador.personas
        
    def transformar_json(self):
        return { 'Nombre' : self.nombre, 'Club' : self.club, 'Posicion' : self.posicion, 'Costo' : self.costo }
        
    def dame_todos_json():
        #js = {}
        #for k, v in Jugador.personas.items():
            #js[str(k)] = v.transformar_json()
        #return js
        return dbacceso.query_db( 'select * from jugador' )
            
    def guardar_bd(self):
        dbacceso.insert_db( 'insert into jugador values (?, ?, ?, ?, ?)', (self.codigo, self.nombre, self.club, self.posicion, self.costo) )
        
        #Jugador.personas[self.codigo] = self
        
    def cargar_bd(self):
        data = dbacceso.query_db('select * from jugador where codigo=?', (self.codigo,), one=True)
        
        return Jugador( data['codigo'], data['nombre'], data['club'], data['posicion'], data['costo'] )
        #return Jugador.personas.get(self.codigo, None)
        
    def eliminar_bd(self):
        dbacceso.insert_db( 'delete from jugador where codigo = ?', (self.codigo,) )
        #Ojeo.eliminar_ojeos_jugador(self.codigo)
        #del Jugador.personas[self.codigo]

    def agregar_ojeo(self, ojo):
        #self.ojeos.append(ojo)
        ojo.guardar_bd()

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.codigo = codigo
        