import re


def password_strength(password):
    """
        Checks the strength of a password and returns a tuple containing the strength
    """
    # Minimum password length
    min_length = 8

    # Regular expressions to check for different character types
    has_lowercase = re.compile(r'[a-z]')
    has_uppercase = re.compile(r'[A-Z]')
    has_digit = re.compile(r'\d')
    has_special = re.compile(r'[!@#$%^&*()_+=\-[\]{};:\'",.<>?/\\|]')

    strength = 0
    messages = []

    if len(password) >= min_length:
        strength += 1
    else:
        messages.append("Password should have at least {} characters.".format(min_length))

    if has_lowercase.search(password):
        strength += 1
    else:
        messages.append("Password should have at least one lowercase letter.")

    if has_uppercase.search(password):
        strength += 1
    else:
        messages.append("Password should have at least one uppercase letter.")

    if has_digit.search(password):
        strength += 1
    else:
        messages.append("Password should have at least one digit.")

    if has_special.search(password):
        strength += 1
    else:
        messages.append("Password should have at least one special character.")

    return strength, messages


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, messages = password_strength(password)

    print("\nPassword Strength: {}".format(strength))
    if strength == 5:
        print("Password is very strong!")
    else:
        print("Password needs improvement:")
        for message in messages:
            print("- {}".format(message))
