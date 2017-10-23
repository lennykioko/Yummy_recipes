""" recipe.py """


class Recipe(object):


    """ Recipe class to handle  creating a new recipe """


    recipes = {}   # initialised an empty dictionary names recipes

    def __init__(self, recipe_category=0, recipe_title=0, recipe_description=0):

        """ Initializing  class instance variables """

        self.recipe_category = recipe_category
        self.recipe_title = recipe_title
        self.recipe_description = recipe_description

    def create_recipe(self, recipe_category, recipe_title, recipe_description):

        """ Method to create a new recipe """

        if len(recipe_category) > 1 and len(recipe_title) > 1 and len(recipe_description) > 1:

            return "Recipe added successfully"

            recipes[recipe_title] = {'category': recipe_category,
                                     'title': recipe_title,
                                     'description' : recipe_description}
        else:
            return "Kindly fill in all fields correctly"
