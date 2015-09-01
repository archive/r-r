# -*- coding: utf-8 -*-

# ändra till https://pythonhosted.org/behave/ ?

import os
import recipes
import unittest
import tempfile

import logging

class RecipesTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, recipes.app.config['DATABASE'] = tempfile.mkstemp()
        self.app = recipes.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(recipes.app.config['DATABASE'])

    def test_recipe(self):
        result = self.app.get('/recipe/1') #result.data
        self.assertEqual(result._status_code, 200)
        assert 200 is result._status_code

if __name__ == '__main__':
    unittest.main()
