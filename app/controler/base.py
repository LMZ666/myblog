from flask import Blueprint

def gen_blueprint(name, import_name):
    return Blueprint(name=name, import_name=import_name)