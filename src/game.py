#Responsible for all the game rendering methods
import pygame
from const import *

class Game:

  def __init__(self):
    pass

  #Show and Hide Methods for Renders

  def show_start_screen(self):
    pass

  def show_chess_board(self, screen):
    for x in range(8):
      for y in range(8):
          rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
          color = WHITE if (x + y) % 2 == 0 else BLACK
          pygame.draw.rect(screen, color, rect)