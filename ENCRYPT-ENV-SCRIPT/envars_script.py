import sys
import getpass

from envars_helper import EncryptionHelper

if __name__ == "__main__":
    import argparse

    encryption_helper = EncryptionHelper()

    parser = argparse.ArgumentParser(description="File Encryption Script with a Password.",
                                     allow_abbrev=False)
    parser.add_argument("file", help="File to encrypt/decrypt.")
    group_args = parser.add_mutually_exclusive_group(required=True)
    group_args.add_argument("-e", "--encrypt", action="store_true",
                            help="To encrypt the file, only -e or --encrypt can be specified.")
    group_args.add_argument("-d", "--decrypt", action="store_true",
                            help="To decrypt the file, only -d or --decrypt can be specified.")

    args = parser.parse_args()
    filename = args.file
    encrypt_arg = args.encrypt
    decrypt_arg = args.decrypt

    try:
        with open(filename, "r") as f:
            file_data = f.readline()
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
    
    password = None
    if encrypt_arg:
        ext = filename.split(".").pop()
        if ext == "envs":
            print("File already encrypted.")
            sys.exit(1)
        password = getpass.getpass("Enter the password for encryption: ")
        while len(password) < 8:
            print("Password must be 8 characters or above. \n")
            password = getpass.getpass("Enter the password for encryption: ")    
    elif decrypt_arg:
        ext = filename.split(".").pop()
        if ext != "envs":
            print("File was not encrypted. Encrypted file has a .envs extension")
            sys.exit(1)
        password = getpass.getpass("Enter the password used for encryption: ")

    if encrypt_arg:
        key = encryption_helper.generate_key(password, filename, save_salt=True)
        encryption_helper.encrypt(filename, key)
    else:
        key = encryption_helper.generate_key(password, filename, load_existing_salt=True)
        encryption_helper.decrypt(filename, key)
