import pygame


class TextWriter:
    def write_text(self, screen, text, color):
        background = pygame.transform.scale(pygame.image.load("data/img/background.png"),
                                            (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 20)
        text_coord = 10
        for line in text:
            string_rendered = font.render(line, True, color)
            text_rect = string_rendered.get_rect()
            text_coord += 10
            text_rect.top = text_coord
            text_rect.x = 50
            text_coord += text_rect.height
            screen.blit(string_rendered, text_rect)