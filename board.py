from piece import Pawn, Rook, Knight, Bishop, Queen, King
from square import Square
from normal_move_validator import NormalMoveValidator


class Board:
    def __init__(self, validator=None):
        self._validator = validator or NormalMoveValidator()
        self.squares = [[Square(r, c) for c in range(8)] for r in range(8)]
        self.initialize()

    def getSquare(self, row, col):
        if self.isValidPosition(row, col):
            return self.squares[row][col]
        return None

    def isValidPosition(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def movePiece(self, from_row, from_col, to_row, to_col):
        from_square = self.getSquare(from_row, from_col)
        to_square = self.getSquare(to_row, to_col)

        if from_square is None or from_square.isEmpty():
            raise ValueError("No piece to move")

        piece = from_square.getPiece()

        if not self._validator.isValidMove(piece, from_row, from_col, to_row, to_col, self):
            raise ValueError("Invalid move")

        to_square.setPiece(piece)
        from_square.setPiece(None)
        piece.markAsMoved()
        return True

    def initialize(self):
        for col in range(8):
            self.getSquare(1, col).setPiece(Pawn("black"))
            self.getSquare(6, col).setPiece(Pawn("white"))
        
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, pieceClass in enumerate(order):
            self.getSquare(0, col).setPiece(pieceClass("black"))
            self.getSquare(7, col).setPiece(pieceClass("white"))

    def printBoard(self):
        for row in self.squares:
            print(" | ".join(
                s.getPiece().getType()[0] if not s.isEmpty() else "." for s in row
            ))

    def __init__ (self):
        outer = []
        for row in range(8):
            inner = []
            for col in range(8):
                inner.append(Square(row, col))
            outer.append(inner)
        self.squares = outer
        self.initialize()
        

    def getSquare(self,row, col):
        if self.isValidPosition(row, col):
            return self.squares[row][col]
        return None
    
    def movePiece(self, from_row, from_col, to_row, to_col):
        if not (self.isValidPosition(from_row, from_col) and self.isValidPosition(to_row, to_col)):
            print("Invalid mode")

        from_square = self.getSquare(from_row, from_col)
        to_square = self.getSquare(to_row, to_col)

        moving_piece = from_square.getPiece()
        target_piece = to_square.getPiece()

        if not from_square or from_square.isEmpty():
            raise ValueError("No piece to move")
        
        if target_piece and target_piece.getColor() == moving_piece.getColor():
            raise ValueError("Cannot move to the same color type")
        
        valid_moves = moving_piece.getValidMoves(from_row, from_col, self)
        if (to_row, to_col) not in valid_moves:
            raise ValueError("Invalid move")

        if from_square.isEmpty():
            raise ValueError("No piece to move.")
        
        to_square.setPiece(from_square.getPiece())
        from_square.setPiece(None)
        return True
    
    def isValidPosition(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def initialize(self):
        for col in range(8):
            self.getSquare(1 ,col).setPiece(Pawn("black"))
            self.getSquare(6, col).setPiece(Pawn("white"))
        
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, pieceClass in enumerate(order):
            self.getSquare(0,col).setPiece(pieceClass("black"))
            self.getSquare(7,col).setPiece(pieceClass("white"))

    def printBoard(self):
        for row in self.squares:
            print(" | ".join(p.getPiece().getType()[0] if not p.isEmpty() else "." for p in row))

board = Board()


board.printBoard()