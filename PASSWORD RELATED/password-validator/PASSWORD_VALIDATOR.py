import string

def passwordValidator():
    """
    Validates passwords to match specific rules
    :return: str
    """
    print('\nYour password should: ')
    print('\t- Have a minimum length of 6;')
    print('\t- Have a maximum length of 12;')
    print('\t- Contain at least an uppercase letter;')
    print('\t- Contain at least a lowercase letter;')
    print('\t- Contain at least a number;')
    print('\t- Contain at least a special character (such as @,+,£,$,%,*^,etc);')
    print('\t- Not contain space(s).')

    userPassword = input('\nEnter a valid password: ').strip()

    # Length check
    if not(6 <= len(userPassword) <= 12):
        return 'Invalid Password..length must be between 6 and 12'
    
    # No spaces allowed
    if ' ' in userPassword:
        return 'Invalid Password..shouldn\'t contain spaces'
    
    # Uppercase letter check
    if not any(i.isupper() for i in userPassword):
        return 'Invalid Password..should contain at least one uppercase letter'
    
    # Lowercase letter check
    if not any(i.islower() for i in userPassword):
        return 'Invalid Password..should contain at least one lowercase letter'
    
    # Number check
    if not any(i.isdigit() for i in userPassword):
        return 'Invalid Password..should contain at least one number'
    
    # Special character check
    if not any(i in string.punctuation for i in userPassword):
        return 'Invalid Password..should contain at least one special character'

    return 'Valid Password!'

my_password = passwordValidator()
print(my_password)
