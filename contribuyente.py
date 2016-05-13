#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from src.windows.contribuyente import ContribuyenteWindow


if __name__ == "__main__":
    main = ContribuyenteWindow()
    Gtk.main()

# EOF
