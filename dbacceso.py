import sqlite3
import json

BASE_RUTA = "juga_base.db"
TESTEO_RUTA = "juga_base_test.db"


BASE_TRABAJO = BASE_RUTA


def activar_testeo(test=True):
    if test:
        BASE_TRABAJO = TESTEO_RUTA
    else:
        BASE_TRABAJO = BASE_RUTA


def query_db(query, args=(), one=False):
    con = sqlite3.connect(BASE_TRABAJO)
    cur = con.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    con.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query, args=()):
    con = sqlite3.connect(BASE_TRABAJO)
    cur = con.execute(query, args)
    con.commit()
    con.close()



class JugadorDAO:
    _instancia = None
    
    def instancia():
        if not JugadorDAO._instancia:
            JugadorDAO._instancia = JugadorDAO()
        
        return JugadorDAO._instancia
    
    def query_todo(self):
        return query_db('select * from jugador order by codigo')
    
    def query_ultimo_codigo(self):
        return query_db('select max(codigo) as codigo from jugador', one=True)
    
    def query_codigo(self, iden):
        # Devuelve un unico campo (si existe)
        return query_db('select * from jugador where codigo=?', (iden,), True)
    
    def _query_todo(self, args):
        #print(args)
        #orde = args.pop()
        return query_db( 'select * from jugador order by '+args.pop(), args )
    
    def query_nombre(self, args):
        return query_db('select * from jugador where nombre LIKE ? order by '+args.pop(), args)
        
    def query_club(self, args):
        return query_db('select * from jugador where club=? order by '+args.pop(), args)
        
    def query_posicion(self, args):
        return query_db('select * from jugador where posicion=? order by '+args.pop(), args)
        
    def query_nombre_club(self, args):
        return query_db('select * from jugador where nombre=? and club=? order by '+args.pop(), args)
        
    def query_nombre_posicion(self, args):
        return query_db('select * from jugador where nombre=? and posicion=? order by '+args.pop(), args)
        
    def query_club_posicion(self, args):
        return query_db('select * from jugador where club=? and posicion=? order by '+args.pop(), args)
        
    def query_nombre_club_posicion(self, args):
        return query_db('''select * from jugador where nombre=? and club=? and posicion=?
        order by '''+args.pop(), args)
    
    def __init__(self):
        self.funcs = [ self._query_todo, self.query_nombre, self.query_club, self.query_nombre_club, self.query_posicion,
         self.query_nombre_posicion, self.query_club_posicion, self.query_nombre_club_posicion ]

    def insertar(self, codigo, nombre, club, posicion, costo):
        insert_db("insert into jugador values (?,?,?,?,?)", (codigo,nombre,club,posicion,costo) )

    def eliminar(self, codigo):
        insert_db( 'delete from jugador where codigo = ?', (codigo,) )
        
    def actualizar(self, codigo, nombre, club, posicion, costo):
        insert_db( 'update jugador set nombre=?, club=?, posicion=?, costo=? where codigo=?', (self.nombre, self.club, self.posicion, self.costo, self.codigo) )
        
        

    # Probando
    def query(self, nombre=None, club=None, posicion=None, ordenar=None, listado=None ):
        codigo = 0
        args = []
        
        if nombre:
            codigo += 1
            args.append(nombre+'%') # Wildcard agregada aca
        if club:
            codigo += 2
            args.append(club)
        if posicion:
            codigo += 4
            args.append(posicion)
           
        if not ordenar:
            ordenar = 'codigo'
        if not listado:
            listado = 'asc'
            
        #args.append(ordenar)
        args.append(ordenar+" "+listado)

        return self.funcs[codigo]( args )
            
        