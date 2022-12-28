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
