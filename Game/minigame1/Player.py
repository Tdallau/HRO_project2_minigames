import pygame
import os
import json
from pygame import *
from minigame1.Entity import *
from minigame1.ExitBlock import *
from minigame1.KeyBlock import *
from minigame1.PilarBlock import *
from minigame1.Text import *
from minigame1.Mobs import *
from minigame1.HighScore import *
from minigame1.Inventory import *


class Player(Entity):
    def __init__(self, screen, font_preferences, entities, x, y):
        Entity.__init__(self)
        self.screen = screen
        self.font_preferences = font_preferences
        self.entities = entities
        self.xvel = 0
        self.yvel = 0
        self.item = False
        self.finished = False
        self.onGround = False
        self.inventory = Inventory({},{},{}) 
        # self.image = Surface((32,64))
        # self.image.fill(Color("#0000FF"))
        # self.image.convert()
        self.key = pygame.image.load(os.path.join("images","player3.png")).convert()
        self.image = self.key
        self.rect = Rect(x, y, 32, 64)

    def update(self, up, down, left, right, running, platforms,mobs):
        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms,mobs)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms,mobs)

    def collide(self, xvel, yvel, platforms, mobs):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    print(self.inventory.slot_1["name"])
                    if self.inventory.slot_1["name"] == "key":
                        
                        self.finished = True
                    else:
                        t = Text("Je hebt de sleutel nog niet, je moet deze eerst vinden", self.font_preferences, 20, (0, 128, 0))
                        text = t.create_text()

                        self.screen.blit(text,
                        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
                if isinstance(p, KeyBlock):
                    
                    # print(p.rect)
                    self.backupKey_x = p.rect.x
                    self.backupKey_y = p.rect.y

                    self.entities.remove(p)
                    platforms.remove(p)

                    # t = Text("Je hebt de sleutel, ga nu naar de finish!", self.font_preferences, 20, (0, 128, 0))
                    # text = t.create_text()

                    # self.screen.blit(text,
                    # (320 - text.get_width() // 2, 240 - text.get_height() // 2))
                    

                    
                    self.inventory.slot_1 = { 'name' : 'key', 'img' : ""}
                if not isinstance(p, PilarBlock):
                   
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        print ("collide right")
                    if xvel < 0:
                        self.rect.left = p.rect.right
                        print ("collide left")
                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0
                    if yvel < 0:
                        self.rect.top = p.rect.bottom

            for m in mobs:
                if pygame.sprite.collide_rect(self, m):
                    # self.rect.x = 0 + self.rect.w
                    # self.rect.y = 576
                    print(m.rect.top + 1)
                    print(self.rect.bottom)
                    if m.rect.top - 1 == self.rect.bottom:
                        print("hit top")
                        m.delete(mobs,m)
                        self.entities.remove(m)
                    else:
                        self.rect.x = 0 + self.rect.w
    
                    

