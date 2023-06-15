import sys
from Classes.Window import Window
from Classes.Button import Button
from Classes.Rules import Rules
from Classes.Levels import Levels
import pygame


class MainMenu(Window):
    def __init__(self):
        self.width = 450
        self.height = 450
        super().__init__(self.width, self.height)
        self.load()
        self.run()

    def load(self):
        self.set_background("data/img/background.png")
        self.exit = Button(self, "data/img/exit.png", self.quit, (100, 50), (300, 100))
        self.rules = Button(self, "data/img/rules.png", self.open_rules, (100, 50), (50, 100))
        self.start = Button(self, "data/img/start.png", self.open_levels, (100, 50), (175, 100))

    def quit(self):
        pygame.quit()
        sys.exit()

    def open_rules(self):
        self.rules_window = Rules(self)

    def open_levels(self):
        self.levels_window = Levels(self)