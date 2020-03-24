from random import randint
import pygame
from pygame.locals import *
from boom_anime import *

SCREEN_SIZE=(480,700)
FPS=60

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_path,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_path)
        self.speed=speed
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.y+=self.speed

class BackGroundSprite(GameSprite):

    def __init__(self,is_alt=False):
        super().__init__('.\\images\\background.png')
        if is_alt:
            self.rect.y=-self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_SIZE[1]:
            self.rect.y = -self.rect.height

class HeroSprite(GameSprite):

    def __init__(self):
        super().__init__('.\\images\\me1.png',0)
        self.rect.x=200
        self.rect.y=450

    def update(self):
        super().update()

class EnemySprite(GameSprite):

    def __init__(self):
        super().__init__('.\\images\\enemy1.png',randint(1,3))
        self.rect.x=randint(0,400)

    def update(self):
        super().update()
        if self.rect.y>=SCREEN_SIZE[1]:
            self.kill()

    def __del__(self):
        pass


class BulletSprite(GameSprite):

    def __init__(self,hero):
        super().__init__('.\\images\\bullet1.png',-2)
        self.hero=hero
        self.rect.x = self.hero.rect.x + self.hero.rect.width / 2
        self.rect.y = self.hero.rect.y

    def update(self):
        super().update()
        if self.rect.y < 0:
            self.kill()

