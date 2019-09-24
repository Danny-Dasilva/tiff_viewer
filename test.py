import csv
# import os

# with open('original.csv', newline='') as inp, open('new.csv', 'wb') as out:
#     writer = csv.writer(out)
#     reader = csv.DictReader(inp)
#     for row in reader:
#         if row['Type'] == 'example5': #add var here
#             print(row)

# os.remove('original.csv')
# os.rename('new.csv', 'original.csv')

# lines = list()

# members= "none"
# with open('original.csv', 'r') as readFile:
#     reader = csv.DictReader(readFile)
#     for row in reader:
#         if row['Type'] != 'example5': #add var here
#             lines.append(row)
# print(lines)
# with open('original.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)

lines = list()

members= "example5"

with open('original.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == members:
                lines.remove(row)


with open('mycsv.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)