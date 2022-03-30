"""
responsible for storing all the information about the state of the game, also will show the valid moves.
"""

class GameState():
  def _init_(self):
    # 8*8 2d list
    #b = black, w = white
    # "--" = empty space
    self.board = [
      ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
      ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["--", "--", "--", "--", "--", "--", "--", "--"],
      ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
    self.whitetomove = True
    self.moveLog = []