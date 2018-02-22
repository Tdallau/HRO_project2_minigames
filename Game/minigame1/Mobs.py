import pygame
import os
from minigame1.Platform import *
from minigame1.PilarBlock import *
from minigame1.Entity import *

class Mobs(Entity):
    def __init__(self,x,y,lives):
        Entity.__init__(self)

        self.xVel = -4
        self.yVel = 0
        self.lives = lives
        self.image = pygame.image.load(os.path.join("images","enemy.png")).convert()
        self.image.set_colorkey(Color("#ffffff"))
        self.rect = Rect(x,y,32,64)
        # self.mobs = []

    def update(self,mobs,platforms,entities):
        self.mobs = mobs
        self.rect.left += self.xVel

        self.collide(platforms,entities)

    def collide(self,platforms,entities):

        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if not isinstance(p, PilarBlock):

                    if isinstance(p, Platform):

                        if self.xVel < 0:
                            self.rect.left = p.rect.right
                            self.xVel = 4
                        elif self.xVel > 0:
                            self.rect.right = p.rect.left
                            self.xVel = -4
                    



    def delete(self,mobs,m):
        print('delete')
        mobs.remove(m)

        self.mobs = mobs
    
