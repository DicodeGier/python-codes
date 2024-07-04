def returnGPA(firstname, lastname, filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    fh.close()

    for line in lines:
        parts = line.strip().split(";")
        if parts[0] == firstname and parts[1] == lastname:
            return parts[2]


print(returnGPA("Bob","Johnson","Q3.txt") == "70%") #if true, 1 point