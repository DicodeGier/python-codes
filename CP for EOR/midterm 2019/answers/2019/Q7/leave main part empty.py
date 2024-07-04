# Question 7

# YearNames = [["Dragon",2000],["Snake",2001],["Horse",2002],["Sheep",2003],["Monkey",2004],["Rooster",2005],["Dog",2006],["Pig",2007],
# ["Rat",2008],["Ox",2009],["Tiger",2010],["Hare",2011]]

# year == 0 --> Monkey
# year == 11 --> Sheep
# year == 12 --> Monkey

A = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Hare","Dragon","Snake","Horse","Sheep"]

def GetAnimal(year):
    if year < 0:
        return "NA"
    else:
        for i in range(0,11+1):
            if (year-i)%12 == 0:
                animal = A[i]
            else:
                continue
    return animal

if __name__ == "__main__":
    print(GetAnimal(2000).lower()=="dragon") #0.25
    print(GetAnimal(12).lower()=="monkey") #0.50
    print(GetAnimal(-1).lower()=="na") #0.25
