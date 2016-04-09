import sqlite3

BASE_RUTA = "juga_base.db"


def query_db(query, args=(), one=False):
    con = sqlite3.connect(BASE_RUTA)
    cur = con.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    con.close()
    return (rv[0] if rv else None) if one else rv


def insert_db(query, args=()):
    con = sqlite3.connect(BASE_RUTA)
    cur = con.execute(query, args)
    con.commit()
    con.close()