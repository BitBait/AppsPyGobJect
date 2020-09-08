import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class CheckHistory(Gtk.Window):
    def __init__(self):
        super(CheckHistory, self).__init__()

        self.Season = None
        self.Year = None
        self.VegList = []

        # Create the seasons toggle radio buttons
        self.Spring = Gtk.RadioButton.new_with_label_from_widget(None, "Spring")
        self.Spring.connect("toggled", self.SetSeason)
        self.Summer = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Summer")
        self.Summer.connect("toggled", self.SetSeason)
        self.Autumn = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Autumn")
        self.Autumn.connect("toggled", self.SetSeason)
        self.Winter = Gtk.RadioButton.new_with_label_from_widget(self.Spring, "Winter")
        self.Winter.connect("toggled", self.SetSeason)

        # Code to generate years box
        self.YearsInput = Gtk.ComboBoxText()
        for i in range(100):
            Year = i + 2000
            self.YearsInput.append_text(str(Year))

        # Confirm Button
        self.Confirm = Gtk.Button(label="Confirm choice")
        self.Confirm.connect("clicked", self.AddVeg)

        # Arrangements of widgets (buttons, combo box's etc)
        # In widget container
        Grid = Gtk.Grid()
        Grid.attach(self.Spring, 1, 1, 1, 1)
        Grid.attach(self.Summer, 1, 2, 1, 1)
        Grid.attach(self.Autumn, 1, 3, 1, 1)
        Grid.attach(self.Winter, 1, 4, 1, 1)
        Grid.attach(self.YearsInput, 2, 1, 1, 1)
        Grid.attach(self.Confirm, 2, 3, 1, 1)

        self.add(Grid)

    def SetSeason(self, Button):
        self.Season = Button.get_label()
        print(self.Season)

    def AddVeg(self, Confirm):
        self.Year = self.YearsInput.get_active_text()
        file = open("{0}-{1}.csv".format(self.Season, self.Year), "r")
        List = file.read()

CheckHistoryWindow = CheckHistory()
CheckHistoryWindow.connect("destroy", Gtk.main_quit)
CheckHistoryWindow.show_all()
Gtk.main()