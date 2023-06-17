import pygame


class Prisoner(pygame.sprite.Sprite):
    def __init__(self, x, y, v):
        super().__init__()
        self.image = pygame.image.load("data/img/prisoner.png")
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.v = v

    def make_step(self):
        self.x += self.v
        self.rect.x = self.x
