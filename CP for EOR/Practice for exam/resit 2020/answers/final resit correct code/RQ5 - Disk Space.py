class DiskSpace(object):
  
  def __init__(self, name, volume):
    self.name = name
    self.volume=volume
    self.__storage = 0
    self.files=[]

  @property
  def freeSpace(self):
    return self.volume - self.__storage 

  def __str__(self):
    return str("Disk: %s; size: %d GB" % (self.name, self.__storage))
    
  def store(self, filename, size):
    if self.__storage + size > self.volume:
      raise Exception("Not enough space on disk")
    self.__storage += size
    self.files.append([filename,size])
    return "file added to disk"
    
  def delete(self, filename):
    for f in self.files:
      if f[0]==filename:
        self.__storage -= f[1]
        self.files.remove(f)
  
  def __iadd__(self,other):
    self.volume+=other
    return self

myDisk = DiskSpace("Drive D",5000)
print(myDisk.volume==5000 and myDisk.name=="Drive D") #0.1 points
print(myDisk._DiskSpace__storage==0) #0.1 points

print(str(myDisk) == "Disk: Drive D; size: 0 GB") #0.2 points

msg=myDisk.store("report1.pdf",1500)
msg=myDisk.store("exam2.py",2500)
print(myDisk._DiskSpace__storage==4000) #0.1 points
print(myDisk.files==[["report1.pdf",1500],["exam2.py",2500]]) #0.2 points
print(msg=="file added to disk") #0.1 points

try:
  myDisk.store("chk.txt",1500)
  msg=""
except Exception as ex:
  msg=str(ex)
print(msg=="Not enough space on disk" and myDisk._DiskSpace__storage==4000) #0.1 points

print(myDisk.freeSpace==5000-1500-2500) #0.2 points

myDisk.delete("report1.pdf")
print(myDisk._DiskSpace__storage==2500) #0.1 points
print(myDisk.files==[["exam2.py",2500]] ) #0.1 points

myDisk+=1000
print(myDisk.volume==5000+1000) #0.2 points