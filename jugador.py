import ojeo

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
        codn = dbacceso.query_db('select max(codigo) as codigo from jugador', one=True)

        return codn['codigo'] if codn['codigo'] else 0

    def dame_ojeos(self):
        return ojeo.Ojeo.dame_todos_json_jugador(self.codigo)

    def dame_todos():
        data = dbacceso.query_db( 'select * from jugador' )
        ret = []
        
        for dic in data:
            ret.append( Jugador( dic['codigo'], dic['nombre'], dic['club'], dic['posicion'], dic['costo'] ) )
        
        return ret
        
    def transformar_json(self):
        return { "codigo" : self.codigo, "nombre" : self.nombre, "club" : self.club, "posicion" : self.posicion, "costo" : self.costo }
        
    def dame_todos_json():
        return dbacceso.query_db( 'select * from jugador' )
            
    def modificar_bd(self):
        dbacceso.insert_db( 'update jugador set nombre=?, club=?, posicion=?, costo=? where codigo=?', (self.nombre, self.club, self.posicion, self.costo, self.codigo) )
            
    def guardar_bd(self):
        dbacceso.insert_db( 'insert into jugador values (?, ?, ?, ?, ?)', (self.codigo, self.nombre, self.club, self.posicion, self.costo) )
        
    def cargar_bd(self):
        data = dbacceso.query_db('select * from jugador where codigo=?', (self.codigo,), one=True)
        
        return Jugador( data['codigo'], data['nombre'], data['club'], data['posicion'], data['costo'] )
        
    def eliminar_bd(self):
        dbacceso.insert_db( 'delete from jugador where codigo = ?', (self.codigo,) )

    def agregar_ojeo(self, ojo):
        ojo.guardar_bd()

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.codigo = codigo
        
        