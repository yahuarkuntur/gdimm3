# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock
from lxml import etree
from ..contribuyente import ContribuyenteModel


class ContribuyenteTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_load_ok(self):

        xml_string = """
          <ruc numero="1002003004001">
            <razon_social>JOHN DOE</razon_social>
            <tipoDocRepLegal>C</tipoDocRepLegal>
            <identificacionRepLegal>1002003004</identificacionRepLegal>
          </ruc>
        """

        model = ContribuyenteModel()
        root = etree.fromstring(xml_string)
        model.load(root)

        self.assertEqual(model.get_ruc(), "1002003004001")
        self.assertEqual(model.get_nombre(), "JOHN DOE")
        self.assertEqual(model.get_documento(), "1002003004")

        model.set_ruc(" 1002003004001 ")
        self.assertEqual(model.get_ruc(), "1002003004001")
        model.set_nombre(" JOHN DOE ")
        self.assertEqual(model.get_nombre(), "JOHN DOE")
        model.set_nombre(" JOHN    DOE ")
        self.assertEqual(model.get_nombre(), "JOHN DOE")
        model.set_documento(" 1002003004 ")
        self.assertEqual(model.get_documento(), "1002003004")


if __name__ == "__main__":
    unittest.main()
