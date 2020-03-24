import pygame
from pygame.locals import *
from plane_sprite import *
from random import randint
from sys import exit
from boom_anime import *

pygame.init()
ENEMY_EVENT=pygame.USEREVENT
HERO_FIRE_EVENT=pygame.USEREVENT + 1

class PlaneGame(object):

    def __init__(self):
        self.screen=pygame.display.set_mode(SCREEN_SIZE)
        self.clock=pygame.time.Clock()
        self.__create_sprite()
        pygame.display.set_caption('飞机大战')
        pygame.time.set_timer(ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,200)

    def start_game(self):
        self.clock.tick(FPS)
        while True:
            self.__update_sprite()
            self.__event_hander()
            self.__check_collision()

    def game_over(self):
        pygame.quit()
        exit()

    def __create_sprite(self):
        bg1=BackGroundSprite()
        bg2=BackGroundSprite(True)
        self.hero=HeroSprite()
        self.bg_group=pygame.sprite.Group(bg1,bg2,self.hero)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()


    def __check_collision(self):

        #子弹与敌机发生碰撞
        b=pygame.sprite.groupcollide(self.bullet_group,self.enemy_group,True,True)
        if len(b)>0:
            print(b.items())

        #敌机与英雄发生碰撞
        enemies=pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            self.hero.kill()
            print('游戏结束')
            self.game_over()

    def __event_hander(self):
        for event in pygame.event.get():

            #退出游戏
            if event.type==QUIT:
                self.game_over()

            #每秒生成一架敌机
            if event.type==ENEMY_EVENT:
                enemy=EnemySprite()
                self.enemy_group.add(enemy)

            #移动英雄飞机
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    self.hero.rect=self.hero.rect.move(0,-50)
                if event.key==K_DOWN:
                    self.hero.rect = self.hero.rect.move(0, 50)
                if event.key==K_LEFT:
                    self.hero.rect=self.hero.rect.move(-50,0)
                if event.key==K_RIGHT:
                    self.hero.rect=self.hero.rect.move(50,0)

            self.__limit_hero()

            #生成子弹
            if event.type==HERO_FIRE_EVENT:
                bullet=BulletSprite(self.hero)
                self.bullet_group.add(bullet)


    def __update_sprite(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)
        pygame.display.update()

    def __limit_hero(self):
        # 限制英雄飞机的移动范围
        if self.hero.rect.top < 0:
            self.hero.rect.top = 0
        elif self.hero.rect.bottom > SCREEN_SIZE[1]:
            self.hero.rect.bottom = SCREEN_SIZE[1]
        elif self.hero.rect.left < 0:
            self.hero.rect.left = 0
        elif self.hero.rect.right > SCREEN_SIZE[0]:
            self.hero.rect.right = SCREEN_SIZE[0]


if __name__ == '__main__':
    game=PlaneGame()
    game.start_game()