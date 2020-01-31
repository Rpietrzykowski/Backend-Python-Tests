import json
import jsonpath


def parse_body_to_json(body):
    body_json = json.dumps(body)
    return body_json


def find_json_key(response, key):
    data = response.json()
    value = jsonpath.jsonpath(data, key)
    return value
