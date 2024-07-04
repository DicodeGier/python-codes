import csv
final_list = []

with open('patstat.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            final_list.append([row[0],row[1]])

print(final_list)

