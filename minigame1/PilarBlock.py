import pygame
from pygame import *
import os
from minigame1.Platform import *


class PilarBlock(Platform):
    def __init__(self,x,y):
        Platform.__init__(self,x,y)

        self.key = pygame.image.load(os.path.join("images","pilaar.png")).convert()
        self.key.set_colorkey( (0,0,0), RLEACCEL )
        self.image = self.key