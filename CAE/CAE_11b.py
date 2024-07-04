class Garage:
    def __init__(self, _numberLevel, _spacePerLevel):
        self.parkingspace = [[0 for i in range(_spacePerLevel)] for j in range(_numberLevel)]
        self.numberavailable = _numberLevel * _spacePerLevel

    def parking(self, level, space):
        if self.parkingspace[level-1][space-1] == 0:
            self.parkingspace[level-1][space-1] = 1
            self.numberavailable -= 1
        else:
            return("place already taken")

    def numberAvailability(self):
        return self.numberavailable

    def checkAvailability(self, level, place):
        if self.parkingspace[level-1][place-1] == 0:
            return("place is available")
        else:
            return("place is unavailable")

    def printGarage(self):
        for i in range(len(self.parkingspace)):
            print(self.parkingspace[i])


parkeergarage = Garage(3,3)
parkeergarage.parking(2,2)
parkeergarage.parking(1,3)
parkeergarage.parking(1,1)
print(parkeergarage.checkAvailability(2,2))
print(parkeergarage.numberAvailability())
parkeergarage.printGarage()