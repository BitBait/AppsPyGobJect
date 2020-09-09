import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

class CheckHistory(Gtk.Window):
    def __init__(self):
        super(CheckHistory, self).__init__()

        # Variables to store the seasonal state in and what veg have been planted
        self.Season = None
        self.Year = None
        self.VegList = []
        self.VegStr = ""

        # CSS and styling
        Screen = Gdk.Screen.get_default()
        Provider = Gtk.CssProvider()
        StyleContext = Gtk.StyleContext()
        StyleContext.add_provider_for_screen(
            Screen, Provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        css = b"""
        #VegLabel {
            font: 20px Sans;
        }
        """

        Provider.load_from_data(css)

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

        # Veg Label
        self.VegLabel = Gtk.Label(label="None")
        self.VegLabel.set_property("name", "VegLabel")

        # Arrangements of widgets (buttons, combo box's etc)
        # In widget container
        Grid = Gtk.Grid()
        Grid.attach(self.Spring, 1, 1, 1, 1)
        Grid.attach(self.Summer, 1, 2, 1, 1)
        Grid.attach(self.Autumn, 1, 3, 1, 1)
        Grid.attach(self.Winter, 1, 4, 1, 1)
        Grid.attach(self.YearsInput, 2, 1, 1, 1)
        Grid.attach(self.Confirm, 2, 3, 1, 1)
        Grid.attach(self.VegLabel, 1, 5, 4, 4)

        self.add(Grid)

    def SetSeason(self, Button):
        self.Season = Button.get_label()
        print(self.Season)

    def AddVeg(self, Confirm):
        self.Year = self.YearsInput.get_active_text()
        file = open("{0}-{1}.csv".format(self.Season, self.Year), "r")
        List = file.read()
        CurrentStr = ""
        for item in List:
            if item == ",":
                self.VegList.append(CurrentStr)
                self.VegStr += CurrentStr + "\n"
                CurrentStr = ""
            else:
                CurrentStr += item

        print(self.VegList)
        self.VegLabel.set_text(self.VegStr)

CheckHistoryWindow = CheckHistory()
CheckHistoryWindow.connect("destroy", Gtk.main_quit)
CheckHistoryWindow.show_all()
Gtk.main()