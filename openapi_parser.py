import yaml


def parse(doc):
    definition_set = set()
    info = doc.get('info', '')
    if info != '':
        desc = info.get('description', 'not defined')
        title = info.get('title', 'not defined')
    print(definition_set, info, desc, title)


def main():
    with open("./products/petstore/petstore-simple.json", 'r') as stream:
        try:
            doc = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    parse(doc)


if __name__ == '__main__':
    main()
