import pygame
from consts import *

class Tetromino:
    def __init__(self, t_type):
        self.type = t_type
        self.x = 5
        self.y = 1
        self.landed = False
        self.set_shape()
        
    def set_shape(self):
        if self.type == "I":
            self.shape = [(0,0),(0, 1), (0,2),(0,3)]
            self.color = red
        elif self.type == "J":
            self.shape = [(0,0),(0, 1), (0,2),(-1,2)]
            self.color = brown
        elif self.type == "L":
            self.shape = [(0,0),(0, 1), (0,2),(1,2)]
            self.color = yellow
        elif self.type == "S":
            self.shape = [(0,0),(-1,0 ), (-1,1),(-2,1)]
            self.color = green
        elif self.type == "Z":
            self.shape = [(0,0),(1,0), (1,1),(2,1)]
            self.color = purple
        elif self.type == "T":
            self.shape = [(0,0),(-1,0), (1,0),(0,1)]
            self.color = orange
        elif self.type == "O":
            self.shape = [(0,0),(1,0), (0,1),(1,1)]
            self.color = blue

    def update(self,board):
        self.y += 1
        
        
        for offset in self.shape:
            next_y = self.y + 1 + offset[1]
            next_x = self.x + offset[0]
            if next_y * TILE_SIZE >= WINDOW_HEIGHT:
                self.landed = True
                break
            elif 
            
            
    def draw(self,screen):
        for i in range(len(self.shape)):
            pygame.draw.rect(screen, self.color, ((self.x + self.shape[i][0]) * TILE_SIZE,(self.y + self.shape[i][1]) * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
        
        
        