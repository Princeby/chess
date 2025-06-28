class GameState:
    def __init__(self):
        self._turn = "white"
        self._game_over = False
    
    def getTurn(self):
        return self._turn
    
    def setTurn(self, turn : str):
        if turn.lower() not in ["white", "black"]:
            raise ValueError("Turn must be 'white' or 'black'")
        self._turn = turn

    def switchTurn(self):
        self._turn = "black" if self._turn == "white" else "white"

    def isGameOver(self):
        return self._game_over
    
    def setGameOver(self, state: bool = True):
        if not isinstance(state, bool):
            raise TypeError("Game state must be a boolean")
        self._game_over = state