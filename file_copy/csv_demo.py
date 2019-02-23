from csv import DictReader

with open('file_copy/fighters.csv') as r:
    csv_reader = DictReader(r, delimiter='|')
    print(type(csv_reader))
    for fighter in csv_reader:
        print(fighter['Name'])
