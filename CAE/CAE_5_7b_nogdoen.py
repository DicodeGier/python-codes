import re

file_input = "monty.txt"##input("give the file name ")
fh = open(file_input, 'r')
contents = fh.read()
fh.close()

test_lines = contents.strip().split("\n")
lines = len(contents.strip().split("\n"))
print(lines)
words = [x for x in re.split(r"\n| ", contents) if x != '']
print(len(words))
characters = [x for x in re.split(r"\n| |\w", contents) if x != '']
print(len(characters))
##??

