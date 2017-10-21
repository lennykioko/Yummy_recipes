""" user.py """


class User(object):


    """ User class to handle  user functions like login and sign up """

    users = {}  # initialised an empty  dictionary named users

    def __init__(self, username=None, email=None, password=None):

        """ Initializing  class instance variables """

        self.username = username
        self.email = email
        self.password = password

    def user_registration(self, username, email, password):

        """ Method to register new users """

        if username != '' and email != '' and password != '':

            return 1

            users = {'username': username, 'email': email, 'password' : password}


    def user_login(self, email, password):

        """ Method to login users """

        if email != '' and password != '':

            if email in users.values() and password in users.values():

                eml = users['email']
                passwd = users['password']

                if eml == email and passwd == password:

                    return 1
            return 2
        return 3
        