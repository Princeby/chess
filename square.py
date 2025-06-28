class Square:
    def __init__(self, row, col):
        self._row = row
        self._col = col    
        self._piece = None
    
    def isEmpty(self):
        return self._piece is None
    
    def setPiece(self, piece):
        self._piece = piece

    def getPiece(self):
        return self._piece
    
    def __repr__(self):
        return f"Square({self.row}, {self.col}, {self.piece})"


