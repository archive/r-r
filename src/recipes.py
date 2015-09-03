# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request
from models import Recipe
import logging
from recipesrepository import RecipesRepository

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='...',
    PROPAGATE_EXCEPTIONS=True
)

dbRecipes = [];
dbRecipes.append(Recipe(1, 'Tomorrow and next week', 'Lipsum...'))
dbRecipes.append(Recipe(2, '7 Thinking Hats', 'Lipsum...'))
dbRecipes.append(Recipe(3, 'Speed boat', 'Lipsum...'))
dbRecipes.append(Recipe(4, 'Learning Matrix', 'Lipsum...'))
dbRecipes.append(Recipe(5, 'Good and throw away', 'Lipsum...'))

#app.logger.info(list(filter(lambda x: x.id == 1, dbRecipes)))
#app.logger.info([recipe for recipe in dbRecipes if recipe.id == 1])

@app.route('/recipe/<id>')
def recipe(id):
    recipe = [recipe for recipe in dbRecipes if recipe.id == 1]
    return jsonify({'result': recipe[0].__dict__})

@app.route('/recipes')
def recipes():
    repository = RecipesRepository()
    recipes = repository.all()
    return jsonify({'result': [recipe.__dict__ for recipe in recipes]})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
