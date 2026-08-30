
"""
    USER MANAGEMENT
"""

from crud.views import User
from services.action import actions
from services.color import change_color


while True:
    print("\033[96m")
    print(
        """
            ========= USER MANAGEMENT ==========

            1. Show users list
            2. Add user
            3. Update user
            4. Delete user
            5. Quite
        """
    )

    try:
        action = input("Enter an action to perform : ")

        if action == '5':
            print("==== PROGRAM ENDED ====")
            break
        
        if action.isdigit():
            actions(action, User)
        else:
            change_color("Enter the action number.", "\033[91m")
    except Exception as e:
        print(str(e))