class Student:
    def __init__(self,_name,_sid,_GPAperYears):
        self.name=_name
        self.sid=_sid
        self.GPAperYears=_GPAperYears

    def getTotalGPA(self):
        return sum(self.GPAperYears)/len(self.GPAperYears)
