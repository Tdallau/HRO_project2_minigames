import pygame as pg
import numpy as np
from menu.Menu import Menu
import minigame1.Minigame1 as m1
import minigame2.Minigame2 as m2
import minigame3.Minigame3 as m3
import minigame4.Minigame4 as m4
import minigame5.Minigame5 as m5
import minigame6.Minigame6 as m6
from minigame1.HighScore import HighScore
from os import path



def main():
    pg.init()
    screen = pg.display.set_mode((800, 640))
    pg.display.set_caption("Het Strand Leven")
    timer = pg.time.Clock()

    menu = Menu(screen)
    sk = ""
 

    # button = Menu.menu(screen)

    
    while True:
        timer.tick(30)

        menu = Menu(screen)
        print(menu.allHigs)
        whileMenu(menu,screen)
        sk = menu.sk
        
        startMiniGame(sk)




def whileMenu (menu,screen):
    screen = pg.display.set_mode((800, 640))
    while not menu.start:
        # print('Menu')
        # hs = menu.test
        button = Menu.menu(screen,menu.m1Higs,menu.m2Higs,menu.m3Higs,menu.m4Higs,menu.m5Higs,menu.m6Higs)
        menu.checkInput(button)

def startMiniGame(sk):
    if(sk == "Minigame1"):
        m1.Tim_2dPlatform()
    elif (sk == "Minigame2"):
        m2.Game().game_intro()
        # m2.Game().run()
    elif (sk == "Minigame3"):
        m3.game()
    elif (sk == "Minigame4"):
        m4.wilco()
    elif (sk == "Minigame5"):
        m5.gameLoop()
    elif (sk == "Minigame6"):
        m6.main()
        
    


if __name__ == "__main__":
    main()
