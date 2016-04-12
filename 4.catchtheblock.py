
# A little 'labirinth' game, to learn how to animate sprites 

import sys
import random
import math
import os
import pygame
from pygame import time
from pygame.locals import *



class Hero(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        self.surface = pygame.image.load('images/blackball.png')
        self.rect = self.surface.get_rect().move(100, 100)
        print self.rect
        print "---------------"
    def update(self, vec, screenwidth, screenheight):
        print self.rect.x, self.rect.y
        pos = self.rect
        pos.left += vec[0]
        pos.top += vec[1]
        if pos.right > screenwidth:
            pos.right = screenwidth
        if pos.top < 0:
            pos.top = 0
        if pos.left < 0:
            pos.left = 0 
        if pos.bottom > screenheight:
            pos.bottom = screenheight
        self.rect = pos
    def die(self):
        self.surface = pygame.image.load('images/blackball-die.gif')
        time.wait(500)
        self.kill()
    def get_size(self):
        width = self.surface.get_rect().width
        height = self.surface.get_rect().height
        return tuple([width, height])
        
class Block(pygame.sprite.Sprite):
    def __init__(self):
        self.surface = pygame.image.load('images/redbox.gif.png')
        self.position = (30, 30) #(RANDOM1, RANDOM2)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().move(self.position)
    def update(self):
        vec = (0,0)#(RANDOM1, RANDOM2)
        pos = self.position
        pos[0] += vec[0]
        pos[1] += vec[1]
        self.position = pos
        
        
        
def write(text, font, size, color, posx, posy):
    # Returns a Surface containing your text
    font = pygame.font.Font(font, size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    if posx:
        textpos.centerx = posx
    if posy:
        textpos.centery = posy
    return {"surface" : text, "rect" : textpos}
        
def main():
    # Intro
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Catch The Block')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    bgcolor = (250, 250, 200)
    background.fill(bgcolor)
    screen.blit(background, (0, 0))

    text = write('Ready?', None, 50, (0,0,0), background.get_rect().centerx, background.get_rect().centery)
    screen.blit(text["surface"], text["rect"])

    # Init the game
    heroes = pygame.sprite.Group()
    hero = Hero(100, 100)
    pygame.sprite.Sprite.__init__(hero)
    heroes.add(hero)
    
    dirty = pygame.Surface(heroes.sprites()[0].get_size()).convert()
    dirty.fill(bgcolor)
    
    pygame.display.flip()
    time.wait(1000)
    text["surface"].fill(bgcolor)
    screen.blit(text["surface"], text["rect"])
    
    text = write('Hit the block moving the ball!', None, 25, (0,0,0), background.get_rect().centerx, background.get_rect().y)
    screen.blit(text["surface"], text["rect"])
    
    vec=[0,0]
    
    #pygame.time.Clock.tick(25)
    n = 0
    while 1:
        n += 1          # actually tick does not work for me, so it's orribly patched :(
        if n == 499999: #
            n = 0       #
            vx=0
            vy=0
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    return
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        vy=-2
                    elif event.key == K_DOWN:
                        vy=2
                    elif event.key == K_LEFT:
                        vx=-2
                    elif event.key == K_RIGHT:
                        vx=2
                    print vx, vy , " - " , hero.surface.get_rect()
            #Recalculate the image to be displayed
            screen.blit(dirty, [hero.rect.x, hero.rect.y])
            hero.update([vx, vy], screen.get_rect().width, screen.get_rect().height)
            screen.blit(hero.surface, [hero.surface.get_rect().x, hero.surface.get_rect().y])
                
            screen.blit(text["surface"], text["rect"])
            pygame.display.flip()


if __name__ == '__main__': main()