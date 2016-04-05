from flask import Flask, request, url_for, render_template

app = Flask(__name__)


class Ojeo:
    CODIGO = 0

    def __init__(self, jugador, fecha, comentarios):
        self.comentarios = comentarios
        self.fecha = fecha
        self.codigo = Ojeo.CODIGO

        Ojeo.CODIGO+=1


class Jugador:
    CODIGO = 0

    def __str__(self):
        return "Nombre: {}      Club: {}        Posicion: {}        Costo: {}".format( self.nombre, self.club, self.posicion, self.costo )
        
    def __repr__(self):
        return "Nombre: {}      Club: {}".format(self.nombre, self.club)

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
personas = {
    0:Jugador("Cebolla", "Independiente", "Volante", 10000000),
    1:Jugador("Messi", "Barcelona", "Delantero", 80000000),
    2:Jugador("Robben", "Bayern Munich", "Delantero", 30312424)
    }
    
ojeos = {}
		
@app.route('/')
def index():
    return "Bienvenido"
	
@app.route('/jugador')
def jugadores():
    return render_template('jugador_listado.html', listado = personas)
	
    
def guardar_sqlite(cod_id, jug):
    personas[cod_id] = jug
    
@app.route('/jugador/<int:cod_id>', methods=['GET', 'POST'])
def jugador(cod_id):
    jug = personas.get(cod_id, None)
    nom = club = posicion = costo = None
    success=0
    
    
    if request.method == 'POST':
        nom = request.args.get('nombre',None)
        club = request.args.get('club', None)
        posicion = request.args.get('posicion', None)
        costo = request.args.get('costo', None)
        
        if not jug and nom and club and posicion and costo:
            jug = Jugador(nom, club, posicion, costo)
            guardar_sqlite(cod_id, jug)
        elif jug:
            success = 1 # Ya existe
        else:
            success = 2 # Parametros insuficientes
    else:
        if jug:
            nom = jug.nombre
            club = jug.club
            posicion = jug.posicion
            costo = jug.costo
        else:
            success = 3 # No existe
    
    return render_template('jugador.html', nombre = nom, club = club, posicion = posicion, costo = costo, error=success )
    #return str(personas[cod_id])

@app.route('/ojeo')
def ojeos():
    return str(ojeos)

@app.route('/ojeo/<int:cod_id>', methods=['GET', 'POST'])
def ojeo(cod_id):
    return ojeos[cod_id]


if __name__ == "__main__":
    app.debug = True
    app.run()