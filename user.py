""" user.py """

users = {}  # initialised an empty  dictionary named users


class User(object):


    """ User class to handle  user functions like login and sign up """

    def __init__(self, username=0, email=0, password=0, cpassword=0):

        """ Initializing  class instance variables """
        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword

    def user_registration(self, username, email, password, cpassword):

        """ Method to register new users """
        if len(username) > 1 and len(email) > 1 and len(password) > 1 and len(cpassword) > 1:  
            password = password.strip()
            cpassword = cpassword.strip()

            if email not in users.keys():
                return "Account created successfully"
                users[email] = {'username': username, 'email': email, 'password' : password}
                
        else:
            return "Please fill in all fields correctly"

    def user_login(self, email, password):

        """ Method to login users """
        if len(email) > 1 and len(password) > 1:

            if email in users.keys():

                result = users[email]
                passwd = result['password']

                if passwd == password:
                    return "Successful log in"

            else:
                return "Invalid credentials" 
        else:
            return "Kindly fill in both fields correctly"
            
            
    def get_username(self, email):

        """ Get username from the dictionary"""

        if email in users.keys():

            user_username = users[email]
            return user_username['username']

        return False
