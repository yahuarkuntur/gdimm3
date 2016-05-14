
from lxml import etree


class ContribuyenteModel:
    _ruc = None
    _nombre = None
    _tipo_doc_rep = None
    _doc_rep = None

    def __init__(self):
        self._data = etree.Element("ruc", numero="")
        self._nombre = etree.SubElement(self._data, "razon_social")
        self._tipo_doc_rep = etree.SubElement(self._data, "tipoDocRepLegal")
        self._doc_rep = etree.SubElement(self._data, "identificacionRepLegal")

    def load(self, data):
        self._data = data
        for i in self._data:
            if i.tag == "razon_social":
                self._nombre = i
            elif i.tag == "tipoDocRepLegal":
                self._tipo_doc_rep = i
            elif i.tag == "identificacionRepLegal":
                self._doc_rep = i

    def set_ruc(self, ruc):
        self._data.set("numero", ruc)

    def set_nombre(self, nombre):
        self._nombre.text = unicode(str(nombre))

    def set_tipo_documento(self, tipo_documento):
        self._tipo_doc_rep.text = tipo_documento

    def set_documento(self, documento):
        self._doc_rep.text = documento

    def get_ruc(self):
        return self._data.get("numero")

    def get_nombre(self):
        return self._nombre.text

    def get_tipo_documento(self):
        return self._tipo_doc_rep.text

    def get_documento(self):
        return self._doc_rep.text

    def __str__(self):
        return tostring(self._data)

    def get_element(self):
        return self._data

# EOF
