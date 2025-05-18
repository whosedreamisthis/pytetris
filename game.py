import pygame
import time
import random
from tile import Tile
from board import Board
from consts import *
from tetromino import Tetromino
slow_sleep = 1
fast_sleep = 0.01
fast = False
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
        self.fast = False
        self.fall_speed = 1  # Tetromino falls 1 block per second (we'll control this with time)
        self.last_fall_time = time.time()
        self.fall = False
        self.paused = False
        
    def get_random_tetromino(self):
        return random.choice(self.tetrominos)
        
    def start(self):
        
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                if event.type == pygame.KEYDOWN:  # Check for a key press
                    if event.key == pygame.K_LEFT:
                        self.current_tetromino.move_left()
                        print("Left arrow key pressed")
                    # Your code to move left, etc.
                    elif event.key == pygame.K_RIGHT:
                        self.current_tetromino.move_right()
                        print("Right arrow key pressed")
                    elif event.key == pygame.K_DOWN:
                        self.fast = True
                        self.fall_speed = fast_sleep
                    elif event.key == pygame.K_a:
                        self.current_tetromino.rotate_counter_clockwise(self.board)
                    elif event.key == pygame.K_d or event.key == pygame.K_UP:
                        self.current_tetromino.rotate_clockwise(self.board)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.fast = False
                        self.fall_speed = slow_sleep
            
            current_time = time.time()
            if current_time - self.last_fall_time >= self.fall_speed:
                self.fall = True  # Move down by one block
                self.last_fall_time = current_time
            else:
                self.fall = False

   
            
                # Your code to move right, etc.
            if not self.paused:
                screen.fill((80,80,80))
                self.board.draw(screen)
                self.current_tetromino.update(self.board, self.fall)            
                self.current_tetromino.draw(screen)
                if self.current_tetromino.landed:
                    self.board.onTetrominoLanded(self.current_tetromino)
                    self.last_fall_time = time.time()
                    self.current_tetromino = self.get_random_tetromino()
                    self.current_tetromino.start()
                    if self.current_tetromino.collided(self.board):
                        self.paused = True
                

            pygame.display.update()
            # clock.tick(1) 
            pygame.time.Clock().tick(60)
            
            # time.sleep(fast_sleep if self.fast else slow_sleep)
            
    def init_tetrominos(self):
        self.tetrominos.append(Tetromino("I"))
        self.tetrominos.append(Tetromino("O"))
        self.tetrominos.append(Tetromino("S"))
        self.tetrominos.append(Tetromino("T"))
        self.tetrominos.append(Tetromino("Z"))
        self.tetrominos.append(Tetromino("J"))
        self.tetrominos.append(Tetromino("L"))
        


        

