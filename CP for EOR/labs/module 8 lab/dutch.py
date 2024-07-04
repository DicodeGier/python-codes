class Customer:
    def __init__(self, _name, _balance):
        self.name = _name
        self.balance = _balance

    def deposit1(self, amount):
        self.balance += amount

    def deposit2(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        else:
            return False

    def deposit3(self, amount):
        if amount >= 0:
            self.balance += amount
            return True, self.balance
        else:
            return False