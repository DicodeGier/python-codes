## exercise 25
fh = open("text-PAH-08-25.txt", 'r')
read = fh.read()
fh.close()

correctRead = read.split()

A = 0
for words in correctRead:
    B = len(words)
    if B>A:
        wordReminder = words
        A = B

print(wordReminder + ' is the longest word')