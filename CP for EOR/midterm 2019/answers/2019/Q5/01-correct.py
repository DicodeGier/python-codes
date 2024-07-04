import math
def pascal(line, filename):
    n=line-1
    A=[]
    for i in range(n+1):
        A.append(math.factorial(n)//(math.factorial(i) * math.factorial(n-i)))
    fh=open(filename,"w")
    for i in A:
        fh.write(str(i)+" ")
    fh.close()

if __name__ == "__main__":
    open("a.txt","w").close()
    pascal(9,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1 8 28 56 70 56 28 8 1")
    open("a.txt","w").close()
    pascal(20,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1 19 171 969 3876 11628 27132 50388 75582 92378 92378 75582 50388 27132 11628 3876 969 171 19 1")

