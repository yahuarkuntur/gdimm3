#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.windows.editar_contribuyente import EditarContribuyenteWindow


if __name__ == "__main__":
    window = EditarContribuyenteWindow()
    window.show()
    Gtk.main()

# EOF
