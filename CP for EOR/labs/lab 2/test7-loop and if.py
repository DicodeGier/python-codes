#1. execute this program that gets a character and print what it is
#2. execute the program line by line
#3. study the section on "string" in lecture 1 
#4. use for loop to turn this code into a program that gets a string (which is a sequence of characters) and prints its character types
# For "Hi all!" as an input, 
#      the program prints: "capital letter | small letter | blank space | small letter | small letter | small letter | special character |"
# For "a1@a.com" as an input, 
#      the program prints: "small letter | digit | special character | small letter | special character | small letter | small letter | small letter |"
#5. use while loop to do the same thing

txt=input("Give a single character: ")
txt2=""
for s in txt:
    if len(s)>=2:
        txt2+="2 or more characters are given | "
    elif s.isdigit():
        txt2+="digit | "
    elif s.isalpha() and s.islower():
        txt2+="small letter | "
    elif s.isalpha() and s.isupper():
        txt2+="capital letter | "
    elif s==" ":
        txt2+="blank space | "
    else:
        txt2+="special character | "

print(txt2)
    