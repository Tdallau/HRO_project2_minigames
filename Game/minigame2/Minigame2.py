import sys
import pygame
from pygame.locals import *
import random
import time
from os import path


pygame.init()
pygame.font.init()
#----------------------------Colors------------------------------#
red = (150,0,0)
green = (0,150,0)
dark_red = (250,0,0)
dark_green = (0,250,0)

#----------------------------Variabelen------------------------------#
width = 1000
height = 600
your_score = 0
font_size_int = 75
font_size_int2 = 30

pygame.mixer.music.load("BackgroundSound.mp3")
HS_file = "highscore.txt"
fontINTRO = pygame.font.SysFont("font", font_size_int, bold=False, italic=False)
fontINTRO2 = pygame.font.SysFont("font", font_size_int2, bold=False, italic=False)
font = pygame.font.get_default_font()
background = pygame.image.load("PythonBackground.png")
smallfont = pygame.font.SysFont("font", 25, bold=False, italic=False)

def score(score, self):
    text = smallfont.render("Score: "+ str(self.ship.your_score), True, (0,0,0))
    self.screen.blit(text,[0,0]) 

#-----------------------Speler-------------------------#

class Ship():

    def __init__(self, screen_rect):

        self.image = pygame.image.load("PythonStickman.png")
        self.image = pygame.transform.scale(self.image, (50,100))
        self.your_score = 0

        self.rect = self.image.get_rect()
   
        self.rect.bottom = screen_rect.bottom 
        self.rect.centerx = screen_rect.centerx

        self.move_x = 0

        self.shots = []
        self.shots_count = 0

        self.max_shots = 2

    #-----------------------------------------------#

    def event_handler(self, event):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.move_x = -10
            elif event.key == K_RIGHT:
                self.move_x = 10
            elif event.key == K_SPACE:
                self.shots.append(Bullet(self.rect.centerx, self.rect.top))

        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                self.move_x = 0

    #-----------------------------------------------------------#            

    def update(self):

        self.rect.x += self.move_x

        for s in self.shots:
            s.update(self.shots)

        for i in range(len(self.shots)-1, -1, -1):
            print ("debug: Ship.update: testing bullet ", i)
            if not self.shots[i].is_alive:
                print ("debug: Ship.update: removing bullet ", i)
                del self.shots[i]
                
                
    #-------------------------------------------------------#

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

        for s in self.shots:
            s.draw(screen)

    def bullet_detect_collison(self, enemy_list):

        for s in self.shots:
            for e in enemy_list:
                if pygame.sprite.collide_circle(s, e):
                    s.is_alive = False
                    e.is_alive = False
                    
                    

#---------------------------Zand-----------------------------#

class Bullet():

    def __init__(self, x, y):

        self.image = pygame.image.load("zand.png")
        self.image = pygame.transform.scale(self.image, (25,25))

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #-----------------------------------------------------------#

    def update(self, shots):

        self.rect.y -= 15
        if self.rect.y < 0:
            shots.remove(self)
    
    #-----------------------------------------------------------#

    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)

#-----------------------------Water------------------------------#

class Enemy():

    def __init__(self, x, y, speed):
        self.speed = speed
        self.image = pygame.image.load("Water.png")

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.is_alive = True

    #-----------------------------------------------------------#

    def update(self, enemies):

        self.rect.y += self.speed
        if self.rect.y > 400:
            enemies.remove(self)

    #------------------------------------------------------------------#

    def draw(self, screen):
        
        screen.blit(self.image, (self.rect.centerx, self.rect.y))
        

#----------------------------------------------------------------------#
def text_objects(text,font):
        
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

#------------------------------Spel------------------------------#

