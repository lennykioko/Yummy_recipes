""" recipe.py """


class Recipe(object):


    """ Recipe class to handle  creating a new recipe """


    recipes = {}   # initialised an empty dictionary names recipes

    def __init__(self, recipe_category=None, recipe_title=None, recipe_description=None):

        """ Initializing  class instance variables """

        self.recipe_category = recipe_category
        self.recipe_title = recipe_title
        self.recipe_description = recipe_description

    def create_recipe(self, recipe_category, recipe_title, recipe_description):

        """ Method to create a new recipe """

        if recipe_category != '' and recipe_title != '' and recipe_description != '':

            return "Recipe added successfully"

            recipes[recipe_title] = {'category': recipe_category,
                                     'title': recipe_title,
                                     'description' : recipe_description}
