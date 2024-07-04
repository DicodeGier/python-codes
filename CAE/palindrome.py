
#dMethod that determines whether a word is a palindrome or not with recursion
#@ param n, the word
#@return boolean, whether the word is a palindrome
def isPalindrome(n):
    i = len(str(n))
    if (i<=1):
        return True
    elif (n[0] != n[-1]):
        return False
    else: 
        #return isPalindrome(n[1:i-1])
        return isPalindrome(n[1:-1])

def main():
    #test method
    word = str(input("Enter a word, to check if it is palindrome: "))

    if isPalindrome(word):
        print(word, "is a palindrome.")
    else:
        print(word, "is a not a palindrome.")

#call main method
main()
