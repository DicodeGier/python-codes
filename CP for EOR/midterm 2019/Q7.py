def AllYears(new_year, year):
    if year <2000:
        number = 0
    else:
        number = int((year - 2000)/12)
    all_years = []
    for i in range(-200,number+3):
        all_years.append(new_year + i*12)
    return all_years

def GetAnimal(year):
    if year < 0:
        return "NA"
    dragon = AllYears(2000, year)
    snake = AllYears(2001, year)
    horse = AllYears(2002, year)
    sheep = AllYears(2003, year)
    monkey = AllYears(2004, year)
    rooster = AllYears(2005, year)
    dog = AllYears(2006, year)
    pig = AllYears(2007, year)
    rat = AllYears(2008, year)
    ox = AllYears(2009, year)
    tiger = AllYears(2010, year)
    hare = AllYears(2011, year)

    if year in dragon:
        return 'dragon'
    elif year in snake:
        return 'snake'
    elif year in horse:
        return 'horse'
    elif year in sheep:
        return 'sheep'
    elif year in monkey:
        return 'monkey'
    elif year in rooster:
        return 'rooster'
    elif year in dog:
        return 'dog'
    elif year in pig:
        return 'pig'
    elif year in rat:
        return 'rat'
    elif year in ox:
        return 'ox'
    elif year in tiger:
        return 'tiger'
    elif year in hare:
        return 'hare'

