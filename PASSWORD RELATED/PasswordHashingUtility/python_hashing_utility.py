import hashlib

def get_hashed_password(password, algorithm='sha256'):
    """
    Hashes the input password using the specified hashing algorithm.

    Args:
        password (str): The input password to be hashed.
        algorithm (str): The hashing algorithm to use (default is SHA-256).

    Returns:
        str: The hashed password as a hexadecimal string.
    """
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hashing algorithm: {algorithm}")

    hashed_password = hashlib.new(algorithm, password.encode()).hexdigest()
    return hashed_password

if __name__ == "__main__":
    print("Password Hashing Utility")
    print("------------------------")

    password = input("Enter your password: ")

    try:
        # You can choose the hashing algorithm here (e.g., 'md5', 'sha256', etc.)
        algorithm = 'sha256'
        hashed_password = get_hashed_password(password, algorithm)
        print(f"Hashed password (using {algorithm.upper()}): {hashed_password}")
    except ValueError as e:
        print(e)
