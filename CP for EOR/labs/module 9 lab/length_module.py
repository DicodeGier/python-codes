metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
class clsLength:
    def __init__(self, _number = 0, _measure = 'm'):
        if _measure not in metric:
            raise Exception("unrecognized unit: {}".format(_measure))
        self.number = _number
        self.measure = _measure
    
    def __str__(self):
        return "{}{}".format(self.number, self.measure)

    def __add__(self, other):
        d = clsLength()
        d.number = self.number*metric[self.measure] + other.number*metric[other.measure]
        d.measure = 'm'
        return d.__str__()

    def ReturnInMetres(self):
        e = clsLength()
        e.number = self.number*metric[self.measure]
        e.measure = 'm'
        return e
    