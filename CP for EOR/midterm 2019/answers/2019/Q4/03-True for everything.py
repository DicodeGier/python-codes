def isPerfect(num):
    if type(num)==str or type(num)!=int:
        return False
    if num==0 or num==1 or num<0 :
        return False
    else:
        for i in range (1,num+1):
            a=0
            if num%i==0:
                 a=a+i
            else:
                pass
        if num==a:
            return True
        else:
            return False

if __name__ == "__main__":
    #[6, 28, 496, 8128])
    #if True is returned for given 5, give 0, do not check the rest
    print(isPerfect(5))
    #if True is returned, for each add 0.5
    print(isPerfect(28))
    #print(isPerfect(496))
    print(isPerfect(32))