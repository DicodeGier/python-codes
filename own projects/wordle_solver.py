def checker(a,b,c,d,e):
    word = str(a)+str(b)+str(c)+str(d)+str(e)
    for i in false_letters:
        if i in word:
            return None
    for j in required_letters:
        if j not in word:
            return None
    for k in not_1:
        if k == str(a):
            return None
    for l in not_2:
        if l == str(b):
            return None
    for m in not_3:
        if m == str(c):
            return None
    for n in not_4:
        if n == str(d):
            return None
    for o in not_5:
        if o == str(e):
            return None
    if word in words:
        return word
    else:
        return None

fh = open("all_words.txt",'r')
words = fh.read()
words = words.strip().split('\n')
fh.close()

all_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

### deze veranderen
#########################################################################
option_1 = all_letters
option_2 = ['l']
option_3 = all_letters
option_4 = all_letters
option_5 = all_letters

not_1 = []
not_2 = []
not_3 = []
not_4 = ['i']
not_5 = ['n']

false_letters = ['p','a']
required_letters = ['i','n']
##############################################################################

for a in option_1:
    if a not in false_letters:
        for b in option_2:
            if b not in false_letters:
                for c in option_3:
                    if c not in false_letters:
                        for d in option_4:
                            if d not in false_letters:
                                for e in option_5:
                                    if e not in false_letters:
                                        solution = checker(a,b,c,d,e)
                                        if solution != None:
                                            print(solution)
