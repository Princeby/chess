# main.py
from board import Board

board = Board()
print("Initial Board:")
board.printBoard()

print("\nMoving white pawn from (6, 4) to (4, 4):")
board.movePiece(6, 4, 4, 4)

print("\nBoard After Move:")
board.printBoard()
