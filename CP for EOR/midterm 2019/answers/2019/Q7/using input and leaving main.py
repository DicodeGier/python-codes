def GetAnimal(year):
    YearNames = [["Dragon",2000],["Snake",2001],["Horse",2002],["Sheep",2003],["Monkey",2004],["Rooster",2005],["Dog",2006],["Pig",2007],["Rat",2008],["Ox",2009],["Tiger",2010],["Hare",2011]]
    animals, years = map(list,zip(*YearNames))

    if year >= 0:
        for i in range(0,8):
            if year % 12 == i:
                return animals[4+i]
        for i in range(8,12):
            if year % 12 == i:
                return animals[i-8]
    else:
        return "NA"
                
def main():
    year = int(input("Enter a year: "))
    print(GetAnimal(year))
main()