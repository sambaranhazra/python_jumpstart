'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johonson
'''
from csv import DictWriter


def add_user(first, last):
    with open('file_copy/users.csv', 'a', newline='') as file:
        csv_writer = DictWriter(file, ["First Name", "Last Name"])
        # csv_writer.writeheader()
        csv_writer.writerow({
            "First Name": first,
            "Last Name": last
        })


add_user('Sambaran', 'Hazra')
add_user('Debangana', 'Hazra')
add_user('Sambaran', 'Hazra')
add_user('Sambaran', 'Hazra')
