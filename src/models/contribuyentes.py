
import os
from lxml import etree
from contribuyente import ContribuyenteModel


class ContribuyentesModel:
    lista = []

    def __init__(self):
        self.filename = os.path.join("xml", "DtsRuc.xml")

    def count(self):
        return len(self.lista)

    def exists_replace(self, ruc):
        for item in self.lista:
            if item.get_ruc() == ruc :
                return self.lista.index(item)
        return None

    def find_by_ruc(self, ruc):
        for item in self.lista:
            if item.get_ruc() == ruc :
                return item
        return None

    def get_empty_model_item(self):
        return ContribuyenteModel()

    def add(self, contribuyente):
        try:
            if not (contribuyente.get_ruc() and contribuyente.get_nombre() and contribuyente.get_tipo_documento() and contribuyente.get_documento()):
                raise Warning('Faltan datos en el contribuyente')
        except AttributeError:
            raise TypeError('El argumento no es un objeto tipo contribuyente')
        
        item_index = self.exists_replace(contribuyente.get_ruc())
        if item_index:
            self.lista[item_index] = contribuyente
        else:
            self.lista.append(contribuyente)

    def remove(self, contribuyente):
        if type(contribuyente)==str:
            oContribuyente = self.find_by_ruc(contribuyente)
        else:
            oContribuyente = contribuyente
        
        if oContribuyente:
            self.lista.remove(oContribuyente)

    def save(self):
        list_size = len(self.lista)
        if list_size >= 0:
            data = etree.Element("datos_ruc")
            
            for item in self.lista:
                data.insert(list_size, item.get_element())

            f = open(self.filename, 'w+')
            f.write(etree.tostring(data, encoding='utf8', pretty_print=True))
            f.close()
    
    def load(self):
        if os.path.exists(self.filename):
            parser = etree.XMLParser(remove_comments=True, encoding='utf8')
            data = etree.parse(self.filename, parser)
            root = data.getroot()
            self.lista = []
            for item in root:
                contrib = ContribuyenteModel()
                contrib.load(item)
                self.lista.append(contrib)
        else:
            raise Exception('No existe el archivo "%s"' % self.filename)

    def get_elements(self):
        return self.lista

# EOF
