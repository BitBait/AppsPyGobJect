import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class CheckHistory(Gtk.Window):
    def __init__(self):
        super(CheckHistory, self).__init__()

        # Variables to store the seasonal state in and what veg have been planted
        self.Season = "Spring"
        self.Year = None
        self.VegList = []
        self.VegStr = ""
        '''
        # CSS and styling
        Screen = Gdk.Screen.get_default()
        Provider = Gtk.CssProvider()
        StyleContext = Gtk.StyleContext()
        StyleContext.add_provider_for_screen(
            Screen, Provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        css = b"""
        label {
            font-family: Montserrat;
        }
        radiobutton {
            font-size: 125%;
            font-weight: 500;  
            margin: 5px          
        }
        """

        Provider.load_from_data(css)
        '''
        # Create the seasons toggle radio buttons
        self.Spring = Gtk.RadioButton.new_with_label_from_widget(None, "Spring")
        self.Spring.connect("toggled", self.SetSeason)
        self.Spring.set_property("name", "Spring")

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
        # self.VegLabel = Gtk.Label(label="None")
        # self.VegLabel.set_property("name", "VegLabel")

        # VegGrid
        self.VegGrid = Gtk.Grid()

        # Arrangements of widgets (buttons, combo box's etc)
        # In widget container
        self.Grid = Gtk.Grid()
        self.Grid.attach(self.Spring, 1, 1, 1, 1)
        self.Grid.attach(self.Summer, 1, 2, 1, 1)
        self.Grid.attach(self.Autumn, 1, 3, 1, 1)
        self.Grid.attach(self.Winter, 1, 4, 1, 1)
        self.Grid.attach(self.YearsInput, 2, 1, 1, 1)
        self.Grid.attach(self.Confirm, 2, 4, 1, 1)
        self.Grid.attach(self.VegGrid, 1, 5, 2, 2)

        self.add(self.Grid)

    def SetSeason(self, Button):
        self.Season = Button.get_label()
        print(self.Season)

    def AddVeg(self, Confirm):
        self.VegList = []
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

        self.Grid.remove(self.VegGrid)
        self.VegGrid = Gtk.Grid()

        for item in range(len(self.VegList)):
                label = Gtk.Label(label=self.VegList[item])
                self.VegGrid.attach(label, 1, item, 1, 1)

        self.Grid.attach(self.VegGrid, 1, 5, 1, 1)
        self.show_all()

CheckHistoryWindow = CheckHistory()
CheckHistoryWindow.connect("destroy", Gtk.main_quit)
CheckHistoryWindow.show_all()
Gtk.main()