def GetAnimal(year):
    YearNames = ["Monkey","Rooster","Dog","Pig","Rat","Ox","Tiger","Hare","Dragon","Snake","Horse","Sheep"]
    if year < 0:
        return "NA"
    else:
        for i in range(12):
            if year % 12 == i:
                animal = YearNames[i]
        return animal

if __name__ == "__main__":
    print(GetAnimal(2000).lower()=="dragon") #0.25
    print(GetAnimal(12).lower()=="monkey") #0.50
    print(GetAnimal(-1).lower()=="na") #0.25
