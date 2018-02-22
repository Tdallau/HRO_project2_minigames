import pygame as pg
import numpy as np
import tkinter as tk
import sys
import os
from os import path


class Menu():
    def __init__(self, screen):
        self.start = False
        self.sk = ""
        self.m2Higs = self.load_data("../minigame2/highscore.txt") 
        self.m1Higs = self.load_data("../minigame1/highscore.txt") 
        self.m3Higs = self.load_data("../minigame3/highscore.txt")
        self.m4Higs = self.load_data("../minigame4/highscore.txt")
        self.m5Higs = self.load_data("../minigame5/highscore.txt")
        self.m6Higs = self.load_data("../minigame6/highscore.txt")
        self.allHigs = self.m1Higs + self.m2Higs + self.m3Higs + self.m4Higs + self.m5Higs + self.m6Higs

    @staticmethod
    def menu(screen,hsm1, hsm2,hsm3, hsm4,hsm5,hsm6):

        fontINTRO = pg.font.SysFont("font", 50, bold=False, italic=False)
        fontHiGS = pg.font.SysFont("font", 25, bold=True, italic=False) 


        m1Text = fontINTRO.render("2D Platformer", True, (0,0,0))
        m2Text = fontINTRO.render("Waterfall", True, (0,0,0))
        m3Text = fontINTRO.render("Picnic Panic", True, (0,0,0))
        m4Text = fontINTRO.render("Endless Runner", True, (0,0,0))
        m5Text = fontINTRO.render("badmeester spel", True, (0,0,0))
        m6Text = fontINTRO.render("naar het strand", True, (0,0,0))

        # text = fontINTRO.render("2D Platformer", True, (0,0,0))
        infoIcon = fontINTRO.render("i", True, (255,0,0)) 

        # bg = pg.image.load(os.path.join("images","strand.jpg")).convert()

        screen.fill((160,160,160))

        button1 = pg.image.load('images/2DPlatformer.png').convert_alpha()
        button2 = pg.image.load('images/waterfall.png').convert_alpha()
        button3 = pg.image.load('images/PicnicPanic.png').convert_alpha()
        button4 = pg.image.load('images/EndlessRunner.png').convert_alpha()
        button5 = pg.image.load('images/badmeesterSpel.png').convert_alpha()
        button6 = pg.image.load('images/NaarHetStrand.png').convert_alpha()

        button1.blit(m1Text, [35,60])
        button2.blit(m2Text, [70,60])
        button3.blit(m3Text, [45,60])
        button4.blit(m4Text, [15,60])
        button5.blit(m5Text, [10,60])
        button6.blit(m6Text, [25,60])

        b = screen.blit(button1,(66,65))
        b2 = screen.blit(button2, (66,255))
        b3 = screen.blit(button3, (66,445))
        b4 = screen.blit(button4, (430,65))
        b5 = screen.blit(button5, (430,255))
        b6 = screen.blit(button6, (430,445))

        m1info = screen.blit(infoIcon, [360,50])
        m2info = screen.blit(infoIcon, [360,240])
        m3info = screen.blit(infoIcon, [360,430])
        m4info = screen.blit(infoIcon, [724,50])
        m5info = screen.blit(infoIcon, [724,240])
        m6info = screen.blit(infoIcon, [724,430])

        Highscorem1 =fontHiGS.render("highscore: " + str(hsm1), True, (0,0,0))
        Highscorem2 = fontHiGS.render("highscore: " + str(hsm2), True, (0,0,0))
        Highscorem3 = fontHiGS.render("highscore: " + str(hsm3), True, (0,0,0))
        Highscorem4 = fontHiGS.render("highscore: " + str(hsm4), True, (0,0,0))
        Highscorem5 = fontHiGS.render("highscore: " + str(hsm5), True, (0,0,0))
        Highscorem6 = fontHiGS.render("highscore: " + str(hsm6), True, (0,0,0))
        screen.blit(Highscorem1, [70,225])
        screen.blit(Highscorem2, [70, 415])
        screen.blit(Highscorem3, [70, 605])
        screen.blit(Highscorem4, [434, 225])
        screen.blit(Highscorem5, [434, 415])
        screen.blit(Highscorem6, [434, 605])

        Highscore = fontHiGS.render("Highscore: " +str(hsm1+hsm2+hsm3+hsm4+hsm5+hsm6), True, (0,0,0))
        screen.blit(Highscore, [10, 620])
        #605

        title = fontINTRO.render("Het strand Leven", True, (0,255,255))
        screen.blit(title, [270,10])

        pg.display.flip()
        button = button1.get_rect()
        btn = []
        btn.append('menu')
        btn.append(b)
        btn.append(b2)
        btn.append(b3)
        btn.append(b4)
        btn.append(b5)
        btn.append(b6)
        btn.append(m1info)
        btn.append(m2info)
        btn.append(m3info)
        btn.append(m4info)
        btn.append(m5info)
        btn.append(m6info)
        return btn

    def checkInput(self,button):
        events = pg.event.get()
        for e in events:
            if e.type == pg.QUIT:
                # self.start = True
                pg.quit()
                sys.exit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_1:
                    self.start = True
                    self.sk = "Minigame1"
                if e.key == pg.K_2:
                    self.start = True
                    self.sk = "Minigame2"
                if e.key == pg.K_3:
                    self.start = True
                    self.sk = "Minigame3"
                if e.key == pg.K_4:
                    self.start = True
                    self.sk = "Minigame4"
                if e.key == pg.K_5:
                    self.start = True
                    self.sk = "Minigame5"
                if e.key == pg.K_6:
                    self.start = True
                    self.sk = "Minigame6"
            if e.type == pg.MOUSEBUTTONDOWN:
                #get pos of mouse click
                pos = pg.mouse.get_pos()
                #get info where clicked
                click = self.check_button_click(button,len(button),pos,1)
                #do things when clicked on a button
                if not np.isscalar(click):
                    # if click[0] == 'menu':
                    print(click[1])
                    if click[1] == 1:
                        self.start = True
                        self.sk = "Minigame1"
                    if click[1] == 2:
                        self.start = True
                        self.sk = "Minigame2"
                        print(self.load_data("../minigame2/highscore.txt"))
                    if click[1] == 3:
                        self.start = True
                        self.sk = "Minigame3"
                    if click[1] == 4:
                        self.start = True
                        self.sk = "Minigame4"
                    if click[1] == 5:
                        self.start = True
                        self.sk = "Minigame5"
                    if click[1] == 6:
                        self.start = True
                        self.sk = "Minigame6"
                    if click[1] == 7:
                        self.popupBox("dit is een 2D platformer, het doel is om de strantbal te vinden en dan zo snel mogelijk naar de finsih te gaan. je kunt dit spel besturen met de pijltjes toetsen.")
                    if click[1] == 8:
                        self.popupBox("dit is waterfall the game, het doel is om zoveel mogelijk water te stopen voor dat de tijd op is. je kunt dit spel besturen met de pijltjes toetsen en de spatiebalk.")
                    if click[1] == 9:
                        self.popupBox("dit is picnic panic, het doel is om zoveel mogelijk voetsel op tevangen voor de tijd op is (maar pas op! voor de niet etbaaren vorwerpen. je kunt dit spel besturen met je muis.")
                    if click[1] == 10:
                        self.popupBox("dit is een endless runner, het doel is om zo lang mogelijk te blijven rennen zonder dde obstacels te raken. je kunt dit spel besturen met de spatiebalk.")
                    if click[1]== 11:
                        self.popupBox("dit is het badmeester spel, het doel is om zo veel mogelijk mensen te reden. je kunt dit spel besturen met de pijltjes toetsen.")
                    if click[1] == 12:
                        self.popupBox("dit is een op weg naar het strand, het doel is om de gigantische strandbal te vinden. je kunt dit spel besturen met de pijltjes toetsen.")


    def check_button_click (self,button,len,pos,n):
        next = 0
        if len - 1 == 0:
            return n - 1
        if len - 1 > 0:
            if button[n].collidepoint(pos):
                btn = []
                btn.append(button[0])
                btn.append(n)

                return btn
                        
            return self.check_button_click(button,len - 1,pos,n+1) 

    def popupBox(self,msg):
        popup = tk.Tk()
        popup.wm_title("!")
        label = tk.Label(popup, text=msg, font=("Verdana",12))
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Oke", command=popup.destroy)
        B1.pack()
        popup.mainloop()
    
    def load_data(self,HS_file):
        
        sdir = path.dirname(__file__)
        with open(path.join(sdir, HS_file), 'r+') as f:
            try:
                return int(f.read())

            except:
                return  0
