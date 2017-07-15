"""
This is the journal file
"""
import os

def load(name):
    """
    The method creates and loads a new program
    :param name: The base name of journal to load
    :return: a journal data structure populated with file data
    """
    filename = extract_full_pathname(name)
    data = []
    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def extract_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name))#this returns the full file path
    return filename

def save(name, journal_data):
    filename = extract_full_pathname(name)
    print('.... saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)
