""" test_user.py """

import unittest

from user import User


class  Testing_users(unittest.TestCase):


    """ setUp initialisation method """

    def setUp(self):
        self.n_user = User()  


    def testing_registration(self):

        """ testing for complete fields """

        self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        result = self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        self.assertEqual("Account created successfully", result)

    def testing_empty_username(self):

        """ Testing for  empty  username """

        result = self.n_user.user_registration("", "lennykmutua@gmail.com", "secret", "secret")
        self.assertEqual("Please fill in all fields correctly", result)

    def testing_empty_email(self):

        """ Testing for empty email  field """

        result = self.n_user.user_registration("Lenny", "", "secret", "secret")
        self.assertEqual("Please fill in all fields correctly", result)

    def testing_empty_password(self):

        """Testing for empty password  field """

        result = self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "", "secret")
        self.assertEqual("Please fill in all fields correctly", result)

    def testing_empty_cpassword(self):

        """Testing for empty confirm password  field """

        result = self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "")
        self.assertEqual("Please fill in all fields correctly", result)


    def test_successful_login(self):

        """ Testing  a successful login"""

        self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        valid_login = self.n_user.user_login("lennykmutua@gmail.com", "secret")
        self.assertEqual("Invalid credentials", valid_login)


    def test_no_password(self):

        """ Testing login when password field is empty"""

        no_password = self.n_user.user_login("lennykmutua@gmail.com", "")
        self.assertEqual("Kindly fill in both fields correctly", no_password)



    def test_no_email(self):

        """ Testing login when  email field is empty"""

        no_email = self.n_user.user_login("", "secret")
        self.assertEqual("Kindly fill in both fields correctly", no_email)

    def test_password_match(self):

        """ Test login with different password."""

        self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        wrong_password = self.n_user.user_login("lennykmutua@gmail.com", "public")
        self.assertEqual("Invalid credentials", wrong_password)



    def test_email_match(self):

        """ Test login with different email."""

        self.n_user.user_registration("Lenny", "lennykmutua@gmail.com", "secret", "secret")
        wrong_email = self.n_user.user_login("okiokii@gmail.com", "secret")
        self.assertEqual("Invalid credentials", wrong_email)


if __name__ == '__main__':

    unittest.main()
