class BarOrder:
    def __init__(self, _drink, _price, _number = 1):
        self.drink = _drink.lower()
        self.price = _price
        self.number = _number

    def isAlcoholic(self):
        if self.drink == "beer" or self.drink == 'wine':
            return True
        elif self.drink == 'coke' or self.drink == 'water':
            return False
        else:
            return None

    def getTotalItemPrice(self):
        total_price = int(self.price)*int(self.number)
        return total_price

class BarOrderList:
    pass

# from here I could not figure it out anymore
        
