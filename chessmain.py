"""
this is the main driver file, it will handle the user input and display the live game.
"""

import pygame as p
from Chess import ChessEngine


WIDTH = HEIGHT = 512 
DIMENSION = 8 # DIMENSIONS OF A REAL CHESS BOARD IS 8*8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # FRAMES PER SECOND 
IMAGES = {}

'''
Initialize a global dictionary of images. this will be called once in the main
'''
def load_Images():
  pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
  for piece in pieces:
    IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
  # I can acess an image by typing, example: "images" ["wp"]

'''
the main driver for the code will handle user input + update graphics
'''
def main():
  p.init()
  screen = p.display.set_mode((WIDTH, HEIGHT))
  clock = p.time.Clock()
  screen.fill(p.color("white"))
  gs = ChessEngine.GameState()
  load_Images()
  running = True
  while running:
    for e in p.event.get():
     if e.type == p.QUIT:
       running = False
    clock.tick(MAX_FPS) 
    p.display.flip()
  
