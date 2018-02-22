import pygame
import os
from pygame import *
from minigame1.Platform import *



class KeyBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)

        self.key = pygame.image.load(os.path.join("images","strandbal.png")).convert()
        self.key.set_colorkey( (255,255,255))
        self.image = self.key