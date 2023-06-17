import sys

import pygame
from Classes.Window import Window
from Classes.TextWriter import TextWriter
from Classes.Button import Button


class Congratulation(Window):
    def __init__(self, result, max_result, last_level, menu):
        self.width = 450
        self.height = 450
        super().__init__(self.width, self.height)
        self.text = ["Поздравляем!", f"Ваш результат - {result}/{max_result}"]
        self.last_level = last_level
        self.menu = menu
        self.load()
        self.run()

    def load(self):
        self.set_background("data/img/background.png")
        self.exit = Button(self, "data/img/exit.png", self.quit, (100, 50), (300, 100))
        self.repeat_button = Button(self, "data/img/repeat.png", self.repeat, (100, 50), (50, 100))
        self.menu_button = Button(self, "data/img/to_menu.png", self.to_menu, (100, 50), (175, 100))

    def sprite_move(self):
        text_writer = TextWriter()
        text_writer.write_text(self.screen, self.text, pygame.Color("black"))
        self.buttons.draw(self.screen)

    def quit(self):
        pygame.quit()
        sys.exit(0)

    def repeat(self):
        self.last_level.reset_timer()
        self.last_level.run()

    def to_menu(self):
        self.menu.run()