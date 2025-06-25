
class Square:
    def __init__(self, position):
        self.position = position
        self.piece = None

    def isEmpty(self):
        return self.position is None
    
    def setPiece(self, piece):
        self.piece = piece
    
    def getPiece(self):
        return self.piece


