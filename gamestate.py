class Gamestate:
    def __init__(self):
        self._turn = "Player One"
        self._state = False
    
    def getTurn(self):
        return self._turn
    
    def setTurn(self, turn : str):
        self._turn = turn

    def getStatus(self):
        return self._state
    
    def setStatus(self):
        self._state = True