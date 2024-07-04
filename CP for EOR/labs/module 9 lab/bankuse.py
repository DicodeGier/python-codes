from bank2 import Customer

c1=Customer("Amin",0,"male")
print(c1._Customer__name=="Amin")
print(c1._Customer__balance==0)

c2=Customer("Jane",10,"female")
print(c2._Customer__name=="Jane")
print(c2._Customer__balance==10)


print(str(c1)=="Name=Amin,balance=0")
print(str(c2)=="Name=Jane,balance=10")

c1.deposit(5)
print(c1._Customer__balance==5)

try:
    c1.deposit(-1)
    print(False, " this line should not be executed as exception is raised")
except Exception as ex:
    print(str(ex)=="amount must be positive")


try:
    c1.withdraw(10)
    print(False, " this line should not be executed as exception is raised since withdrawal is higher than balance")
except Exception as ex:
    print(str(ex)=="amount must be higher than balance")



c1+=10    #__iadd__(self,other)
print(c1._Customer__balance==15)

print(c1.Name=="Mr. Amin") #Name is a property
print(c2.Name=="Ms. Jane")

c1.Name="A." 
print(c1._Customer__name=="A.")

try:
    c1.Name="A"
    print(False, " this line should not be executed as exception is raised")
except Exception as ex:
    print(str(ex)=="Name should have at least two characters!")


