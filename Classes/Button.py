import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, window, path, func, size, position):
        super().__init__(window.buttons)
        self.set_image(path, size)
        self.func = func
        self.rect.x, self.rect.y = position

    def set_image(self, path, size):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()

    def move(self, position):
        self.x, self.y = position

    def check_clicked(self, mouse_pos):
        return self.rect.x <= mouse_pos[0] <= self.rect.x + self.rect.width and\
               self.rect.y <= mouse_pos[1] <= self.rect.y + self.rect.height

    def click(self):
        self.func()