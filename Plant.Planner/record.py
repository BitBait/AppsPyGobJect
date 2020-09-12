import gi
from os import getcwd, path

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk


class RecordInput(Gtk.Window):
    def __init__(self):
        super(RecordInput, self).__init__()
        # Storing the vegetables for input into a file
        self.VegList = []
        self.Season = None
        self.Year = None

        # Season Label
        self.SeasonLabel = Gtk.Label(label="Choose the Season")

        # Code to generate the seasons box
        Seasons = ("Spring", "Summer",  "Autumn", "Winter")
        self.SeasonsInput = Gtk.ComboBoxText()
        for i in Seasons:
            self.SeasonsInput.append_text(i)

        # Seasons Button
        self.SeasonButton = Gtk.Button(label="Save")
        self.SeasonButton.connect("clicked", self.SeasonSave)

        # Years Label
        self.YearsLabel = Gtk.Label(label="Select a year")

        # Code to generate years box
        self.YearsInput = Gtk.ComboBoxText()
        for i in range(100):
            Year = i + 2000
            self.YearsInput.append_text(str(Year))

        # Years Button
        self.YearsButton = Gtk.Button(label="Save")
        self.YearsButton.connect("clicked", self.YearSave)

        # Veg Input label
        self.VegLabel = Gtk.Label(label="Enter a vegetable (one at a time)")

        # Code to generate veg entry
        self.VegEntry = Gtk.Entry()
        self.VegEntry.set_placeholder_text("Enter one vegetable then press add")

        # Add Veg Button
        self.VegButton = Gtk.Button(label="Add vegetable")
        self.VegButton.connect("clicked", self.VegInput)
        self.VegButton.set_sensitive(False)

        # Save Button
        self.SaveButton = Gtk.Button(label="Save Vegetable Data")
        self.SaveButton.connect("clicked", self.SaveVeg)

        # Reset Button
        self.ResetButton = Gtk.Button(label="Reset Form")
        self.ResetButton.connect("clicked", self.Reset)

        # Arrangements of widgets (buttons, combo box's etc)
        # In widget container
        Grid = Gtk.Grid()
        Grid.attach(self.SeasonsInput, 2, 1, 1, 1)
        Grid.attach(self.SeasonLabel, 1, 1, 1, 1)
        Grid.attach(self.SeasonButton, 3, 1, 1, 1)
        Grid.attach(self.YearsInput, 2, 2, 1, 1)
        Grid.attach(self.YearsLabel, 1, 2, 1, 1)
        Grid.attach(self.YearsButton, 3, 2, 1, 1)
        Grid.attach(self.VegEntry, 2, 3, 1, 1)
        Grid.attach(self.VegLabel, 1, 3, 1, 1)
        Grid.attach(self.VegButton, 3, 3, 1, 1)
        Grid.attach(self.SaveButton, 2, 4, 1, 1)
        Grid.attach(self.ResetButton, 3, 4, 1, 1)
        self.add(Grid)

    def VegInput(self, VegButton):
        self.VegList.append(str(self.VegEntry.get_text()).lower())
        print("{0} planted in {1} of {2}".format(self.VegEntry.get_text(),
                                                 self.SeasonsInput.get_active_text(),
                                                 self.YearsInput.get_active_text()))
        self.VegEntry.set_text("")

    def SeasonSave(self, SeasonButton):
        self.Season = self.SeasonsInput.get_active_text()
        self.SeasonsInput.set_sensitive(False)
        if self.Year is not None:
            self.VegButton.set_sensitive(True)

    def YearSave(self, YearButton):
        self.Year = self.YearsInput.get_active_text()
        self.YearsInput.set_sensitive(False)
        if self.Season is not None:
            self.VegButton.set_sensitive(True)

    def SaveVeg(self, SaveButton):
        CompleteName = path.join(getcwd(), "{0}-{1}.csv".format(self.Season, self.Year))
        f = open(CompleteName, "a+")
        for Vegetable in self.VegList:
            f.write(Vegetable + ",")

        f.close()

    def Reset(self, ResetButton):
        self.VegList = []
        self.Season = None
        self.Year = None
        self.SeasonsInput.set_sensitive(True)
        self.YearsInput.set_sensitive(True)
        self.VegButton.set_sensitive(False)


if __name__ == "__main":
    RecordInputWindow = RecordInput()
    RecordInputWindow.connect("destroy", Gtk.main_quit)
    RecordInputWindow.show_all()
    Gtk.main()