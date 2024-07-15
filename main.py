#Import Classes
import sys

import pygame

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = WIDTH // 8
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
ROWS = 8
COLUMNS = 8

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
    

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      draw_chessboard(self.screen)
      pygame.display.flip()
    
    pygame.quit()
      

main = Main()
main.run()
    