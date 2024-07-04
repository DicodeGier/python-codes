class DiskSpace(object):
    def __init__(self, _name, _volume):
        self.name = _name
        self.volume = _volume
        self.__storage = 0
        self.files = []
    
    def __str__(self):
        return "Disk: {}; size: {} GB".format(self.name, self.__storage)

    def store(self, filename, filesize):
        if filesize <= self.volume - self.__storage:
            self.__storage += filesize
            self.files.append([filename, filesize])
            return "file added to disk"
        else:
            raise Exception("Not enough space on disk")

    @property
    def freeSpace(self):
        return self.volume - self.__storage

    def delete(self, filename):
        for n in self.files:
            if n[0] == filename:
                self.files.remove(n)
                self.__storage -= n[1]

    def __iadd__(self, other):
        self.volume += other
        return self



myDisk = DiskSpace("Drive C",500)
print(myDisk.volume==500 and myDisk.name=="Drive C") #0.1 points
print(myDisk._DiskSpace__storage==0) #0.1 points
print(str(myDisk) == "Disk: Drive C; size: 0 GB") #0.2 points
msg=myDisk.store("report.pdf",150)
msg=myDisk.store("exam.py",250)
print(myDisk._DiskSpace__storage==400) #0.1 points
print(myDisk.files==[["report.pdf",150],["exam.py",250]]) #0.2 points
print(msg=="file added to disk") #0.1 points
try:
  myDisk.store("chk.txt",150)
  msg=""
except Exception as ex:
  msg=str(ex)
print(msg=="Not enough space on disk" and myDisk._DiskSpace__storage==400) #0.1 points
print(myDisk.freeSpace==500-150-250) #0.2 points
myDisk.delete("report.pdf")
print(myDisk._DiskSpace__storage==250) #0.1 points
print(myDisk.files==[["exam.py",250]] ) #0.1 points
myDisk+=100
print(myDisk.volume==500+100) #0.2 points


    