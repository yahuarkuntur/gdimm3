
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def DialogBox(text, type='error', window=None, secondary_text=None):
    def close_handler(self, response):
        self.destroy()

    message_type = {
        "error": Gtk.MessageType.ERROR,
        "warning": Gtk.MessageType.WARNING,
        "info": Gtk.MessageType.INFO
    }

    dialog = Gtk.MessageDialog(
        parent=window,
        flags=Gtk.DialogFlags.MODAL,
        type=message_type[type],
        buttons=Gtk.ButtonsType.OK,
        message_format=text
    )

    dialog.format_secondary_text(secondary_text)
    dialog.connect("response", close_handler)
    dialog.show()


class BaseWindow(object):

    def __init__(self, gladefile, window_id):
        self.gladefile = gladefile
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object(window_id)
        self.post_init()

    def on_window_destroy(self, object, data=None):
        self.window.destroy()

    def on_gtk_quit_activate(self, menuitem, data=None):
        self.window.destroy()

    def post_init(self):
        pass


# EOF
