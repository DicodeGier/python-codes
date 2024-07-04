##a
import random
import time

x_start = 0
y_start = 0

current_x = x_start
current_y = y_start

i = 0
max_i = 100000
while i <= max_i:
    print(str(i/max_i*100)+'%', end = '\r')
    next_direction = random.randint(0,3)
    if next_direction == 0:
        current_x += 1
    elif next_direction == 1:
        current_y += 1
    elif next_direction == 2:
        current_x -= 1
    else:
        current_y -= 1
    i += 1

print("({},{})".format(current_x, current_y))




