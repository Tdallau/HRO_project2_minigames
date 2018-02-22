import pygame
import os
from pygame import *
from minigame1.Entity import *

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        # self.image = Surface((32, 32))
        # self.image.fill(Color('#DDDDDD'))
        self.key = pygame.image.load(os.path.join("images","brick.jpg")).convert()
        self.image = self.key
        # self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass