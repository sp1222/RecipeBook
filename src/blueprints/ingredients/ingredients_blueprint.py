'''
Recipe Book Ingredients Blueprint
Handles rendering pages given a route.
'''

from flask import Blueprint, render_template, request
from src.classes.Ingredient import Ingredient
import src.dao.IngredientDao as ingredient

ingredients_blueprint = Blueprint('ingredients', __name__, template_folder='../../../templates/ingredients/')


@ingredients_blueprint.route('/ingredients')
def ingredients():
    '''
    Recipe Book Ingredients Page endpoint.
    :return:
    '''
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    return render_template('ingredients.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/add', methods=['POST', 'GET'])
def addIngredient():
    '''
    Recipe Book Ingredients Page endpoint to add ingredients.
    :return:
    '''
    if request.method == 'POST' and request.form['button'] == 'Add Ingredient':
        id = ingredient.getAvailableId()
        # TODO: input validation, name should be a required field, handle error if empty
        if request.form['name']:
            name = request.form['name'][0].upper() + request.form['name'][1:]
            description = request.form['description']
            tags = list()
            newIngredient = Ingredient(id, name, description, tags)
            ingredient.updateIngredientList(newIngredient)
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    return render_template('add_ingredient.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/edit/id=<id>', methods=['POST', 'GET'])
def editIngredient(id):
    '''
    Recipe Book Ingredients page endpoint to edit a selected ingredient.
    '''
    if request.method == 'POST':
        if request.form['button'] == 'Edit Ingredient':
            name = request.form['name']
            description = request.form['description']
            tags = list()
            updatedIngredient = Ingredient(id, name, description, tags)
            ingredient.updateIngredientList(updatedIngredient)
        elif request.form['button'] == 'Delete Ingredient':
            if not ingredient.isIngredientInARecipe(id):
                ingredient.deleteIngredient(id)
            else:
                print('display error message stating the ingredient is in use in a recipe and cannot be deleted.')
                print('maybe list the recipes the ingredient is in?')
            nameToIdMap = ingredient.getIngredientNameToIdMap()
            return render_template('ingredients.html', nameToIdMap=nameToIdMap)
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    ingredientObj = ingredient.getIngredient(id)
    return render_template('edit_ingredient.html', nameToIdMap=nameToIdMap, ingredientObj=ingredientObj)
