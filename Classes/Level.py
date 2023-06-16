import sys
import pygame
from Classes.Window import Window
from Classes.TextWriter import TextWriter


class Level(Window):
    def __init__(self, name):
        self.width = 450
        self.height = 450
        super().__init__(self.width, self.height)
        self.name = name
        self.load_text(name)
        self.line = 0
        self.index = 0
        self.load()
        self.run()

    def load(self):
        self.set_background("data/img/background.png")

    def load_text(self, name):
        f = open(f"data/texts/{name}.txt", 'r', encoding="UTF-8")
        self.text = list(filter(lambda x: x, map(str.strip, f.readlines())))
        f.close()

    def is_correct(self, letter):
        return letter == self.text[self.line][self.index]

    def sprite_move(self):
        text_writer = TextWriter()
        text_writer.write_text(self.screen,
                               [self.text[self.line][self.index:], "", f"Счёт: {self.line}/{len(self.text)}"],
                               pygame.Color('black'))
        self.buttons.draw(self.screen)

    def keydown(self, event):
        if not event.unicode:
            pass
        elif self.is_correct(event.unicode):
            self.index += 1
        else:
            self.index = 0
        if self.index == len(self.text[self.line]):
            self.index = 0
            self.line += 1
        if self.line == len(self.text):
            self.finish()

    def finish(self):
        sys.exit(0)
        #TODO
