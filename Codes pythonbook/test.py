import re

for i in range(100,491):
    if i%2 == 1:
        continue
    splitted_number = re.split('(\d)',str(i))
    splitted_number = [x for x in splitted_number if x != '']
    if int(splitted_number[1]) != 3 + int(splitted_number[2]):
        continue
    if int(splitted_number[2]) == 2 or int(splitted_number[2]) == 4:
        continue
    if int(splitted_number[0]) + int(splitted_number[1]) + int(splitted_number[2]) != 19:
        continue

    print('the number is ' + i)
    
    

