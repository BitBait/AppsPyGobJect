import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

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

class Plan(Gtk.Window):
    def __init__(self):
        super(Plan, self).__init__()

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

        CurrentAlgoritherms = ("Basic", "None")
        self.AlgorithmInput = Gtk.ComboBoxText()
        for i in CurrentAlgoritherms:
            self.AlgorithmInput.append_text(i)

        self.ConfirmButton = Gtk.Button(label="Confirm Choice")
        self.ConfirmButton.connect("clicked", self.Confirm)

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

        self.add(self.Grid)

    def Confirm(self, ConfirmButton):
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

PlanWindow = Plan()
PlanWindow.connect("destroy", Gtk.main_quit)
PlanWindow.show_all()
Gtk.main()