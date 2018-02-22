#Author: Fatima Abukar
#Pygame Simplified, API version II
import pygame
from pygame import*
pygame.init()

#This is the text class where all the methods for writing and drawing text to a world are
class Text(object):

    #Initialise global variables in constructor
    def __init__(self, World):
        self.font_name = "Arial"
        self.font_size=20
        self.myfont = pygame.font.SysFont(self.font_name, self.font_size)
        self.game_font = pygame.font.Font(None,30)
        self.colour_text = (0, 0, 0)
        self.world = World

    #set the text of your text object    
    def set_text(self,text):
         self.text_object= self.myfont.render(text,True,self.colour_text)
         
    #set the font name and size of the text object    
    def set_font(self,fontname,fontsize):
        self.font_name= fontname
        self.myfont = pygame.font.SysFont(self.font_name, fontsize)
        
    #set the colour of the text object
    def set_colour(self, red,blue,green):
        self.colour_text = (red,blue,green)
        
    #draw the text to the world  
    def draw_text(self, x,y):
        self.world.window.blit(self.text_object,[x,y])
