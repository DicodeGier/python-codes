# there is a constant (fixed number) in this code that limits the functionality of the program
# how can you improve this code?

count = int(input("how many numbers would you like to enter?"))
s=0
for tellers in range(1, count+1):
	i=int(input("Give me a number:"))
	s=s+i
print(s)

