from fileinput import filename
import os
import unittest

from envars_helper import EncryptionHelper


class TestEnvvarsEncryption(unittest.TestCase):

    def setUp(self):
        self.password = "mypassword.com"
        self.filename = ".env"
        self.filename_to_be_decrypted = ".env.envs"
        self.envvars_encryption = EncryptionHelper()

    def tearDown(self):
        #delete test salt file from file
        file_data = open(f"{self.filename}.salt", 'w')
        file_data.close()
        os.remove(file_data.name)

        #delete test encrypted file from file
        file_data = open(f"{self.filename}.envs", 'w')
        file_data.close()
        os.remove(file_data.name)
        
        
    
    def test_is_instance(self):
        """Test class instance. """

        self.assertTrue(isinstance(self.envvars_encryption, EncryptionHelper))

    def test_generate_key_method(self):
        """Test generate key is instance method. """
        self.assertTrue(self.envvars_encryption.generate_key)

    def test_encrypt_method(self):
        """Test encrypt is instance method. """

        self.assertTrue(self.envvars_encryption.encrypt)

    def test_decrypt_method(self):
        """Test decrypt is instance method. """

        self.assertTrue(self.envvars_encryption.decrypt)

    def test_generate_key(self):
        """Test generate key method. """

        gen_key = self.envvars_encryption.generate_key(self.password, self.filename, save_salt=True)
        
        self.assertEqual(type(gen_key), bytes)


    def test_encrypt(self):
        """Test encrypt method. """

        key = self.envvars_encryption.generate_key(self.password, self.filename, save_salt=True)
        encrypted = self.envvars_encryption.encrypt(self.filename, key)
        self.assertEqual(encrypted, "File encrypted successfully...")

    def test_decrypt_file_doesnot_exist(self):
        """Test decryp file does not exist """

        key = self.envvars_encryption.generate_key(self.password, self.filename, save_salt=True)
        self.envvars_encryption.encrypt(self.filename, key)
        self.envvars_encryption.decrypt("wrong.notenvs", key)
        self.assertRaises(SystemExit)
        
    def test_decrypt(self):
        """Test decrypt method. """

        key = self.envvars_encryption.generate_key(self.password, self.filename, save_salt=True)
        self.envvars_encryption.encrypt(self.filename, key)
        decrypted = self.envvars_encryption.decrypt(self.filename_to_be_decrypted, key)
        self.assertEqual(decrypted, "File decrypted successfully...")


if __name__ == '__main__':
    unittest.main()
