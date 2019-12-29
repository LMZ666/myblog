from .base import gen_blueprint, Blueprint
from app.lib.response import response
import json
from flask import request

user_service = gen_blueprint("user", __name__)
authentication = Blueprint("login", __name__)

@user_service.route("abc")
def abc():
    return json.dumps({"a": 1})

@authentication.route("login", methods=['POST'])
def login():
    return response(success=True)