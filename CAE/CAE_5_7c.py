fh = open("input.txt", 'r')
contents = fh.read()
fh.close()
print(contents)

my_file = open("output.txt", 'w')
for x in contents.strip().split("\n"):
    my_file.write(x[::-1])
    my_file.write("\n")