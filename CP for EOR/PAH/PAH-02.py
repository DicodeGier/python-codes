# m = int(input("give a number "))
# if m > 0:
#     print(m, "is positive")

# elif m < 0:
#     print(m, 'is negative')

# else:
#     print(m, "is 0")
########################################################

# if True: 
#     print(101)

# else: 
#     print(202)
###########################################

# if False: 
#     print("Nissan") 

# elif True: 
#     print("Ford") 
    
# elif True:
#     print("BMW") 
    
# else: 
#     print("Audi") 
################################################

# if 1: 
#     print("1 is truthy!") 

# else: 
#     print("???")
###################################################

# m = float(input("give the frequency "))
# l = m - 1
# n = m + 1
# a = 0

# for x in [261.63, 293.66, 329.66, 349.23, 392.00, 440.00, 493.88]:
#     i = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
#     if l <= x <= n:
#         print("the note is", i[a])
#     a += 1
######################################################

# month = input("give a month ")
# day = int(input("give the day of the month "))
# month_lower = month.lower()


# while month_lower != 'january' and month_lower != 'february' and month_lower != 'march' and month_lower != 'april' and month_lower != 'may' and month_lower != 'june' and month_lower != 'july' and month_lower != 'august' and month_lower != 'september' and month_lower != 'october' and month_lower != 'november' and month_lower != 'december':
#     month = input("give a month ")
#     month_lower = month.lower()  

# while day > 31 or day <= 0:
#     day = int(input("give the day of the month "))
         

# if month_lower == 'january':
#     print("winter")

# elif month_lower == 'february':
#     if day > 28:
#         print("february has only 28 days")
#     else:
#         print("winter")

# elif month_lower == 'march':
#     if day < 20:
#         print("winter")
#     elif day >= 20 and day <= 31:
#         print("spring")

# elif month_lower == 'april':
#     if day > 30:
#         print("april has only 30 days")
#     else:
#         print("spring")

# elif month_lower == 'may':
#     print("spring")

# elif month_lower == 'june':
#     if day < 21:
#         print('spring')
#     elif day >= 21 and day <= 30:
#         print("summer")

# elif month_lower == 'july' or 'august':
#     print("summer")

# elif month_lower == 'september':
#     if day < 21:
#         print("summer")
#     elif day >=21 and day <= 30:
#         print("fall")

# elif month_lower == 'october':
#     print("fall")

# elif month_lower == 'november':
#     if day <= 30:
#         print("fall")
#     else:
#         print("november has only 30 days")

# elif month_lower == 'december':
#     if day < 21:
#         print("fall")
#     else:
#         print("winter")
###################################################
# m = str(input("give letter grade "))
# if m == 'A+' or m == 'A':
#     print("4.0")

# if m == 'A-':
#     print("3.7")

# if m == 'B+':
#     print("3.3")

# if m == 'B':
#     print("3.0")

# if m == 'B-':
#     print("2.7")

# if m == "c+":
#     print("2.3")

# if m == "c":
#     print("2.0")

# if m == "C-":
#     print("1.7")

# if m == 'D+':
#    print("1.3")

# if m == 'D':
#     print("1.0")

# if m == 'F':
#     print("0.0")
###############################################
# rating = float(input("give your rating "))
# money_raise = rating * 2600

# if rating == 0.0:
#     print("unacceptable perfomance, your raise is", money_raise )

# elif rating == 0.4:
#     print("acceptable performance, your raise is", money_raise)

# elif rating >= 0.6:
#     print("meritorious perfomance, your raise is", money_raise)

# else:
#     print("you did not give an acceptable rating")
############################################################
# year = int(input("give the year "))
# if year%400 == 0:
#     print("leap year")

# elif year%100 == 0:
#     print("not a leap year")

# elif year%4 == 0:
#     print("leap year")

# else:
#     print("not a leap year")
############################################################
# choose = str(input("choose celsius or fahrenheit "))

