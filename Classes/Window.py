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

    def run(self):
        pygame.init()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
                if event.type == pygame.KEYDOWN:
                    self.keydown(event)
            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))
            self.buttons.draw(self.screen)
            self.sprite_move()
            pygame.display.flip()
        pygame.quit()

    def keydown(self, event):
        pass

    def sprite_move(self):
        pass