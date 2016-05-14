# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from base import BaseWindow, DialogBox
from editar_contribuyente import EditarContribuyenteWindow
from ..models.contribuyentes import ContribuyentesModel


class ContribuyenteWindow(BaseWindow):

    def __init__(self):
        gladefile = os.path.join("glade", "contribuyente.glade")
        BaseWindow.__init__(self, gladefile, "contribuyenteWindow")

    def on_window_destroy(self, object, data=None):
        self.window.destroy()

    def on_btnClose_clicked(self, obj, data=None):
        self.window.destroy()

    def on_btnNuevo_clicked(self, obj, data=None):
        contrib = self.contribuyentes.get_empty_model_item()
        contribuyente_window = EditarContribuyenteWindow()
        contribuyente_window.set_data(contrib)
        contribuyente_window.set_model(self.contribuyentes)
        contribuyente_window.eRUC.set_editable(True)
        contribuyente_window.show()

    def on_btnEditar_clicked(self, obj, data=None):
        selection = self.trContribuyentes.get_selection()
        (model, aiter) = selection.get_selected()
        if aiter is not None:
            contrib = self.contribuyentes.find_by_ruc(model[aiter][0])
            if contrib:
                contribuyente_window = EditarContribuyenteWindow()
                contribuyente_window.set_data(contrib)
                contribuyente_window.set_model(self.contribuyentes)
                contribuyente_window.show()
        else:
            # TODO mostrar mensaje de error
            pass

    def on_btnBorrar_clicked(self, obj, data=None):
        print "on_btnBorrar_clicked"

    def on_trContribuyentes_row_activated(self, obj, aiter, path, data=None):
        selection = obj.get_selection()
        (model, aiter) = selection.get_selected()
        if aiter is not None:
            contrib = self.contribuyentes.find_by_ruc(model[aiter][0])
            if contrib:
                contribuyente_window = EditarContribuyenteWindow()
                contribuyente_window.set_data(contrib)
                contribuyente_window.set_model(self.contribuyentes)
                contribuyente_window.show()

    def load_list(self):
        try:
            self.contribuyentes = ContribuyentesModel()
            self.contribuyentes.load()
        except Exception as ex:
            DialogBox('Ha ocurrido un error!', 'error', self.window, str(ex))
            return

        self.lista_contribuyentes.clear()
        for item in self.contribuyentes.get_elements():
            text = item.get_nombre()
            key = item.get_ruc()
            self.lista_contribuyentes.append([key, text])

    def show_contribuyentes(self):
        # load tree view with data
        self.load_list()

        # create the TreeViewColumn to display the data
        self.columna_ruc = Gtk.TreeViewColumn('RUC')
        self.columna_nombre = Gtk.TreeViewColumn('Razón Social')

        # add tvcolumn to treeview
        self.trContribuyentes.append_column(self.columna_ruc)
        self.trContribuyentes.append_column(self.columna_nombre)

        # create a CellRendererText to render the data
        self.cell = Gtk.CellRendererText()

        # add the cell to the tvcolumn and allow it to expand
        self.columna_ruc.pack_start(self.cell, True)
        self.columna_nombre.pack_start(self.cell, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        self.columna_ruc.add_attribute(self.cell, 'text', 0)
        self.columna_nombre.add_attribute(self.cell, 'text', 1)

        self.trContribuyentes.set_search_column(0)
        self.columna_ruc.set_sort_column_id(0)
        self.columna_nombre.set_sort_column_id(1)

    def post_init(self):
        # setup widgets
        self.trContribuyentes = self.builder.get_object("trContribuyentes")
        self.lista_contribuyentes = Gtk.ListStore(str, str)
        self.trContribuyentes.set_model(self.lista_contribuyentes)
        # show items
        self.show_contribuyentes()

    def show(self):
        self.window.show()

# EOF
