from move_validator import MoveValidator

class NormalMoveValidator(MoveValidator):
    def isValidMove(self, piece, from_row, from_col, to_row, to_col, board):
        # Board bounds check
        if not board.isValidPosition(to_row, to_col):
            return False
        
        # No piece at source
        if piece is None:
            return False

        # Don't capture own piece
        destination_piece = board.getSquare(to_row, to_col).getPiece()
        if destination_piece and destination_piece.getColor() == piece.getColor():
            return False
        
        # Check if target is in piece's valid move list
        valid_moves = piece.getValidMoves(from_row, from_col)
        return (to_row, to_col) in valid_moves