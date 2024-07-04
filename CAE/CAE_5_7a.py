import random
list = []
counter = 0
while counter <= 20:
    entry = random.randint(0,99)
    list.append(entry)
    counter += 1
print(list)
list.sort()
print(list)