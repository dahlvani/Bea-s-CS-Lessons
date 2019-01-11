
import pygame, random
from pygame.locals import *

def drawGround(window):
    """
    load all images into a list
    """
    images = [pygame.image.load("grass.gif").convert(),
              pygame.image.load("road.gif").convert(),
              pygame.image.load("gtoroad.gif").convert(),
              pygame.image.load("rtograss.gif").convert()]



    """
    Create variables to keep track of where to
    draw the grass
    """
    xVARIABLE = 0
    yVARIABLE = 0



    """
    Outer loop runs as long as x is
    not past the right edge of the screen
    """



    #will not run until loops are added in
    #will throw a fit about the indentation

    """
    Inner loop runs as long as y is
    not past the bottom edge of the screen
    Use the y position to determine which tile to draw
    Increase the y
    """
    while(xVARIABLE < 800):
        while(yVARIABLE < 600):
            if(yVARIABLE <= 50):
                window.blit(images[0], (xVARIABLE,yVARIABLE))
                yVARIABLE += 50
            elif(yVARIABLE == 100):
                window.blit(images[2], (xVARIABLE,yVARIABLE))
                yVARIABLE += 50
            elif(yVARIABLE < 500):
                window.blit(images[1], (xVARIABLE,yVARIABLE))
                yVARIABLE += 50
            elif(yVARIABLE == 500):
                window.blit(images[3], (xVARIABLE,yVARIABLE))
                yVARIABLE += 50
            else:
                window.blit(images[0], (xVARIABLE,yVARIABLE))
                yVARIABLE += 50

        xVARIABLE += 50
        yVARIABLE = 0


    """
    Increase the x and reset the y
    """
