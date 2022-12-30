'''
Recipe Book Recipes blueprint
'''

from flask import Blueprint, render_template
import json
import os

recipes_blueprint = Blueprint('recipes', __name__, template_folder='../../../templates/recipes/')


def getRecipeNameToIdMap():
    '''
    Load ingredient names from data to display on the page.
    '''
    nameToIdMap = dict()

    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        for key, obj in data.items():
            nameToIdMap.update({obj['name']: key})
    return nameToIdMap


@recipes_blueprint.route('/recipes')
def recipes():
    '''
    Recipe Book Recipes Page endpoint
    :return:
    '''
    nameToIdMap = getRecipeNameToIdMap()
    return render_template('recipes.html', nameToIdMap=nameToIdMap)


@recipes_blueprint.route('/recipes/add')
def addRecipe():
    '''
    Recipe Book Recipes Page endpoint to add recipes
    :return:
    '''
    nameToIdMap = getRecipeNameToIdMap()
    return render_template('add_recipe.html', nameToIdMap=nameToIdMap)


@recipes_blueprint.route('/recipes/edit')
def editRecipe():
    '''
    Recipe Book Recipes Page endpoint to edit recipes
    :return:
    '''
    nameToIdMap = getRecipeNameToIdMap()
    return render_template('edit_recipe.html', nameToIdMap=nameToIdMap)


@recipes_blueprint.route('/recipes/delete')
def deleteRecipe():
    '''
    Recipe Book Recipes Page endpoint to delete recipes
    :return:
    '''
    nameToIdMap = getRecipeNameToIdMap()
    return render_template('delete_recipe.html', nameToIdMap=nameToIdMap)
