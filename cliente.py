from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields
from flask.ext.compress import Compress
from flask_restful_swagger import swagger
from flask.ext.restful.utils import cors

from functools import update_wrapper
from datetime import timedelta


import json
import hashlib

from jugador import Jugador
from ojeo import Ojeo


from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()



app = Flask(__name__)
#api = Api(app)
api = swagger.docs( Api(app), apiVersion='0.1', api_spec_url='/api/doc' )

compress = Compress()

api.decorators=[cors.crossdomain(origin='*')]



#===
# Parsers
#===
parser_jugadores_get = reqparse.RequestParser()

parser_jugador = reqparse.RequestParser()

parser_ojeo = reqparse.RequestParser()

parser_ojeos = reqparse.RequestParser()

parser_ojeos_jugador = reqparse.RequestParser()
#===
    
def iniciar_parsers():
    parser_jugadores_get.add_argument('nombre', type=str, help='Nombre del jugador')
    parser_jugadores_get.add_argument('club', type=str, help='Nombre del club')
    parser_jugadores_get.add_argument('posicion', type=str, help='Posicion del jugador')
    parser_jugadores_get.add_argument('orden', type=str, help='Ordenar por cual campo')
    parser_jugadores_get.add_argument('listado', type=str, help='Ordenar DESCendente o ASCendente')
    parser_jugadores_get.add_argument('hash', type=str, help='Hash del listado cacheado en el cliente (si se tiene)')
    
    parser_jugador.add_argument('nombre', type=str, help='Nombre del jugador')
    parser_jugador.add_argument('club', type=str, help='Nombre del club')
    parser_jugador.add_argument('posicion', type=str, help='Posicion del jugador')
    parser_jugador.add_argument('costo', type=int, help='Costo del pase')
    
    parser_ojeo.add_argument('fecha', type=str, help='Fecha del ojeo')
    parser_ojeo.add_argument('comentarios', type=str, help='Comentarios sobre el jugador')
    
    parser_ojeos.add_argument('hash', type=str, help='Hash del listado cacheado en el cliente (si se tiene)')
    
    parser_ojeos_jugador.add_argument('hash', type=str, help='Hash del listado cacheado en el cliente (si se tiene)')
    
    
    
@auth.verify_password
def verify_password(username, password):
    return (username == "pepe" and password == "123")
    

    
#/jugador
class RecursoJugadores(Resource):
    "Listar jugadores"
    #@auth.login_required
    @swagger.operation(
        notes='Listado de jugadores',
        nickname='get',
        parameters=[
            {
            "name": "nombre",
            "description": "El nombre por el cual filtrar la lista.",
            "required": False,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "club",
            "description": "El club por el cual filtrar la lista.",
            "required": False,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "posicion",
            "description": "La posicion por la cual filtrar la lista.",
            "required": False,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "orden",
            "description": "El campo por el cual ordenar la lista. [nombre|club|posicion|costo]",
            "required": False,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "listado",
            "description": "La forma de ordenar la lista (ascendente o descendente). [asc|desc]",
            "required": False,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            }
        ]
    )
    #@cors.crossdomain(origin='*')
    def get(self):
        args = parser_jugadores_get.parse_args()

        ordenado = args.get( 'orden', None ) # None => Default
        listado = args.get('listado', None) # None => Default
        ehash = args.get('hash', None)
        
        if ordenado and not ordenado in ['nombre', 'club', 'posicion', 'costo']:
            ordenado = None
        if listado and not listado in ['asc', 'desc']:
            listado = None

        datos = Jugador.query( args.get('nombre', None), args.get('club', None), args.get('posicion', None), ordenado, listado )

        if ehash and ehash == hashlib.sha256( json.dumps( datos, sort_keys=True ).encode() ).hexdigest():
            return '', 304

        return datos, 200
        #Jugador.dame_todos_json(), 200
        
    @swagger.operation(
        notes='Agregar jugador al listado.',
        nickname='post',
        parameters=[
            {
            "name": "nombre",
            "description": "El nombre del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "club",
            "description": "El club del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "posicion",
            "description": "La posicion (usual) del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "costo",
            "description": "El costo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'double',
            "paramType": "query"
            }
        ]
    )
        
    def post(self):
        args = parser_jugador.parse_args()
        tid = Jugador.ultimo_codigo() + 1
        
        juga = Jugador( tid, args['nombre'], args['club'], args['posicion'], args['costo'] )
        juga.guardar_bd()
        
        return juga.transformar_json(), 201


#/jugador/ojeo
class RecursoOjeos(Resource):
    #@auth.login_required
    @swagger.operation(
        notes='Listado de ojeos.',
        nickname='get',
    )
    def get(self):
        args = parser_ojeos.parse_args()
        datos = Ojeo.dame_todos_json()
        
        if args.get('hash', None) == hashlib.sha256( json.dumps(datos, sort_keys=True).encode() ).hexdigest():
            return '', 304
        
        return datos, 200


