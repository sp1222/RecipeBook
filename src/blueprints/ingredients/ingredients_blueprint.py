'''
Recipe Book Ingredients Blueprint
Handles rendering pages given a route.
'''

from flask import Blueprint, render_template
import src.dao.Ingredient as ingredient

ingredients_blueprint = Blueprint('ingredients', __name__, template_folder='../../../templates/ingredients/')


@ingredients_blueprint.route('/ingredients')
def ingredients():
    '''
    Recipe Book Ingredients Page endpoint
    :return:
    '''
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    return render_template('ingredients.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/add')
def addIngredient():
    '''
    Recipe Book Ingredients Page endpoint to add ingredients
    :return:
    '''
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    return render_template('add_ingredient.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/edit/id=<id>')
def editIngredient(id):
    '''
    Recipe Book Ingredients page endpoint to edit a selected ingredient
    '''
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    ingredientObj = ingredient.getIngredient(id)
    return render_template('edit_ingredient.html', nameToIdMap=nameToIdMap, ingredientObj=ingredientObj)


@ingredients_blueprint.route('/ingredients/delete')
def deleteIngredient():
    '''
    Recipe Book Ingredients Page endpoint to delete ingredients
    :return:
    '''
    nameToIdMap = ingredient.getIngredientNameToIdMap()
    return render_template('delete_ingredient.html', nameToIdMap=nameToIdMap)
