import dbacceso

import jugador

class Ojeo:
    CODIGO = 0
    
    
    def ultimo_codigo():
        codn = dbacceso.query_db('select max(codigo) as codigo from ojeo', one=True)
        
        if codn != None and codn['codigo'] != None:
            return codn['codigo']

        return -1

    def dame_todos():
        data = dbacceso.query_db('select * from ojeo') #Ojeo.ojeos
        ret = []
        
        for dic in data:
            ret.append( Ojeo(dic['codigo'], jugador.Jugador(dic['codigo_jugador']), dic['fecha'], dic['comentarios'] ) )
        
        return ret
        
    def eliminar_ojeos_jugador(jid):
        for k, v in Ojeo.ojeos:
            if v.jugador.codigo == jid:
                self.eliminar_bd()

        
    def dame_todos_json_jugador(jid):
        # Query_db devuelve un diccionario, ya que flask-restful puede convertirlo automaticamente a json
        return dbacceso.query_db( '''select o.codigo as codigo, o.comentarios as comentarios, o.fecha as fecha
         from ojeo o, jugador p 
         where p.codigo=? and o.codigo_jugador=p.codigo''', (jid,) )
        
        
    def transformar_json(self):
        return { 'jugador' : self.jugador.transformar_json(), 'fecha' : self.fecha, 'comentarios' : self.comentarios }
        
    # Devuelve los jugadores ojeados
    def dame_todos_json():
        data = dbacceso.query_db('''select distinct j.codigo, j.nombre
        from ojeo o, jugador j
        where o.codigo_jugador = j.codigo
        ORDER BY o.fecha
        ''')
        
        #data = dbacceso.query_db('''select o.codigo as cod, o.codigo_jugador codj, o.fecha, o.comentarios, j.nombre, j.club, j.posicion, j.costo
        #from ojeo o, jugador j
        #where o.codigo_jugador = j.codigo
        #ORDER BY o.fecha
        #''')
        
        #ret = {}
        
        #for x in range(len(data)):
            #data[x] = { "codigo":data[x]['cod'], "fecha":data[x]['fecha'], "jugador":{"codigo_jugador":data[x]['codj'],"nombre":data[x]['nombre'],
             #"#club":data[x]['club'], "posicion":data[x]['posicion'], }, "comentarios":data[x]['comentarios'] }
        
        return data


    def guardar_bd(self):
        dbacceso.insert_db( 'insert into ojeo values (?, ?, ?, ?)', (self.codigo, self.jugador.codigo, self.comentarios, self.fecha) )
        
        
    def cargar_bd(self):
        data =  dbacceso.query_db( 'select * from ojeo where codigo = ?', (self.codigo,), one=True )
        
        return Ojeo( data['codigo'], jugador.Jugador(data['codigo_jugador']).cargar_bd(), data['fecha'], data['comentarios'] )
        
    def eliminar_bd(self):
        dbacceso.insert_db( 'delete from ojeo where codigo = ?', (self.codigo,) )

    def __init__(self, codigo, jugador=None, fecha="", comentarios=""):
        self.comentarios = comentarios
        self.fecha = fecha
        self.codigo = codigo
        self.jugador = jugador # Objeto jugador (NO ES CODIGO)
