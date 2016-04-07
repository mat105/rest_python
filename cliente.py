from flask import Flask, request, url_for, render_template
from flask_restful import Resource, Api, reqparse

import json

from jugador import Jugador
from ojeo import Ojeo


app = Flask(__name__)
api = Api(app)


parser_jugador = reqparse.RequestParser()
parser_jugador.add_argument('nombre', type=str, help='Nombre del jugador')
parser_jugador.add_argument('club', type=str, help='Nombre del club')
parser_jugador.add_argument('posicion', type=str, help='Posicion del jugador')
parser_jugador.add_argument('costo', type=int, help='Costo del pase')

parser_ojeo = reqparse.RequestParser()
parser_ojeo.add_argument('fecha', type=str, help='Fecha del ojeo')
parser_ojeo.add_argument('comentarios', type=str, help='Comentarios sobre el jugador')
    
    
#/jugador
class RecursoJugadores(Resource):
    def get(self):
        return Jugador.dame_todos_json(), 200
        
    def post(self):
        args = parser_jugador.parse_args()
        tid = Jugador.ultimo_codigo() + 1
        
        juga = Jugador( tid, args['nombre'], args['club'], args['posicion'], args['costo'] )
        juga.guardar_bd()
        
        return juga.transformar_json(), 201


#/jugador/ojeo
class RecursoOjeos(Resource):
    def get(self):
        return Ojeo.dame_todos_json(), 200


#/jugador/<cod>
class RecursoJugador(Resource):

    def put(self, id):
        args = parser_jugador.parse_args()
        
        juga = Jugador( id, args['nombre'], args['club'], args['posicion'], args['costo'] )
        juga.guardar_bd()
        
        return juga.transformar_json(), 201

    def get(self, id):
        jug = Jugador(id).cargar_bd()
        
        if jug:
            return jug.transformar_json(), 200
        else:
            return {}, 404
            
    def delete(self, id):
        jug = Jugador(id).cargar_bd()
        
        if jug:
            jug.eliminar_bd()
            return {}, 200
            
        return {}, 404

#/jugador/ojeo/<cod>
class RecursoOjeoEspecifico(Resource):
    def get(self, id):
        ojo = Ojeo(id).cargar_bd()
        
        if ojo:
            return ojo.transformar_json()
        else:
            return {}, 404
            
    def delete(self, id):
        ojo = Ojeo(id).cargar_bd()
        
        if ojo:
            ojo.eliminar_bd()
            return {}, 200
            
        return {}, 404

#/jugador/<cod>/ojeo
class RecursoJugadorOjeos(Resource):
    def get(self, id):
        #jug = Jugador(id).cargar_bd()
        lis = Ojeo.dame_todos_json_jugador(id)
        
        if( lis ):
            return lis
        else:
            return {}, 404 # Error
            
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


api.add_resource(RecursoJugadores, '/jugador')
api.add_resource(RecursoJugador, '/jugador/<int:id>')
api.add_resource(RecursoOjeos, '/jugador/ojeo')
api.add_resource(RecursoOjeoEspecifico, '/jugador/ojeo/<int:id>')
api.add_resource(RecursoJugadorOjeos, '/jugador/<int:id>/ojeo')



def main():
    Jugador.crear_ejemplos()
    
    app.debug = True
    app.run()


if __name__ == "__main__":
    main()