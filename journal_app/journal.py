import os


def load(name):
    """
    Creates and loads journal\n
    :param name: The base name of the journal to load\n
    :return: A new journal data structure
    """
    data = []
    file_name = get_full_pathname(name)

    if os.path.exists(file_name):
        with open(file_name, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


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
