def findpath(routes, node, visited):
    visited.append(node)
    if routes[node]!=[]:
        findpath(routes,routes[node][0],visited)
    return visited

# routes1 = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['B'],
#     'D' : [],
#     'E' : ['F'],
#     'F' : []
# }

# routes2 = {
#     'A' : ['B','C'],
#     'B' : [],
#     'C' : [],
# }

# routes3 = {
#     'A' : ['B','C'],
#     'B' : ['D', 'E'],
#     'C' : ['F'],
#     'D' : ['E'],
#     'E' : ['F'],
#     'F' : []
# }

# print(findpath(routes1,'A',[])==['A', 'B', 'D']) # if true 0.25 points
# print(findpath(routes1,'C',[])==['C', 'B', 'D']) # if true 0.25 points
# print(findpath(routes2,'A',[])==['A', 'B']) # if true 0.25 points
# print(findpath(routes3,'A',[])==['A', 'B', 'D', 'E', 'F']) # if true 0.25 points

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