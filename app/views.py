""" views.py """

from user import User
from recipe import Recipe

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import g

from app import app

app = Flask(__name__)

user = User()

recipe = Recipe()

@app.route("/", methods=["GET", "POST"])

def index():

    return render_template("index.html")

def register():

    """ Handles registration process"""

    if request.method == "POST":

        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        cpassword = request.form['confirmPassword']

        register_value = user.user_registration(username, email, password, cpassword)

        if register_value == "Account created successfully":
            session['username'] = username
            msg_flag = "Registration was successful."
            return render_template('dashboard.html', message=msg_flag)



        elif register_value ==  "Please fill in all fields correctly":
            msg_flag = "Please fill in all the fields"
            return render_template("index.html", message=msg_flag)


def login():

    """Handles the login process"""

    if request.method == "POST":

        email = request.form['emailAddress']
        password = request.form['password']

        login_value = user.user_login(email, password)

        if login_value == "Successful log in":
            username = user.get_username(email)
            session['username'] = username
            return render_template("dashboard.html")



        elif login_value == "Invalid credentials":
            msg_flag = "Wrong credentials given."
            return render_template("index.html", message=msg_flag)


        elif login_value == "Kindly fill in both fields correctly":
            msg_flag = "Please fill all fields"
            return render_template("index.html", message=msg_flag)

        else:
            msg_flag = "An Error occured, Please try again."
            return render_template("index.html", message=msg_flag)

    return render_template("index.html")


@app.route("/recipe", methods=["GET", "POST"])

def create_recipe():

    """Handles creation of a recipe"""

    if g.user:

        if request.method == "POST":

            recipe_category = request.form["InputRecipeCategory"]
            recipe_title = request.form["InputRecipeTitle"]
            recipe_description = request.form["InputRecipeDescription"]

            create_recipe = recipe.create_recipe(recipe_category, recipe_title, recipe_description)


            if create_recipe == "Recipe added successfully":
                msg_flag = "Recipe added successfully"
                return render_template("dashboard.html", message = msg_flag)



            elif create_recipe ==  "Kindly fill in all fields correctly":
                msg_flag = "Kindly fill in all fields correctly"
                return render_template("dashboard.html", message = msg_flag)

            else:
                msg_flag = "Error occured, try again later."
                return render_template("dashboard.html", message = msg_flag)



        return render_template("dashboard.html")

    return render_template("index.html")



if __name__ == "__main__":

    app.run(debug=True)
