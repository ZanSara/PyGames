#
# Just a boucing ball, to get used to PyGame

import sys
import random
import math
import os
import pygame
from pygame import time
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/do.gif')
        self.position = self.image.get_rect().move(0, 480)
        self.size= (self.image.get_width(), self.image.get_height())
        self.speed = speed
        self.time = 1
        self.acc = 0.5
    def update(self, screen):
        self.position = self.calcnewpos(screen)
    def calcnewpos(self, screen):
        """Simulate physics """
        self.time = self.time + 1
        newpos = self.position.move(self.speed)
        speed = list(self.speed)
        if newpos.left < 0:
            newpos.left = 0
            speed[0] *= -1
        if newpos.right > screen.get_width():
            self.kill()
        if newpos.top < 0:
            newpos.top = 0
            speed[1] *= -1
        if newpos.top >= screen.get_height() - 20:
            newpos.top = screen.get_height() - 20
            speed[1] = -speed[1] + (speed[1]*0.1)
        speed[0] += -speed[0]*0.005
        speed[1] += self.acc * self.time
        self.speed = speed
        return newpos
    def set_a(self, acc):
        self.acc = acc
    def set_speed(self, speed):
        self.speed = speed
    def get_size(self):
        print self.size
        return self.size



def fireball(ispeed, balls):
    #Simply creates a new ball in the 'balls' group
    balls.add(Ball(ispeed))
    
def write(text, font, size, color):
    # Returns a Surface containing your text
    font = pygame.font.Font(font, size)
    text = font.render(text, 1, color)
    return text

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Fire Balls')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    bgcolor = (250, 250, 200)
    background.fill(bgcolor)
    screen.blit(background, (0, 0))

    text = write('Ready?', None, 50, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    screen.blit(text, textpos)

    balls = pygame.sprite.Group()
    ispeed = (15, -60)
    fireball(ispeed, balls)
    
    dirty = pygame.Surface(balls.sprites()[0].get_size()).convert()
    dirty.fill(bgcolor)
    
    pygame.display.flip()
    time.wait(1000)
    text.fill(bgcolor)
    screen.blit(text, textpos)
    
    text = write('Press F to fire a ball, and q to quit', None, 25, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    screen.blit(text, textpos)
    
    #pygame.time.Clock.tick(25)
    n = 0
    while 1:
        n += 1          # actually tick does not work for me, so it's orribly patched :(
        if n == 499999: #
            n = 0       #
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
                    return
                if event.type == KEYDOWN and event.key == K_f:
                    fireball(ispeed, balls)
            #Recalculate the image to be displayed
            i = 0
            for b in balls.sprites():
                screen.blit(dirty, b.position)
                b.update(screen)
                screen.blit(b.image, b.position)
                
            screen.blit(text, textpos)
            pygame.display.flip()


if __name__ == '__main__': main()