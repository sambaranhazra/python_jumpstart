'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
from csv import DictReader, DictWriter
import os


def update_users(old_first, old_last, new_first, new_last):
    update_count = 0
    d = {}
    old_file = "users.csv"
    new_file = "new_users.csv"
    with open(old_file, encoding='utf8') as fin:
        with open('%s' % new_file, mode='w', encoding='utf8', newline='') as fout:
            d = DictReader(fin)
            d_out = DictWriter(fout, fieldnames=d.fieldnames)
            d_out.writeheader()
            for s in d:
                first_name = s[d.fieldnames[0]]
                last_name = s[d.fieldnames[1]]
                if first_name == old_first and last_name == old_last:
                    update_count += 1
                    first_name = new_first
                    last_name = new_last
                d_out.writerow({d.fieldnames[0]: first_name, d.fieldnames[1]: last_name})

    os.remove("%s" % old_file)
    os.rename("%s" % new_file, old_file)
    return update_count


print(update_users('Sambaran', 'Hazra', 'Babai', 'Hazra'))
