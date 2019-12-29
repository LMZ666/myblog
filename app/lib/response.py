import json


def response(**kwargs):
    data = kwargs.get('data', {})
    data = json.dumps(data)
    success = kwargs.get('success')
    code = 200
    if not success:
        code = 500
    return data, code
