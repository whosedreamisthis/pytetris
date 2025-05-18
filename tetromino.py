import pygame
from consts import *
from board import Board

class Tetromino:
    def __init__(self, t_type):
        self.type = t_type
        self.original_position = (5,1)
        self.x = self.original_position[0]
        self.y = self.original_position[1]
        self.landed = False
        self.set_shape()
        
    def start(self):
        self.x = self.original_position[0]
        self.y = self.original_position[1]
        self.landed = False
        
    def move_left(self):
        self.x -= 1
        for offset in self.shape:
            next_y = self.y + offset[1]
            next_x = self.x + offset[0]
            
            if next_x < 0:
                self.x += 1

                 
        
    def move_right(self):
        self.x += 1
        for offset in self.shape:
            next_y = self.y + offset[1]
            next_x = self.x + offset[0]
            if next_x * TILE_SIZE >= WINDOW_WIDTH:
                self.x -= 1
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

    def update(self, board, fall):
        if not fall:
            return
        self.y += 1
        
        tiles = board.get_tiles()
        
        for offset in self.shape:
            next_y = self.y + 1 + offset[1]
            next_x = self.x + offset[0]
            if next_y * TILE_SIZE >= WINDOW_HEIGHT:
                self.landed = True
                break
            if tiles[next_x][next_y].filled:
                self.landed = True
            
            
    def draw(self,screen):
        for i in range(len(self.shape)):
            pygame.draw.rect(screen, self.color, ((self.x + self.shape[i][0]) * TILE_SIZE,(self.y + self.shape[i][1]) * TILE_SIZE, TILE_SIZE - 1, TILE_SIZE - 1))
        
        
        