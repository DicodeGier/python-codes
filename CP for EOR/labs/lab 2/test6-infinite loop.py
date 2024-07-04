#1. search the internet to figure out what random.randint does
#2. execute this program and try to stop it using shift+F5
#3. add a piece of code that ends the while loop if the number is divisible by 17 after printing the number
#execute the program and shout out the number divisible by 17 that ended the loop to scare the hell out of your housemate :)
#4. return the cod to its origin (step 2) and add a piece of code that prints **** if a number is divisible by 17 after printing the number
# import random
# loop = True
# while loop == True:
#     n = random.randint(1,100)
#     if n%17 == 0:
#         print(n, "is divisible by 17")
#         loop = False #or break
#     print(n)


import random

while True:
    n = random.randint(1,100)
    print(n)
    if n%17 == 0:
        print("****")
