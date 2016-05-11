#!/usr/bin/env python

import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from widget_builder import WidgetBuilder


class MainWindow:

    def on_mainWindow_destroy(self, object, data=None):
        print "quit with cancel"
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print "quit from menu"
        Gtk.main_quit()

    def __init__(self):
        self.gladefile = os.path.join("ui", "main.glade")
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("mainWindow")
        self.post_init()
        self.window.maximize()
        self.window.show()

    def post_init(self):
        builder = WidgetBuilder('04201403')
        widgets = builder.build()

        layout = self.builder.get_object("fixed1")

        for widget in widgets:
            layout.put(widget.obj, widget.left, widget.top)
            widget.obj.show()

if __name__ == "__main__":
    main = mainWindow()
    Gtk.main()
