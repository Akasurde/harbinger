import yaml
from openapi_parser import parse


def test_parse_v1():
    with open("./products/qualys/api-docs.json", 'r') as stream:
        try:
            doc = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    parse(doc)


def test_parse_v2():
    with open("./products/petstore/petstore-simple.json", 'r') as stream:
        try:
            doc = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    parse(doc)