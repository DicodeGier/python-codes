with open("Customers.txt", 'r') as fh:
    oldContent = fh.read()
    print(oldContent)

A = int(input("give the ID of the customer whose name you want to change "))
B = input("give the new name ")

fh = open("Customers.txt", 'r')
lines = fh.readlines()
fh.close

fh = open("Customers_backup.txt", 'w')
for line in lines:
    parts = line.strip().split("|")
    if parts[0] == str(A):
        parts[2] = str(B) + "\n"
    else:
        parts[2] = parts[2] + "\n"
    fh.write(parts[0] + '|' + parts[1] + '|' + parts[2])
fh.close()

with open("Customers_backup.txt", 'r') as fh:
    s = fh.read()
    print(s)
        
    

