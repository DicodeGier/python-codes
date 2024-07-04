class Customer:
    def __init__(self, _name, _balance, _gender):
        self.__name = _name
        self.__balance = _balance
        self.__gender = _gender
    
    def __str__(self):
        return "Name={},balance={}".format(self.__name, self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise Exception("amount must be positive")

    def withdraw(self, _amount):
        if _amount <= self.__balance:
            self.__balance -= _amount
        else:
            raise Exception("amount must be higher than balance")

    def __iadd__(self, other):
        self.deposit(other)
        return self

    @property
    def Name(self):
        if self.__gender == 'male':
            return "Mr. {}".format(self.__name)
        elif self.__gender == 'female':
            return "Ms. {}".format(self.__name)

    @Name.setter
    def Name(self, newName):
        if len(newName) < 2:
            raise Exception("Name should have at least two characters!")
        else:
            self.__name = newName