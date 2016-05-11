#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.windows.declaracion_window import DeclaracionWindow


if __name__ == "__main__":
    main = DeclaracionWindow()
    Gtk.main()

# EOF
