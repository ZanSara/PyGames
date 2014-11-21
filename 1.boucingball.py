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
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)



class Ball(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/do.gif')
        #area = pygame.display.get_surface()
        #self.area = area.get_rect()
        pos = pygame.image.load('images/do.gif').get_rect()
        self.position = pos.move(0, 480)
        self.size= (self.image.get_width(), self.image.get_height())
        self.speed = speed
        self.time = 1
        self.acc = 0.5
        self.active = 1
    def update(self, screen):
        newpos = self.calcnewpos(screen)
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
    def set_active(self, value):
        self.active = value
    def set_speed(self, vec):
        self.speed = vec
    def get_size(self):
        print self.size
        return self.size
        


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Bouncing Ball')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    bgcolor = (250, 250, 200)
    background.fill(bgcolor)

    # Display some text
    font = pygame.font.Font(None, 50)
    text = font.render("Ready?", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    #Create objects
    balls = pygame.sprite.Group()
    ball = Ball((9, -60))
    balls.add(ball)
    
    #Create the "dirty rects" background
    dirty = pygame.Surface(ball.get_size()).convert()
    dirty.fill(bgcolor)
    
    #Display the text and starts the game
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.wait(1000)
    text.fill(bgcolor)
    screen.blit(text, textpos)
    
    # Event loop
    #pygame.time.Clock.tick(25)
    n = 0
    while 1:
        n += 1          # actually tick does not work for me, so it's orribly patched :(
        if n == 499999: #
            n = 0       #
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            if abs(ball.speed[0]) < 1:
                time.wait(1000)
                return
            #Recalculate the image to be displayed
            screen.blit(dirty, ball.position)
            ball.update(screen)
            screen.blit(ball.image, ball.position)
            pygame.display.flip()


if __name__ == '__main__': main()