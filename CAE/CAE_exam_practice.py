class Garage:
    def __init__(self, numberLevel, spacePerLevel):
        self.parkingSpace = [[0 for i in range(numberLevel)] for j in range(spacePerLevel)]
        self.numberAvailable = numberLevel*spacePerLevel

    def chechAvailability(self,level,place):
        if self.parkingSpace[level-1][place-1] == 0:
            return "position is available"
        else:
            return "position is not available"

    def parking(self,level,place):
        if self.parkingSpace[level-1][place-1] == 1:
            return "position not available"
        else:
            self.parkingSpace[level-1][place-1] == 1
            self.numberAvailable -= 1

    def printGarage(self):
        for i in range(len(self.parkingSpace)):
            print(self.parkingSpace[i])

    def numberAvailability(self):
        return self.numberAvailable