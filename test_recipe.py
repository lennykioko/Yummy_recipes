""" test_recipe.py """

import unittest

from recipe import Recipe


class  RecipeTest(unittest.TestCase):


    """ This tests the initialisation """

    def setUp(self):
        self.recipe = Recipe()    


    def test_create_recipe(self):

        """ This tests for complete fields """

        result = self.recipe.create_recipe("Lunch", "Soft Chapati", "Prepare dough. Fry in hot pan")
        self.assertEqual("Recipe added successfully", result,
                         "New recipe created successfully ")



    def test_empty_category_field(self):

        """ Test for  empty  recipe category field """

        result = self.recipe.create_recipe("", "Soft Chapati", "Prepare dough. Fry in hot pan")
        self.assertEqual("Recipe added successfully", result,
                         "Please fill in the recipe category field")



    def test_empty_title_field(self):

        """ Test for empty recipe title  field """

        result = self.recipe.create_recipe("Lunch", "", "Prepare dough. Fry in hot pan")
        self.assertEqual("Recipe added successfully", result,
                         "Please fill in the recipe title field")



    def test_empty_description_field(self):

        """ Test for empty recipe description field """

        result = self.recipe.create_recipe("Lunch", "Soft Chapati", "")
        self.assertEqual("Recipe added successfully", result,
                         "Please fill in the recipe description field")


if __name__ == '__main__':

    unittest.main()
