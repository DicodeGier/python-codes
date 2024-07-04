class driver:
    def __init__(self, _drv, _name, _team, _eyecolor, _height, _dna):
        self.drv = _drv
        self.name = _name
        self.team = _team
        self.eyecolor = _eyecolor
        self.height = _height
        self.dna = _dna

    def in_dna(self, dna_sequence):
        if dna_sequence in self.dna:
            return True
        else:
            return False

class all_drivers:
    def __init__(self, _filename):
        self.drivers = []
        self.filename = _filename
        self.overload()

    def overload(self):
        fh = open(self.filename, 'r')
        lines = fh.readlines()
        length = len(lines)
        fh.close
        index = 0
        while index < length:
            line = lines[index]
            if line[0] == "-":
                number = line.strip().strip("-----")
            index += 1
            name_team = lines[index].split(":")[1].strip().split("-")
            name = name_team[0].strip()
            team = name_team[1].strip()
            index += 1
            eye_height = lines[index].split(";")
            if eye_height == '["Grading instruction\n"]':
                index += 1
                continue
            else:
                eye = eye_height[0].strip().split(":")[1].strip()
            height = float(eye_height[1].strip().split(":")[1].strip())
            indexstart = index+1
            indexDNA = index
            while lines[index][0] != "-":
                index+=1
                indexDNA+=1
            DNA = ""
            for i in range(indexstart, indexDNA):
                DNA += lines[i].strip()
            DNA = DNA.split(":")[1].strip()
            driver_case = driver(number, name, team, eye, height, DNA)
            self.drivers.append(driver_case)
            index+=1
        return number, name, team
        


#test code driver
d=driver('02','Mich Schumacher','Haas','Brown',176,'atgcatgc')
print(d.drv=='02' and d.name=='Mich Schumacher' and d.team=='Haas' 
    and d.eyecolor=='Brown' and d.height==176 and d.dna=='atgcatgc') #0.2 points
print(d.in_dna('atg')==True and d.in_dna('gcagg')==False)  #0.2
#test codes all_driver
ad=all_drivers("Q6.txt")
d1=ad.drivers[0]
print(d1.drv=='33' and d1.name=='Max Verstappen' and d1.team=='Red Bull')