import unittest

import cliente
import json

import dbacceso

import random

from jugador import Jugador
#from ojeo import Ojeo


testapp = None


def iniciar_testeo_jugador():
    dbacceso.activar_testeo()
    
    dbacceso.insert_db('delete from jugador')
    
    #cliente.Jugador.crear_ejemplos()
    nombres = ["juan", "pepe", "pedro", "samuel", "diego", "cristian", "marcos", "lionel", "victor"]
    clubes = ["independiente", "boca", "racing", "colon", "lanus"]
    posiciones = ["defensor", "delantero", "volante", "arquero"]
    
    ln = len(nombres)
    lc = len(clubes)
    lp = len(posiciones)

    
    for x in range(24):
        Jugador( Jugador.ultimo_codigo()+1, nombres[x%ln], clubes[x%lc], posiciones[x%lp], random.randint(1000, 1000000) ).guardar_bd()
    
    Jugador( Jugador.ultimo_codigo()+1, "ricardito", "river", "defensor", 2345235 ).guardar_bd()
    Jugador( Jugador.ultimo_codigo()+1, "rubencito", "central", "defensor", 4234231 ).guardar_bd()


class TestJugador(unittest.TestCase):

    def setUp(self):
        self.app = cliente.app.test_client()
        
    def test_delete_jugadores(self):
        ret = self.app.delete('/jugador/25')
        
        self.assertEqual( len( json.loads(self.app.get('/jugador').get_data(as_text=True) ) ), 25 )

        
    def test_get_jugadores(self):
        ret = self.app.get('/jugador').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict
        #print(retpy)
    
        self.assertEqual( len(retpy), 25 )
        self.assertEqual( retpy[ len(retpy)-1 ]['nombre'], 'ricardito' )
        
    def test_post_jugador(self):
        ret = self.app.get('/jugador').get_data(as_text=True)
        retpy = len( json.loads(ret) )
        
        self.app.post( '/jugador', data={'nombre':"jaimito", 'club':"racing", 'posicion':"defensor", 'costo':725533} )
        nretpy = json.loads( self.app.get('/jugador', data={'listado':'asc'}).get_data(as_text=True) )
        
        self.assertEqual( nretpy[len(nretpy)-1]['nombre'], 'jaimito' )
        self.assertEqual( len(nretpy), retpy+1 )
        
        
        
        
if __name__ == "__main__":
    cliente.iniciar()
    iniciar_testeo_jugador()
    unittest.main()