""" test_user.py """

import unittest

from user import User


class  UserTest(unittest.TestCase):


    """ This tests the initialisation """

    def setUp(self):
        self.user = User()  

    def test_user_registration(self):

        """ This tests for complete fields """

        result = self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret")
        self.assertEqual(1, result, "User registration successful")

    def test_empty_username_field(self):

        """ Test for  empty  username field """

        result = self.user.user_registration("", "lennykmutua@gmail.com", "secret")
        self.assertEqual(2, result, "Please fill in the username field")

    def test_empty_email_field(self):

        """ Test for empty email  field """

        result = self.user.user_registration("Lenny", "", "secret")
        self.assertEqual(2, result, "Please fill in the email field")

    def test_empty_password_field(self):

        """Test for empty password  field """

        result = self.user.user_registration("Lenny", "lennykmutua@gmail.com", "")
        self.assertEqual(2, result, "Please fill in the password field")


if __name__ == '__main__':

    unittest.main()
