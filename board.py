import pygame
from tile import Tile
from consts import *

class Board:
    def __init__(self):
        self.tiles = []
               
        for x in range(10):
            self.tiles.append([])
            for y in range(20):
                self.tiles[len(self.tiles) - 1].append(Tile(black,x,y))
         
        
    def draw (self,screen):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                self.tiles[x][y].draw(screen)