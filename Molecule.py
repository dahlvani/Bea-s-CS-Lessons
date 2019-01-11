import math, random
import pygame
from pygame.locals import *

class Molecule:
    # class variable shared by all Molecules
    # if it changes in one Molecule, it changes in all Molecules
    speed = 10
    
    def __init__(self, newX, newY, rad,  direction):
        # (x,y) position
        self.x = newX
        self.y = newY
        
        # radius
        self.radius = rad
        
        # direction in degrees
        self.dir = direction % 360


    # Draw the molecule
    def draw(self,window):
        pygame.draw.circle(window, (0,0,200), (self.x,self.y), 10)

        
    def move(self):
        # get the amount to move on the x axis - xSpeed
        # and y axis - ySpeed
        (xSpeed, ySpeed) = self.moveInDirection()
        
        #change x by xSpeed
        self.x += xSpeed
        
        # check to see if the molecule has gone off 
        # the screen to the right or left
        if(self.x >= 790 or self.x <= 10):
            # undo the change to x
            self.x -= xSpeed
            # change the direction
            self.changeDirection()
        
        # change y by YSpeed
        self.y += ySpeed
        # check to see if the molecule has gone off 
        # the screen
        if(self.y >= 590 or self.y <= 10):
            # undo the change to y
            self.y -= ySpeed
            # change the direction
            self.changeDirection()
    
    

    # Increase speed for all Molecules
    # Change Molecule.speed
    def increaseSpeed(self):
        Molecule.speed += 10

    # Decrease speed for all Molecules
    def decreaseSpeed(self):
        Molecule.speed -= 10

    # Set Molecule speed to 10
    def resetSpeed(self):
        Molecule.speed = 10
    
    # Get Molecule Speed
    def getSpeed(self):
        return Molecule.speed

    
    

    # This turns the Molecule in a random direction
    # Do NOT change
    def changeDirection(self):
        self.dir = (self.dir+random.randint(100,150)) % 360

    
    # This determines how far to move on the x and y axis
    # to continue moving in the correct direction
    # Uses SOH CAH TOA
    # Do NOT change
    def moveInDirection(self):
        changeX = (int)(Molecule.speed * math.cos(math.radians(self.dir)))
        changeY = (int)(Molecule.speed * math.sin(math.radians(self.dir)))
        return [changeX,changeY]
    
    
