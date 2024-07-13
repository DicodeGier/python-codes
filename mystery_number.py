import regex as re

for i in range(100000,1000000):
    num = str(i)
    num_split = re.findall(r'\d',num)

    if not '3' in num_split or not '0' in num_split or not '1' in num_split or not '9' in num_split or not '4' in num_split or not '2' in num_split:
        continue
    else:
        pos3 = num_split.index('3')
        pos0 = num_split.index('0')
        pos1 = num_split.index('1')
        pos9 = num_split.index('9')
        pos4 = num_split.index('4')
        pos2 = num_split.index('2')

        if pos3 != pos0 - 1 or pos1 != pos0 + 1 or pos4 != pos3 - 1 or pos9 != pos1 + 2 or pos2 != pos9 - 1:
            continue
        else:
            print(num)
            break 
    
