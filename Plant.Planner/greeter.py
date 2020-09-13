import gi
from record import RecordInput
from view_history import CheckHistory

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class Greeter(Gtk.Window):
    def __init__(self):
        super(Greeter, self).__init__()

        # Greeter label/title
        self.WelcomeLabel = Gtk.Label(label="Welcome to plant planner select an option")

        # Button to plan
        self.RecordButton = Gtk.Button(label="Record a previous season")
        self.RecordButton.connect("clicked", self.Record)

        # Button to view history
        self.ViewHistory = Gtk.Button(label="View a previous season")
        self.ViewHistory.connect("clicked", self.View)

        # Creation of container grid and attachment of child widgets
        self.Grid = Gtk.Grid()
        self.Grid.attach(self.WelcomeLabel, 1, 1, 2, 1)
        self.Grid.attach(self.RecordButton, 1, 2, 1, 1)
        self.Grid.attach(self.ViewHistory, 2, 2, 1, 1)

        self.add(self.Grid)

    def Record(self, RecordButton):
        print("Make a record")
        RecordInputWindow = RecordInput()
        RecordInputWindow.connect("destroy", Gtk.main_quit)
        RecordInputWindow.show_all()

    def View(self, ViewHistory):
        print("View History")
        CheckHistoryWindow = CheckHistory()
        CheckHistoryWindow.connect("destroy", Gtk.main_quit)
        CheckHistoryWindow.show_all()


GreeterWindow = Greeter()
GreeterWindow.connect("destroy", Gtk.main_quit)
GreeterWindow.show_all()
Gtk.main()