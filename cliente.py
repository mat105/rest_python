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

    
    
        
def guardar_sqlite(cod_id, jug):
    personas[cod_id] = jug
    
    
class RecursoJugadores(Resource):
    def get(self):
        return Jugador.dame_todos_json()


class RecursoOjeos(Resource):
    def get(self):
        return Ojeo.dame_todos_json()


class RecursoJugador(Resource):
    def get(self, id):
        jug = Jugador(id).cargar_bd()
        
        if jug:
            return jug.juga_json()
        else:
            return {}
            
    def post(self, id):
        args = parser_jugador.parse_args()


class RecursoOjeo(Resource):
    def get(self, id):
        ojo = Ojeo(id).cargar_bd()
        
        if ojo:
            return ojo
        else:
            return None
            
    def post(self, id):
        args = parser_jugador.parse_args()



api.add_resource(RecursoJugadores, '/jugador')
api.add_resource(RecursoJugador, '/jugador/<int:id>')
api.add_resource(RecursoOjeos, '/ojeo')
api.add_resource(RecursoOjeo, '/ojeo/<int:id>')



def main():
    Jugador.crear_ejemplos()
    
    app.debug = True
    app.run()

if __name__ == "__main__":
    main()