from dutch import Customer

c1 = Customer("Dico", 49500)
c2 = Customer("Daan", 500)

print(c1.name=="Dico")
print(c1.balance==49500)

#option 1
c1.deposit1(500)
print(c1.balance==50000)
#option 2
success=c1.deposit2(500)
print(c1.balance==50500)
print(success==True)
#option3
success, new_balance=c1.deposit3(500)
print(c1.balance==51000)
print(success==True)
print(new_balance==51000)