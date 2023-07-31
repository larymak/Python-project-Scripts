# Password Hashing Utility

The Password Hashing Utility is a Python script that allows users to hash their passwords using various hashing algorithms for secure storage and comparison. Hashing passwords is an essential security measure to protect sensitive user data.

## How to Use

1. Clone the repository or download the script file `password_hashing_utility.py`.

2. Run the script using Python (Python 3.x is recommended).

3. Enter the password you want to hash when prompted.

4. Choose the desired hashing algorithm (e.g., 'md5', 'sha256', etc.).

5. The script will display the hashed password as a hexadecimal string.

## Supported Hashing Algorithms

The utility supports the following hashing algorithms available in the `hashlib` library:

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512
- And more...

Please note that MD5 and SHA-1 are considered less secure due to vulnerabilities, and it is recommended to use stronger algorithms like SHA-256 or SHA-512.

## Example

```bash
$ python password_hashing_utility.py
Password Hashing Utility
------------------------
Enter your password: MySecurePassword
Choose the hashing algorithm (e.g., 'md5', 'sha256'): sha256

Hashed password (using SHA-256): c1ef01b69b3d0e60c91f1c52e2185ab2de548be9f03f64e7c2712d3efea45d9c
```
## Customization
You can modify the algorithm variable in the script to choose a different hashing algorithm. Make sure to use one of the supported algorithms mentioned in the list above.

## Disclaimer
This script provides a basic password hashing utility and is intended for educational purposes only. In real-world applications, consider using a password hashing library with additional security features, such as salting and multiple iterations (e.g., bcrypt, Argon2).

Always follow security best practices to protect user passwords and sensitive data.
