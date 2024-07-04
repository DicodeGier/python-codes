def func(x):
    years = x//372
    x = x-years*372
    months = x//31
    x = x-months*31
    days = x
    x = x-days*x
    return years,months,days

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