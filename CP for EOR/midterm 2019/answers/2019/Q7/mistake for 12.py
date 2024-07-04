def GetAnimal(year):
    if year % 12 == 8 and year >= 0:
        return "dragon"
    elif year % 12 == 7 and year >= 0:
        return "hare"
    elif year % 12 == 6 and year >= 0:
        return "tiger"
    elif year % 12 == 5 and year >= 0:
        return "ox"
    elif year % 12 == 4 and year >= 0:
        return "rat"
    elif year % 12 == 3 and year >= 0:
        return "pig"
    elif year % 12 == 2 and year >= 0:
        return "dog"
    elif year % 12 == 1 and year >= 0:
        return "rooster"
    elif year % 12 == 9 and year >= 0:
        return "snake"
    elif year % 12 == 10 and year >= 0:
        return "horse"
    elif year % 12 == 11 and year >= 0:
        return "sheep"
    elif year % 12 == 12 and year >= 0:
        return "monkey"
    elif year < 0:
        return "NA"

if __name__ == "__main__":
    print(GetAnimal(2000).lower()=="dragon") #0.25
    print(GetAnimal(12).lower()=="monkey") #0.50
    print(GetAnimal(-1).lower()=="na") #0.25


