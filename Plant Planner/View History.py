import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class CheckHistory(Gtk.Window):
    def __init__(self):
        super(CheckHistory, self).__init__()

CheckHistoryWindow = CheckHistory()
CheckHistoryWindow.connect("destroy", Gtk.main_quit)
CheckHistoryWindow.show_all()
Gtk.main()