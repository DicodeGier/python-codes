# i = 1
# while i<50:
#     print(i)
#     i+=1
####################################
# for i in range(1,10):
#     print(i)
####################################
# a = [None] * 11
# total = 0

# for i in range(1,11):
#     a[i] = int(input("give a number "))
#     total += a[i]

# print(total/10)
#################################
# i = 0
# while i<5:
#     print(i)
########################################
# for i in range(10):
#     print(str(i) * i)
##########################################
# m = int(input("give a number "))
# for i in range(1,11):
#     print(m * i)
###########################################
# m = input("give your sentence ")
# m1 = m.upper()
# print(m1)
######################################
# m = input("give a sentence and/or numbers ")
# m_letters = 0
# m_numbers = 0
# totalletters = 0
# totalnumbers = 0
# j = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# k = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# for a in range(0, len(j)):
#     m_letters = m.count(j[a])
#     a +=1
#     totalletters += m_letters

# for b in range(0, len(k)):
#     m_numbers = m.count(k[b])
#     b +=1 
#     totalnumbers += m_numbers

# print("letters:", totalletters)
# print("numbers:", totalnumbers)

# voortaan: .isdigit() en .isalpha() gebruiken
##############################################################
m = int(input("how many passwords do you want to check? "))
A = []
for i in range(m):
    password = input("give your password ")
    A.append(password)

password_letter  = False
password_number = False  
password_upper = False
password_special = False


i = 0
for n in A:
    password_reminder = n
    if len(n)<6 or len(n)>12:
        break
    for n in A[i]:
        if n.isupper():
            password_upper = True
            continue
        elif n.isdigit():
            password_number = True
            continue
        elif n.isalpha():
            password_letter = True
            continue
        elif n == '$' or n == '#':
            password_special = True
            continue
        else:
            continue
    if password_letter == True and password_number == True and password_upper == True and password_special == True:
        print(str(password_reminder) + " fits all the requirements for a password")

    password_letter = False
    password_number = False
    password_upper = False
    password_special = False
    i += 1

            


##########################################
# m = str(input("give string "))
# m1 = m.lower()

# if m1 == 'yes':
#     print("Yes")
# else:
#     print("No")
#########################################
# for i in range(1,5):
#     print("*" * i)
######################################
# import random
# m = random.randint(1,5)
# l =  0
# iteration = 1

# while l != m:
#     l = input("guess the number ")
#     if l == 'exit':
#         break

#     l = int(l)
#     if l<m:
#         print("too low")
#         iteration += 1
        
    
#     if l>m:
#         print("too high")
#         iteration += 1
        



# if l == m:
#     print("you guessed right, this is how many guesses you needed:",iteration)
######################################################################################
# a = []
# for i in range(0,3):
#     hobby = input("give hobby ")
#     a.append(hobby)

# print(a)
##############################################################################
# n = 0
# while n < 21:
#     print(n**2 + 1)
#     n+=1
#############################################################
# s = 'BobTom' 
# for name in ('Bob', 'Ed'): 
#     if name in s:         
#         print('Name {} is in {}'.format(name, s))
############################################################
# m = input("give string ")
# for n in m:
#     print(n)
##########################################################
# for i in range(10):
#     print(str(i) * i)
#################################################
# number = int(input("give a number "))
# total = 0
# for j in range(0,number+1):
#     total += j

# print(total)