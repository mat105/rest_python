from Flask import Flask, url_for

app = Flask(__name__)

@app.route('/')

class Ojeo:
	CODIGO = 0

	def __init__(self, jugador, fecha, comentarios):
		self.comentarios = comentarios
		self.fecha = fecha
		self.codigo = Ojeo.CODIGO
		
		Ojeo.CODIGO+=1

class Jugador:
	CODIGO = 0

	def agregar_ojeo(self, ojo):
		self.ojeos.append(ojo)

	def __init__(self, nombre, club, posicion, costo):
		self.nombre = nombre
		self.club = club
		self.posicion = posicion
		self.costo = costo
		self.ojeos = []
		self.codigo = Jugador.CODIGO
		
		Jugador.CODIGO+=1
		

# A remover
personas = {}
ojeos = {}
		
def index():
	pass
	
@app.route('/jugador')
def jugadores():
	return personas
	
@app.route('/jugador/<int:cod_id>')
def jugador(cod_id):
	return personas[cod_id]

@app.route('/ojeo')
def ojeos():
	return ojeos

@app.route('/ojeo/<int:cod_id>')
def ojeo(cod_id):
	return ojeos[cod_id]
