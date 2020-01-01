
from flask import Blueprint


def my_register_blueprint(app):
    from app.controler.user import user_service, authentication
    app.register_blueprint(user_service, url_prefix="/api/users")
    app.register_blueprint(authentication, url_prefix="/api")
    return app
