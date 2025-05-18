import pygame
from tile import Tile
from consts import *

class Board:
    def __init__(self):
        self.tiles = []
               
        for x in range(BOARD_WIDTH):
            self.tiles.append([])
            for y in range(BOARD_HEIGHT):
                self.tiles[len(self.tiles) - 1].append(Tile(black,x,y))
                
        if GOD_MODE:
            self.god_mode_full_lines()
        
        self.process_full_lines()  
            
                
         
    def onTetrominoLanded(self, tetronimo):
        for offset in tetronimo.shape:
            x = tetronimo.x + offset[0]
            y = tetronimo.y + offset[1]
            self.tiles[x][y].color = FILLED_TILE_COLOR
            self.tiles[x][y].filled = True
        
        self.process_full_lines()    
        # print("onTetrominoLanded",tetronimo)
    
    def god_mode_full_lines(self):
        for x in range(BOARD_WIDTH):
            self.tiles[x][15].filled = True
            self.tiles[x][15].color = white
                
        
    def process_full_lines(self):
        lines_to_delete = []
        for y in range(BOARD_HEIGHT):
            line_filled = True
            for x in range(BOARD_WIDTH):
                if not self.tiles[x][y].filled:
                    line_filled = False
                    break
            if line_filled:
                lines_to_delete.append(y)
          
        lines_to_delete.sort(reverse=True)
        num_lines_cleared = 0
        for y_to_delete in lines_to_delete:
            num_lines_cleared += 1
             # Remove the full line
            for x in range(BOARD_WIDTH):
                self.tiles[x].pop(y_to_delete)
                 # Insert a new empty tile at the top
                self.tiles[x].insert(0, Tile(black, x, 0))
                 # Update y coordinates of all tiles in the column
                for i in range(len(self.tiles[x])):
                    self.tiles[x][i].y = i
        print("num_lines_cleared", num_lines_cleared)
        return num_lines_cleared      
        # for y in lines_to_delete:
        #     for x in range(10):
        #         self.tiles[x][y].filled = False
        #         self.tiles[x][y].color = red
                
            
            
    
    def draw (self,screen):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                self.tiles[x][y].draw(screen)
                
    def get_tiles(self):
        return self.tiles