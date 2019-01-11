
import pygame
from pygame.locals import *


# Create a class called Walker
class Walker:
    # Create a constructor method that sets self.x to newX,
    # self.y to newY and loads the image "dude.gif" into self.img
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("dude.gif")


    # draw the image on the surface
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))


    def moveLeft(self):
        # Change x so that the object can move left
        if self.x > 10:
            self.x = self.x - 20


    def moveRight(self):
        # Change x so that the object can move right
        if self.x < 745:
            self.x = self.x + 20


    def moveUp(self):
        # Change y so that the object can move up
        if self.y > 10:
            self.y = self.y - 20


    def moveDown(self):
        # Change y so that the object can move down
        if self.y < 540:
            self.y = self.y + 20


    #This method returns a rectangle - (x, y, width, height)
    #that represents the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
