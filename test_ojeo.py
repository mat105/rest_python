import unittest

import cliente
import json

from ojeo import Ojeo
import jugador
#from ojeo import Ojeo


class TestOjeo(unittest.TestCase):

    def setUp(self):
        self.app = cliente.app.test_client()
        #cliente.Ojeo.crear_ejemplos()
        
    def test_ultimo_codigo(self):
        previo = Ojeo.ultimo_codigo()

        Ojeo( Ojeo.ultimo_codigo()+1 , jugador.Jugador(1).cargar_bd(), "2014/01/02", "comentarioxx").guardar_bd()
        self.assertNotEqual( Ojeo.ultimo_codigo(), previo )
        
    def test_guardar_bd(self):
        tot = Ojeo.dame_todos()
        len_now = len(tot)
        
        Ojeo( Ojeo.ultimo_codigo()+1 , jugador.Jugador(1).cargar_bd(), "2014/01/02", "comentarioxx").guardar_bd()
        self.assertEqual( len(Ojeo.dame_todos()), len_now+1 )
        
    def test_cargar_bd(self):
        juga = Ojeo( Ojeo.ultimo_codigo()+1 , jugador.Jugador(1).cargar_bd(), "2014/01/02", "comentarioxx")
        juga.guardar_bd()
        
        self.assertEqual( Ojeo( Ojeo.ultimo_codigo() ).cargar_bd().comentarios, juga.comentarios )
        
        
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