class Game():

    def __init__(self):

        pygame.init()

        w, h = 1000, 600
        
        self.screen = pygame.display.set_mode((width, height))

        pygame.mouse.set_visible(False)

        self.ship = Ship(self.screen.get_rect())
        
        self.load_data()

        self.enemies = []
        
        font = pygame.font.SysFont("", 72)
        self.text_paused = font.render("PAUSED", True, (255, 0, 0))
        self.text_paused_rect = self.text_paused.get_rect(center=self.screen.get_rect().center)

    def load_data(self):
        
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_file), 'r+') as f:
            try:
                self.highscore = int(f.read())

            except:
                self.highscore = 0

    def game_over(self):
        
        self.lol = True

        while self.lol:
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Game().game_intro()

            self.screen.blit(background,(0,0))
            game_over_scherm = fontINTRO.render("Het spel is voorbij!", True, (0,0,0))
            self.screen.blit(game_over_scherm,[(width / 2) - 160, height / 2])
            game_over_scherm2 = fontINTRO2.render("Je score is: "+ str(self.ship.your_score), True, (0,0,0))
            self.screen.blit(game_over_scherm2,[(width / 2) - 40, height / 2 + 40])

            self.button("Opniew Spelen", 150,450,150,50,green,dark_green,"play")
            self.button("Terug naar Menu", 750,400,150,50,red,dark_red,"menu")

            pygame.display.update()

    def button(self,tekst,x,y,w,h,ic,ac,action = None):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                if action == "play":
                    Game().run()
                elif action == "quit":
                    self.introt = False
                elif action == "menu":
                    Game().game_intro()
                    self.introt = False
                elif action == "muziekuit":
                    pygame.mixer.music.pause()
                elif action == "muziekaan":
                    pygame.mixer.music.unpause()
                elif action == "muziek":
                    pygame.mixer.music.play(0)
                                           
                    
        else:
            pygame.draw.rect(self.screen, ic, (x,y,w,h))
        
        smallText = pygame.font.SysFont("font", 25)
        textSurf, textRect = text_objects(tekst, smallfont)
        textRect.center = (x + w/2, y + h/2)
        self.screen.blit(textSurf,textRect)

        
#-------------------------Game Intro--------------------------#
    def game_intro(self):
        
        self.introt = True

        pygame.mixer.music.pause()

        while self.introt:
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.introt = False
            
            self.screen.blit(background,(0,0))
            intro = fontINTRO.render("Waterval the Game!", True, (0,0,0))
            self.screen.blit(intro,[(width / 2) - 240, 100])
            intro2 = fontINTRO2.render("Druk op de pijltoetsen om te bewegen", True, (0,0,0))
            self.screen.blit(intro2,[(width / 2) - 179, 160])
            intro2 = fontINTRO2.render("Druk op spatie om te schieten", True, (0,0,0))
            self.screen.blit(intro2,[(width / 2) - 149, 190])
            intro2 = fontINTRO2.render("High Score: " + str(self.highscore), True, (0,0,0))
            self.screen.blit(intro2,[(width / 2) - 70, 0])
            
            self.button("Geluid uit", 515,(float(362.5)),95,25,red,dark_red,"muziekuit")
            self.button("Geluid aan", 390,(float(362.5)),95,25,green,dark_green,"muziek")
            
            self.button("Start!", 150,350,150,50,green,dark_green,"play")
            self.button("Terug naar Menu", 700,350,150,50,red,dark_red,"quit")
            # print(self.highscore)

            pygame.display.update()        

    #------------------------MAIN GAME LOOP--------------------------#
    def run(self):
        global your_score
        clock = pygame.time.Clock()
        pygame.mixer.music.play(-1)
        pygame.mouse.set_visible(True)

        RUNNING = True
        PAUSED = False
        start_tick = pygame.time.get_ticks()
        start = 900
        while RUNNING:
            your_score = 0
            clock.tick(30)
            start -= 1
            
        
            if start <= 0:
                print(self.ship.your_score)
                # Game().game_intro()
                return

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        RUNNING = False

                if not PAUSED:
                    self.ship.event_handler(event)

            #-----------------------------Changes---------------------------#
            
            if not PAUSED:
                seconde = (pygame.time.get_ticks()-start_tick)//1000
                if seconde == 3:
                    for i in range(50, 1000, 100):
                        self.enemies.append(Enemy(i, 100, random.randint(5,15)))
                    start_tick = pygame.time.get_ticks()
                
                self.ship.update()

                for e in self.enemies:
                    e.update(self.enemies)

                self.ship.bullet_detect_collison(self.enemies)
                
                for i in range(len(self.enemies)-1, -1, -1):
                    print ("debug: Ship.update: testing bullet ", i)
                    if not self.enemies[i].is_alive:
                        print ("debug: Ship.update: removing bullet ", i)
                        del self.enemies[i]
                        self.ship.your_score += 1
                    
                if self.ship.your_score > self.highscore:
                    self.highscore = self.ship.your_score
                    with open(path.join(self.dir, HS_file), 'r+') as f:
                        f.write(str(self.ship.your_score))
                        
            #------------------------------Draws------------------------------#
        
            self.screen.blit(background,(0,0))

            self.button("Geluid uit", 895,10,95,25,red,dark_red,"muziekuit")
            self.button("Geluid aan", 895,45,95,25,green,dark_green,"muziekaan")

            self.ship.draw(self.screen)

            for e in self.enemies:
                e.draw(self.screen)

            if PAUSED:
                self.screen.blit(self.text_paused, self.text_paused_rect)

            score(score, self)
        
            pygame.display.update()

        #------------------Quit---------------------#

        pygame.quit()

#-----------------------Calls-------------------------#

# Game().game_intro()    

