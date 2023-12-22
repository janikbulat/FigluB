import os
import sys
import pygame


pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Warrior(pygame.sprite.Sprite):
    image_statistie = load_image('warriorstatistie.png')
    image_warstate = load_image('warriorwarstate.png')

    def __init__(self, x, y, *group, state='statistie'):
        super().__init__(*group)
        self.state = state
        if self.state == 'warstate':
            self.image = Warrior.image_warstate
        else:
            self.image = Warrior.image_statistie
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x=self.rect.x, y=self.rect.y, state=self.state):
        self.rect = self.rect.move(x, y)

