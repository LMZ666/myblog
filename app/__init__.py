from app.controler import my_register_blueprint
from config import app_config
from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object(app_config)
    # print(app_config.DEBUG)
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.config['prot'] = 8000
    app = my_register_blueprint(app)
    return app
