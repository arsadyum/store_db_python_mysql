import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='newuser', password='',
                                  host='localhost',
                                  database='arsad_store')
        return __cnx
