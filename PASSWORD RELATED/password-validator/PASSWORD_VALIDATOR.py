import string

def passwordValidator():
    """
    Validates passwords to match specific rules
    : return: str
    """
    # display rules that a password must conform to
    print('\nYour password should: ')
    print('\t- Have a minimum length of 6;')
    print('\t- Have a maximum length of 12;')
    print('\t- Should not start with a number;')
    print('\t- Contain at least one uppercase letter and one lowercase letter;')
    print('\t- Contain at least a number;')
    print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
    print('\t- Not contain space(s).')
   # get user's password
    userPassword = input('\nEnter a valid password: ').strip()
   # check if user's password conforms 
   # to the rules above

    # Check length of password (6 to 12 characters)
    if not(6 <= len(userPassword) <= 12):
        message = 'Invalid Password: Password should have a minimum '
        message += 'length of 6 and a maximum length of 12'
        return message
    
    # Check if first character is a digit
    if userPassword and not(userPassword[0].isalpha()):
        message = "Invalid Password: First character should be a letter."
        return message
    
    # Check for spaces in password (Password mustn't contain any spaces)
    if ' ' in userPassword:
       message = 'Invalid Password: Password shouldn\'t contain space(s)'
       return message
    
    # Check for at least 1 upper case and 1 lower case letter in password
    if not (any(c.islower() for c in userPassword) and any(c.isupper() for c in userPassword)):
      message = "Invalid Password: Password should contain both uppercase and lowercase letters."
      return message
    
    # Check for at least 1 digit in password
    if not any(c.isdigit() for c in userPassword):
        message = 'Invalid Password: Password should contain at least one number.'
        return message
    
    # Check for at least 1 special character in password
    if not any(i in string.punctuation for i in userPassword): 
       message = 'Invalid Password: Password should contain at least a special character'
       return message
    
    # If no condition fails - password considered to be valid
    return 'Valid Password!'

my_password = passwordValidator()
print(my_password)