'''
Recipe Book Ingredients Data Model
This represents the model/data access layer.
Handles CRUD operations on the data.
'''

from collections import OrderedDict
from src.classes.Ingredient import Ingredient
import json
import os


def getAvailableId():
    '''
    Gets the next available Id for a new ingredient
    '''
    ids = None
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        ids = data.keys()
    currentId = 1
    while True:
        if str(currentId) not in ids:
            break
        currentId += 1
    return currentId


def getIngredientNameToIdMap():
    '''
    Load ingredient names from data.
    '''
    nameToIdMap = dict()
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        data = json.load(f)
        for key, obj in data.items():
            nameToIdMap.update({obj['name']: key})
    nameToIdMap = OrderedDict(sorted(nameToIdMap.items()))
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


def updateIngredientList(ingredient):
    '''
    Update ingredient data given user input
    '''
    ingredients = None
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='r') as f:
        ingredients = json.load(f)
    # TODO: add error handling.
    ingredientToList = dict()
    ingredient.name = ingredient.name[0].upper() + ingredient.name[1:]
    ingredientToList.update({'name':ingredient.name})
    ingredientToList.update({'description':ingredient.description})
    ingredientToList.update({'tags':ingredient.tags})
    ingredients[ingredient.id] = ingredientToList
    with open(os.getcwd() + '/data/testIngredientFile.json', encoding='utf-8', mode='w') as f:
        json.dump(ingredients, f, indent=4)