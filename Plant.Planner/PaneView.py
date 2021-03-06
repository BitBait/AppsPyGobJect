import gi
from os import getcwd, path

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gio

Brassicas = ["brussels sprouts", "cabbage", "cauliflower", "kale", "kohl-rabi",
             "oriental greens", "radish", "swede", "turnips"]
Legumes = ["peas", "broad beans"]
Onions = ["onion", "garlic", "shallot", "leek"]
Potato = ["potato", "tomato"]
Roots = ["beetroot", "carrot", "celeriac", "celery", "florence fennel",
         "parsley", "parsnip"]

AllVeg = []

for i in Brassicas:
    AllVeg.append(i)
for i in Legumes:
    AllVeg.append(i)
for i in Onions:
    AllVeg.append(i)
for i in Potato:
    AllVeg.append(i)
for i in Roots:
    AllVeg.append(i)

class NoteBook(Gtk.Window):
    def __init__(self):
        super(NoteBook, self).__init__()

        # Creation of smaller widgets to fit in notebook
        self.RecordGridWidget = self.CreateRecordGrid()
        self.ViewHistoryWidget = self.CreateViewHistoryGrid()
        self.PlanWidget = self.CreatePlanGrid()

        # Arrangements for higher widgets
        self.Notebook = Gtk.Notebook()
        self.Notebook.append_page(self.RecordGridWidget, Gtk.Label(label="Record your seasons"))
        self.Notebook.append_page(self.ViewHistoryWidget, Gtk.Label(label="View your records"))
        self.Notebook.append_page(self.PlanWidget, Gtk.Label(label="Plan your next year"))
        self.add(self.Notebook)

    def CreateRecordGrid(self):

        # Storing the vegetables for input into a file
        self.VegListRecord = []
        self.SeasonRecord = None
        self.YearRecord = None

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
        self.YearsInputRecord = Gtk.ComboBoxText()
        for i in range(100):
            Year = i + 2000
            self.YearsInputRecord.append_text(str(Year))

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
        self.Grid = Gtk.Grid()
        self.Grid.attach(self.SeasonsInput, 2, 1, 1, 1)
        self.Grid.attach(self.SeasonLabel, 1, 1, 1, 1)
        self.Grid.attach(self.SeasonButton, 3, 1, 1, 1)
        self.Grid.attach(self.YearsInputRecord, 2, 2, 1, 1)
        self.Grid.attach(self.YearsLabel, 1, 2, 1, 1)
        self.Grid.attach(self.YearsButton, 3, 2, 1, 1)
        self.Grid.attach(self.VegEntry, 2, 3, 1, 1)
        self.Grid.attach(self.VegLabel, 1, 3, 1, 1)
        self.Grid.attach(self.VegButton, 3, 3, 1, 1)
        self.Grid.attach(self.SaveButton, 2, 4, 1, 1)
        self.Grid.attach(self.ResetButton, 3, 4, 1, 1)

        return self.Grid

    def CreateViewHistoryGrid(self):

        self.Season = "Spring"
        self.Year = None
        self.VegList = []
        self.VegStr = ""

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

        # Veg Grid as a nicer way of showing what has been planted
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
        self.Grid.attach(self.VegGrid, 3, 1, 1, len(self.VegList))
        return self.Grid

    # Function relating to the input of the vegetable values
    def VegInput(self, VegButton):
        self.VegListRecord.append(str(self.VegEntry.get_text()).lower())
        print("{0} planted in {1} of {2}".format(self.VegEntry.get_text(),
                                                 self.SeasonsInput.get_active_text(),
                                                 self.YearsInputRecord.get_active_text()))
        self.VegEntry.set_text("")

    # Function relating the the picking and saving of the seasons
    # Also checks to see if the add vegetable function should be
    # available
    def SeasonSave(self, SeasonButton):
        self.Season = self.SeasonsInput.get_active_text()
        self.SeasonsInput.set_sensitive(False)
        if self.Year is not None:
            self.VegButton.set_sensitive(True)

    # Function relating the the picking and saving of the years
    # Also checks to see if the add vegetable function should be
    # available
    def YearSave(self, YearButton):
        self.Year = self.YearsInputRecord.get_active_text()
        self.YearsInputRecord.set_sensitive(False)
        if self.Season is not None:
            self.VegButton.set_sensitive(True)

    # Saves the entered vegetables as a CSV file
    def SaveVeg(self, SaveButton):
        CompleteName = path.join(getcwd(), "{0}-{1}.csv".format(self.Season, self.Year))
        file = Gio.file_new_for_path(CompleteName)
        file.create(0, None)
        f = open(CompleteName, "a+")
        for Vegetable in self.VegListRecord:
            f.write(Vegetable + ",")

        f.close()

    # Resets the form including the year and season allowing new entryd
    # to be made
    def Reset(self, ResetButton):
        self.VegListRecord = []
        self.Season = None
        self.Year = None
        self.SeasonsInput.set_sensitive(True)
        self.YearsInputRecord.set_sensitive(True)
        self.VegButton.set_sensitive(False)

    # Function to set the season for the view history widget
    def SetSeason(self, Button):
        self.Season = Button.get_label()
        print(self.Season)

    # Function to set (and reset) the veg text displayed in the text widget
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

        i = 1
        j = 1
        for item in range(len(self.VegList)):
            label = Gtk.Label(label=self.VegList[item] + ",")
            self.VegGrid.attach(label, i, j, 1, 1)
            i += 1
            if i == 5:
                i = 1
                j += 1

        self.Grid.attach(self.VegGrid, 3, 1, 1, len(self.VegList))
        self.show_all()

    def CreatePlanGrid(self):

        self.PlanSeason = None
        self.PlanYear = None
        self.Algorithm = None

        self.PlanSeasonLabel = Gtk.Label(label="Choose the season to plan for: ")
        self.PlanYearLabel = Gtk.Label(label="Choose the year to plan for: ")
        self.PlanAlgorithmLabel = Gtk.Label(label="Choose the algorithm: ")

        self.PlanYearsInput = Gtk.ComboBoxText()
        for i in range(100):
            Year = i + 2000
            self.PlanYearsInput.append_text(str(Year))


        Seasons = ("Spring", "Summer",  "Autumn", "Winter")
        self.PlanSeasonsInput = Gtk.ComboBoxText()
        for i in Seasons:
            self.PlanSeasonsInput.append_text(i)

        CurrentAlgorithms = ("Basic", "None")
        self.AlgorithmInput = Gtk.ComboBoxText()
        for i in CurrentAlgorithms:
            self.AlgorithmInput.append_text(i)

        self.ConfirmButton = Gtk.Button(label="Confirm Choice")
        self.ConfirmButton.connect("clicked", self.confirm)

        # Grid for suggested vegetables
        self.SuggestedVegGrid = Gtk.Grid()

        # Grid for arrangement of widgets
        self.Grid = Gtk.Grid()
        self.Grid.attach(self.PlanSeasonLabel, 1, 1, 1, 1)
        self.Grid.attach(self.PlanYearLabel, 1, 2, 1, 1)
        self.Grid.attach(self.PlanSeasonsInput, 2, 1, 1, 1)
        self.Grid.attach(self.PlanYearsInput, 2, 2, 1, 1)
        self.Grid.attach(self.PlanAlgorithmLabel, 1, 3, 1, 1)
        self.Grid.attach(self.AlgorithmInput, 2, 3, 1, 1)
        self.Grid.attach(self.ConfirmButton, 3, 2, 1, 1)
        self.Grid.attach(self.SuggestedVegGrid, 1, 4, 3, 3)

        return self.Grid

    def confirm(self, ConfirmButton):
        self.PlanSeason = self.PlanSeasonsInput.get_active_text()
        self.PlanYear = self.PlanYearsInput.get_active_text()
        self.Algorithm = self.AlgorithmInput.get_active_text()
        print("Looking for file {0}-{1}.csv".format(self.PlanSeason, str(int(self.PlanYear) -1)))
        if self.Algorithm == "Basic":
            self.PlanVegList = []
            file = open("{0}-{1}.csv".format(self.PlanSeason, str(int(self.PlanYear) - 1)), "r")
            List = file.read()
            CurrentStr = ""
            for item in List:
                if item == ",":
                    self.PlanVegList.append(CurrentStr)
                    #self.VegStr += CurrentStr + "\n"
                    CurrentStr = ""
                else:
                    CurrentStr += item

            for Vegetable in self.PlanVegList:
                if Vegetable in AllVeg:
                    AllVeg.remove(Vegetable)

            i = 1
            j = 1

            for Vegetable in range(len(AllVeg)):
                label = Gtk.Label(label=AllVeg[Vegetable])
                self.SuggestedVegGrid.attach(label, i, j, 1, 1)
                i += 1
                if i == 4:
                    i = 1
                    j += 1

            self.Grid.remove(self.SuggestedVegGrid)
            self.Grid.attach(self.SuggestedVegGrid, 1, 4, 2, 2)
            self.show_all()

Window = NoteBook()
Window.connect("destroy", Gtk.main_quit)
Window.show_all()
Gtk.main()