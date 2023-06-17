import pygame
from Classes.Window import Window
from Classes.TextWriter import TextWriter
from Classes.Prisoner import Prisoner
from Classes.Congratulation import Congratulation


class Level(Window):
    def __init__(self, name, menu):
        self.width = 450
        self.height = 450
        super().__init__(self.width, self.height)
        self.name = name
        self.load_text(name)
        self.timer = 27
        self.menu = menu
        self.reset_level()
        self.reset_timer()
        self.load()
        self.run()

    def reset_level(self):
        self.line = 0
        self.index = 0
        self.prisoners = pygame.sprite.Group()
        self.prisoners_count = 0
        self.add_prisoner()

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
        for prisoner in self.prisoners:
            prisoner.make_step()
            if prisoner.rect.x >= self.width:
                self.finish()
        self.prisoners.draw(self.screen)

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
            self.delete_first_prisoner()
        if self.line == len(self.text):
            self.finish()

    def finish(self):
        result = self.line
        self.reset_level()
        pygame.time.set_timer(self.timer, 0)
        self.congrats = Congratulation(result, len(self.text), self, self.menu)

    def process_events(self, event):
        if event.type == self.timer:
            if self.prisoners_count < len(self.text):
                self.add_prisoner()

    def add_prisoner(self):
        v = 0.15
        if self.prisoners_count < len(self.text) / 3:
            v = 0.1
        elif self.prisoners_count > 2 * len(self.text) / 3:
            v = 0.2
        self.prisoners.add(Prisoner(122, 390, v))
        self.prisoners_count += 1

    def delete_first_prisoner(self):
        first_prisoner = None
        for prisoner in self.prisoners:
            if first_prisoner is None or first_prisoner.rect.x < prisoner.rect.x:
                first_prisoner = prisoner
        first_prisoner.kill()
        if len(self.prisoners) == 0:
            self.add_prisoner()

    def reset_timer(self):
        pygame.time.set_timer(self.timer, 10000)
