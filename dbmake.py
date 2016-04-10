import sqlite3



def db_main():
    conn = sqlite3.connect('juga_base.db')
    
    cur = conn.cursor()
    
    #cur.execute( '''DROP TABLE jugador''' )
    
    cur.execute( ''' CREATE TABLE jugador
    (codigo integer PRIMARY KEY, nombre text, club text, posicion text, costo real) ''' )
    
    cur.execute(''' CREATE TABLE ojeo
    (codigo integer PRIMARY KEY, codigo_jugador integer, comentarios text, fecha text, FOREIGN KEY(codigo_jugador) REFERENCES jugador(codigo))
      ''')
    
    #cur.execute(  )
    conn.commit()
    
    conn.close()

if __name__ == "__main__":
    db_main()