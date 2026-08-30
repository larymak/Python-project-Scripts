import sqlite3

con = sqlite3.connect("users.db")
cursor = con.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age REAL NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS Post(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            post TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES Users(id)
        )
    """
)

cursor.execute(
    "INSERT OR IGNORE INTO Users (name, age, email) VALUES (?,?,?)",
    ('wilondja', 52, 'wilondja@gmail.com')
)

cursor.execute(
    "INSERT INTO Post(user_id, post) VALUES (?,?)", (1, "Nous sommes les enfants de Dieu.")
)
cursor.execute("PRAGMA foreign_keys=ON;")

con.commit()

cursor.execute(
    "SELECT Users.name, Post.post FROM Post INNER JOIN Users ON Post.user_id = Users.id WHERE Post.user_id=?", (1,)
)

result = cursor.fetchone()

print(result)


cursor.close()
con.close()