# if choose == 'celsius':
#     degree_celsius = int(input("give degrees of celsius "))
#     fahrenheit = 9 * (degree_celsius/5) + 32 
#     print('{} Celsius is {} Fahrenheit'.format(degree_celsius, fahrenheit))

# elif choose == 'fahrenheit':
#     degree_fahrenheit = int(input("give degrees of fahrenheit "))
#     celsius = 5 * ((degree_fahrenheit - 32)/9)
#     print('{} Fahrenheit is {} Celsius'.format(degree_fahrenheit, celsius))

# else:
#     print("you did not choose celsius or fahrenheit")
##################################################################################
# a = []
# for i in range(3):
#     i = input("give number ")
#     a.append(i)

# a.sort(reverse = False)
# print("the median is {}".format(a[1]))
##############################################################################
# integer = int(input("give a number "))
# if integer%2 == 0:
#     print("even")
# else:
#     print("odd")
###################################################################
# letter = str(input("give a letter "))
# if letter.isalpha():
#     if letter == 'a' or letter == 'e' or letter =='i' or letter == 'o' or letter == 'u':
#         print("vowel")

#     elif letter == 'y':
#         print("sometimes a vowel, sometimes a consonant")

#     else:
#         print("consonant")

# else:
#     print("you did not choose a letter")
###################################################################
# a = []
# for i in range(3):
#     i = int(input("give side "))
#     a.append(i)

# if a[0] == a[1] == a[2]:
#     print("your triangle is an equilateral")

# elif (a[0] == a[1] and a[1] != a[2]) or (a[0] == a[2] and a[0] != a[1]) or (a[1] == a[2] and a[1] != a[0]): 
#     print("your triangle is an isosceles")

# elif a[0] != a[1] != a[2]:
#     print("your triangle is a scalene")

# else:
#     print("something went wrong, try again")
##################################################################
# amount = int(input("give the amount of letters and numbers on your licence plate "))
# j = 0

# if amount == 6:
#     A=[]
#     for i in range(0,amount):
#         i = input("give letter or number " + str(i+1) + " of your license plate ")
#         A.append(i)
#     for j in range(0,amount):
#         if j<3:
#             if A[j].isalpha():
#                 pass
#             else:
#                 print("your license plate does not have the correct 6 characters style")
#                 break
#         elif j<5:
#             if A[j].isdigit():
#                 pass
#             else:
#                 print("your license plate does not have the correct 6 characters style")
#                 break
#         else:
#             if A[j].isdigit():
#                 pass
#             else:
#                 print("your license plate is not valid for either style of license plates")
#                 break
#             print("your license plate has an older design")
# elif amount == 7:
#     A=[]
#     for i in range(0,amount):
#         i = input("give letter or number " + str(i+1) + " of your license plate ")
#         A.append(i)
#     for j in range(0,amount):
#         if j<4:
#             if A[j].isdigit():
#                 pass
#             else:
#                 print("your license plate does not have the correct 7 characters style")
#                 break
#         elif j<6:
#             if A[j].isalpha():
#                 pass
#             else:
#                 print("your license plate does not have the correct 7 characters style")
#                 break
#         else:
#             if A[j].isalpha():
#                 pass
#             else:
#                 print("your license plate is not valid for either style of license plates")
#                 break
#             print("your license plate has a newer design")
# else:
#     print("your license plate should have either 6 or 7 characters")
#######################################################################
# a = int(input("give positive integer 1 "))
# b = int(input("give positive integer 2 "))
# c = int(input("give positive integer 3 "))
# n = int(input("give the power (higher than 2) "))

# if a <= 0 or b <= 0 or c <= 0 or n <=2:
#     print("you have to give positive integers and a power greater than 2")

# if c**n == a**n + b**n:
#     print("Fermat was wrong")
# else:
#     print("no, that doesn't work")



#################################################
# print (type (5/3 if  4>5  else 5+ 3 ) )
