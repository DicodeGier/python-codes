#1. study the section on "string" in lecture 1
#2. execute this program that gets a string and prints its characters
#4. execute the program line by line
#4.1 If you replace "pass" with "break", what is the output?
#4.2 If you replace "pass" with "continue", what is the output?


txt="HiGuys!!!"
size=len(txt)
for i in range(0,size):
    if i==2:
        continue
    print(txt[i])
