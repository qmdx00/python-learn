from flask import Flask

from python_flask.blueprint_example import *

"""
project start
"""
app = Flask(__name__)
app.register_blueprint(hello_route, url_prefix='/hello')
app.register_blueprint(index_route, url_prefix='/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
