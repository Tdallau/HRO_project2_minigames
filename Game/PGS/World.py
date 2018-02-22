#Author: Fatima Abukar
#Pygame Simplified, API version II
import pygame,sys,os,random
import collections
from pygame.locals import *
from pygame import *
pygame.init()

#This is the world class where the actor lives in
class World(object):
    __singleton = None
    #Initialise global variables in constructor
    def __init__(self,width,height):
        self.window= pygame.display.set_mode((width,height))
        self.width=width
        self.height=height
        self.colour =(0,0,0)
        self.image = pygame.Surface([5, 5])

        #here is a singleton, only one instance of the world class can be created.       
        if World.__singleton:
            raise Exception("You can not have more than one World in a single game")
        World.__singleton = self
       
    #set the caption for the world    
    def set_caption(self,caption):
        pygame.display.set_caption(caption)
        
    #set the background of an image to tile    
    def set_tile_background(self, image):
        ##encase the user fails to upload a background image
        self.window.fill(self.colour)
        self.image=pygame.image.load(image)
        
    #set the background to users choice          
    def set_background(self, image):
         ##encase the user fails to upload a background image  
         self.window.fill(self.colour)
         self.image=pygame.image.load(image)
         
    #allows the user to change the background default fill to what they like    
    def set_backgrond_fill_colour(self,colour1,colour2,colour3):
        self.colour = (colour1,colour2,colour3)
        
    #set the window size to the size of the background image   
    def pack(self):
        background_size =self.image.get_size()
        self.window= pygame.display.set_mode(background_size)
        
    #draws a tiled background that is set   
    def draw_tile_background(self,imagex,imagey):
        for x in range(0, int(self.width/self.image.get_width()+1)):
            for y in range(0, int(self.height/self.image.get_height()+1)):
                self.window.blit(self.image,(x*imagex,y*imagey))
                
    #draws a background that is set    
    def draw_background(self,x,y):
        ##encase the user fails to upload a background image  
        self.window.fill(self.colour)
        self.window.blit(self.image,(x,y))
        
    #add an actor to the world               
    def add_actor(self,Actor,x,y):
        Actor.set_location(x,y)
        self.window.blit(Actor.image,(x,y))
        
    #draw actor to world   
    def draw_actor(self, Actor,x,y):
        self.window.blit(Actor.image,(x,y))
        
    #remove actor from world    
    def remove_actor(self, Actor):
        Actor.set_location(-1000,-1000)
        self.window.blit(self.image,(Actor.x,Actor.y))
        
    #update the world    
    def update(self):
        pygame.display.update()

    #quit the world        
    @classmethod
    def exit_game(cls):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            pygame.display.update()

    


    
