# teacher_courses = {'Amin':3, 'Emiel':1, 'Hans':4}
# l = []
# for teacher in teacher_courses:
#     courses = teacher_courses[teacher]
#     l.append([teacher,courses])

# teachers = [['Amin',3], ['Emiel',1], ['Hans',4]]
# d = {}
# for teacher in teachers:
#     t_name = teacher[0]
#     t_course = teacher[1]
#     d[t_name] = t_course


# print(d=={'Amin':3, 'Emiel':1, 'Hans':4})
#################################################
# a = int(input("give the first number "))
# b = int(input("give the second number "))

# if a>b:
#     print("max is " + str(a))
# elif b>a:
#     print("max is " + str(b))
# else:
#     print(str(a) + ' is ' + str(b))
#####################################################
# def color_pick(s):
#     if s.lower() == 'blue':
#         print("you picked the first color")
#     elif s.lower() == 'white':
#         print("you picked the second color")
#     elif s.lower() == 'red':
#         print("you picked the third color")
#     else:
#         print("you did not pick from the list")

# s1 = input("pick a color: blue, white or red ")
# color_pick(s1)
#########################################################
def DivBy2(x,y):
    z1 = x//2
    z2 = y//2
    return z1,z2

i,j = 7,10
i,j = DivBy2(i,j)
z = print(i == 3 and j == 5)