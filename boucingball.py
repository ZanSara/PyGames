#
# First try with pygame
#

try:
        import sys
        import random
        import math
        import os
 #       import getopt
        import pygame
        from pygame import time
        from pygame import *
 #       from socket import *
        from pygame.locals import *
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

#Some classes
class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/do.gif')
        area = pygame.display.get_surface()
        self.area = area.get_rect()
        pos = pygame.image.load('images/do.gif').get_rect()
        self.position = pos.move(0, 480)
        #print self.position
        self.speed = speed
        self.time = 1
        self.acc = 0.5
        self.active = 1
    def update(self, screen):
        #print self.position
        newpos = self.calcnewpos(screen)
        #print newpos
        self.position = newpos
    def calcnewpos(self, screen):
        self.time = self.time + 1
        """Simulate physics """
        newpos = self.position.move(self.speed)
        speed = list(self.speed)
        if newpos.left < 0:
            newpos.left = 0
            speed[0] *= -1
        if newpos.right >= screen.get_width():
            newpos.right = screen.get_width()
            speed[0] *= -1
        if newpos.top < 0:
            newpos.top = 0
            speed[1] = -speed[1]
        if newpos.top >= screen.get_height() - 20:
            newpos.top = screen.get_height() - 20
            speed[1] = -speed[1] + (speed[1]/9)
        vxf = speed[0] - speed[0]/100
        vyf = speed[1] + self.acc * self.time
        self.speed = (vxf,vyf)
        #print self.time, speed, self.speed
        return newpos
    def new_a(self, acc):
        self.acc = acc
    def set_active(self, value):
        self.active = value
    def set_speed(self, vec)
        self.speed = vec


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('My Game')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 200))

    # Display some text
    font = pygame.font.Font(None, 50)
    text = font.render("Ready?", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #Create objects
    balls = pygame.sprite.Group()
    ball = Ball((9, -50))
    balls.add(ball)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.wait(1000)
    text.fill((250, 250, 200))
    background.blit(text, textpos)
    
    # Event loop
    #pygame.time.Clock.tick(25)
    n = 0
    while 1:
        n += 1
        if n == 699999:
            n = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            #Background blits always first, if needed
            screen.blit(background, (0, 0))
            ball.update(screen)
            screen.blit(ball.image, ball.position)

            pygame.display.flip()


if __name__ == '__main__': main()