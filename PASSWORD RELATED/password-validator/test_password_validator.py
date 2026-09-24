import unittest
from unittest.mock import patch


class TestPasswordValidator(unittest.TestCase):

    def test_password_must_contain_uppercase(self):
        with patch("builtins.input", return_value="abcdef1!"):
            from PASSWORD_VALIDATOR import passwordValidator
            result = passwordValidator()

        self.assertIn("Invalid Password", result)


if __name__ == "__main__":
    unittest.main()