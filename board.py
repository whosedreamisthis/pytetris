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
         
    def onTetrominoLanded(self, tetronimo):
        for offset in tetronimo.shape:
            x = tetronimo.x + offset[0]
            y = tetronimo.y + offset[1]
            self.tiles[x][y].color = FILLED_TILE_COLOR
            self.tiles[x][y].filled = True
        # print("onTetrominoLanded",tetronimo)
        
    def draw (self,screen):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                self.tiles[x][y].draw(screen)
                
    def get_tiles(self):
        return self.tiles