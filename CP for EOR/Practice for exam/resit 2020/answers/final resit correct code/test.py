#Q1
print(triangle_area("(3,3)", "(8,5)", "(8,8)")==7.5)

#Q2
routes1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['B'],
    'D' : [],
    'E' : ['F'],
    'F' : ['A']
}

routes2 = {
    'A' : ['B','C'],
    'B' : [],
    'C' : ['A'],
}

routes3 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['E'],
    'E' : ['F'],
    'F' : []
}

print(findpath(routes1,'E',[])==['E', 'F', 'A', 'B', 'D']) # if true 0.25 points
print(findpath(routes1,'D',[])==['D']) # if true 0.25 points
print(findpath(routes2,'C',[])==['C', 'A', 'B']) # if true 0.25 points
print(findpath(routes3,'C',[])==['C', 'F']) # if true 0.25 points

#Q3
print(getyear("RQ3.txt") == {'Thunder': '1961', 'Live and Let Die': '1973', 'GoldenEye': '1995', 'Spectre': '2015'})

#Q4
volume,cubes,player=reader("RQ4.txt")
print(volume==30) #0.2 points
print(player=='Jack') #0.2 points
print(cubes==[[18, 5, 10], [4, 4, 4], [8, 10, 12], [15, 15, 20],[15, 15, 20]]) #0.6 points
