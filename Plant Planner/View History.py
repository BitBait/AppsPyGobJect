import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class CheckHistory(Gtk.Window):
    def __init__(self):
        super(CheckHistory, self).__init__()

        self.Season = None

        # Create the spring season
        self.Spring = Gtk.RadioButton.new_with_label_from_widget(None, "Spring")
        self.Spring.connect("toggled", self.Test)
        self.Summer = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Summer")
        self.Summer.connect("toggled", self.Test)
        self.Autumn = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Autumn")
        self.Autumn.connect("toggled", self.Test)
        self.Winter = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Winter")
        self.Winter.connect("toggled", self.Test)

        # Arrangements of widgets (buttons, combo box's etc)
        # In widget container
        Grid = Gtk.Grid()
        Grid.attach(self.Spring, 1, 1, 1, 1)
        Grid.attach(self.Summer, 1, 2, 1, 1)
        Grid.attach(self.Autumn, 1, 3, 1, 1)
        Grid.attach(self.Winter, 1, 4, 1, 1)

        self.add(Grid)

    def Test(self, Button):
        self.Season = Button.get_label()
        print(self.Season)

CheckHistoryWindow = CheckHistory()
CheckHistoryWindow.connect("destroy", Gtk.main_quit)
CheckHistoryWindow.show_all()
Gtk.main()