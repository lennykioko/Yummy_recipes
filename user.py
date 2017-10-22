""" user.py """

users = {}  # initialised an empty  dictionary named users


class User(object):


    """ User class to handle  user functions like login and sign up """

    def __init__(self, username=None, email=None, password=None, cpassword=None):

        """ Initializing  class instance variables """

        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword

    def user_registration(self, username, email, password, cpassword):

        """ Method to register new users """

        password = password.strip()
        cpassword = cpassword.strip()

        if username != '' and email != '' and password != '' and password == cpassword:

            if email not in users.keys():

                return "Account created successfully"

                users[email] = {'username': username, 'email': email, 'password' : password}

            return "Please fill in all fields correctly"
                



    def user_login(self, email, password):

        """ Method to login users """

        if email != '' and password != '':

            if email in users.keys():

                result = users[email]
                passwd = result['password']

                if passwd == password:

                    return "Successful log in"

                return "Invalid email" 

            return "Kindly fill in both fields correctly"
            