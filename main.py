#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.ui.main_window import MainWindow


if __name__ == "__main__":
    main = MainWindow()
    Gtk.main()

# EOF
