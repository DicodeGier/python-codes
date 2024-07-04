class Customer:
    def __init__(self):
        self.total = 0
        self.discount = 0
        self.shops = []

    def addPurchase(self, amount, shop_number):
        self.total += amount
        if shop_number not in self.shops:
            self.shops.append(shop_number)

    def discountReached(self):
        while self.total >= 100 and len(self.shops) >= 3:
            self.discount += 10
            self.total -= 100

