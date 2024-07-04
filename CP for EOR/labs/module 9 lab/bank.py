class Customer:
    def __init__(self, _name, _balance, _sex):
        self.__name = _name
        self.__balance = _balance
        self.__sex = _sex.lower()

    def __str__(self):
        return "Name={},balance={}".format(self.__name, self.__balance)

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            raise Exception("amount must be positive")
    
    def withdraw(self, amount):
        if amount >= self.__balance:
            raise Exception("amount must be higher than balance")
        else:
            self.__balance -= amount
    
    def __iadd__(self, other):
        self.deposit(other)
        return self

    @property
    def Name(self):
        if self.__sex == 'male':
            return "Mr. {}".format(self.__name)
        elif self.__sex == 'female':
            return "Ms. {}".format(self.__name)
    
    @Name.setter
    def Name(self,newname):
        if len(newname)<2:
            raise Exception("Name should have at least two characters!")
        self.__name=newname