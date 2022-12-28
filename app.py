'''
My Personal Website
'''

from flask import Flask
from src.blueprints.rb_home_blueprint import rb_home_blueprint

app = Flask(__name__)
app.register_blueprint(rb_home_blueprint)

if __name__ == '__main__':
    print('booting up Recipe Book')
    app.run(debug=True, host='0.0.0.0', port=5000)
