def reader(filename):
    lines=open(filename).readlines()
    volume=int(lines[0].strip().replace('volume=',''))
    count = len(open(filename).readlines(  ))
    player = lines[count-1].strip().split('=')[1].strip('"')
    lines=lines[2:count-1]
    cubes=[]
    for line in lines:
        parts=line.strip().split(',')
        width=int(parts[0].strip('"'))
        length=int(parts[1].strip("'"))
        height=int(parts[2].strip('[').strip(']'))
        cubes.append([width,length,height])
    return volume,cubes,player

volume,cubes,player=reader("RQ4.txt")
print(volume==30) #0.2 points
print(player=='Jack') #0.2 points
print(cubes==[[18, 5, 10], [4, 4, 4], [8, 10, 12], [15, 15, 20],[15, 15, 20]]) #0.6 points
