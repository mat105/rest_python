# rest_python
API REST en python.

/jugador
Devuelve todos los jugadores conocidos.

/jugador/ojeo
Devuelve todos los ojeos conocidos (con la informacion del jugador ojeado incluida).

/jugador/=>codigo_jugador<=/ojeo
Devuelve todos los ojeos para un jugador particular.

/jugador/ojeo/=>codigo_ojeo<=
Devuelve la informacion especifica de un ojeo.

/api/doc
Documentación de la API


Instalar dependencias:
(flask, flask-restful, flask-compress, flask-restful-swagger)
pip install -r requisitos.txt

Instalacion:
python dbmake.py

Levantar:
python cliente.py

Testeo:
python test_jugador.py