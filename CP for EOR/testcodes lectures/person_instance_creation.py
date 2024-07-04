from person import Person
#instance 1
p1=Person("Amin",90,1.80)
#instance 2
name=input("Enter a name: ")
weight=int(input('Enter weight: '))
height=float(input('Enter height: '))
p2=Person(name,weight,height)

#calculate and print bmi
i=p1.getBMI()
print(i)
print(p2.getBMI())

#printing an instance of Person
print(p1)
print(p2)

#adding two Persons
