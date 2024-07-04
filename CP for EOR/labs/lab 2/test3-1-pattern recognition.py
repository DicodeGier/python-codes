#1. execute this program using F5 to figure out what it does
#2. execute this program line by line to figure out what it does
# find the pattern
# turn the pattern to a (i) for loop (ii) while loop
# note that uthe user has to enter FOUR numbers, not five or three numbers
# s=0
# idx=1
# i=int(input("Give me number {}: ".format(idx)))
# s+=i
# idx=2
# i=int(input("Give me number {}: ".format(idx)))
# s+=i
# idx=3
# i=int(input("Give me number {}: ".format(idx)))
# s+=i
# idx=4
# i=int(input("Give me number {}: ".format(idx)))
# s+=i
# print("The sum is: ",s)

s = 0
idx = 1
for idx in range(1,5):
    i=int(input("give me number {}: ".format(idx)))
    s+=i
    idx+=1
print("the sum is: ",s)



