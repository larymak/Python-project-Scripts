from crud.db import db_connection

class Model:
    def user(self):
        con, cursor = db_connection()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    UNIQUE(email)
                )
            """
        )

        con.commit()
