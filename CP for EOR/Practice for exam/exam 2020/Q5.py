class Charity:
    def __init__(self, _name, _balance = 0):
        self.name = _name
        self.donors = {}
        self.__balance = _balance

    def __str__(self):
        return "Charity: {}; Donations: ${}".format(self.name, self.__balance)

    def donateForFirstTime(self, first_name, amount):
        if amount >=0:
            self.__balance += amount
            self.donors[first_name] = amount
        else:
            raise Exception("Donations must be a positive amount")

    def spend(self, withdrawal):
        if withdrawal <= self.__balance:
            self.__balance -= withdrawal
            return("Spending amount: ${}").format(withdrawal)
        else:
            return("Insufficient funds to spend!")

    def __iadd__(self, name, other=5):
        self.donors[name] += other
        self.__balance += other 
        return self

    @property
    def donor_names(self):
        string = ''
        for item in self.donors:
            string = string + item + ','
        return string


myChar = Charity("Friends for Life")
print(myChar.name=="Friends for Life" and myChar.donors=={}) #0.1 points if true
print(myChar._Charity__balance==0) #0.1 points if true
print(str(myChar)=="Charity: Friends for Life; Donations: $0") #0.2 points if true
myChar.donateForFirstTime("Amin",10)
myChar.donateForFirstTime("Arash",20)
print(myChar._Charity__balance==30) #0.1 points if true
print(myChar.donors=={'Amin': 10, 'Arash': 20}) #0.1 points if true
try:
    myChar.donateForFirstTime("John",-12) #trying to donate a negative number is blocked!
    message=""
except Exception as ex:
    message=str(ex)
print(message=="Donations must be a positive amount")  #0.1 points if true
s=myChar.spend(300)  #trying to spend more than balance is blcoked!
print(myChar._Charity__balance==30 and s=="Insufficient funds to spend!") #0.2 points if true
s=myChar.spend(5)
print(myChar._Charity__balance==25 and s=="Spending amount: $5") #0.2 points if true
myChar+="Amin"  #Assume Amin already exists in the dictionary and donates the default $5
print(myChar.donors=={'Amin': 15, 'Arash': 20} and myChar._Charity__balance==30) #0.2 points if true
print(myChar.donor_names=='Amin,Arash,')  #0.2 points if True
