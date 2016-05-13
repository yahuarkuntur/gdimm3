
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class BaseWindow(object):

    def __init__(self, gladefile, window_id):
        self.gladefile = gladefile
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object(window_id)
        self.post_init()

    def on_window_destroy(self, object, data=None):
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        Gtk.main_quit()

    def post_init(self):
        pass


# EOF
