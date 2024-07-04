# import math
# from person import Person
# name = input('give name')
# weight = int(input('give weight'))
# lenght = float(input('give length'))
# person1 = Person(name, weight, lenght)
# BMI = person1.getBMI()
# print(BMI)

##########################################
class Student:

    def _init_(self, name, sid, GPAperyear, getTotalGPA):
        self.name = name
        self.sid = sid
        self.GPAperyear = GPAperyear
    
    def getTotalGPA(self):
        return sum(self.GPAperyear)/len(self.GPAperyear)

