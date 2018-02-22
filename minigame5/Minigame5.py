import pygame
import time
import random
from datetime import datetime
from minigame5.HighScore import *

pygame.init()

global head

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Badmeester')

img = pygame.image.load('lifeguard.png')
personimg = pygame.image.load('person1.png')
seaimg = pygame.image.load('sea.png')
sharkimg = pygame.image.load('shark.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 20
score = 0
difference = 0

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def display_score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def display_difference(difference):
    text = smallfont.render("Time: " + str(difference), True, black)
    gameDisplay.blit(text, [650, 0])

def badmeester(block_size, badmeesterList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    
    gameDisplay.blit(head, (badmeesterList[-1][0], badmeesterList[-1][1]))

    for XnY in badmeesterList[:-1]:
        pygame.draw.rect(gameDisplay,
                         white,
                         [XnY[0],
                          XnY[1],
                          block_size,
                          block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface= smallfont.render(text, True, color)
    elif size == "medium":
        textSurface= medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    highscore = HighScore(0)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    global direction
    direction = "right"
    score = 0
    difference = 0
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    randPersonX = round (random.randrange(0,
                                          display_width-block_size))#/10.0)*10.0
    randPersonY = round (random.randrange(0,
                                          display_height-block_size))#/10.0)*10.0

    randSharkX = round(random.randrange(0,
                                         display_width - block_size))  # /10.0)*10.0
    randSharkY = round(random.randrange(0,
                                         display_height - block_size))  # /10.0)*10.0
    dateSet = True
    while not gameExit:

        if dateSet:
            now = datetime.now()
            dateSet = False 

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        return
                    if event.key == pygame.K_c:
                        
                        # now = datetime.now()
                        # difference = 0
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            highscore.checkForHighScore(score)
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.blit(seaimg, [0, 0])

        later = datetime.now()
        difference = (later - now).total_seconds()

        PersonThickness = 20
        SharkThickness = 20
        gameDisplay.blit(personimg, (randPersonX, randPersonY))
        gameDisplay.blit(sharkimg, (randSharkX, randSharkY))

        badmeesterList = []
        badmeesterhead = []
        badmeesterhead.append(lead_x)
        badmeesterhead.append(lead_y)
        badmeesterList.append(badmeesterhead)
        badmeester(block_size, badmeesterList)
        display_score(score)
        display_difference(difference)

        pygame.display.update()

        player = pygame.Rect(lead_x,lead_y,20,25)
        person = pygame.Rect(randPersonX,randPersonY,20,20)
        enemy = pygame.Rect(randSharkX,randSharkY,20,20)
        # if personimg.colliderect(head):
        if player.colliderect(person):
            randPersonX = round(random.randrange(0,
                                                 display_width - block_size))#/10.0) * 10.0
            randPersonY = round(random.randrange(0,
                                                 display_height - block_size))#/10.0) * 10.0
            score = score + 1

        if player.colliderect(enemy):
            randSharkX = round(random.randrange(0,
                                                display_width - block_size))  # /10.0) * 10.0
            randSharkY = round(random.randrange(0,
                                                display_height - block_size))  # /10.0) * 10.0
            score = score - 1

  

        if difference >= 60:
            highscore.checkForHighScore(score)
            gameOver = True

        clock.tick(FPS)

    pygame.quit()
    quit()


# gameLoop()