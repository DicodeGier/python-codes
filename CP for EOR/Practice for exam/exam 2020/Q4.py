def reader(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    fh.close()

    for i in (0,1):
        parts = lines[i].strip().split("=")
        if i == 0:
            origin = parts[1]
        elif i == 1:
            mileage = parts[1]

    for j in (len(lines)-2, len(lines)-1):
        parts = lines[j].strip().split("=")
        if j == len(lines)-2:
            driver = parts[1].strip('"')
        elif j == len(lines)-1:
            car = parts[1].strip('"')

    lines_tips = lines[2: len(lines)-2]
    locations_tips = {}
    for line in lines_tips:
        splitted = line.split(',')
        x_coordinate = splitted[0].split('=')[1].strip()
        y_coordinate = splitted[1].split('=')[1].strip()
        tip = splitted[2].split(':')[1].strip()
        x_y = "({},{})".format(x_coordinate, y_coordinate)
        locations_tips[x_y] = tip


    return origin, locations_tips, mileage, driver, car 

origin,locations_tips,mileage,driver, car=reader("Q4.txt")
print(origin=='(5,5)') #0.1 points
print(mileage=='15.00') #0.1 points
print(driver=='John') #0.1 points
print(car=='Toyota') #0.1 points
print(locations_tips=={'(8,5)': '5.0', '(8,9)': '10.0', '(12,5)': '12.0', '(15,5)': '20.0'}) #0.6 points