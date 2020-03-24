import pygame

class Enemy1Boom(object):

    def __init__(self):
        self.anime_list=[pygame.image.load('.\\images\\enemy1_down'+str(i)+'.png') for i in range(1,5)]

        #print(self.anime_list)

    def set_pos(self,x,y):
        self.x=x
        self.y=y

    def draw_anime(self):
        for i in range(1,4):
            self.screen.blit(self.anime_list[i],(self.x,self.y))
