user_input = int(input("Enter a number of your choice : "))

if(user_input == 1):
    for i in range(5,0,-1):
        print("*"*i)

elif(user_input == 2):
    for i in range(5,0,-1):
        print("*"*i)
    for j in range(2,6):
        print("-"*j)

else:
    print("Invalid input")