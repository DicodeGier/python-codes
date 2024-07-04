# find the pattern
# turn the pattern to a (i) for loop (ii) while loop
# note that uthe user has to enter FOUR numbers, not five or three numbers

# s=0
# i=int(input("Give me number 1: "))
# s+=i
# i=int(input("Give me number 2: "))
# s+=i
# i=int(input("Give me number 3: "))
# s+=i
# i=int(input("Give me number 4: "))
# s+=i

# print("The sum is: ",s)

s= 0
idx = 1
while idx < 5:
    i=int(input("give me number {}: ".format(idx)))
    s+=i
    idx+=1
print("the sum is",s)

