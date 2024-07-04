class student:
    def __init__(self, _stu, _name, _specialization, _midterm, _quiz, _year, _answer):
        self.stu = _stu
        self.name = _name
        self.specialization = _specialization
        self.midterm = _midterm
        self.quiz =_quiz
        self.year = _year
        self.answer = _answer

    def count_in_answer(self, text):
        splitted = self.answer.strip().split(text)
        return len(splitted) - 1

class all_students:
    def __init__(self, filename):
        self.students = {}
        self.filename = filename
        self.load_file()

    def load_file(self):
        fh = open(self.filename, 'r')
        lines = fh.readlines()
        fh.close()
        length = len(lines)
        start = 0
        for i in range(0, length):
            if lines[i].startswith("-----End-----"):
                end = i
                student = self.retrieve(lines, start+1, end)
                start = end + 1
                self.students[student.stu] = student

    def retrieve(self, lines, start, end):
        i = start
        stu = lines[i-1].strip().strip("-")
        i+=1
        name = lines[i].strip().split(":")[1].split("-")[0].strip()
        specialization = lines[i].strip().split(":")[1].split("-")[1].replace("(", "").replace(")", "").strip()
        i+=1
        midterm = lines[i].strip().split(':')[1].split(";")[0].strip()
        quiz = lines[i].strip().split(':')[2].split("|")[0].strip()
        year = lines[i].strip().split(':')[3].strip()
        i+=1
        answer = lines[i].strip().split(":")[1].strip()
        d = student(stu, name, specialization, midterm, quiz, year, answer)
        return d
    

#test code student
s=student('02','Amin Amiri','IM','9.9','8.8', 3, 'ytuytutytuytut')
print(s.stu=='02' and s.name=='Amin Amiri' and s.specialization=='IM' and 
    s.midterm=='9.9' and s.quiz=='8.8' and s.year==3 
    and s.answer=='ytuytutytuytut')  #0.2 points
print(s.count_in_answer('tut')==2)  #0.1
print(s.count_in_answer('yt')==4)  #0.1
#test codes all_student
alls=all_students("RQ6.txt")
s1=alls.students['223873']
print(s1.stu=='223873' and s1.name=='Max Verstappen' and s1.specialization=='IM'
        and s1.midterm=='3.3' and s1.quiz=='2.2' and s1.year=='2')
#0.3 points
print(s1.answer=='Etiam suscipit eros leo, eu ornare ipsum molestie et. Nunc non lorem sit amet arcu sollicit udin sodales. Vivamus auctor purus dolor, et convallis orci porttitor at. Praesent quis volutpat massa, eu blandit nibh. Integer fringilla neque quis vehicula auctor. Proin at aliquam turpis, id sodales risus. Curabitur commodo diam ut erat finibus volutpat. Donec in dignissim augue, vel vulputate neque.')
#0.2 points
print(len(alls.students)==10)
#0.1 points