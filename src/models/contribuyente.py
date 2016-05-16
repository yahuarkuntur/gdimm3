# -*- coding: utf-8 -*-

import re
from lxml import etree


class ContribuyenteModel:

    def __init__(self):
        self._data = etree.Element("ruc", numero="")
        self._nombre = etree.SubElement(self._data, "razon_social")
        self._tipo_doc_rep = etree.SubElement(self._data, "tipoDocRepLegal")
        self._doc_rep = etree.SubElement(self._data, "identificacionRepLegal")
        self._ruc_regex = re.compile("^\d{13}$")
        self._cedula_regex = re.compile("^\d{10}$")

    def load(self, data):
        self._data = data
        self._nombre = data.find('razon_social')
        self._tipo_doc_rep = data.find('tipoDocRepLegal')
        self._doc_rep = data.find('identificacionRepLegal')

    def set_ruc(self, ruc):
        self._data.set("numero", str(ruc).strip())

    def set_nombre(self, nombre):
        nombre = " ".join(nombre.split())
        self._nombre.text = str(nombre).strip()

    def set_tipo_documento(self, tipo_documento):
        self._tipo_doc_rep.text = str(tipo_documento).strip()

    def set_documento(self, documento):
        self._doc_rep.text = str(documento).strip()

    def get_ruc(self):
        return self._data.get("numero")

    def get_nombre(self):
        return self._nombre.text

    def get_tipo_documento(self):
        return self._tipo_doc_rep.text

    def get_documento(self):
        return self._doc_rep.text

    def __str__(self):
        return etree.tostring(self._data)

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
