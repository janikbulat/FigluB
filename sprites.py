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
    image_blockstate = load_image('warriorblockstate.png')

    def __init__(self, x, y, *group, state='statistie'):
        super().__init__(*group)
        self.state = state
        if self.state == 'warstate':
            self.image = Warrior.image_warstate
        elif self.state == 'statistie':
            self.image = Warrior.image_statistie
        elif self.state == 'blockstate':
            self.image = Warrior.image_blockstate
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hitpoints = 120
        self.attack = 20
        self.good_attack = 25
        self.down_attack = 10

    def update(self, x='', y='', state=''):
        if x == '':
            x = self.rect.x
        if y == '':
            y = self.rect.y
        if state == '':
            state = self.state
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.state = state
        if self.state == 'warstate':
            self.image = Warrior.image_warstate
        elif self.state == 'statistie':
            self.image = Warrior.image_statistie
        elif self.state == 'blockstate':
            self.image = Warrior.image_blockstate
