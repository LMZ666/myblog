import os


class BaseConfig(object):
    DEBUG = True


class DevConfig(BaseConfig):
    SECRET_KEY = "develop"


def get_app_config():
    config = {
        "develop": DevConfig
    }
    env = os.getenv("FLASK_ENV") if os.getenv("FLASK_ENV") else "develop"
    return config.get(env, DevConfig)


app_config = get_app_config()
