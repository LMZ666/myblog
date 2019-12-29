from app.controler import my_register_blueprint

from flask import Flask


def create_app():
    app = Flask(__name__)
    app = my_register_blueprint(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
