from length_module import clsLength
a = clsLength(4)
print("a is equal to:",str(a)) 

b = clsLength(4.5, "yd") 
c= clsLength(10, "cm")
d=b+c
print("d is equal to:", str(d))

e=b.ReturnInMetres()
print("e is equal to:", str(e))
try:
    f=clsLength(23,"league")  #returns an error
except Exception as ex:
    print(str(ex))