#develop a function that gets the numbers of days and returns how many years and months are in there as follows. 
# Assume that a year has 365 days and a month has 31 days. You need to return the least numbers of days and months possible.
def func(days):
    years=0
    
    years=days // 372
    days= days % 372

    months= days // 31
    days= days % 31
  
    return years, months, days

years, months, days = func(62)
print(years==0 and months==2 and days==0) #if True 0.4

years, months, days = func(16)
print(years==0 and months==0 and days==16) #if True 0.4

years, months, days = func(372*2)
print(years==2 and months==0 and days==0) #if True 0.4

years, months, days = func(397)
print(years==1 and months==0 and days==25)  #if True 0.4

years, months, days = func(371)
print(years==0 and months==11 and days==30) #if True 0.4




# years, months, days = func(31)
# print(years==0 and months==1 and days==0) #if True 0.4

# years, months, days = func(30)
# print(years==0 and months==0 and days==30) #if True 0.4

# years, months, days = func(372)
# print(years==1 and months==0 and days==0) #if True 0.4

# years, months, days = func(396)
# print(years==1 and months==0 and days==24)  #if True 0.4

# years, months, days = func(370)
# print(years==0 and months==11 and days==29) #if True 0.4


