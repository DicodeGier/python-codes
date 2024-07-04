## exercise 11
# def median(a,b,c):
#     d = [a, b, c]
#     d.sort(reverse = True)
#     return "the median is {}".format(d[1])

# a = int(input("give the first number "))
# b = int(input("give the second number "))
# c = int(input("give the third number "))

# print(median(a,b,c))
#############################################
## exercise 13

###########################################
## exercise 15
# def isPrime(a):
#     for i in range(2, a):
#         if a%i == 0:
#             return "{} is not a prime number".format(a)
#     else:
#         return "{} is a prime number".format(a)

# a = int(input("give a number "))
# print(isPrime(a))
##########################################
## exercise 16
# import random
# def RandomPassword():
#     a = []
#     for i in range(33, 127):
#         b = chr(i)
#         a.append(b)
#     password = ""
#     characters = random.randint(7,10)
#     for i in range(1,characters + 1):
#         d = random.choice(a)
#         password += d
#     return password

# print(RandomPassword())
######################################
## exercise 17
# def PasswordCheck(a):
#     password_letter  = False
#     password_number = False  
#     password_upper = False


#     for n in a:
#         if len(a)<8:
#             break
#         for n in a:
#             if n.isupper():
#                 password_upper = True
#                 continue
#             elif n.isdigit():
#                 password_number = True
#                 continue
#             elif n.isalpha():
#                 password_letter = True
#                 continue
#             else:
#                 continue
#     if password_letter == True and password_number == True and password_upper == True:
#         return(str(a) + " fits all the requirements for a good password")
#     else:
#         return(str(a) + " does not fit all the requirements for a good password")

# a = input("give your password ")
# print(PasswordCheck(a))
################################################
## exercise 21
# def MagicYear(day, month, year):
#     if day*month == year:
#         return("this date is a magic date")
#     else:
#         return("this date is not a magic date")

# day = int(input("give the number of the day "))
# month = int(input("give the number of the month "))
# year = int(input("give the last two numbers of the year "))
# print(MagicYear(day, month, year))

# for i in range(0,100):
#     for j in range(1,13):
#         for k in range(1,31):
#             if k*j == i:
#                 print(str(k) + " - " + str(j) + " - " + str(i) + " is a magic date")
#                 continue
#################################################
## exercise 24
# import math
# def Factorial(a):
#     return math.factorial(a)

# a = int(input("give a number "))
# print(Factorial(a))
############################################
## exercise 27
# def ReducedFraction(a,b):
#     if a<b:
#         for i in range(1, a-1):
#             if a%i == 0 and b%i == 0:
#                 j = i
#         return "the numerator is {} and the denominator is {}".format(a//j, b//j)

#     elif a>b:
#         for i in range(1, b-1):
#             if b%i == 0 and a%i == 0:
#                 j = i
#         return "the numerator is {} and the denominator is {}".format(a//j, b//j)



# a = int(input("give the numerator "))
# b = int(input("give the denominator "))
# print(ReducedFraction(a,b))
#################################################
## exercise 28
# def Spoon(a,b):
#     if b == 'cup':
#         return "{} cup".format(a)
#     elif b == 'tablespoon':
#         c = a*3
#         d = c//48
#         e = (c-d*48)//3
#         f = (c-d*48-e*3)%3
#         return "{} cup, {} tablespoon, {} teaspoon".format(d,e,f)
#     elif b == 'teaspoon':
#         g = a//48
#         h = (a-g*48)//3
#         i = (a-g*48-h*3)%3
#         return "{} cup, {} tablespoon, {} teaspoon".format(g,h,i)
#     else:
#         return "you did not give a possible unit of measure"

# a = int(input("give the number of units ")) 
# b = input("give the unit of measure: cup, tablespoon or teaspoon ")
# print(Spoon(a,b)) 
###############################################
## exercise 29
# def Multiple():
#     a = []
#     for i in range(2000, 3201):
#        if i%7 == 0 and i%5 != 0:
#            a.append(i)
#     return a

# print(Multiple())
##############################################
## exercise 30
# def Dict(n):
#     dict = {}
#     for i in range(1,n+1):
#         dict |= {i:i**2}
#     return dict

# n = int(input("give a number "))
# print(Dict(n))       
#######################################
## exercise 34
def List(n):
    sample_list = []
    for i in range(0,n):
        number = int(input("give the number "))
        sample_list.append(number)
    
    for a in sample_list:
        z = sample_list.count(a)
        if z>1:
            for j in range(1,z):
                m = sample_list.index(a)
                sample_list.pop(m)
    return sample_list 

n = int(input("how many elements are in the list? "))
print(List(n))