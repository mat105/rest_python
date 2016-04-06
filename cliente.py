from flask import Flask, request, url_for, render_template
from flask_restful import Resource, Api, reqparse
import json

import jugador
import ojeo


app = Flask(__name__)
api = Api(app)


parser_jugador = reqparse.RequestParser()
parser_jugador.add_argument('nombre', type=str, help='Nombre del jugador')
parser_jugador.add_argument('club', type=str, help='Nombre del club')
parser_jugador.add_argument('posicion', type=str, help='Posicion del jugador')
parser_jugador.add_argument('costo', type=int, help='Costo del pase')
		

# A remover

    
    
        
def guardar_sqlite(cod_id, jug):
    personas[cod_id] = jug
    
    
class RecursoJugadores(Resource):
    def get(self):
        return Jugador.dame_todos()


class RecursoOjeos(Resource):
    def get(self):
        return Ojeo.dame_todos()


class RecursoJugador(Resource):
    def get(self, id):
        jug = Persona(id).cargar_bd()
        
        if jug:
            return jug
        else:
            return None
            
    def post(self, id):
        args = parser_jugador.parse_args()


class RecursoOjeo(Resource):
    def get(self, id):
        jug = Ojeo(id).cargar_bd()
        
        if jug:
            return jug
        else:
            return None
            
    def post(self, id):
        args = parser_jugador.parse_args()


if __name__ == "__main__":
    app.debug = True
    app.run()