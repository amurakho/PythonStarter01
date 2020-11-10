import csv

with open('data/example1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)
