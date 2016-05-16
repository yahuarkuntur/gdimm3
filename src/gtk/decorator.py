
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Decorator:

    @staticmethod
    def disabled(widget):
        # TODO obtener color de control deshabilitado desde GTK
        provider = Gtk.CssProvider()
        provider.load_from_data('.disabled-entry { background: #ebebeb; }')
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        widget.get_style_context().add_class("disabled-entry")

# EOF
