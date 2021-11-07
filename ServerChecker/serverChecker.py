import socket 

def is_running(site):
    """This function attempts to connect to the given server using a socket.
        Returns: Whether or not it was able to connect to the server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        site = input('Website to check: ')
        if is_running(f'{site}.com'):
            print(f"{site}.com is running!")
        else:
            print(f'There is a problem with {site}.com!')

        if input("Would You like to check another website(Y/N)? ") in {'n', 'N'}:
            break