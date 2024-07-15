#Import Classes
import sys

import pygame

from const import *
from src.game import Game


def draw_chessboard(screen):
  for x in range(8):
      for y in range(8):
          rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
          color = WHITE if (x + y) % 2 == 0 else BLACK
          pygame.draw.rect(screen, color, rect)

class Main:

  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game")
    self.game = Game()
    

  def run(self):
    running = True
    screen = self.screen
    game = self.game
    
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      game.show_chess_board(screen)
      
      pygame.display.flip()
      pygame.display.update()
    pygame.quit()
      

main = Main()
main.run()
    