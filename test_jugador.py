import unittest

import cliente
import json

from jugador import Jugador
#from ojeo import Ojeo


class TestJugador(unittest.TestCase):

    def setUp(self):
        self.app = cliente.app.test_client()
        #cliente.Jugador.crear_ejemplos()
        
    def test_ultimo_codigo(self):
        previo = Jugador.ultimo_codigo()
        
        Jugador( Jugador.ultimo_codigo()+1 , "Pepe", "Real", "Defensor", 1000).guardar_bd()
        self.assertNotEqual( Jugador.ultimo_codigo(), previo )
        
    def test_guardar_bd(self):
        tot = Jugador.dame_todos()
        len_now = len(tot)
        
        Jugador( Jugador.ultimo_codigo()+1 , "Pepe", "Real", "Defensor", 1000).guardar_bd()
        self.assertEqual( len(Jugador.dame_todos()), len_now+1 )
        
    def test_cargar_bd(self):
        juga = Jugador( Jugador.ultimo_codigo()+1 , "Roman", "Boca", "Volante", 122000)
        juga.guardar_bd()
        
        self.assertEqual( Jugador( Jugador.ultimo_codigo() ).cargar_bd().nombre, juga.nombre )
        
        
    def test_get_jugadores(self):
        return None # --
        ret = self.app.get('/jugador').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict
    
        len_now = len(retpy)
    
        self.app.post('/jugador', data={'nombre':'Cebolla', 'club':'independiente', 'posicion':'volante', 'costo':1000})
    
        ret = self.app.get('/jugador').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict

        self.assertEqual( len(retpy) , len_now+1 )
        
if __name__ == "__main__":
    unittest.main()