# -*- coding: utf-8 -*-

import re
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
        self._ruc_regex = re.compile("^\d{13}$")
        self._cedula_regex = re.compile("^\d{10}$")

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

    def validar(self):
        if self.get_ruc() is None or not len(self.get_ruc()):
            raise Exception('El R.U.C. es requerido.')
            return False

        if not self._ruc_regex.match(self.get_ruc()):
            raise Exception('El R.U.C. no es válido.')
            return False

        if self.get_nombre() is None or not len(self.get_nombre()):
            raise Exception('La razón social es requerida.')
            return False

        if self.get_documento() is None or not len(self.get_documento()):
            raise Exception('El número de documento del representante es requerido.')
            return False

        if "C" == self.get_tipo_documento():
            if not self._cedula_regex.match(self.get_documento()):
                raise Exception('El número de documento del representante no es válido.')
                return False

        return True

# EOF
