import sys
import random
import math
import os
import pygame
from pygame import time
from pygame.locals import *

# Moving object with mass
class Moon(pygame.sprite.Sprite):
    def __init__(self, pos, v, m, imgpath):
        self.G = 0,000006 # This value allows to drop the 10E6 factor in mass values
        self.pos = pos
        self.mass = m
        self.speed = v
        self.acc = (0, 0)
        self.force = (0, 0)
        self.image = pygame.image.load(imgpath)
        self.rect = self.image.get_rect().move(pos)
    def tick(self, group):
        fx = 0
        fy = 0
        f = 0
        for obj in group:
            d = sqrt(pow((self.pos[0]-obj.pos[0]), 2) + pow((self.pos[0]-obj.pos[0]), 2))
            f = G*(self.mass *obj.mass)/(pow(d, 2))
            fx += f * ((self.pos[0]-obj.pos[0]))
        
        self.acc = self.mass / self.force 
        self.speed += self.acc
        self.pos += self.speed
        self.rect = self.rect.move(pos)
    def impact(self):
        self.acc = (0, 0)
        self.speed = (0,0)
        self.force = (0, 0)

# Fixed object generating gravity field    
class Planet(pygame.sprite.Sprite):
    def __init__(self, pos, m, imgpath):
        self.pos = pos
        self.mass = m
        self.image = pygame.image.load(imgpath)
        self.rect = self.image.get_rect().move(pos)
    def tick(self):
        self.pos = self.pos
        
        
        
def write(text, font, size, color, posx, posy):
    font = pygame.font.Font(font, size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    if posx:
        textpos.centerx = posx
    if posy:
        textpos.centery = posy
    return {"surface" : text, "rect" : textpos}


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Gravity')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    bgcolor = (250, 250, 200)
    background.fill(bgcolor)
    screen.blit(background, (0, 0))

    text = write('Gravity', None, 50, (0,0,0), background.get_rect().centerx, background.get_rect().centery)
    screen.blit(text["surface"], text["rect"])

    imgpath = 'dot.png'
    earth = Planet((background.get_rect().centerx, background.get_rect().centery), 6, imgpath)
    moon = Moon((200,100), (0, 0), 1, imgpath)






    while 1:
            n += 1          # actually tick does not work for me, so it's orribly patched :(
            if n == 499999: #
                n = 0       #
                for event in pygame.event.get():
                    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                        return
                    if event.type == KEYDOWN and event.key == K_f:
                        fireball(ispeed, balls) 







    return

if __name__ == '__main__': main()

