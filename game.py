import pygame
import time
import random
from tile import Tile
from board import Board
from consts import *
from tetromino import Tetromino

white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock() 

class Game:
    tetrominos = []
    def __init__(self):
        pygame.init()
        self.quit = False
        self.board = Board()
        self.tetrominos  = []
        self.init_tetrominos()
        self.current_tetromino = self.get_random_tetromino()
        
    def get_random_tetromino(self):
        return random.choice(self.tetrominos)
        
    def start(self):
        
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
            screen.fill(white)
            self.board.draw(screen)
            self.current_tetromino.update()            
            self.current_tetromino.draw(screen)
            if self.current_tetromino.landed:
                self.current_tetromino = self.get_random_tetromino()
                self.current_tetromino.start()
            

            pygame.display.update()
            # clock.tick(60)
            time.sleep(0.1)
            
    def init_tetrominos(self):
        self.tetrominos.append(Tetromino("I"))
        self.tetrominos.append(Tetromino("O"))
        self.tetrominos.append(Tetromino("S"))
        self.tetrominos.append(Tetromino("T"))
        self.tetrominos.append(Tetromino("Z"))
        self.tetrominos.append(Tetromino("J"))
        self.tetrominos.append(Tetromino("L"))
        


        

