import pygame
import sys
import os
import csv
import random
from pygame import *
from minigame1.Player import *
from minigame1.Mobs import *
from minigame1.Camera import *
from minigame1.KeyBlock import *
from minigame1.PilarBlock import *
from minigame1.Text import *
from minigame1.HighScore import *
from pprint import pprint

def Tim_2dPlatform():

    WIN_WIDTH = 800
    WIN_HEIGHT = 640
    HALF_WIDTH = int(WIN_WIDTH / 2)
    HALF_HEIGHT = int(WIN_HEIGHT / 2)

    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
    DEPTH = 32
    FLAGS = 0
    CAMERA_SLACK = 30

    
    global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

    pygame.display.set_caption("2D platform")
    timer = pygame.time.Clock()

    start_tick = pygame.time.get_ticks()

    font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]

    up = down = left = right = running = False
    bg = pygame.image.load(os.path.join("images","strand.jpg")).convert()
    screen.blit(bg,(0,0))

    scoreboard = Surface((180,70))
    scoreboard.fill((255,255,255))
    screen.blit(scoreboard,(scoreboard.get_width(),0))
    print(scoreboard.get_width())

    entities = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    player = Player(screen,font_preferences, entities, 32, 640)
    mob = Mobs(265,WIN_HEIGHT + 64,1)
    platforms = []

    x = y = 0
    drawLevel(x,y,platforms,entities)
    total_level_width  = 44*32
    total_level_height = 25*32
    camera = Camera(complex_camera, total_level_width, total_level_height)

    entities.add(player)
    entities.add(mob)
    mobs.add(mob)

    heighscore = HighScore(0)
    active = True

    #end of game message
    t = Text("Je hebt deze mini-game uitgespeeld. klik op r om de mini-game te reseten of op c om af te sluiten.", font_preferences, 25, (0, 0, 0))
    text = t.create_text()

    #scoreboard tile
    st = Text("Highscore: | Score: ", font_preferences, 20, (0,0,0))
    st_text = st.create_text()



    while active:
        timer.tick(30)
        # pygame.mixer.music.load("strand.mp3")
        # pygame.mixer.music.play()

        # if not player.finished:
        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if player.finished:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
                    heighscore.checkForHighScore(seconde)
                    return heighscore
                if e.type == pygame.KEYDOWN and e.key == pygame.K_r:

                    heighscore.checkForHighScore(seconde)

                    player.inventory.clearInventory()
                    player.rect.x = 32
                    player.rect.y = 640
                    player.xvel = 0
                    player.yvel = 0
                    player.finished = False
                    start_tick = pygame.time.get_ticks()

                    # k = KeyBlock(player.backupKey_x,player.backupKey_y)
                    # entities.add(k)
                    # platforms.append(k)
                    entities = pygame.sprite.Group()
                    entities.add(player)
                    entities.add(mob)
                    player.entities = entities
                    platforms = []
                    x = y = 0
                    drawLevel(x,y,platforms,entities)

                    # mob = Mobs(265,WIN_HEIGHT + 64,1)
                    mob.rect.x = 265
                    mob.rect.y = WIN_HEIGHT + 64
                    # mobs.add(mob)


            if not player.finished:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                    up = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
                    down = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                    left = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                    right = True
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    running = True

                if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                    up = False
                if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                    down = False
                if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                    right = False
                if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                        left = False

        # draw background
        screen.blit(bg,(0,0))
        scoreboard.fill((255,255,255))
        scoreboard.blit(st_text,(0,0))

        #highscore amound
        hsa = Text(str(heighscore.amound), font_preferences, 20, (0,0,0))
        hsa_text = hsa.create_text()

        scoreboard.blit(hsa_text,(20,st_text.get_height() + 10))

        if not player.finished:
            seconde = (pygame.time.get_ticks() - start_tick )//1000
            tm = Text(str(seconde), font_preferences, 20, (0, 0, 0))
            tm_text = tm.create_text()

        scoreboard.blit(tm_text,
        (scoreboard.get_width() - (scoreboard.get_width() / 2) + 40 , st_text.get_height() + 10))

        #draw scoreboard
        # scoreboard.fill((255,255,255))
        screen.blit(scoreboard,(scoreboard.get_width() - 100,0))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms, mobs)
        mob.update(mobs,platforms,entities)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        if player.finished:  
            screen.blit(text,
            (320 - text.get_width() // 2, 400 - text.get_height() // 2))

        entities = player.entities
        mobs = mob.mobs
        pygame.display.update()

def drawLevel (x,y,platforms,entities):
    levels = ["level1", "level2", "level3"]
    
    readCSV = ''
    row = ''
    col = ''
    # print(levels[random.randint(0,1)])

    # build the level
    with open(levels[random.randint(0,2)] + ".csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')

        for row in readCSV:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    platforms.append(p)
                    entities.add(p)
                if col == "E":
                    e = ExitBlock(x, y)
                    platforms.append(e)
                    entities.add(e)
                if col == "K":
                    k = KeyBlock(x, y)
                    platforms.append(k)
                    entities.add(k)    
                if col == "B":
                    b = PilarBlock(x, y)
                    platforms.append(b)
                    entities.add(b)   
                x += 32
            y += 32
            x = 0
        print(readCSV)

        
