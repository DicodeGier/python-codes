def pascal(line,filename):
    if line==1 and not filename:
        return [1]
    elif line ==1 and filename:
        with open(filename,"w+") as f:
            f.write("1")
            return
    else:
        prev = pascal(line-1,"")
        curr = [1]
        for i in range(len(prev)-1):
            curr.append(prev[i]+prev[i+1])
        curr.append(1)

    if filename:
        with open(filename,"w+") as f:
            f.write(" ".join([str(i) for i in curr]))
    else:
        return curr

if __name__ == "__main__":
    open("a.txt","w").close()
    pascal(9,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1 8 28 56 70 56 28 8 1")

    open("a.txt","w").close()
    pascal(20,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1 19 171 969 3876 11628 27132 50388 75582 92378 92378 75582 50388 27132 11628 3876 969 171 19 1")

    open("a.txt","w").close()
    pascal(1,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1")

    open("a.txt","w").close()
    pascal(2,"a.txt")
    fh=open("a.txt")
    print(fh.read().strip()=="1 1")
