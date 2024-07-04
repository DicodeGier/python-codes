class BarOrder:
    def __init__(self, _drink, _price, _number = 1):
        self.drink = _drink.lower()
        self.price = _price
        self.number = _number

    def isAlcoholic(self):
        if self.drink == 'beer' or self.drink == 'wine':
            return True
        elif self.drink == 'coke' or self.drink == 'water':
            return False
        else:
            return None

    def getTotalItemPrice(self):
        return self.price * self.number

class BarOrderList:
    def __init__(self):
        self.list_orders = []

    def addBarOrder(self, _barorder):
        if _barorder.isAlcoholic() == None:
            return False
        self.list_orders.append(_barorder)
        return True

    def getTotal(self):
        total = 0
        for n in self.list_orders:
            total += n.getTotalItemPrice()
        return total

class BarCustomer:
    def __init__(self, given_name, given_age):
        self.name = given_name
        self.age = given_age
        self.bar_order_list = BarOrderList()

    def AllowedToDrink(self):
        if self.age >= 18:
            return True
        else:
            return False

    def addOrder(self, _barorder):
        if _barorder.isAlcoholic() == True and self.AllowedToDrink() == False:
            return False
        else:
            self.bar_order_list.addBarOrder(_barorder)
            return True


    