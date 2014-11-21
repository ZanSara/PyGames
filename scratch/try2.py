import os, sys
import pygame
import cevent
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class CApp(cevent.CEvent):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("images/g-redcircle.png")#.convert()
    def on_loop(self):
        pass
    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    def on_exit(self):
        self._running = False

def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
#def load_sound(name):
    #class NoneSound:
        #def play(self): pass
    #if not pygame.mixer:
        #return NoneSound()
    #fullname = os.path.join('data', name)
    #try:
        #sound = pygame.mixer.Sound(fullname)
    #except pygame.error, message:
        #print 'Cannot load sound:', wav
        #raise SystemExit, message
    #return sound
    
    
        
def main():
    

if __name__ == "__main__" :
    theGame = CApp()
    theGame.on_execute()