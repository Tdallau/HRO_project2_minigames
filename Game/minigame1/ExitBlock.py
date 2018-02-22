import pygame
from pygame import *
from minigame1.Platform import *

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.image.load(os.path.join("images","Finish.png")).convert()