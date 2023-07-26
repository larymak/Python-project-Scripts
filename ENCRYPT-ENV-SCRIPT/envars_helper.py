import os
import base64
import secrets

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import cryptography


class EncryptionHelper:
    """
    A class to represent Encryption.

    Methods
    -------
    load_salt(self, filename):
        A method to read and return a generated salt saved in file.
    derive_key(self, salt, password):
        A method to derive key.
    generate_key(self, password, filename, load_existing_salt=False, save_salt=False):
        A method to generate key.
    encrypt(self, filename, key):
        A method to encrypt file.
    decrypt(self, filename, key):
        A method to decrypt file.
    """

    @staticmethod
    def generate_salt(size: int):
        """ 
        A method to generate a salt.

        Parameters
        ----------
        size : int
            The size of the bytes strings to be generated.

        Returns
        -------
        bytes
            The method returns bytes strings containing the secret token.
        """
       
        return secrets.token_bytes(size)

    @staticmethod
    def load_salt(filename: str):
        """ 
        A method to read and return a save salt file.

        Parameters
        ----------
        filename : str
            The file name to read from.

        Returns
        -------
        bytes
            The method returns bytes containing the salt.
        """

        # load salt from salt file
        return open(filename.replace(".envs", ".salt"), "rb").read()

    @staticmethod
    def derive_key(salt: bytes, password: str):
        """ 
        A method to derive a key using password and salt token.

        Parameters
        ----------
        salt : bytes
            The bytes strings containing the salt token.
        password : str
            The strings of characters containing the password.

        Returns
        -------
        bytes
            The method returns bytes string containing the derived key.
        """

        # derive key using salt and password
        key = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
        return key.derive(password.encode())
    
    @staticmethod
    def generate_key(password: str, filename: str, load_existing_salt=False, save_salt=False):
        """ 
        A method to generate key.

        Parameters
        ----------
        password : str
            The strings of characters containing the password.
        filename : str
            The strings of characters containing file name.
        load_existing_salt : bool, optional
            A boolean value determining existing  salt exists.
        save_salt : bool, optional
            A boolean value determining save salt exists.

        Returns
        -------
        bytes
            The method returns bytes string containing the generated key.
        """
        
        # check existing salt file
        if load_existing_salt:
            try:
                with open(filename.replace(".envs", ".salt"), "rb") as salt_file:
                    salt_file.readline()
            except FileNotFoundError: 
                return base64.urlsafe_b64encode(os.urandom(32))
            # load existing salt
            salt = EncryptionHelper.load_salt(filename)
        if save_salt:
            # generate new salt/token and save it to file
            salt = EncryptionHelper.generate_salt(16)
            with open(f"{filename}.salt", "wb") as salt_file:
                salt_file.write(salt)

        # generate the key from the salt and the password
        derived_key = EncryptionHelper.derive_key(salt, password)
        # encode it using Base 64 and return it
        return base64.urlsafe_b64encode(derived_key)

    @staticmethod
    def encrypt(filename: str, key: bytes):
        """ 
        A method to encrypt file.

        Parameters
        ----------
        filename : str
            The strings of characters containing file name.
        key : bytes
            A bytes of stings containing the encryption key.
        
        Returns
        -------
        None
            The method returns a none value.
        """

        fernet = Fernet(key)

        try:
            with open(filename, "rb") as file:
                file_data = file.read()
        except FileNotFoundError:
            print("File not found")
            return
        
        # encrypting file_data
        encrypted_data = fernet.encrypt(file_data)

        # writing to a new file with the encrypted data
        with open(f"{filename}.envs", "wb") as file:
            file.write(encrypted_data)

        print("File encrypted successfully...")
        return "File encrypted successfully..."

    @staticmethod
    def decrypt(filename: str, key: bytes):
        """ 
        A method to decrypt file.

        Parameters
        ----------
        filename : str
            The strings of characters containing file name.
        key : bytes
            A bytes of stings containing the encryption key.
        
        Returns
        -------
        None
            The method returns a none value.
        """

        fernet = Fernet(key)
        try:
            with open(filename, "rb") as file:
                encrypted_data = file.read()
        except FileNotFoundError:
            print("File not found.")
            return
        # decrypt data using the Fernet object
        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except cryptography.fernet.InvalidToken:
            print("Invalid token, likely the password is incorrect.")
            return
        # write the original file with decrypted content
        with open(filename.replace(".envs", ""), "wb") as file:
            file.write(decrypted_data)
        # delete salt file after decrypting file
        f = open(filename.replace(".envs", ".salt"), 'w')
        f.close()
        os.remove(f.name)
        # delete decrypted file
        os.remove(filename)
        print("File decrypted successfully...")

        return "File decrypted successfully..."
