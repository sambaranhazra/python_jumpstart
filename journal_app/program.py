import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('----------------------')
    print('     JOURNAL APP')
    print('----------------------')


def list_entries(data):
    print('Your Journal Entries')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("Item {} is {}".format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry. Press <enter> to exit')
    journal.add_entry(text, data)


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None
    journal_name = "default"
    journal_data = journal.load(journal_name)
    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip();
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("We don't understand the format")

    journal.save(journal_name, journal_data)
    print('Goodbye')


main()