#/jugador/<cod>
class RecursoJugador(Resource):

    #@auth.login_required
    @swagger.operation(
        notes='Modificar datos del jugador.',
        nickname='put',
        parameters=[
            {
            "name": "id",
            "description": "El codigo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            },
            {
            "name": "nombre",
            "description": "El nombre del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "club",
            "description": "El club del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "posicion",
            "description": "La posicion (usual) del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "costo",
            "description": "El costo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'double',
            "paramType": "query"
            }
        ]
        
    )
    def put(self, id):
        args = parser_jugador.parse_args()
        
        juga = Jugador( id, args['nombre'], args['club'], args['posicion'], args['costo'] )
        #juga.guardar_bd() # Agregando esto podria hacer creacion en caso de que no existe y el update no tendria efecto.
        juga.modificar_bd()
        
        return juga.transformar_json(), 201

    @swagger.operation(
        notes='Ver informacion del jugador.',
        nickname='get',
        parameters = [
            {
            "name": "id",
            "description": "El codigo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            }
            
        ]
    )

    def get(self, id):
        jug = Jugador(id).cargar_bd()
        
        if jug:
            return jug.transformar_json(), 200
        else:
            return {}, 404
            
    @swagger.operation(
        notes='Borrar jugador.',
        nickname='delete',
        parameters = [
            {
            "name": "id",
            "description": "El codigo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            }
            
        ]
    )   
    def delete(self, id):
        jug = Jugador(id).cargar_bd()
        
        if jug:
            jug.eliminar_bd()
            return {}, 200
            
        return {}, 404

#/jugador/ojeo/<cod>
class RecursoOjeoEspecifico(Resource):
    #@auth.login_required
    @swagger.operation(
        notes='Ver informacion del ojeo.',
        nickname='get',
        parameters = [
            {
            "name": "id",
            "description": "El codigo del ojeo.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            }
            
        ]
    )
    def get(self, id):
        ojo = Ojeo(id).cargar_bd()
        
        if ojo:
            return ojo.transformar_json()
        else:
            return {}, 404
            
            
    @swagger.operation(
        notes='Borrar ojeo.',
        nickname='delete',
        parameters = [
            {
            "name": "id",
            "description": "El codigo del ojeo.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            }
            
        ]
    )
    def delete(self, id):
        ojo = Ojeo(id).cargar_bd()
        
        if ojo:
            ojo.eliminar_bd()
            return {}, 200
            
        return {}, 404

#/jugador/<cod>/ojeo
class RecursoJugadorOjeos(Resource):

    @swagger.operation(
        notes='Ver ojeos del jugador.',
        nickname='get',
        parameters = [
            {
            "name": "id",
            "description": "El codigo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            }
            
        ]
    )
    def get(self, id):
        args = parser_ojeos_jugador.parse_args()
        #jug = Jugador(id).cargar_bd()
        lis = Ojeo.dame_todos_json_jugador(id)
        
        if( lis ):
            if args.get('hash', None) == hashlib.sha256( json.dumps(lis, sort_keys=True).encode() ).hexdigest():
                return '', 304
            
            return lis
        else:
            return {}, 404 # Error?. Revisar
            
    @swagger.operation(
        notes='Modificar datos del jugador.',
        nickname='put',
        parameters=[
            {
            "name": "id",
            "description": "El codigo del jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'integer',
            "paramType": "path"
            },
            {
            "name": "fecha",
            "description": "Fecha del ojeo.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            },
            {
            "name": "comentarios",
            "description": "Comentarios sobre el jugador.",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
            "paramType": "query"
            }
        ]
        
    )
    def post(self, id):
        args = parser_ojeo.parse_args()
        tid = Ojeo.ultimo_codigo() + 1
        
        juga = Jugador(id).cargar_bd()
        
        if juga:
            ojo = Ojeo (tid, juga, args['fecha'], args['comentarios'])
            if ojo:
                ojo.guardar_bd()
                return ojo.transformar_json(), 201

        return {}, 404




def iniciar():
    iniciar_parsers()

    api.add_resource(RecursoJugadores, '/jugador')
    api.add_resource(RecursoJugador, '/jugador/<int:id>')
    api.add_resource(RecursoOjeos, '/jugador/ojeo')
    api.add_resource(RecursoOjeoEspecifico, '/jugador/ojeo/<int:id>')
    api.add_resource(RecursoJugadorOjeos, '/jugador/<int:id>/ojeo')


def main():
    #Jugador.crear_ejemplos()
    iniciar()
    app.debug = True
    compress.init_app(app)
    app.run()


if __name__ == "__main__":
    main()