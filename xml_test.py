#!/usr/bin/env python

import os
import gi
gi.require_version('Gtk', '3.0')
from lxml import etree
from gi.repository import Gtk


class main:

    def run(self):
        tree = etree.parse(os.path.join('XML','CMPFRM.xml'))
        formulario = tree.find("version[@codigo='04201403']")

        atributos = ["numero", "top", "left", "width", "height", "etiqueta",
            "tablaReferencial", "mensajeAyuda", "tipoControl", "colorLetra",
            "fontSize"
        ]

        controles = []

        for campo in formulario:
            widget = dict()
            for atributo in atributos:
                widget[atributo] = campo.attrib.get(atributo)
            #print widget

            # etiquetas
            if widget["tipoControl"] == "L":
                print "etiqueta", widget["etiqueta"]
                label = Gtk.Label(widget["etiqueta"])
                #label.set_markup('<span color="#CCC" size="'+fontSize+'">'+widget["etiqueta"]+'</span>');
                controles.append(label)
                #self.fixed1.put(lbl, left, top)
                #lbl.show()

        return controles

if __name__ == "__main__":
    main = main()
    main.run()
