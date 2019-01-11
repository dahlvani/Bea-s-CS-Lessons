
import pygame, random
from Enemy import *

class Enemies:
    def __init__(self):
        self.myList = [Enemy(0,200,25),
                       Enemy(750,270,-25),
                       Enemy(150,340,25),
                       Enemy(550,410,-25)]

    def drawAndCollision(self, screen, guy, changedrecs):
        """ Loop through the list of enemies """
        """  if guy collides with any enemies, return True  """
        """ Add the old position of the enemy to the array of rectangles to be redrawn  """
        """  Move and draw the enemies  """
        """ Add the old position of the enemy to the array of rectangles to be redrawn  """
        """  If the enemy has gone off the screen, remove it  """
        for x in self.myList:
            changedrecs.append(x.getRec())
            x.draw(screen)
            x.move()
            changedrecs.append(x.getRec())
            if(guy.collide(x)):
                return True
            if(x.getRec()[0] >= 800 or x.getRec()[0] <= 0):
                self.myList.remove(x)
            if(x.getRec()[1] >= 500 or x.getRec()[1] <= 100):
                self.myList.remove(x)



    """ create a new enemy and add it to the list of enemies """
    def addEnemy(self, x, y, speed):
        thingything = (25,-25)
        self.myList.append(Enemy(x, y, speed))


    """ Return the length of the list of enemies """
    def numEnemies(self):
        return len(self.myList)
