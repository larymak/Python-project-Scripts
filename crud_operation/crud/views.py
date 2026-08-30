from crud.db import db_connection
from crud.models import Model
from services.color import change_color

Model().user()

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def insert_user(self):
        con, cursor = db_connection()

        clean = self.clean_data()
        if clean:
            cursor.execute(
                "INSERT OR IGNORE INTO Users(first_name, last_name, age, email) VALUES (?,?,?,?)",
                (self.first_name, self.last_name, self.age, self.email)
            )
            con.commit()
            change_color("\n ===> User added successfully", "\033[92m")

    @staticmethod
    def select_user():
        _, cursor = db_connection()

        cursor.execute("SELECT* FROM Users")
        users = cursor.fetchall()
        return users
    
    def update_user(self):
        con, cursor = db_connection()
        user_id = User.user_id('update')

        cursor.execute(
            "SELECT * FROM Users WHERE id=?",
            (user_id,)
        )
        user = cursor.fetchone()
        
        new_age = self.age if self.age not in (None, "") else user[3]
        if isinstance(new_age, str) and new_age.isdigit():
            new_age = int(new_age)
     
        if user:
            cursor.execute(
                "UPDATE Users SET first_name=?, last_name=?, age=?, email=? WHERE id=?",
                (
                    self.first_name or user[1],
                    self.last_name or user[2],new_age,
                    self.email or user[4], user_id)
            )
            con.commit()
            change_color("\n ===> User modified successfully", "\033[92m")
        else:
            change_color("\n ===> User doesn't exist.", "\033[91m")
    
    @staticmethod
    def delete_user():
        con, cursor = db_connection()
        user_id = User.user_id('delete')
        users = User.select_user()

        user = [user for user in users if user[0] == user_id]
        if user:
            cursor.execute(
                "DELETE FROM Users WHERE id=?",(user_id,)
            )
            con.commit()
            change_color("\n ===> User delete successfully", "\033[92m")
        else:
            change_color("\n ===> Enter a valid id", "\033[91m")
            
    @staticmethod
    def user_id(a: str):
        try:
            user_id = int(input(f"Enter a user_id to {a} : "))
            return user_id
        except:
            change_color("Id can be a number.", "\033[91m")

    def clean_data(self):
        if not self.age.isdigit():
            change_color("\n ===> Enter the action number")
            return False
        elif not self.email.endswith("@gmail.com"):
            change_color("\n ===> Enter a valid email.", "\033[91m")
            return False
        return True
