from services.color import change_color

def inputs():
    first_name = input("Fist name: ")
    last_name = input("Last name: ")
    age = input("Age: ")
    email = input("Email: ")

    return (
        first_name,
        last_name,
        age,
        email
    )

def actions(action, User):
    if action == '1':
        users = User.select_user()
        print(f"\n ==> Users list <=== \n")
        if users:
            for user in users:
                print(f"{user[0]} {user[1]} {user[2]} {user[3]} {user[4]}")
        else:
            print(f"Data is emtpy => {users}")

    elif action == '2':
        user = inputs()
        if user:
            User(*user).insert_user()
        else:
            change_color("\n ===> Incorect infos", "\033[0m")
    elif action == '3':
        user = inputs()
        if user:
            User(*user).update_user()
            
    elif action == '4':
        User.delete_user()
    else:
        change_color("\n ===> Enter a valid action.", "\033[0m")