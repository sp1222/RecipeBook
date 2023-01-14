'''
Recipe Book Ingredients Data Model
This represents the model/data access layer.
Handles CRUD operations on the data.
'''

from src.classes.Ingredient import Ingredient
import json
import os


def getIngredientNameToIdMap():
    '''
    Load ingredient names from data.
    '''
    nameToIdMap = dict()
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        for key, obj in data.items():
            nameToIdMap.update({obj['name']: key})
    return nameToIdMap


def getIngredient(id):
    '''
    Load ingredient object from data.
    '''
    # TODO: add error handling.
    ingredient = None
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        ingredient = Ingredient(id, data[id]['name'], data[id]['description'], data[id]['tags'])
    return ingredient


def updateIngredient(id, name, description, tags):
    '''
    Update ingredient data given user input
    '''
    ingredients = None
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        ingredients = json.load(f)
    # TODO: add error handling.
    if id in ingredients:
        ingredients[id]['name'] = name
        ingredients[id]['description'] = description
        # TODO: add tags to page.
        # ingredients[id]['tags'] = tags
        with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='w') as f:
            json.dump(ingredients, f, indent=4)
    else:
        print('something went terribly wrong, id ' + str(id) + ' is not an existing ingredient id O_o')
