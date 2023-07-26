# Password Strength Checker

This is a simple Python script that checks the strength of a given password based on various criteria. It evaluates the password for length, lowercase letters, uppercase letters, digits, and special characters, and provides feedback on its strength.

## How to Use

1. Clone the repository or download the script file `password_strength_checker.py`.

2. Run the script using Python (Python 3.x is recommended).

3. Enter the password you want to check when prompted.

4. The script will evaluate the password and display its strength along with any areas of improvement.

## Criteria for Password Strength

The password is evaluated against the following criteria:

- Minimum password length: The password should have at least 8 characters.

- At least one lowercase letter: The password should contain at least one lowercase letter (a-z).

- At least one uppercase letter: The password should contain at least one uppercase letter (A-Z).

- At least one digit: The password should contain at least one digit (0-9).

- At least one special character: The password should contain at least one special character (!@#$%^&*()_+=-[]{};:'",.<>?/\\|).

## Password Strength Scores

The password is given a strength score based on the number of criteria met:

- 1: Weak - The password does not meet the minimum length requirement.

- 2: Moderate - The password meets the minimum length requirement but lacks some character types.

- 3: Fair - The password meets the minimum length requirement and includes lowercase letters, uppercase letters, and digits.

- 4: Strong - The password meets the minimum length requirement and includes lowercase letters, uppercase letters, digits, and at least one special character.

- 5: Very Strong - The password meets all criteria and is considered very strong.

## Example

```bash
$ python password_strength_checker.py
Enter your password: My$3cureP@ssw0rd

Password Strength: 5
Password is very strong!
```

## Customization

You can customize the min_length variable in the script to set your desired minimum password length.

Feel free to modify and enhance the script according to your needs and security requirements.
