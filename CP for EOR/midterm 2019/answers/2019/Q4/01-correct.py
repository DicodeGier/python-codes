def isPerfect (num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    if sum == num:
        return True
    return False

if __name__ == "__main__":
    #[6, 28, 496, 8128])
    #if True is returned for given 5, give 0, do not check the rest
    print(isPerfect(5)==False)
    #if True is returned, for each add 0.5
    print(isPerfect(28)==True)
    #print(isPerfect(496))
    print(isPerfect(8128)==True)
    