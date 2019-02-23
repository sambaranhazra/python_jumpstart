'''
print_users() # None
# prints to the console:
# Colt Steele
'''
from csv import DictReader


def print_users():
    with open('file_copy/users.csv', 'r') as r:
        csv_data = DictReader(r)
        for row in csv_data:
            print("{} {}".format(row["First Name"], row["Last Name"]))


print_users()
