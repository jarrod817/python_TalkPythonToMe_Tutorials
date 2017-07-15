import Journalfile


def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------------')
    print('        Journal App')
    print('------------------------------')


def run_event_loop():
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = Journalfile.load(journal_name)
    while cmd != 'X' and cmd: #'and cmd' here and in last elif makes it exit the loop if user doesn't enter A L or X
        print('What do you want to do with your journal?')
        cmd = input('[L]ist entries, [A]dd entries, E[X]it journal: ').upper().strip()
        if cmd == "L":
            list_entries(journal_data)
        elif cmd == 'A':
            add_entries(journal_data)
        elif cmd != "X" and cmd:#'and cmd' here and in while loop conditional makes it exit the loop if user doesn't enter A L or X
            print("We don't understand {}, please try again".format(cmd))
    print('Done, goodbye')
    Journalfile.save(journal_name, journal_data)


def list_entries(data):
    entries = reversed(data)
    for (idx, text) in enumerate(entries):
        print('Entry {} -- {}'.format(idx+1, text))


def add_entries(data):
    text = input('Type your entry; <enter> to exit')
    Journalfile.add_entry(text, data)


if __name__ == '__main__':
    main()
