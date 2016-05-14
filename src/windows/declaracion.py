
import os
from ..gtk.widget_factory import WidgetFactory
from base import BaseWindow


class DeclaracionWindow(BaseWindow):

    def __init__(self):
        gladefile = os.path.join("glade", "declaracion.glade")
        BaseWindow.__init__(self, gladefile, "declaracionWindow")

    def on_window_destroy(self, object, data=None):
        self.window.destroy()

    def on_btnCancelar_clicked(self, obj, data=None):
        pass

    def on_btnGuardar_clicked(self, obj, data=None):
        pass

    def show(self):
        self.window.show()
        self.window.maximize()

    def post_init(self):
        factory = WidgetFactory('04201603')
        widgets = factory.build_widgets()

        layout = self.builder.get_object("fixed1")

        for widget in widgets:
            layout.put(widget.obj, widget.left, widget.top)
            widget.obj.show()

# EOF
