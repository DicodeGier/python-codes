def getyear(filename):
    fh = open(filename, 'r')
    lines = fh.readlines()
    fh.close()

    new_dict = {}
    for line in lines:
        parts = line.strip().split("|")
        new_dict[parts[0]] = parts[2]
    return new_dict


print(getyear("RQ3.txt") == {'Thunder': '1961', 'Live and Let Die': '1973', 'GoldenEye': '1995', 'Spectre': '2015'}) #if true, 1 point
print(getyear("RQ3.txt")['Thunder']=='1961') #just another test case for clarification