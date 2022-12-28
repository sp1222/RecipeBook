'''
Recipe Book Ingredients blueprint
'''

from flask import Blueprint, render_template

ingredients_blueprint = Blueprint('ingredients', __name__, template_folder='../../../templates/ingredients/')


@ingredients_blueprint.route('/ingredients')
def ingredients():
    '''
    Recipe Book Ingredients Page endpoint
    :return:
    '''
    return render_template('ingredients.html')


@ingredients_blueprint.route('/ingredients/add')
def addingredient():
    '''
    Recipe Book Ingredients Page endpoint to add ingredients
    :return:
    '''
    return render_template('add_ingredients.html')
