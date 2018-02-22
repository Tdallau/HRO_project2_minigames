#Author: Fatima Abukar
#Pygame Simplified, API version II
import pygame
from pygame import *
pygame.init()
pygame.mixer.init()


#Sound class, so sound can be addded to a game
class Sound(object):

    #Initialise global variables in constructor 
    def __init__(self):
        self.sound = None
        
    #set the file name of the sound    
    def set_sound(self,filename):
        self.sound =pygame.mixer.Sound(filename)
        
    #play the sound    
    def play(self):
        self.sound.play()

    #pause the sound    
    def pause(self):
        self.sound.pause()
        
    #stop the sound   
    def stop(self):
        self.sound.stop()
        
    #set the volume of the sound   
    def set_volume(self, volume):
        self.sound.set_volume(volume)
