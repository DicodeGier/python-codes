#the student should have checked the code with input at least once
def GetAnimal(year):
    if year%12== 0:
        return "Dragon"
    elif year%12 == 1:
        return "Snake"
    elif year%12 == 2:
        return "Horse"
    elif year%12 == 3:
        return "Sheep"
    elif year%12==4:
        return "Monkey"
    elif year%12==5:
        return "Rooster"
    elif year%12==6:
        return "Dog"
    elif year%12 ==7:
        return "Pig"
    elif year%12==8:
        return "Rat"
    elif year%12==9:
        return "Ox"
    elif year%12==10:
        return "Tiger"
    elif year%12==11:
        return "Hare"
    else:
        return "NA"

print(GetAnimal(-1))