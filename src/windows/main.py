# -*- coding: utf-8 -*-

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from base import BaseWindow, DialogBox


class MainWindow(BaseWindow):

    def __init__(self):
        gladefile = os.path.join("glade", "main.glade")
        BaseWindow.__init__(self, gladefile, "mainWindow")

    def on_window_destroy(self, object, data=None):
        Gtk.main_quit()

    def post_init(self):
        self.window.show()

# EOF
