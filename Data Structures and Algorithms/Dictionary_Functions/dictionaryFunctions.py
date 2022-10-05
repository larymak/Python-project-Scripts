def func1():
    print("I am func1")
def func2():
    print("I am func2")
def func3():
    print("I am func3")
def func4():
    print("I am func4")
def func5():
    print("I am func5")

def end():
    print("I hope you learned something about dictionaries in python :)")
    return True


def main():
    dictOfFunctions = {
        '1' : func1,
        '2' : func2,
        '3' : func3,
        '4' : func4,
        '5' : func5,
        'q' : end
    }

    print("Welcome to this simple demo! To exit, enter 'q'")

    while True:
        user = input("Please let me know what function to run (enter a number 1-5)\n> ").lower()
        try:
            output = dictOfFunctions[user]()
            if output:
                break
        except (KeyError, TypeError) as e:
            print("That was an invalid input. Please input either 1-5 or 'q'")

if __name__ == '__main__':
    main()