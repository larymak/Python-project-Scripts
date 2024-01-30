import socket
import pyfiglet


def int_checker(x):
    while True:
        try:
            x = int(x)
            break
        except ValueError:
            print("Error: Invalid input! Please enter an integer.")
            x = input("Enter the port to check: ")
    return x


def port_checker(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("127.0.0.1", port))
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")

    sock.close()


print(pyfiglet.figlet_format("Port Scanner"))
print("Port Scanner")
port_to_check = int_checker(input("Enter the port to check: "))
port_checker(port_to_check)
