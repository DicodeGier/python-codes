# class Customer:
#     def __init__(self,custID):
#         fh=open("Customers.txt","r")
#         custLines=fh.readlines() 
#         for cLine in custLines:       
#             custParts=cLine.strip().split("|")
#             if custParts[0]==str(custID): 
#                 self.custID=int(custParts[0])    
#                 self.PaidUs=int(custParts[1])    
#                 self.custName=custParts[2]  
#                 return
#         raise Exception("Customer not found")

# c=Customer(5)
# print(c.custID==5 and c.PaidUs==333367 and c.custName=="IND") 
############################################################################
# class Customer:
#     def __init__(self, _custID, _amount, _name):
#         self.custID = _custID
#         self.amount = _amount
#         self.name = _name

#     def __str__(self):
#         return "{}|{}|{}\n".format(self.custID, self.amount, self.name)

# class customerFileManager:
#     def __init__(self, filename):
#         self.all_points = {}
#         self.filename = filename
#         self.loadpoints()

#     def loadpoints(self):
#         fh = open(self.filename)
#         for line in fh.readlines():
#             p = self.__dissect(line)
#             self.all_points[p.custID] = p
#         fh.close()

#     def __dissect(self, line):
#         parts = line.strip().split("|")
#         p = Customer(int(parts[0]),int(parts[1]),parts[2])
#         return p

#     def __str__(self):
#         s=""
#         for _,p in self.all_points.items():
#             s+=str(p)
#         return s

#     def add(self, p):
#         self.all_points[p.custID] = p
#         self.save()

#     def change(self, custID, amount, name):
#         self.all_points[custID].amount = amount
#         self.all_points[custID].name = name
#         self.save()

#     def delete(self, custID):
#         self.all_points.pop(custID)
#         self.save()

#     def save(self):
#         fh = open(self.filename, 'w')
#         fh.write(str(self))
#         fh.close() 

# cm = customerFileManager("Customers.txt")
# print("Here is the file:\n",cm)
# c7=Customer(14,4000,'RDW')
# cm.add(c7)
# cm.change(14,4500,'RDW')
# cm.delete(14)
#####################################################
#zijn antwoord
# class Temp:
#     def __init__(self, temperature = 0, unit="c"):
#         self.__temperature = temperature
#         self.__unit=unit

#     def getTemperature(self):
#         return self.__temperature

#     #i=t.Temperature
#     @property
#     def Temperature(self):
#         return self.__temperature
#     #t.Temperature=32

#     @Temperature.setter
#     def Temperature(self,value):
#         self.__temperature=value
    
#     def setTemperature(self,value):
#         self.__temperature=value

#     def __str__(self):
#         return "{0}{1}".format(self.__temperature,self.__unit)
#     def getUnit(self):
#         return self.__unit
    
#     @property
#     def Unit(self):
#         return self.__unit

#     def setUnit(self,unit):
#         if unit!="c" and unit!="f":
#             raise Exception("unit must be 'c' or 'f'")
#         self.__unit=unit

#     @Unit.setter
#     def Unit(self,unit):
#         if unit!="c" and unit!="f":
#             raise Exception("unit must be 'c' or 'f'")
#         self.__unit=unit

#     def to_fahrenheit(self):
#         if self.__unit=="f":
#             return self.__temperature
#         elif self.__unit=="c":
#             return (self.__temperature * 1.8) + 32
    
#     @property
#     def Fahrenheit(self):
#         if self.__unit=="f":
#             return self.__temperature
#         elif self.__unit=="c":
#             return (self.__temperature * 1.8) + 32

#     def to_celsius(self):
#         if self.__unit=="f":
#             return (self.__temperature -32) / 1.8
#         elif self.__unit=="c":
#             return self.__temperature
#     def get_temperature(self):
#         return self.__temperature

#     def set_temperature(self, value):
#         # if value < -273:
#         #     raise Exception("Temperature below -273 is not possible")
#         self.__temperature = value

# t=Temp(32.0,"c")
# s=t.getUnit()
# print(t)
# t._Temp__temperature=34.1
# print(t)
# t._Temp__unit='f'  #for fahrenheit
# print(t)
# t.set_temperature(100.6)
# print(t)
# try:
#     t.setUnit("c")
#     print(t.get_temperature())
#     t.setUnit("d")
# except Exception as e:
#     print(str(e))
# t.setUnit("f")
# t=Temp(100.6,"f")
# print(t.to_fahrenheit())  #a float
# print(str(t.to_celsius())[:5]) #a float
# t.setUnit("c")
# print(str(t.to_fahrenheit())[:6])  #a float
# print(t.to_celsius()) #a float
# print("===========Properties============")
# t.Unit="d"

################################################
# class fraction:
#     def __init__(self, _fid, _n, _d):
#         self.fid = _fid
#         self.n = _n
#         self.d = _d

#     def __str__(self):
#         return "{} {} {}\n".format(self.fid, self.n, self.d)

# class fractionFileManager:
#     def __init__(self, filename):
#         self.all_fractions = {}
#         self.filename = filename
#         self.loadfractions()

