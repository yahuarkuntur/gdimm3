
import os
from ..gtk.widget_factory import WidgetFactory
from base import BaseWindow
from ..models.declaracion import DeclaracionModel


class DeclaracionWindow(BaseWindow):

    def __init__(self):
        gladefile = os.path.join("glade", "declaracion.glade")
        BaseWindow.__init__(self, gladefile, "declaracionWindow")
        self.model = DeclaracionModel()

    def on_window_destroy(self, object, data=None):
        self.window.destroy()

    def on_btnCancelar_clicked(self, obj, data=None):
        pass

    def on_btnGuardar_clicked(self, obj, data=None):
        pass

    def post_init(self):
        self.layout = self.builder.get_object("fixed1")

    def show(self):
        self.load_declaracion()
        self.window.show()
        self.window.maximize()

    def set_model(self, declaracion_model):
        self.model = declaracion_model

    def load_declaracion(self):
        version = self.model.get_codigo_version()
        factory = WidgetFactory(version)
        widgets = factory.build_widgets()

        for widget in widgets:
            self.layout.put(widget.obj, widget.left, widget.top)
            widget.obj.show()

# EOF
