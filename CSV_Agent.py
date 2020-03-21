import pandas as pd
import sys


class CSVAgent():

    id_input = int(sys.argv[1])

    """
    Class to manipulate and manage data
    from CSV format files
    """
    def __init__(self, filepath):
        self.csv_file = pd.read_csv(filepath, engine='c')

    def find_record_by_id(self, id_input=id_input):
        try:
            return str(self.csv_file[self.csv_file.id == id_input]).split()[4]
        except KeyError:
            print("Name with id = {} not found".format(id_input))
