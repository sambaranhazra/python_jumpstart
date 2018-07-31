from csv import DictReader

with open('fighters.csv') as r:
    csv_reader = DictReader(r, delimiter='|')
    print(type(csv_reader))
    for fighter in csv_reader:
        print(fighter['Name'])
