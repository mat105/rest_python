import ojeo

#import dbacceso
from dbacceso import JugadorDAO

class Jugador:
    CODIGO = 0

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
        codn = JugadorDAO.instancia().query_ultimo_codigo() #dbacceso.query_db('select max(codigo) as codigo from jugador', one=True)

        if codn != None and codn['codigo'] != None:
            return codn['codigo']

        return -1

    def dame_ojeos(self):
        return ojeo.Ojeo.dame_todos_json_jugador(self.codigo)

    def dame_todos():
        data = JugadorDAO.instancia().query() #dbacceso.query_db( 'select * from jugador' )
        ret = []
        
        for dic in data:
            ret.append( Jugador( dic['codigo'], dic['nombre'], dic['club'], dic['posicion'], dic['costo'] ) )
        
        return ret
        
    def transformar_json(self):
        return { "codigo" : self.codigo, "nombre" : self.nombre, "club" : self.club, "posicion" : self.posicion, "costo" : self.costo }
        
    def dame_todos_json():
        return JugadorDAO.instancia().query()
        #return dbacceso.query_db( 'select * from jugador' )
        
    def query(nombre=None, club=None, posicion=None, ordenado=None, listado=None):
        return JugadorDAO.instancia().query( nombre, club, posicion, ordenado, listado )
            
    def modificar_bd(self):
        JugadorDAO.instancia().actualizar(codigo, nombre, club, posicion, costo)
        #dbacceso.insert_db( 'update jugador set nombre=?, club=?, posicion=?, costo=? where codigo=?', (self.nombre, self.club, self.posicion, self.costo, self.codigo) )
            
    def guardar_bd(self):
        JugadorDAO.instancia().insertar( self.codigo, self.nombre, self.club, self.posicion, self.costo )
        #dbacceso.insert_db( 'insert into jugador values (?, ?, ?, ?, ?)', (self.codigo, self.nombre, self.club, self.posicion, self.costo) )
        
    def cargar_bd(self):
        #data = dbacceso.query_db('select * from jugador where codigo=?', (self.codigo,), one=True)
        data = JugadorDAO.instancia().query_codigo( self.codigo )
        
        return Jugador( data['codigo'], data['nombre'], data['club'], data['posicion'], data['costo'] )
        
    def eliminar_bd(self):
        JugadorDAO.instancia().eliminar( self.codigo )
        #dbacceso.insert_db( 'delete from jugador where codigo = ?', (self.codigo,) )

    def agregar_ojeo(self, ojo):
        ojo.guardar_bd()

    def __init__(self, codigo, nombre="", club="", posicion="", costo=0):
        self.nombre = nombre
        self.club = club
        self.posicion = posicion
        self.costo = costo
        self.codigo = codigo
        
        