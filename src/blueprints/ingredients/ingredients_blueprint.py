'''
Recipe Book Ingredients blueprint
'''

from flask import Blueprint, render_template
import json
import os

ingredients_blueprint = Blueprint('ingredients', __name__, template_folder='../../../templates/ingredients/')


def getIngredientNameToIdMap():
    '''
    Load ingredient names from data to display on the page.
    '''
    nameToIdMap = dict()

    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        for key, obj in data.items():
            nameToIdMap.update({obj['name']: key})
    return nameToIdMap


@ingredients_blueprint.route('/ingredients')
def ingredients():
    '''
    Recipe Book Ingredients Page endpoint
    :return:
    '''
    nameToIdMap = getIngredientNameToIdMap()
    return render_template('ingredients.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/add')
def addIngredient():
    '''
    Recipe Book Ingredients Page endpoint to add ingredients
    :return:
    '''
    nameToIdMap = getIngredientNameToIdMap()
    return render_template('add_ingredient.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/edit')
def editIngredient():
    '''
    Recipe Book Ingredients Page endpoint to edit ingredients
    :return:
    '''
    nameToIdMap = getIngredientNameToIdMap()
    return render_template('edit_ingredient.html', nameToIdMap=nameToIdMap)


@ingredients_blueprint.route('/ingredients/edit/')


@ingredients_blueprint.route('/ingredients/delete')
def deleteIngredient():
    '''
    Recipe Book Ingredients Page endpoint to delete ingredients
    :return:
    '''
    nameToIdMap = getIngredientNameToIdMap()
    return render_template('delete_ingredient.html', nameToIdMap=nameToIdMap)
