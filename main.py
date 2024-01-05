import pygame
from sprites import *

class FGWindow:
    def __init__(self):
        self.window = pygame.display.set_mode((900, 700))
        pygame.display.set_caption('FigluB')

    def start(self):
        running = True
        self.window.fill((122, 30, 33))
        all_sprites.draw(self.window)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.window.fill((122, 30, 33))
                    if wr.state == 'warstate':
                         wr.update(state='statistie')
                    else:
                        wr.update(state='warstate')
                    all_sprites.draw(self.window)
            pygame.display.flip()
        pygame.quit()

all_sprites = pygame.sprite.Group()
wr = Warrior(40, 40, all_sprites)
figlub_window = FGWindow()
figlub_window.start()
