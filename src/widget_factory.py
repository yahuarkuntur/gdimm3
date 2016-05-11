
import os
import gi
gi.require_version('Gtk', '3.0')
from lxml import etree
from gi.repository import Gtk

Y_FACTOR = 8
X_FACTOR = 12
W_FACTOR = 12
H_FACTOR = 10
W_CHARS = 6
START_TOP = 1200
FONT_FACTOR = 1000


class Object(object):

    def __init__(self, obj, widget):
        self.obj = obj
        self.top = (int(widget["top"]) - START_TOP) / Y_FACTOR
        self.left = int(widget["left"]) / X_FACTOR


class WidgetFactory:

    def __init__(self, formid):
        self.formid = formid
        self.attributes = [
            "numero", "top", "left", "width", "height", "etiqueta",
            "tablaReferencial", "mensajeAyuda", "tipoControl", "colorLetra",
            "fontSize", "editable"
        ]

    def _create_label(self, widget):
        label = Gtk.Label(widget["etiqueta"])
        font_size = int(widget["fontSize"]) * FONT_FACTOR
        markup = (
            '<span color="#000" size="%s">%s</span>' %
            (str(font_size), widget["etiqueta"])
        )
        label.set_markup(markup)
        return Object(label, widget)

    def _create_combobox(self, widget):
        width = int(widget["width"]) / W_FACTOR
        height = int(widget["height"]) / H_FACTOR

        combo = Gtk.ComboBoxText()
        combo.set_entry_text_column(0)
        combo.set_tooltip_text(widget["mensajeAyuda"])
        combo.set_size_request(width, height)

        combo.append_text("")
        combo.set_active(0)

        obj = Object(combo, widget)
        obj.top = obj.top - 10
        return obj

    def _create_entry(self, widget):
        width = int(widget["width"]) / W_FACTOR
        height = int(widget["height"]) / H_FACTOR

        entry = Gtk.Entry()
        entry.set_width_chars(W_CHARS)
        entry.set_size_request(width, height)
        entry.set_tooltip_text(widget["mensajeAyuda"])
        entry.set_property('xalign', 1)

        if widget["tipoControl"] == "T":
            entry.set_text("")
        else:
            entry.set_text("0.00")

        if widget["editable"] != "SI":
            entry.set_editable(False)
            entry.modify_base(Gtk.STATE_NORMAL, Gtk.gdk.color_parse("#cccccc"))

        obj = Object(entry, widget)
        obj.top = obj.top - 10
        return obj

    def build_widgets(self):
        tree = etree.parse(os.path.join('xml', 'CMPFRM.xml'))
        form = tree.find("version[@codigo='%s']" % str(self.formid))

        widgets = []

        for field in form:
            widget = dict()
            for key in self.attributes:
                widget[key] = field.attrib.get(key)

            # labels
            if widget["tipoControl"] == "L":
                obj = self._create_label(widget)
                widgets.append(obj)

            # entries
            if widget["tipoControl"] in ["T", "M"]:
                obj = self._create_entry(widget)
                widgets.append(obj)

            # combobox
            if widget["tipoControl"] == "C":
                obj = self._create_combobox(widget)
                widgets.append(obj)

        return widgets

# EOF
