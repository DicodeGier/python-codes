# you lose the entire grade if 
#   you import any packages (like import math),
#   you use "sum" or "mean" in this code,
#   you change the lines that includes do not touch (you can only change the lines marked with #?) 
#   you add more than one line to the code (maximum one line can be added)

a=[1,2,3,4,5,6]  #Do not touch this line  
s=0.0 #s must be initialized before using  
avg=0.0 #Do not touch this line  
#calculate the average (mean) and store it in a variable called avg
for n in a:  #colon is missing, small a should be used, not capital A. Look for colon.
    s+=n     #n should be used, not a[n]
avg=s/len(a)  #/ should be used, not //
str_print="The average is {}!".format(avg)   #look for {} or {0} in the code or 
print(str_print=="The average is 3.5!")  #Do not touch this line  
#You have the correct answer if True is printed (2 points)

# Grading:
# if the output contains True add 2 
# "sum" or "mean" or "import" in code, then 0
# look for ".format" or 0
# look for {} or {0} or 0
# if "print(str_print=="The average is 3.5!")" not in the code, then 0
# look for s=0 or s= 0 or s =0 or s = 0
# look for a: or a :
# look for //
