def reader(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    fh.close()

    length = len(lines)
    volume = int(lines[0].strip().split("=")[1])
    player = lines[length - 1].strip().split("=")[1].strip('"')
    cubes = []
    for i in range(2,length - 1):
        parts = lines[i].strip().split(",")
        cubes.append([int(parts[0].strip('"')), int(parts[1].strip("'")), int(parts[2].strip("[]"))])
    return volume, cubes, player




volume,cubes,player=reader("RQ4.txt")
print(volume==300) #0.2 points
print(player=='Jane') #0.2 points
print(cubes==[[8, 5, 10], [4, 4, 4], [8, 10, 12], [15, 15, 20]]) #0.6 points