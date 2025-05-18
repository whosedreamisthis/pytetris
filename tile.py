import pygame
from consts import *
class Tile:
    def __init__(self,color,x,y):
        self.color = color
        self.x = x
        self.y = y
        self.filled = False
    
    def draw(self,screen):
         pygame.draw.rect(screen, self.color, ((self.x) * TILE_SIZE + BOARD_OFFSET[0],self.y * TILE_SIZE + BOARD_OFFSET[1], TILE_SIZE - 1, TILE_SIZE - 1))