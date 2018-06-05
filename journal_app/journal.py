import os
from os import close


def load(name):
    # todo: populate from file if it exists
    data = []
    file_name=get_full_pathname(name)
    if os.path.exists(file_name):
        with open(file_name, 'r') as fin:
            for entry in fin.readline():
                print()


def save(name, journal_data):
    filename = get_full_pathname(name)
    print("Saving to {}".format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def get_full_pathname(name):
    return os.path.join('.', 'journals', name + ".jrl")


def add_entry(text, journal_data):
    journal_data.append(text)
