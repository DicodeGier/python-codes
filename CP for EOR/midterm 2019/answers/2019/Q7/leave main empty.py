Yearnames=[["Dragon", 2000],["Snake", 2001], ["Horse", 2002],["Sheep", 2003],["Monkey", 2004], ["Rooster", 2005], ["Dog", 2006], ["Pig", 2007], ["Rat", 2008], ["Ox", 2009], ["Tiger", 2010], ["Haree", 2011]]

def GetAnimal(year):
    if year <= 0:
        return "NA"
    elif year % 12 == 8:
        return "Dragon"
    elif year % 12 == 9:
        return "Snake"
    elif year % 12 == 10:
        return "Horse"
    elif year % 12 == 11:
        return "Sheep"
    elif year % 12 == 0:
        return "Monkey"
    elif year % 12 == 1:
        return "Rooster"
    elif year % 12 == 2:
        return "Dog"
    elif year % 12 == 3:
        return "Pig"
    elif year % 12 == 4:
        return "Rat"
    elif year % 12 == 5:
        return "Ox"
    elif year % 12 == 6:
        return "Tiger"
    elif year % 12 == 7:
        return "Hare"

if __name__ == "__main__":
    print(GetAnimal(2000).lower()=="dragon") #0.25
    print(GetAnimal(12).lower()=="monkey") #0.50
    print(GetAnimal(-1).lower()=="na") #0.25
