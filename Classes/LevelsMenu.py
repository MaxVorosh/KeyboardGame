from Classes.Window import Window
from Classes.Button import Button
from Classes.Level import Level


class LevelsMenu(Window):
    def __init__(self, last_window):
        self.height = 450
        self.width = 450
        super().__init__(self.width, self.height)
        self.last_window = last_window
        self.load()
        self.run()

    def load(self):
        self.set_background("data/img/background.png")
        self.back = Button(self, "data/img/back.png", self.back, (100, 50), (175, 50))
        self.maths = Button(self, "data/img/4.png", self.maths, (50, 50), (350, 125))
        self.east = Button(self, "data/img/3.png", self.east, (50, 50), (250, 125))
        self.maksim = Button(self, "data/img/1.png", self.maksim, (50, 50), (50, 125))
        self.changes = Button(self, "data/img/2.png", self.changes, (50, 50), (150, 125))

    def back(self):
        self.last_window.run()

    def maths(self):
        self.level = Level("Maths", self)

    def east(self):
        self.level = Level("East", self)

    def maksim(self):
        self.level = Level("Maksim", self)

    def changes(self):
        self.level = Level("Changes", self)
