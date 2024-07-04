import re

def checker(a,b,c,d,e,f,g,h):
    line = str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h)
    newline = re.split('([^0-9])', line)
    newline = [x for x in newline if x != '']
    for i in range(0,len(newline)-1):
        if newline[i] in operators and newline[i+1] in operators:
            return None
    if newline.count('=') > 1 or newline.count('=') == 0:
        return None
    if '*' in newline and '/' in newline:
        star_position = newline.index('*')
        slash_position = newline.index('/')
        if star_position > newline.index('='):
            return None
        if star_position == (newline.index('=') - 1):
            return None
        if slash_position > newline.index('='):
            return None
        if slash_position == (newline.index('=') - 1):
            return None
        if star_position < slash_position:
            if newline[slash_position + 1] == 0:
                return None
            newline[star_position-1] = float(newline[star_position-1]) * float(newline[star_position+1])/float(newline[slash_position+1])
            newline.pop(slash_position+1)
            slash_position = newline.index('/')
            newline.pop(slash_position)
            star_position = newline.index('*')
            newline.pop(star_position + 1)
            star_position = newline.index('*')
            newline.pop(star_position)
        elif star_position > slash_position:
            if newline[star_position + 1] == 0:
                return None
            newline[slash_position-1] = float(newline[slash_position-1])/float(newline[slash_position+1])*float(newline[star_position+1])
            newline.pop(star_position+1)
            star_position = newline.index('*')
            newline.pop(star_position)
            slash_position = newline.index('/')
            newline.pop(slash_position + 1)
            slash_position = newline.index('/')
            newline.pop(slash_position)
    if '+' in newline and '-' in newline:
        plus_position = newline.index('+')
        minus_position = newline.index('-')
        if plus_position > newline.index('='):
            return None
        if plus_position == (newline.index('=') - 1):
            return None
        if minus_position > newline.index('='):
            return None
        if minus_position == (newline.index('=') - 1):
            return None
        if plus_position < minus_position:
            newline[plus_position-1] = float(newline[plus_position-1]) + float(newline[plus_position+1]) - float(newline[minus_position+1])
            newline.pop(minus_position+1)
            minus_position = newline.index('-')
            newline.pop(minus_position)
            plus_position = newline.index('+')
            newline.pop(plus_position + 1)
            plus_position = newline.index('+')
            newline.pop(plus_position)
        elif plus_position > minus_position:
            newline[minus_position-1] = float(newline[minus_position-1]) - float(newline[minus_position+1])+float(newline[plus_position+1])
            newline.pop(plus_position+1)
            plus_position = newline.index('+')
            newline.pop(plus_position)
            minus_position = newline.index('-')
            newline.pop(minus_position + 1)
            minus_position = newline.index('-')
            newline.pop(minus_position)
    while '*' in newline:
        if newline.index('*') > newline.index('='):
            return None
        if newline.index('*') == (newline.index('=') - 1):
            return None
        finder = newline.index('*')
        newline[finder - 1] = int(newline[finder - 1]) * int(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('*')
        newline.pop(finder)

    while '/' in newline:
        if newline.index('/') > newline.index('='):
            return None
        if newline.index('/') == (newline.index('=') - 1):
            return None
        finder = newline.index('/')
        if int(newline[finder + 1]) == 0:
            return None
        newline[finder - 1] = float(newline[finder - 1]) / float(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('/')
        newline.pop(finder)

    while '+' in newline:
        if newline.index('+') > newline.index('='):
            return None
        if newline.index('+') == (newline.index('=') - 1):
            return None
        finder = newline.index('+')
        newline[finder - 1] = float(newline[finder - 1]) + float(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('+')
        newline.pop(finder)

    while '-' in newline:
        if newline.index('-') > newline.index('='):
            return None
        if newline.index('-') == (newline.index('=') - 1):
            return None
        finder = newline.index('-')
        newline[finder - 1] = float(newline[finder - 1]) - float(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('-')
        newline.pop(finder)

    finder = newline.index('=')
    if newline[finder - 1] == float(newline[finder + 1]):
        """
        all_parts = re.split('([0-9,+,-,*,/])',line)
        all_parts = [x for x in all_parts if x != '']
        for i in option_1:
            if str(i) not in all_parts:
                return None
        for j in option_2:
            if str(j) not in all_parts:
                return None
        for k in option_3:
            if str(k) not in all_parts:
                return None
        for l in option_4:
            if str(l) not in all_parts:
                return None
        for m in option_5:
            if str(m) not in all_parts:
                return None
        for n in option_6:
            if str(n) not in all_parts:
                return None
        for o in option_7:
            if str(o) not in all_parts:
                return None
        for p in option_8:
            if str(p) not in all_parts:
                return None
        """
        return line

numbers = [0,1,2,3,4,5,6,7,8,9]
operators = ['+', '-', '*', '/', '=']


##deze veranderen
###########################################
option_1 = [3]
option_2 = [9]
option_3 = [9]
option_4 = ['/']
option_5 = [7]
option_6 = ['=']
option_7 = [5]
option_8 = [4,7]
############################################

for a in option_1:
    for b in option_2:
        for c in option_3:
            for d in option_4:
                for e in option_5:
                    for f in option_6:
                        for g in option_7:
                            for h in option_8:
                                solution = checker(a,b,c,d,e,f,g,h) 
                                if solution != None:
                                    print(solution)

# option_1 = [0,1,2,3,4,5,6,7,8,9]
# option_2 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']
# option_3 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']
# option_4 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']
# option_5 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/','=']
# option_6 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/','=']
# option_7 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/','=']
# option_8 = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/']
