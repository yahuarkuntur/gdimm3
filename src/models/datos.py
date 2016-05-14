
import os
from lxml import etree


class DatosModel:

    def __init__(self):
        self.parser = etree.XMLParser(remove_comments=True, encoding='utf8')
        self.tree = etree.parse(os.path.join('xml', 'DtsRfr.xml'), self.parser)

    def get_list_from_code(self, code):
        data = []
        nodes = self.tree.find('/*[@codigo="'+str(code)+'"]')

        if nodes is None:
            return data

        for node in nodes:
            codigo = node.find('codigo')
            if codigo is None:
                continue

            nombre = node.find('nombre')
            if nombre is not None:
                data.append([codigo.text, nombre.text])

            descripcion = node.find('descripcion')
            if descripcion is not None:
                data.append([codigo.text, descripcion.text])

        return data

    def find_item_from_key_value(self, items, key, value):
        for item in items:
            if key in item.keys():
                if item[key] == value:
                    return item
        return None

    def get_full_list_from_code(self, code):
        data = []
        nodes = self.tree.find('/*[@codigo="'+str(code)+'"]')

        if nodes is None:
            return data

        for node in nodes:
            a = dict()
            for name, value in node.items():
                a[name] = value
            data.append(a)

        return data

# EOF
