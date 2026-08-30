import sqlite3

def db_connection():
    con = sqlite3.connect("db/users.db")
    cursor = con.cursor()

    return con, cursor
