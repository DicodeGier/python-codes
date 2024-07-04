from pickle import TRUE
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
            newline[star_position-1] = int(newline[star_position-1]) * int(newline[star_position+1])/int(newline[slash_position+1])
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
            newline[slash_position-1] = int(newline[slash_position-1])/int(newline[slash_position+1])*int(newline[star_position+1])
            newline.pop(star_position+1)
            star_position = newline.index('*')
            newline.pop(star_position)
            slash_position = newline.index('/')
            newline.pop(slash_position + 1)
            slash_position = newline.index('/')
            newline.pop(slash_position)
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
        newline[finder - 1] = int(newline[finder - 1]) + int(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('+')
        newline.pop(finder)

    while '-' in newline:
        if newline.index('-') > newline.index('='):
            return None
        if newline.index('-') == (newline.index('=') - 1):
            return None
        finder = newline.index('-')
        newline[finder - 1] = int(newline[finder - 1]) - int(newline[finder + 1])
        newline.pop(finder + 1)
        finder = newline.index('-')
        newline.pop(finder)

    finder = newline.index('=')
    if newline[finder - 1] == int(newline[finder + 1]):
        all_parts = re.split('([0-9,+,-,*,/])',line)
        all_parts = [x for x in all_parts if x != '']
        for i in options:
            if str(i) not in all_parts:
                return None
        return line

numbers = [0,1,2,3,4,5,6,7,8,9]
operators = ['+', '-', '*', '/', '=']


options = [1,2,4,8,9,'/','=']

for a in options:
    if a not in operators:
        for b in options:
            for c in options:
                for d in options:
                    for e in options:
                        for f in options:
                            for g in options:
                                for h in options:
                                    if h != '=':
                                        solution = checker(a,b,c,d,e,f,g,h) 
                                        if solution != None:
                                            print(solution)

 
# options = [0,1,2,3,4,5,6,7,8,9,'+','-','*','/','=']
 