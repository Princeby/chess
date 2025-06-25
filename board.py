from piece import Pawn, Rook, Knight, Bishop, Queen, King

class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col    
        self.piece = None
    
    def isEmpty(self):
        return self.piece is None
    
    def setPiece(self, piece):
        self.piece = piece

    def getPiece(self):
        return self.piece
    
    def __repr__(self):
        return f"Square({self.row}, {self.col}, {self.piece})"
    
class Board:
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

        if from_square.isEmpty():
            print("No piece to move.")
            return False
        
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