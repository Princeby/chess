# Create Player class
# Properties: color, capturedPieces list
# Methods: addCapturedPiece(), getCapturedPieces()
# Implement board initialization with pieces in starting positions
from typing import Optional, List

from piece import Piece, Pawn, Rook

class Player:
    def __init__ (self, color, capturedPieces: Optional[List[Piece]] = None):
        self.color = color
        self.capturedPieces = capturedPieces if capturedPieces is not None else []
    
    def addCapturedPiece(self, piece: Piece):
        self.capturedPieces.append(piece)
    
    def getCapturedPieces(self):
        return self.capturedPieces
    
    def __repr__(self):
        return f"Player({self.color}, Captured: {[p.getType() for p in self.capturedPieces]})"

player_one = Player("white")
player_two = Player("black")

captured = Pawn("black")
captured_two = Rook("black")
player_one.addCapturedPiece(captured)
player_one.addCapturedPiece(captured_two)

print(player_one)