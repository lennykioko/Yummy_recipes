""" test_user.py """

import unittest

from user import User


class  UserTest(unittest.TestCase):


    """ This tests the initialisation """

    def setUp(self):
        self.user = User()  

    def test_user_registration(self):

        """ This tests for complete fields """
        self.user.users = {}
        self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        result = self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        self.assertEqual("Account created successfully", result, "User registration successful")

    def test_empty_username_field(self):

        """ Test for  empty  username field """

        result = self.user.user_registration("", "lennykmutua@gmail.com", "secret", "secret")
        self.assertEqual("Please fill in all fields correctly", result,
                         "Please fill in the username field")

    def test_empty_email_field(self):

        """ Test for empty email  field """

        result = self.user.user_registration("Lenny", "", "secret", "secret")
        self.assertEqual("Please fill in all fields correctly", result,
                         "Please fill in the email field")

    def test_empty_password_field(self):

        """Test for empty password  field """

        result = self.user.user_registration("Lenny", "lennykmutua@gmail.com", "", "secret")
        self.assertEqual("Please fill in all fields correctly", result,
                         "Please fill in the password field")

    def test_empty_cpassword_field(self):

        """Test for empty confirm password  field """

        result = self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "")
        self.assertEqual("Please fill in all fields correctly", result,
                         "Please fill in the password field")

    def test_successful_login(self):

        """ Test the required inputs for a successful login"""

        self.user.users = {}
        self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        valid_login = self.user.user_login("lennykmutua@gmail.com", "secret")
        self.assertEqual("Invalid credentials", valid_login, "Log in successful.")


    def test_login_emptypassword(self):

        """ Test login when password field is empty"""

        emptypassword = self.user.user_login("lennykmutua@gmail.com", "")
        self.assertEqual("Kindly fill in both fields correctly", emptypassword,
                         "Kindly fill in password field.")



    def test_login_emptyemail(self):

        """ Test login when  email field is empty"""

        emptyemail = self.user.user_login("", "secret")
        self.assertEqual("Kindly fill in both fields correctly", emptyemail,
                         "Kindly fill in email field.")

    def test_login_match_password(self):

        """ Test login when the password differs with the one in the dictionary."""

        self.user.users = {}

        self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        wrongpassword = self.user.user_login("lennykmutua@gmail.com", "public")
        self.assertEqual("Invalid credentials", wrongpassword, "Incorrect password given.")



    def test_login_match_email(self):

        """ Test login when the email differs with the one in the dictionary."""

        self.user.users = {}
        self.user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        wrongemail = self.user.user_login("okiokii@gmail.com", "secret")
        self.assertEqual("Invalid credentials", wrongemail, "Incorrect email given.")


if __name__ == '__main__':

    unittest.main()
