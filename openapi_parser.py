import yaml


class AnsibleParameter:
    def __init__(self, data):
        self.ansible_native_datatype = {
            'string': 'str',
            'integer': 'int',
            'boolean': 'bool',
            'array': 'list',
        }
        self.ansible_element_datatype = {
            'csv': 'str'
        }
        self.name = data.get('name')
        self.required = data.get('required', False)
        self.datatype = self.ansible_native_datatype[data.get('type', 'string')]
        self.elements = None
        if data.get('collectionFormat', None):
            self.elements = self.ansible_element_datatype[data.get('collectionFormat')]

    def __repr__(self):
        r = ""
        if self.required is not None:
            r += "required=%s, " % self.required
        if self.datatype:
            r += "type='%s', " % self.datatype
        if self.elements:
            r += "elements='%s', " % self.elements

        r = r.rstrip(', ')
        return '%s=dict(%s)' % (self.name, r)


class ModuleObj:
    def __init__(self):
        self.doc = None

    def parse(self, doc):
        self.doc = doc

    def get_paths(self):
        parameters = {}
        for url, value in self.doc['paths'].items():
            if value.get('get'):
                ansi_param = []
                for i in value['get'].get('parameters', ''):
                    ansi_param.append(AnsibleParameter(i))
                parameters[url] = ansi_param
        print(parameters)
        return parameters


def render_parameters(url, params):
    from jinja2 import Environment, FileSystemLoader
    file_loader = FileSystemLoader('provider/ansible')
    env = Environment(loader=file_loader)
    template = env.get_template('main.tpl')
    output = template.render(
        url=url,
        params=params
    )
    import random
    with open("output/modules/module_%s.py" % random.randint(1, 100000), "w") as f:
        f.write(output)


def main():
    m = ModuleObj()
    url = "./products/qualys/api-docs.json"
    if 1:
        url = "./products/petstore/petstore-simple.json"
    with open(url, 'r') as stream:
        try:
            doc = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    m.parse(doc)
    parameters = m.get_paths()
    for url, params in parameters.items():
        render_parameters(url=url, params=params)


if __name__ == "__main__":
    main()
