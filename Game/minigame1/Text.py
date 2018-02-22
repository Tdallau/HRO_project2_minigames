import pygame
from pygame import *

class Text():
    
    def __init__(self, text, fonts, size, color):
        self.text = text
        self.fonts = fonts
        self.size = size
        self.color = color
        self._cached_fonts = {}
        self._cached_text = {}
        

    def create_text(self):
        key = '|'.join(map(str, (self.fonts, self.size, self.color, self.text)))
        image = self._cached_text.get(key, None)
        if image == None:
            font = self.get_font(self.fonts, self.size)
            image = font.render(self.text, True, self.color)
            self._cached_text[key] = image
        return image

    def get_font(self,font_preferences,size):

        key = str(font_preferences) + '|' + str(size)
        font = self._cached_fonts.get(key, None)
        if font == None:
            font = self.make_font(font_preferences, size)
            self._cached_fonts[key] = font
        return font
            
    def make_font(self,fonts,size):
        available = pygame.font.get_fonts()
        # get_fonts() returns a list of lowercase spaceless font names 
        choices = map(lambda x:x.lower().replace(' ', ''), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        return pygame.font.Font(None, size)
       
        