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
pygame.init()
clock = pygame.time.Clock() 
try:
    font = pygame.font.Font("./assets/font/CourierPrime-Bold.ttf", 36)  # Try loading an Arial font
except pygame.error:
    font = pygame.font.Font(None, 38)  # Fallback to default font

# Text to display
text_to_show = "GAME OVER"

# Render the text
text_surface = font.render(text_to_show, True, green)

# Get the rectangular area of the text surface
text_rect = text_surface.get_rect()

# Center the text on the screen
text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

class Game:
    tetrominos = []
    def __init__(self):
        
        self.quit = False
        self.board = Board()
        self.tetrominos  = []
        self.init_tetrominos()
        self.current_tetromino = self.get_random_tetromino()
        self.fast = False
        self.fall_speed = 1  # Tetromino falls 1 block per second (we'll control this with time)
        self.last_fall_time = time.time()
        self.fall = False
        self.game_over = False
        
    def get_random_tetromino(self):
        return random.choice(self.tetrominos)
        
    def process_input(self):
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
                        self.current_tetromino.rotate_clockwise(self.current_tetromino.shape,self.board)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.fast = False
                        self.fall_speed = slow_sleep
                        
    def start(self):
        
        while not self.quit:
            
            self.process_input()
            current_time = time.time()
            if current_time - self.last_fall_time >= self.fall_speed:
                self.fall = True  # Move down by one block
                self.last_fall_time = current_time
            else:
                self.fall = False

   
            
                # Your code to move right, etc.
            if not self.game_over:
                screen.fill((80,80,80))
                self.board.draw(screen)
                self.current_tetromino.update(self.board, self.fall)            
                self.current_tetromino.draw(screen)
                # if self.current_tetromino.landed:
                #     self.board.onTetrominoLanded(self.current_tetromino)
                #     self.last_fall_time = time.time()
                #     self.current_tetromino = self.get_random_tetromino()
                #     self.current_tetromino.start()
                #     if self.current_tetromino.collided(self.board):
                #         self.paused = True
                
                
                if self.current_tetromino.landed:
                    self.board.onTetrominoLanded(self.current_tetromino)
                    if self.check_game_over():  # New function to check game over
                        self.game_over = True
                    else:
                        self.last_fall_time = time.time()
                        self.current_tetromino = self.get_random_tetromino()
                        self.current_tetromino.start()
            else:
                pygame.draw.rect(screen,(128,128,128), text_rect)    
                screen.blit(text_surface, text_rect)
            pygame.display.update()
            # clock.tick(1) 
            pygame.time.Clock().tick(60)
            
            # time.sleep(fast_sleep if self.fast else slow_sleep)
            
    def check_game_over(self):
        # Create a new tetromino to check for collision
        temp_tetromino = self.get_random_tetromino()
        temp_tetromino.start()  # Reset its position

        return temp_tetromino.collided(temp_tetromino.shape,self.board)
    
    def init_tetrominos(self):
        self.tetrominos.append(Tetromino("I"))
        self.tetrominos.append(Tetromino("O"))
        self.tetrominos.append(Tetromino("S"))
        self.tetrominos.append(Tetromino("T"))
        self.tetrominos.append(Tetromino("Z"))
        self.tetrominos.append(Tetromino("J"))
        self.tetrominos.append(Tetromino("L"))
        


        

