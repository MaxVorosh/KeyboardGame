import pygame
from Classes.Button import Button


class Window:
    def __init__(self, width, height):
        self.resize(width, height)
        self.buttons = pygame.sprite.Group()

    def set_background(self, path):
        self.background = pygame.image.load(path)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def click(self, mouse_pos):
        for btn in self.buttons:
            if btn.check_clicked(mouse_pos):
                btn.click()