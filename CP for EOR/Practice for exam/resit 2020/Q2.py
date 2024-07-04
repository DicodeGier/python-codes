def findpath(dictionnary, starting_point, list):
    list.append(starting_point)
    value = dictionnary[starting_point]
    if value == []:
        return list
    final_value = value[0]
    return findpath(dictionnary, final_value, list)

routes1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['B'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
routes2 = {
    'A' : ['B','C'],
    'B' : [],
    'C' : [],
}
routes3 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['E'],
    'E' : ['F'],
    'F' : []
}
print(findpath(routes1,'A',[])==['A', 'B', 'D']) # if true 0.25 points
print(findpath(routes1,'C',[])==['C', 'B', 'D']) # if true 0.25 points
print(findpath(routes2,'A',[])==['A', 'B']) # if true 0.25 points
print(findpath(routes3,'A',[])==['A', 'B', 'D', 'E', 'F']) # if true 0.25 points