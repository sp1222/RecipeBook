'''
My Personal Website
'''

from flask import Flask
from src.blueprints.home_blueprint import home_blueprint
from src.blueprints.ingredients.ingredients_blueprint import ingredients_blueprint
from src.blueprints.recipes.recipes_blueprint import recipes_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)
app.register_blueprint(ingredients_blueprint)
app.register_blueprint(recipes_blueprint)

if __name__ == '__main__':
    print('booting up Recipe Book')
    app.run(debug=True, host='0.0.0.0', port=5000)
