import json
from os import path


def load_schema(filename):
    filename = path.join(path.dirname(__file__), 'schemas', filename)
    with open(filename, 'r') as f:
        return json.load(f)


# TODO lazy loading?
class Schema(object):

    GET_BLOCK = load_schema('get_block.json')
    GET_DYNAMIC_GLOBAL_PROPERTIES = load_schema('get_dynamic_global_properties_current.json')
