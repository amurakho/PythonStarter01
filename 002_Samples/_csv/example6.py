import csv

csv.QUOTE_ALL

sniffer = csv.Sniffer()
dialect = None

# with open('data/undefined_dialect.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

with open('data/undefined_dialect.csv', 'r') as f:
    content = f.read()
    dialect = sniffer.sniff(content)


with open('data/undefined_dialect.csv', 'r') as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)


n = 10
