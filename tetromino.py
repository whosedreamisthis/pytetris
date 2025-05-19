import pygame
from consts import *
from board import Board

class Tetromino:
    def __init__(self, t_type):
        self.type = t_type
        self.original_position = (5,-1)
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

    def rotate_clockwise(self,shape,board):
        rotated_shape = []
        for x, y in shape:
            rotated_shape.append((-y, x))
            
        filled = self.collided(rotated_shape,board)
        
        if not filled:
            self.shape = rotated_shape
        

    def rotate_counter_clockwise(self,shape,board):
        rotated_shape = []
        for x, y in shape:
            rotated_shape.append((y, -x))
        # print("shape before",self.shape)
        # print("shape after",rotated_shape)
        filled = self.collided(rotated_shape, board)
        
        if not filled:
            self.shape = rotated_shape
        
    
            
    def collided(self, shape, board):
        filled = False
        for offset in shape:
            next_x = self.x + offset[0]
            next_y = self.y + offset[1]

            # Boundary checks:
            if next_x < 0 or next_x >= len(board.tiles) or next_y >= len(board.tiles[0]):
                return True  # Collision with boundary

            if next_y >= 0 and board.tiles[next_x][next_y].filled:
                filled = True
                break
        return filled

        
    def move_right(self):
        self.x += 1
        for offset in self.shape:
            next_y = self.y + offset[1]
            next_x = self.x + offset[0]
            if next_x  >= BOARD_WIDTH:
                self.x -= 1
    def set_shape(self):
        if self.type == "I":
            self.shape = [(0,0),(0, 1), (0,-1),(0,-2)]
            self.color = red
        elif self.type == "J":
            self.shape = [(0,0),(-1,1), (0,1),(0,-1)]
            self.color = brown
        elif self.type == "L":
            self.shape = [(0,0),(1,1), (0,1),(0,-1)]
            self.color = yellow
        elif self.type == "S":
            self.shape = [(0,0),(1,0 ), (0,1),(-1,1)]
            self.color = green
        elif self.type == "Z":
            self.shape = [(0,0),(-1,0), (0,1),(1,1)]
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
            if next_y >= BOARD_HEIGHT:
                self.landed = True
                break
            if tiles[next_x][next_y].filled:
                self.landed = True
                break
            
            
    def draw(self,screen):
        for i in range(len(self.shape)):
            pygame.draw.rect(screen, self.color, ((self.x + self.shape[i][0]) * TILE_SIZE + BOARD_OFFSET[0],(self.y + self.shape[i][1]) * TILE_SIZE + BOARD_OFFSET[1], TILE_SIZE - 1, TILE_SIZE - 1))
        
        
        