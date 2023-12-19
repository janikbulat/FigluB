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

    def __init__(self, x, y, *group, state='statistie'):
        super().__init__(*group)
        if state == 'statistie':
            self.image = Warrior.image_statistie
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y):
        self.rect = self.rect.move(x, y)

