from pymongo import MongoClient

class RecipesRepository():
    def __init__(self):
        self.test = 'asd'

    def all(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.rr
        print(db.recipes.count())
        recipes = list(db.recipes.find()) # change to use async callback
        return recipes
