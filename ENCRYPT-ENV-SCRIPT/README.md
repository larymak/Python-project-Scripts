# ENCRYPTING ENVIRONMENT VARIABLE FILE SCRIPT

## A commandline software script to encrypt or decrypt an env file, specifically to share secret encrypted environment variables using a password via git
The encryption uses the cryptography library using symmetric encryption, which means the same key used to encrypt data, is also usable for decryption.


**To run the software:**
```
pip3 install -r requirements.txt
python3 envvars_script.py --help
```

**Output:**
```
usage: ennvars_script.py [-h] (-e | -d) file

File Encryption Script with a Password.

positional arguments:
  file           File to encrypt/decrypt.

optional arguments:
  -h, --help     show this help message and exit
  -e, --encrypt  To encrypt the file, only -e or --encrypt can be specified.
  -d, --decrypt  To decrypt the file, only -d or --decrypt can be specified.
```

### Encrypt a file
* Encrypting a file for example ".env". Create the file in the project root directory and save it with the env content. Run the following example command:
    ```
     python3 envvars_script.py <.env> --encrypt
     OR
     python3 envvars_script.py <.env> -e
    ```
    * replace <.env> with the right filename.
* Enter password to encrypt file. Note: password must be atleast 8 characters

* Check file content has been encrypted with the following files created:
```
      .env.envs
      .env.salt

```

### Decrypt file
* To decrypt file, (use same password used in encryting the file otherwise decrypting won't work). Run the following example command:
    ```
    python3 envvars_script.py <.env.envs> --decrypt
    OR
    python3 envvars_script.py <.env.envs> -d
    ```
    * replace <.env.envs> with the right filename.
* Enter password to decrypt file. This must be the same password used in encrypting the file.

* Check file has been decrypted and updated with the original content(before encryption) if .env existed otherwise new .env file created with content.

**To run unit test:**
```
 python3 test_script.py
```
