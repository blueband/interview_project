import csv

def get_csvDdata(*args):
    with open(args[0], 'r') as data_file:
        data = list(csv.reader(data_file))
    return data