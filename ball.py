#ball
import pygame
import numpy as np
class Ball:
    RADIUS = 10


    def __init__(self, x, y, vx, vy, screen, fgcolor,bgcolor,angle):
        self.x = x
        self.y = y
        self.screen = screen
        self.fgcolor = fgcolor
        self.vx = vx
        self.vy = vy
        self.bgcolor = bgcolor
        self.angle = angle

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x,self.y), Ball.RADIUS)

    def collide(self):
       
        
        if self.y+Ball.RADIUS >= 458:# you could do the math so that velocity hits the border just right
            self.vy = -self.vy       # I just made an invisible border so that the ball doesn't delete the walls
        if self.x-Ball.RADIUS <= 22:
            self.vx = -self.vx
        if self.y-Ball.RADIUS <= 22:
            self.vy = -self.vy
        
    
    def update(self):
        self.show(self.bgcolor)
        self.collide()
        self.x = self.x + self.vx*np.cos(self.angle)
        self.y = self.y + self.vy*np.sin(self.angle)
        self.show(self.fgcolor)
        #todo make not collide