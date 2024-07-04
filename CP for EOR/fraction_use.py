class fraction:
    def __init__(self, _fid, _numerator, _denominator):
        self.fid = _fid
        self.numerator = _numerator
        self.denominator = _denominator

    def __str__(self):
        return "{} {} {}\n".format(self.fid, self.numerator, self.denominator)


class fractionFileManager:
    def __init__(self, filename):
        self.all_fractions = {}
        self.filename = filename
        self.load_fractions()

    def load_fractions(self):
        fh = open(self.filename, 'r')
        lines = fh.readlines()
        for line in lines:
            f= self.__disect(line)
            self.all_fractions[f.fid] = f
        fh.close()

    def __disect(self, line):
        parts = line.strip().split(" ")
        f = fraction(parts[0], int(parts[1]), int(parts[2]))
        return f

    def __str__(self):
        s = ""
        for _,f in self.all_fractions.items():
            s += str(f)
        return s

    def add(self, f):
        self.all_fractions[f.fid] = f
        self.save()

    def change(self, fid, newN, newD):
        self.all_fractions[fid].numerator = newN
        self.all_fractions[fid].denominator = newD
        self.save()

    def delete(self, fid):
        self.all_fractions.pop(fid)
        self.save()

    def save(self):
        fh = open(self.filename, 'w')
        fh.write(str(self))
        fh.close()







pm=fractionFileManager("fractions.txt")
print("Here is the file:\n",pm)
p4=fraction('f5',4,4)
pm.add(p4)
pm.change('f5',3,3)
pm.delete('f5')