from abc import ABC, abstractmethod

class MoveValidator(ABC):
    @abstractmethod
    def isValidMove(self, piece, from_row, from_col, to_row, to_col, board):
        pass