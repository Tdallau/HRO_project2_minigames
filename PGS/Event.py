#Author: Fatima Abukar
#Events class wrapper with many thanks to: http://www.pygame.org/wiki/InputWrapper?parent=CookBook

import pygame,sys
from pygame.locals import *
from pygame import *

         

class Event(object):
    pygame.init()
    #create global variables    
    m_DOWN = "isdown"
    k_DOWN= "isdown"
    m_UP="isup"
    k_UP="isup"
    MOTION = "motion"
    Quit = True
    butt = {1: "Button1", 2: "Button2", 3: "Button3"}
    events = {}
    keydict={}
    mousedict={}
    quitdict={}
    button_state = ()
    mouse_pos = ()
    sizex, sizey=0,0
    newkeyname =""
        
    #add a keyevent to dictionary     
    @classmethod
    def __add_keyDict(cls,event):
        if event.type ==KEYDOWN:
            Event.keydict.update({event.key:[event, Event.k_DOWN]})
        elif event.type==KEYUP:
            Event.keydict.update({event.key:[event, Event.k_UP]})

    #add an mouseevent to dictionary 
    @classmethod
    def __add_mouseDict(cls, event):
        if event.type == MOUSEBUTTONDOWN:
            Event.events.update({Event.butt[event.button]: [event, Event.m_DOWN]})
        elif event.type == MOUSEBUTTONUP:
            Event.events.update({Event.butt[event.button]: [event, Event.m_UP]})
        elif event.type == MOUSEMOTION:
            Event.events.update({MOUSEMOTION: [event, Event.MOTION]})
            
    #add a quitevent to dictionary     
    @classmethod      
    def __add_quitDict(cls,event):
        if event.type == pygame.QUIT:
            Event.quitdict.update({"exit": [event, Event.Quit]})
            
    #add a list of events to dictionaries
    @classmethod
    def __add_events(cls, events):
        for event in events:
            Event.__add_mouseDict(event)
            Event.__add_keyDict(event)
            Event.__add_quitDict(event)

    #set the keycodes    
    @classmethod
    def __set_code(cls,keyname):
        if keyname =="left":
            keyname = K_LEFT
        elif keyname =="right":
            keyname =K_RIGHT
        elif keyname== "up":
            keyname = K_UP
        elif keyname == "down":
            keyname = K_DOWN
        Event.newkeyname = keyname

    #update the mouse buttons and positions    
    @classmethod
    def __update_mouse(cls, buttons = (0,0,0), pos = (0,0)):
        Event.mouse_pos = pos
        Event.button_state = buttons

    #checks if the key is "quit" so you can exit the game      
    @classmethod
    def contains(cls, name):
        for names in Event.quitdict:
            if names == name:
                return name
            
    #quits the game      
    @classmethod
    def quit_game(cls):
        pygame.quit()
        sys.exit()
        
    @classmethod
    def exit_game(cls,game):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                pygame.quit()
            
            
    #checks if the key is at a down state and you have entered a keyname
    @classmethod
    def is_key(cls, keyname):
        Event.__set_code(keyname)
        event  = Event.keydict.get(Event.newkeyname)
        novalue = None
        if event == novalue:
            key_code = novalue
        else:
            key_code = event[1]
        if key_code == Event.k_DOWN:
            return True
        else:
            return False
        
    #checks if the key has been released
    @classmethod
    def key_up(cls, keyname):
        #get event               
        event = Event.keydict.get(keyname)
        novalue = None
        #if the event has no value        
        if event==novalue:
            #key has no value            
            key_code = novalue
        else:
            #key has state
            key_code = event[1]
        #if the key equals the state            
        if  key_code == Event.k_UP:
            #then the key has been released            
            return True
        #otherwise the key has not been released        
        return False
          
    #checks if the mouse has been pressed  
    @classmethod
    def mouse_down(cls, button):
    
        event = Event.events.get(button)
        novalue=None
        if event ==novalue:
            key_code = novalue
        else:
            key_code = event[1]
      
        if key_code == Event.m_DOWN:           
            return True
        else:
            return False

    #sets the image size for the cursor  
    @classmethod
    def set_CursorPosOnImage(cls,sizex,sizey):
        Event.sizex=sizex
        Event.sizey=sizey

    #sets the cursor position on the image  
    @classmethod   
    def set_MouseCursorPos(cls,x,y):
        ## the passed x and y is the position of the cursor.       
        x,y=Event.mouse_pos
        ##subtract half the image size from cursor x and y     
        x=x-Event.sizex/2
        y=y-Event.sizey/2
        ## set the new mouse position of x and y.     
        Event.mouse_pos=x,y
        
    #updates all the events    
    @classmethod
    def update(cls):
        clock = pygame.time.Clock()
        time_passed = clock.tick(60)
        Event.__update_mouse(pygame.mouse.get_pressed(),pygame.mouse.get_pos())
        Event.__add_events(pygame.event.get())
        x,y = Event.mouse_pos
        Event.set_MouseCursorPos(x,y)

    
 
   
