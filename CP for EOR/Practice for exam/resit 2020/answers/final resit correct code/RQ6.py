class student:

    def __init__(self,stu,name,specialization,midterm,quiz,year,answer):
        self.stu,self.name,self.specialization,self.midterm,self.quiz,self.year,self.answer=stu,name,specialization,midterm,quiz,year,answer

    def count_in_answer(self,sequence):
        return self.answer.count(sequence)

#not every 21 lines

class all_students:
    def __init__(self,filename):
        self.students={}
        fh=open(filename)
        lines=fh.readlines()
        start=0
        for idx in range(0,len(lines)):
            if lines[idx].startswith("-----End-----"):
                end=idx
                student=self.retrieve(lines,start+1,end)
                start=end+1
                # self.students.append(student)
                self.students[student.stu]=student

    def retrieve(self,lines,start,end):
        idx=start
        # -----33-----
        stu=lines[idx-1].strip().strip('-')
        # Student: Max Verstappen - IM
        idx+=1
        s=lines[idx].split(':')[1]
        s=s.split('-')
        name=s[0].strip()
        sp=s[1].strip('(').strip()
        specialization=sp.replace('(','').replace(')','')
        # Midterm: 3.3; quiz: 2.2
        idx+=1
        p=lines[idx].split(';')
        midterm=p[0].split(':')[1].strip()
        q=p[1].split('|')
        quiz=q[0].split(':')[1].strip()
        year=q[1].split(':')[1].strip()
        # answer Sequence: ctccacagatttgtgaggtcagctttccctcaccctgaagttaatagctactgacgttag
        idx+=1
        answer=lines[idx].split(':')[1].strip() + "".join(lines[idx+1:end]).replace('\n','')
        d=student(stu,name,specialization,midterm,quiz,year,answer)
        return d

#test code student
s=student('01','Amin','I','9.9','8.8', 3, 'ttttrrryyytrtr')
print(s.stu=='01' and s.name=='Amin' and s.specialization=='I' and 
    s.midterm=='9.9' and s.quiz=='8.8' and s.year==3 
    and s.answer=='ttttrrryyytrtr')  #0.2 points
print(s.count_in_answer('tr')==3)  #0.1
print(s.count_in_answer('t')==6)  #0.1

#test codes all_student
alls=all_students("RQ6.txt")
s1=alls.students['929599']
print(s1.stu=='929599' and s1.name=='Pierre Gasly' and s1.specialization=='ORM'
        and s1.midterm=='1.4' and s1.quiz=='5.2' and s1.year=='2')
#0.3 points

print(s1.answer=='Morbi faucibus id felis in sodales. Phasellus pretium ut quam a consequat. Nullam interdum ornare tincidunt. Sed mollis leo nisl, et gravida leo malesuada non. Sed vehicula a mauris sed porttitor. Proin pellentesque egestas quam sed volutpat. Donec et turpis sit amet ante luctus feugiat. Pellentesque dignissim est at velit sollicitudin dignissim. Quisque porta quis eros a vestibulum. Sed fermentum nec velit eget sodales.')
#0.2 points

print(len(alls.students)==9)
#0.1 points

s10=alls.students['948375']
print(s10.stu=='948375' and s10.name=='Carlos Sainz' and s10.specialization=='IM'
        and s10.midterm=='4.3' and s10.quiz=='2.0' and
        s10.answer=='Duis non magna id tortor egestas porttitor ut at tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eu elit eu diam efficitur lobortis. Sed interdum neque id nisi rhoncus blandit. Nulla a libero auctor, varius mi at, auctor justo. Morbi in augue eu nisl scelerisque tincidunt ac eget justo. Proin a feugiat enim. Donec eget leo sit amet mauris lobortis sagittis.')
#0.2 points



