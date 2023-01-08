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