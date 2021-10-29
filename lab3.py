import pygame
from paddle import Paddle
from ball import Ball
import random
def main():

    pygame.init()

    pygame.display.set_caption("Lab3 - Luis Gjuraj")
    WIDTH = 800
    HEIGHT = 480
    VELOCITY = 5
    FPS = 120
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((255,0,0))
    pygame.display.update()
    bgcolor = pygame.Color("Red")
    fgcolor = pygame.Color("Purple")
    #WALLS
    wcolor = pygame.Color("purple")
    BORDER = 20
    #top wall
    # Rect((left, top), (width, height)) -> Rect
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)) )
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER,HEIGHT)) )
    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((20,460),(780,20)) )
    # pygame.draw.rect(screen, wcolor, pygame.Rect(?) )

    #Ball init
    x0=WIDTH - Ball.RADIUS
    y0= HEIGHT//2
    vx0 = -VELOCITY
    vy0 = VELOCITY
    #TODO randomly pick a 45^ angle
    angles = [-45, 0, 45]
    angle = random.choice(angles)
    b0 = Ball(x0,y0,vx0,vy0,screen,fgcolor, bgcolor, angle)
    b0.show(fgcolor)
    

    pygame.display.update()
    

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        b0.update()
            
if __name__=="__main__":
    # call the main function
    main()

    #GIT + GIF, put in README that shows collision and random start