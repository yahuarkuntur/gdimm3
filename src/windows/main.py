# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from base import BaseWindow, DialogBox
from ..gtk.utils import *
from ..models.datos import DatosModel
from ..models.declaracion import DeclaracionModel
from ..models.contribuyentes import ContribuyentesModel
from contribuyente import ContribuyenteWindow
from declaracion import DeclaracionWindow


class MainWindow(BaseWindow):

    def __init__(self):
        self.datos_model = DatosModel()
        gladefile = os.path.join("glade", "main.glade")
        BaseWindow.__init__(self, gladefile, "mainWindow")

    def on_window_destroy(self, object, data=None):
        Gtk.main_quit()

    def update_combobox(self, combobox, list_store):
        combobox.set_model(list_store)
        combobox.clear()
        combobox.set_active(0)

        renderer_text = Gtk.CellRendererText()
        combobox.pack_start(renderer_text, True)
        combobox.add_attribute(renderer_text, "text", 0)

    def load_contribuyentes(self):
        contribuyentes = ContribuyentesModel()
        contribuyentes.load()
        list_store = Gtk.ListStore(str, str)
        for item in contribuyentes.get_elements():
            text = item.get_ruc() + ' - ' + item.get_nombre()
            list_store.append([text, item.get_ruc()])
        self.update_combobox(self.cmbContribuyentes, list_store)

    def load_formularios(self):
        list_store = Gtk.ListStore(str, str)
        for item in self.datos_model.get_full_list_from_code(5):
            text = item['nombre'] + ' - ' + item['descripcion_impuesto']
            list_store.append([text, item['version']])
        self.update_combobox(self.cmbFormularios, list_store)

    def load_periodos(self, code=-1):
        items = []
        if code != -1:
            items = self.datos_model.get_list_from_code(code)
        list_store = Gtk.ListStore(str, str)
        for item in items:
            list_store.append([item[1], item[0]])
        self.update_combobox(self.cmbPeriodos, list_store)

    def load_anios(self):
        list_store = Gtk.ListStore(str, str)
        for item in self.datos_model.get_list_from_code(30):
            list_store.append([item[1], item[0]])
        self.update_combobox(self.cmbAnios, list_store)

    def post_init(self):
        # setup widgets
        self.cmbContribuyentes = self.builder.get_object("cmbContribuyentes")
        self.cmbFormularios = self.builder.get_object("cmbFormularios")
        self.cmbPeriodos = self.builder.get_object("cmbPeriodos")
        self.cmbAnios = self.builder.get_object("cmbAnios")
        self.hbSustituye = self.builder.get_object("hbSustituye")
        self.rbSemestral = self.builder.get_object("rbSemestral")
        self.rbMensual = self.builder.get_object("rbMensual")
        self.rbSustitutiva = self.builder.get_object("rbSustitutiva")
        self.txtSustituye = self.builder.get_object("txtSustituye")

        # load comboboxes and show window
        self.load_contribuyentes()
        self.load_formularios()
        self.load_periodos()
        self.load_anios()
        self.window.show()

    def on_btnContribuyentes_clicked(self, obj, data=None):
        contribuyente_window = ContribuyenteWindow()
        contribuyente_window.show()

    def on_btnEditar_clicked(self, obj, data=None):
        pass

    def on_btnHelp_clicked(self, obj, data=None):
        pass

    def on_btnAbout_clicked(self, obj, data=None):
        pass

    def on_btnClose_clicked(self, obj, data=None):
        Gtk.main_quit()

    def on_btnAceptar_clicked(self, obj, data=None):
        # alias del formulario
        version = get_active_text(self.cmbFormularios)
        alias = ''
        for item in self.datos_model.get_full_list_from_code(5):
            if item['version'] == version:
                alias = item['nombre']
        alias = alias.replace("FORMULARIO ", "")

        # obtener anio
        anio = get_active_text(self.cmbAnios)

        # obtener mes o periodo
        periodo = get_active_text(self.cmbPeriodos)

        # info del formulario seleccionado
        formularios = self.datos_model.get_full_list_from_code(5)
        data = self.datos_model.find_item_from_key_value(
            formularios,
            'version',
            version
        )

        codigo_version = self.datos_model.get_codigo_version_formulario(
            data['nombre'],
            data['periodicidad']
        )

        # init model
        declaracion = DeclaracionModel()
        declaracion.set_alias_formulario(alias)
        declaracion.set_anio(anio)
        declaracion.set_mes(periodo)
        declaracion.set_periodicidad(data['periodicidad'])
        declaracion.set_version(version)
        declaracion.set_codigo_version(codigo_version)

        # sustitutiva ?
        if self.rbSustitutiva.get_active():
            declaracion.set_original('S')
            declaracion.set_sustituye(self.txtSustituye.get_text())

        # show window
        declaracion_window = DeclaracionWindow()
        declaracion_window.set_model(declaracion)
        declaracion_window.show()

    def on_rbSustitutiva_toggled(self, obj, data=None):
        if obj.get_active():
            self.hbSustituye.show()
        else:
            self.hbSustituye.hide()

    def on_cmbFormularios_changed(self, obj, data=None):
        version = get_active_text(obj)
        formularios = self.datos_model.get_full_list_from_code(5)
        data = self.datos_model.find_item_from_key_value(
            formularios,
            'version',
            version
        )

        if data['periodicidad'] == "SEMESTRAL":
            self.load_periodos(40)
        elif data['periodicidad'] == "MENSUAL":
            self.load_periodos(20)
        else:
            self.load_periodos(-1)  # anual

# EOF