#     def loadfractions(self):
#         fh = open(self.filename)
#         for line in fh.readlines():
#             f = self.__dissect(line)
#             self.all_fractions[f.fid] = f
#         fh.close()

#     def __dissect(self, line):
#         parts = line.strip().split(" ")
#         f = fraction(parts[0], int(parts[1]), int(parts[2]))
#         return f

#     def __str__(self):
#         s = ""
#         for _,f in self.all_fractions.items():
#             s += str(f)
#         return s

#     def add(self, f):
#         self.all_fractions[f.fid] = f
#         self.save()

#     def change(self, fid, newN, newD):
#         self.all_fractions[fid].n = newN
#         self.all_fractions[fid].d = newD
#         self.save()

#     def delete(self, fid):
#         self.all_fractions.pop(fid)
#         self.save()

#     def save(self):
#         fh = open(self.filename, 'w')
#         fh.write(str(self))
#         fh.close()
###############################################
# class fraction:
#     def __init__(self, _fid, _N, _D):
#         self.fid = _fid
#         self.N = _N
#         self.D = _D

#     def __str__(self):
#         return "{} {} {}\n".format(self.fid, self.N, self.D)
    

# class fractionFileManager:
#     def __init__(self, _filename):
#         self.filename = _filename
#         self.all_fractions = {}
#         self.load_fractions()

#     def load_fractions(self):
#         fh = open(self.filename, 'r')
#         lines = fh.readlines()
#         for line in lines:
#             f = self.__dissect(line)
#             self.all_fractions[f.fid] = f
#         fh.close()

#     def __dissect(self, line):
#         parts = line.strip().split(" ")
#         f = fraction(parts[0], int(parts[1]), int(parts[2]))
#         return f

#     def __str__(self):
#         s = ""
#         for _,f in self.all_fractions.items():
#             s += str(f)
#         return s

#     def add(self, f):
#         self.all_fractions[f.fid] = f
#         self.save()

#     def change(self, fid, newN, newD):
#         self.all_fractions[fid].n = newN
#         self.all_fractions[fid].d = newD
#         self.save()

#     def delete(self, fid):
#         self.all_fractions.pop(fid)

#     def save(self):
#         fh = open(self.filename, 'w')
#         fh.write(str(self))
#         fh.close()
######################################################################

# class fraction:
#     def __init__(self, _fid, _N, _D):
#         self.fid = _fid
#         self.N = _N
#         self.D = _D

#     def __str__(self):
#         return "{} {} {}\n".format(self.fid, self.N, self.D)

# class fractionFileManager:
#     def __init__(self, _filename):
#         self.all_fractions = {}
#         self.filename = _filename
#         self.load_fractions()

#     def load_fractions(self):
#         fh = open(self.filename, 'r')
#         lines = fh.readlines()
#         for line in lines:
#             f = self.__disect(line)
#             self.all_fractions[f.fid] = f
#         fh.close()

#     def __disect(self, line):
#         parts = line.strip().split(" ")
#         f = fraction(parts[0], int(parts[1]), int(parts[2]))
#         return f

#     def __str__(self):
#         s = ""
#         for _,f in self.all_fractions.items():
#             s += str(f)
#         return s

#     def add(self, f):
#         self.all_fractions[f.fid] = f
#         self.save()

#     def change(self, fid, newN, newD):
#         self.all_fractions[fid].N = newN
#         self.all_fractions[fid].D = newD
#         self.save()

#     def delete(self, fid):
#         self.all_fractions.pop(fid)
#         self.save()

#     def save(self):
#         fh = open(self.filename, 'w')
#         fh.write(str(self))
#         fh.close
#############################################################
class fraction:
    def __init__(self, _fid, _N, _D):
        self.fid = _fid
        self.N = _N
        self.D = _D

    def __str__(self):
        return "{} {} {}\n".format(self.fid, self.N, self.D)

class fractionFileManager:
    def __init__(self, _filename):
        self.filename = _filename
        self.all_fractions = {}
        self.load_fractions()

    def load_fractions(self):
        fh = open(self.filename, 'r')
        lines = fh.readlines()
        for line in lines:
            f = self.__disect(line)
            self.all_fractions[f.fid] = f
        fh.close()

    def __disect(self, line):
        parts = line.strip().split(" ")
        f = fraction(parts[0], int(parts[1]), int(parts[2]))
        return f

    def __str__(self):
        s = ""
        for _,f in self.all_fractions.items():
            s += str(f)
        return s

    def add(self, f):
        self.all_fractions[f.fid] = f
        self.save()

    def change(self, fid, newN, newD):
        self.all_fractions[fid].N = newN
        self.all_fractions[fid].D = newD
        self.save()

    def delete(self, fid):
        self.all_fractions.pop(fid)
        self.save()

    def save(self):
        fh = open(self.filename, 'w')
        fh.write(str(self))
        fh.close()
            

pm=fractionFileManager("fractions.txt")
print("Here is the file:\n",pm)
p4=fraction('f5',4,4)
pm.add(p4)
pm.change('f5',3,3)
pm.delete('f5')

