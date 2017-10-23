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
        self.assertEqual("Recipe added successfully", result)



    def test_empty_category(self):

        """ Test for  empty  recipe category field """

        result = self.recipe.create_recipe("", "Soft Chapati", "Prepare dough. Fry in hot pan")
        self.assertEqual("Kindly fill in all fields correctly", result)



    def test_empty_title(self):

        """ Test for empty recipe title  field """

        result = self.recipe.create_recipe("Lunch", "", "Prepare dough. Fry in hot pan")
        self.assertEqual("Kindly fill in all fields correctly", result)



    def test_empty_description(self):

        """ Test for empty recipe description field """

        result = self.recipe.create_recipe("Lunch", "Soft Chapati", "")
        self.assertEqual("Kindly fill in all fields correctly", result)

if __name__ == '__main__':

    unittest.main()
