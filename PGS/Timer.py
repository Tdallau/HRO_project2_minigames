#Author: Fatima Abukar
#Pygame Simplified, API version II
import pygame,sys,os,random
import collections
from pygame.locals import *
pygame.init()

#Timer class, allows you to set the timer by incrementing or decrementing it
class Timer(object):

    #Initialise global variables in constructor 
    clock = pygame.time.Clock()
    seconds =0
    frame_count= 0
    frame_rate=30

    @classmethod
    def get_seconds(cls):
        return  Timer.seconds
        
    @classmethod 
    #set the timer buy decrementing it          
    def decrement_timer(cls, timer):
        total_seconds = Timer.frame_count // Timer.frame_rate
        # Use modulo (remainder) to get seconds
        Timer.seconds = total_seconds % timer
        Timer.frame_count -= 1
        Timer.clock.tick(Timer.frame_rate)

    @classmethod
    #set the timer buy incrementing it          
    def increment_timer(cls, timer):
        total_seconds = Timer.frame_count // Timer.frame_rate
        # Use modulo (remainder) to get seconds
        Timer.seconds = total_seconds % timer   
        Timer.frame_count += 1
        Timer.clock.tick(Timer.frame_rate)
