max_number = int(input("maximum number of multiplication table "))
number_of_spaces = len(str(max_number * max_number))

for i in range(1,max_number + 1):
    for j in range(1,max_number + 1):
        actual_spaces_ij = len(str(i*j))
        print(i*j,end=" " * (number_of_spaces - actual_spaces_ij + 1))
    print("")