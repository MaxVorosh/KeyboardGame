from Classes.Window import Window
from Classes.Button import Button
from Classes.TextWriter import TextWriter
import pygame


class Rules(Window):
    def __init__(self, last_window):
        self.height = 450
        self.width = 450
        super().__init__(self.width, self.height)
        self.last_window = last_window
        self.rules = ['Вы - охранник, мимо которого хотят', 'пробежать несколько опасных людей.',
                      'Не допустите этого!', 'Печатайте слова, появляющиеся в верху экрана.',
                      'Каждая верно написанная строчка', 'нейтрализует одного преступника.',
                      'Каждая ошибка заставляет писать строчку заново.',
                      'Как только кто-то сбежит - вы проиграли.']
        self.load()
        self.run()

    def load(self):
        self.set_background("data/img/background.png")
        self.ok = Button(self, "data/img/ok.png", self.menu, (100, 50), (175, 250))

    def menu(self):
        self.last_window.run()

    def sprite_move(self):
        text_writer = TextWriter()
        text_writer.writeText(self.screen, self.rules, pygame.Color("black"))
        self.buttons.draw(self.screen)
