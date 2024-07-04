from pickle import FALSE, TRUE


class bug:
    def __init__(self, _initialPosition = 0, _forward = TRUE):
        self.initialPosition = _initialPosition
        self.forward = _forward

    def turn(self):
        if self.forward == TRUE:
            self.forward = FALSE
        else:
            self.forward = TRUE

    
    def move(self):
        if self.forward == TRUE:
            self.initialPosition += 1
        else:
            self.initialPosition -= 1

    def getPosition(self):
        return(self.initialPosition)
