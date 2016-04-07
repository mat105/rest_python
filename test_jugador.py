import unittest

import cliente
import json


class TestJugador(unittest.TestCase):

    def setUp(self):
        self.app = cliente.app.test_client()
        #cliente.Jugador.crear_ejemplos()
        
    def test_get_jugadores(self):
        ret = self.app.get('/jugador').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict
    
        self.assertEqual( len(retpy), 0 )
    
        self.app.post('/jugador', data={'nombre':'Cebolla', 'club':'independiente', 'posicion':'volante', 'costo':1000})
    
        ret = self.app.get('/jugador').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict

        self.assertEqual( len(retpy) , 1 )
        
if __name__ == "__main__":
    unittest.main()