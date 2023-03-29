import string
import secrets

# Define the set of characters to be used in the password
CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    """Generate a random password of the specified length."""
    password = ''.join(secrets.choice(CHARACTER_SET) for i in range(length))
    return password

def main():
    # Prompt the user for the number of passwords to generate and their length
    while True:
        try:
            num_pass = int(input("How many passwords do you want to generate? "))
            password_length = int(input("Enter the length of the password(s): "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate the specified number of passwords and print them to the console
    print("Generated passwords:")
    for i in range(num_pass):
        password = generate_password(password_length)
        print(f"{i+1}. {password}")

if __name__ == "__main__":
    main()
