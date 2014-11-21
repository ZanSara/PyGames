#
# Just a boucing ball, to get used to PyGame

try:
        import sys
        import random
        import math
        import os
        import pygame
        from pygame import time
        #from pygame import *
        from pygame.locals import *
        import cevent
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)


class Ball(pygame.sprite.Sprite, CEvent):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/do.gif')
        pos = pygame.image.load('images/do.gif').get_rect()
        self.position = pos.move(0, 480)
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
        #This time I set a different behavior for the screen borders
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
        vxf = speed[0]-speed[0]*0.005
        vyf = speed[1] + self.acc * self.time
        self.speed = (vxf,vyf)
        return newpos
    def set_a(self, acc):
        self.acc = acc
    def set_speed(self, vec):
        self.speed = vec
    def get_size(self):
        print self.size
        return self.size

        
def fireball():
    #Create the group and the first ball
    balls = pygame.sprite.Group()
    ball = []
    ball.append(Ball((15, -60)))
    balls.add(ball)

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Many Bouncing Balls')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    bgcolor = (250, 250, 200)
    background.fill(bgcolor)

    font = pygame.font.Font(None, 50)
    text = font.render("Ready?", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    fireball()
    
    dirty = pygame.Surface(ball[0].get_size()).convert() #knowing that all balls are equal
    dirty.fill(bgcolor)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.wait(1000)
    text.fill(bgcolor)
    screen.blit(text, textpos)
    
    #pygame.time.Clock.tick(25)
    n = 0
    while 1:
        n += 1          # actually tick does not work for me, so it's orribly patched :(
        if n == 499999: #
            n = 0       #
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            #Recalculate the image to be displayed
            i = 0
            for b in ball:
                i += 1
                screen.blit(dirty, b.position)
                b.update(screen)
                screen.blit(b.image, b.position)
                if b.position.x > 200 and b.position.x <222:
                    ball.append(Ball((15, -60)))
            pygame.display.flip()


if __name__ == '__main__': main()