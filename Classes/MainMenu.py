import sys
from Classes.Window import Window
from Classes.Button import Button
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
        pass

    def open_levels(self):
        pass

    def run(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))
            self.buttons.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
