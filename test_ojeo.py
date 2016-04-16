import unittest

import cliente
import json

from ojeo import Ojeo
import jugador
#from ojeo import Ojeo


class TestOjeo(unittest.TestCase):

    def setUp(self):
        dbacceso.activar_testeo()
        self.app = cliente.app.test_client()
        #cliente.Ojeo.crear_ejemplos()
        dbacceso.insert_test_db('delete from jugador')

        
    def test_get_Ojeos(self):
        return None # --
        ret = self.app.get('/Ojeo').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict
    
        len_now = len(retpy)
    
        self.app.post('/Ojeo', data={'nombre':'Cebolla', 'club':'independiente', 'posicion':'volante', 'costo':1000})
    
        ret = self.app.get('/Ojeo').get_data(as_text=True) # JSON string
        retpy = json.loads(ret) # Python dict

        self.assertEqual( len(retpy) , len_now+1 )
        
if __name__ == "__main__":
    unittest.main()