# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from base import BaseWindow, DialogBox
from ..models.contribuyente import ContribuyenteModel
from ..gtk.decorator import Decorator


def strip_non_alpha(string):
    lower = range(96, 124)
    upper = range(64, 92)
    upper.append(32)  # 32 = SPACE
    stripped = (c for c in string if ord(c) in lower or ord(c) in upper)
    return ''.join(stripped)


class EditarContribuyenteWindow(BaseWindow):

    def __init__(self):
        gladefile = os.path.join("glade", "editar_contribuyente.glade")
        BaseWindow.__init__(self, gladefile, "editarContribuyenteWindow")
        self.set_modal(True)

    def on_btnCancel_clicked(self, obj, data=None):
        self.window.destroy()

    def on_numericfield_changed(self, entry):
        text = entry.get_text()
        text = str(text).strip()
        entry.set_text(''.join([i for i in text if i in '0123456789']))

    def on_alphafield_changed(self, entry):
        text = entry.get_text()
        text = strip_non_alpha(text)
        entry.set_text(text.upper())

    def on_btnSave_clicked(self, obj, data=None):
        contrib = ContribuyenteModel()
        contrib.set_ruc(self.eRUC.get_text())
        contrib.set_nombre(self.eRazonSocial.get_text().upper())
        contrib.set_documento(self.eDocumento.get_text())

        aiter = self.cmbTipoDocumento.get_active_iter()
        if aiter:
            contrib.set_tipo_documento(self.modeloTipo.get_value(aiter, 1))

        # validar modelo
        try:
            self.model.add(contrib)
            self.model.save()
        except Exception as ex:
            DialogBox('Ha ocurrido un error!', 'error', self.window, str(ex))
            return

        # recargar listado principal
        self.parent.load_list()
        self.window.destroy()

    def set_data(self, model):
        self.eRUC.set_text(model.get_ruc() or "")
        self.eRazonSocial.set_text(model.get_nombre() or "")
        self.eDocumento.set_text(model.get_documento() or "")

    def set_model(self, model):
        self.model = model

    def show(self):
        if not self.eRUC.get_editable():
            Decorator.disabled(self.eRUC)
        self.window.show()

    def post_init(self):
        self.eRUC = self.builder.get_object("eRUC")
        self.eRazonSocial = self.builder.get_object("eRazonSocial")
        self.eDocumento = self.builder.get_object("eDocumento")
        self.cmbTipoDocumento = self.builder.get_object("cmbTipoDocumento")

        # connect events
        self.eRUC.connect("changed", self.on_numericfield_changed)
        self.eDocumento.connect("changed", self.on_numericfield_changed)
        self.eRazonSocial.connect("changed", self.on_alphafield_changed)

        self.modeloTipo = Gtk.ListStore(str, str)
        self.modeloTipo.append(['Cédula', "C"])
        # self.modeloTipo.append(['Pasaporte', "P"])

        self.cmbTipoDocumento.set_model(self.modeloTipo)
        self.cmbTipoDocumento.set_active(0)

        renderer_text = Gtk.CellRendererText()
        self.cmbTipoDocumento.pack_start(renderer_text, True)
        self.cmbTipoDocumento.add_attribute(renderer_text, "text", 0)

# EOF
