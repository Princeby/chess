from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self, color):
        self.color = color
        self.pieceType = "Unknown"
        self._hasMoved = False
    
    def getColor(self):
        return self.color
    
    def getType(self):
        return self.pieceType
    
    @abstractmethod
    def getValidMoves(self, row, col):
        pass
    
    def markAsMoved(self):
        self._hasMoved = True

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "Pawn"
    
    def getValidMoves(self, row, col):
            direction = -1 if self.color == "white" else 1
            return [(row + direction, col)]

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "Rook"
    
    def getValidMoves(self, row, col):
        moves = []
        for i in range(8):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
        return moves

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "Bishop"
    def getValidMoves(self, row, col):
        moves = []
        for i in range(1, 8):
            if row + i < 8 and col + i < 8:
                moves.append((row + i, col + i))
            if row - i >= 0 and col - i >= 0:
                moves.append((row - i, col - i))
            if row + i < 8 and col - i >= 0:
                moves.append((row + i, col - i))
            if row - i >= 0 and col + i < 8:
                moves.append((row - i, col + i))
        return moves

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "Knight"

    def getValidMoves(self, row, col):
        deltas = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        moves = [(row + dr, col + dc) for dr, dc in deltas
                 if 0 <= row + dr < 8 and 0 <= col + dc < 8]
        return moves
    
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "Queen"
    
    def getValidMoves(self, row, col):
        # Combine rook and bishop logic
        moves = Rook(self.color).getValidMoves(row, col)
        moves += Bishop(self.color).getValidMoves(row, col)
        return moves

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.pieceType = "King"
    
    def getValidMoves(self, row, col):
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        moves.append((new_row, new_col))
        return moves

def test_pieces():
    pieces = [
        Pawn("white"),
        Rook("black"),
        Bishop("white"),
        Knight("black"),
        Queen("white"),
        King("black")
    ]

    start_row, start_col = 4, 4  # Center square (e5)
    for piece in pieces:
        moves = piece.getValidMoves(start_row, start_col)
        print(f"{piece.getType()} ({piece.getColor()}): {moves}")

test_pieces()
# Coding Assignment:
# Make Piece abstract with abstract method getValidMoves(board, position)
# How do I make a class abstract to ensure only those that inherit can get it
# Implement all piece classes: Rook, Bishop, Knight, Queen, King, Pawn
# Each piece implements its own movement logic in getValidMoves()
# Create a test that puts different pieces in an array and calls getValidMoves() on each
# generic = Piece('white')
# print(f'{generic.color} and {generic.getType()}')
white_pawn = Pawn('black')
print(f"{white_pawn.color} and {white_pawn.getType()}")