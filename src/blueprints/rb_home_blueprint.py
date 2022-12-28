'''
Recipe Book Homepage blueprint
'''

from flask import Blueprint, render_template

rb_home_blueprint = Blueprint('rb_home', __name__, template_folder='../../templates/')


@rb_home_blueprint.route('/')
def home():
    '''
    Recipe Book Home Page endpoint
    :return:
    '''
    return render_template('home.html')
