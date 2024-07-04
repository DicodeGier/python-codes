def getyear(filename):
    lines=open(filename).readlines()
    md={}
    for line in lines:
        parts=line.strip().split('|')
        md[parts[0]] = parts[2]
    return md

print(getyear("RQ3.txt") == {'Thunder': '1961', 'Live and Let Die': '1973', 'GoldenEye': '1995', 'Spectre': '2015'}) #if true, 1 point
print(getyear("RQ3.txt")['Thunder']=='1961')