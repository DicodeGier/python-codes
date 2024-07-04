from bar import BarOrder, BarOrderList, BarCustomer
""" (example easy questions to pass the exam) """
#test code for BarOrder 
d1=BarOrder("Beer",6)
print(d1.drink=="beer") #prints True
print(d1.price==6) #prints True
print(d1.isAlcoholic()==True)#prints True
print(d1.number==1)#prints True
print(d1.getTotalItemPrice()==6)#prints True

d2=BarOrder("wine",12,2)
print(d2.drink=="wine") #prints True
print(d2.price==12) #prints True
print(d2.isAlcoholic()==True)#prints True
print(d2.number==2)#prints True
print(d2.getTotalItemPrice()==24)#prints True

d3=BarOrder("Coke",3,10)
print(d3.drink=="coke") #prints True
print(d3.price==3) #prints True
print(d3.isAlcoholic()==False)#prints True
print(d3.number==10)#prints True
print(d3.getTotalItemPrice()==30)#prints True

d4=BarOrder("Water",5)
print(d4.drink=="water") #prints True
print(d4.price==5) #prints True
print(d4.isAlcoholic()==False)#prints True
print(d4.number==1)#prints True
print(d4.getTotalItemPrice()==5)#prints True

d5=BarOrder("Sandwich",5)
print(d5.drink=="sandwich") #prints True
print(d5.price==5) #prints True
print(d5.isAlcoholic()==None)#prints True

""" (example medium questions to get 6.5 to 8) """
#test code for BarOrderList 
bol=BarOrderList()
print(bol.list_orders==[])#prints True

isadded=bol.addBarOrder(d1)
print(isadded==True) #prints True
print(bol.list_orders==[d1]) #prints True
print(bol.getTotal()==6) #prints True

isadded=bol.addBarOrder(d2)
print(isadded==True) #prints True
print(bol.list_orders==[d1,d2]) #prints True
print(bol.getTotal()==30) #prints True
    
isadded=bol.addBarOrder(d3)
print(isadded==True) #prints True
print(bol.list_orders==[d1,d2,d3]) #prints True
print(bol.getTotal()==60) #prints True

isadded=bol.addBarOrder(d4)
print(isadded==True) #prints True
print(bol.list_orders==[d1,d2,d3,d4]) #prints True
print(bol.getTotal()==65) #prints True

isadded=bol.addBarOrder(d5)
print(isadded==False) #prints True
print(bol.list_orders==[d1,d2,d3,d4]) #prints True
print(bol.getTotal()==65) #prints True

# """ example difficult question for those who shoot for 8.5 o higher """
#test code for BarCustomer
c1=BarCustomer("Amin",40)
print(c1.name=="Amin")#prints True
print(c1.age==40)#prints True
print(len(c1.bar_order_list.list_orders)==0) #prints True
print(c1.AllowedToDrink()==True) #prints True

c2=BarCustomer("Peter",16)
print(c2.name=="Peter")#prints True
print(c2.age==16)#prints True
print(c2.AllowedToDrink()==False) #prints True
print(len(c2.bar_order_list.list_orders)==0) #prints True

isadded=c1.addOrder(d1)  #can drink alcoholic
print(isadded==True) #prints True
print(len(c1.bar_order_list.list_orders)==1) #prints True

isadded=c2.addOrder(d1)  #cannot drink alcoholic
print(isadded==False) #prints True
print(len(c2.bar_order_list.list_orders)==0) #prints True

isadded=c1.addOrder(d3)  #coke
print(isadded==True) #prints True
print(len(c1.bar_order_list.list_orders)==2) #prints True

isadded=c2.addOrder(d3)  #coke
print(isadded==True) #prints True
print(len(c2.bar_order_list.list_orders)==1) #prints True

print(c1.bar_order_list.getTotal()==36)#prints True
print(c2.bar_order_list.getTotal()==30)#prints True
